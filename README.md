# MLIR-based Vitis HLS LLVM Bridge
📥 🎯 MLIR toolchain to import and export Vitis HLS LLVM (.ll) files.

![](https://mlir.llvm.org//mlir-logo.png)

**WARNING:** This is a work-in-progress and will be actively changed.

This repository contains an [MLIR-based](https://mlir.llvm.org/) toolchain that bridges Vitis HLS LLVM (.ll) files with MLIR workflow.  It imports LLVM source code into the MLIR LLVM dialect and allows the generation of Vitis HLS-compatible LLVM outputs from the MLIR LLVM dialect.  As a future work, it will raise the Vitis HLS pragmas and intrinsics into high level dialects.

## How to Build

### 0. Clone MLIR-Vitis and install prerequisites

```
git clone https://github.com/heterosys/mlir-vitis.git
cd mlir-vitis

sudo apt-get install -y build-essential python3-pip
pip3 install cmake ninja psutil
```

### 1. Build MLIR-Vitis

```sh
cmake -S . -B build \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_MAKE_PROGRAM=ninja -G Ninja
cmake --build build --target all
```

This will build a modified version of LLVM.

To test MLIR-Vitis:

```sh
cmake --build build --target check-vitis
```

Cheers! 🍺

---

Copyright (c) 2022 Jason Lau
