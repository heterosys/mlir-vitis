// RUN: vitis-translate --mlir-to-llvmir -opaque-pointers=0 %s | FileCheck %s

module {
  llvm.func @kernel0() {
    %0 = llvm.mlir.constant(2 : i32) : i32
    %1 = llvm.mlir.constant(0 : i32) : i32
    %2 = llvm.mlir.constant(1 : i32) : i32
    %3 = llvm.mlir.constant(false) : i1
    llvm.intr.sideeffect(%0, %1, %2, %3) {llvm.bundle.xlx_array_partition = 4 : i64} : i32, i32, i32, i1

    // CHECK: call void @llvm.sideeffect() [ "xlx_array_partition"(i32 2, i32 0, i32 1, i1 false) ]
    
    llvm.return
  }
}