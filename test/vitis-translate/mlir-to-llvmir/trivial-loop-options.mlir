// RUN: vitis-translate --mlir-to-llvmir -opaque-pointers=0 %s | FileCheck %s

module {
// CHECK: define void @kernel0()
  llvm.func @kernel0() {

// CHECK-DAG: !{!"llvm.loop.name", !"VITIS_LOOP_53_6"}
// CHECK-DAG: !{!"llvm.loop.vectorize.width", i32 1}
// CHECK-DAG: !{!"llvm.loop.interleave.count", i32 2}
// CHECK-DAG: !{!"llvm.loop.unroll.count", i32 3}
// CHECK-DAG: !{!"llvm.loop.unroll.withoutcheck", i32 4}
// CHECK-DAG: !{!"llvm.loop.vectorize.enable", i1 false}
// CHECK-DAG: !{!"llvm.loop.distribute.enable", i1 true}
// CHECK-DAG: !{!"llvm.loop.flatten.enable", i1 false}
// CHECK-DAG: !{!"llvm.loop.dataflow.enable", i1 true}
// CHECK-DAG: !{!"llvm.loop.pipeline.enable", i32 5, i1 true, i8 6}
// CHECK-DAG: !{!"llvm.loop.latency", i32 5, i32 6}
// CHECK-DAG: !{!"llvm.loop.tripcount", i32 5, i32 6, i32 7}
// CHECK-DAG: !{!"llvm.loop.unroll.enable"}

    llvm.br ^bb1 {llvm.loop.dataflow.enable = true, llvm.loop.distribute.enable = true, llvm.loop.flatten.enable = false, llvm.loop.interleave.count = 2 : i32, llvm.loop.latency = [5 : i32, 6 : i32], llvm.loop.name = "VITIS_LOOP_53_6", llvm.loop.pipeline.enable = [5 : i32, true, 6 : i8], llvm.loop.tripcount = [5 : i32, 6 : i32, 7 : i32], llvm.loop.unroll.enable, llvm.loop.unroll.count = 3 : i32, llvm.loop.unroll.withoutcheck = 4 : i32, llvm.loop.vectorize.enable = false, llvm.loop.vectorize.width = 1 : i32}
  ^bb1:
    llvm.return
  }
}
