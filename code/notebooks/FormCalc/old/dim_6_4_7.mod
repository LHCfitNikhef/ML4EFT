(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)
(*                                                                             *)
(*         This file has been automatically generated by FeynRules.            *)
(*                                                                             *)
(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)


FR$ModelInformation={
  ModelName->"SMEFTsim",
  Authors -> {"I. Brivio"},
  Version -> "3.0.1",
  Date -> "January 2021",
  Institutions -> {"ITP, Universita"t Heidelberg"},
  Emails -> {"brivio@thphys.uni-heidelberg.de"},
  References -> {"arXiv:1709.06492", "arXiv:2012.11343"},
  URLs -> {"https://feynrules.irmp.ucl.ac.be/wiki/SMEFT", "https://SMEFTsim.github.io"}};

FR$ClassesTranslation={};

FR$InteractionOrderPerturbativeExpansion={{QCD, 0}, {QED, 0}, {SMHLOOP, 0}, {NP, 0}, {NPshifts, 0}, {NPprop, 0}, {NPcpv, 0}, {NPcdB, 0}, {NPcdd, 0}, {NPcdd1, 0}, {NPcdG, 0}, {NPcdH, 0}, {NPcdW, 0}, {NPceB, 0}, {NPced, 0}, {NPcee, 0}, {NPceH, 0}, {NPceu, 0}, {NPceW, 0}, {NPcG, 0}, {NPcGtil, 0}, {NPcH, 0}, {NPcHB, 0}, {NPcHbox, 0}, {NPcHBtil, 0}, {NPcHd, 0}, {NPcHDD, 0}, {NPcHe, 0}, {NPcHG, 0}, {NPcHGtil, 0}, {NPcHl1, 0}, {NPcHl3, 0}, {NPcHq1, 0}, {NPcHq3, 0}, {NPcHu, 0}, {NPcHud, 0}, {NPcHW, 0}, {NPcHWB, 0}, {NPcHWBtil, 0}, {NPcHWtil, 0}, {NPcld, 0}, {NPcle, 0}, {NPcledq, 0}, {NPclequ1, 0}, {NPclequ3, 0}, {NPcll, 0}, {NPcll1, 0}, {NPclq1, 0}, {NPclq3, 0}, {NPclu, 0}, {NPcqd1, 0}, {NPcqd8, 0}, {NPcqe, 0}, {NPcqq1, 0}, {NPcqq11, 0}, {NPcqq3, 0}, {NPcqq31, 0}, {NPcqu1, 0}, {NPcqu8, 0}, {NPcquqd1, 0}, {NPcquqd11, 0}, {NPcquqd8, 0}, {NPcquqd81, 0}, {NPcuB, 0}, {NPcud1, 0}, {NPcud8, 0}, {NPcuG, 0}, {NPcuH, 0}, {NPcuu, 0}, {NPcuu1, 0}, {NPcuW, 0}, {NPcW, 0}, {NPcWtil, 0}};

FR$GoldstoneList={S[2], S[3]};

(*     Declared indices    *)

IndexRange[ Index[Gluon] ] = NoUnfold[ Range[ 8 ] ]

IndexRange[ Index[SU2W] ] = Range[ 3 ]

IndexRange[ Index[Generation] ] = Range[ 3 ]

IndexRange[ Index[Colour] ] = NoUnfold[ Range[ 3 ] ]

IndexRange[ Index[SU2D] ] = Range[ 2 ]

(*     Declared particles    *)

M$ClassesDescription = {
V[1] == {
    SelfConjugate -> True,
    PropagatorLabel -> "a",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> 0,
    Indices -> {} },

V[2] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Z",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {} },

V[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorLabel -> "W",
    PropagatorType -> Sine,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

V[4] == {
    SelfConjugate -> True,
    Indices -> {Index[Gluon]},
    PropagatorLabel -> "G",
    PropagatorType -> Cycles,
    PropagatorArrow -> None,
    Mass -> 0 },

U[1] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uA",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {} },

U[2] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uZ",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MZ,
    Indices -> {} },

U[31] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, Q},
    PropagatorLabel -> "uWp",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

U[32] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, -Q},
    PropagatorLabel -> "uWm",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

U[4] == {
    SelfConjugate -> False,
    Indices -> {Index[Gluon]},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uG",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0 },

V[13] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Superscript[Z,,]",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZ1,
    Indices -> {} },

V[14] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorLabel -> "Superscript[W,,]",
    PropagatorType -> Sine,
    PropagatorArrow -> Forward,
    Mass -> MW1,
    Indices -> {} },

F[1] == {
    Indices -> {Index[Generation]},
    SelfConjugate -> False,
    QuantumNumbers -> {LeptonNumber},
    PropagatorLabel -> "v",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0 },

F[2] == {
    Indices -> {Index[Generation]},
    SelfConjugate -> False,
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorLabel -> "l",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Ml },

F[3] == {
    Indices -> {Index[Generation], Index[Colour]},
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorLabel -> "uq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Mu },

F[4] == {
    Indices -> {Index[Generation], Index[Colour]},
    SelfConjugate -> False,
    QuantumNumbers -> {-Q/3},
    PropagatorLabel -> "dq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Md },

F[31] == {
    Indices -> {Index[Colour]},
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorLabel -> "Superscript[t,,]",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MT1 },

S[1] == {
    SelfConjugate -> True,
    PropagatorLabel -> "H",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MH,
    Indices -> {} },

S[2] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Go",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {} },

S[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorLabel -> "GP",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MW,
    Indices -> {} },

S[4] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Superscript[H,,]",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MH1,
    Indices -> {} }
}


(*        Definitions       *)

GaugeXi[ V[1] ] = GaugeXi[A];
GaugeXi[ V[2] ] = GaugeXi[Z];
GaugeXi[ V[3] ] = GaugeXi[W];
GaugeXi[ V[4] ] = GaugeXi[G];
GaugeXi[ U[1] ] = GaugeXi[A];
GaugeXi[ U[2] ] = GaugeXi[Z];
GaugeXi[ U[31] ] = GaugeXi[W];
GaugeXi[ U[32] ] = GaugeXi[W];
GaugeXi[ U[4] ] = GaugeXi[G];
GaugeXi[ S[1] ] = 1;
GaugeXi[ S[2] ] = GaugeXi[Z];
GaugeXi[ S[3] ] = GaugeXi[W];

MZ[ ___ ] := MZ;
MW[ ___ ] := MW;
MZ1[ ___ ] := MZ1;
MW1[ ___ ] := MW1;
Ml[ 1 ] := Me;
Ml[ 2 ] := MMU;
Ml[ 3 ] := MTA;
Mu[ 1, _ ] := MU;
Mu[ 1 ] := MU;
Mu[ 2, _ ] := MC;
Mu[ 2 ] := MC;
Mu[ 3, _ ] := MT;
Mu[ 3 ] := MT;
Md[ 1, _ ] := MD;
Md[ 1 ] := MD;
Md[ 2, _ ] := MS;
Md[ 2 ] := MS;
Md[ 3, _ ] := MB;
Md[ 3 ] := MB;
MT1[ ___ ] := MT1;
MH[ ___ ] := MH;
MH1[ ___ ] := MH1;


TheLabel[ V[4, {__}] ] := TheLabel[V[4]];
TheLabel[ U[4, {__}] ] := TheLabel[U[4]];
TheLabel[ F[1, {1}] ] := "ve";
TheLabel[ F[1, {2}] ] := "vm";
TheLabel[ F[1, {3}] ] := "vt";
TheLabel[ F[2, {1}] ] := "e";
TheLabel[ F[2, {2}] ] := "mu";
TheLabel[ F[2, {3}] ] := "ta";
TheLabel[ F[3, {1, _}] ] := "u";
TheLabel[ F[3, {1}] ] := "u";
TheLabel[ F[3, {2, _}] ] := "c";
TheLabel[ F[3, {2}] ] := "c";
TheLabel[ F[3, {3, _}] ] := "t";
TheLabel[ F[3, {3}] ] := "t";
TheLabel[ F[4, {1, _}] ] := "d";
TheLabel[ F[4, {1}] ] := "d";
TheLabel[ F[4, {2, _}] ] := "s";
TheLabel[ F[4, {2}] ] := "s";
TheLabel[ F[4, {3, _}] ] := "b";
TheLabel[ F[4, {3}] ] := "b";
TheLabel[ F[31, {__}] ] := TheLabel[F[31]];


(*      Couplings (calculated by FeynRules)      *)

M$CouplingMatrices = {

C[ S[1] , S[1] , S[1] , S[1] ] == {{((6*I)*lam*(-1 + sth^2))/cth^2, 0}},

C[ S[1] , S[1] , S[1] ] == {{((6*I)*lam*(-1 + sth^2)*vevhat)/cth^2, 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] ] == {{-(gc3*SUNF[e1x2, e2x2, e3x2]), 0}, {gc3*SUNF[e1x2, e2x2, e3x2], 0}, {gc3*SUNF[e1x2, e2x2, e3x2], 0}, {-(gc3*SUNF[e1x2, e2x2, e3x2]), 0}, {-(gc3*SUNF[e1x2, e2x2, e3x2]), 0}, {gc3*SUNF[e1x2, e2x2, e3x2], 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] ] == {{(-I)*gc4*(SUNF[e1x2, e2x2, e3x2, e4x2] + SUNF[e1x2, e3x2, e2x2, e4x2]), 0}, {I*gc4*(SUNF[e1x2, e2x2, e3x2, e4x2] - SUNF[e1x2, e4x2, e2x2, e3x2]), 0}, {I*gc4*(SUNF[e1x2, e3x2, e2x2, e4x2] + SUNF[e1x2, e4x2, e2x2, e3x2]), 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[1] ] == {{I*gc5*IndexDelta[e1x2, e2x2], 0}, {I*gc5*IndexDelta[e1x2, e2x2], 0}},

C[ V[1] , V[3] , -V[3] ] == {{(-I)*gc6*(LambdaSMEFT^2*sth + (cHWB*cth - 2*cHW*sth)*vevhat^2), 0}, {I*gc6*sth*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {I*gc6*(LambdaSMEFT^2*sth + (cHWB*cth - 2*cHW*sth)*vevhat^2), 0}, {(-I)*gc6*sth*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {(-I)*gc6*sth*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {I*gc6*sth*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}},

C[ S[1] , S[1] , V[3] , -V[3] ] == {{(-8*I)*cHW*gc7*sth^2, 0}, {(I*EL^2*gc7*LambdaSMEFT^2*(-1 + sth^2))/cth^2, 0}, {(8*I)*cHW*gc7*sth^2, 0}},

C[ S[1] , V[3] , -V[3] ] == {{(-8*I)*cHW*gc8*sth^2, 0}, {(I*EL^2*gc8*LambdaSMEFT^2*(-1 + sth^2))/cth^2, 0}, {(8*I)*cHW*gc8*sth^2, 0}},

C[ V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc9, 0}, {(-I)*gc9, 0}, {(2*I)*gc9, 0}},

C[ V[3] , -V[3] , V[2] ] == {{I*cth*gc10*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {(-I)*cth*gc10*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {(-I)*cth*gc10*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {I*gc10*(-(cHWB*sth*vevhat^2) + cth*(LambdaSMEFT^2 - 2*cHW*vevhat^2)), 0}, {I*cth*gc10*(LambdaSMEFT^2 - 2*cHW*vevhat^2), 0}, {I*gc10*(-(cth*LambdaSMEFT^2) + 2*cHW*cth*vevhat^2 + cHWB*sth*vevhat^2), 0}},

C[ V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc11, 0}, {(-I)*gc11, 0}, {(2*I)*gc11, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] ] == {{I*gc12L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc12R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[1] ] == {{I*gc13L[e1x2, e2x2], 0}, {I*gc13R[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] ] == {{I*gc14L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc14R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc15, 0}, {I*gc15, 0}, {I*gc15, 0}},

C[ S[1] , S[1] , V[2] , V[2] ] == {{(-8*I)*cth^2*gc16*sth^2*(cHW*cth^2 + sth*(cHWB*cth + cHB*sth)), 0}, {(-I)*EL^2*gc16*LambdaSMEFT^2, 0}, {(8*I)*cth^2*gc16*sth^2*(cHW*cth^2 + sth*(cHWB*cth + cHB*sth)), 0}},

C[ S[1] , V[2] , V[2] ] == {{(-8*I)*cth^2*gc17*sth^2*(cHW*cth^2 + sth*(cHWB*cth + cHB*sth)), 0}, {(-I)*EL^2*gc17*LambdaSMEFT^2, 0}, {(8*I)*cth^2*gc17*sth^2*(cHW*cth^2 + sth*(cHWB*cth + cHB*sth)), 0}},

C[ V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc18, 0}, {(-I)*gc18, 0}, {(2*I)*gc18, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[1] ] == {{I*gc19*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc19*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[1] ] == {{I*gc20*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc20*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc21*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc21*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc22*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc22*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[3] ] == {{I*gc23[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[1, {e1x2}] , F[2, {e2x2}] , V[3] ] == {{I*gc24*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , -V[3] ] == {{I*gc25[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[2, {e1x2}] , F[1, {e2x2}] , -V[3] ] == {{I*gc26*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[2] ] == {{I*gc27L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc27R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[2] ] == {{I*gc28L*IndexDelta[e1x2, e2x2], 0}, {I*gc28R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[2] ] == {{I*gc29L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc29R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[1, {e1x2}] , F[1, {e2x2}] , V[2] ] == {{I*gc30*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ S[1] , S[1] , V[1] , V[1] ] == {{(-I)*gc31, 0}, {0, 0}, {I*gc31, 0}},

C[ S[1] , V[1] , V[1] ] == {{(-I)*gc32, 0}, {0, 0}, {I*gc32, 0}},

C[ S[1] , S[1] , V[1] , V[2] ] == {{(-I)*gc33, 0}, {0, 0}, {I*gc33, 0}},

C[ S[1] , V[1] , V[2] ] == {{(-I)*gc34, 0}, {0, 0}, {I*gc34, 0}},

C[ S[1] , S[1] , V[1] , V[3] , -V[3] ] == {{I*gc35*(cHWB*cth - 2*cHW*sth), 0}, {(2*I)*cHW*gc35*sth, 0}, {(-I)*gc35*(cHWB*cth - 2*cHW*sth), 0}, {(-2*I)*cHW*gc35*sth, 0}, {(-2*I)*cHW*gc35*sth, 0}, {(2*I)*cHW*gc35*sth, 0}},

C[ S[1] , V[1] , V[3] , -V[3] ] == {{I*gc36*(cHWB*cth - 2*cHW*sth), 0}, {(2*I)*cHW*gc36*sth, 0}, {(-I)*gc36*(cHWB*cth - 2*cHW*sth), 0}, {(-2*I)*cHW*gc36*sth, 0}, {(-2*I)*cHW*gc36*sth, 0}, {(2*I)*cHW*gc36*sth, 0}},

C[ S[1] , S[1] , V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc37, 0}, {(-I)*gc37, 0}, {(2*I)*gc37, 0}},

C[ S[1] , V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc38, 0}, {(-I)*gc38, 0}, {(2*I)*gc38, 0}},

C[ S[1] , S[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*cHW*cth*gc39, 0}, {(2*I)*cHW*cth*gc39, 0}, {(2*I)*cHW*cth*gc39, 0}, {(-I)*gc39*(2*cHW*cth + cHWB*sth), 0}, {(-2*I)*cHW*cth*gc39, 0}, {I*gc39*(2*cHW*cth + cHWB*sth), 0}},

C[ S[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*cHW*cth*gc40, 0}, {(2*I)*cHW*cth*gc40, 0}, {(2*I)*cHW*cth*gc40, 0}, {(-I)*gc40*(2*cHW*cth + cHWB*sth), 0}, {(-2*I)*cHW*cth*gc40, 0}, {I*gc40*(2*cHW*cth + cHWB*sth), 0}},

C[ S[1] , S[1] , V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc41, 0}, {(-I)*gc41, 0}, {(2*I)*gc41, 0}},

C[ S[1] , V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc42, 0}, {(-I)*gc42, 0}, {(2*I)*gc42, 0}},

C[ S[1] , S[1] , V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc43, 0}, {I*gc43, 0}, {I*gc43, 0}},

C[ S[1] , V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc44, 0}, {I*gc44, 0}, {I*gc44, 0}},

C[ S[1] , S[1] , V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc45, 0}, {(-I)*gc45, 0}, {(2*I)*gc45, 0}},

C[ S[1] , V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc46, 0}, {(-I)*gc46, 0}, {(2*I)*gc46, 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] , S[1] , V[3] ] == {{I*gc47[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] , V[3] ] == {{I*gc48[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] , S[1] , -V[3] ] == {{I*gc49[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] , -V[3] ] == {{I*gc50[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] , S[1] , V[2] ] == {{I*gc51*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] , V[2] ] == {{I*gc52*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] , S[1] , V[2] ] == {{I*gc53*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] , V[2] ] == {{I*gc54*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}}

}

(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)

(* Parameter replacement lists (These lists were created by FeynRules) *)

(* FA Couplings *)

M$FACouplings = {
     gc3 -> GS,
     gc4 -> -GS^2,
     gc5 -> EL,
     gc6 -> -(EL/(LambdaSMEFT^2*sth)),
     gc7 -> -1/(2*LambdaSMEFT^2*sth^2),
     gc8 -> -vevhat/(2*LambdaSMEFT^2*sth^2),
     gc9 -> EL^2*(-1 + (2*cHW*vevhat^2)/LambdaSMEFT^2),
     gc10 -> EL/(LambdaSMEFT^2*sth),
     gc11 -> (EL^2*(LambdaSMEFT^2 - 2*cHW*vevhat^2))/(LambdaSMEFT^2*sth^2),
     gc12L[e1x2_, e2x2_] -> -(yd[e1x2, e2x2]/Sqrt[2]),
     gc12R[e1x2_, e2x2_] -> -(yd[e2x2, e1x2]/Sqrt[2]),
     gc13L[e1x2_, e2x2_] -> -(yl[e1x2, e2x2]/Sqrt[2]),
     gc13R[e1x2_, e2x2_] -> -(yl[e2x2, e1x2]/Sqrt[2]),
     gc14L[e1x2_, e2x2_] -> -(yu[e1x2, e2x2]/Sqrt[2]),
     gc14R[e1x2_, e2x2_] -> -(yu[e2x2, e1x2]/Sqrt[2]),
     gc15 -> (cth*EL^2*(LambdaSMEFT^2 - 2*cHW*vevhat^2))/(LambdaSMEFT^2*sth),
     gc16 -> -1/(2*cth^2*LambdaSMEFT^2*sth^2),
     gc17 -> -vevhat/(2*cth^2*LambdaSMEFT^2*sth^2),
     gc18 -> (EL^2*(-1 + sth^2)*(LambdaSMEFT^2 - 2*cHW*vevhat^2))/(LambdaSMEFT^2*sth^2),
     gc19 -> EL/3,
     gc20 -> (-2*EL)/3,
     gc21 -> -GS,
     gc22 -> -GS,
     gc23[e1x2_, e2x2_] -> -((EL*(LambdaSMEFT^2 + cHq3*vevhat^2)*CKM[e1x2, e2x2])/(Sqrt[2]*LambdaSMEFT^2*sth)),
     gc24 -> -(EL/(Sqrt[2]*sth)),
     gc25[e1x2_, e2x2_] -> -((EL*(LambdaSMEFT^2 + cHq3*vevhat^2)*Conjugate[CKM[e2x2, e1x2]])/(Sqrt[2]*LambdaSMEFT^2*sth)),
     gc26 -> -(EL/(Sqrt[2]*sth)),
     gc27L -> -(EL*(LambdaSMEFT^2*(-3 + 2*sth^2) - 3*cHq3*vevhat^2))/(6*cth*LambdaSMEFT^2*sth),
     gc27R -> -(EL*sth)/(3*cth),
     gc28L -> -(EL*(-1 + 2*sth^2))/(2*cth*sth),
     gc28R -> -((EL*sth)/cth),
     gc29L -> (EL*(LambdaSMEFT^2*(-3 + 4*sth^2) - 3*cHq3*vevhat^2))/(6*cth*LambdaSMEFT^2*sth),
     gc29R -> (2*EL*sth)/(3*cth),
     gc30 -> -EL/(2*cth*sth),
     gc31 -> (-4*(cHB*cth^2 + sth*(-(cHWB*cth) + cHW*sth)))/LambdaSMEFT^2,
     gc32 -> (-4*(cHB*cth^2 + sth*(-(cHWB*cth) + cHW*sth))*vevhat)/LambdaSMEFT^2,
     gc33 -> (2*(cHWB + 2*(cHB - cHW)*cth*sth - 2*cHWB*sth^2))/LambdaSMEFT^2,
     gc34 -> (2*(cHWB + 2*(cHB - cHW)*cth*sth - 2*cHWB*sth^2)*vevhat)/LambdaSMEFT^2,
     gc35 -> (2*EL)/(LambdaSMEFT^2*sth),
     gc36 -> (2*EL*vevhat)/(LambdaSMEFT^2*sth),
     gc37 -> (4*cHW*EL^2)/LambdaSMEFT^2,
     gc38 -> (4*cHW*EL^2*vevhat)/LambdaSMEFT^2,
     gc39 -> (2*EL)/(LambdaSMEFT^2*sth),
     gc40 -> (2*EL*vevhat)/(LambdaSMEFT^2*sth),
     gc41 -> (-4*cHW*EL^2)/(LambdaSMEFT^2*sth^2),
     gc42 -> (-4*cHW*EL^2*vevhat)/(LambdaSMEFT^2*sth^2),
     gc43 -> (-4*cHW*cth*EL^2)/(LambdaSMEFT^2*sth),
     gc44 -> (-4*cHW*cth*EL^2*vevhat)/(LambdaSMEFT^2*sth),
     gc45 -> (4*cHW*cth^2*EL^2)/(LambdaSMEFT^2*sth^2),
     gc46 -> (4*cHW*cth^2*EL^2*vevhat)/(LambdaSMEFT^2*sth^2),
     gc47[e1x2_, e2x2_] -> -((Sqrt[2]*cHq3*EL*CKM[e1x2, e2x2])/(LambdaSMEFT^2*sth)),
     gc48[e1x2_, e2x2_] -> -((Sqrt[2]*cHq3*EL*vevhat*CKM[e1x2, e2x2])/(LambdaSMEFT^2*sth)),
     gc49[e1x2_, e2x2_] -> -((Sqrt[2]*cHq3*EL*Conjugate[CKM[e2x2, e1x2]])/(LambdaSMEFT^2*sth)),
     gc50[e1x2_, e2x2_] -> -((Sqrt[2]*cHq3*EL*vevhat*Conjugate[CKM[e2x2, e1x2]])/(LambdaSMEFT^2*sth)),
     gc51 -> (cHq3*EL)/(cth*LambdaSMEFT^2*sth),
     gc52 -> (cHq3*EL*vevhat)/(cth*LambdaSMEFT^2*sth),
     gc53 -> -((cHq3*EL)/(cth*LambdaSMEFT^2*sth)),
     gc54 -> -((cHq3*EL*vevhat)/(cth*LambdaSMEFT^2*sth))};

