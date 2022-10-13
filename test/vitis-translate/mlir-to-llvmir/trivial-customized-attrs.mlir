// RUN: vitis-translate --mlir-to-llvmir %s | FileCheck %s

module {
  // CHECK: define void @kernel0() #0
  llvm.func @kernel0() attributes {llvm.string.fpga.demangled.name = "kernel0", llvm.string.fpga.top.func = "kernel0"} {
    llvm.return
  }
}

// CHECK: attributes #0 = { "fpga.demangled.name"="kernel0" "fpga.top.func"="kernel0" }