# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Tue 19 May 2020 18:01:33

import configuration

from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000,
                   texname = '\\text{Lambda}',
                   lhablock = 'DIM6',
                   lhacode = [ 1 ])

ctp = Parameter(name = 'ctp',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctp}',
                lhablock = 'DIM6',
                lhacode = [ 2 ])

ctpI = Parameter(name = 'ctpI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctpI}',
                 lhablock = 'DIM6',
                 lhacode = [ 3 ])

cpQM = Parameter(name = 'cpQM',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cpQM}',
                 lhablock = 'DIM6',
                 lhacode = [ 4 ])

cpQ3 = Parameter(name = 'cpQ3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cpQ3}',
                 lhablock = 'DIM6',
                 lhacode = [ 5 ])

cpt = Parameter(name = 'cpt',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cpt}',
                lhablock = 'DIM6',
                lhacode = [ 6 ])

cpb = Parameter(name = 'cpb',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cpb}',
                lhablock = 'DIM6',
                lhacode = [ 7 ])

cptb = Parameter(name = 'cptb',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cptb}',
                 lhablock = 'DIM6',
                 lhacode = [ 8 ])

cptbI = Parameter(name = 'cptbI',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cptbI}',
                  lhablock = 'DIM6',
                  lhacode = [ 9 ])

ctW = Parameter(name = 'ctW',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctW}',
                lhablock = 'DIM6',
                lhacode = [ 10 ])

ctZ = Parameter(name = 'ctZ',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctZ}',
                lhablock = 'DIM6',
                lhacode = [ 11 ])

ctWI = Parameter(name = 'ctWI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctWI}',
                 lhablock = 'DIM6',
                 lhacode = [ 12 ])

ctZI = Parameter(name = 'ctZI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctZI}',
                 lhablock = 'DIM6',
                 lhacode = [ 13 ])

cbW = Parameter(name = 'cbW',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cbW}',
                lhablock = 'DIM6',
                lhacode = [ 14 ])

cbWI = Parameter(name = 'cbWI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cbWI}',
                 lhablock = 'DIM6',
                 lhacode = [ 15 ])

ctG = Parameter(name = 'ctG',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctG}',
                lhablock = 'DIM6',
                lhacode = [ 16 ])

ctGI = Parameter(name = 'ctGI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctGI}',
                 lhablock = 'DIM6',
                 lhacode = [ 17 ])

cQlM1 = Parameter(name = 'cQlM1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM1}',
                  lhablock = 'DIM6',
                  lhacode = [ 18 ])

cQlM2 = Parameter(name = 'cQlM2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM2}',
                  lhablock = 'DIM6',
                  lhacode = [ 19 ])

cQlM3 = Parameter(name = 'cQlM3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM3}',
                  lhablock = 'DIM6',
                  lhacode = [ 20 ])

cQl31 = Parameter(name = 'cQl31',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl31}',
                  lhablock = 'DIM6',
                  lhacode = [ 21 ])

cQl32 = Parameter(name = 'cQl32',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl32}',
                  lhablock = 'DIM6',
                  lhacode = [ 22 ])

cQl33 = Parameter(name = 'cQl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl33}',
                  lhablock = 'DIM6',
                  lhacode = [ 23 ])

cQe1 = Parameter(name = 'cQe1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe1}',
                 lhablock = 'DIM6',
                 lhacode = [ 24 ])

cQe2 = Parameter(name = 'cQe2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe2}',
                 lhablock = 'DIM6',
                 lhacode = [ 25 ])

cQe3 = Parameter(name = 'cQe3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe3}',
                 lhablock = 'DIM6',
                 lhacode = [ 26 ])

ctl1 = Parameter(name = 'ctl1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl1}',
                 lhablock = 'DIM6',
                 lhacode = [ 27 ])

ctl2 = Parameter(name = 'ctl2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl2}',
                 lhablock = 'DIM6',
                 lhacode = [ 28 ])

ctl3 = Parameter(name = 'ctl3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl3}',
                 lhablock = 'DIM6',
                 lhacode = [ 29 ])

cte1 = Parameter(name = 'cte1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte1}',
                 lhablock = 'DIM6',
                 lhacode = [ 30 ])

cte2 = Parameter(name = 'cte2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte2}',
                 lhablock = 'DIM6',
                 lhacode = [ 31 ])

cte3 = Parameter(name = 'cte3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte3}',
                 lhablock = 'DIM6',
                 lhacode = [ 32 ])

ctlS1 = Parameter(name = 'ctlS1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS1}',
                  lhablock = 'DIM6',
                  lhacode = [ 33 ])

ctlSI1 = Parameter(name = 'ctlSI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 34 ])

ctlS2 = Parameter(name = 'ctlS2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS2}',
                  lhablock = 'DIM6',
                  lhacode = [ 35 ])

ctlSI2 = Parameter(name = 'ctlSI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 36 ])

ctlS3 = Parameter(name = 'ctlS3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS3}',
                  lhablock = 'DIM6',
                  lhacode = [ 37 ])

ctlSI3 = Parameter(name = 'ctlSI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 38 ])

ctlT1 = Parameter(name = 'ctlT1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT1}',
                  lhablock = 'DIM6',
                  lhacode = [ 39 ])

ctlTI1 = Parameter(name = 'ctlTI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 40 ])

ctlT2 = Parameter(name = 'ctlT2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT2}',
                  lhablock = 'DIM6',
                  lhacode = [ 41 ])

ctlTI2 = Parameter(name = 'ctlTI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 42 ])

ctlT3 = Parameter(name = 'ctlT3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT3}',
                  lhablock = 'DIM6',
                  lhacode = [ 43 ])

ctlTI3 = Parameter(name = 'ctlTI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 44 ])

cblS1 = Parameter(name = 'cblS1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS1}',
                  lhablock = 'DIM6',
                  lhacode = [ 45 ])

cblSI1 = Parameter(name = 'cblSI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 46 ])

cblS2 = Parameter(name = 'cblS2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS2}',
                  lhablock = 'DIM6',
                  lhacode = [ 47 ])

cblSI2 = Parameter(name = 'cblSI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 48 ])

cblS3 = Parameter(name = 'cblS3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS3}',
                  lhablock = 'DIM6',
                  lhacode = [ 49 ])

cblSI3 = Parameter(name = 'cblSI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 50 ])

cQq83 = Parameter(name = 'cQq83',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq83}',
                  lhablock = 'DIM6',
                  lhacode = [ 51 ])

cQq81 = Parameter(name = 'cQq81',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq81}',
                  lhablock = 'DIM6',
                  lhacode = [ 52 ])

cQu8 = Parameter(name = 'cQu8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQu8}',
                 lhablock = 'DIM6',
                 lhacode = [ 53 ])

cQd8 = Parameter(name = 'cQd8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQd8}',
                 lhablock = 'DIM6',
                 lhacode = [ 54 ])

ctq8 = Parameter(name = 'ctq8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctq8}',
                 lhablock = 'DIM6',
                 lhacode = [ 55 ])

ctu8 = Parameter(name = 'ctu8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctu8}',
                 lhablock = 'DIM6',
                 lhacode = [ 56 ])

ctd8 = Parameter(name = 'ctd8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctd8}',
                 lhablock = 'DIM6',
                 lhacode = [ 57 ])

cQq13 = Parameter(name = 'cQq13',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq13}',
                  lhablock = 'DIM6',
                  lhacode = [ 58 ])

cQq11 = Parameter(name = 'cQq11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq11}',
                  lhablock = 'DIM6',
                  lhacode = [ 59 ])

cQu1 = Parameter(name = 'cQu1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQu1}',
                 lhablock = 'DIM6',
                 lhacode = [ 60 ])

cQd1 = Parameter(name = 'cQd1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQd1}',
                 lhablock = 'DIM6',
                 lhacode = [ 61 ])

ctq1 = Parameter(name = 'ctq1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctq1}',
                 lhablock = 'DIM6',
                 lhacode = [ 62 ])

ctu1 = Parameter(name = 'ctu1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctu1}',
                 lhablock = 'DIM6',
                 lhacode = [ 63 ])

ctd1 = Parameter(name = 'ctd1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctd1}',
                 lhablock = 'DIM6',
                 lhacode = [ 64 ])

cQQ1 = Parameter(name = 'cQQ1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQQ1}',
                 lhablock = 'DIM6',
                 lhacode = [ 65 ])

cQQ8 = Parameter(name = 'cQQ8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQQ8}',
                 lhablock = 'DIM6',
                 lhacode = [ 66 ])

cQt1 = Parameter(name = 'cQt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQt1}',
                 lhablock = 'DIM6',
                 lhacode = [ 67 ])

cQb1 = Parameter(name = 'cQb1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQb1}',
                 lhablock = 'DIM6',
                 lhacode = [ 68 ])

ctt1 = Parameter(name = 'ctt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctt1}',
                 lhablock = 'DIM6',
                 lhacode = [ 69 ])

ctb1 = Parameter(name = 'ctb1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctb1}',
                 lhablock = 'DIM6',
                 lhacode = [ 70 ])

cQt8 = Parameter(name = 'cQt8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQt8}',
                 lhablock = 'DIM6',
                 lhacode = [ 71 ])

cQb8 = Parameter(name = 'cQb8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQb8}',
                 lhablock = 'DIM6',
                 lhacode = [ 72 ])

ctb8 = Parameter(name = 'ctb8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctb8}',
                 lhablock = 'DIM6',
                 lhacode = [ 73 ])

ctQqu1 = Parameter(name = 'ctQqu1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctQqu1}',
                   lhablock = 'DIM6',
                   lhacode = [ 74 ])

ctQqu1I = Parameter(name = 'ctQqu1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctQqu1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 75 ])

ctQqu8 = Parameter(name = 'ctQqu8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctQqu8}',
                   lhablock = 'DIM6',
                   lhacode = [ 76 ])

ctQqu8I = Parameter(name = 'ctQqu8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctQqu8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 77 ])

cbQqd1 = Parameter(name = 'cbQqd1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbQqd1}',
                   lhablock = 'DIM6',
                   lhacode = [ 78 ])

cbQqd1I = Parameter(name = 'cbQqd1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbQqd1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 79 ])

cbQqd8 = Parameter(name = 'cbQqd8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbQqd8}',
                   lhablock = 'DIM6',
                   lhacode = [ 80 ])

cbQqd8I = Parameter(name = 'cbQqd8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbQqd8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 81 ])

cQtqd1 = Parameter(name = 'cQtqd1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQtqd1}',
                   lhablock = 'DIM6',
                   lhacode = [ 82 ])

cQtqd1I = Parameter(name = 'cQtqd1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtqd1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 83 ])

cQtqd8 = Parameter(name = 'cQtqd8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQtqd8}',
                   lhablock = 'DIM6',
                   lhacode = [ 84 ])

cQtqd8I = Parameter(name = 'cQtqd8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtqd8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 85 ])

cQbqu1 = Parameter(name = 'cQbqu1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQbqu1}',
                   lhablock = 'DIM6',
                   lhacode = [ 86 ])

cQbqu1I = Parameter(name = 'cQbqu1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQbqu1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 87 ])

cQbqu8 = Parameter(name = 'cQbqu8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQbqu8}',
                   lhablock = 'DIM6',
                   lhacode = [ 88 ])

cQbqu8I = Parameter(name = 'cQbqu8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQbqu8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 89 ])

ctQqu1T = Parameter(name = 'ctQqu1T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctQqu1T}',
                    lhablock = 'DIM6',
                    lhacode = [ 90 ])

ctQqu1TI = Parameter(name = 'ctQqu1TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctQqu1TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 91 ])

ctQqu8T = Parameter(name = 'ctQqu8T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctQqu8T}',
                    lhablock = 'DIM6',
                    lhacode = [ 92 ])

ctQqu8TI = Parameter(name = 'ctQqu8TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctQqu8TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 93 ])

cbQqd1T = Parameter(name = 'cbQqd1T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbQqd1T}',
                    lhablock = 'DIM6',
                    lhacode = [ 94 ])

cbQqd1TI = Parameter(name = 'cbQqd1TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cbQqd1TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 95 ])

cbQqd8T = Parameter(name = 'cbQqd8T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbQqd8T}',
                    lhablock = 'DIM6',
                    lhacode = [ 96 ])

cbQqd8TI = Parameter(name = 'cbQqd8TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cbQqd8TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 97 ])

cQtqd1T = Parameter(name = 'cQtqd1T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtqd1T}',
                    lhablock = 'DIM6',
                    lhacode = [ 98 ])

cQtqd1TI = Parameter(name = 'cQtqd1TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQtqd1TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 99 ])

cQtqd8T = Parameter(name = 'cQtqd8T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtqd8T}',
                    lhablock = 'DIM6',
                    lhacode = [ 100 ])

cQtqd8TI = Parameter(name = 'cQtqd8TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQtqd8TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 101 ])

cQbqu1T = Parameter(name = 'cQbqu1T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQbqu1T}',
                    lhablock = 'DIM6',
                    lhacode = [ 102 ])

cQbqu1TI = Parameter(name = 'cQbqu1TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQbqu1TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 103 ])

cQbqu8T = Parameter(name = 'cQbqu8T',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQbqu8T}',
                    lhablock = 'DIM6',
                    lhacode = [ 104 ])

cQbqu8TI = Parameter(name = 'cQbqu8TI',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQbqu8TI}',
                     lhablock = 'DIM6',
                     lhacode = [ 105 ])

cbtud1 = Parameter(name = 'cbtud1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbtud1}',
                   lhablock = 'DIM6',
                   lhacode = [ 106 ])

cbtud1I = Parameter(name = 'cbtud1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbtud1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 107 ])

cbtud8 = Parameter(name = 'cbtud8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbtud8}',
                   lhablock = 'DIM6',
                   lhacode = [ 108 ])

cbtud8I = Parameter(name = 'cbtud8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbtud8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 109 ])

cQtQb1 = Parameter(name = 'cQtQb1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQtQb1}',
                   lhablock = 'DIM6',
                   lhacode = [ 110 ])

cQtQb8 = Parameter(name = 'cQtQb8',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cQtQb8}',
                   lhablock = 'DIM6',
                   lhacode = [ 111 ])

cQtQb1I = Parameter(name = 'cQtQb1I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtQb1I}',
                    lhablock = 'DIM6',
                    lhacode = [ 112 ])

cQtQb8I = Parameter(name = 'cQtQb8I',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cQtQb8I}',
                    lhablock = 'DIM6',
                    lhacode = [ 113 ])

ctpx13 = Parameter(name = 'ctpx13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctpx13}',
                   lhablock = 'FCNC',
                   lhacode = [ 1 ])

ctpx23 = Parameter(name = 'ctpx23',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctpx23}',
                   lhablock = 'FCNC',
                   lhacode = [ 2 ])

ctpx31 = Parameter(name = 'ctpx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctpx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 3 ])

ctpx32 = Parameter(name = 'ctpx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctpx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 4 ])

ctpIx13 = Parameter(name = 'ctpIx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctpIx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 5 ])

ctpIx23 = Parameter(name = 'ctpIx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctpIx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 6 ])

ctpIx31 = Parameter(name = 'ctpIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctpIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 7 ])

ctpIx32 = Parameter(name = 'ctpIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctpIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 8 ])

cpQMx31 = Parameter(name = 'cpQMx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpQMx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 9 ])

cpQMx32 = Parameter(name = 'cpQMx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpQMx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 10 ])

cpQMIx31 = Parameter(name = 'cpQMIx31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cpQMIx31}',
                     lhablock = 'FCNC',
                     lhacode = [ 11 ])

cpQMIx32 = Parameter(name = 'cpQMIx32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cpQMIx32}',
                     lhablock = 'FCNC',
                     lhacode = [ 12 ])

cpQ3x31 = Parameter(name = 'cpQ3x31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpQ3x31}',
                    lhablock = 'FCNC',
                    lhacode = [ 13 ])

cpQ3x32 = Parameter(name = 'cpQ3x32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpQ3x32}',
                    lhablock = 'FCNC',
                    lhacode = [ 14 ])

cpQ3Ix31 = Parameter(name = 'cpQ3Ix31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cpQ3Ix31}',
                     lhablock = 'FCNC',
                     lhacode = [ 15 ])

cpQ3Ix32 = Parameter(name = 'cpQ3Ix32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cpQ3Ix32}',
                     lhablock = 'FCNC',
                     lhacode = [ 16 ])

cptx31 = Parameter(name = 'cptx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cptx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 17 ])

cptx32 = Parameter(name = 'cptx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cptx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 18 ])

cptIx31 = Parameter(name = 'cptIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 19 ])

cptIx32 = Parameter(name = 'cptIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 20 ])

cptbx13 = Parameter(name = 'cptbx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptbx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 21 ])

cptbx23 = Parameter(name = 'cptbx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptbx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 22 ])

cptbx31 = Parameter(name = 'cptbx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptbx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 23 ])

cptbx32 = Parameter(name = 'cptbx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cptbx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 24 ])

cptbIx13 = Parameter(name = 'cptbIx13',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cptbIx13}',
                     lhablock = 'FCNC',
                     lhacode = [ 25 ])

cptbIx23 = Parameter(name = 'cptbIx23',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cptbIx23}',
                     lhablock = 'FCNC',
                     lhacode = [ 26 ])

cptbIx31 = Parameter(name = 'cptbIx31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cptbIx31}',
                     lhablock = 'FCNC',
                     lhacode = [ 27 ])

cptbIx32 = Parameter(name = 'cptbIx32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cptbIx32}',
                     lhablock = 'FCNC',
                     lhacode = [ 28 ])

ctAx13 = Parameter(name = 'ctAx13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctAx13}',
                   lhablock = 'FCNC',
                   lhacode = [ 29 ])

ctAx23 = Parameter(name = 'ctAx23',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctAx23}',
                   lhablock = 'FCNC',
                   lhacode = [ 30 ])

ctAx31 = Parameter(name = 'ctAx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctAx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 31 ])

ctAx32 = Parameter(name = 'ctAx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctAx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 32 ])

ctAIx13 = Parameter(name = 'ctAIx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctAIx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 33 ])

ctAIx23 = Parameter(name = 'ctAIx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctAIx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 34 ])

ctAIx31 = Parameter(name = 'ctAIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctAIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 35 ])

ctAIx32 = Parameter(name = 'ctAIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctAIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 36 ])

ctZx13 = Parameter(name = 'ctZx13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctZx13}',
                   lhablock = 'FCNC',
                   lhacode = [ 37 ])

ctZx23 = Parameter(name = 'ctZx23',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctZx23}',
                   lhablock = 'FCNC',
                   lhacode = [ 38 ])

ctZx31 = Parameter(name = 'ctZx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctZx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 39 ])

ctZx32 = Parameter(name = 'ctZx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctZx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 40 ])

ctZIx13 = Parameter(name = 'ctZIx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctZIx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 41 ])

ctZIx23 = Parameter(name = 'ctZIx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctZIx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 42 ])

ctZIx31 = Parameter(name = 'ctZIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctZIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 43 ])

ctZIx32 = Parameter(name = 'ctZIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctZIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 44 ])

cbWx13 = Parameter(name = 'cbWx13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbWx13}',
                   lhablock = 'FCNC',
                   lhacode = [ 45 ])

cbWx23 = Parameter(name = 'cbWx23',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbWx23}',
                   lhablock = 'FCNC',
                   lhacode = [ 46 ])

cbWx31 = Parameter(name = 'cbWx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbWx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 47 ])

cbWx32 = Parameter(name = 'cbWx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cbWx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 48 ])

cbWIx13 = Parameter(name = 'cbWIx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbWIx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 49 ])

cbWIx23 = Parameter(name = 'cbWIx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbWIx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 50 ])

cbWIx31 = Parameter(name = 'cbWIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbWIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 51 ])

cbWIx32 = Parameter(name = 'cbWIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cbWIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 52 ])

ctGx13 = Parameter(name = 'ctGx13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctGx13}',
                   lhablock = 'FCNC',
                   lhacode = [ 53 ])

ctGx23 = Parameter(name = 'ctGx23',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctGx23}',
                   lhablock = 'FCNC',
                   lhacode = [ 54 ])

ctGx31 = Parameter(name = 'ctGx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctGx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 55 ])

ctGx32 = Parameter(name = 'ctGx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctGx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 56 ])

ctGIx13 = Parameter(name = 'ctGIx13',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctGIx13}',
                    lhablock = 'FCNC',
                    lhacode = [ 57 ])

ctGIx23 = Parameter(name = 'ctGIx23',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctGIx23}',
                    lhablock = 'FCNC',
                    lhacode = [ 58 ])

ctGIx31 = Parameter(name = 'ctGIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctGIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 59 ])

ctGIx32 = Parameter(name = 'ctGIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{ctGIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 60 ])

cQl3x1x31 = Parameter(name = 'cQl3x1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 61 ])

cQl3x1x32 = Parameter(name = 'cQl3x1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 62 ])

cQl3x2x31 = Parameter(name = 'cQl3x2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 63 ])

cQl3x2x32 = Parameter(name = 'cQl3x2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 64 ])

cQl3x3x31 = Parameter(name = 'cQl3x3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 65 ])

cQl3x3x32 = Parameter(name = 'cQl3x3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQl3x3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 66 ])

cQl3Ix1x31 = Parameter(name = 'cQl3Ix1x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix1x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 67 ])

cQl3Ix1x32 = Parameter(name = 'cQl3Ix1x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix1x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 68 ])

cQl3Ix2x31 = Parameter(name = 'cQl3Ix2x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix2x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 69 ])

cQl3Ix2x32 = Parameter(name = 'cQl3Ix2x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix2x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 70 ])

cQl3Ix3x31 = Parameter(name = 'cQl3Ix3x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix3x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 71 ])

cQl3Ix3x32 = Parameter(name = 'cQl3Ix3x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQl3Ix3x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 72 ])

cQlMx1x31 = Parameter(name = 'cQlMx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 73 ])

cQlMx1x32 = Parameter(name = 'cQlMx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 74 ])

cQlMx2x31 = Parameter(name = 'cQlMx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 75 ])

cQlMx2x32 = Parameter(name = 'cQlMx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 76 ])

cQlMx3x31 = Parameter(name = 'cQlMx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 77 ])

cQlMx3x32 = Parameter(name = 'cQlMx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQlMx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 78 ])

cQlMIx1x31 = Parameter(name = 'cQlMIx1x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx1x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 79 ])

cQlMIx1x32 = Parameter(name = 'cQlMIx1x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx1x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 80 ])

cQlMIx2x31 = Parameter(name = 'cQlMIx2x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx2x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 81 ])

cQlMIx2x32 = Parameter(name = 'cQlMIx2x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx2x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 82 ])

cQlMIx3x31 = Parameter(name = 'cQlMIx3x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx3x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 83 ])

cQlMIx3x32 = Parameter(name = 'cQlMIx3x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cQlMIx3x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 84 ])

cQex1x31 = Parameter(name = 'cQex1x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex1x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 85 ])

cQex1x32 = Parameter(name = 'cQex1x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex1x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 86 ])

cQex2x31 = Parameter(name = 'cQex2x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex2x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 87 ])

cQex2x32 = Parameter(name = 'cQex2x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex2x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 88 ])

cQex3x31 = Parameter(name = 'cQex3x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex3x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 89 ])

cQex3x32 = Parameter(name = 'cQex3x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{cQex3x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 90 ])

cQeIx1x31 = Parameter(name = 'cQeIx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 91 ])

cQeIx1x32 = Parameter(name = 'cQeIx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 92 ])

cQeIx2x31 = Parameter(name = 'cQeIx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 93 ])

cQeIx2x32 = Parameter(name = 'cQeIx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 94 ])

cQeIx3x31 = Parameter(name = 'cQeIx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 95 ])

cQeIx3x32 = Parameter(name = 'cQeIx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cQeIx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 96 ])

ctlx1x31 = Parameter(name = 'ctlx1x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx1x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 97 ])

ctlx1x32 = Parameter(name = 'ctlx1x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx1x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 98 ])

ctlx2x31 = Parameter(name = 'ctlx2x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx2x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 99 ])

ctlx2x32 = Parameter(name = 'ctlx2x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx2x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 100 ])

ctlx3x31 = Parameter(name = 'ctlx3x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx3x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 101 ])

ctlx3x32 = Parameter(name = 'ctlx3x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctlx3x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 102 ])

ctlIx1x31 = Parameter(name = 'ctlIx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 103 ])

ctlIx1x32 = Parameter(name = 'ctlIx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 104 ])

ctlIx2x31 = Parameter(name = 'ctlIx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 105 ])

ctlIx2x32 = Parameter(name = 'ctlIx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 106 ])

ctlIx3x31 = Parameter(name = 'ctlIx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 107 ])

ctlIx3x32 = Parameter(name = 'ctlIx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlIx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 108 ])

ctex1x31 = Parameter(name = 'ctex1x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex1x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 109 ])

ctex1x32 = Parameter(name = 'ctex1x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex1x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 110 ])

ctex2x31 = Parameter(name = 'ctex2x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex2x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 111 ])

ctex2x32 = Parameter(name = 'ctex2x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex2x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 112 ])

ctex3x31 = Parameter(name = 'ctex3x31',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex3x31}',
                     lhablock = 'FCNC',
                     lhacode = [ 113 ])

ctex3x32 = Parameter(name = 'ctex3x32',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ctex3x32}',
                     lhablock = 'FCNC',
                     lhacode = [ 114 ])

cteIx1x31 = Parameter(name = 'cteIx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 115 ])

cteIx1x32 = Parameter(name = 'cteIx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 116 ])

cteIx2x31 = Parameter(name = 'cteIx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 117 ])

cteIx2x32 = Parameter(name = 'cteIx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 118 ])

cteIx3x31 = Parameter(name = 'cteIx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 119 ])

cteIx3x32 = Parameter(name = 'cteIx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cteIx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 120 ])

ctlSx1x13 = Parameter(name = 'ctlSx1x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx1x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 121 ])

ctlSx1x23 = Parameter(name = 'ctlSx1x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx1x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 122 ])

ctlSx1x31 = Parameter(name = 'ctlSx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 123 ])

ctlSx1x32 = Parameter(name = 'ctlSx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 124 ])

ctlSx2x13 = Parameter(name = 'ctlSx2x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx2x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 125 ])

ctlSx2x23 = Parameter(name = 'ctlSx2x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx2x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 126 ])

ctlSx2x31 = Parameter(name = 'ctlSx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 127 ])

ctlSx2x32 = Parameter(name = 'ctlSx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 128 ])

ctlSx3x13 = Parameter(name = 'ctlSx3x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx3x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 129 ])

ctlSx3x23 = Parameter(name = 'ctlSx3x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx3x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 130 ])

ctlSx3x31 = Parameter(name = 'ctlSx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 131 ])

ctlSx3x32 = Parameter(name = 'ctlSx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlSx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 132 ])

ctlSIx1x13 = Parameter(name = 'ctlSIx1x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx1x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 133 ])

ctlSIx1x23 = Parameter(name = 'ctlSIx1x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx1x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 134 ])

ctlSIx1x31 = Parameter(name = 'ctlSIx1x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx1x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 135 ])

ctlSIx1x32 = Parameter(name = 'ctlSIx1x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx1x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 136 ])

ctlSIx2x13 = Parameter(name = 'ctlSIx2x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx2x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 137 ])

ctlSIx2x23 = Parameter(name = 'ctlSIx2x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx2x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 138 ])

ctlSIx2x31 = Parameter(name = 'ctlSIx2x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx2x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 139 ])

ctlSIx2x32 = Parameter(name = 'ctlSIx2x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx2x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 140 ])

ctlSIx3x13 = Parameter(name = 'ctlSIx3x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx3x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 141 ])

ctlSIx3x23 = Parameter(name = 'ctlSIx3x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx3x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 142 ])

ctlSIx3x31 = Parameter(name = 'ctlSIx3x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx3x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 143 ])

ctlSIx3x32 = Parameter(name = 'ctlSIx3x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlSIx3x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 144 ])

ctlTx1x13 = Parameter(name = 'ctlTx1x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx1x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 145 ])

ctlTx1x23 = Parameter(name = 'ctlTx1x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx1x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 146 ])

ctlTx1x31 = Parameter(name = 'ctlTx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 147 ])

ctlTx1x32 = Parameter(name = 'ctlTx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 148 ])

ctlTx2x13 = Parameter(name = 'ctlTx2x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx2x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 149 ])

ctlTx2x23 = Parameter(name = 'ctlTx2x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx2x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 150 ])

ctlTx2x31 = Parameter(name = 'ctlTx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 151 ])

ctlTx2x32 = Parameter(name = 'ctlTx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 152 ])

ctlTx3x13 = Parameter(name = 'ctlTx3x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx3x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 153 ])

ctlTx3x23 = Parameter(name = 'ctlTx3x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx3x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 154 ])

ctlTx3x31 = Parameter(name = 'ctlTx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 155 ])

ctlTx3x32 = Parameter(name = 'ctlTx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{ctlTx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 156 ])

ctlTIx1x13 = Parameter(name = 'ctlTIx1x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx1x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 157 ])

ctlTIx1x23 = Parameter(name = 'ctlTIx1x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx1x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 158 ])

ctlTIx1x31 = Parameter(name = 'ctlTIx1x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx1x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 159 ])

ctlTIx1x32 = Parameter(name = 'ctlTIx1x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx1x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 160 ])

ctlTIx2x13 = Parameter(name = 'ctlTIx2x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx2x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 161 ])

ctlTIx2x23 = Parameter(name = 'ctlTIx2x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx2x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 162 ])

ctlTIx2x31 = Parameter(name = 'ctlTIx2x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx2x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 163 ])

ctlTIx2x32 = Parameter(name = 'ctlTIx2x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx2x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 164 ])

ctlTIx3x13 = Parameter(name = 'ctlTIx3x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx3x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 165 ])

ctlTIx3x23 = Parameter(name = 'ctlTIx3x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx3x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 166 ])

ctlTIx3x31 = Parameter(name = 'ctlTIx3x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx3x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 167 ])

ctlTIx3x32 = Parameter(name = 'ctlTIx3x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{ctlTIx3x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 168 ])

cqq11x3331 = Parameter(name = 'cqq11x3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq11x3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 169 ])

cqq11x3332 = Parameter(name = 'cqq11x3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq11x3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 170 ])

cqq11Ix3331 = Parameter(name = 'cqq11Ix3331',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq11Ix3331}',
                        lhablock = 'FCNC',
                        lhacode = [ 171 ])

cqq11Ix3332 = Parameter(name = 'cqq11Ix3332',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq11Ix3332}',
                        lhablock = 'FCNC',
                        lhacode = [ 172 ])

cqq13x3331 = Parameter(name = 'cqq13x3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq13x3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 173 ])

cqq13x3332 = Parameter(name = 'cqq13x3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq13x3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 174 ])

cqq13Ix3331 = Parameter(name = 'cqq13Ix3331',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq13Ix3331}',
                        lhablock = 'FCNC',
                        lhacode = [ 175 ])

cqq13Ix3332 = Parameter(name = 'cqq13Ix3332',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq13Ix3332}',
                        lhablock = 'FCNC',
                        lhacode = [ 176 ])

cuu1x3331 = Parameter(name = 'cuu1x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu1x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 177 ])

cuu1x3332 = Parameter(name = 'cuu1x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu1x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 178 ])

cuu1Ix3331 = Parameter(name = 'cuu1Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu1Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 179 ])

cuu1Ix3332 = Parameter(name = 'cuu1Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu1Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 180 ])

cqu1x3331 = Parameter(name = 'cqu1x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 181 ])

cqu1x3332 = Parameter(name = 'cqu1x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 182 ])

cqu1Ix3331 = Parameter(name = 'cqu1Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 183 ])

cqu1Ix3332 = Parameter(name = 'cqu1Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 184 ])

cqu1x3133 = Parameter(name = 'cqu1x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 185 ])

cqu1x3233 = Parameter(name = 'cqu1x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 186 ])

cqu1Ix3133 = Parameter(name = 'cqu1Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 187 ])

cqu1Ix3233 = Parameter(name = 'cqu1Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 188 ])

cqu8x3331 = Parameter(name = 'cqu8x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 189 ])

cqu8x3332 = Parameter(name = 'cqu8x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 190 ])

cqu8Ix3331 = Parameter(name = 'cqu8Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 191 ])

cqu8Ix3332 = Parameter(name = 'cqu8Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 192 ])

cqu8x3233 = Parameter(name = 'cqu8x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 193 ])

cqu8x3133 = Parameter(name = 'cqu8x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 194 ])

cqu8Ix3133 = Parameter(name = 'cqu8Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 195 ])

cqu8Ix3233 = Parameter(name = 'cqu8Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 196 ])

cqd1x3331 = Parameter(name = 'cqd1x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 197 ])

cqd1x3332 = Parameter(name = 'cqd1x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 198 ])

cqd1Ix3331 = Parameter(name = 'cqd1Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 199 ])

cqd1Ix3332 = Parameter(name = 'cqd1Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 200 ])

cqd1x3133 = Parameter(name = 'cqd1x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 201 ])

cqd1x3233 = Parameter(name = 'cqd1x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 202 ])

cqd1Ix3133 = Parameter(name = 'cqd1Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 203 ])

cqd1Ix3233 = Parameter(name = 'cqd1Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 204 ])

cqd8x3331 = Parameter(name = 'cqd8x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 205 ])

cqd8x3332 = Parameter(name = 'cqd8x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 206 ])

cqd8Ix3331 = Parameter(name = 'cqd8Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 207 ])

cqd8Ix3332 = Parameter(name = 'cqd8Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 208 ])

cqd8x3133 = Parameter(name = 'cqd8x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 209 ])

cqd8x3233 = Parameter(name = 'cqd8x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 210 ])

cqd8Ix3133 = Parameter(name = 'cqd8Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 211 ])

cqd8Ix3233 = Parameter(name = 'cqd8Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 212 ])

cud1x3331 = Parameter(name = 'cud1x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 213 ])

cud1x3332 = Parameter(name = 'cud1x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 214 ])

cud1Ix3331 = Parameter(name = 'cud1Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 215 ])

cud1Ix3332 = Parameter(name = 'cud1Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 216 ])

cud1x3133 = Parameter(name = 'cud1x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 217 ])

cud1x3233 = Parameter(name = 'cud1x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 218 ])

cud1Ix3133 = Parameter(name = 'cud1Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 219 ])

cud1Ix3233 = Parameter(name = 'cud1Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 220 ])

cud8x3331 = Parameter(name = 'cud8x3331',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x3331}',
                      lhablock = 'FCNC',
                      lhacode = [ 221 ])

cud8x3332 = Parameter(name = 'cud8x3332',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x3332}',
                      lhablock = 'FCNC',
                      lhacode = [ 222 ])

cud8Ix3331 = Parameter(name = 'cud8Ix3331',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix3331}',
                       lhablock = 'FCNC',
                       lhacode = [ 223 ])

cud8Ix3332 = Parameter(name = 'cud8Ix3332',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix3332}',
                       lhablock = 'FCNC',
                       lhacode = [ 224 ])

cud8x3133 = Parameter(name = 'cud8x3133',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x3133}',
                      lhablock = 'FCNC',
                      lhacode = [ 225 ])

cud8x3233 = Parameter(name = 'cud8x3233',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x3233}',
                      lhablock = 'FCNC',
                      lhacode = [ 226 ])

cud8Ix3133 = Parameter(name = 'cud8Ix3133',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix3133}',
                       lhablock = 'FCNC',
                       lhacode = [ 227 ])

cud8Ix3233 = Parameter(name = 'cud8Ix3233',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix3233}',
                       lhablock = 'FCNC',
                       lhacode = [ 228 ])

cquqd1x3331 = Parameter(name = 'cquqd1x3331',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3331}',
                        lhablock = 'FCNC',
                        lhacode = [ 229 ])

cquqd1x3332 = Parameter(name = 'cquqd1x3332',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3332}',
                        lhablock = 'FCNC',
                        lhacode = [ 230 ])

cquqd1x3313 = Parameter(name = 'cquqd1x3313',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3313}',
                        lhablock = 'FCNC',
                        lhacode = [ 231 ])

cquqd1x3323 = Parameter(name = 'cquqd1x3323',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3323}',
                        lhablock = 'FCNC',
                        lhacode = [ 232 ])

cquqd1x3133 = Parameter(name = 'cquqd1x3133',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3133}',
                        lhablock = 'FCNC',
                        lhacode = [ 233 ])

cquqd1x3233 = Parameter(name = 'cquqd1x3233',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x3233}',
                        lhablock = 'FCNC',
                        lhacode = [ 234 ])

cquqd1x1333 = Parameter(name = 'cquqd1x1333',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x1333}',
                        lhablock = 'FCNC',
                        lhacode = [ 235 ])

cquqd1x2333 = Parameter(name = 'cquqd1x2333',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd1x2333}',
                        lhablock = 'FCNC',
                        lhacode = [ 236 ])

cquqd1Ix3331 = Parameter(name = 'cquqd1Ix3331',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3331}',
                         lhablock = 'FCNC',
                         lhacode = [ 237 ])

cquqd1Ix3332 = Parameter(name = 'cquqd1Ix3332',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3332}',
                         lhablock = 'FCNC',
                         lhacode = [ 238 ])

cquqd1Ix3313 = Parameter(name = 'cquqd1Ix3313',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3313}',
                         lhablock = 'FCNC',
                         lhacode = [ 239 ])

cquqd1Ix3323 = Parameter(name = 'cquqd1Ix3323',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3323}',
                         lhablock = 'FCNC',
                         lhacode = [ 240 ])

cquqd1Ix3133 = Parameter(name = 'cquqd1Ix3133',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3133}',
                         lhablock = 'FCNC',
                         lhacode = [ 241 ])

cquqd1Ix3233 = Parameter(name = 'cquqd1Ix3233',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix3233}',
                         lhablock = 'FCNC',
                         lhacode = [ 242 ])

cquqd1Ix1333 = Parameter(name = 'cquqd1Ix1333',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix1333}',
                         lhablock = 'FCNC',
                         lhacode = [ 243 ])

cquqd1Ix2333 = Parameter(name = 'cquqd1Ix2333',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd1Ix2333}',
                         lhablock = 'FCNC',
                         lhacode = [ 244 ])

cquqd8x3331 = Parameter(name = 'cquqd8x3331',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3331}',
                        lhablock = 'FCNC',
                        lhacode = [ 245 ])

cquqd8x3332 = Parameter(name = 'cquqd8x3332',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3332}',
                        lhablock = 'FCNC',
                        lhacode = [ 246 ])

cquqd8x3313 = Parameter(name = 'cquqd8x3313',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3313}',
                        lhablock = 'FCNC',
                        lhacode = [ 247 ])

cquqd8x3323 = Parameter(name = 'cquqd8x3323',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3323}',
                        lhablock = 'FCNC',
                        lhacode = [ 248 ])

cquqd8x3133 = Parameter(name = 'cquqd8x3133',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3133}',
                        lhablock = 'FCNC',
                        lhacode = [ 249 ])

cquqd8x3233 = Parameter(name = 'cquqd8x3233',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x3233}',
                        lhablock = 'FCNC',
                        lhacode = [ 250 ])

cquqd8x1333 = Parameter(name = 'cquqd8x1333',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x1333}',
                        lhablock = 'FCNC',
                        lhacode = [ 251 ])

cquqd8x2333 = Parameter(name = 'cquqd8x2333',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cquqd8x2333}',
                        lhablock = 'FCNC',
                        lhacode = [ 252 ])

cquqd8Ix3331 = Parameter(name = 'cquqd8Ix3331',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3331}',
                         lhablock = 'FCNC',
                         lhacode = [ 253 ])

cquqd8Ix3332 = Parameter(name = 'cquqd8Ix3332',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3332}',
                         lhablock = 'FCNC',
                         lhacode = [ 254 ])

cquqd8Ix3313 = Parameter(name = 'cquqd8Ix3313',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3313}',
                         lhablock = 'FCNC',
                         lhacode = [ 255 ])

cquqd8Ix3323 = Parameter(name = 'cquqd8Ix3323',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3323}',
                         lhablock = 'FCNC',
                         lhacode = [ 256 ])

cquqd8Ix3133 = Parameter(name = 'cquqd8Ix3133',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3133}',
                         lhablock = 'FCNC',
                         lhacode = [ 257 ])

cquqd8Ix3233 = Parameter(name = 'cquqd8Ix3233',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix3233}',
                         lhablock = 'FCNC',
                         lhacode = [ 258 ])

cquqd8Ix1333 = Parameter(name = 'cquqd8Ix1333',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix1333}',
                         lhablock = 'FCNC',
                         lhacode = [ 259 ])

cquqd8Ix2333 = Parameter(name = 'cquqd8Ix2333',
                         nature = 'external',
                         type = 'real',
                         value = 0.,
                         texname = '\\text{cquqd8Ix2333}',
                         lhablock = 'FCNC',
                         lhacode = [ 260 ])

cqq11x31ii = Parameter(name = 'cqq11x31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq11x31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 261 ])

cqq11x32ii = Parameter(name = 'cqq11x32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq11x32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 262 ])

cqq11Ix31ii = Parameter(name = 'cqq11Ix31ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq11Ix31ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 263 ])

cqq11Ix32ii = Parameter(name = 'cqq11Ix32ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq11Ix32ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 264 ])

cqq13x31ii = Parameter(name = 'cqq13x31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq13x31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 265 ])

cqq13x32ii = Parameter(name = 'cqq13x32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq13x32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 266 ])

cqq13Ix31ii = Parameter(name = 'cqq13Ix31ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq13Ix31ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 267 ])

cqq13Ix32ii = Parameter(name = 'cqq13Ix32ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq13Ix32ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 268 ])

cqq81x31ii = Parameter(name = 'cqq81x31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq81x31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 269 ])

cqq81x32ii = Parameter(name = 'cqq81x32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq81x32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 270 ])

cqq81Ix31ii = Parameter(name = 'cqq81Ix31ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq81Ix31ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 271 ])

cqq81Ix32ii = Parameter(name = 'cqq81Ix32ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq81Ix32ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 272 ])

cqq83x31ii = Parameter(name = 'cqq83x31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq83x31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 273 ])

cqq83x32ii = Parameter(name = 'cqq83x32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqq83x32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 274 ])

cqq83Ix31ii = Parameter(name = 'cqq83Ix31ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq83Ix31ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 275 ])

cqq83Ix32ii = Parameter(name = 'cqq83Ix32ii',
                        nature = 'external',
                        type = 'real',
                        value = 0.,
                        texname = '\\text{cqq83Ix32ii}',
                        lhablock = 'FCNC',
                        lhacode = [ 276 ])

cuu1x31ii = Parameter(name = 'cuu1x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu1x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 277 ])

cuu1x32ii = Parameter(name = 'cuu1x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu1x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 278 ])

cuu1Ix31ii = Parameter(name = 'cuu1Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu1Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 279 ])

cuu1Ix32ii = Parameter(name = 'cuu1Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu1Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 280 ])

cuu8x31ii = Parameter(name = 'cuu8x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu8x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 281 ])

cuu8x32ii = Parameter(name = 'cuu8x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cuu8x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 282 ])

cuu8Ix31ii = Parameter(name = 'cuu8Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu8Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 283 ])

cuu8Ix32ii = Parameter(name = 'cuu8Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cuu8Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 284 ])

cud1x31ii = Parameter(name = 'cud1x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 285 ])

cud1x32ii = Parameter(name = 'cud1x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud1x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 286 ])

cud1Ix31ii = Parameter(name = 'cud1Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 287 ])

cud1Ix32ii = Parameter(name = 'cud1Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud1Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 288 ])

cud8x31ii = Parameter(name = 'cud8x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 289 ])

cud8x32ii = Parameter(name = 'cud8x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cud8x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 290 ])

cud8Ix31ii = Parameter(name = 'cud8Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 291 ])

cud8Ix32ii = Parameter(name = 'cud8Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cud8Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 292 ])

cqu1x31ii = Parameter(name = 'cqu1x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 293 ])

cqu1x32ii = Parameter(name = 'cqu1x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 294 ])

cqu1Ix31ii = Parameter(name = 'cqu1Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 295 ])

cqu1Ix32ii = Parameter(name = 'cqu1Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 296 ])

cqu8x31ii = Parameter(name = 'cqu8x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 297 ])

cqu8x32ii = Parameter(name = 'cqu8x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 298 ])

cqu8Ix31ii = Parameter(name = 'cqu8Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 299 ])

cqu8Ix32ii = Parameter(name = 'cqu8Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 300 ])

cqu1xii31 = Parameter(name = 'cqu1xii31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1xii31}',
                      lhablock = 'FCNC',
                      lhacode = [ 301 ])

cqu1xii32 = Parameter(name = 'cqu1xii32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu1xii32}',
                      lhablock = 'FCNC',
                      lhacode = [ 302 ])

cqu1Ixii31 = Parameter(name = 'cqu1Ixii31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ixii31}',
                       lhablock = 'FCNC',
                       lhacode = [ 303 ])

cqu1Ixii32 = Parameter(name = 'cqu1Ixii32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu1Ixii32}',
                       lhablock = 'FCNC',
                       lhacode = [ 304 ])

cqu8xii31 = Parameter(name = 'cqu8xii31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8xii31}',
                      lhablock = 'FCNC',
                      lhacode = [ 305 ])

cqu8xii32 = Parameter(name = 'cqu8xii32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqu8xii32}',
                      lhablock = 'FCNC',
                      lhacode = [ 306 ])

cqu8Ixii31 = Parameter(name = 'cqu8Ixii31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ixii31}',
                       lhablock = 'FCNC',
                       lhacode = [ 307 ])

cqu8Ixii32 = Parameter(name = 'cqu8Ixii32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqu8Ixii32}',
                       lhablock = 'FCNC',
                       lhacode = [ 308 ])

cqd1x31ii = Parameter(name = 'cqd1x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 309 ])

cqd1x32ii = Parameter(name = 'cqd1x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd1x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 310 ])

cqd1Ix31ii = Parameter(name = 'cqd1Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 311 ])

cqd1Ix32ii = Parameter(name = 'cqd1Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd1Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 312 ])

cqd8Ix31ii = Parameter(name = 'cqd8Ix31ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix31ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 313 ])

cqd8Ix32ii = Parameter(name = 'cqd8Ix32ii',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cqd8Ix32ii}',
                       lhablock = 'FCNC',
                       lhacode = [ 314 ])

cqd8x31ii = Parameter(name = 'cqd8x31ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x31ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 315 ])

cqd8x32ii = Parameter(name = 'cqd8x32ii',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cqd8x32ii}',
                      lhablock = 'FCNC',
                      lhacode = [ 316 ])

cpbIx31 = Parameter(name = 'cpbIx31',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpbIx31}',
                    lhablock = 'FCNC',
                    lhacode = [ 317 ])

cpbIx32 = Parameter(name = 'cpbIx32',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cpbIx32}',
                    lhablock = 'FCNC',
                    lhacode = [ 318 ])

cpbx31 = Parameter(name = 'cpbx31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cpbx31}',
                   lhablock = 'FCNC',
                   lhacode = [ 319 ])

cpbx32 = Parameter(name = 'cpbx32',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cpbx32}',
                   lhablock = 'FCNC',
                   lhacode = [ 320 ])

cblSx1x13 = Parameter(name = 'cblSx1x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx1x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 321 ])

cblSx1x23 = Parameter(name = 'cblSx1x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx1x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 322 ])

cblSx1x31 = Parameter(name = 'cblSx1x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx1x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 323 ])

cblSx1x32 = Parameter(name = 'cblSx1x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx1x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 324 ])

cblSx2x13 = Parameter(name = 'cblSx2x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx2x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 325 ])

cblSx2x23 = Parameter(name = 'cblSx2x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx2x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 326 ])

cblSx2x31 = Parameter(name = 'cblSx2x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx2x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 327 ])

cblSx2x32 = Parameter(name = 'cblSx2x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx2x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 328 ])

cblSx3x13 = Parameter(name = 'cblSx3x13',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx3x13}',
                      lhablock = 'FCNC',
                      lhacode = [ 329 ])

cblSx3x23 = Parameter(name = 'cblSx3x23',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx3x23}',
                      lhablock = 'FCNC',
                      lhacode = [ 330 ])

cblSx3x31 = Parameter(name = 'cblSx3x31',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx3x31}',
                      lhablock = 'FCNC',
                      lhacode = [ 331 ])

cblSx3x32 = Parameter(name = 'cblSx3x32',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{cblSx3x32}',
                      lhablock = 'FCNC',
                      lhacode = [ 332 ])

cblSIx1x13 = Parameter(name = 'cblSIx1x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx1x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 333 ])

cblSIx1x23 = Parameter(name = 'cblSIx1x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx1x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 334 ])

cblSIx1x31 = Parameter(name = 'cblSIx1x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx1x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 335 ])

cblSIx1x32 = Parameter(name = 'cblSIx1x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx1x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 336 ])

cblSIx2x13 = Parameter(name = 'cblSIx2x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx2x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 337 ])

cblSIx2x23 = Parameter(name = 'cblSIx2x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx2x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 338 ])

cblSIx2x31 = Parameter(name = 'cblSIx2x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx2x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 339 ])

cblSIx2x32 = Parameter(name = 'cblSIx2x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx2x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 340 ])

cblSIx3x13 = Parameter(name = 'cblSIx3x13',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx3x13}',
                       lhablock = 'FCNC',
                       lhacode = [ 341 ])

cblSIx3x23 = Parameter(name = 'cblSIx3x23',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx3x23}',
                       lhablock = 'FCNC',
                       lhacode = [ 342 ])

cblSIx3x31 = Parameter(name = 'cblSIx3x31',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx3x31}',
                       lhablock = 'FCNC',
                       lhacode = [ 343 ])

cblSIx3x32 = Parameter(name = 'cblSIx3x32',
                       nature = 'external',
                       type = 'real',
                       value = 0.,
                       texname = '\\text{cblSIx3x32}',
                       lhablock = 'FCNC',
                       lhacode = [ 344 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

sq2 = Parameter(name = 'sq2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(2)',
                texname = '\\text{sq2}')

cQQplus = Parameter(name = 'cQQplus',
                    nature = 'internal',
                    type = 'real',
                    value = 'cQQ1/2+cQQ8/6',
                    texname = '\\text{cQQplus}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Gstrong = Parameter(name = 'Gstrong',
                    nature = 'internal',
                    type = 'real',
                    value = 'G' if configuration.norm_chromo_gs else '1.',
                    texname = '\\text{Gstrong}')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '1./cmath.sqrt(Gf*cmath.sqrt(2))',
                texname = '\\text{vev}')

if configuration.mw_ew_input:
    MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 79.8244,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])
else:
    aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])
    aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')
    MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

ee = Parameter(name = 'ee',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/vev' if configuration.mw_ew_input else '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
                texname = 'e')

ctA = Parameter(name = 'ctA',
                nature = 'internal',
                type = 'real',
                value = '(ctW-cw*ctZ)/sw',
                texname = '\\text{ctA}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

