#!/usr/bin/env python

import sys
import torssh

# TODO
def parse_args():
  return " ".join(sys.argv[1:]) 

def ssh():
  torssh.tor_wrap('ssh', parse_args())
  
def scp():
  torssh.tor_wrap('scp', parse_args())