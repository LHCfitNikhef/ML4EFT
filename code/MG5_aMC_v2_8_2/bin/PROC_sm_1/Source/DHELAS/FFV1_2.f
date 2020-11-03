C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,1)
C     
      SUBROUTINE FFV1_2(F1, V3, COUP, M2, W2,F2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(6)
      REAL*8 M2
      REAL*8 P2(0:3)
      COMPLEX*16 V3(*)
      REAL*8 W2
      COMPLEX*16 DENOM
      F2(1) = +F1(1)+V3(1)
      F2(2) = +F1(2)+V3(2)
      P2(0) = -DBLE(F2(1))
      P2(1) = -DBLE(F2(2))
      P2(2) = -DIMAG(F2(2))
      P2(3) = -DIMAG(F2(1))
      DENOM = COUP/(P2(0)**2-P2(1)**2-P2(2)**2-P2(3)**2 - M2 * (M2 -CI
     $ * W2))
      F2(3)= DENOM*CI*(F1(3)*(P2(0)*(V3(3)+V3(6))+(P2(1)*(-1D0)*(V3(4)
     $ +CI*(V3(5)))+(P2(2)*(+CI*(V3(4))-V3(5))-P2(3)*(V3(3)+V3(6)))))
     $ +(F1(4)*(P2(0)*(V3(4)-CI*(V3(5)))+(P2(1)*(V3(6)-V3(3))+(P2(2)*(
     $ -CI*(V3(6))+CI*(V3(3)))+P2(3)*(+CI*(V3(5))-V3(4)))))+M2*(F1(5)
     $ *(V3(3)-V3(6))+F1(6)*(+CI*(V3(5))-V3(4)))))
      F2(4)= DENOM*(-CI)*(F1(3)*(P2(0)*(-1D0)*(V3(4)+CI*(V3(5)))+(P2(1)
     $ *(V3(3)+V3(6))+(P2(2)*(+CI*(V3(3)+V3(6)))-P2(3)*(V3(4)+CI*(V3(5)
     $ )))))+(F1(4)*(P2(0)*(V3(6)-V3(3))+(P2(1)*(V3(4)-CI*(V3(5)))
     $ +(P2(2)*(V3(5)+CI*(V3(4)))+P2(3)*(V3(6)-V3(3)))))+M2*(F1(5)
     $ *(V3(4)+CI*(V3(5)))-F1(6)*(V3(3)+V3(6)))))
      F2(5)= DENOM*(-CI)*(F1(5)*(P2(0)*(V3(6)-V3(3))+(P2(1)*(V3(4)+CI
     $ *(V3(5)))+(P2(2)*(V3(5)-CI*(V3(4)))+P2(3)*(V3(6)-V3(3)))))
     $ +(F1(6)*(P2(0)*(V3(4)-CI*(V3(5)))+(P2(1)*(-1D0)*(V3(3)+V3(6))
     $ +(P2(2)*(+CI*(V3(3)+V3(6)))+P2(3)*(V3(4)-CI*(V3(5))))))+M2
     $ *(F1(3)*(-1D0)*(V3(3)+V3(6))+F1(4)*(+CI*(V3(5))-V3(4)))))
      F2(6)= DENOM*CI*(F1(5)*(P2(0)*(-1D0)*(V3(4)+CI*(V3(5)))+(P2(1)
     $ *(V3(3)-V3(6))+(P2(2)*(-CI*(V3(6))+CI*(V3(3)))+P2(3)*(V3(4)+CI
     $ *(V3(5))))))+(F1(6)*(P2(0)*(V3(3)+V3(6))+(P2(1)*(+CI*(V3(5))
     $ -V3(4))+(P2(2)*(-1D0)*(V3(5)+CI*(V3(4)))-P2(3)*(V3(3)+V3(6)))))
     $ +M2*(F1(3)*(V3(4)+CI*(V3(5)))+F1(4)*(V3(3)-V3(6)))))
      END


