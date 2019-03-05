# pybonjour

Pure-Python interface to Apple Bonjour.

Author: [Christopher Stawarz](cstawarz@csail.mit.edu)
Author: [Wim Haanstra](wim@wim.me)
Author: [Timoteus Ruotsalainen](timoteus.ruotsalainen@iki.fi)
Version: 1.1.2
October 5, 2017

----------------------------------------------------

## Introduction

This is based on the fork of Timoteus Ruotsalainen fork from [https://github.com/depl0y/pybonjour-python3](https://github.com/depl0y/pybonjour-python3) who forked the code from [https://code.google.com/archive/p/pybonjour/](https://code.google.com/archive/p/pybonjour/)

[Ryan McGuire](https://github.com/EnigmaCurry) made some updates regarding python3 in 2013 and I have added some more fixes for it to work with python3.

pybonjour provides a pure-Python interface (via ctypes) to Apple Bonjour and compatible DNS-SD libraries (such as Avahi).  It allows Python scripts to take advantage of Zero Configuration Networking (Zeroconf) to register, discover, and resolve services on both local and wide-area networks.  Since pybonjour is implemented in pure Python, scripts that use it can easily be ported to Mac OS X, Windows, Linux, and other systems that run Bonjour.

pybonjour is free software, distributed under the MIT license.

## Requirements

pybonjour requires Python 2.7 or later. It also depends on ctypes (version 1.0.1 or later), which is part of the standard library in Python 2.5 and later.

No additional software is required to use pybonjour under Mac OS X. To use it under Windows, the Bonjour for Windows package must be installed on your system. Most Linux systems use Avahi rather than Bonjour for DNS-SD. If this is the case on your system, you'll need to install Avahi's Bonjour compatibility library. (Under Ubuntu, the package to install is libavahi-compat-libdnssd1.) Otherwise, or to use pybonjour under other POSIX systems, you must download, compile, and install Bonjour from source.
