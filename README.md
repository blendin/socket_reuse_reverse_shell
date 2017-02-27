# Small proof of concept for findpeer.sh socket reuse shells
Used when bindshells and reverse shells won't work.

Proof of concept of client and payloads for reusing TCP sockets as shells. Motivated by shellcode used to do the same thing (see shellcraft findpeersh or metasploit findpeersh). Unrestricted upload attempt found [here](http://pentestmonkey.net/tools/web-shells/php-findsock-shell).

## Usage
Attacker Side  
`poc.py http://victim.org:8080 ports/findpeer.sh`  

Victim  
`victim/victim.py`

## Idea
Reuse the TCP socket used to send exploit for our shell [shell example for finding file descriptor](ports/findpeer.sh)

## License
MIT
