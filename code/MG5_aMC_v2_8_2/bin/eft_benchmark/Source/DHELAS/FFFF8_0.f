C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     ProjM(4,3)*ProjP(2,1)
C     
      SUBROUTINE FFFF8_0(F1, F2, F3, F4, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP22
      COMPLEX*16 TMP31
      COMPLEX*16 VERTEX
      TMP22 = (F1(5)*F2(5)+F1(6)*F2(6))
      TMP31 = (F4(3)*F3(3)+F4(4)*F3(4))
      VERTEX = COUP*(-CI * TMP31*TMP22)
      END


