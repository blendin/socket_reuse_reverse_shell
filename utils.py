#!/usr/bin/env python

import telnetlib

def ip2hex(ip):
  """
  Convert a normal ip address `127.0.0.1` to /proc/net/tcp format
  """
  
  pass


def port2hex(port):
  """
  Convert a normal port '8080' to /proc/net/tcp format
  """
  return hex(int(port))[2:].upper()


def interact(s):
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()
