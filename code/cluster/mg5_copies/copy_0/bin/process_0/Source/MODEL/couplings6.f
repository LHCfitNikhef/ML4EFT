ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP6()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_347 = (2.000000D+00*MDL_CHGTIL*G*MDL_VEVHAT__EXP__2)
     $ /MDL_LAMBDASMEFT__EXP__2
      GC_988 = (MDL_CUGIM*MDL_COMPLEXI*G*MDL_VEVHAT*MDL_YT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_989 = (MDL_CUGRE*G*MDL_VEVHAT*MDL_YT)/(MDL_LAMBDASMEFT__EXP__2
     $ *MDL_SQRT__2)
      GC_6 = -(MDL_COMPLEXI*G)
      GC_7 = G
      END
