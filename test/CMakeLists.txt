##===- CMakeLists.txt - LIT Testing ---------------------------*- cmake -*-===//
##
## Configure the MLIR-Vitis tests.
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau
##
##===----------------------------------------------------------------------===//

configure_lit_site_cfg(
  ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
  ${CMAKE_CURRENT_BINARY_DIR}/lit.site.cfg.py
  MAIN_CONFIG
  ${CMAKE_CURRENT_SOURCE_DIR}/lit.cfg.py
)

set(VITIS_TEST_DEPENDS
  FileCheck count not
  vitis-translate
  MlirVitisTools
)

add_lit_testsuite(check-vitis
  "Running the MLIR-Vitis regression tests"
  ${CMAKE_CURRENT_BINARY_DIR}
  DEPENDS ${VITIS_TEST_DEPENDS}
)
set_target_properties(check-vitis PROPERTIES FOLDER "Tests")

add_lit_testsuites(VITIS
  ${CMAKE_CURRENT_SOURCE_DIR}
  DEPENDS ${VITIS_TEST_DEPS}
)
