##===- CMakeLists.txt - MLIR-Vitis cmake root -----------------*- cmake -*-===//
##
## Configure the MLIR-Vitis build.
## Adapted from llvm/circt/CMakeLists.txt
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau.
##
##===----------------------------------------------------------------------===//

cmake_minimum_required(VERSION 3.13.4)

if(POLICY CMP0068)
  cmake_policy(SET CMP0068 NEW)
  set(CMAKE_BUILD_WITH_INSTALL_NAME_DIR ON)
endif()

if(POLICY CMP0075)
  cmake_policy(SET CMP0075 NEW)
endif()

if(POLICY CMP0077)
  cmake_policy(SET CMP0077 NEW)
endif()

# CMP0116: Ninja generators transform `DEPFILE`s from `add_custom_command()`
# New in CMake 3.20. https://cmake.org/cmake/help/latest/policy/CMP0116.html
if(POLICY CMP0116)
  cmake_policy(SET CMP0116 OLD)
endif()

if(POLICY CMP0135)
  cmake_policy(SET CMP0135 NEW)
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

# Build custom version of LLVM
add_subdirectory(llvm)

#-------------------------------------------------------------------------------
# Project setup and globals
#-------------------------------------------------------------------------------
project(Vitis LANGUAGES CXX C)

message(STATUS "Using LLVMConfig.cmake in: ${LLVM_SOURCE_DIR}")
message(STATUS "Using MLIRConfig.cmake in: ${MLIR_SOURCE_DIR}")
list(APPEND CMAKE_MODULE_PATH "${LLVM_SOURCE_DIR}/cmake/modules")
list(APPEND CMAKE_MODULE_PATH "${MLIR_SOURCE_DIR}/cmake/modules")
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake/modules")

#-------------------------------------------------------------------------------
# Options and settings
#-------------------------------------------------------------------------------
option(LLVM_INCLUDE_TOOLS "Generate build targets for the LLVM tools." ON)
option(LLVM_BUILD_TOOLS "Build the LLVM tools. If OFF, just generate build targets." ON)

if(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHs-c- /GR-")
else()
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-exceptions -fno-rtti")
endif()

# Enable address sanitizer in santize mode
if (CMAKE_BUILD_TYPE STREQUAL "Sanitize")
  add_compile_options(-fsanitize=address)
  add_link_options(-fsanitize=address)
endif()

#-------------------------------------------------------------------------------
# MLIR/LLVM Configuration
#-------------------------------------------------------------------------------

include(TableGen)
include(AddLLVM)
include(AddMLIR)
include(AddMLIRPython)
include(HandleLLVMOptions)
include(AddVitis)

# Add MLIR and LLVM headers to the include path
include_directories(${LLVM_INCLUDE_DIRS})
include_directories(${MLIR_INCLUDE_DIRS})

#-------------------------------------------------------------------------------
# MLIR-Vitis configuration
#-------------------------------------------------------------------------------

set(VITIS_MAIN_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR} ) # --src-root
set(VITIS_MAIN_INCLUDE_DIR ${VITIS_MAIN_SRC_DIR}/include)

set(VITIS_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(VITIS_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})
set(VITIS_INCLUDE_DIR ${CMAKE_CURRENT_BINARY_DIR}/include)
set(VITIS_LIBRARY_DIR ${CMAKE_BINARY_DIR}/lib)
set(VITIS_TOOLS_DIR ${CMAKE_BINARY_DIR}/bin)
set(VITIS_UTILS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/utils)
set(VITIS_PYTHON_PACKAGES_DIR ${VITIS_BINARY_DIR}/python_packages)

# Add MLIR-Vitis files to the include path
include_directories(${VITIS_INCLUDE_DIR})

#-------------------------------------------------------------------------------
# Directory setup
#-------------------------------------------------------------------------------

add_subdirectory(tools)
add_subdirectory(test)
