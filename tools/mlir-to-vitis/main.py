#!/usr/bin/env python3
##===- main.py --------------------------------------=--------*- python -*-===//
##
## The main file converting an MLIR program to Vitis HLS compatible LLVM.
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
  mlir = file.read()

  # Convert to MLIR LLVM Dialect
  p = Popen(['vitis-translate', '--mlir-to-llvmir', '-opaque-pointers=0'],
            stdout=PIPE,
            stdin=PIPE,
            stderr=PIPE)

  llvm, err = p.communicate(input=mlir.encode())

  # Print out MLIR code
  if p.returncode == 0:
    llvm = santize_llvm(llvm.decode())
    print(llvm)

  if verbose or p.returncode != 0:
    # Debug information
    print(err.decode(), file=sys.stderr)


def santize_llvm(llvm: str) -> str:
  # Santizing the new-fashion LLVM output to be HLS compatible.

  # (1) implicit entry label was not supported.
  llvm = add_entry_label(llvm)

  # (2) values must be sequential or starts with alphabet.
  llvm = re.sub(r'%([0-9][0-9]*)([^0-9])', r'%v\1\2', llvm)

  # (3) labels are values as well.
  llvm = re.sub(r'\n([0-9][0-9]*):', r'\nv\1:', llvm)

  # (4) immarg is new.
  llvm = re.sub(r' immarg,', r',', llvm)

  # (5) remove new attributes.
  llvm = re.sub(r' nocallback ', r' ', llvm)
  llvm = re.sub(r' nofree ', r' ', llvm)
  llvm = re.sub(r' nosync ', r' ', llvm)
  llvm = re.sub(r' willreturn ', r' ', llvm)

  # (6) remove unsupported fields in DISubprogram
  llvm = re.sub(r', spFlags:[^,)]*', r'', llvm)
  llvm = re.sub(r', retainedNodes:[^,)]*', r'', llvm)

  # (7) remove debug information as they may fail Vitis's analysis passes
  llvm = re.sub(r', !dbg ![0-9]*', r'', llvm)
  llvm = re.sub(r'!dbg ![0-9]*', r'', llvm)

  # (8) TODO: temporary workaround:
  # sideeffect function call must have a body which is not emitted now.
  llvm = re.sub(r'call void @llvm.sideeffect\(\)', r'', llvm)

  return llvm


def add_entry_label(llvm: str) -> str:
  lines = llvm.split('\n')

  # Look for function definition
  for i, line in enumerate(lines):

    # Skips non definitions
    if not line.startswith('define '):
      continue

    # Look for the last parameter value
    value = re.findall(r"%([0-9][0-9]*)[^%]*$", line)

    lines[i] += '\nv' + str(int(value[-1]) + 1) + ':'

  return '\n'.join(lines)


if __name__ == '__main__':
  entry_point()
