; RUN: vitis-translate --import-llvm %s | FileCheck %s

; CHECK-DAG: llvm.func @kernel0() attributes {llvm.alwaysinline}
define void @kernel0() #0 {
entry:
  ret void
}

; CHECK-DAG: llvm.func @kernel1() attributes {llvm.noinline}
define void @kernel1() #1 {
entry:
  ret void
}

attributes #0 = { alwaysinline }
attributes #1 = { noinline }