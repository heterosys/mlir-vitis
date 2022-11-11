; RUN: vitis-translate --import-llvm %s | FileCheck %s

; CHECK-DAG: llvm.func @kernel0() attributes {llvm.string.fpga.demangled.name = "kernel0", llvm.string.fpga.top.func = "kernel0"}
define void @kernel0() #0 {
entry:
  ret void
}

attributes #0 = { "fpga.demangled.name"="kernel0" "fpga.top.func"="kernel0" }