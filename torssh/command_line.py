#!/usr/bin/env python

import os
import sys
import signal

from shutil import which

import stem.process

from stem.util import term

SOCKS_PORT = 7070

# Start an instance of Tor and proxies the ssh client via torsocks
# Note that this likely will not work if you have another Tor instance running.

def print_bootstrap_lines(line):
  """This prints Tor's bootstrap information as it starts"""
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


def start_tor_process():
  print(term.format("\nStarting Tor:\n", term.Attr.BOLD, term.Color.BLUE))
  tor_process = stem.process.launch_tor_with_config(
    config = {
      'SocksPort': str(SOCKS_PORT),
#     'ExitNodes': '{ru}',
    },
    init_msg_handler = print_bootstrap_lines,
  )
  return tor_process


def close_tor_process(tor_process):
  if tor_process:
      tor_process.kill()
      print(term.format("\nTor Service Stopped Correctly\n", term.Attr.BOLD, term.Color.BLUE))


def main():
  for x in ['tor', 'torsocks']:
    if which(x) is None:
      print(term.format('\nPlease install {}\n'.format(x), term.Attr.BOLD, term.Color.RED))
      exit()

  args = " ".join(sys.argv[1:])
  tor_process = None

  def interrupt_handler(signal, frame):
    close_tor_process(tor_process)

  signal.signal(signal.SIGHUP, interrupt_handler)
  signal.signal(signal.SIGTERM, interrupt_handler)

  try:
    tor_process = start_tor_process()
    os.system('torsocks -P {} ssh {}'.format(str(SOCKS_PORT), args))
  finally:
    close_tor_process(tor_process) # stops tor background process


if __name__ == "__main__":
  main()