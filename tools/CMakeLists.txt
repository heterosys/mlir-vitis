##===- CMakeLists.txt - CMake tools targets -------------------*- cmake -*-===//
##
## Adapted from UCLA-VAST/tapa/backend/CMakeLists.txt
## Build a customized LLVM version so that it could support HLS LLVM
## input/output.
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau.
##
##===----------------------------------------------------------------------===//

add_custom_target(
  vitis-translate
  ALL
  DEPENDS mlir-translate
  COMMAND
    ${CMAKE_COMMAND} -E copy_if_different ${MLIR_TOOLS_DIR}/mlir-translate
    ${VITIS_TOOLS_DIR}/vitis-translate
)

declare_mlir_python_sources(MlirVitisToolsSources
  ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}"
  SOURCES
  mlir-to-vitis/__init__.py
  mlir-to-vitis/main.py
  vitis-to-mlir/__init__.py
  vitis-to-mlir/main.py
)

add_mlir_python_modules(MlirVitisTools
  ROOT_PREFIX "${VITIS_PYTHON_PACKAGES_DIR}/mlir-vitis"
  INSTALL_PREFIX "python_packages/mlir-vitis"
  DECLARED_SOURCES
  MlirVitisToolsSources
)
