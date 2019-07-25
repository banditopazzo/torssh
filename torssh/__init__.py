import os
import signal
import stem.process
from shutil import which
from stem.util import term

# Start an instance of Tor and proxies the ssh client via torsocks
# Note that this likely will not work if you have another Tor instance running.

def check_tor_installation():
  for x in ['tor', 'torsocks']:
    if which(x) is None:
      print(term.format('\nPlease install {}\n'.format(x), term.Attr.BOLD, term.Color.RED))
      exit()

def print_bootstrap_lines(line):
  """This prints Tor's bootstrap information as it starts"""
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


def start_tor_process(socks_port):
  print(term.format("\nStarting Tor:\n", term.Attr.BOLD, term.Color.BLUE))
  tor_process = stem.process.launch_tor_with_config(
    config = {
      'SocksPort': str(socks_port),
#     'ExitNodes': '{ru}',
    },
    init_msg_handler = print_bootstrap_lines,
  )
  return tor_process


def close_tor_process(tor_process):
  if tor_process:
      tor_process.kill()
      print(term.format("\nTor Service Stopped Correctly\n", term.Attr.BOLD, term.Color.BLUE))


def tor_wrap(cmd, args, socks_port = 9050):
  check_tor_installation()
  tor_process = None

  def interrupt_handler(signal, frame):
    close_tor_process(tor_process)

  signal.signal(signal.SIGHUP, interrupt_handler)
  signal.signal(signal.SIGTERM, interrupt_handler)

  try:
    tor_process = start_tor_process(socks_port)
    os.system(f'torsocks -P {socks_port} {cmd} {args}')
  finally:
    close_tor_process(tor_process) # stops tor background process