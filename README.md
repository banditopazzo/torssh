# Torssh
Torssh is a simple utility to connect to SSH services exposed (and to copy file via SCP) over the Tor network.  
The behaviour is simple: it launches a background tor service and proxies the ssh/scp connection to it.

Usage
---
The usage is identical to the normal SSH or SCP utility.  

Log in to a remote host:

    torssh username@address.onion

Copy the file "foobar.txt" from a remote host to the local host:

    torscp username@address.onion:/some/remote/directory foobar.txt

Copy the file "foobar.txt" from the local host to a remote host:

    torscp foobar.txt username@address.onion:/some/remote/directory

And so on...

Installation
---
To install torssh you just need to clone it from git and install it using pip:

      git clone https://github.com/banditopazzo/torssh.git

      cd torssh
      
      pip install .

Pre-requisites
---
* To install torssh you need to have `python` and `pip` installed on your system.
    - python: https://www.python.org/downloads/
    - pip: https://pip.pypa.io/en/stable/installing/

* To use torssh you need to have `tor` installed on your system. Please refer to official guide or guide for your distribution for the installation.

Disclaimer
---
* This is version 0.1 of the software, so I expect some bugs to be present

* This tool has been tested only on a Arch Linux laptop

Therefore, if this tool is not working for you, I apologise and I will try to fix it.

Any suggestions and comments are welcome!
