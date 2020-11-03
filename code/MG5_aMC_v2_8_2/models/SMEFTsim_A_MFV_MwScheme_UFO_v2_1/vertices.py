# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Sat 10 Mar 2018 00:31:47


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
             couplings = {(0,0):C.GC_9,(0,2):C.GC_601,(0,1):C.GC_602})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1334})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1011})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
             couplings = {(0,0):C.GC_963,(0,2):C.GC_964,(0,1):C.GC_965})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_1385})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_1032})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_960})

V_8 = Vertex(name = 'V_8',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_1314})

V_9 = Vertex(name = 'V_9',
             particles = [ P.a, P.a, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVSS2 ],
             couplings = {(0,0):C.GC_826})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_961})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_966})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_603})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_604,(0,0):C.GC_725})

V_14 = Vertex(name = 'V_14',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1335})

V_15 = Vertex(name = 'V_15',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_967,(0,0):C.GC_989})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1386})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2, L.VVV3, L.VVV4 ],
              couplings = {(0,2):C.GC_746,(0,0):C.GC_3,(0,1):C.GC_1013})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_1361})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_962,(0,0):C.GC_1388})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_1315})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_827,(0,0):C.GC_1378})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_825,(0,0):C.GC_824})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1377})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1313,(0,0):C.GC_1312})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1387})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV2, L.VVV4 ],
              couplings = {(0,2):C.GC_608,(0,1):C.GC_739,(0,0):C.GC_1012})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_1362})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_7})

V_29 = Vertex(name = 'V_29',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV2, L.VVV4 ],
              couplings = {(0,1):C.GC_600,(0,0):C.GC_7})

V_30 = Vertex(name = 'V_30',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3 ],
              couplings = {(0,0):C.GC_970})

V_31 = Vertex(name = 'V_31',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
              couplings = {(0,1):C.GC_610,(1,5):C.GC_610,(2,4):C.GC_610,(1,2):C.GC_8,(0,0):C.GC_8,(2,3):C.GC_8})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3 ],
              couplings = {(0,1):C.GC_968,(0,0):C.GC_992})

V_33 = Vertex(name = 'V_33',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_747,(0,1):C.GC_5})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_1363})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6, L.VVVV9 ],
              couplings = {(0,1):C.GC_609,(0,0):C.GC_1364})

V_36 = Vertex(name = 'V_36',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_740})

V_37 = Vertex(name = 'V_37',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3 ],
              couplings = {(0,1):C.GC_991,(0,0):C.GC_969})

V_38 = Vertex(name = 'V_38',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_741,(0,1):C.GC_726})

V_39 = Vertex(name = 'V_39',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_728})

V_40 = Vertex(name = 'V_40',
              particles = [ P.d__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_986,(0,2):C.GC_1467,(0,1):C.GC_983})

V_41 = Vertex(name = 'V_41',
              particles = [ P.s__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_987,(0,2):C.GC_1691,(0,1):C.GC_984})

V_42 = Vertex(name = 'V_42',
              particles = [ P.b__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_988,(0,2):C.GC_1390,(0,1):C.GC_985})

V_43 = Vertex(name = 'V_43',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_1466,(0,0):C.GC_1331,(0,1):C.GC_1328})

V_44 = Vertex(name = 'V_44',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1481})

V_45 = Vertex(name = 'V_45',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_1690,(0,0):C.GC_1332,(0,1):C.GC_1329})

V_46 = Vertex(name = 'V_46',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1705})

V_47 = Vertex(name = 'V_47',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_1389,(0,0):C.GC_1333,(0,1):C.GC_1330})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1404})

V_49 = Vertex(name = 'V_49',
              particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS3 ],
              couplings = {(0,0):C.GC_1487})

V_50 = Vertex(name = 'V_50',
              particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS3 ],
              couplings = {(0,0):C.GC_1590})

V_51 = Vertex(name = 'V_51',
              particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS3 ],
              couplings = {(0,0):C.GC_1792})

V_52 = Vertex(name = 'V_52',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1484})

V_53 = Vertex(name = 'V_53',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1575})

V_54 = Vertex(name = 'V_54',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1576})

V_55 = Vertex(name = 'V_55',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1587})

V_56 = Vertex(name = 'V_56',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1678})

V_57 = Vertex(name = 'V_57',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1679})

V_58 = Vertex(name = 'V_58',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1789})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1880})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_1881})

V_61 = Vertex(name = 'V_61',
              particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_861,(0,1):C.GC_672,(0,2):C.GC_671,(0,3):C.GC_670,(0,5):C.GC_1586,(0,0):C.GC_1585})

V_62 = Vertex(name = 'V_62',
              particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_861,(0,1):C.GC_672,(0,2):C.GC_671,(0,3):C.GC_670,(0,5):C.GC_1689,(0,0):C.GC_1688})

V_63 = Vertex(name = 'V_63',
              particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_861,(0,1):C.GC_672,(0,2):C.GC_671,(0,3):C.GC_670,(0,5):C.GC_1891,(0,0):C.GC_1890})

V_64 = Vertex(name = 'V_64',
              particles = [ P.s__tilde__, P.d, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_333,(0,0):C.GC_643})

V_65 = Vertex(name = 'V_65',
              particles = [ P.s__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_333,(0,0):C.GC_643})

V_66 = Vertex(name = 'V_66',
              particles = [ P.s__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_333,(0,0):C.GC_643})

V_67 = Vertex(name = 'V_67',
              particles = [ P.b__tilde__, P.d, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_347,(0,0):C.GC_646})

V_68 = Vertex(name = 'V_68',
              particles = [ P.b__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_347,(0,0):C.GC_646})

V_69 = Vertex(name = 'V_69',
              particles = [ P.b__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_347,(0,0):C.GC_646})

V_70 = Vertex(name = 'V_70',
              particles = [ P.d__tilde__, P.s, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_361,(0,0):C.GC_649})

V_71 = Vertex(name = 'V_71',
              particles = [ P.d__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_361,(0,0):C.GC_649})

V_72 = Vertex(name = 'V_72',
              particles = [ P.d__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_361,(0,0):C.GC_649})

V_73 = Vertex(name = 'V_73',
              particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_905,(0,1):C.GC_694,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_1709,(0,0):C.GC_1708})

V_74 = Vertex(name = 'V_74',
              particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_905,(0,1):C.GC_694,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_1711,(0,0):C.GC_1710})

V_75 = Vertex(name = 'V_75',
              particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_905,(0,1):C.GC_694,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_1893,(0,0):C.GC_1892})

V_76 = Vertex(name = 'V_76',
              particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_375,(0,0):C.GC_652})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_375,(0,0):C.GC_652})

V_78 = Vertex(name = 'V_78',
              particles = [ P.b__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_375,(0,0):C.GC_652})

V_79 = Vertex(name = 'V_79',
              particles = [ P.d__tilde__, P.b, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_389,(0,0):C.GC_655})

V_80 = Vertex(name = 'V_80',
              particles = [ P.d__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_389,(0,0):C.GC_655})

V_81 = Vertex(name = 'V_81',
              particles = [ P.d__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_389,(0,0):C.GC_655})

V_82 = Vertex(name = 'V_82',
              particles = [ P.s__tilde__, P.b, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_403,(0,0):C.GC_658})

V_83 = Vertex(name = 'V_83',
              particles = [ P.s__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_403,(0,0):C.GC_658})

V_84 = Vertex(name = 'V_84',
              particles = [ P.s__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF4 ],
              couplings = {(0,1):C.GC_403,(0,0):C.GC_658})

V_85 = Vertex(name = 'V_85',
              particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_956,(0,1):C.GC_724,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_1578,(0,0):C.GC_1577})

V_86 = Vertex(name = 'V_86',
              particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_956,(0,1):C.GC_724,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_1681,(0,0):C.GC_1680})

V_87 = Vertex(name = 'V_87',
              particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
              couplings = {(0,4):C.GC_956,(0,1):C.GC_724,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_1883,(0,0):C.GC_1882})

V_88 = Vertex(name = 'V_88',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_862,(0,5):C.GC_1543,(0,3):C.GC_1542,(0,4):C.GC_1542,(0,1):C.GC_1541,(0,0):C.GC_1532})

V_89 = Vertex(name = 'V_89',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_611,(0,5):C.GC_1546,(0,3):C.GC_1545,(0,4):C.GC_1545,(0,1):C.GC_1544,(0,0):C.GC_1533})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_612,(0,5):C.GC_1549,(0,3):C.GC_1548,(0,4):C.GC_1548,(0,1):C.GC_1547,(0,0):C.GC_1534})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_613,(0,5):C.GC_1552,(0,3):C.GC_1551,(0,4):C.GC_1551,(0,1):C.GC_1550,(0,0):C.GC_1535})

V_92 = Vertex(name = 'V_92',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_906,(0,5):C.GC_1555,(0,3):C.GC_1554,(0,4):C.GC_1554,(0,1):C.GC_1553,(0,0):C.GC_1536})

V_93 = Vertex(name = 'V_93',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_614,(0,5):C.GC_1558,(0,3):C.GC_1557,(0,4):C.GC_1557,(0,1):C.GC_1556,(0,0):C.GC_1537})

V_94 = Vertex(name = 'V_94',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_615,(0,5):C.GC_1561,(0,3):C.GC_1560,(0,4):C.GC_1560,(0,1):C.GC_1559,(0,0):C.GC_1538})

V_95 = Vertex(name = 'V_95',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_616,(0,5):C.GC_1564,(0,3):C.GC_1563,(0,4):C.GC_1563,(0,1):C.GC_1562,(0,0):C.GC_1539})

V_96 = Vertex(name = 'V_96',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_957,(0,5):C.GC_1567,(0,3):C.GC_1566,(0,4):C.GC_1566,(0,1):C.GC_1565,(0,0):C.GC_1540})

V_97 = Vertex(name = 'V_97',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_862,(0,5):C.GC_1646,(0,3):C.GC_1645,(0,4):C.GC_1645,(0,1):C.GC_1644,(0,0):C.GC_1635})

V_98 = Vertex(name = 'V_98',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_611,(0,5):C.GC_1649,(0,3):C.GC_1648,(0,4):C.GC_1648,(0,1):C.GC_1647,(0,0):C.GC_1636})

V_99 = Vertex(name = 'V_99',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_612,(0,5):C.GC_1652,(0,3):C.GC_1651,(0,4):C.GC_1651,(0,1):C.GC_1650,(0,0):C.GC_1637})

V_100 = Vertex(name = 'V_100',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_613,(0,5):C.GC_1655,(0,3):C.GC_1654,(0,4):C.GC_1654,(0,1):C.GC_1653,(0,0):C.GC_1638})

V_101 = Vertex(name = 'V_101',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_906,(0,5):C.GC_1658,(0,3):C.GC_1657,(0,4):C.GC_1657,(0,1):C.GC_1656,(0,0):C.GC_1639})

V_102 = Vertex(name = 'V_102',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_614,(0,5):C.GC_1661,(0,3):C.GC_1660,(0,4):C.GC_1660,(0,1):C.GC_1659,(0,0):C.GC_1640})

V_103 = Vertex(name = 'V_103',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_615,(0,5):C.GC_1664,(0,3):C.GC_1663,(0,4):C.GC_1663,(0,1):C.GC_1662,(0,0):C.GC_1641})

V_104 = Vertex(name = 'V_104',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_616,(0,5):C.GC_1667,(0,3):C.GC_1666,(0,4):C.GC_1666,(0,1):C.GC_1665,(0,0):C.GC_1642})

V_105 = Vertex(name = 'V_105',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_957,(0,5):C.GC_1670,(0,3):C.GC_1669,(0,4):C.GC_1669,(0,1):C.GC_1668,(0,0):C.GC_1643})

V_106 = Vertex(name = 'V_106',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_862,(0,5):C.GC_1848,(0,3):C.GC_1847,(0,4):C.GC_1847,(0,1):C.GC_1846,(0,0):C.GC_1837})

V_107 = Vertex(name = 'V_107',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_611,(0,5):C.GC_1851,(0,3):C.GC_1850,(0,4):C.GC_1850,(0,1):C.GC_1849,(0,0):C.GC_1838})

V_108 = Vertex(name = 'V_108',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_612,(0,5):C.GC_1854,(0,3):C.GC_1853,(0,4):C.GC_1853,(0,1):C.GC_1852,(0,0):C.GC_1839})

V_109 = Vertex(name = 'V_109',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_613,(0,5):C.GC_1857,(0,3):C.GC_1856,(0,4):C.GC_1856,(0,1):C.GC_1855,(0,0):C.GC_1840})

V_110 = Vertex(name = 'V_110',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_906,(0,5):C.GC_1860,(0,3):C.GC_1859,(0,4):C.GC_1859,(0,1):C.GC_1858,(0,0):C.GC_1841})

V_111 = Vertex(name = 'V_111',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,4):C.GC_1862,(0,2):C.GC_614,(0,5):C.GC_1863,(0,3):C.GC_1862,(0,1):C.GC_1861,(0,0):C.GC_1842})

V_112 = Vertex(name = 'V_112',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_615,(0,5):C.GC_1866,(0,3):C.GC_1865,(0,4):C.GC_1865,(0,1):C.GC_1864,(0,0):C.GC_1843})

V_113 = Vertex(name = 'V_113',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_616,(0,5):C.GC_1869,(0,3):C.GC_1868,(0,4):C.GC_1868,(0,1):C.GC_1867,(0,0):C.GC_1844})

V_114 = Vertex(name = 'V_114',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_957,(0,5):C.GC_1872,(0,3):C.GC_1871,(0,4):C.GC_1871,(0,1):C.GC_1870,(0,0):C.GC_1845})

V_115 = Vertex(name = 'V_115',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_863,(0,4):C.GC_1507,(0,2):C.GC_1506,(0,3):C.GC_1506,(0,0):C.GC_1496,(0,1):C.GC_1505})

V_116 = Vertex(name = 'V_116',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_617,(0,4):C.GC_1510,(0,2):C.GC_1509,(0,3):C.GC_1509,(0,0):C.GC_1497,(0,1):C.GC_1508})

V_117 = Vertex(name = 'V_117',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_618,(0,4):C.GC_1513,(0,2):C.GC_1512,(0,3):C.GC_1512,(0,0):C.GC_1498,(0,1):C.GC_1511})

V_118 = Vertex(name = 'V_118',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_863,(0,4):C.GC_1610,(0,2):C.GC_1609,(0,3):C.GC_1609,(0,0):C.GC_1599,(0,1):C.GC_1608})

V_119 = Vertex(name = 'V_119',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_617,(0,4):C.GC_1613,(0,2):C.GC_1612,(0,3):C.GC_1612,(0,0):C.GC_1600,(0,1):C.GC_1611})

V_120 = Vertex(name = 'V_120',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_618,(0,4):C.GC_1616,(0,2):C.GC_1615,(0,3):C.GC_1615,(0,0):C.GC_1601,(0,1):C.GC_1614})

V_121 = Vertex(name = 'V_121',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_863,(0,4):C.GC_1812,(0,2):C.GC_1811,(0,3):C.GC_1811,(0,0):C.GC_1801,(0,1):C.GC_1810})

V_122 = Vertex(name = 'V_122',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_617,(0,4):C.GC_1815,(0,2):C.GC_1814,(0,3):C.GC_1814,(0,0):C.GC_1802,(0,1):C.GC_1813})

V_123 = Vertex(name = 'V_123',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_618,(0,4):C.GC_1818,(0,2):C.GC_1817,(0,3):C.GC_1817,(0,0):C.GC_1803,(0,1):C.GC_1816})

V_124 = Vertex(name = 'V_124',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_619,(0,4):C.GC_1516,(0,2):C.GC_1515,(0,3):C.GC_1515,(0,0):C.GC_1499,(0,1):C.GC_1514})

V_125 = Vertex(name = 'V_125',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_907,(0,4):C.GC_1519,(0,2):C.GC_1518,(0,3):C.GC_1518,(0,0):C.GC_1500,(0,1):C.GC_1517})

V_126 = Vertex(name = 'V_126',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_620,(0,4):C.GC_1522,(0,2):C.GC_1521,(0,3):C.GC_1521,(0,0):C.GC_1501,(0,1):C.GC_1520})

V_127 = Vertex(name = 'V_127',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_619,(0,4):C.GC_1619,(0,2):C.GC_1618,(0,3):C.GC_1618,(0,0):C.GC_1602,(0,1):C.GC_1617})

V_128 = Vertex(name = 'V_128',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_907,(0,4):C.GC_1622,(0,2):C.GC_1621,(0,3):C.GC_1621,(0,0):C.GC_1603,(0,1):C.GC_1620})

V_129 = Vertex(name = 'V_129',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_620,(0,4):C.GC_1625,(0,2):C.GC_1624,(0,3):C.GC_1624,(0,0):C.GC_1604,(0,1):C.GC_1623})

V_130 = Vertex(name = 'V_130',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_619,(0,4):C.GC_1821,(0,2):C.GC_1820,(0,3):C.GC_1820,(0,0):C.GC_1804,(0,1):C.GC_1819})

V_131 = Vertex(name = 'V_131',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_907,(0,4):C.GC_1824,(0,2):C.GC_1823,(0,3):C.GC_1823,(0,0):C.GC_1805,(0,1):C.GC_1822})

V_132 = Vertex(name = 'V_132',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_620,(0,4):C.GC_1827,(0,2):C.GC_1826,(0,3):C.GC_1826,(0,0):C.GC_1806,(0,1):C.GC_1825})

V_133 = Vertex(name = 'V_133',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_621,(0,4):C.GC_1525,(0,2):C.GC_1524,(0,3):C.GC_1524,(0,0):C.GC_1502,(0,1):C.GC_1523})

V_134 = Vertex(name = 'V_134',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_622,(0,4):C.GC_1528,(0,2):C.GC_1527,(0,3):C.GC_1527,(0,0):C.GC_1503,(0,1):C.GC_1526})

V_135 = Vertex(name = 'V_135',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_958,(0,4):C.GC_1531,(0,2):C.GC_1530,(0,3):C.GC_1530,(0,0):C.GC_1504,(0,1):C.GC_1529})

V_136 = Vertex(name = 'V_136',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_621,(0,4):C.GC_1628,(0,2):C.GC_1627,(0,3):C.GC_1627,(0,0):C.GC_1605,(0,1):C.GC_1626})

V_137 = Vertex(name = 'V_137',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_622,(0,4):C.GC_1631,(0,2):C.GC_1630,(0,3):C.GC_1630,(0,0):C.GC_1606,(0,1):C.GC_1629})

V_138 = Vertex(name = 'V_138',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_958,(0,4):C.GC_1634,(0,2):C.GC_1633,(0,3):C.GC_1633,(0,0):C.GC_1607,(0,1):C.GC_1632})

V_139 = Vertex(name = 'V_139',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_621,(0,4):C.GC_1830,(0,2):C.GC_1829,(0,3):C.GC_1829,(0,0):C.GC_1807,(0,1):C.GC_1828})

V_140 = Vertex(name = 'V_140',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_622,(0,4):C.GC_1833,(0,2):C.GC_1832,(0,3):C.GC_1832,(0,0):C.GC_1808,(0,1):C.GC_1831})

V_141 = Vertex(name = 'V_141',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_958,(0,4):C.GC_1836,(0,2):C.GC_1835,(0,3):C.GC_1835,(0,0):C.GC_1809,(0,1):C.GC_1834})

V_142 = Vertex(name = 'V_142',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_978,(0,2):C.GC_1914,(0,1):C.GC_972})

V_143 = Vertex(name = 'V_143',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_980,(0,2):C.GC_1419,(0,1):C.GC_974})

V_144 = Vertex(name = 'V_144',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_982,(0,2):C.GC_1726,(0,1):C.GC_976})

V_145 = Vertex(name = 'V_145',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_1900,(0,0):C.GC_1325,(0,1):C.GC_1322})

V_146 = Vertex(name = 'V_146',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_1958})

V_147 = Vertex(name = 'V_147',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_1405,(0,0):C.GC_1326,(0,1):C.GC_1323})

V_148 = Vertex(name = 'V_148',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_1463})

V_149 = Vertex(name = 'V_149',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_1712,(0,0):C.GC_1327,(0,1):C.GC_1324})

V_150 = Vertex(name = 'V_150',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_1770})

V_151 = Vertex(name = 'V_151',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_1985,(0,7):C.GC_1984,(1,0):C.GC_1961,(3,0):C.GC_1919,(0,5):C.GC_11,(2,5):C.GC_92,(1,4):C.GC_834,(3,4):C.GC_837,(1,2):C.GC_840,(3,2):C.GC_847,(1,3):C.GC_828,(3,3):C.GC_831,(1,8):C.GC_1962,(3,8):C.GC_1928,(0,1):C.GC_518,(2,1):C.GC_173})

V_152 = Vertex(name = 'V_152',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2048,(0,4):C.GC_2047,(0,2):C.GC_20,(2,2):C.GC_101,(1,1):C.GC_623,(3,1):C.GC_624,(0,0):C.GC_519,(2,0):C.GC_176})

V_153 = Vertex(name = 'V_153',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2111,(0,4):C.GC_2110,(0,2):C.GC_29,(2,2):C.GC_110,(1,1):C.GC_626,(3,1):C.GC_627,(0,0):C.GC_520,(2,0):C.GC_179})

V_154 = Vertex(name = 'V_154',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_1987,(0,4):C.GC_1986,(0,2):C.GC_12,(2,2):C.GC_93,(1,1):C.GC_629,(3,1):C.GC_630,(0,0):C.GC_527,(2,0):C.GC_174})

V_155 = Vertex(name = 'V_155',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2050,(0,7):C.GC_2049,(1,0):C.GC_1483,(3,0):C.GC_1424,(0,5):C.GC_21,(2,5):C.GC_102,(1,4):C.GC_871,(3,4):C.GC_874,(1,2):C.GC_879,(3,2):C.GC_887,(1,3):C.GC_865,(3,3):C.GC_868,(1,8):C.GC_1482,(3,8):C.GC_1433,(0,1):C.GC_528,(2,1):C.GC_177})

V_156 = Vertex(name = 'V_156',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2113,(0,4):C.GC_2112,(0,2):C.GC_30,(2,2):C.GC_111,(1,1):C.GC_632,(3,1):C.GC_633,(0,0):C.GC_529,(2,0):C.GC_180})

V_157 = Vertex(name = 'V_157',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_1989,(0,4):C.GC_1988,(0,2):C.GC_13,(2,2):C.GC_94,(1,1):C.GC_635,(3,1):C.GC_636,(0,0):C.GC_536,(2,0):C.GC_175})

V_158 = Vertex(name = 'V_158',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2052,(0,4):C.GC_2051,(0,2):C.GC_22,(2,2):C.GC_103,(1,1):C.GC_638,(3,1):C.GC_639,(0,0):C.GC_537,(2,0):C.GC_178})

V_159 = Vertex(name = 'V_159',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2115,(0,7):C.GC_2114,(1,0):C.GC_1773,(3,0):C.GC_1731,(0,5):C.GC_31,(2,5):C.GC_112,(1,4):C.GC_915,(3,4):C.GC_918,(1,2):C.GC_925,(3,2):C.GC_934,(1,3):C.GC_909,(3,3):C.GC_912,(1,8):C.GC_1774,(3,8):C.GC_1740,(0,1):C.GC_538,(2,1):C.GC_181})

V_160 = Vertex(name = 'V_160',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_1991,(0,5):C.GC_1990,(1,0):C.GC_1901,(3,0):C.GC_1920,(0,3):C.GC_14,(2,3):C.GC_95,(1,2):C.GC_641,(3,2):C.GC_642,(1,6):C.GC_1907,(3,6):C.GC_1929,(0,1):C.GC_545,(2,1):C.GC_200})

V_161 = Vertex(name = 'V_161',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2054,(0,3):C.GC_2053,(0,1):C.GC_23,(2,1):C.GC_104,(0,0):C.GC_546,(2,0):C.GC_203})

V_162 = Vertex(name = 'V_162',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2117,(0,3):C.GC_2116,(0,1):C.GC_32,(2,1):C.GC_113,(0,0):C.GC_547,(2,0):C.GC_206})

V_163 = Vertex(name = 'V_163',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_1993,(0,3):C.GC_1992,(0,1):C.GC_15,(2,1):C.GC_96,(0,0):C.GC_554,(2,0):C.GC_201})

V_164 = Vertex(name = 'V_164',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2056,(0,5):C.GC_2055,(1,0):C.GC_1406,(3,0):C.GC_1425,(0,3):C.GC_24,(2,3):C.GC_105,(1,2):C.GC_641,(3,2):C.GC_642,(1,6):C.GC_1412,(3,6):C.GC_1434,(0,1):C.GC_555,(2,1):C.GC_204})

V_165 = Vertex(name = 'V_165',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2119,(0,3):C.GC_2118,(0,1):C.GC_33,(2,1):C.GC_114,(0,0):C.GC_556,(2,0):C.GC_207})

V_166 = Vertex(name = 'V_166',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_1995,(0,3):C.GC_1994,(0,1):C.GC_16,(2,1):C.GC_97,(0,0):C.GC_563,(2,0):C.GC_202})

V_167 = Vertex(name = 'V_167',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2058,(0,3):C.GC_2057,(0,1):C.GC_25,(2,1):C.GC_106,(0,0):C.GC_564,(2,0):C.GC_205})

V_168 = Vertex(name = 'V_168',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2121,(0,5):C.GC_2120,(1,0):C.GC_1713,(3,0):C.GC_1732,(0,3):C.GC_34,(2,3):C.GC_115,(1,2):C.GC_641,(3,2):C.GC_642,(1,6):C.GC_1719,(3,6):C.GC_1741,(0,1):C.GC_565,(2,1):C.GC_208})

V_169 = Vertex(name = 'V_169',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_1997,(0,5):C.GC_1996,(1,0):C.GC_1902,(3,0):C.GC_1921,(0,3):C.GC_17,(2,3):C.GC_98,(1,2):C.GC_644,(3,2):C.GC_645,(1,6):C.GC_1908,(3,6):C.GC_1930,(0,1):C.GC_572,(2,1):C.GC_227})

V_170 = Vertex(name = 'V_170',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2060,(0,3):C.GC_2059,(0,1):C.GC_26,(2,1):C.GC_107,(0,0):C.GC_573,(2,0):C.GC_230})

V_171 = Vertex(name = 'V_171',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2123,(0,3):C.GC_2122,(0,1):C.GC_35,(2,1):C.GC_116,(0,0):C.GC_574,(2,0):C.GC_233})

V_172 = Vertex(name = 'V_172',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_1999,(0,3):C.GC_1998,(0,1):C.GC_18,(2,1):C.GC_99,(0,0):C.GC_581,(2,0):C.GC_228})

V_173 = Vertex(name = 'V_173',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2062,(0,5):C.GC_2061,(1,0):C.GC_1407,(3,0):C.GC_1426,(0,3):C.GC_27,(2,3):C.GC_108,(1,2):C.GC_644,(3,2):C.GC_645,(1,6):C.GC_1413,(3,6):C.GC_1435,(0,1):C.GC_582,(2,1):C.GC_231})

V_174 = Vertex(name = 'V_174',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2125,(0,3):C.GC_2124,(0,1):C.GC_36,(2,1):C.GC_117,(0,0):C.GC_583,(2,0):C.GC_234})

V_175 = Vertex(name = 'V_175',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2001,(0,3):C.GC_2000,(0,1):C.GC_19,(2,1):C.GC_100,(0,0):C.GC_590,(2,0):C.GC_229})

V_176 = Vertex(name = 'V_176',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2064,(0,3):C.GC_2063,(0,1):C.GC_28,(2,1):C.GC_109,(0,0):C.GC_591,(2,0):C.GC_232})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2127,(0,5):C.GC_2126,(1,0):C.GC_1714,(3,0):C.GC_1733,(0,3):C.GC_37,(2,3):C.GC_118,(1,2):C.GC_644,(3,2):C.GC_645,(1,6):C.GC_1720,(3,6):C.GC_1742,(0,1):C.GC_592,(2,1):C.GC_235})

V_178 = Vertex(name = 'V_178',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2006,(0,5):C.GC_2005,(1,0):C.GC_1903,(3,0):C.GC_1922,(0,3):C.GC_38,(2,3):C.GC_119,(1,2):C.GC_647,(3,2):C.GC_648,(1,6):C.GC_1909,(3,6):C.GC_1931,(0,1):C.GC_521,(2,1):C.GC_182})

V_179 = Vertex(name = 'V_179',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2069,(0,3):C.GC_2068,(0,1):C.GC_47,(2,1):C.GC_128,(0,0):C.GC_522,(2,0):C.GC_185})

V_180 = Vertex(name = 'V_180',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2132,(0,3):C.GC_2131,(0,1):C.GC_56,(2,1):C.GC_137,(0,0):C.GC_523,(2,0):C.GC_188})

V_181 = Vertex(name = 'V_181',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2008,(0,3):C.GC_2007,(0,1):C.GC_39,(2,1):C.GC_120,(0,0):C.GC_530,(2,0):C.GC_183})

V_182 = Vertex(name = 'V_182',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2071,(0,5):C.GC_2070,(1,0):C.GC_1408,(3,0):C.GC_1427,(0,3):C.GC_48,(2,3):C.GC_129,(1,2):C.GC_647,(3,2):C.GC_648,(1,6):C.GC_1414,(3,6):C.GC_1436,(0,1):C.GC_531,(2,1):C.GC_186})

V_183 = Vertex(name = 'V_183',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2134,(0,3):C.GC_2133,(0,1):C.GC_57,(2,1):C.GC_138,(0,0):C.GC_532,(2,0):C.GC_189})

V_184 = Vertex(name = 'V_184',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2010,(0,3):C.GC_2009,(0,1):C.GC_40,(2,1):C.GC_121,(0,0):C.GC_539,(2,0):C.GC_184})

V_185 = Vertex(name = 'V_185',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2073,(0,3):C.GC_2072,(0,1):C.GC_49,(2,1):C.GC_130,(0,0):C.GC_540,(2,0):C.GC_187})

V_186 = Vertex(name = 'V_186',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2136,(0,5):C.GC_2135,(1,0):C.GC_1715,(3,0):C.GC_1734,(0,3):C.GC_58,(2,3):C.GC_139,(1,2):C.GC_647,(3,2):C.GC_648,(1,6):C.GC_1721,(3,6):C.GC_1743,(0,1):C.GC_541,(2,1):C.GC_190})

V_187 = Vertex(name = 'V_187',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2012,(0,7):C.GC_2011,(1,0):C.GC_1975,(3,0):C.GC_1923,(0,5):C.GC_41,(2,5):C.GC_122,(1,4):C.GC_835,(3,4):C.GC_838,(1,2):C.GC_841,(3,2):C.GC_848,(1,3):C.GC_829,(3,3):C.GC_832,(1,8):C.GC_1976,(3,8):C.GC_1932,(0,1):C.GC_548,(2,1):C.GC_209})

V_188 = Vertex(name = 'V_188',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2075,(0,4):C.GC_2074,(0,2):C.GC_50,(2,2):C.GC_131,(1,1):C.GC_623,(3,1):C.GC_624,(0,0):C.GC_549,(2,0):C.GC_212})

V_189 = Vertex(name = 'V_189',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2138,(0,4):C.GC_2137,(0,2):C.GC_59,(2,2):C.GC_140,(1,1):C.GC_626,(3,1):C.GC_627,(0,0):C.GC_550,(2,0):C.GC_215})

V_190 = Vertex(name = 'V_190',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2014,(0,4):C.GC_2013,(0,2):C.GC_42,(2,2):C.GC_123,(1,1):C.GC_629,(3,1):C.GC_630,(0,0):C.GC_557,(2,0):C.GC_210})

V_191 = Vertex(name = 'V_191',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2077,(0,7):C.GC_2076,(1,0):C.GC_1707,(3,0):C.GC_1428,(0,5):C.GC_51,(2,5):C.GC_132,(1,4):C.GC_872,(3,4):C.GC_875,(1,2):C.GC_880,(3,2):C.GC_888,(1,3):C.GC_866,(3,3):C.GC_869,(1,8):C.GC_1706,(3,8):C.GC_1437,(0,1):C.GC_558,(2,1):C.GC_213})

V_192 = Vertex(name = 'V_192',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2140,(0,4):C.GC_2139,(0,2):C.GC_60,(2,2):C.GC_141,(1,1):C.GC_632,(3,1):C.GC_633,(0,0):C.GC_559,(2,0):C.GC_216})

V_193 = Vertex(name = 'V_193',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2016,(0,4):C.GC_2015,(0,2):C.GC_43,(2,2):C.GC_124,(1,1):C.GC_635,(3,1):C.GC_636,(0,0):C.GC_566,(2,0):C.GC_211})

V_194 = Vertex(name = 'V_194',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2079,(0,4):C.GC_2078,(0,2):C.GC_52,(2,2):C.GC_133,(1,1):C.GC_638,(3,1):C.GC_639,(0,0):C.GC_567,(2,0):C.GC_214})

V_195 = Vertex(name = 'V_195',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2142,(0,7):C.GC_2141,(1,0):C.GC_1787,(3,0):C.GC_1735,(0,5):C.GC_61,(2,5):C.GC_142,(1,4):C.GC_916,(3,4):C.GC_919,(1,2):C.GC_926,(3,2):C.GC_935,(1,3):C.GC_910,(3,3):C.GC_913,(1,8):C.GC_1788,(3,8):C.GC_1744,(0,1):C.GC_568,(2,1):C.GC_217})

V_196 = Vertex(name = 'V_196',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2018,(0,5):C.GC_2017,(1,0):C.GC_1904,(3,0):C.GC_1924,(0,3):C.GC_44,(2,3):C.GC_125,(1,2):C.GC_650,(3,2):C.GC_651,(1,6):C.GC_1910,(3,6):C.GC_1933,(0,1):C.GC_575,(2,1):C.GC_236})

V_197 = Vertex(name = 'V_197',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2081,(0,3):C.GC_2080,(0,1):C.GC_53,(2,1):C.GC_134,(0,0):C.GC_576,(2,0):C.GC_239})

V_198 = Vertex(name = 'V_198',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2144,(0,3):C.GC_2143,(0,1):C.GC_62,(2,1):C.GC_143,(0,0):C.GC_577,(2,0):C.GC_242})

V_199 = Vertex(name = 'V_199',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2020,(0,3):C.GC_2019,(0,1):C.GC_45,(2,1):C.GC_126,(0,0):C.GC_584,(2,0):C.GC_237})

V_200 = Vertex(name = 'V_200',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2083,(0,5):C.GC_2082,(1,0):C.GC_1409,(3,0):C.GC_1429,(0,3):C.GC_54,(2,3):C.GC_135,(1,2):C.GC_650,(3,2):C.GC_651,(1,6):C.GC_1415,(3,6):C.GC_1438,(0,1):C.GC_585,(2,1):C.GC_240})

V_201 = Vertex(name = 'V_201',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2146,(0,3):C.GC_2145,(0,1):C.GC_63,(2,1):C.GC_144,(0,0):C.GC_586,(2,0):C.GC_243})

V_202 = Vertex(name = 'V_202',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2022,(0,3):C.GC_2021,(0,1):C.GC_46,(2,1):C.GC_127,(0,0):C.GC_593,(2,0):C.GC_238})

V_203 = Vertex(name = 'V_203',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2085,(0,3):C.GC_2084,(0,1):C.GC_55,(2,1):C.GC_136,(0,0):C.GC_594,(2,0):C.GC_241})

V_204 = Vertex(name = 'V_204',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2148,(0,5):C.GC_2147,(1,0):C.GC_1716,(3,0):C.GC_1736,(0,3):C.GC_64,(2,3):C.GC_145,(1,2):C.GC_650,(3,2):C.GC_651,(1,6):C.GC_1722,(3,6):C.GC_1745,(0,1):C.GC_595,(2,1):C.GC_244})

V_205 = Vertex(name = 'V_205',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2027,(0,5):C.GC_2026,(1,0):C.GC_1905,(3,0):C.GC_1925,(0,3):C.GC_65,(2,3):C.GC_146,(1,2):C.GC_653,(3,2):C.GC_654,(1,6):C.GC_1911,(3,6):C.GC_1934,(0,1):C.GC_524,(2,1):C.GC_191})

V_206 = Vertex(name = 'V_206',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2090,(0,3):C.GC_2089,(0,1):C.GC_74,(2,1):C.GC_155,(0,0):C.GC_525,(2,0):C.GC_194})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2153,(0,3):C.GC_2152,(0,1):C.GC_83,(2,1):C.GC_164,(0,0):C.GC_526,(2,0):C.GC_197})

V_208 = Vertex(name = 'V_208',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2029,(0,3):C.GC_2028,(0,1):C.GC_66,(2,1):C.GC_147,(0,0):C.GC_533,(2,0):C.GC_192})

V_209 = Vertex(name = 'V_209',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2092,(0,5):C.GC_2091,(1,0):C.GC_1410,(3,0):C.GC_1430,(0,3):C.GC_75,(2,3):C.GC_156,(1,2):C.GC_653,(3,2):C.GC_654,(1,6):C.GC_1416,(3,6):C.GC_1439,(0,1):C.GC_534,(2,1):C.GC_195})

V_210 = Vertex(name = 'V_210',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2155,(0,3):C.GC_2154,(0,1):C.GC_84,(2,1):C.GC_165,(0,0):C.GC_535,(2,0):C.GC_198})

V_211 = Vertex(name = 'V_211',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2031,(0,3):C.GC_2030,(0,1):C.GC_67,(2,1):C.GC_148,(0,0):C.GC_542,(2,0):C.GC_193})

V_212 = Vertex(name = 'V_212',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2094,(0,3):C.GC_2093,(0,1):C.GC_76,(2,1):C.GC_157,(0,0):C.GC_543,(2,0):C.GC_196})

V_213 = Vertex(name = 'V_213',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2157,(0,5):C.GC_2156,(1,0):C.GC_1717,(3,0):C.GC_1737,(0,3):C.GC_85,(2,3):C.GC_166,(1,2):C.GC_653,(3,2):C.GC_654,(1,6):C.GC_1723,(3,6):C.GC_1746,(0,1):C.GC_544,(2,1):C.GC_199})

V_214 = Vertex(name = 'V_214',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2033,(0,5):C.GC_2032,(1,0):C.GC_1906,(3,0):C.GC_1926,(0,3):C.GC_68,(2,3):C.GC_149,(1,2):C.GC_656,(3,2):C.GC_657,(1,6):C.GC_1912,(3,6):C.GC_1935,(0,1):C.GC_551,(2,1):C.GC_218})

V_215 = Vertex(name = 'V_215',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2096,(0,3):C.GC_2095,(0,1):C.GC_77,(2,1):C.GC_158,(0,0):C.GC_552,(2,0):C.GC_221})

V_216 = Vertex(name = 'V_216',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2159,(0,3):C.GC_2158,(0,1):C.GC_86,(2,1):C.GC_167,(0,0):C.GC_553,(2,0):C.GC_224})

V_217 = Vertex(name = 'V_217',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2035,(0,3):C.GC_2034,(0,1):C.GC_69,(2,1):C.GC_150,(0,0):C.GC_560,(2,0):C.GC_219})

V_218 = Vertex(name = 'V_218',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2098,(0,5):C.GC_2097,(1,0):C.GC_1411,(3,0):C.GC_1431,(0,3):C.GC_78,(2,3):C.GC_159,(1,2):C.GC_656,(3,2):C.GC_657,(1,6):C.GC_1417,(3,6):C.GC_1440,(0,1):C.GC_561,(2,1):C.GC_222})

V_219 = Vertex(name = 'V_219',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2161,(0,3):C.GC_2160,(0,1):C.GC_87,(2,1):C.GC_168,(0,0):C.GC_562,(2,0):C.GC_225})

V_220 = Vertex(name = 'V_220',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2037,(0,3):C.GC_2036,(0,1):C.GC_70,(2,1):C.GC_151,(0,0):C.GC_569,(2,0):C.GC_220})

V_221 = Vertex(name = 'V_221',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_2100,(0,3):C.GC_2099,(0,1):C.GC_79,(2,1):C.GC_160,(0,0):C.GC_570,(2,0):C.GC_223})

V_222 = Vertex(name = 'V_222',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,4):C.GC_2163,(0,5):C.GC_2162,(1,0):C.GC_1718,(3,0):C.GC_1738,(0,3):C.GC_88,(2,3):C.GC_169,(1,2):C.GC_656,(3,2):C.GC_657,(1,6):C.GC_1724,(3,6):C.GC_1747,(0,1):C.GC_571,(2,1):C.GC_226})

V_223 = Vertex(name = 'V_223',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2039,(0,7):C.GC_2038,(1,0):C.GC_1959,(3,0):C.GC_1927,(0,5):C.GC_71,(2,5):C.GC_152,(1,4):C.GC_836,(3,4):C.GC_839,(1,2):C.GC_842,(3,2):C.GC_849,(1,3):C.GC_830,(3,3):C.GC_833,(1,8):C.GC_1960,(3,8):C.GC_1936,(0,1):C.GC_578,(2,1):C.GC_245})

V_224 = Vertex(name = 'V_224',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2102,(0,4):C.GC_2101,(0,2):C.GC_80,(2,2):C.GC_161,(1,1):C.GC_623,(3,1):C.GC_624,(0,0):C.GC_579,(2,0):C.GC_248})

V_225 = Vertex(name = 'V_225',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2165,(0,4):C.GC_2164,(0,2):C.GC_89,(2,2):C.GC_170,(1,1):C.GC_626,(3,1):C.GC_627,(0,0):C.GC_580,(2,0):C.GC_251})

V_226 = Vertex(name = 'V_226',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2041,(0,4):C.GC_2040,(0,2):C.GC_72,(2,2):C.GC_153,(1,1):C.GC_629,(3,1):C.GC_630,(0,0):C.GC_587,(2,0):C.GC_246})

V_227 = Vertex(name = 'V_227',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2104,(0,7):C.GC_2103,(1,0):C.GC_1464,(3,0):C.GC_1432,(0,5):C.GC_81,(2,5):C.GC_162,(1,4):C.GC_873,(3,4):C.GC_876,(1,2):C.GC_881,(3,2):C.GC_889,(1,3):C.GC_867,(3,3):C.GC_870,(1,8):C.GC_1465,(3,8):C.GC_1441,(0,1):C.GC_588,(2,1):C.GC_249})

V_228 = Vertex(name = 'V_228',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2167,(0,4):C.GC_2166,(0,2):C.GC_90,(2,2):C.GC_171,(1,1):C.GC_632,(3,1):C.GC_633,(0,0):C.GC_589,(2,0):C.GC_252})

V_229 = Vertex(name = 'V_229',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2043,(0,4):C.GC_2042,(0,2):C.GC_73,(2,2):C.GC_154,(1,1):C.GC_635,(3,1):C.GC_636,(0,0):C.GC_596,(2,0):C.GC_247})

V_230 = Vertex(name = 'V_230',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,3):C.GC_2106,(0,4):C.GC_2105,(0,2):C.GC_82,(2,2):C.GC_163,(1,1):C.GC_638,(3,1):C.GC_639,(0,0):C.GC_597,(2,0):C.GC_250})

V_231 = Vertex(name = 'V_231',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_2169,(0,7):C.GC_2168,(1,0):C.GC_1771,(3,0):C.GC_1739,(0,5):C.GC_91,(2,5):C.GC_172,(1,4):C.GC_917,(3,4):C.GC_920,(1,2):C.GC_927,(3,2):C.GC_936,(1,3):C.GC_911,(3,3):C.GC_914,(1,8):C.GC_1772,(3,8):C.GC_1748,(0,1):C.GC_598,(2,1):C.GC_253})

V_232 = Vertex(name = 'V_232',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_859,(0,11):C.GC_1968,(0,9):C.GC_1966,(0,10):C.GC_1966,(0,6):C.GC_1964,(0,1):C.GC_864,(0,2):C.GC_858,(0,3):C.GC_857,(0,7):C.GC_1967,(0,4):C.GC_1965,(0,5):C.GC_1965,(0,0):C.GC_1963})

V_233 = Vertex(name = 'V_233',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_258,(0,0):C.GC_625})

V_234 = Vertex(name = 'V_234',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_263,(0,0):C.GC_628})

V_235 = Vertex(name = 'V_235',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_268,(0,0):C.GC_631})

V_236 = Vertex(name = 'V_236',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_903,(0,11):C.GC_1584,(0,9):C.GC_1582,(0,10):C.GC_1582,(0,6):C.GC_1580,(0,1):C.GC_908,(0,2):C.GC_902,(0,3):C.GC_901,(0,7):C.GC_1583,(0,4):C.GC_1581,(0,5):C.GC_1581,(0,0):C.GC_1579})

V_237 = Vertex(name = 'V_237',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_273,(0,0):C.GC_634})

V_238 = Vertex(name = 'V_238',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_278,(0,0):C.GC_637})

V_239 = Vertex(name = 'V_239',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_283,(0,0):C.GC_640})

V_240 = Vertex(name = 'V_240',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_954,(0,11):C.GC_1780,(0,9):C.GC_1778,(0,10):C.GC_1778,(0,6):C.GC_1776,(0,1):C.GC_959,(0,2):C.GC_953,(0,3):C.GC_952,(0,7):C.GC_1779,(0,4):C.GC_1777,(0,5):C.GC_1777,(0,0):C.GC_1775})

V_241 = Vertex(name = 'V_241',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_859,(0,11):C.GC_1974,(0,9):C.GC_1972,(0,10):C.GC_1972,(0,6):C.GC_1970,(0,1):C.GC_864,(0,2):C.GC_858,(0,3):C.GC_857,(0,7):C.GC_1973,(0,4):C.GC_1971,(0,5):C.GC_1971,(0,0):C.GC_1969})

V_242 = Vertex(name = 'V_242',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_258,(0,0):C.GC_625})

V_243 = Vertex(name = 'V_243',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_263,(0,0):C.GC_628})

V_244 = Vertex(name = 'V_244',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_268,(0,0):C.GC_631})

V_245 = Vertex(name = 'V_245',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_903,(0,11):C.GC_1687,(0,9):C.GC_1685,(0,10):C.GC_1685,(0,6):C.GC_1683,(0,1):C.GC_908,(0,2):C.GC_902,(0,3):C.GC_901,(0,7):C.GC_1686,(0,4):C.GC_1684,(0,5):C.GC_1684,(0,0):C.GC_1682})

V_246 = Vertex(name = 'V_246',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_273,(0,0):C.GC_634})

V_247 = Vertex(name = 'V_247',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_278,(0,0):C.GC_637})

V_248 = Vertex(name = 'V_248',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_283,(0,0):C.GC_640})

V_249 = Vertex(name = 'V_249',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_954,(0,11):C.GC_1786,(0,9):C.GC_1784,(0,10):C.GC_1784,(0,6):C.GC_1782,(0,1):C.GC_959,(0,2):C.GC_953,(0,3):C.GC_952,(0,7):C.GC_1785,(0,4):C.GC_1783,(0,5):C.GC_1783,(0,0):C.GC_1781})

V_250 = Vertex(name = 'V_250',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_859,(0,11):C.GC_1982,(0,9):C.GC_1980,(0,10):C.GC_1980,(0,6):C.GC_1978,(0,1):C.GC_864,(0,2):C.GC_858,(0,3):C.GC_857,(0,7):C.GC_1981,(0,4):C.GC_1979,(0,5):C.GC_1979,(0,0):C.GC_1977})

V_251 = Vertex(name = 'V_251',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_258,(0,0):C.GC_625})

V_252 = Vertex(name = 'V_252',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_263,(0,0):C.GC_628})

V_253 = Vertex(name = 'V_253',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_268,(0,0):C.GC_631})

V_254 = Vertex(name = 'V_254',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_903,(0,11):C.GC_1889,(0,9):C.GC_1887,(0,10):C.GC_1887,(0,6):C.GC_1885,(0,1):C.GC_908,(0,2):C.GC_902,(0,3):C.GC_901,(0,7):C.GC_1888,(0,4):C.GC_1886,(0,5):C.GC_1886,(0,0):C.GC_1884})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_273,(0,0):C.GC_634})

V_256 = Vertex(name = 'V_256',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_278,(0,0):C.GC_637})

V_257 = Vertex(name = 'V_257',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_283,(0,0):C.GC_640})

V_258 = Vertex(name = 'V_258',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_954,(0,11):C.GC_1899,(0,9):C.GC_1897,(0,10):C.GC_1897,(0,6):C.GC_1895,(0,1):C.GC_959,(0,2):C.GC_953,(0,3):C.GC_952,(0,7):C.GC_1898,(0,4):C.GC_1896,(0,5):C.GC_1896,(0,0):C.GC_1894})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV3 ],
               couplings = {(0,0):C.GC_742,(0,1):C.GC_727})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_1346})

V_261 = Vertex(name = 'V_261',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV6, L.FFV7 ],
               couplings = {(0,4):C.GC_1,(0,3):C.GC_1374,(0,0):C.GC_1360,(0,2):C.GC_1242,(0,1):C.GC_1269})

V_262 = Vertex(name = 'V_262',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1245,(0,0):C.GC_1272})

V_263 = Vertex(name = 'V_263',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1248,(0,0):C.GC_1275})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1251,(0,0):C.GC_1278})

V_265 = Vertex(name = 'V_265',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV6, L.FFV7 ],
               couplings = {(0,4):C.GC_1,(0,3):C.GC_1374,(0,0):C.GC_1360,(0,2):C.GC_1254,(0,1):C.GC_1281})

V_266 = Vertex(name = 'V_266',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1257,(0,0):C.GC_1284})

V_267 = Vertex(name = 'V_267',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1260,(0,0):C.GC_1287})

V_268 = Vertex(name = 'V_268',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1263,(0,0):C.GC_1290})

V_269 = Vertex(name = 'V_269',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV6, L.FFV7 ],
               couplings = {(0,4):C.GC_1,(0,3):C.GC_1374,(0,0):C.GC_1360,(0,2):C.GC_1266,(0,1):C.GC_1293})

V_270 = Vertex(name = 'V_270',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV13, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_1375,(0,0):C.GC_1360,(0,1):C.GC_1574})

V_271 = Vertex(name = 'V_271',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV13, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_1375,(0,0):C.GC_1360,(0,1):C.GC_1677})

V_272 = Vertex(name = 'V_272',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV13, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_1375,(0,0):C.GC_1360,(0,1):C.GC_1879})

V_273 = Vertex(name = 'V_273',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV13, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,4):C.GC_2,(0,5):C.GC_1374,(0,0):C.GC_1359,(0,3):C.GC_1237,(0,2):C.GC_1957,(0,1):C.GC_1234})

V_274 = Vertex(name = 'V_274',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV13, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,4):C.GC_2,(0,5):C.GC_1374,(0,0):C.GC_1359,(0,3):C.GC_1238,(0,2):C.GC_1462,(0,1):C.GC_1235})

V_275 = Vertex(name = 'V_275',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV13, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,4):C.GC_2,(0,5):C.GC_1374,(0,0):C.GC_1359,(0,3):C.GC_1239,(0,2):C.GC_1769,(0,1):C.GC_1236})

V_276 = Vertex(name = 'V_276',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1376})

V_277 = Vertex(name = 'V_277',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1376})

V_278 = Vertex(name = 'V_278',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1376})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_6,(0,1):C.GC_1033,(0,0):C.GC_1060})

V_280 = Vertex(name = 'V_280',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1036,(0,0):C.GC_1063})

V_281 = Vertex(name = 'V_281',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1039,(0,0):C.GC_1066})

V_282 = Vertex(name = 'V_282',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1042,(0,0):C.GC_1069})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_6,(0,1):C.GC_1045,(0,0):C.GC_1072})

V_284 = Vertex(name = 'V_284',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1048,(0,0):C.GC_1075})

V_285 = Vertex(name = 'V_285',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1051,(0,0):C.GC_1078})

V_286 = Vertex(name = 'V_286',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_1054,(0,0):C.GC_1081})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_6,(0,1):C.GC_1057,(0,0):C.GC_1084})

V_288 = Vertex(name = 'V_288',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV13, L.FFV4, L.FFV7 ],
               couplings = {(0,3):C.GC_6,(0,2):C.GC_977,(0,1):C.GC_1913,(0,0):C.GC_971})

V_289 = Vertex(name = 'V_289',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV13, L.FFV4, L.FFV7 ],
               couplings = {(0,3):C.GC_6,(0,2):C.GC_979,(0,1):C.GC_1418,(0,0):C.GC_973})

V_290 = Vertex(name = 'V_290',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV13, L.FFV4, L.FFV7 ],
               couplings = {(0,3):C.GC_6,(0,2):C.GC_981,(0,1):C.GC_1725,(0,0):C.GC_975})

V_291 = Vertex(name = 'V_291',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1087,(0,1):C.GC_1471,(0,0):C.GC_730,(0,3):C.GC_1014})

V_292 = Vertex(name = 'V_292',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1337})

V_293 = Vertex(name = 'V_293',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1090,(0,0):C.GC_731,(0,2):C.GC_1015})

V_294 = Vertex(name = 'V_294',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1338})

V_295 = Vertex(name = 'V_295',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1093,(0,0):C.GC_732,(0,2):C.GC_1016})

V_296 = Vertex(name = 'V_296',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1339})

V_297 = Vertex(name = 'V_297',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1096,(0,0):C.GC_733,(0,2):C.GC_1017})

V_298 = Vertex(name = 'V_298',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1340})

V_299 = Vertex(name = 'V_299',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1099,(0,1):C.GC_1695,(0,0):C.GC_734,(0,3):C.GC_1018})

V_300 = Vertex(name = 'V_300',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1341})

V_301 = Vertex(name = 'V_301',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1102,(0,0):C.GC_735,(0,2):C.GC_1019})

V_302 = Vertex(name = 'V_302',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1342})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1105,(0,0):C.GC_736,(0,2):C.GC_1020})

V_304 = Vertex(name = 'V_304',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1343})

V_305 = Vertex(name = 'V_305',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1108,(0,0):C.GC_737,(0,2):C.GC_1021})

V_306 = Vertex(name = 'V_306',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1344})

V_307 = Vertex(name = 'V_307',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1111,(0,1):C.GC_1394,(0,0):C.GC_738,(0,3):C.GC_1022})

V_308 = Vertex(name = 'V_308',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1345})

V_309 = Vertex(name = 'V_309',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_404,(0,3):C.GC_1468,(0,2):C.GC_993,(0,0):C.GC_1186})

V_310 = Vertex(name = 'V_310',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_405,(0,2):C.GC_994,(0,0):C.GC_1187})

V_311 = Vertex(name = 'V_311',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_406,(0,2):C.GC_995,(0,0):C.GC_1188})

V_312 = Vertex(name = 'V_312',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_407,(0,2):C.GC_996,(0,0):C.GC_1189})

V_313 = Vertex(name = 'V_313',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_408,(0,3):C.GC_1692,(0,2):C.GC_997,(0,0):C.GC_1190})

V_314 = Vertex(name = 'V_314',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_409,(0,2):C.GC_998,(0,0):C.GC_1191})

V_315 = Vertex(name = 'V_315',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_410,(0,2):C.GC_999,(0,0):C.GC_1192})

V_316 = Vertex(name = 'V_316',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_411,(0,2):C.GC_1000,(0,0):C.GC_1193})

V_317 = Vertex(name = 'V_317',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_412,(0,3):C.GC_1391,(0,2):C.GC_1001,(0,0):C.GC_1194})

V_318 = Vertex(name = 'V_318',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_1489,(0,0):C.GC_729})

V_319 = Vertex(name = 'V_319',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_320 = Vertex(name = 'V_320',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_1592,(0,0):C.GC_729})

V_321 = Vertex(name = 'V_321',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_322 = Vertex(name = 'V_322',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_1794,(0,0):C.GC_729})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_324 = Vertex(name = 'V_324',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS8 ],
               couplings = {(0,1):C.GC_1486,(0,0):C.GC_990})

V_325 = Vertex(name = 'V_325',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS8 ],
               couplings = {(0,1):C.GC_1589,(0,0):C.GC_990})

V_326 = Vertex(name = 'V_326',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS8 ],
               couplings = {(0,1):C.GC_1791,(0,0):C.GC_990})

V_327 = Vertex(name = 'V_327',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_1469,(0,3):C.GC_413,(0,2):C.GC_1002,(0,0):C.GC_2002})

V_328 = Vertex(name = 'V_328',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_414,(0,1):C.GC_1003,(0,0):C.GC_2065})

V_329 = Vertex(name = 'V_329',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_415,(0,1):C.GC_1004,(0,0):C.GC_2128})

V_330 = Vertex(name = 'V_330',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_416,(0,1):C.GC_1005,(0,0):C.GC_2023})

V_331 = Vertex(name = 'V_331',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_1693,(0,3):C.GC_417,(0,2):C.GC_1006,(0,0):C.GC_2086})

V_332 = Vertex(name = 'V_332',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_418,(0,1):C.GC_1007,(0,0):C.GC_2149})

V_333 = Vertex(name = 'V_333',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_419,(0,1):C.GC_1008,(0,0):C.GC_2044})

V_334 = Vertex(name = 'V_334',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS8 ],
               couplings = {(0,2):C.GC_420,(0,1):C.GC_1009,(0,0):C.GC_2107})

V_335 = Vertex(name = 'V_335',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS8 ],
               couplings = {(0,1):C.GC_1392,(0,3):C.GC_421,(0,2):C.GC_1010,(0,0):C.GC_2170})

V_336 = Vertex(name = 'V_336',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,4):C.GC_1472,(0,2):C.GC_1115,(0,3):C.GC_1470,(0,1):C.GC_1114,(0,0):C.GC_2003,(0,5):C.GC_1023})

V_337 = Vertex(name = 'V_337',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1983})

V_338 = Vertex(name = 'V_338',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1119,(0,1):C.GC_1118,(0,0):C.GC_2066,(0,3):C.GC_1024})

V_339 = Vertex(name = 'V_339',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2046})

V_340 = Vertex(name = 'V_340',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1123,(0,1):C.GC_1122,(0,0):C.GC_2129,(0,3):C.GC_1025})

V_341 = Vertex(name = 'V_341',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2109})

V_342 = Vertex(name = 'V_342',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1127,(0,1):C.GC_1126,(0,0):C.GC_2024,(0,3):C.GC_1026})

V_343 = Vertex(name = 'V_343',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2004})

V_344 = Vertex(name = 'V_344',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,4):C.GC_1696,(0,2):C.GC_1131,(0,3):C.GC_1694,(0,1):C.GC_1130,(0,0):C.GC_2087,(0,5):C.GC_1027})

V_345 = Vertex(name = 'V_345',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2067})

V_346 = Vertex(name = 'V_346',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1135,(0,1):C.GC_1134,(0,0):C.GC_2150,(0,3):C.GC_1028})

V_347 = Vertex(name = 'V_347',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2130})

V_348 = Vertex(name = 'V_348',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1139,(0,1):C.GC_1138,(0,0):C.GC_2045,(0,3):C.GC_1029})

V_349 = Vertex(name = 'V_349',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2025})

V_350 = Vertex(name = 'V_350',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV5 ],
               couplings = {(0,2):C.GC_1143,(0,1):C.GC_1142,(0,0):C.GC_2108,(0,3):C.GC_1030})

V_351 = Vertex(name = 'V_351',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2088})

V_352 = Vertex(name = 'V_352',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,4):C.GC_1395,(0,2):C.GC_1147,(0,3):C.GC_1393,(0,1):C.GC_1146,(0,0):C.GC_2171,(0,5):C.GC_1031})

V_353 = Vertex(name = 'V_353',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2151})

V_354 = Vertex(name = 'V_354',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1489,(0,1):C.GC_1488,(0,0):C.GC_729})

V_355 = Vertex(name = 'V_355',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_356 = Vertex(name = 'V_356',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1592,(0,1):C.GC_1591,(0,0):C.GC_729})

V_357 = Vertex(name = 'V_357',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_358 = Vertex(name = 'V_358',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1794,(0,1):C.GC_1793,(0,0):C.GC_729})

V_359 = Vertex(name = 'V_359',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1336})

V_360 = Vertex(name = 'V_360',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1486,(0,1):C.GC_1485,(0,0):C.GC_990})

V_361 = Vertex(name = 'V_361',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1589,(0,1):C.GC_1588,(0,0):C.GC_990})

V_362 = Vertex(name = 'V_362',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1791,(0,1):C.GC_1790,(0,0):C.GC_990})

V_363 = Vertex(name = 'V_363',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_749,(0,5):C.GC_1368,(0,4):C.GC_1240,(0,2):C.GC_1267,(0,3):C.GC_1241,(0,1):C.GC_1268})

V_364 = Vertex(name = 'V_364',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1365,(0,1):C.GC_743})

V_365 = Vertex(name = 'V_365',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1353,(0,4):C.GC_1243,(0,2):C.GC_1270,(0,3):C.GC_1244,(0,1):C.GC_1271})

V_366 = Vertex(name = 'V_366',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1354,(0,4):C.GC_1246,(0,2):C.GC_1273,(0,3):C.GC_1247,(0,1):C.GC_1274})

V_367 = Vertex(name = 'V_367',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1355,(0,4):C.GC_1249,(0,2):C.GC_1276,(0,3):C.GC_1250,(0,1):C.GC_1277})

V_368 = Vertex(name = 'V_368',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_749,(0,5):C.GC_1369,(0,4):C.GC_1252,(0,2):C.GC_1279,(0,3):C.GC_1253,(0,1):C.GC_1280})

V_369 = Vertex(name = 'V_369',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1366,(0,1):C.GC_743})

V_370 = Vertex(name = 'V_370',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1356,(0,4):C.GC_1255,(0,2):C.GC_1282,(0,3):C.GC_1256,(0,1):C.GC_1283})

V_371 = Vertex(name = 'V_371',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1357,(0,4):C.GC_1258,(0,2):C.GC_1285,(0,3):C.GC_1259,(0,1):C.GC_1286})

V_372 = Vertex(name = 'V_372',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1358,(0,4):C.GC_1261,(0,2):C.GC_1288,(0,3):C.GC_1262,(0,1):C.GC_1289})

V_373 = Vertex(name = 'V_373',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_749,(0,5):C.GC_1370,(0,4):C.GC_1264,(0,2):C.GC_1291,(0,3):C.GC_1265,(0,1):C.GC_1292})

V_374 = Vertex(name = 'V_374',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1367,(0,1):C.GC_743})

V_375 = Vertex(name = 'V_375',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1307,(0,3):C.GC_1306,(0,2):C.GC_752,(0,5):C.GC_788,(0,1):C.GC_753,(0,4):C.GC_789})

V_376 = Vertex(name = 'V_376',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1300,(0,2):C.GC_756,(0,4):C.GC_792,(0,1):C.GC_757,(0,3):C.GC_793})

V_377 = Vertex(name = 'V_377',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1301,(0,2):C.GC_760,(0,4):C.GC_796,(0,1):C.GC_761,(0,3):C.GC_797})

V_378 = Vertex(name = 'V_378',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1302,(0,2):C.GC_764,(0,4):C.GC_800,(0,1):C.GC_765,(0,3):C.GC_801})

V_379 = Vertex(name = 'V_379',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1309,(0,3):C.GC_1308,(0,2):C.GC_768,(0,5):C.GC_804,(0,1):C.GC_769,(0,4):C.GC_805})

V_380 = Vertex(name = 'V_380',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1303,(0,2):C.GC_772,(0,4):C.GC_808,(0,1):C.GC_773,(0,3):C.GC_809})

V_381 = Vertex(name = 'V_381',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1304,(0,2):C.GC_776,(0,4):C.GC_812,(0,1):C.GC_777,(0,3):C.GC_813})

V_382 = Vertex(name = 'V_382',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1305,(0,2):C.GC_780,(0,4):C.GC_816,(0,1):C.GC_781,(0,3):C.GC_817})

V_383 = Vertex(name = 'V_383',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1311,(0,3):C.GC_1310,(0,2):C.GC_784,(0,5):C.GC_820,(0,1):C.GC_785,(0,4):C.GC_821})

V_384 = Vertex(name = 'V_384',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_751,(0,5):C.GC_1373,(0,4):C.GC_1572,(0,2):C.GC_1572,(0,3):C.GC_1573,(0,1):C.GC_1573})

V_385 = Vertex(name = 'V_385',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1372,(0,1):C.GC_745})

V_386 = Vertex(name = 'V_386',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_751,(0,5):C.GC_1373,(0,4):C.GC_1675,(0,2):C.GC_1675,(0,3):C.GC_1676,(0,1):C.GC_1676})

V_387 = Vertex(name = 'V_387',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1372,(0,1):C.GC_745})

V_388 = Vertex(name = 'V_388',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_751,(0,5):C.GC_1373,(0,4):C.GC_1877,(0,2):C.GC_1877,(0,3):C.GC_1878,(0,1):C.GC_1878})

V_389 = Vertex(name = 'V_389',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1372,(0,1):C.GC_745})

V_390 = Vertex(name = 'V_390',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1233,(0,3):C.GC_1231,(0,2):C.GC_1568,(0,5):C.GC_1568,(0,1):C.GC_1569,(0,4):C.GC_1569})

V_391 = Vertex(name = 'V_391',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1233,(0,3):C.GC_1231,(0,2):C.GC_1671,(0,5):C.GC_1671,(0,1):C.GC_1672,(0,4):C.GC_1672})

V_392 = Vertex(name = 'V_392',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1233,(0,3):C.GC_1231,(0,2):C.GC_1873,(0,5):C.GC_1873,(0,1):C.GC_1874,(0,4):C.GC_1874})

V_393 = Vertex(name = 'V_393',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1317,(0,3):C.GC_1316,(0,2):C.GC_1938,(0,5):C.GC_1937,(0,1):C.GC_1940,(0,4):C.GC_1939})

V_394 = Vertex(name = 'V_394',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1294})

V_395 = Vertex(name = 'V_395',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1295})

V_396 = Vertex(name = 'V_396',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1296})

V_397 = Vertex(name = 'V_397',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1319,(0,3):C.GC_1318,(0,2):C.GC_1443,(0,5):C.GC_1442,(0,1):C.GC_1445,(0,4):C.GC_1444})

V_398 = Vertex(name = 'V_398',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1297})

V_399 = Vertex(name = 'V_399',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1298})

V_400 = Vertex(name = 'V_400',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1299})

V_401 = Vertex(name = 'V_401',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_1321,(0,3):C.GC_1320,(0,2):C.GC_1750,(0,5):C.GC_1749,(0,1):C.GC_1752,(0,4):C.GC_1751})

V_402 = Vertex(name = 'V_402',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_748,(0,5):C.GC_1379,(0,4):C.GC_1954,(0,2):C.GC_1953,(0,3):C.GC_1956,(0,1):C.GC_1955})

V_403 = Vertex(name = 'V_403',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1380,(0,1):C.GC_744})

V_404 = Vertex(name = 'V_404',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1347})

V_405 = Vertex(name = 'V_405',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1348})

V_406 = Vertex(name = 'V_406',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1349})

V_407 = Vertex(name = 'V_407',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_748,(0,5):C.GC_1381,(0,4):C.GC_1459,(0,2):C.GC_1458,(0,3):C.GC_1461,(0,1):C.GC_1460})

V_408 = Vertex(name = 'V_408',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1382,(0,1):C.GC_744})

V_409 = Vertex(name = 'V_409',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1350})

V_410 = Vertex(name = 'V_410',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1351})

V_411 = Vertex(name = 'V_411',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1352})

V_412 = Vertex(name = 'V_412',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_748,(0,5):C.GC_1383,(0,4):C.GC_1766,(0,2):C.GC_1765,(0,3):C.GC_1768,(0,1):C.GC_1767})

V_413 = Vertex(name = 'V_413',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_1384,(0,1):C.GC_744})

V_414 = Vertex(name = 'V_414',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_750})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1371})

V_416 = Vertex(name = 'V_416',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_750})

V_417 = Vertex(name = 'V_417',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1371})

V_418 = Vertex(name = 'V_418',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_750})

V_419 = Vertex(name = 'V_419',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1371})

V_420 = Vertex(name = 'V_420',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1232})

V_421 = Vertex(name = 'V_421',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1232})

V_422 = Vertex(name = 'V_422',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1232})

V_423 = Vertex(name = 'V_423',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_669,(0,7):C.GC_668,(0,0):C.GC_662,(2,0):C.GC_666,(1,3):C.GC_660,(3,3):C.GC_664,(1,1):C.GC_661,(3,1):C.GC_665,(1,2):C.GC_659,(0,4):C.GC_663,(2,4):C.GC_667,(0,5):C.GC_659})

V_424 = Vertex(name = 'V_424',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_457,(0,3):C.GC_453,(1,0):C.GC_430,(3,0):C.GC_432,(0,1):C.GC_448,(2,1):C.GC_451})

V_425 = Vertex(name = 'V_425',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_469,(0,3):C.GC_465,(1,0):C.GC_438,(3,0):C.GC_440,(0,1):C.GC_460,(2,1):C.GC_463})

V_426 = Vertex(name = 'V_426',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_478,(0,3):C.GC_480,(0,0):C.GC_423,(2,0):C.GC_425,(1,1):C.GC_471,(3,1):C.GC_474})

V_427 = Vertex(name = 'V_427',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_688,(0,5):C.GC_689,(1,2):C.GC_673,(2,2):C.GC_674,(1,0):C.GC_678,(2,0):C.GC_683,(1,1):C.GC_675,(0,3):C.GC_676})

V_428 = Vertex(name = 'V_428',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_488,(0,2):C.GC_491,(1,0):C.GC_482,(2,0):C.GC_485})

V_429 = Vertex(name = 'V_429',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_502,(0,3):C.GC_504,(0,0):C.GC_427,(2,0):C.GC_429,(1,1):C.GC_495,(3,1):C.GC_498})

V_430 = Vertex(name = 'V_430',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_512,(0,2):C.GC_515,(1,0):C.GC_506,(2,0):C.GC_509})

V_431 = Vertex(name = 'V_431',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_716,(0,5):C.GC_718,(1,2):C.GC_695,(2,2):C.GC_697,(1,0):C.GC_704,(2,0):C.GC_710,(1,1):C.GC_699,(0,3):C.GC_701})

V_432 = Vertex(name = 'V_432',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_456,(0,3):C.GC_454,(1,0):C.GC_431,(3,0):C.GC_433,(0,1):C.GC_447,(2,1):C.GC_450})

V_433 = Vertex(name = 'V_433',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_467,(0,2):C.GC_464,(0,0):C.GC_458,(2,0):C.GC_461})

V_434 = Vertex(name = 'V_434',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_452,(0,2):C.GC_455,(1,0):C.GC_446,(2,0):C.GC_449})

V_435 = Vertex(name = 'V_435',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_468,(0,3):C.GC_466,(1,0):C.GC_439,(3,0):C.GC_441,(0,1):C.GC_459,(2,1):C.GC_462})

V_436 = Vertex(name = 'V_436',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_477,(0,3):C.GC_481,(0,0):C.GC_422,(2,0):C.GC_424,(1,1):C.GC_472,(3,1):C.GC_475})

V_437 = Vertex(name = 'V_437',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_503,(0,2):C.GC_500,(0,0):C.GC_494,(2,0):C.GC_497})

V_438 = Vertex(name = 'V_438',
               particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_476,(0,2):C.GC_479,(1,0):C.GC_470,(2,0):C.GC_473})

V_439 = Vertex(name = 'V_439',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_691,(0,7):C.GC_690,(0,0):C.GC_681,(2,0):C.GC_686,(1,3):C.GC_679,(3,3):C.GC_684,(1,1):C.GC_680,(3,1):C.GC_685,(1,2):C.GC_677,(0,4):C.GC_682,(2,4):C.GC_687,(0,5):C.GC_677})

V_440 = Vertex(name = 'V_440',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_493,(0,3):C.GC_489,(1,0):C.GC_442,(3,0):C.GC_444,(0,1):C.GC_484,(2,1):C.GC_487})

V_441 = Vertex(name = 'V_441',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_514,(0,3):C.GC_516,(0,0):C.GC_435,(2,0):C.GC_437,(1,1):C.GC_507,(3,1):C.GC_510})

V_442 = Vertex(name = 'V_442',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_717,(0,5):C.GC_719,(1,2):C.GC_696,(2,2):C.GC_698,(1,0):C.GC_705,(2,0):C.GC_711,(1,1):C.GC_700,(0,3):C.GC_702})

V_443 = Vertex(name = 'V_443',
               particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_492,(0,3):C.GC_490,(1,0):C.GC_443,(3,0):C.GC_445,(0,1):C.GC_483,(2,1):C.GC_486})

V_444 = Vertex(name = 'V_444',
               particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_501,(0,3):C.GC_505,(0,0):C.GC_426,(2,0):C.GC_428,(1,1):C.GC_496,(3,1):C.GC_499})

V_445 = Vertex(name = 'V_445',
               particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_513,(0,3):C.GC_517,(0,0):C.GC_434,(2,0):C.GC_436,(1,1):C.GC_508,(3,1):C.GC_511})

V_446 = Vertex(name = 'V_446',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_721,(0,7):C.GC_720,(0,0):C.GC_708,(2,0):C.GC_714,(1,3):C.GC_706,(3,3):C.GC_712,(1,1):C.GC_707,(3,1):C.GC_713,(1,2):C.GC_703,(0,4):C.GC_709,(2,4):C.GC_715,(0,5):C.GC_703})

V_447 = Vertex(name = 'V_447',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_10,(0,7):C.GC_10,(0,0):C.GC_605,(0,3):C.GC_605,(0,1):C.GC_605,(0,2):C.GC_599,(0,4):C.GC_605,(0,5):C.GC_599})

V_448 = Vertex(name = 'V_448',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_606,(0,4):C.GC_607,(0,2):C.GC_605,(0,0):C.GC_605,(0,1):C.GC_599})

V_449 = Vertex(name = 'V_449',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_606,(0,4):C.GC_607,(0,2):C.GC_605,(0,0):C.GC_605,(0,1):C.GC_599})

V_450 = Vertex(name = 'V_450',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_10,(0,7):C.GC_10,(0,0):C.GC_605,(0,3):C.GC_605,(0,1):C.GC_605,(0,2):C.GC_599,(0,4):C.GC_605,(0,5):C.GC_599})

V_451 = Vertex(name = 'V_451',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_606,(0,4):C.GC_607,(0,2):C.GC_605,(0,0):C.GC_605,(0,1):C.GC_599})

V_452 = Vertex(name = 'V_452',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_10,(0,7):C.GC_10,(0,0):C.GC_605,(0,3):C.GC_605,(0,1):C.GC_605,(0,2):C.GC_599,(0,4):C.GC_605,(0,5):C.GC_599})

V_453 = Vertex(name = 'V_453',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_855,(0,7):C.GC_856,(0,0):C.GC_843,(2,0):C.GC_850,(1,3):C.GC_845,(3,3):C.GC_852,(1,1):C.GC_846,(3,1):C.GC_853,(1,2):C.GC_854,(0,4):C.GC_844,(2,4):C.GC_851,(0,5):C.GC_854})

V_454 = Vertex(name = 'V_454',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_331,(0,3):C.GC_327,(1,0):C.GC_254,(3,0):C.GC_256,(0,1):C.GC_322,(2,1):C.GC_325})

V_455 = Vertex(name = 'V_455',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_345,(0,3):C.GC_341,(1,0):C.GC_259,(3,0):C.GC_261,(0,1):C.GC_336,(2,1):C.GC_339})

V_456 = Vertex(name = 'V_456',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_358,(0,3):C.GC_356,(0,0):C.GC_349,(2,0):C.GC_352,(1,1):C.GC_265,(3,1):C.GC_267})

V_457 = Vertex(name = 'V_457',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_897,(0,5):C.GC_898,(1,2):C.GC_877,(2,2):C.GC_878,(1,0):C.GC_882,(2,0):C.GC_890,(1,1):C.GC_895,(0,3):C.GC_895})

V_458 = Vertex(name = 'V_458',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_368,(0,2):C.GC_371,(1,0):C.GC_362,(2,0):C.GC_365})

V_459 = Vertex(name = 'V_459',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_386,(0,3):C.GC_384,(0,0):C.GC_377,(2,0):C.GC_380,(1,1):C.GC_275,(3,1):C.GC_277})

V_460 = Vertex(name = 'V_460',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_396,(0,2):C.GC_399,(1,0):C.GC_390,(2,0):C.GC_393})

V_461 = Vertex(name = 'V_461',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_946,(0,5):C.GC_948,(1,2):C.GC_921,(2,2):C.GC_923,(1,0):C.GC_928,(2,0):C.GC_937,(1,1):C.GC_943,(0,3):C.GC_943})

V_462 = Vertex(name = 'V_462',
               particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_328,(0,3):C.GC_330,(1,0):C.GC_321,(3,0):C.GC_324,(0,1):C.GC_255,(2,1):C.GC_257})

V_463 = Vertex(name = 'V_463',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_343,(0,2):C.GC_340,(0,0):C.GC_334,(2,0):C.GC_337})

V_464 = Vertex(name = 'V_464',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_326,(0,2):C.GC_329,(1,0):C.GC_320,(2,0):C.GC_323})

V_465 = Vertex(name = 'V_465',
               particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_342,(0,3):C.GC_344,(1,0):C.GC_335,(3,0):C.GC_338,(0,1):C.GC_260,(2,1):C.GC_262})

V_466 = Vertex(name = 'V_466',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_355,(0,3):C.GC_359,(0,0):C.GC_264,(2,0):C.GC_266,(1,1):C.GC_350,(3,1):C.GC_353})

V_467 = Vertex(name = 'V_467',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_385,(0,2):C.GC_382,(0,0):C.GC_376,(2,0):C.GC_379})

V_468 = Vertex(name = 'V_468',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,1):C.GC_354,(0,2):C.GC_357,(1,0):C.GC_348,(2,0):C.GC_351})

V_469 = Vertex(name = 'V_469',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_899,(0,7):C.GC_900,(0,0):C.GC_883,(2,0):C.GC_891,(1,3):C.GC_885,(3,3):C.GC_893,(1,1):C.GC_886,(3,1):C.GC_894,(1,2):C.GC_896,(0,4):C.GC_884,(2,4):C.GC_892,(0,5):C.GC_896})

V_470 = Vertex(name = 'V_470',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_373,(0,3):C.GC_369,(1,0):C.GC_269,(3,0):C.GC_271,(0,1):C.GC_364,(2,1):C.GC_367})

V_471 = Vertex(name = 'V_471',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_400,(0,3):C.GC_398,(0,0):C.GC_391,(2,0):C.GC_394,(1,1):C.GC_280,(3,1):C.GC_282})

V_472 = Vertex(name = 'V_472',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_947,(0,5):C.GC_949,(1,2):C.GC_922,(2,2):C.GC_924,(1,0):C.GC_929,(2,0):C.GC_938,(1,1):C.GC_944,(0,3):C.GC_944})

V_473 = Vertex(name = 'V_473',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_370,(0,3):C.GC_372,(1,0):C.GC_363,(3,0):C.GC_366,(0,1):C.GC_270,(2,1):C.GC_272})

V_474 = Vertex(name = 'V_474',
               particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_383,(0,3):C.GC_387,(0,0):C.GC_274,(2,0):C.GC_276,(1,1):C.GC_378,(3,1):C.GC_381})

V_475 = Vertex(name = 'V_475',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_397,(0,3):C.GC_401,(0,0):C.GC_279,(2,0):C.GC_281,(1,1):C.GC_392,(3,1):C.GC_395})

V_476 = Vertex(name = 'V_476',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_950,(0,7):C.GC_951,(0,0):C.GC_930,(2,0):C.GC_939,(1,3):C.GC_932,(3,3):C.GC_941,(1,1):C.GC_933,(3,1):C.GC_942,(1,2):C.GC_945,(0,4):C.GC_931,(2,4):C.GC_940,(0,5):C.GC_945})

V_477 = Vertex(name = 'V_477',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_860,(0,0):C.GC_671})

V_478 = Vertex(name = 'V_478',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_860,(0,0):C.GC_671})

V_479 = Vertex(name = 'V_479',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_860,(0,0):C.GC_671})

V_480 = Vertex(name = 'V_480',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_332})

V_481 = Vertex(name = 'V_481',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_332})

V_482 = Vertex(name = 'V_482',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_332})

V_483 = Vertex(name = 'V_483',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_346})

V_484 = Vertex(name = 'V_484',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_346})

V_485 = Vertex(name = 'V_485',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_346})

V_486 = Vertex(name = 'V_486',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_360})

V_487 = Vertex(name = 'V_487',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_360})

V_488 = Vertex(name = 'V_488',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_360})

V_489 = Vertex(name = 'V_489',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_904,(0,0):C.GC_693})

V_490 = Vertex(name = 'V_490',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_904,(0,0):C.GC_693})

V_491 = Vertex(name = 'V_491',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_904,(0,0):C.GC_693})

V_492 = Vertex(name = 'V_492',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_374})

V_493 = Vertex(name = 'V_493',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_374})

V_494 = Vertex(name = 'V_494',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_374})

V_495 = Vertex(name = 'V_495',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_388})

V_496 = Vertex(name = 'V_496',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_388})

V_497 = Vertex(name = 'V_497',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_388})

V_498 = Vertex(name = 'V_498',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_402})

V_499 = Vertex(name = 'V_499',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_402})

V_500 = Vertex(name = 'V_500',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_402})

V_501 = Vertex(name = 'V_501',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_955,(0,0):C.GC_723})

V_502 = Vertex(name = 'V_502',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_955,(0,0):C.GC_723})

V_503 = Vertex(name = 'V_503',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_955,(0,0):C.GC_723})

V_504 = Vertex(name = 'V_504',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_861,(0,0):C.GC_858})

V_505 = Vertex(name = 'V_505',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_861,(0,0):C.GC_858})

V_506 = Vertex(name = 'V_506',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_861,(0,0):C.GC_858})

V_507 = Vertex(name = 'V_507',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_333})

V_508 = Vertex(name = 'V_508',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_333})

V_509 = Vertex(name = 'V_509',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_333})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_347})

V_511 = Vertex(name = 'V_511',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_347})

V_512 = Vertex(name = 'V_512',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_347})

V_513 = Vertex(name = 'V_513',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_361})

V_514 = Vertex(name = 'V_514',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_361})

V_515 = Vertex(name = 'V_515',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_361})

V_516 = Vertex(name = 'V_516',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_905,(0,0):C.GC_902})

V_517 = Vertex(name = 'V_517',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_905,(0,0):C.GC_902})

V_518 = Vertex(name = 'V_518',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_905,(0,0):C.GC_902})

V_519 = Vertex(name = 'V_519',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_375})

V_520 = Vertex(name = 'V_520',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_375})

V_521 = Vertex(name = 'V_521',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_375})

V_522 = Vertex(name = 'V_522',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_389})

V_523 = Vertex(name = 'V_523',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_389})

V_524 = Vertex(name = 'V_524',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_389})

V_525 = Vertex(name = 'V_525',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_403})

V_526 = Vertex(name = 'V_526',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_403})

V_527 = Vertex(name = 'V_527',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_403})

V_528 = Vertex(name = 'V_528',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_956,(0,0):C.GC_953})

V_529 = Vertex(name = 'V_529',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_956,(0,0):C.GC_953})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_956,(0,0):C.GC_953})

V_531 = Vertex(name = 'V_531',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_10,(0,0):C.GC_605})

V_532 = Vertex(name = 'V_532',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_533 = Vertex(name = 'V_533',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_534 = Vertex(name = 'V_534',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_535 = Vertex(name = 'V_535',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_536 = Vertex(name = 'V_536',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_537 = Vertex(name = 'V_537',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_538 = Vertex(name = 'V_538',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_10,(0,0):C.GC_605})

V_539 = Vertex(name = 'V_539',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_540 = Vertex(name = 'V_540',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_541 = Vertex(name = 'V_541',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_542 = Vertex(name = 'V_542',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_607})

V_543 = Vertex(name = 'V_543',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_544 = Vertex(name = 'V_544',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_606,(0,0):C.GC_605})

V_545 = Vertex(name = 'V_545',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_10,(0,0):C.GC_605})

V_546 = Vertex(name = 'V_546',
               particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_10,(0,1):C.GC_10})

V_547 = Vertex(name = 'V_547',
               particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_606,(0,1):C.GC_607})

V_548 = Vertex(name = 'V_548',
               particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_606,(0,1):C.GC_607})

V_549 = Vertex(name = 'V_549',
               particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_10,(0,1):C.GC_10})

V_550 = Vertex(name = 'V_550',
               particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_606,(0,1):C.GC_607})

V_551 = Vertex(name = 'V_551',
               particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_10,(0,1):C.GC_10})

V_552 = Vertex(name = 'V_552',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_754,(0,3):C.GC_790,(0,0):C.GC_755,(0,2):C.GC_791})

V_553 = Vertex(name = 'V_553',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_758,(0,3):C.GC_794,(0,0):C.GC_759,(0,2):C.GC_795})

V_554 = Vertex(name = 'V_554',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_762,(0,3):C.GC_798,(0,0):C.GC_763,(0,2):C.GC_799})

V_555 = Vertex(name = 'V_555',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_766,(0,3):C.GC_802,(0,0):C.GC_767,(0,2):C.GC_803})

V_556 = Vertex(name = 'V_556',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_770,(0,3):C.GC_806,(0,0):C.GC_771,(0,2):C.GC_807})

V_557 = Vertex(name = 'V_557',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_774,(0,3):C.GC_810,(0,0):C.GC_775,(0,2):C.GC_811})

V_558 = Vertex(name = 'V_558',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_778,(0,3):C.GC_814,(0,0):C.GC_779,(0,2):C.GC_815})

V_559 = Vertex(name = 'V_559',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_782,(0,3):C.GC_818,(0,0):C.GC_783,(0,2):C.GC_819})

V_560 = Vertex(name = 'V_560',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_786,(0,3):C.GC_822,(0,0):C.GC_787,(0,2):C.GC_823})

V_561 = Vertex(name = 'V_561',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_285,(0,3):C.GC_303,(0,0):C.GC_284,(0,2):C.GC_302})

V_562 = Vertex(name = 'V_562',
               particles = [ P.s__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_287,(0,3):C.GC_305,(0,0):C.GC_286,(0,2):C.GC_304})

V_563 = Vertex(name = 'V_563',
               particles = [ P.b__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_289,(0,3):C.GC_307,(0,0):C.GC_288,(0,2):C.GC_306})

V_564 = Vertex(name = 'V_564',
               particles = [ P.d__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_291,(0,3):C.GC_309,(0,0):C.GC_290,(0,2):C.GC_308})

V_565 = Vertex(name = 'V_565',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_293,(0,3):C.GC_311,(0,0):C.GC_292,(0,2):C.GC_310})

V_566 = Vertex(name = 'V_566',
               particles = [ P.b__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_295,(0,3):C.GC_313,(0,0):C.GC_294,(0,2):C.GC_312})

V_567 = Vertex(name = 'V_567',
               particles = [ P.d__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_297,(0,3):C.GC_315,(0,0):C.GC_296,(0,2):C.GC_314})

V_568 = Vertex(name = 'V_568',
               particles = [ P.s__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_299,(0,3):C.GC_317,(0,0):C.GC_298,(0,2):C.GC_316})

V_569 = Vertex(name = 'V_569',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_301,(0,3):C.GC_319,(0,0):C.GC_300,(0,2):C.GC_318})

V_570 = Vertex(name = 'V_570',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1035,(0,0):C.GC_1034,(0,3):C.GC_1062,(0,2):C.GC_1061})

V_571 = Vertex(name = 'V_571',
               particles = [ P.s__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1038,(0,0):C.GC_1037,(0,3):C.GC_1065,(0,2):C.GC_1064})

V_572 = Vertex(name = 'V_572',
               particles = [ P.b__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1041,(0,0):C.GC_1040,(0,3):C.GC_1068,(0,2):C.GC_1067})

V_573 = Vertex(name = 'V_573',
               particles = [ P.d__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1044,(0,0):C.GC_1043,(0,3):C.GC_1071,(0,2):C.GC_1070})

V_574 = Vertex(name = 'V_574',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1047,(0,0):C.GC_1046,(0,3):C.GC_1074,(0,2):C.GC_1073})

V_575 = Vertex(name = 'V_575',
               particles = [ P.b__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1050,(0,0):C.GC_1049,(0,3):C.GC_1077,(0,2):C.GC_1076})

V_576 = Vertex(name = 'V_576',
               particles = [ P.d__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1053,(0,0):C.GC_1052,(0,3):C.GC_1080,(0,2):C.GC_1079})

V_577 = Vertex(name = 'V_577',
               particles = [ P.s__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1056,(0,0):C.GC_1055,(0,3):C.GC_1083,(0,2):C.GC_1082})

V_578 = Vertex(name = 'V_578',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1059,(0,0):C.GC_1058,(0,3):C.GC_1086,(0,2):C.GC_1085})

V_579 = Vertex(name = 'V_579',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1476,(0,0):C.GC_1474,(0,3):C.GC_1117,(0,2):C.GC_1116})

V_580 = Vertex(name = 'V_580',
               particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1121,(0,0):C.GC_1120})

V_581 = Vertex(name = 'V_581',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1125,(0,0):C.GC_1124})

V_582 = Vertex(name = 'V_582',
               particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1129,(0,0):C.GC_1128})

V_583 = Vertex(name = 'V_583',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1700,(0,0):C.GC_1698,(0,3):C.GC_1133,(0,2):C.GC_1132})

V_584 = Vertex(name = 'V_584',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1137,(0,0):C.GC_1136})

V_585 = Vertex(name = 'V_585',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1141,(0,0):C.GC_1140})

V_586 = Vertex(name = 'V_586',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1145,(0,0):C.GC_1144})

V_587 = Vertex(name = 'V_587',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1399,(0,0):C.GC_1397,(0,3):C.GC_1149,(0,2):C.GC_1148})

V_588 = Vertex(name = 'V_588',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1151,(0,0):C.GC_1150,(0,3):C.GC_1169,(0,2):C.GC_1168})

V_589 = Vertex(name = 'V_589',
               particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1153,(0,0):C.GC_1152,(0,3):C.GC_1171,(0,2):C.GC_1170})

V_590 = Vertex(name = 'V_590',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1155,(0,0):C.GC_1154,(0,3):C.GC_1173,(0,2):C.GC_1172})

V_591 = Vertex(name = 'V_591',
               particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1157,(0,0):C.GC_1156,(0,3):C.GC_1175,(0,2):C.GC_1174})

V_592 = Vertex(name = 'V_592',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1159,(0,0):C.GC_1158,(0,3):C.GC_1177,(0,2):C.GC_1176})

V_593 = Vertex(name = 'V_593',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1161,(0,0):C.GC_1160,(0,3):C.GC_1179,(0,2):C.GC_1178})

V_594 = Vertex(name = 'V_594',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1163,(0,0):C.GC_1162,(0,3):C.GC_1181,(0,2):C.GC_1180})

V_595 = Vertex(name = 'V_595',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1165,(0,0):C.GC_1164,(0,3):C.GC_1183,(0,2):C.GC_1182})

V_596 = Vertex(name = 'V_596',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1167,(0,0):C.GC_1166,(0,3):C.GC_1185,(0,2):C.GC_1184})

V_597 = Vertex(name = 'V_597',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1570,(0,3):C.GC_1570,(0,0):C.GC_1571,(0,2):C.GC_1571})

V_598 = Vertex(name = 'V_598',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1673,(0,3):C.GC_1673,(0,0):C.GC_1674,(0,2):C.GC_1674})

V_599 = Vertex(name = 'V_599',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1875,(0,3):C.GC_1875,(0,0):C.GC_1876,(0,2):C.GC_1876})

V_600 = Vertex(name = 'V_600',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1491,(0,0):C.GC_1490})

V_601 = Vertex(name = 'V_601',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1594,(0,0):C.GC_1593})

V_602 = Vertex(name = 'V_602',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1796,(0,0):C.GC_1795})

V_603 = Vertex(name = 'V_603',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1493,(0,0):C.GC_1492,(0,3):C.GC_1493,(0,2):C.GC_1492})

V_604 = Vertex(name = 'V_604',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1596,(0,0):C.GC_1595,(0,3):C.GC_1596,(0,2):C.GC_1595})

V_605 = Vertex(name = 'V_605',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1798,(0,0):C.GC_1797,(0,3):C.GC_1798,(0,2):C.GC_1797})

V_606 = Vertex(name = 'V_606',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1944,(0,3):C.GC_1943,(0,0):C.GC_1942,(0,2):C.GC_1941})

V_607 = Vertex(name = 'V_607',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1449,(0,3):C.GC_1448,(0,0):C.GC_1447,(0,2):C.GC_1446})

V_608 = Vertex(name = 'V_608',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1756,(0,3):C.GC_1755,(0,0):C.GC_1754,(0,2):C.GC_1753})

V_609 = Vertex(name = 'V_609',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1918,(0,3):C.GC_1917,(0,0):C.GC_1916,(0,2):C.GC_1915})

V_610 = Vertex(name = 'V_610',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1423,(0,3):C.GC_1422,(0,0):C.GC_1421,(0,2):C.GC_1420})

V_611 = Vertex(name = 'V_611',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_1730,(0,3):C.GC_1729,(0,0):C.GC_1728,(0,2):C.GC_1727})

V_612 = Vertex(name = 'V_612',
               particles = [ P.u__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1948,(0,0):C.GC_1946,(0,3):C.GC_1947,(0,2):C.GC_1945})

V_613 = Vertex(name = 'V_613',
               particles = [ P.c__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1453,(0,0):C.GC_1451,(0,3):C.GC_1452,(0,2):C.GC_1450})

V_614 = Vertex(name = 'V_614',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1760,(0,0):C.GC_1758,(0,3):C.GC_1759,(0,2):C.GC_1757})

V_615 = Vertex(name = 'V_615',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1088,(0,0):C.GC_1089,(0,3):C.GC_1473,(0,2):C.GC_1475})

V_616 = Vertex(name = 'V_616',
               particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1091,(0,0):C.GC_1092})

V_617 = Vertex(name = 'V_617',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1094,(0,0):C.GC_1095})

V_618 = Vertex(name = 'V_618',
               particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1097,(0,0):C.GC_1098})

V_619 = Vertex(name = 'V_619',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1100,(0,0):C.GC_1101,(0,3):C.GC_1697,(0,2):C.GC_1699})

V_620 = Vertex(name = 'V_620',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1103,(0,0):C.GC_1104})

V_621 = Vertex(name = 'V_621',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1106,(0,0):C.GC_1107})

V_622 = Vertex(name = 'V_622',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1109,(0,0):C.GC_1110})

V_623 = Vertex(name = 'V_623',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1112,(0,0):C.GC_1113,(0,3):C.GC_1396,(0,2):C.GC_1398})

V_624 = Vertex(name = 'V_624',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1950,(0,0):C.GC_1952,(0,3):C.GC_1949,(0,2):C.GC_1951})

V_625 = Vertex(name = 'V_625',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1455,(0,0):C.GC_1457,(0,3):C.GC_1454,(0,2):C.GC_1456})

V_626 = Vertex(name = 'V_626',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1762,(0,0):C.GC_1764,(0,3):C.GC_1761,(0,2):C.GC_1763})

V_627 = Vertex(name = 'V_627',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1478,(0,0):C.GC_1480,(0,3):C.GC_1213,(0,2):C.GC_1214})

V_628 = Vertex(name = 'V_628',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1215,(0,0):C.GC_1216})

V_629 = Vertex(name = 'V_629',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1217,(0,0):C.GC_1218})

V_630 = Vertex(name = 'V_630',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1219,(0,0):C.GC_1220})

V_631 = Vertex(name = 'V_631',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1702,(0,0):C.GC_1704,(0,3):C.GC_1221,(0,2):C.GC_1222})

V_632 = Vertex(name = 'V_632',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1223,(0,0):C.GC_1224})

V_633 = Vertex(name = 'V_633',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1225,(0,0):C.GC_1226})

V_634 = Vertex(name = 'V_634',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1227,(0,0):C.GC_1228})

V_635 = Vertex(name = 'V_635',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1401,(0,0):C.GC_1403,(0,3):C.GC_1229,(0,2):C.GC_1230})

V_636 = Vertex(name = 'V_636',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1494,(0,0):C.GC_1495})

V_637 = Vertex(name = 'V_637',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1597,(0,0):C.GC_1598})

V_638 = Vertex(name = 'V_638',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1799,(0,0):C.GC_1800})

V_639 = Vertex(name = 'V_639',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1196,(0,0):C.GC_1195,(0,3):C.GC_1479,(0,2):C.GC_1477})

V_640 = Vertex(name = 'V_640',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1198,(0,0):C.GC_1197})

V_641 = Vertex(name = 'V_641',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1200,(0,0):C.GC_1199})

V_642 = Vertex(name = 'V_642',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1202,(0,0):C.GC_1201})

V_643 = Vertex(name = 'V_643',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1204,(0,0):C.GC_1203,(0,3):C.GC_1703,(0,2):C.GC_1701})

V_644 = Vertex(name = 'V_644',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1206,(0,0):C.GC_1205})

V_645 = Vertex(name = 'V_645',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1208,(0,0):C.GC_1207})

V_646 = Vertex(name = 'V_646',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,1):C.GC_1210,(0,0):C.GC_1209})

V_647 = Vertex(name = 'V_647',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2, L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1212,(0,0):C.GC_1211,(0,3):C.GC_1402,(0,2):C.GC_1400})

V_648 = Vertex(name = 'V_648',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1490,(0,0):C.GC_1491})

V_649 = Vertex(name = 'V_649',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1593,(0,0):C.GC_1594})

V_650 = Vertex(name = 'V_650',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1795,(0,0):C.GC_1796})

V_651 = Vertex(name = 'V_651',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1495,(0,0):C.GC_1494})

V_652 = Vertex(name = 'V_652',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1598,(0,0):C.GC_1597})

V_653 = Vertex(name = 'V_653',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,1):C.GC_1800,(0,0):C.GC_1799})

