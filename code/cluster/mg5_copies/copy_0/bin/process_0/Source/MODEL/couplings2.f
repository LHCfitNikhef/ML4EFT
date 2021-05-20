ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP2()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_478 = -((MDL_CDGIM*MDL_VEVHAT*MDL_YB)/(MDL_LAMBDASMEFT__EXP__2
     $ *MDL_SQRT__2))
      GC_479 = (MDL_CDGRE*MDL_COMPLEXI*MDL_VEVHAT*MDL_YB)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_538 = -((MDL_CUGIM*MDL_VEVHAT*MDL_YC)/(MDL_LAMBDASMEFT__EXP__2
     $ *MDL_SQRT__2))
      GC_539 = (MDL_CUGRE*MDL_COMPLEXI*MDL_VEVHAT*MDL_YC)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_612 = -((MDL_CDGIM*MDL_VEVHAT*MDL_YDO)/(MDL_LAMBDASMEFT__EXP__
     $2*MDL_SQRT__2))
      GC_613 = (MDL_CDGRE*MDL_COMPLEXI*MDL_VEVHAT*MDL_YDO)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_878 = -((MDL_CDGIM*MDL_VEVHAT*MDL_YS)/(MDL_LAMBDASMEFT__EXP__2
     $ *MDL_SQRT__2))
      GC_879 = (MDL_CDGRE*MDL_COMPLEXI*MDL_VEVHAT*MDL_YS)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_976 = -((MDL_CUGIM*MDL_VEVHAT*MDL_YT)/(MDL_LAMBDASMEFT__EXP__2
     $ *MDL_SQRT__2))
      GC_977 = (MDL_CUGRE*MDL_COMPLEXI*MDL_VEVHAT*MDL_YT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_1005 = -((MDL_CQUQD11IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2)
     $ 
      GC_1006 = (MDL_CQUQD11IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2
      GC_1007 = -((MDL_CQUQD11RE*MDL_COMPLEXI*MDL_YB*MDL_YT)
     $ /MDL_LAMBDASMEFT__EXP__2)
      GC_1008 = -((MDL_CQUQD1IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2)
      GC_1009 = (MDL_CQUQD1IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2
      GC_1010 = (MDL_CQUQD1RE*MDL_COMPLEXI*MDL_YB*MDL_YT)
     $ /MDL_LAMBDASMEFT__EXP__2
      GC_1011 = -((MDL_CQUQD81IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2)
     $ 
      GC_1012 = (MDL_CQUQD81IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2
      GC_1013 = -((MDL_CQUQD81RE*MDL_COMPLEXI*MDL_YB*MDL_YT)
     $ /MDL_LAMBDASMEFT__EXP__2)
      GC_1014 = -((MDL_CQUQD8IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2)
      GC_1015 = (MDL_CQUQD8IM*MDL_YB*MDL_YT)/MDL_LAMBDASMEFT__EXP__2
      GC_1016 = (MDL_CQUQD8RE*MDL_COMPLEXI*MDL_YB*MDL_YT)
     $ /MDL_LAMBDASMEFT__EXP__2
      GC_1023 = -((MDL_CQUQD11IM*MDL_YDO*MDL_YT)/MDL_LAMBDASMEFT__EXP__
     $2)
      GC_1024 = (MDL_CQUQD11IM*MDL_YDO*MDL_YT)/MDL_LAMBDASMEFT__EXP__2
      GC_1025 = -((MDL_CQUQD11RE*MDL_COMPLEXI*MDL_YDO*MDL_YT)
     $ /MDL_LAMBDASMEFT__EXP__2)
      END
