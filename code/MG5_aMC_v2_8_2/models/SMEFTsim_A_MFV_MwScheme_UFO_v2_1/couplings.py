# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Sat 10 Mar 2018 00:31:47


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(2*cll*complex(0,1))/LambdaSMEFT**2 + (2*cll1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_12 = Coupling(name = 'GC_12',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_13 = Coupling(name = 'GC_13',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_14 = Coupling(name = 'GC_14',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_15 = Coupling(name = 'GC_15',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_16 = Coupling(name = 'GC_16',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_17 = Coupling(name = 'GC_17',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_19 = Coupling(name = 'GC_19',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a11*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a11)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_20 = Coupling(name = 'GC_20',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_21 = Coupling(name = 'GC_21',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_22 = Coupling(name = 'GC_22',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_23 = Coupling(name = 'GC_23',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_25 = Coupling(name = 'GC_25',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_27 = Coupling(name = 'GC_27',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_28 = Coupling(name = 'GC_28',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a12*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a12)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_31 = Coupling(name = 'GC_31',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_32 = Coupling(name = 'GC_32',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_33 = Coupling(name = 'GC_33',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_37 = Coupling(name = 'GC_37',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a13*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a13)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_39 = Coupling(name = 'GC_39',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_43 = Coupling(name = 'GC_43',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a21*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a21)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_49 = Coupling(name = 'GC_49',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_53 = Coupling(name = 'GC_53',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a22*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a22)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a23*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a23)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a31*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a31)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a32*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a32)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((cquqd10*complex(0,1)*I10a11*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a11)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a11*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((cquqd10*complex(0,1)*I10a12*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a12)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a12*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((cquqd10*complex(0,1)*I10a13*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a13)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a13*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((cquqd10*complex(0,1)*I10a21*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a21)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a21*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((cquqd10*complex(0,1)*I10a22*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a22)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a22*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((cquqd10*complex(0,1)*I10a23*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a23)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a23*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cquqd10*complex(0,1)*I10a31*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a31)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a31*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((cquqd10*complex(0,1)*I10a32*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a32)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a32*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cquqd10*complex(0,1)*I10a33*I29a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I29a33*I30a33)/LambdaSMEFT**2 - (Delta2cquqd1*complex(0,1)*I10a33*I36a33)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((cquqd80*complex(0,1)*I10a11*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((cquqd80*complex(0,1)*I10a12*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_94 = Coupling(name = 'GC_94',
                 value = '-((cquqd80*complex(0,1)*I10a13*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((cquqd80*complex(0,1)*I10a21*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((cquqd80*complex(0,1)*I10a22*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((cquqd80*complex(0,1)*I10a23*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cquqd80*complex(0,1)*I10a31*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((cquqd80*complex(0,1)*I10a32*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a1*I38a1)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':4})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a1*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a1*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a1*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a1*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a2*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a2*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a1*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a1*I31a3*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a3*I38a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a2*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a1*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a1*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_136 = Coupling(name = 'GC_136',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a2*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a2*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a2*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a2*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a2*I31a3*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a3*I38a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a3*I31a1)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a1*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a1*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a3*I31a2)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a2*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a2*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((cquqd80*complex(0,1)*I10a11*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a11*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((cquqd80*complex(0,1)*I10a12*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a12*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((cquqd80*complex(0,1)*I10a13*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a13*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((cquqd80*complex(0,1)*I10a21*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a21*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((cquqd80*complex(0,1)*I10a22*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a22*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cquqd80*complex(0,1)*I10a23*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a23*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((cquqd80*complex(0,1)*I10a31*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a31*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((cquqd80*complex(0,1)*I10a32*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a32*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((cquqd80*complex(0,1)*I10a33*I28a3*I31a3)/LambdaSMEFT**2) - (Delta1cquqd8*complex(0,1)*I28a3*I31a3*I32a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I10a33*I37a3*I38a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a11*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a11*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a11*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a12*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a12*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a12*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a13*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a13*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a13*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a21*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a21*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a21*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a22*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a22*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a22*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a23*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a23*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a23*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a31*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a31*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a31*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a32*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a32*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a32*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a1*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a1*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a33*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a2*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a2*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a33*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a1*I34a3*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a1*I34a3*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a33*I47a1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a11*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a11*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a11*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a12*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a12*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a12*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a13*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a13*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a13*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_209 = Coupling(name = 'GC_209',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a21*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a21*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a21*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a22*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_213 = Coupling(name = 'GC_213',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a22*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a22*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_215 = Coupling(name = 'GC_215',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a23*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a23*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_217 = Coupling(name = 'GC_217',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a23*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_218 = Coupling(name = 'GC_218',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a31*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_219 = Coupling(name = 'GC_219',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a31*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_220 = Coupling(name = 'GC_220',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a31*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a32*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a32*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a32*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a1*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a1*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a33*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a2*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a2*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a33*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a2*I34a3*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a2*I34a3*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a33*I47a2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a11*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a11*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a11)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a11)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a11*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a12*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a12*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a12)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a12)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a12*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a13*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_234 = Coupling(name = 'GC_234',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a13*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_235 = Coupling(name = 'GC_235',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a13)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a13)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a13*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_236 = Coupling(name = 'GC_236',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a21*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a21*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_238 = Coupling(name = 'GC_238',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a21)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a21)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a21*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_239 = Coupling(name = 'GC_239',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a22*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a22*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a22)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a22)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a22*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a23*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a23*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_244 = Coupling(name = 'GC_244',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a23)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a23)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a23*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a31*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a31*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a31)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a31)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a31*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a32*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a32*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_250 = Coupling(name = 'GC_250',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a32)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a32)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a32*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_251 = Coupling(name = 'GC_251',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a1*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a1*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a1*I46a33*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_252 = Coupling(name = 'GC_252',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a2*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a2*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a2*I46a33*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((Delta1cquqd8*complex(0,1)*I25a3*I34a3*I35a33)/LambdaSMEFT**2) - (cquqd80*complex(0,1)*I25a3*I34a3*I42a33)/LambdaSMEFT**2 - (Delta2cquqd8*complex(0,1)*I45a3*I46a33*I47a3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_254 = Coupling(name = 'GC_254',
                  value = '(Delta1dcqu1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(Delta1dcqu1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(Delta1dcqu8*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(Delta1dcqu8*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(Deltadclq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(Delta1dcqu1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(Delta1dcqu1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(Delta1dcqu8*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(Delta1dcqu8*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '(Deltadclq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '(Delta1dcqu1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '(Delta1dcqu1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(Delta1dcqu8*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(Delta1dcqu8*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '(Deltadclq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(Delta1dcqu1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(Delta1dcqu1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(Delta1dcqu8*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '(Delta1dcqu8*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(Deltadclq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '(Delta1dcqu1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(Delta1dcqu1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '(Delta1dcqu8*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '(Delta1dcqu8*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '(Deltadclq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '(Delta1dcqu1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(Delta1dcqu1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(Delta1dcqu8*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(Delta1dcqu8*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(Deltadclq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '-((DeltacdG*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_285 = Coupling(name = 'GC_285',
                  value = '(DeltacdG*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((DeltacdG*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_287 = Coupling(name = 'GC_287',
                  value = '(DeltacdG*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((DeltacdG*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_289 = Coupling(name = 'GC_289',
                  value = '(DeltacdG*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_290 = Coupling(name = 'GC_290',
                  value = '-((DeltacdG*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_291 = Coupling(name = 'GC_291',
                  value = '(DeltacdG*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_292 = Coupling(name = 'GC_292',
                  value = '-((DeltacdG*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_293 = Coupling(name = 'GC_293',
                  value = '(DeltacdG*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_294 = Coupling(name = 'GC_294',
                  value = '-((DeltacdG*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_295 = Coupling(name = 'GC_295',
                  value = '(DeltacdG*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((DeltacdG*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_297 = Coupling(name = 'GC_297',
                  value = '(DeltacdG*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_298 = Coupling(name = 'GC_298',
                  value = '-((DeltacdG*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_299 = Coupling(name = 'GC_299',
                  value = '(DeltacdG*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_300 = Coupling(name = 'GC_300',
                  value = '-((DeltacdG*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_301 = Coupling(name = 'GC_301',
                  value = '(DeltacdG*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_302 = Coupling(name = 'GC_302',
                  value = '-((DeltacdG*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_303 = Coupling(name = 'GC_303',
                  value = '(DeltacdG*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_304 = Coupling(name = 'GC_304',
                  value = '-((DeltacdG*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_305 = Coupling(name = 'GC_305',
                  value = '(DeltacdG*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_306 = Coupling(name = 'GC_306',
                  value = '-((DeltacdG*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_307 = Coupling(name = 'GC_307',
                  value = '(DeltacdG*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_308 = Coupling(name = 'GC_308',
                  value = '-((DeltacdG*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_309 = Coupling(name = 'GC_309',
                  value = '(DeltacdG*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_310 = Coupling(name = 'GC_310',
                  value = '-((DeltacdG*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_311 = Coupling(name = 'GC_311',
                  value = '(DeltacdG*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_312 = Coupling(name = 'GC_312',
                  value = '-((DeltacdG*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_313 = Coupling(name = 'GC_313',
                  value = '(DeltacdG*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_314 = Coupling(name = 'GC_314',
                  value = '-((DeltacdG*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_315 = Coupling(name = 'GC_315',
                  value = '(DeltacdG*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_316 = Coupling(name = 'GC_316',
                  value = '-((DeltacdG*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_317 = Coupling(name = 'GC_317',
                  value = '(DeltacdG*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_318 = Coupling(name = 'GC_318',
                  value = '-((DeltacdG*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_319 = Coupling(name = 'GC_319',
                  value = '(DeltacdG*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_320 = Coupling(name = 'GC_320',
                  value = '(Delta1dcqu1*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_321 = Coupling(name = 'GC_321',
                  value = '(Delta1dcqu1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_322 = Coupling(name = 'GC_322',
                  value = '(Delta1dcqu1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = '(Delta1dcqu8*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = '(Delta1dcqu8*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = '(Delta1dcqu8*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = '(Delta1dcqq1*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '(Delta1dcqq11*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '(Delta1dcqq1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '(Delta1dcqq11*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(Delta1dcqq11*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '(Delta1dcqq1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '(Deltadclq1*complex(0,1)*I5a12)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(Deltadclq1*complex(0,1)*I5a12)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '(Delta1dcqu1*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(Delta1dcqu1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(Delta1dcqu1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(Delta1dcqu8*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(Delta1dcqu8*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(Delta1dcqu8*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(Delta1dcqq1*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(Delta1dcqq11*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '(Delta1dcqq1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(Delta1dcqq11*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(Delta1dcqq11*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(Delta1dcqq1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(Deltadclq1*complex(0,1)*I5a13)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(Deltadclq1*complex(0,1)*I5a13)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(Delta1dcqu1*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(Delta1dcqu1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '(Delta1dcqu1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '(Delta1dcqu8*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '(Delta1dcqu8*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '(Delta1dcqu8*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '(Delta1dcqq1*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(Delta1dcqq11*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(Delta1dcqq1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(Delta1dcqq11*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a12)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '(Delta1dcqq11*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_359 = Coupling(name = 'GC_359',
                  value = '(Delta1dcqq1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a12)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_360 = Coupling(name = 'GC_360',
                  value = '(Deltadclq1*complex(0,1)*I5a21)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = '(Deltadclq1*complex(0,1)*I5a21)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_362 = Coupling(name = 'GC_362',
                  value = '(Delta1dcqu1*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_363 = Coupling(name = 'GC_363',
                  value = '(Delta1dcqu1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(Delta1dcqu1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(Delta1dcqu8*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '(Delta1dcqu8*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(Delta1dcqu8*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(Delta1dcqq1*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(Delta1dcqq11*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(Delta1dcqq1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(Delta1dcqq11*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(Delta1dcqq11*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(Delta1dcqq1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(Deltadclq1*complex(0,1)*I5a23)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(Deltadclq1*complex(0,1)*I5a23)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(Delta1dcqu1*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '(Delta1dcqu1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(Delta1dcqu1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(Delta1dcqu8*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(Delta1dcqu8*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '(Delta1dcqu8*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(Delta1dcqq1*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(Delta1dcqq11*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(Delta1dcqq1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(Delta1dcqq11*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a13)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '(Delta1dcqq11*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(Delta1dcqq1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a13)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '(Deltadclq1*complex(0,1)*I5a31)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(Deltadclq1*complex(0,1)*I5a31)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '(Delta1dcqu1*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '(Delta1dcqu1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '(Delta1dcqu1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '(Delta1dcqu8*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(Delta1dcqu8*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(Delta1dcqu8*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '(Delta1dcqq1*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '(Delta1dcqq11*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_398 = Coupling(name = 'GC_398',
                  value = '(Delta1dcqq1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '(Delta1dcqq11*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a23)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '(Delta1dcqq11*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '(Delta1dcqq1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a23)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '(Deltadclq1*complex(0,1)*I5a32)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(Deltadclq1*complex(0,1)*I5a32)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '(DeltacuW*complex(0,1)*I62a11)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_405 = Coupling(name = 'GC_405',
                  value = '(DeltacuW*complex(0,1)*I62a12)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_406 = Coupling(name = 'GC_406',
                  value = '(DeltacuW*complex(0,1)*I62a13)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_407 = Coupling(name = 'GC_407',
                  value = '(DeltacuW*complex(0,1)*I62a21)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_408 = Coupling(name = 'GC_408',
                  value = '(DeltacuW*complex(0,1)*I62a22)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_409 = Coupling(name = 'GC_409',
                  value = '(DeltacuW*complex(0,1)*I62a23)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_410 = Coupling(name = 'GC_410',
                  value = '(DeltacuW*complex(0,1)*I62a31)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_411 = Coupling(name = 'GC_411',
                  value = '(DeltacuW*complex(0,1)*I62a32)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_412 = Coupling(name = 'GC_412',
                  value = '(DeltacuW*complex(0,1)*I62a33)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_413 = Coupling(name = 'GC_413',
                  value = '(DeltacuW*complex(0,1)*I67a11)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_414 = Coupling(name = 'GC_414',
                  value = '(DeltacuW*complex(0,1)*I67a12)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_415 = Coupling(name = 'GC_415',
                  value = '(DeltacuW*complex(0,1)*I67a13)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_416 = Coupling(name = 'GC_416',
                  value = '(DeltacuW*complex(0,1)*I67a21)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_417 = Coupling(name = 'GC_417',
                  value = '(DeltacuW*complex(0,1)*I67a22)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_418 = Coupling(name = 'GC_418',
                  value = '(DeltacuW*complex(0,1)*I67a23)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_419 = Coupling(name = 'GC_419',
                  value = '(DeltacuW*complex(0,1)*I67a31)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_420 = Coupling(name = 'GC_420',
                  value = '(DeltacuW*complex(0,1)*I67a32)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_421 = Coupling(name = 'GC_421',
                  value = '(DeltacuW*complex(0,1)*I67a33)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_422 = Coupling(name = 'GC_422',
                  value = '(Delta1ucqd1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(Delta1ucqd1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '(Delta1ucqd8*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(Delta1ucqd8*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(Delta1ucqd1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(Delta1ucqd1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '(Delta1ucqd8*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '(Delta1ucqd8*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(Delta1ucqd1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(Delta1ucqd1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '(Delta1ucqd8*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '(Delta1ucqd8*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '(Delta1ucqd1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '(Delta1ucqd1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '(Delta1ucqd8*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '(Delta1ucqd8*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '(Delta1ucqd1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '(Delta1ucqd1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '(Delta1ucqd8*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(Delta1ucqd8*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(Delta1ucqd1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '(Delta1ucqd1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '(Delta1ucqd8*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '(Delta1ucqd8*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '(Delta1ucqd1*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '(Delta1ucqd1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '(Delta1ucqd1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '(Delta1ucqd8*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(Delta1ucqd8*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(Delta1ucqd8*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(Delta1ucqq1*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(Delta1ucqq11*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(Delta1ucqq1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(Delta1ucqq11*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a12)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(Delta1ucqq11*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(Delta1ucqq1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a12)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(Delta1ucqd1*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '(Delta1ucqd1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(Delta1ucqd1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '(Delta1ucqd8*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '(Delta1ucqd8*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(Delta1ucqd8*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '(Delta1ucqq1*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '(Delta1ucqq11*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(Delta1ucqq1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '(Delta1ucqq11*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a13)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '(Delta1ucqq11*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '(Delta1ucqq1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a13)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '(Delta1ucqd1*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '(Delta1ucqd1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '(Delta1ucqd1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '(Delta1ucqd8*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(Delta1ucqd8*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '(Delta1ucqd8*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '(Delta1ucqq1*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '(Delta1ucqq11*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '(Delta1ucqq1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '(Delta1ucqq11*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a12)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a21)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '(Delta1ucqq11*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '(Delta1ucqq1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a12)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a21)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '(Delta1ucqd1*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '(Delta1ucqd1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '(Delta1ucqd1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '(Delta1ucqd8*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_486 = Coupling(name = 'GC_486',
                  value = '(Delta1ucqd8*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(Delta1ucqd8*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_488 = Coupling(name = 'GC_488',
                  value = '(Delta1ucqq1*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_489 = Coupling(name = 'GC_489',
                  value = '(Delta1ucqq11*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_490 = Coupling(name = 'GC_490',
                  value = '(Delta1ucqq1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_491 = Coupling(name = 'GC_491',
                  value = '(Delta1ucqq11*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a23)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_492 = Coupling(name = 'GC_492',
                  value = '(Delta1ucqq11*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_493 = Coupling(name = 'GC_493',
                  value = '(Delta1ucqq1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a23)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_494 = Coupling(name = 'GC_494',
                  value = '(Delta1ucqd1*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_495 = Coupling(name = 'GC_495',
                  value = '(Delta1ucqd1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_496 = Coupling(name = 'GC_496',
                  value = '(Delta1ucqd1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_497 = Coupling(name = 'GC_497',
                  value = '(Delta1ucqd8*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_498 = Coupling(name = 'GC_498',
                  value = '(Delta1ucqd8*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '(Delta1ucqd8*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '(Delta1ucqq1*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '(Delta1ucqq11*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(Delta1ucqq1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '(Delta1ucqq11*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a13)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a31)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '(Delta1ucqq11*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_505 = Coupling(name = 'GC_505',
                  value = '(Delta1ucqq1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a13)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a31)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_506 = Coupling(name = 'GC_506',
                  value = '(Delta1ucqd1*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_507 = Coupling(name = 'GC_507',
                  value = '(Delta1ucqd1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_508 = Coupling(name = 'GC_508',
                  value = '(Delta1ucqd1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_509 = Coupling(name = 'GC_509',
                  value = '(Delta1ucqd8*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_510 = Coupling(name = 'GC_510',
                  value = '(Delta1ucqd8*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_511 = Coupling(name = 'GC_511',
                  value = '(Delta1ucqd8*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_512 = Coupling(name = 'GC_512',
                  value = '(Delta1ucqq1*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_513 = Coupling(name = 'GC_513',
                  value = '(Delta1ucqq11*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '(Delta1ucqq1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_515 = Coupling(name = 'GC_515',
                  value = '(Delta1ucqq11*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a23)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a32)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '(Delta1ucqq11*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_517 = Coupling(name = 'GC_517',
                  value = '(Delta1ucqq1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a23)/(2.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a32)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_520 = Coupling(name = 'GC_520',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_521 = Coupling(name = 'GC_521',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_522 = Coupling(name = 'GC_522',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_524 = Coupling(name = 'GC_524',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_526 = Coupling(name = 'GC_526',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a11)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a11)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a11)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_527 = Coupling(name = 'GC_527',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_528 = Coupling(name = 'GC_528',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_529 = Coupling(name = 'GC_529',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_530 = Coupling(name = 'GC_530',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_531 = Coupling(name = 'GC_531',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_532 = Coupling(name = 'GC_532',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_533 = Coupling(name = 'GC_533',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_534 = Coupling(name = 'GC_534',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_535 = Coupling(name = 'GC_535',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a12)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a12)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_536 = Coupling(name = 'GC_536',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_537 = Coupling(name = 'GC_537',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_538 = Coupling(name = 'GC_538',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_539 = Coupling(name = 'GC_539',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_540 = Coupling(name = 'GC_540',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_541 = Coupling(name = 'GC_541',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_542 = Coupling(name = 'GC_542',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_543 = Coupling(name = 'GC_543',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_544 = Coupling(name = 'GC_544',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a13)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a13)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_546 = Coupling(name = 'GC_546',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_547 = Coupling(name = 'GC_547',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_548 = Coupling(name = 'GC_548',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_549 = Coupling(name = 'GC_549',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_550 = Coupling(name = 'GC_550',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_552 = Coupling(name = 'GC_552',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_553 = Coupling(name = 'GC_553',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a21)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a21)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_554 = Coupling(name = 'GC_554',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_555 = Coupling(name = 'GC_555',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_556 = Coupling(name = 'GC_556',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_557 = Coupling(name = 'GC_557',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_558 = Coupling(name = 'GC_558',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_560 = Coupling(name = 'GC_560',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_562 = Coupling(name = 'GC_562',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a22)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a22)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a22)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_563 = Coupling(name = 'GC_563',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_564 = Coupling(name = 'GC_564',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_565 = Coupling(name = 'GC_565',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_566 = Coupling(name = 'GC_566',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_567 = Coupling(name = 'GC_567',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_568 = Coupling(name = 'GC_568',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_569 = Coupling(name = 'GC_569',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_570 = Coupling(name = 'GC_570',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_571 = Coupling(name = 'GC_571',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a23)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a23)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_572 = Coupling(name = 'GC_572',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_573 = Coupling(name = 'GC_573',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_574 = Coupling(name = 'GC_574',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_575 = Coupling(name = 'GC_575',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_576 = Coupling(name = 'GC_576',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_577 = Coupling(name = 'GC_577',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_578 = Coupling(name = 'GC_578',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_579 = Coupling(name = 'GC_579',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_580 = Coupling(name = 'GC_580',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a31)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a31)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_581 = Coupling(name = 'GC_581',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_582 = Coupling(name = 'GC_582',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_583 = Coupling(name = 'GC_583',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_584 = Coupling(name = 'GC_584',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_585 = Coupling(name = 'GC_585',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_586 = Coupling(name = 'GC_586',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_587 = Coupling(name = 'GC_587',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_588 = Coupling(name = 'GC_588',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_589 = Coupling(name = 'GC_589',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a32)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a32)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_590 = Coupling(name = 'GC_590',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a11*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a11*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a11*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_591 = Coupling(name = 'GC_591',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a12*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a12*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a12*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_592 = Coupling(name = 'GC_592',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a13*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a13*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a13*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_593 = Coupling(name = 'GC_593',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a21*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a21*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a21*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_594 = Coupling(name = 'GC_594',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a22*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a22*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a22*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_595 = Coupling(name = 'GC_595',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a23*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a23*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a23*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_596 = Coupling(name = 'GC_596',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a31*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a31*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a31*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_597 = Coupling(name = 'GC_597',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a32*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a32*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a32*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_598 = Coupling(name = 'GC_598',
                  value = '-((Delta2cquqd1*complex(0,1)*I43a33*I44a33)/LambdaSMEFT**2) - (Delta1cquqd1*complex(0,1)*I33a33*I8a33)/LambdaSMEFT**2 - (cquqd10*complex(0,1)*I41a33*I8a33)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_599 = Coupling(name = 'GC_599',
                  value = '(2*cee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '(-6*cG)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_601 = Coupling(name = 'GC_601',
                  value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_602 = Coupling(name = 'GC_602',
                  value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_603 = Coupling(name = 'GC_603',
                  value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_604 = Coupling(name = 'GC_604',
                  value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_605 = Coupling(name = 'GC_605',
                  value = '(cle*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '(2*cll*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_607 = Coupling(name = 'GC_607',
                  value = '(2*cll1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_608 = Coupling(name = 'GC_608',
                  value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_609 = Coupling(name = 'GC_609',
                  value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_610 = Coupling(name = 'GC_610',
                  value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_611 = Coupling(name = 'GC_611',
                  value = '(2*Deltadclq3*complex(0,1)*I11a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '(2*Deltadclq3*complex(0,1)*I11a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '(2*Deltadclq3*complex(0,1)*I11a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '(2*Deltadclq3*complex(0,1)*I11a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '(2*Deltadclq3*complex(0,1)*I11a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '(2*Deltadclq3*complex(0,1)*I11a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '(2*Deltadclq3*complex(0,1)*I16a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '(2*Deltadclq3*complex(0,1)*I16a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '(2*Deltadclq3*complex(0,1)*I16a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '(2*Deltadclq3*complex(0,1)*I16a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '(2*Deltadclq3*complex(0,1)*I16a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '(2*Deltadclq3*complex(0,1)*I16a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '(Delta1dcqd1*complex(0,1)*I50a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '(Delta1dcqd8*complex(0,1)*I50a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '(Deltadcqe*complex(0,1)*I50a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '(Delta1dcqd1*complex(0,1)*I50a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '(Delta1dcqd8*complex(0,1)*I50a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '(Deltadcqe*complex(0,1)*I50a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '(Delta1dcqd1*complex(0,1)*I50a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(Delta1dcqd8*complex(0,1)*I50a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(Deltadcqe*complex(0,1)*I50a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(Delta1dcqd1*complex(0,1)*I50a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '(Delta1dcqd8*complex(0,1)*I50a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(Deltadcqe*complex(0,1)*I50a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '(Delta1dcqd1*complex(0,1)*I50a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '(Delta1dcqd8*complex(0,1)*I50a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '(Deltadcqe*complex(0,1)*I50a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '(Delta1dcqd1*complex(0,1)*I50a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '(Delta1dcqd8*complex(0,1)*I50a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '(Deltadcqe*complex(0,1)*I50a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '(Delta1ucqu1*complex(0,1)*I6a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '(Delta1ucqu8*complex(0,1)*I6a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '(Deltaucqe*complex(0,1)*I6a12)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_644 = Coupling(name = 'GC_644',
                  value = '(Delta1ucqu1*complex(0,1)*I6a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = '(Delta1ucqu8*complex(0,1)*I6a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '(Deltaucqe*complex(0,1)*I6a13)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(Delta1ucqu1*complex(0,1)*I6a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(Delta1ucqu8*complex(0,1)*I6a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '(Deltaucqe*complex(0,1)*I6a21)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '(Delta1ucqu1*complex(0,1)*I6a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '(Delta1ucqu8*complex(0,1)*I6a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '(Deltaucqe*complex(0,1)*I6a23)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '(Delta1ucqu1*complex(0,1)*I6a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '(Delta1ucqu8*complex(0,1)*I6a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '(Deltaucqe*complex(0,1)*I6a31)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '(Delta1ucqu1*complex(0,1)*I6a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '(Delta1ucqu8*complex(0,1)*I6a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '(Deltaucqe*complex(0,1)*I6a32)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (2*cdd10*complex(0,1))/LambdaSMEFT**2 + (2*Delta1cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I71a11)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I69a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I70a11)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I71a11)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I71a11)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '(ced0*complex(0,1))/LambdaSMEFT**2 + (Deltaced*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cld0*complex(0,1))/LambdaSMEFT**2 + (Deltacld*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*Sd1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_675 = Coupling(name = 'GC_675',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_676 = Coupling(name = 'GC_676',
                  value = '(2*cdd10*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_677 = Coupling(name = 'GC_677',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (2*cdd10*complex(0,1))/LambdaSMEFT**2 + (2*Delta1cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_680 = Coupling(name = 'GC_680',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_681 = Coupling(name = 'GC_681',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_682 = Coupling(name = 'GC_682',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_684 = Coupling(name = 'GC_684',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_686 = Coupling(name = 'GC_686',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_687 = Coupling(name = 'GC_687',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_688 = Coupling(name = 'GC_688',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_689 = Coupling(name = 'GC_689',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_690 = Coupling(name = 'GC_690',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I71a22)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I69a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I70a22)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I71a22)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I71a22)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(ced0*complex(0,1))/LambdaSMEFT**2 + (Deltaced*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(cld0*complex(0,1))/LambdaSMEFT**2 + (Deltacld*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*Sd2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_696 = Coupling(name = 'GC_696',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_697 = Coupling(name = 'GC_697',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_698 = Coupling(name = 'GC_698',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_699 = Coupling(name = 'GC_699',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_701 = Coupling(name = 'GC_701',
                  value = '(2*cdd10*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_702 = Coupling(name = 'GC_702',
                  value = '(2*cdd10*complex(0,1))/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_703 = Coupling(name = 'GC_703',
                  value = '(2*cdd0*complex(0,1))/LambdaSMEFT**2 + (2*cdd10*complex(0,1))/LambdaSMEFT**2 + (2*Delta1cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2cdd*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2cdd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_704 = Coupling(name = 'GC_704',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1dcqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1dcqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_707 = Coupling(name = 'GC_707',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1dcqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqd8*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1dcqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_717 = Coupling(name = 'GC_717',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq3*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq1*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq3*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a11)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I69a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I6a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I70a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq31*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq11*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta2ucqq31*complex(0,1)*I71a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I71a33)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I69a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I70a33)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I71a33)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*I71a33)/LambdaSMEFT**2 + (2*Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq11*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '(ced0*complex(0,1))/LambdaSMEFT**2 + (Deltaced*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(cld0*complex(0,1))/LambdaSMEFT**2 + (Deltacld*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*Sd3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(ee**2*complex(0,1))/(2.*sth**2)',
                  order = {'QED':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '-((ee**2*complex(0,1))/sth**2)',
                  order = {'QED':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '(cth**2*ee**2*complex(0,1))/sth**2',
                  order = {'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '(-2*dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'QED':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '-((CKM1x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '-((CKM1x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '-((CKM1x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((CKM2x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '-((CKM2x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '-((CKM2x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '-((CKM3x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '-((CKM3x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '-((CKM3x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '-((cth*ee*complex(0,1))/sth)',
                  order = {'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '(-2*cth*ee**2*complex(0,1))/sth',
                  order = {'QED':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_742 = Coupling(name = 'GC_742',
                  value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_743 = Coupling(name = 'GC_743',
                  value = '-(ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '(2*ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '-((ee*complex(0,1)*sth)/cth)',
                  order = {'QED':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_748 = Coupling(name = 'GC_748',
                  value = '-(cth*ee*complex(0,1))/(2.*sth) + (ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '(cth*ee*complex(0,1))/(2.*sth) + (ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '-(cth*ee*complex(0,1))/(2.*sth) - (ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cth*ee*complex(0,1))/(2.*sth) - (ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_753 = Coupling(name = 'GC_753',
                  value = '(cth*DeltacdW*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_754 = Coupling(name = 'GC_754',
                  value = '(cth*DeltacdB*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_755 = Coupling(name = 'GC_755',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_756 = Coupling(name = 'GC_756',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_757 = Coupling(name = 'GC_757',
                  value = '(cth*DeltacdW*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_758 = Coupling(name = 'GC_758',
                  value = '(cth*DeltacdB*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_759 = Coupling(name = 'GC_759',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_760 = Coupling(name = 'GC_760',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_761 = Coupling(name = 'GC_761',
                  value = '(cth*DeltacdW*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_762 = Coupling(name = 'GC_762',
                  value = '(cth*DeltacdB*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_763 = Coupling(name = 'GC_763',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_764 = Coupling(name = 'GC_764',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_765 = Coupling(name = 'GC_765',
                  value = '(cth*DeltacdW*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_766 = Coupling(name = 'GC_766',
                  value = '(cth*DeltacdB*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_767 = Coupling(name = 'GC_767',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_768 = Coupling(name = 'GC_768',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_769 = Coupling(name = 'GC_769',
                  value = '(cth*DeltacdW*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_770 = Coupling(name = 'GC_770',
                  value = '(cth*DeltacdB*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_771 = Coupling(name = 'GC_771',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_772 = Coupling(name = 'GC_772',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_773 = Coupling(name = 'GC_773',
                  value = '(cth*DeltacdW*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_774 = Coupling(name = 'GC_774',
                  value = '(cth*DeltacdB*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_775 = Coupling(name = 'GC_775',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_776 = Coupling(name = 'GC_776',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_777 = Coupling(name = 'GC_777',
                  value = '(cth*DeltacdW*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_778 = Coupling(name = 'GC_778',
                  value = '(cth*DeltacdB*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_779 = Coupling(name = 'GC_779',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_780 = Coupling(name = 'GC_780',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_781 = Coupling(name = 'GC_781',
                  value = '(cth*DeltacdW*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_782 = Coupling(name = 'GC_782',
                  value = '(cth*DeltacdB*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_783 = Coupling(name = 'GC_783',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_784 = Coupling(name = 'GC_784',
                  value = '-((cth*DeltacdW*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_785 = Coupling(name = 'GC_785',
                  value = '(cth*DeltacdW*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_786 = Coupling(name = 'GC_786',
                  value = '(cth*DeltacdB*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_787 = Coupling(name = 'GC_787',
                  value = '-((cth*DeltacdB*complex(0,1)*I55a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I56a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I55a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I56a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_788 = Coupling(name = 'GC_788',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_789 = Coupling(name = 'GC_789',
                  value = '(cth*DeltacdW*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_790 = Coupling(name = 'GC_790',
                  value = '(cth*DeltacdB*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_791 = Coupling(name = 'GC_791',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_792 = Coupling(name = 'GC_792',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cth*DeltacdW*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cth*DeltacdB*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_795 = Coupling(name = 'GC_795',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a12)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a12)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a12*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_796 = Coupling(name = 'GC_796',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_797 = Coupling(name = 'GC_797',
                  value = '(cth*DeltacdW*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_798 = Coupling(name = 'GC_798',
                  value = '(cth*DeltacdB*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_799 = Coupling(name = 'GC_799',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a13)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a13)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a13*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_800 = Coupling(name = 'GC_800',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_801 = Coupling(name = 'GC_801',
                  value = '(cth*DeltacdW*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_802 = Coupling(name = 'GC_802',
                  value = '(cth*DeltacdB*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_803 = Coupling(name = 'GC_803',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a21)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a21)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a21*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_804 = Coupling(name = 'GC_804',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cth*DeltacdW*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_806 = Coupling(name = 'GC_806',
                  value = '(cth*DeltacdB*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_807 = Coupling(name = 'GC_807',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_808 = Coupling(name = 'GC_808',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_809 = Coupling(name = 'GC_809',
                  value = '(cth*DeltacdW*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_810 = Coupling(name = 'GC_810',
                  value = '(cth*DeltacdB*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_811 = Coupling(name = 'GC_811',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a23)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a23)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a23*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_812 = Coupling(name = 'GC_812',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cth*DeltacdW*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_814 = Coupling(name = 'GC_814',
                  value = '(cth*DeltacdB*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_815 = Coupling(name = 'GC_815',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a31)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a31)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a31*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_816 = Coupling(name = 'GC_816',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_817 = Coupling(name = 'GC_817',
                  value = '(cth*DeltacdW*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_818 = Coupling(name = 'GC_818',
                  value = '(cth*DeltacdB*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_819 = Coupling(name = 'GC_819',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a32)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a32)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a32*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_820 = Coupling(name = 'GC_820',
                  value = '-((cth*DeltacdW*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_821 = Coupling(name = 'GC_821',
                  value = '(cth*DeltacdW*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_822 = Coupling(name = 'GC_822',
                  value = '(cth*DeltacdB*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_823 = Coupling(name = 'GC_823',
                  value = '-((cth*DeltacdB*complex(0,1)*I57a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB0*cth*complex(0,1)*I58a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdW*complex(0,1)*I57a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*complex(0,1)*I58a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_824 = Coupling(name = 'GC_824',
                  value = 'ee**2*complex(0,1) + (cth**2*ee**2*complex(0,1))/(2.*sth**2) + (ee**2*complex(0,1)*sth**2)/(2.*cth**2)',
                  order = {'QED':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '(4*cHW*cth**2*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '(4*cHB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '(-2*cHWB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_842 = Coupling(name = 'GC_842',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_843 = Coupling(name = 'GC_843',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_844 = Coupling(name = 'GC_844',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_845 = Coupling(name = 'GC_845',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_846 = Coupling(name = 'GC_846',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_847 = Coupling(name = 'GC_847',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_848 = Coupling(name = 'GC_848',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_849 = Coupling(name = 'GC_849',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_850 = Coupling(name = 'GC_850',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_851 = Coupling(name = 'GC_851',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_852 = Coupling(name = 'GC_852',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_853 = Coupling(name = 'GC_853',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '(4*cuu0*complex(0,1))/LambdaSMEFT**2 + (4*Delta1cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (4*Delta2cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_855 = Coupling(name = 'GC_855',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I5a11)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I11a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I16a11)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I5a11)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(ceu0*complex(0,1))/LambdaSMEFT**2 + (Deltaceu*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '(clu0*complex(0,1))/LambdaSMEFT**2 + (Deltaclu*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a11)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 + (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a11)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Deltauclq3*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I11a11)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_863 = Coupling(name = 'GC_863',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I16a11)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*Su1x1)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_866 = Coupling(name = 'GC_866',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_868 = Coupling(name = 'GC_868',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_869 = Coupling(name = 'GC_869',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_870 = Coupling(name = 'GC_870',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_871 = Coupling(name = 'GC_871',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_872 = Coupling(name = 'GC_872',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_873 = Coupling(name = 'GC_873',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_874 = Coupling(name = 'GC_874',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_875 = Coupling(name = 'GC_875',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_876 = Coupling(name = 'GC_876',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_877 = Coupling(name = 'GC_877',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_878 = Coupling(name = 'GC_878',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_881 = Coupling(name = 'GC_881',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_883 = Coupling(name = 'GC_883',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_885 = Coupling(name = 'GC_885',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_886 = Coupling(name = 'GC_886',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_887 = Coupling(name = 'GC_887',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_888 = Coupling(name = 'GC_888',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_889 = Coupling(name = 'GC_889',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_890 = Coupling(name = 'GC_890',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_891 = Coupling(name = 'GC_891',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_892 = Coupling(name = 'GC_892',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_893 = Coupling(name = 'GC_893',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_894 = Coupling(name = 'GC_894',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '(2*cuu0*complex(0,1))/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_896 = Coupling(name = 'GC_896',
                  value = '(4*cuu0*complex(0,1))/LambdaSMEFT**2 + (4*Delta1cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (4*Delta2cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_897 = Coupling(name = 'GC_897',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_898 = Coupling(name = 'GC_898',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_899 = Coupling(name = 'GC_899',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I5a22)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I11a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I16a22)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I5a22)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_901 = Coupling(name = 'GC_901',
                  value = '(ceu0*complex(0,1))/LambdaSMEFT**2 + (Deltaceu*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_902 = Coupling(name = 'GC_902',
                  value = '(clu0*complex(0,1))/LambdaSMEFT**2 + (Deltaclu*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_903 = Coupling(name = 'GC_903',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_904 = Coupling(name = 'GC_904',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a22)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_905 = Coupling(name = 'GC_905',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 + (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a22)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Deltauclq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_906 = Coupling(name = 'GC_906',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I11a22)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_907 = Coupling(name = 'GC_907',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I16a22)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_908 = Coupling(name = 'GC_908',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*Su2x2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_909 = Coupling(name = 'GC_909',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_910 = Coupling(name = 'GC_910',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cud10*complex(0,1))/LambdaSMEFT**2 + (Delta2cud1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_912 = Coupling(name = 'GC_912',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_913 = Coupling(name = 'GC_913',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_914 = Coupling(name = 'GC_914',
                  value = '(cud80*complex(0,1))/LambdaSMEFT**2 + (Delta2cud8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1cud8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_915 = Coupling(name = 'GC_915',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_917 = Coupling(name = 'GC_917',
                  value = '(cqd10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_918 = Coupling(name = 'GC_918',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_919 = Coupling(name = 'GC_919',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '(cqd80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqd8*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2cqd8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqd8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_921 = Coupling(name = 'GC_921',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2cqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_922 = Coupling(name = 'GC_922',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2cqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2cqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2cqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_925 = Coupling(name = 'GC_925',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1ucqu1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1ucqu1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_933 = Coupling(name = 'GC_933',
                  value = '(cqu10*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu1*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta1ucqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu1*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_934 = Coupling(name = 'GC_934',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_937 = Coupling(name = 'GC_937',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1ucqu8*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_938 = Coupling(name = 'GC_938',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqu8*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1ucqu8*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '(cqu80*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqu8*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta1ucqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cqu8*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '(2*cuu0*complex(0,1))/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '(2*cuu0*complex(0,1))/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '(4*cuu0*complex(0,1))/LambdaSMEFT**2 + (4*Delta1cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (4*Delta2cuu*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq3*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq1*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq3*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a11)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_949 = Coupling(name = 'GC_949',
                  value = '(2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I11a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I16a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I50a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a22)/(4.*LambdaSMEFT**2) + (Delta1dcqq11*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1dcqq31*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq11*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta2dcqq31*complex(0,1)*I5a33)/(4.*LambdaSMEFT**2) + (Delta1ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_950 = Coupling(name = 'GC_950',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I5a33)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 + (2*cqq110*complex(0,1))/LambdaSMEFT**2 + (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (2*cqq310*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I11a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1dcqq3*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta2dcqq3*complex(0,1)*I16a33)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta1dcqq31*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Delta2dcqq31*complex(0,1)*I5a33)/LambdaSMEFT**2 + (2*Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq11*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '(ceu0*complex(0,1))/LambdaSMEFT**2 + (Deltaceu*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_953 = Coupling(name = 'GC_953',
                  value = '(clu0*complex(0,1))/LambdaSMEFT**2 + (Deltaclu*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_954 = Coupling(name = 'GC_954',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_955 = Coupling(name = 'GC_955',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 - (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a33)/LambdaSMEFT**2 - (Deltadclq3*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Deltauclq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_956 = Coupling(name = 'GC_956',
                  value = '(clq10*complex(0,1))/LambdaSMEFT**2 + (clq30*complex(0,1))/LambdaSMEFT**2 + (Deltadclq1*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Deltadclq3*complex(0,1)*I5a33)/LambdaSMEFT**2 + (Deltauclq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Deltauclq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_957 = Coupling(name = 'GC_957',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I11a33)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_958 = Coupling(name = 'GC_958',
                  value = '(2*clq30*complex(0,1))/LambdaSMEFT**2 + (2*Deltadclq3*complex(0,1)*I16a33)/LambdaSMEFT**2 + (2*Deltauclq3*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_959 = Coupling(name = 'GC_959',
                  value = '(cqe0*complex(0,1))/LambdaSMEFT**2 + (Deltadcqe*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Deltaucqe*complex(0,1)*Su3x3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_960 = Coupling(name = 'GC_960',
                  value = '(4*complex(0,1)*gHaa)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(4*complex(0,1)*gHgg)/vevhat',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '(2*complex(0,1)*gHza)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '-6*complex(0,1)*lam*vevhat',
                  order = {'QED':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_969 = Coupling(name = 'GC_969',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_970 = Coupling(name = 'GC_970',
                  value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QCD':1,'QED':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '(DeltacuG*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_972 = Coupling(name = 'GC_972',
                  value = '(3*DeltacuH*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_973 = Coupling(name = 'GC_973',
                  value = '(DeltacuG*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_974 = Coupling(name = 'GC_974',
                  value = '(3*DeltacuH*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_975 = Coupling(name = 'GC_975',
                  value = '(DeltacuG*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_976 = Coupling(name = 'GC_976',
                  value = '(3*DeltacuH*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_977 = Coupling(name = 'GC_977',
                  value = '(DeltacuG*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_978 = Coupling(name = 'GC_978',
                  value = '(3*DeltacuH*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_979 = Coupling(name = 'GC_979',
                  value = '(DeltacuG*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_980 = Coupling(name = 'GC_980',
                  value = '(3*DeltacuH*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_981 = Coupling(name = 'GC_981',
                  value = '(DeltacuG*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_982 = Coupling(name = 'GC_982',
                  value = '(3*DeltacuH*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_983 = Coupling(name = 'GC_983',
                  value = '(3*DeltacdH*complex(0,1)*I1a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_984 = Coupling(name = 'GC_984',
                  value = '(3*DeltacdH*complex(0,1)*I1a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_985 = Coupling(name = 'GC_985',
                  value = '(3*DeltacdH*complex(0,1)*I1a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_986 = Coupling(name = 'GC_986',
                  value = '(3*DeltacdH*complex(0,1)*I2a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_987 = Coupling(name = 'GC_987',
                  value = '(3*DeltacdH*complex(0,1)*I2a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_988 = Coupling(name = 'GC_988',
                  value = '(3*DeltacdH*complex(0,1)*I2a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_989 = Coupling(name = 'GC_989',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((cHl3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':2})

GC_991 = Coupling(name = 'GC_991',
                  value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_992 = Coupling(name = 'GC_992',
                  value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_993 = Coupling(name = 'GC_993',
                  value = '(cHud*ee*complex(0,1)*I61a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_994 = Coupling(name = 'GC_994',
                  value = '(cHud*ee*complex(0,1)*I61a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_995 = Coupling(name = 'GC_995',
                  value = '(cHud*ee*complex(0,1)*I61a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_996 = Coupling(name = 'GC_996',
                  value = '(cHud*ee*complex(0,1)*I61a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_997 = Coupling(name = 'GC_997',
                  value = '(cHud*ee*complex(0,1)*I61a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_998 = Coupling(name = 'GC_998',
                  value = '(cHud*ee*complex(0,1)*I61a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_999 = Coupling(name = 'GC_999',
                  value = '(cHud*ee*complex(0,1)*I61a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(cHud*ee*complex(0,1)*I61a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(cHud*ee*complex(0,1)*I61a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(cHud*ee*complex(0,1)*I66a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(cHud*ee*complex(0,1)*I66a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(cHud*ee*complex(0,1)*I66a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(cHud*ee*complex(0,1)*I66a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(cHud*ee*complex(0,1)*I66a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(cHud*ee*complex(0,1)*I66a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(cHud*ee*complex(0,1)*I66a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(cHud*ee*complex(0,1)*I66a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(cHud*ee*complex(0,1)*I66a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':4})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '(45*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-(cHWB*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(cHud*ee*complex(0,1)*I61a11*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(cHud*ee*complex(0,1)*I61a12*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cHud*ee*complex(0,1)*I61a13*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(cHud*ee*complex(0,1)*I61a21*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(cHud*ee*complex(0,1)*I61a22*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(cHud*ee*complex(0,1)*I61a23*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(cHud*ee*complex(0,1)*I61a31*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(cHud*ee*complex(0,1)*I61a32*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(cHud*ee*complex(0,1)*I61a33*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cHud*ee*complex(0,1)*I66a11*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(cHud*ee*complex(0,1)*I66a12*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(cHud*ee*complex(0,1)*I66a13*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(cHud*ee*complex(0,1)*I66a21*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(cHud*ee*complex(0,1)*I66a22*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(cHud*ee*complex(0,1)*I66a23*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(cHud*ee*complex(0,1)*I66a31*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '(cHud*ee*complex(0,1)*I66a32*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(cHud*ee*complex(0,1)*I66a33*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(15*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':-1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(DeltacdG*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-((DeltacdG*G*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(DeltacdG*G*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(DeltacdG*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((DeltacdG*G*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(DeltacdG*G*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(DeltacdG*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((DeltacdG*G*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '(DeltacdG*G*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '(DeltacdG*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((DeltacdG*G*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(DeltacdG*G*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(DeltacdG*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((DeltacdG*G*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(DeltacdG*G*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(DeltacdG*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-((DeltacdG*G*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(DeltacdG*G*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(DeltacdG*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((DeltacdG*G*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(DeltacdG*G*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(DeltacdG*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-((DeltacdG*G*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(DeltacdG*G*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(DeltacdG*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '-((DeltacdG*G*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(DeltacdG*G*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(DeltacdG*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-((DeltacdG*G*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(DeltacdG*G*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '(DeltacdG*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-((DeltacdG*G*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(DeltacdG*G*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(DeltacdG*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((DeltacdG*G*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(DeltacdG*G*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(DeltacdG*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((DeltacdG*G*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(DeltacdG*G*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(DeltacdG*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-((DeltacdG*G*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(DeltacdG*G*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '(DeltacdG*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-((DeltacdG*G*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '(DeltacdG*G*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(DeltacdG*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-((DeltacdG*G*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(DeltacdG*G*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(DeltacdG*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-((DeltacdG*G*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '(DeltacdG*G*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(DeltacdG*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-((DeltacdG*G*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdG0*G*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(DeltacdG*G*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdG0*G*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '(DeltacuW*complex(0,1)*I62a11*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a11*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '(DeltacuW*ee*complex(0,1)*I62a11*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '(DeltacuW*complex(0,1)*I62a12*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a12*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(DeltacuW*ee*complex(0,1)*I62a12*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(DeltacuW*complex(0,1)*I62a13*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a13*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(DeltacuW*ee*complex(0,1)*I62a13*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(DeltacuW*complex(0,1)*I62a21*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a21*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(DeltacuW*ee*complex(0,1)*I62a21*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(DeltacuW*complex(0,1)*I62a22*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a22*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(DeltacuW*ee*complex(0,1)*I62a22*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '(DeltacuW*complex(0,1)*I62a23*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a23*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(DeltacuW*ee*complex(0,1)*I62a23*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(DeltacuW*complex(0,1)*I62a31*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a31*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(DeltacuW*ee*complex(0,1)*I62a31*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(DeltacuW*complex(0,1)*I62a32*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a32*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(DeltacuW*ee*complex(0,1)*I62a32*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(DeltacuW*complex(0,1)*I62a33*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I63a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-((DeltacuW*ee*complex(0,1)*I62a33*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I63a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(DeltacuW*ee*complex(0,1)*I62a33*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I63a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '-((DeltacuW*complex(0,1)*I67a11*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(DeltacuW*complex(0,1)*I67a11*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a11*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(DeltacuW*ee*complex(0,1)*I67a11*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a11*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-((DeltacuW*complex(0,1)*I67a12*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(DeltacuW*complex(0,1)*I67a12*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a12*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(DeltacuW*ee*complex(0,1)*I67a12*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a12*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-((DeltacuW*complex(0,1)*I67a13*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(DeltacuW*complex(0,1)*I67a13*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a13*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(DeltacuW*ee*complex(0,1)*I67a13*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a13*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '-((DeltacuW*complex(0,1)*I67a21*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(DeltacuW*complex(0,1)*I67a21*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a21*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(DeltacuW*ee*complex(0,1)*I67a21*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a21*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-((DeltacuW*complex(0,1)*I67a22*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(DeltacuW*complex(0,1)*I67a22*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a22*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(DeltacuW*ee*complex(0,1)*I67a22*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a22*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-((DeltacuW*complex(0,1)*I67a23*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(DeltacuW*complex(0,1)*I67a23*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a23*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(DeltacuW*ee*complex(0,1)*I67a23*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a23*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-((DeltacuW*complex(0,1)*I67a31*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(DeltacuW*complex(0,1)*I67a31*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a31*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(DeltacuW*ee*complex(0,1)*I67a31*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a31*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-((DeltacuW*complex(0,1)*I67a32*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(DeltacuW*complex(0,1)*I67a32*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a32*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(DeltacuW*ee*complex(0,1)*I67a32*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a32*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((DeltacuW*complex(0,1)*I67a33*vevhat)/LambdaSMEFT**2) - (cuW0*complex(0,1)*I68a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '(DeltacuW*complex(0,1)*I67a33*vevhat)/LambdaSMEFT**2 + (cuW0*complex(0,1)*I68a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-((DeltacuW*ee*complex(0,1)*I67a33*vevhat)/LambdaSMEFT**2) - (cuW0*ee*complex(0,1)*I68a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '(DeltacuW*ee*complex(0,1)*I67a33*vevhat)/LambdaSMEFT**2 + (cuW0*ee*complex(0,1)*I68a33*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(DeltacdW*ee*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(DeltacdW*ee*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '(DeltacdW*ee*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(DeltacdW*ee*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(DeltacdW*ee*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(DeltacdW*ee*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(DeltacdW*ee*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(DeltacdW*ee*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '-((DeltacdW*ee*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(DeltacdW*ee*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(DeltacdW*ee*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(DeltacdW*ee*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(DeltacdW*ee*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(DeltacdW*ee*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(DeltacdW*ee*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(DeltacdW*ee*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(DeltacdW*ee*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '(DeltacdW*ee*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-((DeltacdW*ee*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cdW0*ee*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '(DeltacdW*ee*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cdW0*ee*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '-((cHq30*CKM1x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a11*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a11*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '-((cHq30*CKM1x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a12*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a12*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-((cHq30*CKM1x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a13*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a13*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '-((cHq30*CKM2x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a21*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a21*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-((cHq30*CKM2x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a22*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a22*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-((cHq30*CKM2x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a23*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a23*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '-((cHq30*CKM3x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a31*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a31*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '-((cHq30*CKM3x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a32*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a32*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '-((cHq30*CKM3x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltadcHq3*ee*complex(0,1)*I59a33*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (DeltaucHq3*ee*complex(0,1)*I60a33*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a11*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a11*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a11*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a11*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a12*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a12*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a12*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a12*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a13*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a13*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a13*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a13*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a21*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a21*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a21*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a21*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a22*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a22*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a22*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a22*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a23*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a23*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a23*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a23*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a31*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a31*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a31*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a31*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a32*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a32*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a32*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a32*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I62a33*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I63a33*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I62a33*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I63a33*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a11*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a11*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a11*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a11*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a12*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a12*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a12*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a12*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a13*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a13*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a13*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a13*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a21*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a21*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a21*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a21*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a22*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a22*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a22*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a22*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a23*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a23*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a23*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a23*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a31*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a31*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a31*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a31*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a32*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a32*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a32*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a32*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '-((cth*DeltacuW*ee*complex(0,1)*I67a33*vevhat)/(LambdaSMEFT**2*sth)) - (cth*cuW0*ee*complex(0,1)*I68a33*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(cth*DeltacuW*ee*complex(0,1)*I67a33*vevhat)/(LambdaSMEFT**2*sth) + (cth*cuW0*ee*complex(0,1)*I68a33*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(cHe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '(cHl1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '(cHl1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '(cth*DeltacuB*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '(cth*DeltacuB*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '(cth*DeltacuB*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '(cth*DeltacuB*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '(cth*DeltacuB*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '(cth*DeltacuB*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(cth*DeltacdW*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '(cth*DeltacdB*complex(0,1)*I55a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '(cth*DeltacdW*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(cth*DeltacdB*complex(0,1)*I55a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(cth*DeltacdW*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '(cth*DeltacdB*complex(0,1)*I55a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '(cth*DeltacdW*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(cth*DeltacdB*complex(0,1)*I55a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '(cth*DeltacdW*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '(cth*DeltacdB*complex(0,1)*I55a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '(cth*DeltacdW*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(cth*DeltacdB*complex(0,1)*I55a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(cth*DeltacdW*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '(cth*DeltacdB*complex(0,1)*I55a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '(cth*DeltacdW*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '(cth*DeltacdB*complex(0,1)*I55a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-((cth*DeltacdW*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I55a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I56a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '(cth*DeltacdW*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I55a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I56a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '(cth*DeltacdB*complex(0,1)*I55a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I56a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I55a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I56a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '(cth*DeltacdW*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '(cth*DeltacdB*complex(0,1)*I57a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '(cth*DeltacdW*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '(cth*DeltacdB*complex(0,1)*I57a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a12*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a12*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(cth*DeltacdW*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '(cth*DeltacdB*complex(0,1)*I57a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a13*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a13*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(cth*DeltacdW*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '(cth*DeltacdB*complex(0,1)*I57a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a21*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a21*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '(cth*DeltacdW*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '(cth*DeltacdB*complex(0,1)*I57a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(cth*DeltacdW*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '(cth*DeltacdB*complex(0,1)*I57a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a23*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a23*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '(cth*DeltacdW*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '(cth*DeltacdB*complex(0,1)*I57a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a31*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a31*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(cth*DeltacdW*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '(cth*DeltacdB*complex(0,1)*I57a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a32*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a32*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '-((cth*DeltacdW*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdW0*cth*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdB*complex(0,1)*I57a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdB0*complex(0,1)*I58a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '(cth*DeltacdW*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdW0*cth*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacdB*complex(0,1)*I57a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*complex(0,1)*I58a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '(cth*DeltacdB*complex(0,1)*I57a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cdB0*cth*complex(0,1)*I58a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdW*complex(0,1)*I57a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW0*complex(0,1)*I58a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a12*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a12*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a12*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a12*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a13*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a13*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a13*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a13*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a21*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a21*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a21*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a21*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a23*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a23*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a23*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a23*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a31*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a31*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a31*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a31*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a32*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a32*vevhat)/(LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a32*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a32*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a12*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a12*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a12*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a12*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a13*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a13*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a13*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a13*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a21*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a21*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a21*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a21*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a23*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a23*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a23*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a23*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a31*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a31*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a31*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a31*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a32*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a32*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a32*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a32*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '(cHd0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd1x1*vevhat)/(LambdaSMEFT**2*sth) + (cHd0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd1x1*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a11*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a11*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd1x1*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd1x1*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a11*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a11*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd1x1*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd1x1*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '(cHd0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd2x2*vevhat)/(LambdaSMEFT**2*sth) + (cHd0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd2x2*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a22*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a22*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd2x2*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd2x2*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a22*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a22*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd2x2*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd2x2*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '(cHd0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd3x3*vevhat)/(LambdaSMEFT**2*sth) + (cHd0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd3x3*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a33*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a33*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd3x3*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd3x3*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a33*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a33*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd3x3*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd3x3*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1312 = Coupling(name = 'GC_1312',
                   value = 'ee**2*complex(0,1)*vevhat + (cth**2*ee**2*complex(0,1)*vevhat)/(2.*sth**2) + (ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2)',
                   order = {'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '(4*cHW*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '(4*cHB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(-2*cHWB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '(cHu0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su1x1*vevhat)/(LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su1x1*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a11*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a11*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a11*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a11*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su1x1*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su1x1*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su1x1*vevhat)/(cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su1x1*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(cHu0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su2x2*vevhat)/(LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su2x2*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a22*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a22*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a22*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a22*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su2x2*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su2x2*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su2x2*vevhat)/(cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su2x2*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '(cHu0*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu0*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su3x3*vevhat)/(LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su3x3*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(cHq10*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a33*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a33*vevhat)/(LambdaSMEFT**2*sth) + (cHq10*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a33*sth*vevhat)/(cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a33*sth*vevhat)/(cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su3x3*vevhat)/(LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su3x3*vevhat)/(LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su3x3*vevhat)/(cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su3x3*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '(3*DeltacuH*complex(0,1)*I17a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I19a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(3*DeltacuH*complex(0,1)*I17a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I19a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '(3*DeltacuH*complex(0,1)*I17a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I19a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(3*DeltacuH*complex(0,1)*I18a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I20a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '(3*DeltacuH*complex(0,1)*I18a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I20a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(3*DeltacuH*complex(0,1)*I18a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuH*complex(0,1)*I20a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '(3*DeltacdH*complex(0,1)*I1a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I3a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(3*DeltacdH*complex(0,1)*I1a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I3a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '(3*DeltacdH*complex(0,1)*I1a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I3a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(3*DeltacdH*complex(0,1)*I2a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I4a11*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '(3*DeltacdH*complex(0,1)*I2a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I4a22*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(3*DeltacdH*complex(0,1)*I2a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacdH*complex(0,1)*I4a33*vevhat**2)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '(6*dMH2*complex(0,1)*lam)/MH**2 - (24*cHbox*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + (6*cHDD*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + 6*dGf*complex(0,1)*lam*cmath.sqrt(2)',
                   order = {'NP':1,'QED':2})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(dgw*ee**2*complex(0,1))/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2)',
                   order = {'NP':1,'QED':2})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHl3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '-((CKM1x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM1x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a11*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a11*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-((CKM1x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM1x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a12*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a12*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '-((CKM1x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM1x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a13*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a13*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '-((CKM2x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM2x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a21*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a21*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-((CKM2x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM2x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a22*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a22*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '-((CKM2x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM2x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a23*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a23*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '-((CKM3x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM3x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a31*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a31*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '-((CKM3x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM3x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a32*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a32*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '-((CKM3x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq30*CKM3x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltadcHq3*ee*complex(0,1)*I59a33*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (DeltaucHq3*ee*complex(0,1)*I60a33*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '(2*cth**2*dgw*ee**2*complex(0,1))/sth**2 - (dsth2*ee**2*complex(0,1))/sth**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (2*cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a12*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a12*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a12*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a12*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a13*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a13*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a13*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a13*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a21*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a21*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a21*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a21*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a23*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a23*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a23*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a23*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a31*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a31*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a31*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a31*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '(cth*DeltadcHq1*ee*complex(0,1)*I5a32*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a32*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltadcHq1*ee*complex(0,1)*I5a32*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a32*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a12*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a12*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a12*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a12*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a13*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a13*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a13*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a13*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a21*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a21*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a21*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a21*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a23*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a23*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a23*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a23*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a31*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a31*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a31*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a31*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '(cth*DeltaucHq1*ee*complex(0,1)*I6a32*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a32*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*I6a32*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a32*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '-(dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '(dgw*ee*complex(0,1))/2. + (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '-(dgw*ee*complex(0,1)) - (dsth2*ee*complex(0,1))/(2.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '-((cth*dgw*ee*complex(0,1))/sth) + (dsth2*ee*complex(0,1))/(2.*cth*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '2*dgw*ee**2*complex(0,1) + (dsth2*ee**2*complex(0,1))/sth**2 - (2*cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-((cth*dsth2*ee**2*complex(0,1))/sth**3) - (4*cth*dgw*ee**2*complex(0,1))/sth + (dsth2*ee**2*complex(0,1))/(cth*sth) + (cHWB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (4*cHW*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) - (dsth2*ee*complex(0,1))/(6.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a11*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a11*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a11*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a11*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd1x1*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd1x1*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) - (dsth2*ee*complex(0,1))/(6.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a22*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a22*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a22*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a22*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd2x2*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd2x2*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) - (dsth2*ee*complex(0,1))/(6.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq1*ee*complex(0,1)*I6a33*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltaucHq3*ee*complex(0,1)*I6a33*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*Sd3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq3*ee*complex(0,1)*Sd3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltaucHq1*ee*complex(0,1)*I6a33*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltaucHq3*ee*complex(0,1)*I6a33*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*Sd3x3*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (DeltadcHq3*ee*complex(0,1)*Sd3x3*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-(dsth2*ee*complex(0,1))/(6.*cth*sth) - (dg1*ee*complex(0,1)*sth)/(3.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHd0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHd0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd1x1*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '-(dsth2*ee*complex(0,1))/(6.*cth*sth) - (dg1*ee*complex(0,1)*sth)/(3.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHd0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHd0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd2x2*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-(dsth2*ee*complex(0,1))/(6.*cth*sth) - (dg1*ee*complex(0,1)*sth)/(3.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) + (cHd0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltacHd*ee*complex(0,1)*Sd3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHd0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (DeltacHd*ee*complex(0,1)*Sd3x3*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) - (dsth2*ee*complex(0,1))/(2.*cth*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '-(dsth2*ee*complex(0,1))/(2.*cth*sth) - (dg1*ee*complex(0,1)*sth)/cth - (cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHe*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(cth*LambdaSMEFT**2) + (cHe*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-(dg1*ee*complex(0,1))/6. + (dsth2*ee*complex(0,1))/(12.*cth**2) + (cHB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth*vevhat**2)/(12.*cth*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '(dg1*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '(dg1*ee*complex(0,1))/2. - (dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = 'dg1*ee**2*complex(0,1) + dgw*ee**2*complex(0,1) + (cth**2*dgw*ee**2*complex(0,1))/sth**2 + (dg1*ee**2*complex(0,1)*sth**2)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHbox*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (5*cHDD*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (5*cHDD*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (5*cHDD*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**2)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**2)/(cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '(cth*dsth2*ee**2*complex(0,1))/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1))/(2.*sth) + (cth*dgw*ee**2*complex(0,1))/(2.*sth) + (dsth2*ee**2*complex(0,1))/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**2)/(2.*cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(dsth2*ee*complex(0,1))/(3.*cth*sth) + (2*dg1*ee*complex(0,1)*sth)/(3.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) + (cHu0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (2*cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHu0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (2*cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (2*cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su1x1*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) + (dsth2*ee*complex(0,1))/(3.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a11*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a11*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a11*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a11*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su1x1*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su1x1*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su1x1*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(dsth2*ee*complex(0,1))/(3.*cth*sth) + (2*dg1*ee*complex(0,1)*sth)/(3.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) + (cHu0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (2*cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHu0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (2*cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (2*cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su2x2*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) + (dsth2*ee*complex(0,1))/(3.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a22*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a22*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a22*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a22*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su2x2*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su2x2*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su2x2*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '(dsth2*ee*complex(0,1))/(3.*cth*sth) + (2*dg1*ee*complex(0,1)*sth)/(3.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) + (cHu0*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (2*cHB*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cHu0*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (2*cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2) + (2*cHB*ee*complex(0,1)*sth**3*vevhat**2)/(3.*cth*LambdaSMEFT**2) + (cth*DeltacHu*ee*complex(0,1)*Su3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltacHu*ee*complex(0,1)*sth*Su3x3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) + (dsth2*ee*complex(0,1))/(3.*cth*sth) + (dg1*ee*complex(0,1)*sth)/(6.*cth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq10*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq30*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cth*DeltadcHq1*ee*complex(0,1)*I5a33*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltadcHq3*ee*complex(0,1)*I5a33*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHq10*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq30*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (DeltadcHq1*ee*complex(0,1)*I5a33*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltadcHq3*ee*complex(0,1)*I5a33*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cth*DeltaucHq1*ee*complex(0,1)*Su3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cth*DeltaucHq3*ee*complex(0,1)*Su3x3*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (DeltaucHq1*ee*complex(0,1)*sth*Su3x3*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (DeltaucHq3*ee*complex(0,1)*sth*Su3x3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(6*dMH2*complex(0,1)*lam*vevhat)/MH**2 - (18*cHbox*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2 + (9*cHDD*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2) + 3*dGf*complex(0,1)*lam*vevhat*cmath.sqrt(2)',
                   order = {'NP':1,'QED':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '(dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) + (dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = 'dg1*ee**2*complex(0,1)*vevhat + dgw*ee**2*complex(0,1)*vevhat + (cth**2*dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (dg1*ee**2*complex(0,1)*sth**2*vevhat)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (3*cHDD*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) + (3*cHDD*cth**2*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**3)/(2.*cth**2*LambdaSMEFT**2) + (3*cHDD*ee**2*complex(0,1)*sth**2*vevhat**3)/(8.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**3)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**3)/(cth**2*LambdaSMEFT**2) + (dGf*ee**2*complex(0,1)*vevhat)/cmath.sqrt(2) + (cth**2*dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2)) + (dGf*ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '(cth*dsth2*ee**2*complex(0,1)*vevhat)/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1)*vevhat)/(2.*sth) + (cth*dgw*ee**2*complex(0,1)*vevhat)/(2.*sth) + (dsth2*ee**2*complex(0,1)*vevhat)/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth*vevhat)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**3)/(2.*cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '(3*cdH0*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '(DeltacdW*complex(0,1)*I1a33)/LambdaSMEFT**2 + (cdW0*complex(0,1)*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '(DeltacdW*complex(0,1)*I2a33)/LambdaSMEFT**2 + (cdW0*complex(0,1)*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '-((DeltacdW*complex(0,1)*I2a33*vevhat)/LambdaSMEFT**2) - (cdW0*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '(DeltacdW*complex(0,1)*I1a33*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(DeltacdW*complex(0,1)*I2a33*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '-((DeltacdW*ee*complex(0,1)*I1a33*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '-((DeltacdW*ee*complex(0,1)*I2a33*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '(DeltacdW*ee*complex(0,1)*I1a33*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(DeltacdW*ee*complex(0,1)*I2a33*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I1a33*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I2a33*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I1a33*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I2a33*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '(dGf*complex(0,1)*yb)/2. + (cdH0*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '(Delta2cquqd1*complex(0,1)*I39a12*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '(Delta2cquqd1*complex(0,1)*I39a13*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '(Delta2cquqd1*complex(0,1)*I39a21*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '(Delta2cquqd1*complex(0,1)*I39a23*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '(Delta2cquqd1*complex(0,1)*I39a31*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '(Delta2cquqd1*complex(0,1)*I39a32*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '(Delta2cquqd1*complex(0,1)*I48a12*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(Delta2cquqd1*complex(0,1)*I48a13*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '(Delta2cquqd1*complex(0,1)*I48a21*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(Delta2cquqd1*complex(0,1)*I48a23*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '(Delta2cquqd1*complex(0,1)*I48a31*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '(Delta2cquqd1*complex(0,1)*I48a32*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '(cuG0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(3*cuH0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-((DeltacuG*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '-((DeltacuG*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '(DeltacuG*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(DeltacuG*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a22*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a22*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a22*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a22*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a22*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a22*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a22*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a22*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a22*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a22*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a22*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a22*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a1*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a22*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a22*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a22*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a2*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a22*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a1*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a22*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a2*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a22*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a3*yc)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a3*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '(cth*DeltacuW*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '(cth*DeltacuW*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-((cth*DeltacuB*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I17a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '-((cth*DeltacuB*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I18a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '(cth*DeltacuB*complex(0,1)*I17a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '(cth*DeltacuB*complex(0,1)*I18a22)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a22*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '-((DeltacuG*G*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '-((DeltacuG*G*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '(DeltacuG*G*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(DeltacuG*G*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '-((DeltacuW*ee*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '-((DeltacuW*ee*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '(DeltacuW*ee*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '(DeltacuW*ee*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '(cth*DeltacuW*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(cth*DeltacuW*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '(cth*cuB0*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '(dGf*complex(0,1)*yc)/2. - (cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2)) + (cuH0*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '(Delta1cquqd1*complex(0,1)*I22a22*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a33*yc)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '(Delta1cquqd1*complex(0,1)*I21a22*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a33*yc)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '(3*cdH0*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '(DeltacdW*complex(0,1)*I1a11)/LambdaSMEFT**2 + (cdW0*complex(0,1)*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '(DeltacdW*complex(0,1)*I2a11)/LambdaSMEFT**2 + (cdW0*complex(0,1)*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '-((DeltacdW*complex(0,1)*I2a11*vevhat)/LambdaSMEFT**2) - (cdW0*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(DeltacdW*complex(0,1)*I1a11*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '(DeltacdW*complex(0,1)*I2a11*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-((DeltacdW*ee*complex(0,1)*I1a11*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-((DeltacdW*ee*complex(0,1)*I2a11*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '(DeltacdW*ee*complex(0,1)*I1a11*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '(DeltacdW*ee*complex(0,1)*I2a11*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I1a11*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I2a11*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I1a11*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I2a11*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(dGf*complex(0,1)*ydo)/2. + (cdH0*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '(Delta2cquqd1*complex(0,1)*I48a11*yc)/LambdaSMEFT**2 + (Delta1cquqd1*complex(0,1)*I21a22*ydo)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(Delta2cquqd1*complex(0,1)*I39a11*yc)/LambdaSMEFT**2 + (Delta1cquqd1*complex(0,1)*I22a22*ydo)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-((ceW*complex(0,1)*ye)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '(ceW*complex(0,1)*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(3*ceH*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-((ceW*complex(0,1)*vevhat*ye)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(ceW*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(ceW*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(ceW*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '-((ceW*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':3})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(ceW*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '(Deltacledq*complex(0,1)*I12a11*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a11*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '(Deltacledq*complex(0,1)*I12a12*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a12*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '(Deltacledq*complex(0,1)*I12a13*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a13*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(Deltacledq*complex(0,1)*I12a21*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a21*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(Deltacledq*complex(0,1)*I12a22*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a22*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '(Deltacledq*complex(0,1)*I12a23*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a23*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '(Deltacledq*complex(0,1)*I12a31*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a31*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '(Deltacledq*complex(0,1)*I12a32*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a32*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '(Deltacledq*complex(0,1)*I12a33*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a33*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '(Deltaclequ1*complex(0,1)*I14a11*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a11*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '(Deltaclequ3*complex(0,1)*I14a11*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a11*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '-(Deltaclequ3*complex(0,1)*I14a11*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a11*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '(Deltaclequ1*complex(0,1)*I14a12*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a12*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '(Deltaclequ3*complex(0,1)*I14a12*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a12*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '-(Deltaclequ3*complex(0,1)*I14a12*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a12*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '(Deltaclequ1*complex(0,1)*I14a13*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a13*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '(Deltaclequ3*complex(0,1)*I14a13*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a13*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '-(Deltaclequ3*complex(0,1)*I14a13*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a13*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '(Deltaclequ1*complex(0,1)*I14a21*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a21*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '(Deltaclequ3*complex(0,1)*I14a21*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a21*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '-(Deltaclequ3*complex(0,1)*I14a21*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a21*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '(Deltaclequ1*complex(0,1)*I14a22*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a22*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '(Deltaclequ3*complex(0,1)*I14a22*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a22*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '-(Deltaclequ3*complex(0,1)*I14a22*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a22*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(Deltaclequ1*complex(0,1)*I14a23*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a23*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '(Deltaclequ3*complex(0,1)*I14a23*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a23*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '-(Deltaclequ3*complex(0,1)*I14a23*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a23*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(Deltaclequ1*complex(0,1)*I14a31*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a31*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '(Deltaclequ3*complex(0,1)*I14a31*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a31*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '-(Deltaclequ3*complex(0,1)*I14a31*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a31*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(Deltaclequ1*complex(0,1)*I14a32*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a32*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(Deltaclequ3*complex(0,1)*I14a32*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a32*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '-(Deltaclequ3*complex(0,1)*I14a32*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a32*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(Deltaclequ1*complex(0,1)*I14a33*ye)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a33*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '(Deltaclequ3*complex(0,1)*I14a33*ye)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a33*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '-(Deltaclequ3*complex(0,1)*I14a33*ye)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a33*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '(Deltacledq*complex(0,1)*I7a11*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a11*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '(Deltacledq*complex(0,1)*I7a12*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a12*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '(Deltacledq*complex(0,1)*I7a13*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a13*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(Deltacledq*complex(0,1)*I7a21*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a21*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(Deltacledq*complex(0,1)*I7a22*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a22*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '(Deltacledq*complex(0,1)*I7a23*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a23*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(Deltacledq*complex(0,1)*I7a31*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a31*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '(Deltacledq*complex(0,1)*I7a32*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a32*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '(Deltacledq*complex(0,1)*I7a33*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a33*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '(clequ10*complex(0,1)*I10a11*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a11*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '(clequ30*complex(0,1)*I10a11*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a11*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '-(clequ30*complex(0,1)*I10a11*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a11*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '(clequ10*complex(0,1)*I10a12*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a12*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '(clequ30*complex(0,1)*I10a12*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a12*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '-(clequ30*complex(0,1)*I10a12*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a12*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '(clequ10*complex(0,1)*I10a13*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a13*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '(clequ30*complex(0,1)*I10a13*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a13*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '-(clequ30*complex(0,1)*I10a13*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a13*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '(clequ10*complex(0,1)*I10a21*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a21*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '(clequ30*complex(0,1)*I10a21*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a21*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '-(clequ30*complex(0,1)*I10a21*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a21*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '(clequ10*complex(0,1)*I10a22*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a22*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '(clequ30*complex(0,1)*I10a22*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a22*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '-(clequ30*complex(0,1)*I10a22*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a22*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '(clequ10*complex(0,1)*I10a23*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a23*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(clequ30*complex(0,1)*I10a23*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a23*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '-(clequ30*complex(0,1)*I10a23*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a23*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '(clequ10*complex(0,1)*I10a31*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a31*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '(clequ30*complex(0,1)*I10a31*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a31*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '-(clequ30*complex(0,1)*I10a31*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a31*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(clequ10*complex(0,1)*I10a32*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a32*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '(clequ30*complex(0,1)*I10a32*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a32*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '-(clequ30*complex(0,1)*I10a32*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a32*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '(clequ10*complex(0,1)*I10a33*ye)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a33*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '(clequ30*complex(0,1)*I10a33*ye)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a33*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '-(clequ30*complex(0,1)*I10a33*ye)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a33*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '-((ceW*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '(ceW*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '(ceB*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '-((ceB*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))) + (ceW*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-((ceW*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '(ceW*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(ceB*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '(dGf*complex(0,1)*ye)/2. + (ceH*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(cHbox*dGf*complex(0,1)*vevhat**2*ye)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ye)/(8.*LambdaSMEFT**2) - (ceH*cHbox*complex(0,1)*vevhat**4*ye)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ye)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(Deltacledq*complex(0,1)*I1a33*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(Deltacledq*complex(0,1)*I2a33*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '-((Deltaclequ1*complex(0,1)*I21a22*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '-((Deltaclequ1*complex(0,1)*I22a22*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '-(Deltaclequ3*complex(0,1)*I21a22*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '-(Deltaclequ3*complex(0,1)*I22a22*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '(Deltaclequ3*complex(0,1)*I21a22*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '(Deltaclequ3*complex(0,1)*I22a22*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '(Deltacledq*complex(0,1)*I1a11*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '(Deltacledq*complex(0,1)*I2a11*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ye)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '-((ceW*complex(0,1)*ym)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '(ceW*complex(0,1)*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(3*ceH*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '-((ceW*complex(0,1)*vevhat*ym)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '(ceW*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '(ceW*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(ceW*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '-((ceW*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':3})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '(ceW*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '(Deltacledq*complex(0,1)*I12a11*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a11*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(Deltacledq*complex(0,1)*I12a12*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a12*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '(Deltacledq*complex(0,1)*I12a13*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a13*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(Deltacledq*complex(0,1)*I12a21*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a21*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '(Deltacledq*complex(0,1)*I12a22*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a22*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '(Deltacledq*complex(0,1)*I12a23*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a23*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '(Deltacledq*complex(0,1)*I12a31*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a31*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(Deltacledq*complex(0,1)*I12a32*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a32*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '(Deltacledq*complex(0,1)*I12a33*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a33*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '(Deltaclequ1*complex(0,1)*I14a11*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a11*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '(Deltaclequ3*complex(0,1)*I14a11*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a11*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '-(Deltaclequ3*complex(0,1)*I14a11*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a11*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '(Deltaclequ1*complex(0,1)*I14a12*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a12*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '(Deltaclequ3*complex(0,1)*I14a12*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a12*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '-(Deltaclequ3*complex(0,1)*I14a12*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a12*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '(Deltaclequ1*complex(0,1)*I14a13*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a13*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '(Deltaclequ3*complex(0,1)*I14a13*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a13*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '-(Deltaclequ3*complex(0,1)*I14a13*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a13*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '(Deltaclequ1*complex(0,1)*I14a21*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a21*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '(Deltaclequ3*complex(0,1)*I14a21*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a21*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '-(Deltaclequ3*complex(0,1)*I14a21*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a21*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '(Deltaclequ1*complex(0,1)*I14a22*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a22*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '(Deltaclequ3*complex(0,1)*I14a22*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a22*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '-(Deltaclequ3*complex(0,1)*I14a22*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a22*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(Deltaclequ1*complex(0,1)*I14a23*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a23*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '(Deltaclequ3*complex(0,1)*I14a23*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a23*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '-(Deltaclequ3*complex(0,1)*I14a23*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a23*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '(Deltaclequ1*complex(0,1)*I14a31*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a31*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '(Deltaclequ3*complex(0,1)*I14a31*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a31*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '-(Deltaclequ3*complex(0,1)*I14a31*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a31*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(Deltaclequ1*complex(0,1)*I14a32*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a32*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '(Deltaclequ3*complex(0,1)*I14a32*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a32*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '-(Deltaclequ3*complex(0,1)*I14a32*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a32*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(Deltaclequ1*complex(0,1)*I14a33*ym)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a33*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(Deltaclequ3*complex(0,1)*I14a33*ym)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a33*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '-(Deltaclequ3*complex(0,1)*I14a33*ym)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a33*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(Deltacledq*complex(0,1)*I7a11*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a11*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(Deltacledq*complex(0,1)*I7a12*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a12*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '(Deltacledq*complex(0,1)*I7a13*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a13*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(Deltacledq*complex(0,1)*I7a21*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a21*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '(Deltacledq*complex(0,1)*I7a22*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a22*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '(Deltacledq*complex(0,1)*I7a23*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a23*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '(Deltacledq*complex(0,1)*I7a31*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a31*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '(Deltacledq*complex(0,1)*I7a32*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a32*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '(Deltacledq*complex(0,1)*I7a33*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a33*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(clequ10*complex(0,1)*I10a11*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a11*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '(clequ30*complex(0,1)*I10a11*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a11*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '-(clequ30*complex(0,1)*I10a11*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a11*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '(clequ10*complex(0,1)*I10a12*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a12*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(clequ30*complex(0,1)*I10a12*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a12*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '-(clequ30*complex(0,1)*I10a12*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a12*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '(clequ10*complex(0,1)*I10a13*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a13*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '(clequ30*complex(0,1)*I10a13*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a13*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '-(clequ30*complex(0,1)*I10a13*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a13*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '(clequ10*complex(0,1)*I10a21*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a21*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(clequ30*complex(0,1)*I10a21*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a21*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '-(clequ30*complex(0,1)*I10a21*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a21*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '(clequ10*complex(0,1)*I10a22*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a22*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '(clequ30*complex(0,1)*I10a22*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a22*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '-(clequ30*complex(0,1)*I10a22*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a22*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(clequ10*complex(0,1)*I10a23*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a23*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '(clequ30*complex(0,1)*I10a23*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a23*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '-(clequ30*complex(0,1)*I10a23*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a23*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(clequ10*complex(0,1)*I10a31*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a31*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '(clequ30*complex(0,1)*I10a31*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a31*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '-(clequ30*complex(0,1)*I10a31*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a31*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '(clequ10*complex(0,1)*I10a32*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a32*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(clequ30*complex(0,1)*I10a32*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a32*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '-(clequ30*complex(0,1)*I10a32*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a32*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '(clequ10*complex(0,1)*I10a33*ym)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a33*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '(clequ30*complex(0,1)*I10a33*ym)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a33*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '-(clequ30*complex(0,1)*I10a33*ym)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a33*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '-((ceW*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(ceW*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '(ceB*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '-((ceB*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))) + (ceW*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '-((ceW*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(ceW*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '(ceB*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(dGf*complex(0,1)*ym)/2. + (ceH*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(cHbox*dGf*complex(0,1)*vevhat**2*ym)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ym)/(8.*LambdaSMEFT**2) - (ceH*cHbox*complex(0,1)*vevhat**4*ym)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ym)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '(Deltacledq*complex(0,1)*I1a33*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '(Deltacledq*complex(0,1)*I2a33*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '-((Deltaclequ1*complex(0,1)*I21a22*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '-((Deltaclequ1*complex(0,1)*I22a22*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '-(Deltaclequ3*complex(0,1)*I21a22*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '-(Deltaclequ3*complex(0,1)*I22a22*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(Deltaclequ3*complex(0,1)*I21a22*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '(Deltaclequ3*complex(0,1)*I22a22*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '(Deltacledq*complex(0,1)*I1a11*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '(Deltacledq*complex(0,1)*I2a11*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ym)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '(3*cdH0*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '(DeltacdW*complex(0,1)*I1a22)/LambdaSMEFT**2 + (cdW0*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '(DeltacdW*complex(0,1)*I2a22)/LambdaSMEFT**2 + (cdW0*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '-((DeltacdW*complex(0,1)*I2a22*vevhat)/LambdaSMEFT**2) - (cdW0*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '(DeltacdW*complex(0,1)*I1a22*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '(DeltacdW*complex(0,1)*I2a22*vevhat)/LambdaSMEFT**2 + (cdW0*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '-((DeltacdW*ee*complex(0,1)*I1a22*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '-((DeltacdW*ee*complex(0,1)*I2a22*vevhat)/LambdaSMEFT**2) - (cdW0*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '(DeltacdW*ee*complex(0,1)*I1a22*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '(DeltacdW*ee*complex(0,1)*I2a22*vevhat)/LambdaSMEFT**2 + (cdW0*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I1a22*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '-((cth*DeltacdW*ee*complex(0,1)*I2a22*vevhat)/(LambdaSMEFT**2*sth)) - (cdW0*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I1a22*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(cth*DeltacdW*ee*complex(0,1)*I2a22*vevhat)/(LambdaSMEFT**2*sth) + (cdW0*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '(dGf*complex(0,1)*ys)/2. + (cdH0*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '(Delta2cquqd1*complex(0,1)*I48a22*yc)/LambdaSMEFT**2 + (Delta1cquqd1*complex(0,1)*I21a22*ys)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '(Delta2cquqd1*complex(0,1)*I39a22*yc)/LambdaSMEFT**2 + (Delta1cquqd1*complex(0,1)*I22a22*ys)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(Deltacledq*complex(0,1)*I1a22*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ye*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '(Deltacledq*complex(0,1)*I2a22*ye)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ye*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '(Deltacledq*complex(0,1)*I1a22*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ym*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '(Deltacledq*complex(0,1)*I2a22*ym)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ym*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '(Delta2cquqd1*complex(0,1)*I39a12*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '(Delta2cquqd1*complex(0,1)*I39a13*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '(Delta2cquqd1*complex(0,1)*I39a21*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '(Delta2cquqd1*complex(0,1)*I39a23*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '(Delta2cquqd1*complex(0,1)*I39a31*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(Delta2cquqd1*complex(0,1)*I39a32*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '(Delta2cquqd1*complex(0,1)*I48a12*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '(Delta2cquqd1*complex(0,1)*I48a13*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '(Delta2cquqd1*complex(0,1)*I48a21*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(Delta2cquqd1*complex(0,1)*I48a23*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '(Delta2cquqd1*complex(0,1)*I48a31*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '(Delta2cquqd1*complex(0,1)*I48a32*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '(cuG0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(3*cuH0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '-((DeltacuG*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '-((DeltacuG*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '(DeltacuG*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '(DeltacuG*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a33*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a33*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a33*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a33*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a33*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a33*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a33*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a33*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a33*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a33*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a33*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a33*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a1*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a33*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a33*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a33*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a2*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a33*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a1*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a33*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a2*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a33*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a3*yt)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a3*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '(cth*DeltacuW*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(cth*DeltacuW*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '-((cth*DeltacuB*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I17a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '-((cth*DeltacuB*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I18a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '(cth*DeltacuB*complex(0,1)*I17a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '(cth*DeltacuB*complex(0,1)*I18a33)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a33*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '-((DeltacuG*G*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '-((DeltacuG*G*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '(DeltacuG*G*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1760 = Coupling(name = 'GC_1760',
                   value = '(DeltacuG*G*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '-((DeltacuW*ee*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '-((DeltacuW*ee*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '(DeltacuW*ee*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1764 = Coupling(name = 'GC_1764',
                   value = '(DeltacuW*ee*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '(cth*DeltacuW*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '(cth*DeltacuW*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '(cth*cuB0*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(dGf*complex(0,1)*yt)/2. - (cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2)) + (cuH0*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '(Delta1cquqd1*complex(0,1)*I22a33*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a33*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(Delta1cquqd1*complex(0,1)*I21a33*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a33*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '(Delta1cquqd1*complex(0,1)*I22a33*ydo)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a11*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(Delta1cquqd1*complex(0,1)*I21a33*ydo)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a11*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '-((Deltaclequ1*complex(0,1)*I21a33*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ye*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '-((Deltaclequ1*complex(0,1)*I22a33*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ye*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1777 = Coupling(name = 'GC_1777',
                   value = '-(Deltaclequ3*complex(0,1)*I21a33*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ye*yt)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '-(Deltaclequ3*complex(0,1)*I22a33*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ye*yt)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '(Deltaclequ3*complex(0,1)*I21a33*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ye*yt)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '(Deltaclequ3*complex(0,1)*I22a33*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ye*yt)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '-((Deltaclequ1*complex(0,1)*I21a33*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ym*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '-((Deltaclequ1*complex(0,1)*I22a33*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ym*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '-(Deltaclequ3*complex(0,1)*I21a33*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ym*yt)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '-(Deltaclequ3*complex(0,1)*I22a33*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ym*yt)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '(Deltaclequ3*complex(0,1)*I21a33*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ym*yt)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '(Deltaclequ3*complex(0,1)*I22a33*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ym*yt)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '(Delta1cquqd1*complex(0,1)*I22a33*ys)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a22*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '(Delta1cquqd1*complex(0,1)*I21a33*ys)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a22*yt)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '-((ceW*complex(0,1)*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '(ceW*complex(0,1)*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '(3*ceH*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '-((ceW*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1794 = Coupling(name = 'GC_1794',
                   value = '(ceW*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '(ceW*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '-((ceW*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '(ceW*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '-((ceW*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':3})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '(ceW*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '(Deltacledq*complex(0,1)*I12a11*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a11*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '(Deltacledq*complex(0,1)*I12a12*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a12*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1803 = Coupling(name = 'GC_1803',
                   value = '(Deltacledq*complex(0,1)*I12a13*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a13*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '(Deltacledq*complex(0,1)*I12a21*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a21*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '(Deltacledq*complex(0,1)*I12a22*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a22*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '(Deltacledq*complex(0,1)*I12a23*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a23*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '(Deltacledq*complex(0,1)*I12a31*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a31*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(Deltacledq*complex(0,1)*I12a32*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a32*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '(Deltacledq*complex(0,1)*I12a33*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I13a33*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '(Deltaclequ1*complex(0,1)*I14a11*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a11*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '(Deltaclequ3*complex(0,1)*I14a11*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a11*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '-(Deltaclequ3*complex(0,1)*I14a11*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a11*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '(Deltaclequ1*complex(0,1)*I14a12*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a12*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '(Deltaclequ3*complex(0,1)*I14a12*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a12*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '-(Deltaclequ3*complex(0,1)*I14a12*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a12*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '(Deltaclequ1*complex(0,1)*I14a13*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a13*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '(Deltaclequ3*complex(0,1)*I14a13*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a13*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '-(Deltaclequ3*complex(0,1)*I14a13*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a13*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '(Deltaclequ1*complex(0,1)*I14a21*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a21*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '(Deltaclequ3*complex(0,1)*I14a21*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a21*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '-(Deltaclequ3*complex(0,1)*I14a21*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a21*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '(Deltaclequ1*complex(0,1)*I14a22*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a22*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '(Deltaclequ3*complex(0,1)*I14a22*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a22*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '-(Deltaclequ3*complex(0,1)*I14a22*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a22*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '(Deltaclequ1*complex(0,1)*I14a23*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a23*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '(Deltaclequ3*complex(0,1)*I14a23*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a23*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '-(Deltaclequ3*complex(0,1)*I14a23*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a23*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '(Deltaclequ1*complex(0,1)*I14a31*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a31*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '(Deltaclequ3*complex(0,1)*I14a31*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a31*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '-(Deltaclequ3*complex(0,1)*I14a31*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a31*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '(Deltaclequ1*complex(0,1)*I14a32*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a32*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '(Deltaclequ3*complex(0,1)*I14a32*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a32*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '-(Deltaclequ3*complex(0,1)*I14a32*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a32*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1834 = Coupling(name = 'GC_1834',
                   value = '(Deltaclequ1*complex(0,1)*I14a33*ytau)/LambdaSMEFT**2 + (clequ10*complex(0,1)*I15a33*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1835 = Coupling(name = 'GC_1835',
                   value = '(Deltaclequ3*complex(0,1)*I14a33*ytau)/(4.*LambdaSMEFT**2) + (clequ30*complex(0,1)*I15a33*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1836 = Coupling(name = 'GC_1836',
                   value = '-(Deltaclequ3*complex(0,1)*I14a33*ytau)/(2.*LambdaSMEFT**2) - (clequ30*complex(0,1)*I15a33*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '(Deltacledq*complex(0,1)*I7a11*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a11*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '(Deltacledq*complex(0,1)*I7a12*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a12*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '(Deltacledq*complex(0,1)*I7a13*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a13*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '(Deltacledq*complex(0,1)*I7a21*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a21*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '(Deltacledq*complex(0,1)*I7a22*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a22*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '(Deltacledq*complex(0,1)*I7a23*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a23*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '(Deltacledq*complex(0,1)*I7a31*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a31*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(Deltacledq*complex(0,1)*I7a32*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a32*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '(Deltacledq*complex(0,1)*I7a33*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*I8a33*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(clequ10*complex(0,1)*I10a11*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a11*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '(clequ30*complex(0,1)*I10a11*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a11*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '-(clequ30*complex(0,1)*I10a11*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a11*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '(clequ10*complex(0,1)*I10a12*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a12*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '(clequ30*complex(0,1)*I10a12*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a12*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '-(clequ30*complex(0,1)*I10a12*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a12*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '(clequ10*complex(0,1)*I10a13*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a13*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '(clequ30*complex(0,1)*I10a13*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a13*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '-(clequ30*complex(0,1)*I10a13*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a13*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '(clequ10*complex(0,1)*I10a21*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a21*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '(clequ30*complex(0,1)*I10a21*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a21*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '-(clequ30*complex(0,1)*I10a21*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a21*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '(clequ10*complex(0,1)*I10a22*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a22*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1859 = Coupling(name = 'GC_1859',
                   value = '(clequ30*complex(0,1)*I10a22*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a22*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '-(clequ30*complex(0,1)*I10a22*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a22*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1861 = Coupling(name = 'GC_1861',
                   value = '(clequ10*complex(0,1)*I10a23*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a23*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '(clequ30*complex(0,1)*I10a23*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a23*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '-(clequ30*complex(0,1)*I10a23*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a23*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '(clequ10*complex(0,1)*I10a31*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a31*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '(clequ30*complex(0,1)*I10a31*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a31*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '-(clequ30*complex(0,1)*I10a31*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a31*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '(clequ10*complex(0,1)*I10a32*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a32*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '(clequ30*complex(0,1)*I10a32*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a32*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '-(clequ30*complex(0,1)*I10a32*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a32*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '(clequ10*complex(0,1)*I10a33*ytau)/LambdaSMEFT**2 + (Deltaclequ1*complex(0,1)*I9a33*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '(clequ30*complex(0,1)*I10a33*ytau)/(4.*LambdaSMEFT**2) + (Deltaclequ3*complex(0,1)*I9a33*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '-(clequ30*complex(0,1)*I10a33*ytau)/(2.*LambdaSMEFT**2) - (Deltaclequ3*complex(0,1)*I9a33*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '-((ceW*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '(ceW*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '(ceB*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '-((ceB*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))) + (ceW*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '-((ceW*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(ceW*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) + (ceB*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '(ceB*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '(dGf*complex(0,1)*ytau)/2. + (ceH*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1881 = Coupling(name = 'GC_1881',
                   value = '(cHbox*dGf*complex(0,1)*vevhat**2*ytau)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ytau)/(8.*LambdaSMEFT**2) - (ceH*cHbox*complex(0,1)*vevhat**4*ytau)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ytau)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1882 = Coupling(name = 'GC_1882',
                   value = '(Deltacledq*complex(0,1)*I1a33*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1883 = Coupling(name = 'GC_1883',
                   value = '(Deltacledq*complex(0,1)*I2a33*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*yb*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '-((Deltaclequ1*complex(0,1)*I21a22*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '-((Deltaclequ1*complex(0,1)*I22a22*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yc*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '-(Deltaclequ3*complex(0,1)*I21a22*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '-(Deltaclequ3*complex(0,1)*I22a22*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '(Deltaclequ3*complex(0,1)*I21a22*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '(Deltaclequ3*complex(0,1)*I22a22*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(Deltacledq*complex(0,1)*I1a11*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '(Deltacledq*complex(0,1)*I2a11*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ydo*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(Deltacledq*complex(0,1)*I1a22*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ys*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '(Deltacledq*complex(0,1)*I2a22*ytau)/LambdaSMEFT**2 + (cledq0*complex(0,1)*ys*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '-((Deltaclequ1*complex(0,1)*I21a33*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yt*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1895 = Coupling(name = 'GC_1895',
                   value = '-((Deltaclequ1*complex(0,1)*I22a33*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*yt*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1896 = Coupling(name = 'GC_1896',
                   value = '-(Deltaclequ3*complex(0,1)*I21a33*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yt*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1897 = Coupling(name = 'GC_1897',
                   value = '-(Deltaclequ3*complex(0,1)*I22a33*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*yt*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1898 = Coupling(name = 'GC_1898',
                   value = '(Deltaclequ3*complex(0,1)*I21a33*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yt*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1899 = Coupling(name = 'GC_1899',
                   value = '(Deltaclequ3*complex(0,1)*I22a33*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*yt*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1900 = Coupling(name = 'GC_1900',
                   value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1901 = Coupling(name = 'GC_1901',
                   value = '(Delta2cquqd1*complex(0,1)*I39a12*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1902 = Coupling(name = 'GC_1902',
                   value = '(Delta2cquqd1*complex(0,1)*I39a13*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1903 = Coupling(name = 'GC_1903',
                   value = '(Delta2cquqd1*complex(0,1)*I39a21*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1904 = Coupling(name = 'GC_1904',
                   value = '(Delta2cquqd1*complex(0,1)*I39a23*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1905 = Coupling(name = 'GC_1905',
                   value = '(Delta2cquqd1*complex(0,1)*I39a31*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1906 = Coupling(name = 'GC_1906',
                   value = '(Delta2cquqd1*complex(0,1)*I39a32*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1907 = Coupling(name = 'GC_1907',
                   value = '(Delta2cquqd1*complex(0,1)*I48a12*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1908 = Coupling(name = 'GC_1908',
                   value = '(Delta2cquqd1*complex(0,1)*I48a13*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1909 = Coupling(name = 'GC_1909',
                   value = '(Delta2cquqd1*complex(0,1)*I48a21*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1910 = Coupling(name = 'GC_1910',
                   value = '(Delta2cquqd1*complex(0,1)*I48a23*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1911 = Coupling(name = 'GC_1911',
                   value = '(Delta2cquqd1*complex(0,1)*I48a31*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1912 = Coupling(name = 'GC_1912',
                   value = '(Delta2cquqd1*complex(0,1)*I48a32*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1913 = Coupling(name = 'GC_1913',
                   value = '(cuG0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1914 = Coupling(name = 'GC_1914',
                   value = '(3*cuH0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1915 = Coupling(name = 'GC_1915',
                   value = '-((DeltacuG*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1916 = Coupling(name = 'GC_1916',
                   value = '-((DeltacuG*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1917 = Coupling(name = 'GC_1917',
                   value = '(DeltacuG*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1918 = Coupling(name = 'GC_1918',
                   value = '(DeltacuG*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1919 = Coupling(name = 'GC_1919',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a11*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1920 = Coupling(name = 'GC_1920',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a11*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1921 = Coupling(name = 'GC_1921',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a11*I28a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1922 = Coupling(name = 'GC_1922',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a11*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1923 = Coupling(name = 'GC_1923',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a11*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1924 = Coupling(name = 'GC_1924',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a11*I28a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1925 = Coupling(name = 'GC_1925',
                   value = '(Delta1cquqd8*complex(0,1)*I26a1*I27a11*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a1*I28a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a1*I40a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1926 = Coupling(name = 'GC_1926',
                   value = '(Delta1cquqd8*complex(0,1)*I26a2*I27a11*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a2*I28a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a2*I40a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1927 = Coupling(name = 'GC_1927',
                   value = '(Delta1cquqd8*complex(0,1)*I26a3*I27a11*I28a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I26a3*I28a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I26a3*I40a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1928 = Coupling(name = 'GC_1928',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a11*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1929 = Coupling(name = 'GC_1929',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a11*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1930 = Coupling(name = 'GC_1930',
                   value = '(Delta1cquqd8*complex(0,1)*I23a1*I24a11*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a1*I25a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a1*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1931 = Coupling(name = 'GC_1931',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a11*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1932 = Coupling(name = 'GC_1932',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a11*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1933 = Coupling(name = 'GC_1933',
                   value = '(Delta1cquqd8*complex(0,1)*I23a2*I24a11*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a2*I25a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a2*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1934 = Coupling(name = 'GC_1934',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a11*I25a1)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a1*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a1*I49a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1935 = Coupling(name = 'GC_1935',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a11*I25a2)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a2*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a2*I49a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1936 = Coupling(name = 'GC_1936',
                   value = '(Delta1cquqd8*complex(0,1)*I23a3*I24a11*I25a3)/LambdaSMEFT**2 + (cquqd80*complex(0,1)*I23a3*I25a3*yup)/LambdaSMEFT**2 + (Delta2cquqd8*complex(0,1)*I47a3*I49a3*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1937 = Coupling(name = 'GC_1937',
                   value = '(cth*DeltacuW*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1938 = Coupling(name = 'GC_1938',
                   value = '(cth*DeltacuW*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1939 = Coupling(name = 'GC_1939',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1940 = Coupling(name = 'GC_1940',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1941 = Coupling(name = 'GC_1941',
                   value = '-((cth*DeltacuB*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I17a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1942 = Coupling(name = 'GC_1942',
                   value = '-((cth*DeltacuB*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2))) - (DeltacuW*complex(0,1)*I18a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuB0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuW0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1943 = Coupling(name = 'GC_1943',
                   value = '(cth*DeltacuB*complex(0,1)*I17a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I17a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1944 = Coupling(name = 'GC_1944',
                   value = '(cth*DeltacuB*complex(0,1)*I18a11)/(LambdaSMEFT**2*cmath.sqrt(2)) + (DeltacuW*complex(0,1)*I18a11*sth)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuB0*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1945 = Coupling(name = 'GC_1945',
                   value = '-((DeltacuG*G*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1946 = Coupling(name = 'GC_1946',
                   value = '-((DeltacuG*G*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cuG0*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1947 = Coupling(name = 'GC_1947',
                   value = '(DeltacuG*G*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1948 = Coupling(name = 'GC_1948',
                   value = '(DeltacuG*G*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuG0*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1949 = Coupling(name = 'GC_1949',
                   value = '-((DeltacuW*ee*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1950 = Coupling(name = 'GC_1950',
                   value = '-((DeltacuW*ee*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (cuW0*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1951 = Coupling(name = 'GC_1951',
                   value = '(DeltacuW*ee*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1952 = Coupling(name = 'GC_1952',
                   value = '(DeltacuW*ee*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) + (cuW0*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1953 = Coupling(name = 'GC_1953',
                   value = '(cth*DeltacuW*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I17a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1954 = Coupling(name = 'GC_1954',
                   value = '(cth*DeltacuW*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (DeltacuB*complex(0,1)*I18a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cth*cuW0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB0*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1955 = Coupling(name = 'GC_1955',
                   value = '-((cth*DeltacuW*complex(0,1)*I17a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I17a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1956 = Coupling(name = 'GC_1956',
                   value = '-((cth*DeltacuW*complex(0,1)*I18a11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) + (DeltacuB*complex(0,1)*I18a11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cth*cuW0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuB0*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1957 = Coupling(name = 'GC_1957',
                   value = '(cth*cuB0*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW0*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1958 = Coupling(name = 'GC_1958',
                   value = '(dGf*complex(0,1)*yup)/2. - (cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2)) + (cuH0*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1959 = Coupling(name = 'GC_1959',
                   value = '(Delta1cquqd1*complex(0,1)*I22a11*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a33*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1960 = Coupling(name = 'GC_1960',
                   value = '(Delta1cquqd1*complex(0,1)*I21a11*yb)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a33*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1961 = Coupling(name = 'GC_1961',
                   value = '(Delta1cquqd1*complex(0,1)*I22a11*ydo)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a11*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1962 = Coupling(name = 'GC_1962',
                   value = '(Delta1cquqd1*complex(0,1)*I21a11*ydo)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a11*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1963 = Coupling(name = 'GC_1963',
                   value = '-((Deltaclequ1*complex(0,1)*I21a11*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ye*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1964 = Coupling(name = 'GC_1964',
                   value = '-((Deltaclequ1*complex(0,1)*I22a11*ye)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ye*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1965 = Coupling(name = 'GC_1965',
                   value = '-(Deltaclequ3*complex(0,1)*I21a11*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1966 = Coupling(name = 'GC_1966',
                   value = '-(Deltaclequ3*complex(0,1)*I22a11*ye)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1967 = Coupling(name = 'GC_1967',
                   value = '(Deltaclequ3*complex(0,1)*I21a11*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1968 = Coupling(name = 'GC_1968',
                   value = '(Deltaclequ3*complex(0,1)*I22a11*ye)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1969 = Coupling(name = 'GC_1969',
                   value = '-((Deltaclequ1*complex(0,1)*I21a11*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ym*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1970 = Coupling(name = 'GC_1970',
                   value = '-((Deltaclequ1*complex(0,1)*I22a11*ym)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ym*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1971 = Coupling(name = 'GC_1971',
                   value = '-(Deltaclequ3*complex(0,1)*I21a11*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1972 = Coupling(name = 'GC_1972',
                   value = '-(Deltaclequ3*complex(0,1)*I22a11*ym)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1973 = Coupling(name = 'GC_1973',
                   value = '(Deltaclequ3*complex(0,1)*I21a11*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1974 = Coupling(name = 'GC_1974',
                   value = '(Deltaclequ3*complex(0,1)*I22a11*ym)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1975 = Coupling(name = 'GC_1975',
                   value = '(Delta1cquqd1*complex(0,1)*I22a11*ys)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I39a22*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1976 = Coupling(name = 'GC_1976',
                   value = '(Delta1cquqd1*complex(0,1)*I21a11*ys)/LambdaSMEFT**2 + (Delta2cquqd1*complex(0,1)*I48a22*yup)/LambdaSMEFT**2 + (cquqd10*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1977 = Coupling(name = 'GC_1977',
                   value = '-((Deltaclequ1*complex(0,1)*I21a11*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ytau*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1978 = Coupling(name = 'GC_1978',
                   value = '-((Deltaclequ1*complex(0,1)*I22a11*ytau)/LambdaSMEFT**2) - (clequ10*complex(0,1)*ytau*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1979 = Coupling(name = 'GC_1979',
                   value = '-(Deltaclequ3*complex(0,1)*I21a11*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1980 = Coupling(name = 'GC_1980',
                   value = '-(Deltaclequ3*complex(0,1)*I22a11*ytau)/(4.*LambdaSMEFT**2) - (clequ30*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1981 = Coupling(name = 'GC_1981',
                   value = '(Deltaclequ3*complex(0,1)*I21a11*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1982 = Coupling(name = 'GC_1982',
                   value = '(Deltaclequ3*complex(0,1)*I22a11*ytau)/(2.*LambdaSMEFT**2) + (clequ30*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1983 = Coupling(name = 'GC_1983',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1984 = Coupling(name = 'GC_1984',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1985 = Coupling(name = 'GC_1985',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (CKM1x1*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1986 = Coupling(name = 'GC_1986',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1987 = Coupling(name = 'GC_1987',
                   value = '(Delta1dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (CKM2x1*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1988 = Coupling(name = 'GC_1988',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1989 = Coupling(name = 'GC_1989',
                   value = '(Delta1dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (CKM3x1*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1990 = Coupling(name = 'GC_1990',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1991 = Coupling(name = 'GC_1991',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1992 = Coupling(name = 'GC_1992',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1993 = Coupling(name = 'GC_1993',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1994 = Coupling(name = 'GC_1994',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1995 = Coupling(name = 'GC_1995',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1996 = Coupling(name = 'GC_1996',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1997 = Coupling(name = 'GC_1997',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1998 = Coupling(name = 'GC_1998',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1999 = Coupling(name = 'GC_1999',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2000 = Coupling(name = 'GC_2000',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a11)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a11)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2001 = Coupling(name = 'GC_2001',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a11)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a11)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a11)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a11)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2002 = Coupling(name = 'GC_2002',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a11*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a11*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM1x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2003 = Coupling(name = 'GC_2003',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a11*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a11*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2004 = Coupling(name = 'GC_2004',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2005 = Coupling(name = 'GC_2005',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2006 = Coupling(name = 'GC_2006',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2007 = Coupling(name = 'GC_2007',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2008 = Coupling(name = 'GC_2008',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2009 = Coupling(name = 'GC_2009',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2010 = Coupling(name = 'GC_2010',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2011 = Coupling(name = 'GC_2011',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2012 = Coupling(name = 'GC_2012',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (CKM1x2*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2013 = Coupling(name = 'GC_2013',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2014 = Coupling(name = 'GC_2014',
                   value = '(Delta1dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (CKM2x2*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2015 = Coupling(name = 'GC_2015',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2016 = Coupling(name = 'GC_2016',
                   value = '(Delta1dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (CKM3x2*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2017 = Coupling(name = 'GC_2017',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2018 = Coupling(name = 'GC_2018',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2019 = Coupling(name = 'GC_2019',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2020 = Coupling(name = 'GC_2020',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2021 = Coupling(name = 'GC_2021',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a21)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a21)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2022 = Coupling(name = 'GC_2022',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a21)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a21)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a21)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a21)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2023 = Coupling(name = 'GC_2023',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a21*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a21*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM1x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2024 = Coupling(name = 'GC_2024',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a21*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a21*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2025 = Coupling(name = 'GC_2025',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2026 = Coupling(name = 'GC_2026',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2027 = Coupling(name = 'GC_2027',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2028 = Coupling(name = 'GC_2028',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2029 = Coupling(name = 'GC_2029',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2030 = Coupling(name = 'GC_2030',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2031 = Coupling(name = 'GC_2031',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2032 = Coupling(name = 'GC_2032',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2033 = Coupling(name = 'GC_2033',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2034 = Coupling(name = 'GC_2034',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2035 = Coupling(name = 'GC_2035',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2036 = Coupling(name = 'GC_2036',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2037 = Coupling(name = 'GC_2037',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2038 = Coupling(name = 'GC_2038',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a11)/LambdaSMEFT**2 + (2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2039 = Coupling(name = 'GC_2039',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a11)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a11)/LambdaSMEFT**2 + (CKM1x3*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su1x1)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su1x1)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2040 = Coupling(name = 'GC_2040',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a21)/LambdaSMEFT**2 + (2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2041 = Coupling(name = 'GC_2041',
                   value = '(Delta1dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a21)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a21)/LambdaSMEFT**2 + (CKM2x3*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2042 = Coupling(name = 'GC_2042',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a31)/LambdaSMEFT**2 + (2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a31)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a31)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2043 = Coupling(name = 'GC_2043',
                   value = '(Delta1dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a31)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a31)/LambdaSMEFT**2 + (CKM3x3*Delta1dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a31)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a31)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a31)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a31)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2044 = Coupling(name = 'GC_2044',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a31*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a31*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM1x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2045 = Coupling(name = 'GC_2045',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a31*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a31*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2046 = Coupling(name = 'GC_2046',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2047 = Coupling(name = 'GC_2047',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2048 = Coupling(name = 'GC_2048',
                   value = '(Delta1dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (CKM1x1*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2049 = Coupling(name = 'GC_2049',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2050 = Coupling(name = 'GC_2050',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (CKM2x1*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2051 = Coupling(name = 'GC_2051',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2052 = Coupling(name = 'GC_2052',
                   value = '(Delta1dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (CKM3x1*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2053 = Coupling(name = 'GC_2053',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2054 = Coupling(name = 'GC_2054',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2055 = Coupling(name = 'GC_2055',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2056 = Coupling(name = 'GC_2056',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2057 = Coupling(name = 'GC_2057',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2058 = Coupling(name = 'GC_2058',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2059 = Coupling(name = 'GC_2059',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2060 = Coupling(name = 'GC_2060',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2061 = Coupling(name = 'GC_2061',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2062 = Coupling(name = 'GC_2062',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2063 = Coupling(name = 'GC_2063',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a12)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a12)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2064 = Coupling(name = 'GC_2064',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a12)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a12)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a12)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a12)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2065 = Coupling(name = 'GC_2065',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a12*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a12*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM2x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2066 = Coupling(name = 'GC_2066',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a12*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a12*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2067 = Coupling(name = 'GC_2067',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2068 = Coupling(name = 'GC_2068',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2069 = Coupling(name = 'GC_2069',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2070 = Coupling(name = 'GC_2070',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2071 = Coupling(name = 'GC_2071',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2072 = Coupling(name = 'GC_2072',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2073 = Coupling(name = 'GC_2073',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2074 = Coupling(name = 'GC_2074',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2075 = Coupling(name = 'GC_2075',
                   value = '(Delta1dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (CKM1x2*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2076 = Coupling(name = 'GC_2076',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2077 = Coupling(name = 'GC_2077',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (CKM2x2*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2078 = Coupling(name = 'GC_2078',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2079 = Coupling(name = 'GC_2079',
                   value = '(Delta1dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (CKM3x2*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2080 = Coupling(name = 'GC_2080',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2081 = Coupling(name = 'GC_2081',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2082 = Coupling(name = 'GC_2082',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2083 = Coupling(name = 'GC_2083',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2084 = Coupling(name = 'GC_2084',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a22)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a22)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2085 = Coupling(name = 'GC_2085',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a22)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a22)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a22)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a22)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2086 = Coupling(name = 'GC_2086',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a22*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a22*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM2x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2087 = Coupling(name = 'GC_2087',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a22*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a22*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2088 = Coupling(name = 'GC_2088',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2089 = Coupling(name = 'GC_2089',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2090 = Coupling(name = 'GC_2090',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2091 = Coupling(name = 'GC_2091',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2092 = Coupling(name = 'GC_2092',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2093 = Coupling(name = 'GC_2093',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2094 = Coupling(name = 'GC_2094',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2095 = Coupling(name = 'GC_2095',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2096 = Coupling(name = 'GC_2096',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2097 = Coupling(name = 'GC_2097',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2098 = Coupling(name = 'GC_2098',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2099 = Coupling(name = 'GC_2099',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2100 = Coupling(name = 'GC_2100',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2101 = Coupling(name = 'GC_2101',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a12)/LambdaSMEFT**2 + (2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2102 = Coupling(name = 'GC_2102',
                   value = '(Delta1dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a12)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a12)/LambdaSMEFT**2 + (CKM1x3*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2103 = Coupling(name = 'GC_2103',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a22)/LambdaSMEFT**2 + (2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2104 = Coupling(name = 'GC_2104',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a22)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a22)/LambdaSMEFT**2 + (CKM2x3*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su2x2)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su2x2)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2105 = Coupling(name = 'GC_2105',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a32)/LambdaSMEFT**2 + (2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a32)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a32)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2106 = Coupling(name = 'GC_2106',
                   value = '(Delta1dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a32)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a32)/LambdaSMEFT**2 + (CKM3x3*Delta1dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a32)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a32)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a32)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a32)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2107 = Coupling(name = 'GC_2107',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a32*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a32*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM2x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2108 = Coupling(name = 'GC_2108',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a32*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a32*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2109 = Coupling(name = 'GC_2109',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2110 = Coupling(name = 'GC_2110',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2111 = Coupling(name = 'GC_2111',
                   value = '(Delta1dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (CKM1x1*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2112 = Coupling(name = 'GC_2112',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2113 = Coupling(name = 'GC_2113',
                   value = '(Delta1dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (CKM2x1*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2114 = Coupling(name = 'GC_2114',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a11)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2115 = Coupling(name = 'GC_2115',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (CKM3x1*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a11)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a11)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd1x1)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd1x1)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2116 = Coupling(name = 'GC_2116',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2117 = Coupling(name = 'GC_2117',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2118 = Coupling(name = 'GC_2118',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2119 = Coupling(name = 'GC_2119',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2120 = Coupling(name = 'GC_2120',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a12)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2121 = Coupling(name = 'GC_2121',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a12)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a12)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2122 = Coupling(name = 'GC_2122',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2123 = Coupling(name = 'GC_2123',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2124 = Coupling(name = 'GC_2124',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2125 = Coupling(name = 'GC_2125',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2126 = Coupling(name = 'GC_2126',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a13)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a13)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a13)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2127 = Coupling(name = 'GC_2127',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a13)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a13)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a13)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a13)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a13)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a13)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2128 = Coupling(name = 'GC_2128',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a13*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a13*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM3x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2129 = Coupling(name = 'GC_2129',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a13*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a13*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2130 = Coupling(name = 'GC_2130',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2131 = Coupling(name = 'GC_2131',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2132 = Coupling(name = 'GC_2132',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2133 = Coupling(name = 'GC_2133',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2134 = Coupling(name = 'GC_2134',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2135 = Coupling(name = 'GC_2135',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a21)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2136 = Coupling(name = 'GC_2136',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a21)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a21)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2137 = Coupling(name = 'GC_2137',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2138 = Coupling(name = 'GC_2138',
                   value = '(Delta1dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (CKM1x2*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2139 = Coupling(name = 'GC_2139',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2140 = Coupling(name = 'GC_2140',
                   value = '(Delta1dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (CKM2x2*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2141 = Coupling(name = 'GC_2141',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a22)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2142 = Coupling(name = 'GC_2142',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (CKM3x2*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a22)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a22)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd2x2)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd2x2)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2143 = Coupling(name = 'GC_2143',
                   value = '(2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2144 = Coupling(name = 'GC_2144',
                   value = '(CKM1x3*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2145 = Coupling(name = 'GC_2145',
                   value = '(2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2146 = Coupling(name = 'GC_2146',
                   value = '(CKM2x3*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2147 = Coupling(name = 'GC_2147',
                   value = '(2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a23)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a23)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a23)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2148 = Coupling(name = 'GC_2148',
                   value = '(CKM3x3*Delta1dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a23)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a23)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a23)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a23)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a23)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a23)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2149 = Coupling(name = 'GC_2149',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a23*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a23*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM3x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2150 = Coupling(name = 'GC_2150',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a23*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a23*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2151 = Coupling(name = 'GC_2151',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2152 = Coupling(name = 'GC_2152',
                   value = '(2*CKM1x1*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x1*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x1*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x1*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM1x1*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2153 = Coupling(name = 'GC_2153',
                   value = '(CKM1x1*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x1*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x1*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x1*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x1*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x1*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM1x1*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x1*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x1*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM1x1*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a11*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2154 = Coupling(name = 'GC_2154',
                   value = '(2*CKM2x1*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x1*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x1*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x1*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM2x1*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2155 = Coupling(name = 'GC_2155',
                   value = '(CKM2x1*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x1*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x1*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x1*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x1*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x1*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM2x1*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x1*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x1*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM2x1*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a12*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2156 = Coupling(name = 'GC_2156',
                   value = '(2*CKM3x1*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x1*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x1*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM3x1*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a31)/LambdaSMEFT**2 + (4*CKM3x1*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2157 = Coupling(name = 'GC_2157',
                   value = '(CKM3x1*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x1*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x1*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x1*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x1*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x1*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM3x1*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x1*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a31)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a31)/LambdaSMEFT**2 + (2*CKM3x1*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM3x1*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a13*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2158 = Coupling(name = 'GC_2158',
                   value = '(2*CKM1x2*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x2*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x2*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x2*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM1x2*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2159 = Coupling(name = 'GC_2159',
                   value = '(CKM1x2*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x2*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x2*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x2*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x2*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x2*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM1x2*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x2*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x2*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM1x2*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a21*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2160 = Coupling(name = 'GC_2160',
                   value = '(2*CKM2x2*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x2*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x2*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x2*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM2x2*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2161 = Coupling(name = 'GC_2161',
                   value = '(CKM2x2*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x2*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x2*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x2*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x2*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x2*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM2x2*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x2*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x2*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM2x2*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a22*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2162 = Coupling(name = 'GC_2162',
                   value = '(2*CKM3x2*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x2*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x2*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM3x2*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a32)/LambdaSMEFT**2 + (4*CKM3x2*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2163 = Coupling(name = 'GC_2163',
                   value = '(CKM3x2*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x2*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x2*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x2*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x2*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x2*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM3x2*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x2*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a32)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a32)/LambdaSMEFT**2 + (2*CKM3x2*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM3x2*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a23*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2164 = Coupling(name = 'GC_2164',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a13)/LambdaSMEFT**2 + (2*CKM1x3*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x3*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM1x3*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x3*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM1x3*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2165 = Coupling(name = 'GC_2165',
                   value = '(Delta1dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a13)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a13)/LambdaSMEFT**2 + (CKM1x3*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x3*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x3*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM1x3*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM1x3*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x3*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM1x3*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM1x3*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM1x3*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM1x3*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a31*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2166 = Coupling(name = 'GC_2166',
                   value = '(2*Delta1dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a23)/LambdaSMEFT**2 + (2*CKM2x3*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x3*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM2x3*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x3*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (4*CKM2x3*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2167 = Coupling(name = 'GC_2167',
                   value = '(Delta1dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a23)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a23)/LambdaSMEFT**2 + (CKM2x3*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x3*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x3*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM2x3*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM2x3*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x3*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM2x3*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM2x3*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM2x3*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM2x3*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a32*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2168 = Coupling(name = 'GC_2168',
                   value = '(4*cqq310*complex(0,1))/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*I50a33)/LambdaSMEFT**2 + (2*CKM3x3*Delta1dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x3*Delta2dcqq3*complex(0,1)*I52a33)/LambdaSMEFT**2 + (2*CKM3x3*Delta1ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*CKM3x3*Delta2ucqq3*complex(0,1)*I53a33)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*I6a33)/LambdaSMEFT**2 + (2*Delta1dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta2dcqq31*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (2*Delta1ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*Delta2ucqq31*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (4*CKM3x3*cqq30*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2dcqq3*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta1ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (2*Delta2ucqq3*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2169 = Coupling(name = 'GC_2169',
                   value = '(2*cqq10*complex(0,1))/LambdaSMEFT**2 - (2*cqq30*complex(0,1))/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*I50a33)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*I50a33)/LambdaSMEFT**2 + (CKM3x3*Delta1dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x3*Delta1dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x3*Delta2dcqq11*complex(0,1)*I52a33)/LambdaSMEFT**2 - (CKM3x3*Delta2dcqq31*complex(0,1)*I52a33)/LambdaSMEFT**2 + (CKM3x3*Delta1ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x3*Delta1ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (CKM3x3*Delta2ucqq11*complex(0,1)*I53a33)/LambdaSMEFT**2 - (CKM3x3*Delta2ucqq31*complex(0,1)*I53a33)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*I6a33)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*I6a33)/LambdaSMEFT**2 + (Delta1dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta1dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta2dcqq1*complex(0,1)*Sd3x3)/LambdaSMEFT**2 - (Delta2dcqq3*complex(0,1)*Sd3x3)/LambdaSMEFT**2 + (Delta1ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta1ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (Delta2ucqq1*complex(0,1)*Su3x3)/LambdaSMEFT**2 - (Delta2ucqq3*complex(0,1)*Su3x3)/LambdaSMEFT**2 + (2*CKM3x3*cqq110*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (2*CKM3x3*cqq310*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2dcqq11*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2dcqq31*complex(0,1)*I51a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta1ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta1ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 + (Delta2ucqq11*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2 - (Delta2ucqq31*complex(0,1)*I54a33*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2170 = Coupling(name = 'GC_2170',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a33*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth)) - (DeltaucHq3*ee*complex(0,1)*I65a33*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth) - (cHq30*ee*complex(0,1)*vevhat*complexconjugate(CKM3x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2171 = Coupling(name = 'GC_2171',
                   value = '-((DeltadcHq3*ee*complex(0,1)*I64a33*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (DeltaucHq3*ee*complex(0,1)*I65a33*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)) - (cHq30*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

