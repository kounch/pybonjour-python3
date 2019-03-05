#!/usr/bin/env python

# This file is licensed under the terms of the MIT License.
# See the LICENSE file in the root of this repository for complete details.

from __future__ import with_statement

import sys
import os
from setuptools import setup

import pybonjour

base_dir = os.path.dirname(__file__)

pybonjour_classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Topic :: System :: Distributed Computing",
    "Topic :: System :: Networking",
]

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name="pybonjour",
    version=pybonjour.__version__,
    description=("pybonjour provides a pure-Python interface (via ctypes) to "
               " Apple Bonjour and compatible DNS-SD libraries (like Avahi)."),
    long_description=long_description,
    license="MIT License",
    url="http://o2s.csail.mit.edu/o2s-wiki/pybonjour",
    py_modules=["pybonjour"],
    author="Christopher J. Stawarz",
    author_email="cstawarz@csail.mit.edu",
    classifiers=pybonjour_classifiers,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
)
