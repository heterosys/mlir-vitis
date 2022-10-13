// RUN: vitis-translate --mlir-to-llvmir %s | FileCheck %s

module {
// CHECK: define void @kernel1() #0
  llvm.func @kernel1() attributes {llvm.noinline} {
    llvm.return
  }

// CHECK: define void @kernel0() #1
  llvm.func @kernel0() attributes {llvm.alwaysinline} {
    llvm.return
  }
}

// CHECK: attributes #0 = { noinline }
// CHECK: attributes #1 = { alwaysinline }