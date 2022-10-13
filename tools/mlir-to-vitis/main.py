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


@click.command()
@click.option('--verbose',
              '-v',
              default=0,
              count=True,
              help='Increase logging verbosity.')
@click.argument('file', type=click.File('r'))
def entry_point(verbose, file):
  # Read the input file
  content = file.read()


if __name__ == '__main__':
  entry_point()
