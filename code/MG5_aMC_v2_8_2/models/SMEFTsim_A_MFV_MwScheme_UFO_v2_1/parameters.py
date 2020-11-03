# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Sat 10 Mar 2018 00:31:47



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

CKMlambda = Parameter(name = 'CKMlambda',
                      nature = 'external',
                      type = 'real',
                      value = 0.22506,
                      texname = '\\text{CKMlambda}',
                      lhablock = 'CKMBLOCK',
                      lhacode = [ 2 ])

CKMA = Parameter(name = 'CKMA',
                 nature = 'external',
                 type = 'real',
                 value = 0.811,
                 texname = '\\text{CKMA}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 3 ])

CKMrho = Parameter(name = 'CKMrho',
                   nature = 'external',
                   type = 'real',
                   value = 0.124,
                   texname = '\\text{CKMrho}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 4 ])

CKMeta = Parameter(name = 'CKMeta',
                   nature = 'external',
                   type = 'real',
                   value = 0.356,
                   texname = '\\text{CKMeta}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 5 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1181,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.0047,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0022,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.096,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.28,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 173.2,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

LambdaSMEFT = Parameter(name = 'LambdaSMEFT',
                        nature = 'external',
                        type = 'real',
                        value = 1000,
                        texname = '\\Lambda',
                        lhablock = 'FRBlock',
                        lhacode = [ 1 ])

cG = Parameter(name = 'cG',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = 'c_G',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

cW = Parameter(name = 'cW',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = 'c_W',
               lhablock = 'FRBlock',
               lhacode = [ 3 ])

cH = Parameter(name = 'cH',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = 'c_H',
               lhablock = 'FRBlock',
               lhacode = [ 4 ])

cHbox = Parameter(name = 'cHbox',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'c_{H \\square }',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

cHDD = Parameter(name = 'cHDD',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{HD}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 6 ])

cHG = Parameter(name = 'cHG',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{HG}}',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

cHW = Parameter(name = 'cHW',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{HW}}',
                lhablock = 'FRBlock',
                lhacode = [ 8 ])

cHB = Parameter(name = 'cHB',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{HB}}',
                lhablock = 'FRBlock',
                lhacode = [ 9 ])

cHWB = Parameter(name = 'cHWB',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{HWB}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 10 ])

ceH = Parameter(name = 'ceH',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{eH}}',
                lhablock = 'FRBlock',
                lhacode = [ 11 ])

cuH0 = Parameter(name = 'cuH0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{uH}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 12 ])

cdH0 = Parameter(name = 'cdH0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{dH}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 13 ])

DeltacuH = Parameter(name = 'DeltacuH',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{uH}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

DeltacdH = Parameter(name = 'DeltacdH',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{dH}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ceW = Parameter(name = 'ceW',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{eW}}',
                lhablock = 'FRBlock',
                lhacode = [ 16 ])

ceB = Parameter(name = 'ceB',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{eB}}',
                lhablock = 'FRBlock',
                lhacode = [ 17 ])

cuG0 = Parameter(name = 'cuG0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{uG}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 18 ])

DeltacuG = Parameter(name = 'DeltacuG',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{uG}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 19 ])

cuW0 = Parameter(name = 'cuW0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{uW}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 20 ])

DeltacuW = Parameter(name = 'DeltacuW',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{uW}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 21 ])

cuB0 = Parameter(name = 'cuB0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{uB}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 22 ])

DeltacuB = Parameter(name = 'DeltacuB',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{uB}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 23 ])

cdG0 = Parameter(name = 'cdG0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{dG}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 24 ])

DeltacdG = Parameter(name = 'DeltacdG',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{dG}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 25 ])

cdW0 = Parameter(name = 'cdW0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{dW}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 26 ])

DeltacdW = Parameter(name = 'DeltacdW',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{dW}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 27 ])

cdB0 = Parameter(name = 'cdB0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{dB}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 28 ])

DeltacdB = Parameter(name = 'DeltacdB',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{dB}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 29 ])

cHl1 = Parameter(name = 'cHl1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Subsuperscript}[c,\\text{Hl},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 30 ])

cHl3 = Parameter(name = 'cHl3',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Subsuperscript}[c,\\text{Hl},3]',
                 lhablock = 'FRBlock',
                 lhacode = [ 31 ])

cHe = Parameter(name = 'cHe',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{He}}',
                lhablock = 'FRBlock',
                lhacode = [ 32 ])

cHq10 = Parameter(name = 'cHq10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{Hq},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 33 ])

DeltaucHq1 = Parameter(name = 'DeltaucHq1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{Hq},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 34 ])

DeltadcHq1 = Parameter(name = 'DeltadcHq1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{Hq},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 35 ])

cHq30 = Parameter(name = 'cHq30',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{Hq},3]',
                  lhablock = 'FRBlock',
                  lhacode = [ 36 ])

DeltaucHq3 = Parameter(name = 'DeltaucHq3',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{Hq},3]',
                       lhablock = 'FRBlock',
                       lhacode = [ 37 ])

DeltadcHq3 = Parameter(name = 'DeltadcHq3',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{Hq},3]',
                       lhablock = 'FRBlock',
                       lhacode = [ 38 ])

cHu0 = Parameter(name = 'cHu0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{Hu}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 39 ])

DeltacHu = Parameter(name = 'DeltacHu',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{Hu}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 40 ])

cHd0 = Parameter(name = 'cHd0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{Hd}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 41 ])

DeltacHd = Parameter(name = 'DeltacHd',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{Hd}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 42 ])

cHud = Parameter(name = 'cHud',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{Hud}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 43 ])

cll = Parameter(name = 'cll',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{ll}}',
                lhablock = 'FRBlock',
                lhacode = [ 44 ])

cll1 = Parameter(name = 'cll1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Subsuperscript}[c,\\text{ll},\\text{Prime}]',
                 lhablock = 'FRBlock',
                 lhacode = [ 45 ])

cqq10 = Parameter(name = 'cqq10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qq},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 46 ])

Delta1ucqq1 = Parameter(name = 'Delta1ucqq1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{qq},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 47 ])

Delta1dcqq1 = Parameter(name = 'Delta1dcqq1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{qq},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 48 ])

Delta2ucqq1 = Parameter(name = 'Delta2ucqq1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{2 u} \\text{Subsuperscript}[c,\\text{qq},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 49 ])

Delta2dcqq1 = Parameter(name = 'Delta2dcqq1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{2 d} \\text{Subsuperscript}[c,\\text{qq},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 50 ])

cqq110 = Parameter(name = 'cqq110',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                   lhablock = 'FRBlock',
                   lhacode = [ 51 ])

Delta1ucqq11 = Parameter(name = 'Delta1ucqq11',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 52 ])

Delta1dcqq11 = Parameter(name = 'Delta1dcqq11',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 53 ])

Delta2ucqq11 = Parameter(name = 'Delta2ucqq11',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _{2 u} \\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 54 ])

Delta2dcqq11 = Parameter(name = 'Delta2dcqq11',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _{2 d} \\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 55 ])

cqq30 = Parameter(name = 'cqq30',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qq},3]',
                  lhablock = 'FRBlock',
                  lhacode = [ 56 ])

Delta1ucqq3 = Parameter(name = 'Delta1ucqq3',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{qq},3]',
                        lhablock = 'FRBlock',
                        lhacode = [ 57 ])

Delta1dcqq3 = Parameter(name = 'Delta1dcqq3',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{qq},3]',
                        lhablock = 'FRBlock',
                        lhacode = [ 58 ])

Delta2ucqq3 = Parameter(name = 'Delta2ucqq3',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{2 u} \\text{Subsuperscript}[c,\\text{qq},3]',
                        lhablock = 'FRBlock',
                        lhacode = [ 59 ])

Delta2dcqq3 = Parameter(name = 'Delta2dcqq3',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{2 d} \\text{Subsuperscript}[c,\\text{qq},3]',
                        lhablock = 'FRBlock',
                        lhacode = [ 60 ])

cqq310 = Parameter(name = 'cqq310',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                   lhablock = 'FRBlock',
                   lhacode = [ 61 ])

Delta1ucqq31 = Parameter(name = 'Delta1ucqq31',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 62 ])

Delta1dcqq31 = Parameter(name = 'Delta1dcqq31',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 63 ])

Delta2ucqq31 = Parameter(name = 'Delta2ucqq31',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _{2 u} \\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 64 ])

Delta2dcqq31 = Parameter(name = 'Delta2dcqq31',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _{2 d} \\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                         lhablock = 'FRBlock',
                         lhacode = [ 65 ])

clq10 = Parameter(name = 'clq10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{lq},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 66 ])

Deltauclq1 = Parameter(name = 'Deltauclq1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{lq},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 67 ])

Deltadclq1 = Parameter(name = 'Deltadclq1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{lq},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 68 ])

clq30 = Parameter(name = 'clq30',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{lq},3]',
                  lhablock = 'FRBlock',
                  lhacode = [ 69 ])

Deltauclq3 = Parameter(name = 'Deltauclq3',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _u \\text{Subsuperscript}[c,\\text{lq},3]',
                       lhablock = 'FRBlock',
                       lhacode = [ 70 ])

Deltadclq3 = Parameter(name = 'Deltadclq3',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _d \\text{Subsuperscript}[c,\\text{lq},3]',
                       lhablock = 'FRBlock',
                       lhacode = [ 71 ])

cee = Parameter(name = 'cee',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{e^2}',
                lhablock = 'FRBlock',
                lhacode = [ 72 ])

cuu0 = Parameter(name = 'cuu0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{uu}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 73 ])

Delta1cuu = Parameter(name = 'Delta1cuu',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _1 c_{\\text{uu}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 74 ])

Delta2cuu = Parameter(name = 'Delta2cuu',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _2 c_{\\text{uu}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 75 ])

cuu10 = Parameter(name = 'cuu10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{uu},\\text{Prime}]',
                  lhablock = 'FRBlock',
                  lhacode = [ 76 ])

Delta1cuu1 = Parameter(name = 'Delta1cuu1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{uu},\\text{Prime}]',
                       lhablock = 'FRBlock',
                       lhacode = [ 77 ])

Delta2cuu1 = Parameter(name = 'Delta2cuu1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{uu},\\text{Prime}]',
                       lhablock = 'FRBlock',
                       lhacode = [ 78 ])

cdd0 = Parameter(name = 'cdd0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{dd}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 79 ])

Delta1cdd = Parameter(name = 'Delta1cdd',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _1 c_{\\text{dd}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 80 ])

Delta2cdd = Parameter(name = 'Delta2cdd',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _2 c_{\\text{dd}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 81 ])

cdd10 = Parameter(name = 'cdd10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{dd},\\text{Prime}]',
                  lhablock = 'FRBlock',
                  lhacode = [ 82 ])

Delta1cdd1 = Parameter(name = 'Delta1cdd1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{dd},\\text{Prime}]',
                       lhablock = 'FRBlock',
                       lhacode = [ 83 ])

Delta2cdd1 = Parameter(name = 'Delta2cdd1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{dd},\\text{Prime}]',
                       lhablock = 'FRBlock',
                       lhacode = [ 84 ])

ceu0 = Parameter(name = 'ceu0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{eu}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 85 ])

Deltaceu = Parameter(name = 'Deltaceu',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{eu}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 86 ])

ced0 = Parameter(name = 'ced0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{ed}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 87 ])

Deltaced = Parameter(name = 'Deltaced',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{ed}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 88 ])

cud10 = Parameter(name = 'cud10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{ud},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 89 ])

Delta1cud1 = Parameter(name = 'Delta1cud1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{ud},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 90 ])

Delta2cud1 = Parameter(name = 'Delta2cud1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{ud},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 91 ])

cud80 = Parameter(name = 'cud80',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{ud},8]',
                  lhablock = 'FRBlock',
                  lhacode = [ 92 ])

Delta1cud8 = Parameter(name = 'Delta1cud8',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{ud},8]',
                       lhablock = 'FRBlock',
                       lhacode = [ 93 ])

Delta2cud8 = Parameter(name = 'Delta2cud8',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{ud},8]',
                       lhablock = 'FRBlock',
                       lhacode = [ 94 ])

cle = Parameter(name = 'cle',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = 'c_{\\text{le}}',
                lhablock = 'FRBlock',
                lhacode = [ 95 ])

clu0 = Parameter(name = 'clu0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{lu}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 96 ])

Deltaclu = Parameter(name = 'Deltaclu',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{lu}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 97 ])

cld0 = Parameter(name = 'cld0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{ld}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 98 ])

Deltacld = Parameter(name = 'Deltacld',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\Delta $c}_{\\text{ld}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 99 ])

cqe0 = Parameter(name = 'cqe0',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'c_{\\text{qe}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 100 ])

Deltaucqe = Parameter(name = 'Deltaucqe',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _u c_{\\text{qe}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 101 ])

Deltadcqe = Parameter(name = 'Deltadcqe',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\Delta _d c_{\\text{qe}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 102 ])

cqu10 = Parameter(name = 'cqu10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qu},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 103 ])

Delta1ucqu1 = Parameter(name = 'Delta1ucqu1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 u} \\text{Subsuperscript}[c,\\text{qu},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 104 ])

Delta1dcqu1 = Parameter(name = 'Delta1dcqu1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 d} \\text{Subsuperscript}[c,\\text{qu},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 105 ])

Delta2cqu1 = Parameter(name = 'Delta2cqu1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{qu},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 106 ])

cqu80 = Parameter(name = 'cqu80',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qu},8]',
                  lhablock = 'FRBlock',
                  lhacode = [ 107 ])

Delta1ucqu8 = Parameter(name = 'Delta1ucqu8',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 u} \\text{Subsuperscript}[c,\\text{qu},8]',
                        lhablock = 'FRBlock',
                        lhacode = [ 108 ])

Delta1dcqu8 = Parameter(name = 'Delta1dcqu8',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 d} \\text{Subsuperscript}[c,\\text{qu},8]',
                        lhablock = 'FRBlock',
                        lhacode = [ 109 ])

Delta2cqu8 = Parameter(name = 'Delta2cqu8',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{qu},8]',
                       lhablock = 'FRBlock',
                       lhacode = [ 110 ])

cqd10 = Parameter(name = 'cqd10',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qd},1]',
                  lhablock = 'FRBlock',
                  lhacode = [ 111 ])

Delta1ucqd1 = Parameter(name = 'Delta1ucqd1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 u} \\text{Subsuperscript}[c,\\text{qd},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 112 ])

Delta1dcqd1 = Parameter(name = 'Delta1dcqd1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 d} \\text{Subsuperscript}[c,\\text{qd},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 113 ])

Delta2cqd1 = Parameter(name = 'Delta2cqd1',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{qd},1]',
                       lhablock = 'FRBlock',
                       lhacode = [ 114 ])

cqd80 = Parameter(name = 'cqd80',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Subsuperscript}[c,\\text{qd},8]',
                  lhablock = 'FRBlock',
                  lhacode = [ 115 ])

Delta1ucqd8 = Parameter(name = 'Delta1ucqd8',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 u} \\text{Subsuperscript}[c,\\text{qd},8]',
                        lhablock = 'FRBlock',
                        lhacode = [ 116 ])

Delta1dcqd8 = Parameter(name = 'Delta1dcqd8',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\Delta _{1 d} \\text{Subsuperscript}[c,\\text{qd},8]',
                        lhablock = 'FRBlock',
                        lhacode = [ 117 ])

Delta2cqd8 = Parameter(name = 'Delta2cqd8',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{qd},8]',
                       lhablock = 'FRBlock',
                       lhacode = [ 118 ])

cledq0 = Parameter(name = 'cledq0',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'c_{\\text{leqd}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 119 ])

Deltacledq = Parameter(name = 'Deltacledq',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\text{$\\Delta $c}_{\\text{leqd}}',
                       lhablock = 'FRBlock',
                       lhacode = [ 120 ])

cquqd10 = Parameter(name = 'cquqd10',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Subsuperscript}[c,\\text{quqd},1]',
                    lhablock = 'FRBlock',
                    lhacode = [ 121 ])

Delta1cquqd1 = Parameter(name = 'Delta1cquqd1',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{quqd},1]',
                         lhablock = 'FRBlock',
                         lhacode = [ 122 ])

Delta2cquqd1 = Parameter(name = 'Delta2cquqd1',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{quqd},1]',
                         lhablock = 'FRBlock',
                         lhacode = [ 123 ])

cquqd80 = Parameter(name = 'cquqd80',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Subsuperscript}[c,\\text{quqd},8]',
                    lhablock = 'FRBlock',
                    lhacode = [ 124 ])

Delta1cquqd8 = Parameter(name = 'Delta1cquqd8',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _1 \\text{Subsuperscript}[c,\\text{quqd},8]',
                         lhablock = 'FRBlock',
                         lhacode = [ 125 ])

Delta2cquqd8 = Parameter(name = 'Delta2cquqd8',
                         nature = 'external',
                         type = 'real',
                         value = 1,
                         texname = '\\Delta _2 \\text{Subsuperscript}[c,\\text{quqd},8]',
                         lhablock = 'FRBlock',
                         lhacode = [ 126 ])

clequ10 = Parameter(name = 'clequ10',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Subsuperscript}[c,\\text{lequ},1]',
                    lhablock = 'FRBlock',
                    lhacode = [ 127 ])

Deltaclequ1 = Parameter(name = 'Deltaclequ1',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\text{Subsuperscript}[\\text{$\\Delta $c},\\text{lequ},1]',
                        lhablock = 'FRBlock',
                        lhacode = [ 128 ])

clequ30 = Parameter(name = 'clequ30',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Subsuperscript}[c,\\text{lequ},3]',
                    lhablock = 'FRBlock',
                    lhacode = [ 129 ])

Deltaclequ3 = Parameter(name = 'Deltaclequ3',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\text{Subsuperscript}[\\text{$\\Delta $c},\\text{lequ},3]',
                        lhablock = 'FRBlock',
                        lhacode = [ 130 ])

MW0 = Parameter(name = 'MW0',
                nature = 'external',
                type = 'real',
                value = 80.387,
                texname = 'M_W',
                lhablock = 'FRBlock',
                lhacode = [ 131 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0022,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.28,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.2,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.0047,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.096,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.18,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
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

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'MW0',
               texname = 'M_W')

vevhat = Parameter(name = 'vevhat',
                   nature = 'internal',
                   type = 'real',
                   value = '1/(2**0.25*cmath.sqrt(Gf))',
                   texname = '\\hat{v}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MH**2)/cmath.sqrt(2)',
                texname = '\\text{lam}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMlambda',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-CKMlambda',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**2',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(1 - CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMA*CKMlambda**2)',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

Su1x1 = Parameter(name = 'Su1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{Su1x1}')

Su2x2 = Parameter(name = 'Su2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{Su2x2}')

Sd1x1 = Parameter(name = 'Sd1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{Sd1x1}')

Sd2x2 = Parameter(name = 'Sd2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{Sd2x2}')

sth2 = Parameter(name = 'sth2',
                 nature = 'internal',
                 type = 'real',
                 value = '1 - MW**2/MZ**2',
                 texname = '\\text{sth2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MW**2*(1 - MW**2/MZ**2)*cmath.sqrt(2))/cmath.pi',
                texname = '\\alpha _{\\text{EW}}')

dGf = Parameter(name = 'dGf',
                nature = 'internal',
                type = 'real',
                value = '(vevhat**2*(-(cll1/cmath.sqrt(2)) + cHl3*cmath.sqrt(2)))/LambdaSMEFT**2',
                texname = '\\text{dGf}')

dMH2 = Parameter(name = 'dMH2',
                 nature = 'internal',
                 type = 'real',
                 value = '((2*cHbox - cHDD/2. - (3*cH)/(2.*lam))*MH**2*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMH2}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vevhat',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vevhat',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vevhat',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vevhat',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vevhat',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vevhat',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vevhat',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vevhat',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vevhat',
                texname = '\\text{yup}')

gHgg = Parameter(name = 'gHgg',
                 nature = 'internal',
                 type = 'real',
                 value = '(G**2*(0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2)))/(16.*cmath.pi**2)',
                 texname = 'g_{\\text{HGG}}')

barlam = Parameter(name = 'barlam',
                   nature = 'internal',
                   type = 'real',
                   value = 'lam*(1 - dMH2/MH**2 - dGf*cmath.sqrt(2))',
                   texname = '\\text{barlam}')

cth = Parameter(name = 'cth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - sth2)',
                texname = 'c_{\\theta }')

Sd3x3 = Parameter(name = 'Sd3x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'yb**2',
                  texname = '\\text{Sd3x3}')

sth = Parameter(name = 'sth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(sth2)',
                texname = 's_{\\theta }')

Su3x3 = Parameter(name = 'Su3x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'yt**2',
                  texname = '\\text{Su3x3}')

vevT = Parameter(name = 'vevT',
                 nature = 'internal',
                 type = 'real',
                 value = 'vevhat*(1 + dGf/cmath.sqrt(2))',
                 texname = '\\text{vevT}')

dgw = Parameter(name = 'dgw',
                nature = 'internal',
                type = 'real',
                value = '-(dGf/cmath.sqrt(2))',
                texname = '\\text{dgw}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gwsh = Parameter(name = 'gwsh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dgw - (cHW*vevhat**2)/LambdaSMEFT**2))/sth',
                 texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(1 - (3*cH*vevhat**2)/(8.*lam*LambdaSMEFT**2))*vevT',
                texname = '\\text{vev}')

dMZ2 = Parameter(name = 'dMZ2',
                 nature = 'internal',
                 type = 'real',
                 value = '(MZ**2*(cHDD/2. + 2*cHWB*cth*sth)*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMZ2}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cth',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sth',
               texname = 'g_w')

gHaa = Parameter(name = 'gHaa',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(-1.75 + (4*(0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2)))/3. - (29*MH**6)/(16800.*MW0**6) - (19*MH**4)/(1680.*MW0**4) - (11*MH**2)/(120.*MW0**2)))/(8.*cmath.pi**2)',
                 texname = 'g_{\\text{H$\\gamma \\gamma $}}')

gHza = Parameter(name = 'gHza',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(((0.4583333333333333 + (29*MH**6)/(100800.*MW0**6) + (19*MH**4)/(10080.*MW0**4) + (11*MH**2)/(720.*MW0**2) + (MH**4*MZ**2)/(2100.*MW0**6) + (MH**2*MZ**2)/(280.*MW0**4) + (7*MZ**2)/(180.*MW0**2) + (67*MH**2*MZ**4)/(100800.*MW0**6) + (53*MZ**4)/(10080.*MW0**4) + (43*MZ**6)/(50400.*MW0**6) - (31*cth**2)/(24.*sth**2) - (29*cth**2*MH**6)/(20160.*MW0**6*sth**2) - (19*cth**2*MH**4)/(2016.*MW0**4*sth**2) - (11*cth**2*MH**2)/(144.*MW0**2*sth**2) - (cth**2*MH**4*MZ**2)/(560.*MW0**6*sth**2) - (31*cth**2*MH**2*MZ**2)/(2520.*MW0**4*sth**2) - (cth**2*MZ**2)/(9.*MW0**2*sth**2) - (43*cth**2*MH**2*MZ**4)/(20160.*MW0**6*sth**2) - (17*cth**2*MZ**4)/(1120.*MW0**4*sth**2) - (5*cth**2*MZ**6)/(2016.*MW0**6*sth**2))*sth)/cth + ((0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2) + (MH**4*MZ**2)/(2400.*MT**6) + (MH**2*MZ**2)/(315.*MT**4) + (11*MZ**2)/(360.*MT**2) + (29*MH**2*MZ**4)/(50400.*MT**6) + (11*MZ**4)/(2520.*MT**4) + (37*MZ**6)/(50400.*MT**6))*(0.5 - (4*sth**2)/3.))/(cth*sth)))/(4.*cmath.pi**2)',
                 texname = 'g_{\\text{HZ$\\gamma $}}')

dg1 = Parameter(name = 'dg1',
                nature = 'internal',
                type = 'real',
                value = '(-(dMZ2/(MZ**2*sth**2)) - dGf*cmath.sqrt(2))/2.',
                texname = '\\text{dg1}')

g1sh = Parameter(name = 'g1sh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dg1 - (cHB*vevhat**2)/LambdaSMEFT**2))/cth',
                 texname = 'g_1')

dsth2 = Parameter(name = 'dsth2',
                  nature = 'internal',
                  type = 'real',
                  value = '2*cth**2*(dg1 - dgw)*sth**2 + (cHWB*cth*sth*(1 - 2*sth**2)*vevhat**2)/LambdaSMEFT**2',
                  texname = '\\text{dsth2}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd1x1*ydo',
                  texname = '\\text{I1a11}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd2x2*ys',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd3x3*yb',
                  texname = '\\text{I1a33}')

I10a11 = Parameter(name = 'I10a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*yup',
                   texname = '\\text{I10a11}')

I10a12 = Parameter(name = 'I10a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*yc',
                   texname = '\\text{I10a12}')

I10a13 = Parameter(name = 'I10a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*yt',
                   texname = '\\text{I10a13}')

I10a21 = Parameter(name = 'I10a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*yup',
                   texname = '\\text{I10a21}')

I10a22 = Parameter(name = 'I10a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*yc',
                   texname = '\\text{I10a22}')

I10a23 = Parameter(name = 'I10a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*yt',
                   texname = '\\text{I10a23}')

I10a31 = Parameter(name = 'I10a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yup',
                   texname = '\\text{I10a31}')

I10a32 = Parameter(name = 'I10a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*yc',
                   texname = '\\text{I10a32}')

I10a33 = Parameter(name = 'I10a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yt',
                   texname = '\\text{I10a33}')

I11a11 = Parameter(name = 'I11a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I11a11}')

I11a12 = Parameter(name = 'I11a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I11a12}')

I11a13 = Parameter(name = 'I11a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I11a13}')

I11a21 = Parameter(name = 'I11a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I11a21}')

I11a22 = Parameter(name = 'I11a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I11a22}')

I11a23 = Parameter(name = 'I11a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I11a23}')

I11a31 = Parameter(name = 'I11a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I11a31}')

I11a32 = Parameter(name = 'I11a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I11a32}')

I11a33 = Parameter(name = 'I11a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I11a33}')

I12a11 = Parameter(name = 'I12a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM1x1)',
                   texname = '\\text{I12a11}')

I12a12 = Parameter(name = 'I12a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM2x1)',
                   texname = '\\text{I12a12}')

I12a13 = Parameter(name = 'I12a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM3x1)',
                   texname = '\\text{I12a13}')

I12a21 = Parameter(name = 'I12a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM1x2)',
                   texname = '\\text{I12a21}')

I12a22 = Parameter(name = 'I12a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I12a22}')

I12a23 = Parameter(name = 'I12a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM3x2)',
                   texname = '\\text{I12a23}')

I12a31 = Parameter(name = 'I12a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM1x3)',
                   texname = '\\text{I12a31}')

I12a32 = Parameter(name = 'I12a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM2x3)',
                   texname = '\\text{I12a32}')

I12a33 = Parameter(name = 'I12a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I12a33}')

I13a11 = Parameter(name = 'I13a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM1x1)',
                   texname = '\\text{I13a11}')

I13a12 = Parameter(name = 'I13a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM2x1)',
                   texname = '\\text{I13a12}')

I13a13 = Parameter(name = 'I13a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM3x1)',
                   texname = '\\text{I13a13}')

I13a21 = Parameter(name = 'I13a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM1x2)',
                   texname = '\\text{I13a21}')

I13a22 = Parameter(name = 'I13a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I13a22}')

I13a23 = Parameter(name = 'I13a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM3x2)',
                   texname = '\\text{I13a23}')

I13a31 = Parameter(name = 'I13a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM1x3)',
                   texname = '\\text{I13a31}')

I13a32 = Parameter(name = 'I13a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM2x3)',
                   texname = '\\text{I13a32}')

I13a33 = Parameter(name = 'I13a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I13a33}')

I14a11 = Parameter(name = 'I14a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I14a11}')

I14a12 = Parameter(name = 'I14a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I14a12}')

I14a13 = Parameter(name = 'I14a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I14a13}')

I14a21 = Parameter(name = 'I14a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I14a21}')

I14a22 = Parameter(name = 'I14a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I14a22}')

I14a23 = Parameter(name = 'I14a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I14a23}')

I14a31 = Parameter(name = 'I14a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I14a31}')

I14a32 = Parameter(name = 'I14a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I14a32}')

I14a33 = Parameter(name = 'I14a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I14a33}')

I15a11 = Parameter(name = 'I15a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I15a11}')

I15a12 = Parameter(name = 'I15a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I15a12}')

I15a13 = Parameter(name = 'I15a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I15a13}')

I15a21 = Parameter(name = 'I15a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I15a21}')

I15a22 = Parameter(name = 'I15a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I15a22}')

I15a23 = Parameter(name = 'I15a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I15a23}')

I15a31 = Parameter(name = 'I15a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I15a31}')

I15a32 = Parameter(name = 'I15a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I15a32}')

I15a33 = Parameter(name = 'I15a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I15a33}')

I16a11 = Parameter(name = 'I16a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I16a11}')

I16a12 = Parameter(name = 'I16a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I16a12}')

I16a13 = Parameter(name = 'I16a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I16a13}')

I16a21 = Parameter(name = 'I16a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I16a21}')

I16a22 = Parameter(name = 'I16a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I16a22}')

I16a23 = Parameter(name = 'I16a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I16a23}')

I16a31 = Parameter(name = 'I16a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I16a31}')

I16a32 = Parameter(name = 'I16a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I16a32}')

I16a33 = Parameter(name = 'I16a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I16a33}')

I17a11 = Parameter(name = 'I17a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I17a11}')

I17a22 = Parameter(name = 'I17a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I17a22}')

I17a33 = Parameter(name = 'I17a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I17a33}')

I18a11 = Parameter(name = 'I18a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I18a11}')

I18a22 = Parameter(name = 'I18a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I18a22}')

I18a33 = Parameter(name = 'I18a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I18a33}')

I19a11 = Parameter(name = 'I19a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I19a11}')

I19a22 = Parameter(name = 'I19a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I19a22}')

I19a33 = Parameter(name = 'I19a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I19a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd1x1*ydo',
                  texname = '\\text{I2a11}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd2x2*ys',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd3x3*yb',
                  texname = '\\text{I2a33}')

I20a11 = Parameter(name = 'I20a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I20a11}')

I20a22 = Parameter(name = 'I20a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I20a22}')

I20a33 = Parameter(name = 'I20a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I20a33}')

I21a11 = Parameter(name = 'I21a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I21a11}')

I21a22 = Parameter(name = 'I21a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I21a22}')

I21a33 = Parameter(name = 'I21a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I21a33}')

I22a11 = Parameter(name = 'I22a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I22a11}')

I22a22 = Parameter(name = 'I22a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I22a22}')

I22a33 = Parameter(name = 'I22a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I22a33}')

I23a1 = Parameter(name = 'I23a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x1) + complexconjugate(CKM2x1) + complexconjugate(CKM3x1)',
                  texname = '\\text{I23a1}')

I23a2 = Parameter(name = 'I23a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x2) + complexconjugate(CKM2x2) + complexconjugate(CKM3x2)',
                  texname = '\\text{I23a2}')

I23a3 = Parameter(name = 'I23a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x3) + complexconjugate(CKM2x3) + complexconjugate(CKM3x3)',
                  texname = '\\text{I23a3}')

I24a11 = Parameter(name = 'I24a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I24a11}')

I24a22 = Parameter(name = 'I24a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I24a22}')

I24a33 = Parameter(name = 'I24a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I24a33}')

I25a1 = Parameter(name = 'I25a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo + CKM2x1*ydo + CKM3x1*ydo',
                  texname = '\\text{I25a1}')

I25a2 = Parameter(name = 'I25a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys + CKM2x2*ys + CKM3x2*ys',
                  texname = '\\text{I25a2}')

I25a3 = Parameter(name = 'I25a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb + CKM2x3*yb + CKM3x3*yb',
                  texname = '\\text{I25a3}')

I26a1 = Parameter(name = 'I26a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1 + CKM2x1 + CKM3x1',
                  texname = '\\text{I26a1}')

I26a2 = Parameter(name = 'I26a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2 + CKM2x2 + CKM3x2',
                  texname = '\\text{I26a2}')

I26a3 = Parameter(name = 'I26a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3 + CKM2x3 + CKM3x3',
                  texname = '\\text{I26a3}')

I27a11 = Parameter(name = 'I27a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup',
                   texname = '\\text{I27a11}')

I27a22 = Parameter(name = 'I27a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc',
                   texname = '\\text{I27a22}')

I27a33 = Parameter(name = 'I27a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt',
                   texname = '\\text{I27a33}')

I28a1 = Parameter(name = 'I28a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1) + ydo*complexconjugate(CKM2x1) + ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I28a1}')

I28a2 = Parameter(name = 'I28a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2) + ys*complexconjugate(CKM2x2) + ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I28a2}')

I28a3 = Parameter(name = 'I28a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3) + yb*complexconjugate(CKM2x3) + yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I28a3}')

I29a11 = Parameter(name = 'I29a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM1x1)',
                   texname = '\\text{I29a11}')

I29a12 = Parameter(name = 'I29a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM2x1)',
                   texname = '\\text{I29a12}')

I29a13 = Parameter(name = 'I29a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM3x1)',
                   texname = '\\text{I29a13}')

I29a21 = Parameter(name = 'I29a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM1x2)',
                   texname = '\\text{I29a21}')

I29a22 = Parameter(name = 'I29a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I29a22}')

I29a23 = Parameter(name = 'I29a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM3x2)',
                   texname = '\\text{I29a23}')

I29a31 = Parameter(name = 'I29a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM1x3)',
                   texname = '\\text{I29a31}')

I29a32 = Parameter(name = 'I29a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM2x3)',
                   texname = '\\text{I29a32}')

I29a33 = Parameter(name = 'I29a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I29a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd1x1*ydo',
                  texname = '\\text{I3a11}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd2x2*ys',
                  texname = '\\text{I3a22}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd3x3*yb',
                  texname = '\\text{I3a33}')

I30a11 = Parameter(name = 'I30a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*yup',
                   texname = '\\text{I30a11}')

I30a12 = Parameter(name = 'I30a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Su2x2*yc',
                   texname = '\\text{I30a12}')

I30a13 = Parameter(name = 'I30a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Su3x3*yt',
                   texname = '\\text{I30a13}')

I30a21 = Parameter(name = 'I30a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*yup',
                   texname = '\\text{I30a21}')

I30a22 = Parameter(name = 'I30a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Su2x2*yc',
                   texname = '\\text{I30a22}')

I30a23 = Parameter(name = 'I30a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Su3x3*yt',
                   texname = '\\text{I30a23}')

I30a31 = Parameter(name = 'I30a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*yup',
                   texname = '\\text{I30a31}')

I30a32 = Parameter(name = 'I30a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Su2x2*yc',
                   texname = '\\text{I30a32}')

I30a33 = Parameter(name = 'I30a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Su3x3*yt',
                   texname = '\\text{I30a33}')

I31a1 = Parameter(name = 'I31a1',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I31a1}')

I31a2 = Parameter(name = 'I31a2',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I31a2}')

I31a3 = Parameter(name = 'I31a3',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I31a3}')

I32a11 = Parameter(name = 'I32a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*yup',
                   texname = '\\text{I32a11}')

I32a12 = Parameter(name = 'I32a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Su2x2*yc',
                   texname = '\\text{I32a12}')

I32a13 = Parameter(name = 'I32a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Su3x3*yt',
                   texname = '\\text{I32a13}')

I32a21 = Parameter(name = 'I32a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*yup',
                   texname = '\\text{I32a21}')

I32a22 = Parameter(name = 'I32a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Su2x2*yc',
                   texname = '\\text{I32a22}')

I32a23 = Parameter(name = 'I32a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Su3x3*yt',
                   texname = '\\text{I32a23}')

I32a31 = Parameter(name = 'I32a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*yup',
                   texname = '\\text{I32a31}')

I32a32 = Parameter(name = 'I32a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Su2x2*yc',
                   texname = '\\text{I32a32}')

I32a33 = Parameter(name = 'I32a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Su3x3*yt',
                   texname = '\\text{I32a33}')

I33a11 = Parameter(name = 'I33a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I33a11}')

I33a12 = Parameter(name = 'I33a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I33a12}')

I33a13 = Parameter(name = 'I33a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I33a13}')

I33a21 = Parameter(name = 'I33a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I33a21}')

I33a22 = Parameter(name = 'I33a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I33a22}')

I33a23 = Parameter(name = 'I33a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I33a23}')

I33a31 = Parameter(name = 'I33a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I33a31}')

I33a32 = Parameter(name = 'I33a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I33a32}')

I33a33 = Parameter(name = 'I33a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I33a33}')

I34a1 = Parameter(name = 'I34a1',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I34a1}')

I34a2 = Parameter(name = 'I34a2',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I34a2}')

I34a3 = Parameter(name = 'I34a3',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I34a3}')

I35a11 = Parameter(name = 'I35a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I35a11}')

I35a12 = Parameter(name = 'I35a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I35a12}')

I35a13 = Parameter(name = 'I35a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I35a13}')

I35a21 = Parameter(name = 'I35a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I35a21}')

I35a22 = Parameter(name = 'I35a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I35a22}')

I35a23 = Parameter(name = 'I35a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I35a23}')

I35a31 = Parameter(name = 'I35a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I35a31}')

I35a32 = Parameter(name = 'I35a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I35a32}')

I35a33 = Parameter(name = 'I35a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I35a33}')

I36a11 = Parameter(name = 'I36a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM1x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM1x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a11}')

I36a12 = Parameter(name = 'I36a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM1x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a12}')

I36a13 = Parameter(name = 'I36a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM1x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM1x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                   texname = '\\text{I36a13}')

I36a21 = Parameter(name = 'I36a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM2x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM2x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a21}')

I36a22 = Parameter(name = 'I36a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM2x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a22}')

I36a23 = Parameter(name = 'I36a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM2x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM2x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                   texname = '\\text{I36a23}')

I36a31 = Parameter(name = 'I36a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM3x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM3x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a31}')

I36a32 = Parameter(name = 'I36a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM3x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3)',
                   texname = '\\text{I36a32}')

I36a33 = Parameter(name = 'I36a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                   texname = '\\text{I36a33}')

I37a1 = Parameter(name = 'I37a1',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I37a1}')

I37a2 = Parameter(name = 'I37a2',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I37a2}')

I37a3 = Parameter(name = 'I37a3',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I37a3}')

I38a1 = Parameter(name = 'I38a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM1x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM1x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM1x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM1x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM1x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM1x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM1x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I38a1}')

I38a2 = Parameter(name = 'I38a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM2x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM2x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM2x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM2x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM2x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM2x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM2x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I38a2}')

I38a3 = Parameter(name = 'I38a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM3x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM3x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM3x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I38a3}')

I39a11 = Parameter(name = 'I39a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I39a11}')

I39a12 = Parameter(name = 'I39a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I39a12}')

I39a13 = Parameter(name = 'I39a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I39a13}')

I39a21 = Parameter(name = 'I39a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I39a21}')

I39a22 = Parameter(name = 'I39a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I39a22}')

I39a23 = Parameter(name = 'I39a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I39a23}')

I39a31 = Parameter(name = 'I39a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I39a31}')

I39a32 = Parameter(name = 'I39a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I39a32}')

I39a33 = Parameter(name = 'I39a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I39a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd1x1*ydo',
                  texname = '\\text{I4a11}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd2x2*ys',
                  texname = '\\text{I4a22}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Sd3x3*yb',
                  texname = '\\text{I4a33}')

I40a1 = Parameter(name = 'I40a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM1x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM1x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM1x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM1x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM1x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM1x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM1x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM1x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM1x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM1x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I40a1}')

I40a2 = Parameter(name = 'I40a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM2x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM2x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM2x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM2x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM2x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM2x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM2x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM2x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I40a2}')

I40a3 = Parameter(name = 'I40a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)**2 + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM1x3) + CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x1*Sd1x1*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x2) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM2x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)**2 + CKM3x3*Sd3x3*ys*complexconjugate(CKM1x2)*complexconjugate(CKM2x3) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x2)*complexconjugate(CKM2x3) + CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*ydo*complexconjugate(CKM1x2)*complexconjugate(CKM3x1) + CKM3x1*Sd1x1*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x3*Sd3x3*ydo*complexconjugate(CKM1x3)*complexconjugate(CKM3x1) + CKM3x1*Sd1x1*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x2) + CKM3x1*Sd1x1*ys*complexconjugate(CKM2x1)*complexconjugate(CKM3x2) + CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2)*complexconjugate(CKM3x2) + CKM3x2*Sd2x2*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*ys*complexconjugate(CKM2x3)*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3)*complexconjugate(CKM3x3) + CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3)*complexconjugate(CKM3x3) + CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1)*complexconjugate(CKM3x3) + CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2)*complexconjugate(CKM3x3) + CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3)**2',
                  texname = '\\text{I40a3}')

I41a11 = Parameter(name = 'I41a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I41a11}')

I41a12 = Parameter(name = 'I41a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I41a12}')

I41a13 = Parameter(name = 'I41a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I41a13}')

I41a21 = Parameter(name = 'I41a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I41a21}')

I41a22 = Parameter(name = 'I41a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I41a22}')

I41a23 = Parameter(name = 'I41a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I41a23}')

I41a31 = Parameter(name = 'I41a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I41a31}')

I41a32 = Parameter(name = 'I41a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I41a32}')

I41a33 = Parameter(name = 'I41a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I41a33}')

I42a11 = Parameter(name = 'I42a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I42a11}')

I42a12 = Parameter(name = 'I42a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I42a12}')

I42a13 = Parameter(name = 'I42a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I42a13}')

I42a21 = Parameter(name = 'I42a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I42a21}')

I42a22 = Parameter(name = 'I42a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I42a22}')

I42a23 = Parameter(name = 'I42a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I42a23}')

I42a31 = Parameter(name = 'I42a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I42a31}')

I42a32 = Parameter(name = 'I42a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I42a32}')

I42a33 = Parameter(name = 'I42a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I42a33}')

I43a11 = Parameter(name = 'I43a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I43a11}')

I43a12 = Parameter(name = 'I43a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I43a12}')

I43a13 = Parameter(name = 'I43a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I43a13}')

I43a21 = Parameter(name = 'I43a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I43a21}')

I43a22 = Parameter(name = 'I43a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I43a22}')

I43a23 = Parameter(name = 'I43a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I43a23}')

I43a31 = Parameter(name = 'I43a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I43a31}')

I43a32 = Parameter(name = 'I43a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I43a32}')

I43a33 = Parameter(name = 'I43a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I43a33}')

I44a11 = Parameter(name = 'I44a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM1x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM1x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM1x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM1x3)',
                   texname = '\\text{I44a11}')

I44a12 = Parameter(name = 'I44a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM1x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM1x1) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM1x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM1x3)',
                   texname = '\\text{I44a12}')

I44a13 = Parameter(name = 'I44a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM1x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM1x1) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM1x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM1x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM1x3)',
                   texname = '\\text{I44a13}')

I44a21 = Parameter(name = 'I44a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM2x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM2x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I44a21}')

I44a22 = Parameter(name = 'I44a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM2x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM2x1) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM2x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I44a22}')

I44a23 = Parameter(name = 'I44a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM2x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM2x1) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM2x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM2x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I44a23}')

I44a31 = Parameter(name = 'I44a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM3x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM3x3)',
                   texname = '\\text{I44a31}')

I44a32 = Parameter(name = 'I44a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM3x1) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM3x3)',
                   texname = '\\text{I44a32}')

I44a33 = Parameter(name = 'I44a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM3x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM3x1) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM3x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM3x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM3x3)',
                   texname = '\\text{I44a33}')

I45a1 = Parameter(name = 'I45a1',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I45a1}')

I45a2 = Parameter(name = 'I45a2',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I45a2}')

I45a3 = Parameter(name = 'I45a3',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{I45a3}')

I46a11 = Parameter(name = 'I46a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I46a11}')

I46a12 = Parameter(name = 'I46a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I46a12}')

I46a13 = Parameter(name = 'I46a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I46a13}')

I46a21 = Parameter(name = 'I46a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I46a21}')

I46a22 = Parameter(name = 'I46a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I46a22}')

I46a23 = Parameter(name = 'I46a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I46a23}')

I46a31 = Parameter(name = 'I46a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I46a31}')

I46a32 = Parameter(name = 'I46a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I46a32}')

I46a33 = Parameter(name = 'I46a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I46a33}')

I47a1 = Parameter(name = 'I47a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM1x1) + CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM1x1) + CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM1x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM1x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM1x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM1x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM1x2) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM1x2) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM1x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM1x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM1x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM1x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM1x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM1x3)',
                  texname = '\\text{I47a1}')

I47a2 = Parameter(name = 'I47a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM2x1) + CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM2x1) + CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM2x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM2x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM2x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM2x2) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM2x2) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM2x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM2x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM2x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM2x3)',
                  texname = '\\text{I47a2}')

I47a3 = Parameter(name = 'I47a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM2x3*CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM3x1*CKM3x3*Sd1x1*yb*complexconjugate(CKM3x1) + CKM1x1**2*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM1x1*CKM2x1*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM1x1*CKM3x1*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM1x2*CKM2x1*Sd1x1*ys*complexconjugate(CKM3x1) + CKM2x1*CKM2x2*Sd1x1*ys*complexconjugate(CKM3x1) + CKM2x1*CKM3x2*Sd1x1*ys*complexconjugate(CKM3x1) + CKM1x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM2x3*CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM3x2*CKM3x3*Sd2x2*yb*complexconjugate(CKM3x2) + CKM1x1*CKM1x2*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM1x2*CKM2x1*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM1x2*CKM3x1*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM1x2*CKM2x2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM2x2**2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM2x2*CKM3x2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM1x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3) + CKM2x3*CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3) + CKM3x3**2*Sd3x3*yb*complexconjugate(CKM3x3) + CKM1x1*CKM1x3*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM1x3*CKM2x1*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM1x3*CKM3x1*Sd3x3*ydo*complexconjugate(CKM3x3) + CKM1x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM3x3) + CKM2x2*CKM2x3*Sd3x3*ys*complexconjugate(CKM3x3) + CKM2x3*CKM3x2*Sd3x3*ys*complexconjugate(CKM3x3)',
                  texname = '\\text{I47a3}')

I48a11 = Parameter(name = 'I48a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I48a11}')

I48a12 = Parameter(name = 'I48a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM2x3)',
                   texname = '\\text{I48a12}')

I48a13 = Parameter(name = 'I48a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*ydo*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*ydo*complexconjugate(CKM3x3)',
                   texname = '\\text{I48a13}')

I48a21 = Parameter(name = 'I48a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ys*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM1x3)',
                   texname = '\\text{I48a21}')

I48a22 = Parameter(name = 'I48a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ys*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I48a22}')

I48a23 = Parameter(name = 'I48a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*ys*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*ys*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*ys*complexconjugate(CKM3x3)',
                   texname = '\\text{I48a23}')

I48a31 = Parameter(name = 'I48a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*yb*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM1x3)',
                   texname = '\\text{I48a31}')

I48a32 = Parameter(name = 'I48a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*yb*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM2x3)',
                   texname = '\\text{I48a32}')

I48a33 = Parameter(name = 'I48a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*yb*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*yb*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I48a33}')

I49a1 = Parameter(name = 'I49a1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x1) + complexconjugate(CKM2x1) + complexconjugate(CKM3x1)',
                  texname = '\\text{I49a1}')

I49a2 = Parameter(name = 'I49a2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x2) + complexconjugate(CKM2x2) + complexconjugate(CKM3x2)',
                  texname = '\\text{I49a2}')

I49a3 = Parameter(name = 'I49a3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM1x3) + complexconjugate(CKM2x3) + complexconjugate(CKM3x3)',
                  texname = '\\text{I49a3}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*complexconjugate(CKM1x3)',
                  texname = '\\text{I5a11}')

I5a12 = Parameter(name = 'I5a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*complexconjugate(CKM2x3)',
                  texname = '\\text{I5a12}')

I5a13 = Parameter(name = 'I5a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I5a13}')

I5a21 = Parameter(name = 'I5a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*complexconjugate(CKM1x3)',
                  texname = '\\text{I5a21}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*complexconjugate(CKM2x3)',
                  texname = '\\text{I5a22}')

I5a23 = Parameter(name = 'I5a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I5a23}')

I5a31 = Parameter(name = 'I5a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*complexconjugate(CKM1x3)',
                  texname = '\\text{I5a31}')

I5a32 = Parameter(name = 'I5a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*complexconjugate(CKM2x3)',
                  texname = '\\text{I5a32}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I5a33}')

I50a11 = Parameter(name = 'I50a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM1x1) + CKM1x2*Sd2x2*complexconjugate(CKM1x2) + CKM1x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I50a11}')

I50a12 = Parameter(name = 'I50a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM2x1) + CKM1x2*Sd2x2*complexconjugate(CKM2x2) + CKM1x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I50a12}')

I50a13 = Parameter(name = 'I50a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*complexconjugate(CKM3x1) + CKM1x2*Sd2x2*complexconjugate(CKM3x2) + CKM1x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I50a13}')

I50a21 = Parameter(name = 'I50a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM1x1) + CKM2x2*Sd2x2*complexconjugate(CKM1x2) + CKM2x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I50a21}')

I50a22 = Parameter(name = 'I50a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM2x1) + CKM2x2*Sd2x2*complexconjugate(CKM2x2) + CKM2x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I50a22}')

I50a23 = Parameter(name = 'I50a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1*complexconjugate(CKM3x1) + CKM2x2*Sd2x2*complexconjugate(CKM3x2) + CKM2x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I50a23}')

I50a31 = Parameter(name = 'I50a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM1x1) + CKM3x2*Sd2x2*complexconjugate(CKM1x2) + CKM3x3*Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I50a31}')

I50a32 = Parameter(name = 'I50a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM2x1) + CKM3x2*Sd2x2*complexconjugate(CKM2x2) + CKM3x3*Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I50a32}')

I50a33 = Parameter(name = 'I50a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1*complexconjugate(CKM3x1) + CKM3x2*Sd2x2*complexconjugate(CKM3x2) + CKM3x3*Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I50a33}')

I51a11 = Parameter(name = 'I51a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1',
                   texname = '\\text{I51a11}')

I51a12 = Parameter(name = 'I51a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1',
                   texname = '\\text{I51a12}')

I51a13 = Parameter(name = 'I51a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1',
                   texname = '\\text{I51a13}')

I51a21 = Parameter(name = 'I51a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Sd2x2',
                   texname = '\\text{I51a21}')

I51a22 = Parameter(name = 'I51a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Sd2x2',
                   texname = '\\text{I51a22}')

I51a23 = Parameter(name = 'I51a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Sd2x2',
                   texname = '\\text{I51a23}')

I51a31 = Parameter(name = 'I51a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Sd3x3',
                   texname = '\\text{I51a31}')

I51a32 = Parameter(name = 'I51a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Sd3x3',
                   texname = '\\text{I51a32}')

I51a33 = Parameter(name = 'I51a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Sd3x3',
                   texname = '\\text{I51a33}')

I52a11 = Parameter(name = 'I52a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I52a11}')

I52a12 = Parameter(name = 'I52a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM2x1)',
                   texname = '\\text{I52a12}')

I52a13 = Parameter(name = 'I52a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM3x1)',
                   texname = '\\text{I52a13}')

I52a21 = Parameter(name = 'I52a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM1x2)',
                   texname = '\\text{I52a21}')

I52a22 = Parameter(name = 'I52a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I52a22}')

I52a23 = Parameter(name = 'I52a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM3x2)',
                   texname = '\\text{I52a23}')

I52a31 = Parameter(name = 'I52a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I52a31}')

I52a32 = Parameter(name = 'I52a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I52a32}')

I52a33 = Parameter(name = 'I52a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I52a33}')

I53a11 = Parameter(name = 'I53a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I53a11}')

I53a12 = Parameter(name = 'I53a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x1)',
                   texname = '\\text{I53a12}')

I53a13 = Parameter(name = 'I53a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I53a13}')

I53a21 = Parameter(name = 'I53a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x2)',
                   texname = '\\text{I53a21}')

I53a22 = Parameter(name = 'I53a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I53a22}')

I53a23 = Parameter(name = 'I53a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I53a23}')

I53a31 = Parameter(name = 'I53a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x3)',
                   texname = '\\text{I53a31}')

I53a32 = Parameter(name = 'I53a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x3)',
                   texname = '\\text{I53a32}')

I53a33 = Parameter(name = 'I53a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I53a33}')

I54a11 = Parameter(name = 'I54a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1',
                   texname = '\\text{I54a11}')

I54a12 = Parameter(name = 'I54a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Su2x2',
                   texname = '\\text{I54a12}')

I54a13 = Parameter(name = 'I54a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Su3x3',
                   texname = '\\text{I54a13}')

I54a21 = Parameter(name = 'I54a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1',
                   texname = '\\text{I54a21}')

I54a22 = Parameter(name = 'I54a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Su2x2',
                   texname = '\\text{I54a22}')

I54a23 = Parameter(name = 'I54a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Su3x3',
                   texname = '\\text{I54a23}')

I54a31 = Parameter(name = 'I54a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1',
                   texname = '\\text{I54a31}')

I54a32 = Parameter(name = 'I54a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Su2x2',
                   texname = '\\text{I54a32}')

I54a33 = Parameter(name = 'I54a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Su3x3',
                   texname = '\\text{I54a33}')

I55a11 = Parameter(name = 'I55a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1*ydo',
                   texname = '\\text{I55a11}')

I55a12 = Parameter(name = 'I55a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Sd1x1*ydo',
                   texname = '\\text{I55a12}')

I55a13 = Parameter(name = 'I55a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Sd1x1*ydo',
                   texname = '\\text{I55a13}')

I55a21 = Parameter(name = 'I55a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd2x2*ys',
                   texname = '\\text{I55a21}')

I55a22 = Parameter(name = 'I55a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Sd2x2*ys',
                   texname = '\\text{I55a22}')

I55a23 = Parameter(name = 'I55a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Sd2x2*ys',
                   texname = '\\text{I55a23}')

I55a31 = Parameter(name = 'I55a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd3x3*yb',
                   texname = '\\text{I55a31}')

I55a32 = Parameter(name = 'I55a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Sd3x3*yb',
                   texname = '\\text{I55a32}')

I55a33 = Parameter(name = 'I55a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Sd3x3*yb',
                   texname = '\\text{I55a33}')

I56a11 = Parameter(name = 'I56a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*ydo',
                   texname = '\\text{I56a11}')

I56a12 = Parameter(name = 'I56a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*ydo',
                   texname = '\\text{I56a12}')

I56a13 = Parameter(name = 'I56a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*ydo',
                   texname = '\\text{I56a13}')

I56a21 = Parameter(name = 'I56a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*ys',
                   texname = '\\text{I56a21}')

I56a22 = Parameter(name = 'I56a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*ys',
                   texname = '\\text{I56a22}')

I56a23 = Parameter(name = 'I56a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*ys',
                   texname = '\\text{I56a23}')

I56a31 = Parameter(name = 'I56a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*yb',
                   texname = '\\text{I56a31}')

I56a32 = Parameter(name = 'I56a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*yb',
                   texname = '\\text{I56a32}')

I56a33 = Parameter(name = 'I56a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yb',
                   texname = '\\text{I56a33}')

I57a11 = Parameter(name = 'I57a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM1x1)',
                   texname = '\\text{I57a11}')

I57a12 = Parameter(name = 'I57a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM2x1)',
                   texname = '\\text{I57a12}')

I57a13 = Parameter(name = 'I57a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM3x1)',
                   texname = '\\text{I57a13}')

I57a21 = Parameter(name = 'I57a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM1x2)',
                   texname = '\\text{I57a21}')

I57a22 = Parameter(name = 'I57a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I57a22}')

I57a23 = Parameter(name = 'I57a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM3x2)',
                   texname = '\\text{I57a23}')

I57a31 = Parameter(name = 'I57a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I57a31}')

I57a32 = Parameter(name = 'I57a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I57a32}')

I57a33 = Parameter(name = 'I57a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I57a33}')

I58a11 = Parameter(name = 'I58a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM1x1)',
                   texname = '\\text{I58a11}')

I58a12 = Parameter(name = 'I58a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM2x1)',
                   texname = '\\text{I58a12}')

I58a13 = Parameter(name = 'I58a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM3x1)',
                   texname = '\\text{I58a13}')

I58a21 = Parameter(name = 'I58a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM1x2)',
                   texname = '\\text{I58a21}')

I58a22 = Parameter(name = 'I58a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I58a22}')

I58a23 = Parameter(name = 'I58a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM3x2)',
                   texname = '\\text{I58a23}')

I58a31 = Parameter(name = 'I58a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*complexconjugate(CKM1x3)',
                   texname = '\\text{I58a31}')

I58a32 = Parameter(name = 'I58a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*complexconjugate(CKM2x3)',
                   texname = '\\text{I58a32}')

I58a33 = Parameter(name = 'I58a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*complexconjugate(CKM3x3)',
                   texname = '\\text{I58a33}')

I59a11 = Parameter(name = 'I59a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Sd1x1',
                   texname = '\\text{I59a11}')

I59a12 = Parameter(name = 'I59a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Sd2x2',
                   texname = '\\text{I59a12}')

I59a13 = Parameter(name = 'I59a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Sd3x3',
                   texname = '\\text{I59a13}')

I59a21 = Parameter(name = 'I59a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Sd1x1',
                   texname = '\\text{I59a21}')

I59a22 = Parameter(name = 'I59a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Sd2x2',
                   texname = '\\text{I59a22}')

I59a23 = Parameter(name = 'I59a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Sd3x3',
                   texname = '\\text{I59a23}')

I59a31 = Parameter(name = 'I59a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Sd1x1',
                   texname = '\\text{I59a31}')

I59a32 = Parameter(name = 'I59a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Sd2x2',
                   texname = '\\text{I59a32}')

I59a33 = Parameter(name = 'I59a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Sd3x3',
                   texname = '\\text{I59a33}')

I6a11 = Parameter(name = 'I6a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Su1x1*complexconjugate(CKM1x1) + CKM2x1*Su2x2*complexconjugate(CKM2x1) + CKM3x1*Su3x3*complexconjugate(CKM3x1)',
                  texname = '\\text{I6a11}')

I6a12 = Parameter(name = 'I6a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*Su1x1*complexconjugate(CKM1x1) + CKM2x2*Su2x2*complexconjugate(CKM2x1) + CKM3x2*Su3x3*complexconjugate(CKM3x1)',
                  texname = '\\text{I6a12}')

I6a13 = Parameter(name = 'I6a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*Su1x1*complexconjugate(CKM1x1) + CKM2x3*Su2x2*complexconjugate(CKM2x1) + CKM3x3*Su3x3*complexconjugate(CKM3x1)',
                  texname = '\\text{I6a13}')

I6a21 = Parameter(name = 'I6a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Su1x1*complexconjugate(CKM1x2) + CKM2x1*Su2x2*complexconjugate(CKM2x2) + CKM3x1*Su3x3*complexconjugate(CKM3x2)',
                  texname = '\\text{I6a21}')

I6a22 = Parameter(name = 'I6a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*Su1x1*complexconjugate(CKM1x2) + CKM2x2*Su2x2*complexconjugate(CKM2x2) + CKM3x2*Su3x3*complexconjugate(CKM3x2)',
                  texname = '\\text{I6a22}')

I6a23 = Parameter(name = 'I6a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*Su1x1*complexconjugate(CKM1x2) + CKM2x3*Su2x2*complexconjugate(CKM2x2) + CKM3x3*Su3x3*complexconjugate(CKM3x2)',
                  texname = '\\text{I6a23}')

I6a31 = Parameter(name = 'I6a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Su1x1*complexconjugate(CKM1x3) + CKM2x1*Su2x2*complexconjugate(CKM2x3) + CKM3x1*Su3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I6a31}')

I6a32 = Parameter(name = 'I6a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*Su1x1*complexconjugate(CKM1x3) + CKM2x2*Su2x2*complexconjugate(CKM2x3) + CKM3x2*Su3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I6a32}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*Su1x1*complexconjugate(CKM1x3) + CKM2x3*Su2x2*complexconjugate(CKM2x3) + CKM3x3*Su3x3*complexconjugate(CKM3x3)',
                  texname = '\\text{I6a33}')

I60a11 = Parameter(name = 'I60a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1',
                   texname = '\\text{I60a11}')

I60a12 = Parameter(name = 'I60a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1',
                   texname = '\\text{I60a12}')

I60a13 = Parameter(name = 'I60a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1',
                   texname = '\\text{I60a13}')

I60a21 = Parameter(name = 'I60a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Su2x2',
                   texname = '\\text{I60a21}')

I60a22 = Parameter(name = 'I60a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Su2x2',
                   texname = '\\text{I60a22}')

I60a23 = Parameter(name = 'I60a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Su2x2',
                   texname = '\\text{I60a23}')

I60a31 = Parameter(name = 'I60a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Su3x3',
                   texname = '\\text{I60a31}')

I60a32 = Parameter(name = 'I60a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Su3x3',
                   texname = '\\text{I60a32}')

I60a33 = Parameter(name = 'I60a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Su3x3',
                   texname = '\\text{I60a33}')

I61a11 = Parameter(name = 'I61a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*ydo*yup',
                   texname = '\\text{I61a11}')

I61a12 = Parameter(name = 'I61a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*ys*yup',
                   texname = '\\text{I61a12}')

I61a13 = Parameter(name = 'I61a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yb*yup',
                   texname = '\\text{I61a13}')

I61a21 = Parameter(name = 'I61a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*yc*ydo',
                   texname = '\\text{I61a21}')

I61a22 = Parameter(name = 'I61a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*yc*ys',
                   texname = '\\text{I61a22}')

I61a23 = Parameter(name = 'I61a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*yb*yc',
                   texname = '\\text{I61a23}')

I61a31 = Parameter(name = 'I61a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*ydo*yt',
                   texname = '\\text{I61a31}')

I61a32 = Parameter(name = 'I61a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*ys*yt',
                   texname = '\\text{I61a32}')

I61a33 = Parameter(name = 'I61a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yb*yt',
                   texname = '\\text{I61a33}')

I62a11 = Parameter(name = 'I62a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*yup',
                   texname = '\\text{I62a11}')

I62a12 = Parameter(name = 'I62a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*yup',
                   texname = '\\text{I62a12}')

I62a13 = Parameter(name = 'I62a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*yup',
                   texname = '\\text{I62a13}')

I62a21 = Parameter(name = 'I62a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*Su2x2*yc',
                   texname = '\\text{I62a21}')

I62a22 = Parameter(name = 'I62a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Su2x2*yc',
                   texname = '\\text{I62a22}')

I62a23 = Parameter(name = 'I62a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*Su2x2*yc',
                   texname = '\\text{I62a23}')

I62a31 = Parameter(name = 'I62a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*Su3x3*yt',
                   texname = '\\text{I62a31}')

I62a32 = Parameter(name = 'I62a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*Su3x3*yt',
                   texname = '\\text{I62a32}')

I62a33 = Parameter(name = 'I62a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Su3x3*yt',
                   texname = '\\text{I62a33}')

I63a11 = Parameter(name = 'I63a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*yup',
                   texname = '\\text{I63a11}')

I63a12 = Parameter(name = 'I63a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*yup',
                   texname = '\\text{I63a12}')

I63a13 = Parameter(name = 'I63a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yup',
                   texname = '\\text{I63a13}')

I63a21 = Parameter(name = 'I63a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x1*yc',
                   texname = '\\text{I63a21}')

I63a22 = Parameter(name = 'I63a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*yc',
                   texname = '\\text{I63a22}')

I63a23 = Parameter(name = 'I63a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x3*yc',
                   texname = '\\text{I63a23}')

I63a31 = Parameter(name = 'I63a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x1*yt',
                   texname = '\\text{I63a31}')

I63a32 = Parameter(name = 'I63a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x2*yt',
                   texname = '\\text{I63a32}')

I63a33 = Parameter(name = 'I63a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yt',
                   texname = '\\text{I63a33}')

I64a11 = Parameter(name = 'I64a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I64a11}')

I64a12 = Parameter(name = 'I64a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM2x1)',
                   texname = '\\text{I64a12}')

I64a13 = Parameter(name = 'I64a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd1x1*complexconjugate(CKM3x1)',
                   texname = '\\text{I64a13}')

I64a21 = Parameter(name = 'I64a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM1x2)',
                   texname = '\\text{I64a21}')

I64a22 = Parameter(name = 'I64a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I64a22}')

I64a23 = Parameter(name = 'I64a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd2x2*complexconjugate(CKM3x2)',
                   texname = '\\text{I64a23}')

I64a31 = Parameter(name = 'I64a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I64a31}')

I64a32 = Parameter(name = 'I64a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I64a32}')

I64a33 = Parameter(name = 'I64a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Sd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I64a33}')

I65a11 = Parameter(name = 'I65a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I65a11}')

I65a12 = Parameter(name = 'I65a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x1)',
                   texname = '\\text{I65a12}')

I65a13 = Parameter(name = 'I65a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I65a13}')

I65a21 = Parameter(name = 'I65a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x2)',
                   texname = '\\text{I65a21}')

I65a22 = Parameter(name = 'I65a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I65a22}')

I65a23 = Parameter(name = 'I65a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I65a23}')

I65a31 = Parameter(name = 'I65a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*complexconjugate(CKM1x3)',
                   texname = '\\text{I65a31}')

I65a32 = Parameter(name = 'I65a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*complexconjugate(CKM2x3)',
                   texname = '\\text{I65a32}')

I65a33 = Parameter(name = 'I65a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I65a33}')

I66a11 = Parameter(name = 'I66a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I66a11}')

I66a12 = Parameter(name = 'I66a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*ydo*complexconjugate(CKM2x1)',
                   texname = '\\text{I66a12}')

I66a13 = Parameter(name = 'I66a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydo*yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I66a13}')

I66a21 = Parameter(name = 'I66a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I66a21}')

I66a22 = Parameter(name = 'I66a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*ys*complexconjugate(CKM2x2)',
                   texname = '\\text{I66a22}')

I66a23 = Parameter(name = 'I66a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ys*yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I66a23}')

I66a31 = Parameter(name = 'I66a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I66a31}')

I66a32 = Parameter(name = 'I66a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I66a32}')

I66a33 = Parameter(name = 'I66a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yb*yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I66a33}')

I67a11 = Parameter(name = 'I67a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I67a11}')

I67a12 = Parameter(name = 'I67a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I67a12}')

I67a13 = Parameter(name = 'I67a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I67a13}')

I67a21 = Parameter(name = 'I67a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I67a21}')

I67a22 = Parameter(name = 'I67a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I67a22}')

I67a23 = Parameter(name = 'I67a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I67a23}')

I67a31 = Parameter(name = 'I67a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su1x1*yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I67a31}')

I67a32 = Parameter(name = 'I67a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su2x2*yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I67a32}')

I67a33 = Parameter(name = 'I67a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Su3x3*yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I67a33}')

I68a11 = Parameter(name = 'I68a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x1)',
                   texname = '\\text{I68a11}')

I68a12 = Parameter(name = 'I68a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x1)',
                   texname = '\\text{I68a12}')

I68a13 = Parameter(name = 'I68a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x1)',
                   texname = '\\text{I68a13}')

I68a21 = Parameter(name = 'I68a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x2)',
                   texname = '\\text{I68a21}')

I68a22 = Parameter(name = 'I68a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x2)',
                   texname = '\\text{I68a22}')

I68a23 = Parameter(name = 'I68a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x2)',
                   texname = '\\text{I68a23}')

I68a31 = Parameter(name = 'I68a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yup*complexconjugate(CKM1x3)',
                   texname = '\\text{I68a31}')

I68a32 = Parameter(name = 'I68a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yc*complexconjugate(CKM2x3)',
                   texname = '\\text{I68a32}')

I68a33 = Parameter(name = 'I68a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yt*complexconjugate(CKM3x3)',
                   texname = '\\text{I68a33}')

I69a11 = Parameter(name = 'I69a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x1) + CKM2x1*Su2x2*complexconjugate(CKM2x1) + CKM3x1*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I69a11}')

I69a12 = Parameter(name = 'I69a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x1) + CKM2x2*Su2x2*complexconjugate(CKM2x1) + CKM3x2*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I69a12}')

I69a13 = Parameter(name = 'I69a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x1) + CKM2x3*Su2x2*complexconjugate(CKM2x1) + CKM3x3*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I69a13}')

I69a21 = Parameter(name = 'I69a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x2) + CKM2x1*Su2x2*complexconjugate(CKM2x2) + CKM3x1*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I69a21}')

I69a22 = Parameter(name = 'I69a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x2) + CKM2x2*Su2x2*complexconjugate(CKM2x2) + CKM3x2*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I69a22}')

I69a23 = Parameter(name = 'I69a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x2) + CKM2x3*Su2x2*complexconjugate(CKM2x2) + CKM3x3*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I69a23}')

I69a31 = Parameter(name = 'I69a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x3) + CKM2x1*Su2x2*complexconjugate(CKM2x3) + CKM3x1*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I69a31}')

I69a32 = Parameter(name = 'I69a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x3) + CKM2x2*Su2x2*complexconjugate(CKM2x3) + CKM3x2*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I69a32}')

I69a33 = Parameter(name = 'I69a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x3) + CKM2x3*Su2x2*complexconjugate(CKM2x3) + CKM3x3*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I69a33}')

I7a11 = Parameter(name = 'I7a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Sd1x1*ydo',
                  texname = '\\text{I7a11}')

I7a12 = Parameter(name = 'I7a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Sd1x1*ydo',
                  texname = '\\text{I7a12}')

I7a13 = Parameter(name = 'I7a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Sd1x1*ydo',
                  texname = '\\text{I7a13}')

I7a21 = Parameter(name = 'I7a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*Sd2x2*ys',
                  texname = '\\text{I7a21}')

I7a22 = Parameter(name = 'I7a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*Sd2x2*ys',
                  texname = '\\text{I7a22}')

I7a23 = Parameter(name = 'I7a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*Sd2x2*ys',
                  texname = '\\text{I7a23}')

I7a31 = Parameter(name = 'I7a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*Sd3x3*yb',
                  texname = '\\text{I7a31}')

I7a32 = Parameter(name = 'I7a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*Sd3x3*yb',
                  texname = '\\text{I7a32}')

I7a33 = Parameter(name = 'I7a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Sd3x3*yb',
                  texname = '\\text{I7a33}')

I70a11 = Parameter(name = 'I70a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x1) + CKM2x1*Su2x2*complexconjugate(CKM2x1) + CKM3x1*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I70a11}')

I70a12 = Parameter(name = 'I70a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x2) + CKM2x1*Su2x2*complexconjugate(CKM2x2) + CKM3x1*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I70a12}')

I70a13 = Parameter(name = 'I70a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x3) + CKM2x1*Su2x2*complexconjugate(CKM2x3) + CKM3x1*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I70a13}')

I70a21 = Parameter(name = 'I70a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x1) + CKM2x2*Su2x2*complexconjugate(CKM2x1) + CKM3x2*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I70a21}')

I70a22 = Parameter(name = 'I70a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x2) + CKM2x2*Su2x2*complexconjugate(CKM2x2) + CKM3x2*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I70a22}')

I70a23 = Parameter(name = 'I70a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x3) + CKM2x2*Su2x2*complexconjugate(CKM2x3) + CKM3x2*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I70a23}')

I70a31 = Parameter(name = 'I70a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x1) + CKM2x3*Su2x2*complexconjugate(CKM2x1) + CKM3x3*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I70a31}')

I70a32 = Parameter(name = 'I70a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x2) + CKM2x3*Su2x2*complexconjugate(CKM2x2) + CKM3x3*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I70a32}')

I70a33 = Parameter(name = 'I70a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x3) + CKM2x3*Su2x2*complexconjugate(CKM2x3) + CKM3x3*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I70a33}')

I71a11 = Parameter(name = 'I71a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x1) + CKM2x1*Su2x2*complexconjugate(CKM2x1) + CKM3x1*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I71a11}')

I71a12 = Parameter(name = 'I71a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x1) + CKM2x2*Su2x2*complexconjugate(CKM2x1) + CKM3x2*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I71a12}')

I71a13 = Parameter(name = 'I71a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x1) + CKM2x3*Su2x2*complexconjugate(CKM2x1) + CKM3x3*Su3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I71a13}')

I71a21 = Parameter(name = 'I71a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x2) + CKM2x1*Su2x2*complexconjugate(CKM2x2) + CKM3x1*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I71a21}')

I71a22 = Parameter(name = 'I71a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x2) + CKM2x2*Su2x2*complexconjugate(CKM2x2) + CKM3x2*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I71a22}')

I71a23 = Parameter(name = 'I71a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x2) + CKM2x3*Su2x2*complexconjugate(CKM2x2) + CKM3x3*Su3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I71a23}')

I71a31 = Parameter(name = 'I71a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Su1x1*complexconjugate(CKM1x3) + CKM2x1*Su2x2*complexconjugate(CKM2x3) + CKM3x1*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I71a31}')

I71a32 = Parameter(name = 'I71a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*Su1x1*complexconjugate(CKM1x3) + CKM2x2*Su2x2*complexconjugate(CKM2x3) + CKM3x2*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I71a32}')

I71a33 = Parameter(name = 'I71a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*Su1x1*complexconjugate(CKM1x3) + CKM2x3*Su2x2*complexconjugate(CKM2x3) + CKM3x3*Su3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I71a33}')

I8a11 = Parameter(name = 'I8a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I8a11}')

I8a12 = Parameter(name = 'I8a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I8a12}')

I8a13 = Parameter(name = 'I8a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I8a13}')

I8a21 = Parameter(name = 'I8a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I8a21}')

I8a22 = Parameter(name = 'I8a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I8a22}')

I8a23 = Parameter(name = 'I8a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I8a23}')

I8a31 = Parameter(name = 'I8a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I8a31}')

I8a32 = Parameter(name = 'I8a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I8a32}')

I8a33 = Parameter(name = 'I8a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I8a33}')

I9a11 = Parameter(name = 'I9a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Su1x1*yup',
                  texname = '\\text{I9a11}')

I9a12 = Parameter(name = 'I9a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*Su2x2*yc',
                  texname = '\\text{I9a12}')

I9a13 = Parameter(name = 'I9a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*Su3x3*yt',
                  texname = '\\text{I9a13}')

I9a21 = Parameter(name = 'I9a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*Su1x1*yup',
                  texname = '\\text{I9a21}')

I9a22 = Parameter(name = 'I9a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*Su2x2*yc',
                  texname = '\\text{I9a22}')

I9a23 = Parameter(name = 'I9a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*Su3x3*yt',
                  texname = '\\text{I9a23}')

I9a31 = Parameter(name = 'I9a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*Su1x1*yup',
                  texname = '\\text{I9a31}')

I9a32 = Parameter(name = 'I9a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*Su2x2*yc',
                  texname = '\\text{I9a32}')

I9a33 = Parameter(name = 'I9a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Su3x3*yt',
                  texname = '\\text{I9a33}')

