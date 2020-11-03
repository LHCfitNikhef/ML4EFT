ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP5()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_6 = -G
      GC_7 = MDL_COMPLEXI*G
      GC_727 = -((MDL_CTG*G*MDL_GSTRONG*MDL_VEV)/(MDL_LAMBDA__EXP__2
     $ *MDL_SQRT__2))
      GC_728 = (MDL_CTGI*MDL_COMPLEXI*G*MDL_GSTRONG*MDL_VEV)
     $ /(MDL_LAMBDA__EXP__2*MDL_SQRT__2)
      END
