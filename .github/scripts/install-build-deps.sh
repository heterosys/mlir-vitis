##===- install-build-deps.sh - GitHub CI scripts -----------------*- sh -*-===//
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau.
##
##===----------------------------------------------------------------------===//
#!/bin/sh
set -e

sudo apt-get update
sudo apt-get purge -y libgcc-*-dev || true
sudo apt-get install -y build-essential python3-pip
sudo apt-get autoremove -y

sudo -H python3 -m pip install --upgrade pip==20.3.4
sudo -H python3 -m pip install cmake
sudo -H python3 -m pip install ninja
sudo -H python3 -m pip install lit
sudo -H python3 -m pip install psutil
