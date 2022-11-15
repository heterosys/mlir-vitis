; RUN: vitis-translate --import-llvm %s | FileCheck %s

declare void @llvm.sideeffect()

; CHECK-DAG: llvm.func @kernel0()
define void @kernel0() {
entry:
  ; CHECK-DAG: llvm.intr.sideeffect(%0, %1, %2, %3) {llvm.bundle.xlx_array_partition = 4 : i64} : i32, i32, i32, i1
  call void @llvm.sideeffect() [ "xlx_array_partition"(i32 2, i32 0, i32 1, i1 false) ]
  ret void
}