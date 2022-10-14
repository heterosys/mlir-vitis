#!/usr/bin/env python3
##===- main.py --------------------------------------=--------*- python -*-===//
##
## The main file converting a Vitis HLS LLVM to MLIR.
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau.
##
##===----------------------------------------------------------------------===//

import click
import re
import sys
from subprocess import Popen, PIPE, STDOUT


@click.command()
@click.option('--verbose',
              '-v',
              default=0,
              count=True,
              help='Increase logging verbosity.')
@click.argument('file', type=click.File('r'))
def entry_point(verbose, file):
  # Read the input file
  llvm = file.read()

  # Santizing the old-fashion LLVM input to be compatible.
  # (1) `sret` should have the structure type as its argument.
  llvm = re.sub(r'(%.*)\*([^%]*)sret ', r'\1*\2sret(\1) ', llvm)
  # (2) !DISubprogram does not have variables
  llvm = re.sub(r', variables: ![0-9]*', r'', llvm)

  # Convert to MLIR LLVM Dialect
  p = Popen(['vitis-translate', '--import-llvm'],
            stdout=PIPE,
            stdin=PIPE,
            stderr=PIPE)

  mlir, err = p.communicate(input=llvm.encode())

  # Print out MLIR code
  if p.returncode == 0:
    print(mlir.decode())

  if verbose or p.returncode != 0:
    # Debug information
    print(err.decode(), file=sys.stderr)


if __name__ == '__main__':
  entry_point()
