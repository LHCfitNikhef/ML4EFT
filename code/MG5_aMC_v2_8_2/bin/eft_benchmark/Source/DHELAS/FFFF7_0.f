C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(-2,-6,-5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Gamma(-1,4,-6)*Pro
C     jM(-5,3)*ProjM(-3,1)
C     
      SUBROUTINE FFFF7_0(F1, F2, F3, F4, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP33
      COMPLEX*16 VERTEX
      TMP33 = (F1(3)*F3(4)*(F2(3)*F4(4)-F2(4)*F4(3))+F1(4)*F3(3)*(F2(4)
     $ *F4(3)-F2(3)*F4(4)))
      VERTEX = COUP*(-8D0 * CI * TMP33)
      END


