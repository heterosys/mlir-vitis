##===- CMakeLists.txt - CMake library targets -----------------*- cmake -*-===//
##
## Adapted from llvm/circt/cmake/modules/CMakeLists.txt
## Generate a list of CMake library targets so that other CMake projects can
## link against them.
##
## This file is licensed under the Apache License v2.0 with LLVM Exceptions.
## See https://llvm.org/LICENSE.txt for license information.
## SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
##
## Copyright (C) 2022, Jason Lau.
##
##===----------------------------------------------------------------------===//

set(VITIS_INSTALL_PACKAGE_DIR lib${LLVM_LIBDIR_SUFFIX}/cmake/vitis)
set(vitis_cmake_builddir "${CMAKE_BINARY_DIR}/${VITIS_INSTALL_PACKAGE_DIR}")

# Keep this in sync with mlir/cmake/CMakeLists.txt!
set(MLIR_INSTALL_PACKAGE_DIR lib${LLVM_LIBDIR_SUFFIX}/cmake/mlir)
set(mlir_cmake_builddir "${MLIR_BINARY_DIR}/${MLIR_INSTALL_PACKAGE_DIR}")

# Keep this in sync with llvm/cmake/CMakeLists.txt!
set(LLVM_INSTALL_PACKAGE_DIR lib${LLVM_LIBDIR_SUFFIX}/cmake/llvm)
set(llvm_cmake_builddir "${LLVM_BINARY_DIR}/${LLVM_INSTALL_PACKAGE_DIR}")

# Generate a list of CMake library targets so that other CMake projects can
# link against them. LLVM calls its version of this file LLVMExports.cmake, but
# the usual CMake convention seems to be ${Project}Targets.cmake.
get_property(VITIS_EXPORTS GLOBAL PROPERTY VITIS_EXPORTS)
export(TARGETS ${VITIS_EXPORTS} FILE ${vitis_cmake_builddir}/VitisTargets.cmake)

get_property(VITIS_ALL_LIBS GLOBAL PROPERTY VITIS_ALL_LIBS)
get_property(VITIS_DIALECT_LIBS GLOBAL PROPERTY VITIS_DIALECT_LIBS)
get_property(VITIS_CONVERSION_LIBS GLOBAL PROPERTY VITIS_CONVERSION_LIBS)
get_property(VITIS_TRANSLATION_LIBS GLOBAL PROPERTY VITIS_TRANSLATION_LIBS)
get_property(VITIS_ANALYSIS_LIBS GLOBAL PROPERTY VITIS_ANALYSIS_LIBS)

# Generate VITISConfig.cmake for the build tree.
set(VITIS_CONFIG_CMAKE_DIR "${vitis_cmake_builddir}")
set(VITIS_CONFIG_LLVM_CMAKE_DIR "${llvm_cmake_builddir}")
set(VITIS_CONFIG_MLIR_CMAKE_DIR "${mlir_cmake_builddir}")
set(VITIS_CONFIG_LIBRARY_DIRS "${VITIS_LIBRARY_DIR}")
set(VITIS_CONFIG_BINARY_DIR "${VITIS_BINARY_DIR}")
set(VITIS_CONFIG_TOOLS_DIR "${VITIS_TOOLS_DIR}")
set(VITIS_CONFIG_INCLUDE_EXPORTS "include(\"\${VITIS_CMAKE_DIR}/VitisTargets.cmake\")")
set(VITIS_CONFIG_INCLUDE_DIRS
  "${VITIS_SOURCE_DIR}/include"
  "${VITIS_BINARY_DIR}/include"
)
configure_file(
  ${CMAKE_CURRENT_SOURCE_DIR}/VitisConfig.cmake.in
  ${vitis_cmake_builddir}/VitisConfig.cmake
  @ONLY
)
set(VITIS_CONFIG_CMAKE_DIR)
set(VITIS_CONFIG_LLVM_CMAKE_DIR)
set(VITIS_CONFIG_MLIR_CMAKE_DIR)
set(VITIS_CONFIG_LIBRARY_DIRS)
set(VITIS_CONFIG_BINARY_DIR)
set(VITIS_CONFIG_TOOLS_DIR)
set(VITIS_CONFIG_INCLUDE_EXPORTS)
set(VITIS_CONFIG_INCLUDE_DIRS)

# Generate VitisConfig.cmake for the install tree.
set(VITIS_CONFIG_CODE "
# Compute the installation prefix from this VitisConfig.cmake file location.
get_filename_component(VITIS_INSTALL_PREFIX \"\${CMAKE_CURRENT_LIST_FILE}\" PATH)")
# Construct the proper number of get_filename_component(... PATH)
# calls to compute the installation prefix.
string(REGEX REPLACE "/" ";" _count "${VITIS_INSTALL_PACKAGE_DIR}")
foreach(p ${_count})
  set(VITIS_CONFIG_CODE "${VITIS_CONFIG_CODE}
get_filename_component(VITIS_INSTALL_PREFIX \"\${VITIS_INSTALL_PREFIX}\" PATH)")
endforeach(p)
set(VITIS_CONFIG_CMAKE_DIR "\${VITIS_INSTALL_PREFIX}/${VITIS_INSTALL_PACKAGE_DIR}")
set(VITIS_CONFIG_LLVM_CMAKE_DIR "\${VITIS_INSTALL_PREFIX}/${LLVM_INSTALL_PACKAGE_DIR}")
set(VITIS_CONFIG_MLIR_CMAKE_DIR "\${VITIS_INSTALL_PREFIX}/${MLIR_INSTALL_PACKAGE_DIR}")
set(VITIS_CONFIG_LIBRARY_DIRS "\${VITIS_INSTALL_PREFIX}/lib")
set(VITIS_CONFIG_BINARY_DIR "\${VITIS_INSTALL_PREFIX}")
set(VITIS_CONFIG_TOOLS_DIR "\${VITIS_INSTALL_PREFIX}/bin")
set(VITIS_CONFIG_INCLUDE_EXPORTS "include(\"\${VITIS_CMAKE_DIR}/VitisTargets.cmake\")")
set(VITIS_CONFIG_INCLUDE_DIRS
  "\${VITIS_INSTALL_PREFIX}/include"
)
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/VitisConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/VitisConfig.cmake
    @ONLY
)
set(VITIS_CONFIG_CODE)
set(VITIS_CONFIG_CMAKE_DIR)
set(VITIS_CONFIG_LLVM_CMAKE_DIR)
set(VITIS_CONFIG_MLIR_CMAKE_DIR)
set(VITIS_CONFIG_LIBRARY_DIRS)
set(VITIS_CONFIG_BINARY_DIR)
set(VITIS_CONFIG_TOOLS_DIR)
set(VITIS_CONFIG_INCLUDE_EXPORTS)
set(VITIS_CONFIG_INCLUDE_DIRS)

if(NOT LLVM_INSTALL_TOOLCHAIN_ONLY)
  # Not TOOLCHAIN ONLY, so install the Vitis parts as well
  # Include the cmake files so other tools can use vitis-tblgen, etc.
  install(EXPORT VitisTargets DESTINATION ${VITIS_INSTALL_PACKAGE_DIR}
          COMPONENT vitis-cmake-exports)

  install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/VitisConfig.cmake
    ${CMAKE_CURRENT_SOURCE_DIR}/AddVitis.cmake
    DESTINATION ${VITIS_INSTALL_PACKAGE_DIR}
    COMPONENT vitis-cmake-exports)

  if(NOT LLVM_ENABLE_IDE)
    # Add a dummy target so this can be used with LLVM_DISTRIBUTION_COMPONENTS
    add_custom_target(vitis-cmake-exports)
    add_llvm_install_targets(install-vitis-cmake-exports
                             COMPONENT vitis-cmake-exports)
  endif()
endif()
