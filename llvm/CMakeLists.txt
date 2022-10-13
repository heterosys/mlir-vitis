##===- CMakeLists.txt - CMake llvm targets --------------------*- cmake -*-===//
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

include(FetchContent)
FetchContent_Declare(
  llvm
  URL "https://github.com/heterosys/llvm-nightly/archive/refs/tags/snapshot-20220926.tar.gz"
  PATCH_COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/llvm/include/llvm/IR/CMakeLists.txt llvm/include/llvm/IR/CMakeLists.txt
  COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/llvm/include/llvm/IR/Intrinsics.td llvm/include/llvm/IR/Intrinsics.td
  COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/llvm/include/llvm/IR/IntrinsicsFPGA.td llvm/include/llvm/IR/IntrinsicsFPGA.td
  COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/llvm/include/llvm/IR/IntrinsicsSPIR.td llvm/include/llvm/IR/IntrinsicsSPIR.td
  COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/llvm/lib/IR/Verifier.cpp llvm/lib/IR/Verifier.cpp
  COMMAND
  ln -sf ${CMAKE_CURRENT_LIST_DIR}/mlir/include/mlir/Dialect/LLVMIR/LLVMIntrinsicOps.td mlir/include/mlir/Dialect/LLVMIR/LLVMIntrinsicOps.td
)

FetchContent_GetProperties(llvm)
if(NOT llvm_POPULATED)
  FetchContent_Populate(llvm)
  set(CMAKE_BUILD_TYPE Release)
  set(CMAKE_CXX_STANDARD 17)

  # Disable unnecessary components to speed up build and reduce binary size.
  set(CLANG_ANALYZER_ENABLE_Z3_SOLVER OFF CACHE BOOL "" FORCE)
  set(CLANG_BUILD_TOOLS OFF CACHE BOOL "" FORCE)
  set(CLANG_ENABLE_ARCMT OFF CACHE BOOL "" FORCE)
  set(CLANG_ENABLE_STATIC_ANALYZER OFF CACHE BOOL "" FORCE)
  set(LLVM_APPEND_VC_REV OFF CACHE BOOL "" FORCE)
  set(LLVM_ENABLE_BINDINGS OFF CACHE BOOL "" FORCE)
  set(LLVM_ENABLE_LIBXML2 OFF CACHE BOOL "" FORCE)
  set(LLVM_ENABLE_PROJECTS "mlir" CACHE STRING "" FORCE)
  set(LLVM_INCLUDE_BENCHMARKS OFF CACHE BOOL "" FORCE)
  set(LLVM_INCLUDE_EXAMPLES OFF CACHE BOOL "" FORCE)
  set(LLVM_INCLUDE_TESTS OFF CACHE BOOL "" FORCE)
  set(LLVM_INCLUDE_TOOLS ON CACHE BOOL "" FORCE)
  set(LLVM_TARGETS_TO_BUILD X86 CACHE STRING "" FORCE)

  add_subdirectory(${llvm_SOURCE_DIR}/llvm ${llvm_BINARY_DIR}
                    EXCLUDE_FROM_ALL)

  set(MLIR_SOURCE_DIR ${llvm_SOURCE_DIR}/mlir PARENT_SCOPE)
  set(LLVM_SOURCE_DIR ${llvm_SOURCE_DIR}/llvm PARENT_SCOPE)
  set(LLVM_TOOLS_DIR ${llvm_BINARY_DIR}/bin PARENT_SCOPE)
  set(MLIR_TOOLS_DIR ${llvm_BINARY_DIR}/bin PARENT_SCOPE)
  set(LLVM_INCLUDE_DIRS
      ${llvm_SOURCE_DIR}/llvm/include ${llvm_BINARY_DIR}/include
      PARENT_SCOPE)
  set(MLIR_INCLUDE_DIRS
      ${llvm_SOURCE_DIR}/mlir/include ${llvm_BINARY_DIR}/mlir/include
      PARENT_SCOPE)
      set(MLIR_BINARY_DIR ${llvm_BINARY_DIR}/bin PARENT_SCOPE)
  set(LLVM_BINARY_DIR ${llvm_BINARY_DIR} PARENT_SCOPE)
endif()