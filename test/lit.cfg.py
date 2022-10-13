##===- lit.cfg.py - lit configuration ------------------------*- python -*-===//
##
## Adapted from llvm/circt/test/lit.cfg.py
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau
##
##===----------------------------------------------------------------------===//

import os
import platform
import re
import shutil
import subprocess
import tempfile

import lit.formats
import lit.util

from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst
from lit.llvm.subst import FindTool

# Configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = 'Vitis'

config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

# suffixes: A list of file extensions to treat as test files.
config.suffixes = ['.mlir', '.ll', '.sh']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.join(config.vitis_obj_root, 'test')

config.substitutions.append(('%PATH%', config.environment['PATH']))
config.substitutions.append(('%shlibext', config.llvm_shlib_ext))
config.substitutions.append(('%shlibdir', config.vitis_shlib_dir))

config.substitutions.append(('vitis-to-mlir', os.path.join(
    config.vitis_python_packages_dir, 'mlir-vitis', 'vitis-to-mlir', 'main.py')))
config.substitutions.append(('mlir-to-vitis', os.path.join(
    config.vitis_python_packages_dir, 'mlir-vitis', 'mlir-to-vitis', 'main.py')))

llvm_config.with_system_environment(['HOME', 'INCLUDE', 'LIB', 'TMP', 'TEMP'])

llvm_config.use_default_substitutions()

# excludes: A list of directories to exclude from the testsuite. The 'Inputs'
# subdirectories contain auxiliary inputs for various tests in their parent
# directories.
config.excludes = ['Inputs', 'CMakeLists.txt', 'README.txt', 'LICENSE.txt']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.join(config.vitis_obj_root, 'test')

# Tweak the PATH to include the tools dir.
llvm_config.with_environment('PATH', config.vitis_tools_dir, append_path=True)
llvm_config.with_environment('PATH', config.mlir_tools_dir, append_path=True)
llvm_config.with_environment('PATH', config.llvm_tools_dir, append_path=True)

tool_dirs = [config.vitis_tools_dir, config.mlir_tools_dir, config.llvm_tools_dir]
tools = ['vitis-translate', 'FileCheck', 'not', 'count']

llvm_config.add_tool_substitutions(tools, tool_dirs)
