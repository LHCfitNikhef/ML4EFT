C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     -(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) +
C      P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)
C     
      SUBROUTINE FFV10_3(F1, F2, COUP, M3, W3,V3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      REAL*8 M3
      REAL*8 P3(0:3)
      COMPLEX*16 TMP10
      COMPLEX*16 V3(6)
      REAL*8 W3
      COMPLEX*16 DENOM
      V3(1) = +F1(1)+F2(1)
      V3(2) = +F1(2)+F2(2)
      P3(0) = -DBLE(V3(1))
      P3(1) = -DBLE(V3(2))
      P3(2) = -DIMAG(V3(2))
      P3(3) = -DIMAG(V3(1))
      TMP10 = (F1(5)*-F2(5)*(P3(1)*P3(1)+P3(2)*P3(2)+P3(3)*P3(3)-P3(0)
     $ *P3(0))-F1(6)*F2(6)*(P3(1)*P3(1)+P3(2)*P3(2)+P3(3)*P3(3)-P3(0)
     $ *P3(0)))
      DENOM = COUP/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 -CI
     $ * W3))
      V3(3)= DENOM*2D0 * CI*(F1(5)*(F2(6)*(P3(1)+CI*(P3(2)))+F2(5)
     $ *P3(3))+F1(6)*(F2(5)*(P3(1)-CI*(P3(2)))-F2(6)*P3(3)))
      V3(4)= DENOM*2D0 * CI*(F1(5)*(F2(6)*(P3(0)-P3(3))-CI*(F2(5)*P3(2)
     $ ))+F1(6)*(F2(5)*(P3(0)+P3(3))+CI*(F2(6)*P3(2))))
      V3(5)= DENOM*2D0*(F1(5)*(F2(6)*(P3(3)-P3(0))-F2(5)*P3(1))+F1(6)
     $ *(F2(5)*(P3(0)+P3(3))+F2(6)*P3(1)))
      V3(6)= DENOM*2D0 * CI*(F1(5)*(F2(6)*(P3(1)+CI*(P3(2)))+F2(5)
     $ *P3(0))+F1(6)*(F2(5)*(+CI*(P3(2))-P3(1))-F2(6)*P3(0)))
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     -(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) +
C      P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)
C     
      SUBROUTINE FFV10_3_3(F1, F2, COUP1, COUP2, M3, W3,V3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP1
      COMPLEX*16 COUP2
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      REAL*8 M3
      REAL*8 P3(0:3)
      COMPLEX*16 V3(6)
      COMPLEX*16 VTMP(6)
      REAL*8 W3
      COMPLEX*16 DENOM
      INTEGER*4 I
      CALL FFV10_3(F1,F2,COUP1,M3,W3,V3)
      CALL FFV3_3(F1,F2,COUP2,M3,W3,VTMP)
      DO I = 3, 6
        V3(I) = V3(I) + VTMP(I)
      ENDDO
      END


