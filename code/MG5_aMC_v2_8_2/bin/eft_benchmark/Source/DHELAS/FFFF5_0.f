C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,1)*ProjM(-2,3)
C     
      SUBROUTINE FFFF5_0(F1, F2, F3, F4, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP32
      COMPLEX*16 VERTEX
      TMP32 = (F1(3)*F3(4)*(F2(6)*F4(5)-F2(5)*F4(6))+F1(4)*F3(3)*(F2(5)
     $ *F4(6)-F2(6)*F4(5)))
      VERTEX = COUP*(-2D0 * CI * TMP32)
      END


