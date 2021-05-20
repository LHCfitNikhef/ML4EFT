C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,-1)*Gamma(4,-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(
C     -1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)
C     
      SUBROUTINE FFVV3_0(F1, F2, V3, V4, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 TMP33
      COMPLEX*16 V3(*)
      COMPLEX*16 TMP31
      COMPLEX*16 F1(*)
      COMPLEX*16 V4(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 TMP32
      COMPLEX*16 VERTEX
      COMPLEX*16 COUP
      TMP33 = (F1(5)*(F2(5)*(V3(3)*(V4(3)+V4(6))+(V3(4)*(+CI*(V4(5))
     $ -V4(4))+(V3(5)*(-1D0)*(V4(5)+CI*(V4(4)))-V3(6)*(V4(3)+V4(6)))))
     $ +F2(6)*(V3(3)*(V4(4)+CI*(V4(5)))+(V3(4)*(V4(6)-V4(3))+(V3(5)*(
     $ -CI*(V4(3))+CI*(V4(6)))-V3(6)*(V4(4)+CI*(V4(5)))))))+F1(6)
     $ *(F2(5)*(V3(3)*(V4(4)-CI*(V4(5)))+(V3(4)*(-1D0)*(V4(3)+V4(6))
     $ +(V3(5)*(+CI*(V4(3)+V4(6)))+V3(6)*(V4(4)-CI*(V4(5))))))+F2(6)
     $ *(V3(3)*(V4(3)-V4(6))+(V3(4)*(-1D0)*(V4(4)+CI*(V4(5)))+(V3(5)*(
     $ +CI*(V4(4))-V4(5))+V3(6)*(V4(3)-V4(6)))))))
      TMP32 = (F1(3)*(F2(3)*(V3(3)*(V4(3)-V4(6))+(V3(4)*(+CI*(V4(5))
     $ -V4(4))+(V3(5)*(-1D0)*(V4(5)+CI*(V4(4)))+V3(6)*(V4(3)-V4(6)))))
     $ +F2(4)*(V3(3)*(-1D0)*(V4(4)+CI*(V4(5)))+(V3(4)*(V4(3)+V4(6))
     $ +(V3(5)*(+CI*(V4(3)+V4(6)))-V3(6)*(V4(4)+CI*(V4(5)))))))+F1(4)
     $ *(F2(3)*(V3(3)*(+CI*(V4(5))-V4(4))+(V3(4)*(V4(3)-V4(6))+(V3(5)
     $ *(-CI*(V4(3))+CI*(V4(6)))+V3(6)*(V4(4)-CI*(V4(5))))))+F2(4)
     $ *(V3(3)*(V4(3)+V4(6))+(V3(4)*(-1D0)*(V4(4)+CI*(V4(5)))+(V3(5)*(
     $ +CI*(V4(4))-V4(5))-V3(6)*(V4(3)+V4(6)))))))
      TMP31 = (F1(3)*(F2(3)*(V3(3)*(V4(3)+V4(6))+(V3(4)*(-1D0)*(V4(4)
     $ +CI*(V4(5)))+(V3(5)*(+CI*(V4(4))-V4(5))-V3(6)*(V4(3)+V4(6)))))
     $ +F2(4)*(V3(3)*(V4(4)+CI*(V4(5)))+(V3(4)*(-1D0)*(V4(3)+V4(6))
     $ +(V3(5)*(-1D0)*(+CI*(V4(3)+V4(6)))+V3(6)*(V4(4)+CI*(V4(5)))))))
     $ +(F1(4)*(F2(3)*(V3(3)*(V4(4)-CI*(V4(5)))+(V3(4)*(V4(6)-V4(3))
     $ +(V3(5)*(-CI*(V4(6))+CI*(V4(3)))+V3(6)*(+CI*(V4(5))-V4(4)))))
     $ +F2(4)*(V3(3)*(V4(3)-V4(6))+(V3(4)*(+CI*(V4(5))-V4(4))+(V3(5)*(
     $ -1D0)*(V4(5)+CI*(V4(4)))+V3(6)*(V4(3)-V4(6))))))+(F1(5)*(F2(5)
     $ *(V3(3)*(V4(3)-V4(6))+(V3(4)*(-1D0)*(V4(4)+CI*(V4(5)))+(V3(5)*(
     $ +CI*(V4(4))-V4(5))+V3(6)*(V4(3)-V4(6)))))+F2(6)*(V3(3)*(-1D0)
     $ *(V4(4)+CI*(V4(5)))+(V3(4)*(V4(3)-V4(6))+(V3(5)*(-CI*(V4(6))+CI
     $ *(V4(3)))+V3(6)*(V4(4)+CI*(V4(5)))))))+F1(6)*(F2(5)*(V3(3)*(+CI
     $ *(V4(5))-V4(4))+(V3(4)*(V4(3)+V4(6))+(V3(5)*(-1D0)*(+CI*(V4(3)
     $ +V4(6)))+V3(6)*(+CI*(V4(5))-V4(4)))))+F2(6)*(V3(3)*(V4(3)+V4(6))
     $ +(V3(4)*(+CI*(V4(5))-V4(4))+(V3(5)*(-1D0)*(V4(5)+CI*(V4(4)))
     $ -V3(6)*(V4(3)+V4(6)))))))))
      VERTEX = COUP*(-CI*(TMP31)+CI*(TMP32+TMP33))
      END


