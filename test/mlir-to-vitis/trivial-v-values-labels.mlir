// RUN: mlir-to-vitis %s | FileCheck %s

module {
  // CHECK: define float @kernel0(float %v0, float %v1)
  // CHECK: v2:
  // CHECK:   %v3 =
  llvm.func @kernel0(%0 : f32, %1 : f32) -> f32 {
    %2 = llvm.fadd %0, %1  : f32
    llvm.return %2 : f32
  }
}