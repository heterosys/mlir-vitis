; RUN: vitis-translate --import-llvm %s | FileCheck %s

; CHECK-DAG: llvm.func @kernel0()
define void @kernel0() {
entry:
  br label %for
for:

  br label %for, !llvm.loop !1
  ret void
}

!1 = distinct !{!1, !2, !3, !4, !5, !6, !7, !8, !9, !10, !11, !12, !13, !14}

; CHECK-DAG: llvm.loop.name = "VITIS_LOOP_53_6"
!2 = !{!"llvm.loop.name", !"VITIS_LOOP_53_6"}

; CHECK-DAG: llvm.loop.vectorize.width = 1 : i32
!3 = !{!"llvm.loop.vectorize.width", i32 1}

; CHECK-DAG: llvm.loop.interleave.count = 2 : i32
!4 = !{!"llvm.loop.interleave.count", i32 2}

; CHECK-DAG: llvm.loop.unroll.count = 3 : i32
!5 = !{!"llvm.loop.unroll.count", i32 3}

; CHECK-DAG: llvm.loop.unroll.withoutcheck = 4 : i32
!6 = !{!"llvm.loop.unroll.withoutcheck", i32 4}

; CHECK-DAG: llvm.loop.vectorize.enable = false
!7 = !{!"llvm.loop.vectorize.enable", i1 false}

; CHECK-DAG: llvm.loop.distribute.enable = true
!8 = !{!"llvm.loop.distribute.enable", i1 true}

; CHECK-DAG: llvm.loop.flatten.enable = false
!9 = !{!"llvm.loop.flatten.enable", i1 false}

; CHECK-DAG: llvm.loop.dataflow.enable = true
!10 = !{!"llvm.loop.dataflow.enable", i1 true}

; CHECK-DAG: llvm.loop.pipeline.enable = [5 : i32, true, 6 : i8]
!11 = !{!"llvm.loop.pipeline.enable", i32 5, i1 true, i8 6}

; CHECK-DAG: llvm.loop.latency = [5 : i32, 6 : i32]
!12 = !{!"llvm.loop.latency", i32 5, i32 6}

; CHECK-DAG: llvm.loop.tripcount = [5 : i32, 6 : i32, 7 : i32]
!13 = !{!"llvm.loop.tripcount", i32 5, i32 6, i32 7}

; CHECK-DAG: llvm.loop.unroll.enable
!14 = !{!"llvm.loop.unroll.enable"}
