function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x579ae]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x461ae: v461ae(0x579ae) = CONST 
    0x461ce: JUMPI v461ae(0x579ae), v8

    Begin block 0xd
    prev=[0x0], succ=[0x583ae, 0x3a]
    =================================
    0xd: vd(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2b: v2b(0x0) = CONST 
    0x2d: v2d = CALLDATALOAD v2b(0x0)
    0x2e: v2e = DIV v2d, vd(0x100000000000000000000000000000000000000000000000000000000)
    0x2f: v2f(0x6fdde03) = CONST 
    0x35: v35 = EQ v2e, v2f(0x6fdde03)
    0x46bae: v46bae(0x583ae) = CONST 
    0x46bce: JUMPI v46bae(0x583ae), v35

    Begin block 0x583ae
    prev=[0xd], succ=[]
    =================================
    0x583ce: v583ce(0x15d) = CONST 
    0x583ee: CALLPRIVATE v583ce(0x15d)

    Begin block 0x3a
    prev=[0xd], succ=[0x58dae, 0x45]
    =================================
    0x3b: v3b(0x95ea7b3) = CONST 
    0x40: v40 = EQ v3b(0x95ea7b3), v2e
    0x475ae: v475ae(0x58dae) = CONST 
    0x475ce: JUMPI v475ae(0x58dae), v40

    Begin block 0x58dae
    prev=[0x3a], succ=[]
    =================================
    0x58dce: v58dce(0x1e7) = CONST 
    0x58dee: CALLPRIVATE v58dce(0x1e7)

    Begin block 0x45
    prev=[0x3a], succ=[0x597ae, 0x50]
    =================================
    0x46: v46(0x18160ddd) = CONST 
    0x4b: v4b = EQ v46(0x18160ddd), v2e
    0x47fae: v47fae(0x597ae) = CONST 
    0x47fce: JUMPI v47fae(0x597ae), v4b

    Begin block 0x597ae
    prev=[0x45], succ=[]
    =================================
    0x597ce: v597ce(0x234) = CONST 
    0x597ee: CALLPRIVATE v597ce(0x234)

    Begin block 0x50
    prev=[0x45], succ=[0x5a1ae, 0x5b]
    =================================
    0x51: v51(0x23b872dd) = CONST 
    0x56: v56 = EQ v51(0x23b872dd), v2e
    0x489ae: v489ae(0x5a1ae) = CONST 
    0x489ce: JUMPI v489ae(0x5a1ae), v56

    Begin block 0x5a1ae
    prev=[0x50], succ=[]
    =================================
    0x5a1ce: v5a1ce(0x25b) = CONST 
    0x5a1ee: CALLPRIVATE v5a1ce(0x25b)

    Begin block 0x5b
    prev=[0x50], succ=[0x5abae, 0x66]
    =================================
    0x5c: v5c(0x2baabddf) = CONST 
    0x61: v61 = EQ v5c(0x2baabddf), v2e
    0x493ae: v493ae(0x5abae) = CONST 
    0x493ce: JUMPI v493ae(0x5abae), v61

    Begin block 0x5abae
    prev=[0x5b], succ=[]
    =================================
    0x5abce: v5abce(0x29e) = CONST 
    0x5abee: CALLPRIVATE v5abce(0x29e)

    Begin block 0x66
    prev=[0x5b], succ=[0x5b5ae, 0x71]
    =================================
    0x67: v67(0x2c4e722e) = CONST 
    0x6c: v6c = EQ v67(0x2c4e722e), v2e
    0x49dae: v49dae(0x5b5ae) = CONST 
    0x49dce: JUMPI v49dae(0x5b5ae), v6c

    Begin block 0x5b5ae
    prev=[0x66], succ=[]
    =================================
    0x5b5ce: v5b5ce(0x2a8) = CONST 
    0x5b5ee: CALLPRIVATE v5b5ce(0x2a8)

    Begin block 0x71
    prev=[0x66], succ=[0x5bfae, 0x7c]
    =================================
    0x72: v72(0x2e1a7d4d) = CONST 
    0x77: v77 = EQ v72(0x2e1a7d4d), v2e
    0x4a7ae: v4a7ae(0x5bfae) = CONST 
    0x4a7ce: JUMPI v4a7ae(0x5bfae), v77

    Begin block 0x5bfae
    prev=[0x71], succ=[]
    =================================
    0x5bfce: v5bfce(0x2bd) = CONST 
    0x5bfee: CALLPRIVATE v5bfce(0x2bd)

    Begin block 0x7c
    prev=[0x71], succ=[0x5c9ae, 0x87]
    =================================
    0x7d: v7d(0x313ce567) = CONST 
    0x82: v82 = EQ v7d(0x313ce567), v2e
    0x4b1ae: v4b1ae(0x5c9ae) = CONST 
    0x4b1ce: JUMPI v4b1ae(0x5c9ae), v82

    Begin block 0x5c9ae
    prev=[0x7c], succ=[]
    =================================
    0x5c9ce: v5c9ce(0x2e7) = CONST 
    0x5c9ee: CALLPRIVATE v5c9ce(0x2e7)

    Begin block 0x87
    prev=[0x7c], succ=[0x5d3ae, 0x92]
    =================================
    0x88: v88(0x365a5306) = CONST 
    0x8d: v8d = EQ v88(0x365a5306), v2e
    0x4bbae: v4bbae(0x5d3ae) = CONST 
    0x4bbce: JUMPI v4bbae(0x5d3ae), v8d

    Begin block 0x5d3ae
    prev=[0x87], succ=[]
    =================================
    0x5d3ce: v5d3ce(0x312) = CONST 
    0x5d3ee: CALLPRIVATE v5d3ce(0x312)

    Begin block 0x92
    prev=[0x87], succ=[0x5ddae, 0x9d]
    =================================
    0x93: v93(0x39509351) = CONST 
    0x98: v98 = EQ v93(0x39509351), v2e
    0x4c5ae: v4c5ae(0x5ddae) = CONST 
    0x4c5ce: JUMPI v4c5ae(0x5ddae), v98

    Begin block 0x5ddae
    prev=[0x92], succ=[]
    =================================
    0x5ddce: v5ddce(0x33c) = CONST 
    0x5ddee: CALLPRIVATE v5ddce(0x33c)

    Begin block 0x9d
    prev=[0x92], succ=[0x5e7ae, 0xa8]
    =================================
    0x9e: v9e(0x5216aeec) = CONST 
    0xa3: va3 = EQ v9e(0x5216aeec), v2e
    0x4cfae: v4cfae(0x5e7ae) = CONST 
    0x4cfce: JUMPI v4cfae(0x5e7ae), va3

    Begin block 0x5e7ae
    prev=[0x9d], succ=[]
    =================================
    0x5e7ce: v5e7ce(0x375) = CONST 
    0x5e7ee: CALLPRIVATE v5e7ce(0x375)

    Begin block 0xa8
    prev=[0x9d], succ=[0x5f1ae, 0xb3]
    =================================
    0xa9: va9(0x70a08231) = CONST 
    0xae: vae = EQ va9(0x70a08231), v2e
    0x4d9ae: v4d9ae(0x5f1ae) = CONST 
    0x4d9ce: JUMPI v4d9ae(0x5f1ae), vae

    Begin block 0x5f1ae
    prev=[0xa8], succ=[]
    =================================
    0x5f1ce: v5f1ce(0x38a) = CONST 
    0x5f1ee: CALLPRIVATE v5f1ce(0x38a)

    Begin block 0xb3
    prev=[0xa8], succ=[0x5fbae, 0xbe]
    =================================
    0xb4: vb4(0x715018a6) = CONST 
    0xb9: vb9 = EQ vb4(0x715018a6), v2e
    0x4e3ae: v4e3ae(0x5fbae) = CONST 
    0x4e3ce: JUMPI v4e3ae(0x5fbae), vb9

    Begin block 0x5fbae
    prev=[0xb3], succ=[]
    =================================
    0x5fbce: v5fbce(0x3bd) = CONST 
    0x5fbee: CALLPRIVATE v5fbce(0x3bd)

    Begin block 0xbe
    prev=[0xb3], succ=[0x605ae, 0xc9]
    =================================
    0xbf: vbf(0x7ab503db) = CONST 
    0xc4: vc4 = EQ vbf(0x7ab503db), v2e
    0x4edae: v4edae(0x605ae) = CONST 
    0x4edce: JUMPI v4edae(0x605ae), vc4

    Begin block 0x605ae
    prev=[0xbe], succ=[]
    =================================
    0x605ce: v605ce(0x3d2) = CONST 
    0x605ee: CALLPRIVATE v605ce(0x3d2)

    Begin block 0xc9
    prev=[0xbe], succ=[0x60fae, 0xd4]
    =================================
    0xca: vca(0x7f084848) = CONST 
    0xcf: vcf = EQ vca(0x7f084848), v2e
    0x4f7ae: v4f7ae(0x60fae) = CONST 
    0x4f7ce: JUMPI v4f7ae(0x60fae), vcf

    Begin block 0x60fae
    prev=[0xc9], succ=[]
    =================================
    0x60fce: v60fce(0x403) = CONST 
    0x60fee: CALLPRIVATE v60fce(0x403)

    Begin block 0xd4
    prev=[0xc9], succ=[0x619ae, 0xdf]
    =================================
    0xd5: vd5(0x8ac2c680) = CONST 
    0xda: vda = EQ vd5(0x8ac2c680), v2e
    0x501ae: v501ae(0x619ae) = CONST 
    0x501ce: JUMPI v501ae(0x619ae), vda

    Begin block 0x619ae
    prev=[0xd4], succ=[]
    =================================
    0x619ce: v619ce(0x418) = CONST 
    0x619ee: CALLPRIVATE v619ce(0x418)

    Begin block 0xdf
    prev=[0xd4], succ=[0x623ae, 0xea]
    =================================
    0xe0: ve0(0x8c5a2083) = CONST 
    0xe5: ve5 = EQ ve0(0x8c5a2083), v2e
    0x50bae: v50bae(0x623ae) = CONST 
    0x50bce: JUMPI v50bae(0x623ae), ve5

    Begin block 0x623ae
    prev=[0xdf], succ=[]
    =================================
    0x623ce: v623ce(0x42d) = CONST 
    0x623ee: CALLPRIVATE v623ce(0x42d)

    Begin block 0xea
    prev=[0xdf], succ=[0x62dae, 0xf5]
    =================================
    0xeb: veb(0x8da5cb5b) = CONST 
    0xf0: vf0 = EQ veb(0x8da5cb5b), v2e
    0x515ae: v515ae(0x62dae) = CONST 
    0x515ce: JUMPI v515ae(0x62dae), vf0

    Begin block 0x62dae
    prev=[0xea], succ=[]
    =================================
    0x62dce: v62dce(0x442) = CONST 
    0x62dee: CALLPRIVATE v62dce(0x442)

    Begin block 0xf5
    prev=[0xea], succ=[0x637ae, 0x100]
    =================================
    0xf6: vf6(0x8f32d59b) = CONST 
    0xfb: vfb = EQ vf6(0x8f32d59b), v2e
    0x51fae: v51fae(0x637ae) = CONST 
    0x51fce: JUMPI v51fae(0x637ae), vfb

    Begin block 0x637ae
    prev=[0xf5], succ=[]
    =================================
    0x637ce: v637ce(0x457) = CONST 
    0x637ee: CALLPRIVATE v637ce(0x457)

    Begin block 0x100
    prev=[0xf5], succ=[0x641ae, 0x10b]
    =================================
    0x101: v101(0x95d89b41) = CONST 
    0x106: v106 = EQ v101(0x95d89b41), v2e
    0x529ae: v529ae(0x641ae) = CONST 
    0x529ce: JUMPI v529ae(0x641ae), v106

    Begin block 0x641ae
    prev=[0x100], succ=[]
    =================================
    0x641ce: v641ce(0x46c) = CONST 
    0x641ee: CALLPRIVATE v641ce(0x46c)

    Begin block 0x10b
    prev=[0x100], succ=[0x64bae, 0x116]
    =================================
    0x10c: v10c(0xa457c2d7) = CONST 
    0x111: v111 = EQ v10c(0xa457c2d7), v2e
    0x533ae: v533ae(0x64bae) = CONST 
    0x533ce: JUMPI v533ae(0x64bae), v111

    Begin block 0x64bae
    prev=[0x10b], succ=[]
    =================================
    0x64bce: v64bce(0x481) = CONST 
    0x64bee: CALLPRIVATE v64bce(0x481)

    Begin block 0x116
    prev=[0x10b], succ=[0x655ae, 0x121]
    =================================
    0x117: v117(0xa9059cbb) = CONST 
    0x11c: v11c = EQ v117(0xa9059cbb), v2e
    0x53dae: v53dae(0x655ae) = CONST 
    0x53dce: JUMPI v53dae(0x655ae), v11c

    Begin block 0x655ae
    prev=[0x116], succ=[]
    =================================
    0x655ce: v655ce(0x4ba) = CONST 
    0x655ee: CALLPRIVATE v655ce(0x4ba)

    Begin block 0x121
    prev=[0x116], succ=[0x65fae, 0x12c]
    =================================
    0x122: v122(0xc1a816ce) = CONST 
    0x127: v127 = EQ v122(0xc1a816ce), v2e
    0x547ae: v547ae(0x65fae) = CONST 
    0x547ce: JUMPI v547ae(0x65fae), v127

    Begin block 0x65fae
    prev=[0x121], succ=[]
    =================================
    0x65fce: v65fce(0x4f3) = CONST 
    0x65fee: CALLPRIVATE v65fce(0x4f3)

    Begin block 0x12c
    prev=[0x121], succ=[0x669ae, 0x137]
    =================================
    0x12d: v12d(0xd0febe4c) = CONST 
    0x132: v132 = EQ v12d(0xd0febe4c), v2e
    0x551ae: v551ae(0x669ae) = CONST 
    0x551ce: JUMPI v551ae(0x669ae), v132

    Begin block 0x669ae
    prev=[0x12c], succ=[]
    =================================
    0x669ce: v669ce(0x508) = CONST 
    0x669ee: CALLPRIVATE v669ce(0x508)

    Begin block 0x137
    prev=[0x12c], succ=[0x673ae, 0x142]
    =================================
    0x138: v138(0xdd62ed3e) = CONST 
    0x13d: v13d = EQ v138(0xdd62ed3e), v2e
    0x55bae: v55bae(0x673ae) = CONST 
    0x55bce: JUMPI v55bae(0x673ae), v13d

    Begin block 0x673ae
    prev=[0x137], succ=[]
    =================================
    0x673ce: v673ce(0x510) = CONST 
    0x673ee: CALLPRIVATE v673ce(0x510)

    Begin block 0x142
    prev=[0x137], succ=[0x67dae, 0x14d]
    =================================
    0x143: v143(0xf2fde38b) = CONST 
    0x148: v148 = EQ v143(0xf2fde38b), v2e
    0x565ae: v565ae(0x67dae) = CONST 
    0x565ce: JUMPI v565ae(0x67dae), v148

    Begin block 0x67dae
    prev=[0x142], succ=[]
    =================================
    0x67dce: v67dce(0x54b) = CONST 
    0x67dee: CALLPRIVATE v67dce(0x54b)

    Begin block 0x14d
    prev=[0x142], succ=[0x579ae, 0x687ae]
    =================================
    0x14e: v14e(0xf4027274) = CONST 
    0x153: v153 = EQ v14e(0xf4027274), v2e
    0x56fae: v56fae(0x687ae) = CONST 
    0x56fce: JUMPI v56fae(0x687ae), v153

    Begin block 0x579ae
    prev=[0x0, 0x14d], succ=[]
    =================================
    0x579ce: v579ce(0x158) = CONST 
    0x579ee: CALLPRIVATE v579ce(0x158)

    Begin block 0x687ae
    prev=[0x14d], succ=[]
    =================================
    0x687ce: v687ce(0x57e) = CONST 
    0x687ee: CALLPRIVATE v687ce(0x57e)

}

function 0x1010(v1010arg0, v1010arg1, v1010arg2) private {
    Begin block 0x1010
    prev=[], succ=[0x101b, 0x106a]
    =================================
    0x1011: v1011(0x0) = CONST 
    0x1015: v1015 = GT v1010arg0, v1010arg1
    0x1016: v1016 = ISZERO v1015
    0x1017: v1017(0x106a) = CONST 
    0x101a: JUMPI v1017(0x106a), v1016

    Begin block 0x101b
    prev=[0x1010], succ=[]
    =================================
    0x101b: v101b(0x40) = CONST 
    0x101e: v101e = MLOAD v101b(0x40)
    0x101f: v101f(0xe5) = CONST 
    0x1021: v1021(0x2) = CONST 
    0x1023: v1023(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1021(0x2), v101f(0xe5)
    0x1024: v1024(0x461bcd) = CONST 
    0x1028: v1028(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1024(0x461bcd), v1023(0x2000000000000000000000000000000000000000000000000000000000)
    0x102a: MSTORE v101e, v1028(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x102b: v102b(0x20) = CONST 
    0x102d: v102d(0x4) = CONST 
    0x1030: v1030 = ADD v101e, v102d(0x4)
    0x1031: MSTORE v1030, v102b(0x20)
    0x1032: v1032(0x1e) = CONST 
    0x1034: v1034(0x24) = CONST 
    0x1037: v1037 = ADD v101e, v1034(0x24)
    0x1038: MSTORE v1037, v1032(0x1e)
    0x1039: v1039(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x105a: v105a(0x44) = CONST 
    0x105d: v105d = ADD v101e, v105a(0x44)
    0x105e: MSTORE v105d, v1039(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1060: v1060 = MLOAD v101b(0x40)
    0x1064: v1064(0x0) = SUB v101e, v1060
    0x1065: v1065(0x64) = CONST 
    0x1067: v1067(0x64) = ADD v1065(0x64), v1064(0x0)
    0x1069: REVERT v1060, v1067(0x64)

    Begin block 0x106a
    prev=[0x1010], succ=[]
    =================================
    0x106d: v106d = SUB v1010arg1, v1010arg0
    0x106f: RETURNPRIVATE v1010arg2, v106d

}

function 0x10df(v10dfarg0, v10dfarg1, v10dfarg2) private {
    Begin block 0x10df
    prev=[], succ=[0x10f0, 0x10e9]
    =================================
    0x10e0: v10e0(0x0) = CONST 
    0x10e3: v10e3 = ISZERO v10dfarg1
    0x10e4: v10e4 = ISZERO v10e3
    0x10e5: v10e5(0x10f0) = CONST 
    0x10e8: JUMPI v10e5(0x10f0), v10e4

    Begin block 0x10f0
    prev=[0x10df], succ=[0x10fe, 0x10ff]
    =================================
    0x10f3: v10f3 = MUL v10dfarg0, v10dfarg1
    0x10f8: v10f8 = ISZERO v10dfarg1
    0x10f9: v10f9 = ISZERO v10f8
    0x10fa: v10fa(0x10ff) = CONST 
    0x10fd: JUMPI v10fa(0x10ff), v10f9

    Begin block 0x10fe
    prev=[0x10f0], succ=[]
    =================================
    0x10fe: THROW 

    Begin block 0x10ff
    prev=[0x10f0], succ=[0x1106, 0x22fb9]
    =================================
    0x1100: v1100 = DIV v10f3, v10dfarg1
    0x1101: v1101 = EQ v1100, v10dfarg0
    0x1102: v1102(0x22fb9) = CONST 
    0x1105: JUMPI v1102(0x22fb9), v1101

    Begin block 0x1106
    prev=[0x10ff], succ=[]
    =================================
    0x1106: v1106(0x40) = CONST 
    0x1109: v1109 = MLOAD v1106(0x40)
    0x110a: v110a(0xe5) = CONST 
    0x110c: v110c(0x2) = CONST 
    0x110e: v110e(0x2000000000000000000000000000000000000000000000000000000000) = EXP v110c(0x2), v110a(0xe5)
    0x110f: v110f(0x461bcd) = CONST 
    0x1113: v1113(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v110f(0x461bcd), v110e(0x2000000000000000000000000000000000000000000000000000000000)
    0x1115: MSTORE v1109, v1113(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1116: v1116(0x20) = CONST 
    0x1118: v1118(0x4) = CONST 
    0x111b: v111b = ADD v1109, v1118(0x4)
    0x111c: MSTORE v111b, v1116(0x20)
    0x111d: v111d(0x21) = CONST 
    0x111f: v111f(0x24) = CONST 
    0x1122: v1122 = ADD v1109, v111f(0x24)
    0x1123: MSTORE v1122, v111d(0x21)
    0x1124: v1124(0x536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f) = CONST 
    0x1145: v1145(0x44) = CONST 
    0x1148: v1148 = ADD v1109, v1145(0x44)
    0x1149: MSTORE v1148, v1124(0x536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f)
    0x114a: v114a(0x7700000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x116b: v116b(0x64) = CONST 
    0x116e: v116e = ADD v1109, v116b(0x64)
    0x116f: MSTORE v116e, v114a(0x7700000000000000000000000000000000000000000000000000000000000000)
    0x1171: v1171 = MLOAD v1106(0x40)
    0x1175: v1175(0x0) = SUB v1109, v1171
    0x1176: v1176(0x84) = CONST 
    0x1178: v1178(0x84) = ADD v1176(0x84), v1175(0x0)
    0x117a: REVERT v1171, v1178(0x84)

    Begin block 0x22fb9
    prev=[0x10ff], succ=[]
    =================================
    0x22fbf: RETURNPRIVATE v10dfarg2, v10f3

    Begin block 0x10e9
    prev=[0x10df], succ=[0x22f94]
    =================================
    0x10ea: v10ea(0x0) = CONST 
    0x10ec: v10ec(0x22f94) = CONST 
    0x10ef: JUMP v10ec(0x22f94)

    Begin block 0x22f94
    prev=[0x10e9], succ=[]
    =================================
    0x22f99: RETURNPRIVATE v10dfarg2, v10ea(0x0)

}

function 0x12c3(v12c3arg0, v12c3arg1, v12c3arg2) private {
    Begin block 0x12c3
    prev=[], succ=[0x12d1, 0x22fdf]
    =================================
    0x12c4: v12c4(0x0) = CONST 
    0x12c8: v12c8 = ADD v12c3arg0, v12c3arg1
    0x12cb: v12cb = LT v12c8, v12c3arg1
    0x12cc: v12cc = ISZERO v12cb
    0x12cd: v12cd(0x22fdf) = CONST 
    0x12d0: JUMPI v12cd(0x22fdf), v12cc

    Begin block 0x12d1
    prev=[0x12c3], succ=[]
    =================================
    0x12d1: v12d1(0x40) = CONST 
    0x12d4: v12d4 = MLOAD v12d1(0x40)
    0x12d5: v12d5(0xe5) = CONST 
    0x12d7: v12d7(0x2) = CONST 
    0x12d9: v12d9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v12d7(0x2), v12d5(0xe5)
    0x12da: v12da(0x461bcd) = CONST 
    0x12de: v12de(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v12da(0x461bcd), v12d9(0x2000000000000000000000000000000000000000000000000000000000)
    0x12e0: MSTORE v12d4, v12de(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12e1: v12e1(0x20) = CONST 
    0x12e3: v12e3(0x4) = CONST 
    0x12e6: v12e6 = ADD v12d4, v12e3(0x4)
    0x12e7: MSTORE v12e6, v12e1(0x20)
    0x12e8: v12e8(0x1b) = CONST 
    0x12ea: v12ea(0x24) = CONST 
    0x12ed: v12ed = ADD v12d4, v12ea(0x24)
    0x12ee: MSTORE v12ed, v12e8(0x1b)
    0x12ef: v12ef(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x1310: v1310(0x44) = CONST 
    0x1313: v1313 = ADD v12d4, v1310(0x44)
    0x1314: MSTORE v1313, v12ef(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x1316: v1316 = MLOAD v12d1(0x40)
    0x131a: v131a(0x0) = SUB v12d4, v1316
    0x131b: v131b(0x64) = CONST 
    0x131d: v131d(0x64) = ADD v131b(0x64), v131a(0x0)
    0x131f: REVERT v1316, v131d(0x64)

    Begin block 0x22fdf
    prev=[0x12c3], succ=[]
    =================================
    0x22fe5: RETURNPRIVATE v12c3arg2, v12c8

}

function 0x1320(v1320arg0, v1320arg1, v1320arg2) private {
    Begin block 0x1320
    prev=[], succ=[0x141c]
    =================================
    0x1321: v1321(0x132a) = CONST 
    0x1326: v1326(0x141c) = CONST 
    0x1329: JUMP v1326(0x141c)

    Begin block 0x141c
    prev=[0x1320], succ=[0x142d, 0x147c]
    =================================
    0x141d: v141d(0x1) = CONST 
    0x141f: v141f(0xa0) = CONST 
    0x1421: v1421(0x2) = CONST 
    0x1423: v1423(0x10000000000000000000000000000000000000000) = EXP v1421(0x2), v141f(0xa0)
    0x1424: v1424(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1423(0x10000000000000000000000000000000000000000), v141d(0x1)
    0x1426: v1426 = AND v1320arg1, v1424(0xffffffffffffffffffffffffffffffffffffffff)
    0x1427: v1427 = ISZERO v1426
    0x1428: v1428 = ISZERO v1427
    0x1429: v1429(0x147c) = CONST 
    0x142c: JUMPI v1429(0x147c), v1428

    Begin block 0x142d
    prev=[0x141c], succ=[]
    =================================
    0x142d: v142d(0x40) = CONST 
    0x1430: v1430 = MLOAD v142d(0x40)
    0x1431: v1431(0xe5) = CONST 
    0x1433: v1433(0x2) = CONST 
    0x1435: v1435(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1433(0x2), v1431(0xe5)
    0x1436: v1436(0x461bcd) = CONST 
    0x143a: v143a(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1436(0x461bcd), v1435(0x2000000000000000000000000000000000000000000000000000000000)
    0x143c: MSTORE v1430, v143a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x143d: v143d(0x20) = CONST 
    0x143f: v143f(0x4) = CONST 
    0x1442: v1442 = ADD v1430, v143f(0x4)
    0x1443: MSTORE v1442, v143d(0x20)
    0x1444: v1444(0x1f) = CONST 
    0x1446: v1446(0x24) = CONST 
    0x1449: v1449 = ADD v1430, v1446(0x24)
    0x144a: MSTORE v1449, v1444(0x1f)
    0x144b: v144b(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300) = CONST 
    0x146c: v146c(0x44) = CONST 
    0x146f: v146f = ADD v1430, v146c(0x44)
    0x1470: MSTORE v146f, v144b(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300)
    0x1472: v1472 = MLOAD v142d(0x40)
    0x1476: v1476(0x0) = SUB v1430, v1472
    0x1477: v1477(0x64) = CONST 
    0x1479: v1479(0x64) = ADD v1477(0x64), v1476(0x0)
    0x147b: REVERT v1472, v1479(0x64)

    Begin block 0x147c
    prev=[0x141c], succ=[0x148f]
    =================================
    0x147d: v147d(0x3) = CONST 
    0x147f: v147f = SLOAD v147d(0x3)
    0x1480: v1480(0x148f) = CONST 
    0x1485: v1485(0xffffffff) = CONST 
    0x148a: v148a(0x12c3) = CONST 
    0x148d: v148d(0x12c3) = AND v148a(0x12c3), v1485(0xffffffff)
    0x148e: v148e_0 = CALLPRIVATE v148d(0x12c3), v1320arg0, v147f, v1480(0x148f)

    Begin block 0x148f
    prev=[0x147c], succ=[0x14bb]
    =================================
    0x1490: v1490(0x3) = CONST 
    0x1492: SSTORE v1490(0x3), v148e_0
    0x1493: v1493(0x1) = CONST 
    0x1495: v1495(0xa0) = CONST 
    0x1497: v1497(0x2) = CONST 
    0x1499: v1499(0x10000000000000000000000000000000000000000) = EXP v1497(0x2), v1495(0xa0)
    0x149a: v149a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1499(0x10000000000000000000000000000000000000000), v1493(0x1)
    0x149c: v149c = AND v1320arg1, v149a(0xffffffffffffffffffffffffffffffffffffffff)
    0x149d: v149d(0x0) = CONST 
    0x14a1: MSTORE v149d(0x0), v149c
    0x14a2: v14a2(0x1) = CONST 
    0x14a4: v14a4(0x20) = CONST 
    0x14a6: MSTORE v14a4(0x20), v14a2(0x1)
    0x14a7: v14a7(0x40) = CONST 
    0x14aa: v14aa = SHA3 v149d(0x0), v14a7(0x40)
    0x14ab: v14ab = SLOAD v14aa
    0x14ac: v14ac(0x14bb) = CONST 
    0x14b1: v14b1(0xffffffff) = CONST 
    0x14b6: v14b6(0x12c3) = CONST 
    0x14b9: v14b9(0x12c3) = AND v14b6(0x12c3), v14b1(0xffffffff)
    0x14ba: v14ba_0 = CALLPRIVATE v14b9(0x12c3), v1320arg0, v14ab, v14ac(0x14bb)

    Begin block 0x14bb
    prev=[0x148f], succ=[0x132a]
    =================================
    0x14bc: v14bc(0x1) = CONST 
    0x14be: v14be(0xa0) = CONST 
    0x14c0: v14c0(0x2) = CONST 
    0x14c2: v14c2(0x10000000000000000000000000000000000000000) = EXP v14c0(0x2), v14be(0xa0)
    0x14c3: v14c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14c2(0x10000000000000000000000000000000000000000), v14bc(0x1)
    0x14c5: v14c5 = AND v1320arg1, v14c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x14c6: v14c6(0x0) = CONST 
    0x14ca: MSTORE v14c6(0x0), v14c5
    0x14cb: v14cb(0x1) = CONST 
    0x14cd: v14cd(0x20) = CONST 
    0x14d1: MSTORE v14cd(0x20), v14cb(0x1)
    0x14d2: v14d2(0x40) = CONST 
    0x14d6: v14d6 = SHA3 v14c6(0x0), v14d2(0x40)
    0x14da: SSTORE v14d6, v14ba_0
    0x14dc: v14dc = MLOAD v14d2(0x40)
    0x14df: MSTORE v14dc, v1320arg0
    0x14e1: v14e1 = MLOAD v14d2(0x40)
    0x14e6: v14e6(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x150a: v150a(0x0) = SUB v14dc, v14e1
    0x150d: v150d(0x20) = ADD v14cd(0x20), v150a(0x0)
    0x150f: LOG3 v14e1, v150d(0x20), v14e6(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v14c6(0x0), v14c5
    0x1512: JUMP v1321(0x132a)

    Begin block 0x132a
    prev=[0x14bb], succ=[]
    =================================
    0x132d: RETURNPRIVATE v1320arg2

}

function fallback()() public {
    Begin block 0x158
    prev=[], succ=[]
    =================================
    0x159: v159(0x0) = CONST 
    0x15c: REVERT v159(0x0), v159(0x0)

}

function name()() public {
    Begin block 0x15d
    prev=[], succ=[0x165, 0x169]
    =================================
    0x15e: v15e = CALLVALUE 
    0x160: v160 = ISZERO v15e
    0x161: v161(0x169) = CONST 
    0x164: JUMPI v161(0x169), v160

    Begin block 0x165
    prev=[0x15d], succ=[]
    =================================
    0x165: v165(0x0) = CONST 
    0x168: REVERT v165(0x0), v165(0x0)

    Begin block 0x169
    prev=[0x15d], succ=[0x5b1B0x169]
    =================================
    0x16b: v16b(0xa584) = CONST 
    0x16e: v16e(0x5b1) = CONST 
    0x171: JUMP v16e(0x5b1)

    Begin block 0x5b1B0x169
    prev=[0x169], succ=[0x5f7B0x169, 0xfc8cB0x169]
    =================================
    0x5b2S0x169: v5b2V169(0xa) = CONST 
    0x5b5S0x169: v5b5V169 = SLOAD v5b2V169(0xa)
    0x5b6S0x169: v5b6V169(0x40) = CONST 
    0x5b9S0x169: v5b9V169 = MLOAD v5b6V169(0x40)
    0x5baS0x169: v5baV169(0x20) = CONST 
    0x5bcS0x169: v5bcV169(0x1f) = CONST 
    0x5beS0x169: v5beV169(0x2) = CONST 
    0x5c0S0x169: v5c0V169(0x0) = CONST 
    0x5c2S0x169: v5c2V169(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v5c0V169(0x0)
    0x5c3S0x169: v5c3V169(0x100) = CONST 
    0x5c6S0x169: v5c6V169(0x1) = CONST 
    0x5c9S0x169: v5c9V169 = AND v5b5V169, v5c6V169(0x1)
    0x5caS0x169: v5caV169 = ISZERO v5c9V169
    0x5cbS0x169: v5cbV169 = MUL v5caV169, v5c3V169(0x100)
    0x5ccS0x169: v5ccV169 = ADD v5cbV169, v5c2V169(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x5cfS0x169: v5cfV169 = AND v5b5V169, v5ccV169
    0x5d3S0x169: v5d3V169 = DIV v5cfV169, v5beV169(0x2)
    0x5d6S0x169: v5d6V169 = ADD v5d3V169, v5bcV169(0x1f)
    0x5d9S0x169: v5d9V169 = DIV v5d6V169, v5baV169(0x20)
    0x5dbS0x169: v5dbV169 = MUL v5baV169(0x20), v5d9V169
    0x5ddS0x169: v5ddV169 = ADD v5b9V169, v5dbV169
    0x5dfS0x169: v5dfV169 = ADD v5baV169(0x20), v5ddV169
    0x5e2S0x169: MSTORE v5b6V169(0x40), v5dfV169
    0x5e5S0x169: MSTORE v5b9V169, v5d3V169
    0x5e6S0x169: v5e6V169(0x60) = CONST 
    0x5eeS0x169: v5eeV169 = ADD v5b9V169, v5baV169(0x20)
    0x5f2S0x169: v5f2V169 = ISZERO v5d3V169
    0x5f3S0x169: v5f3V169(0xfc8c) = CONST 
    0x5f6S0x169: JUMPI v5f3V169(0xfc8c), v5f2V169

    Begin block 0x5f7B0x169
    prev=[0x5b1B0x169], succ=[0x5ffB0x169, 0x6120x5b1B0x169]
    =================================
    0x5f8S0x169: v5f8V169(0x1f) = CONST 
    0x5faS0x169: v5faV169 = LT v5f8V169(0x1f), v5d3V169
    0x5fbS0x169: v5fbV169(0x612) = CONST 
    0x5feS0x169: JUMPI v5fbV169(0x612), v5faV169

    Begin block 0x5ffB0x169
    prev=[0x5f7B0x169], succ=[0xfcb5B0x169]
    =================================
    0x5ffS0x169: v5ffV169(0x100) = CONST 
    0x604S0x169: v604V169 = SLOAD v5b2V169(0xa)
    0x605S0x169: v605V169 = DIV v604V169, v5ffV169(0x100)
    0x606S0x169: v606V169 = MUL v605V169, v5ffV169(0x100)
    0x608S0x169: MSTORE v5eeV169, v606V169
    0x60aS0x169: v60aV169(0x20) = CONST 
    0x60cS0x169: v60cV169 = ADD v60aV169(0x20), v5eeV169
    0x60eS0x169: v60eV169(0xfcb5) = CONST 
    0x611S0x169: JUMP v60eV169(0xfcb5)

    Begin block 0xfcb5B0x169
    prev=[0x5ffB0x169], succ=[0xa584]
    =================================
    0xfcbeS0x169: JUMP v16b(0xa584)

    Begin block 0xa584
    prev=[0xfc8cB0x169, 0xfcb5B0x169, 0x230050x5b1B0x169], succ=[0x1940x15d]
    =================================
    0xa585: va585(0x40) = CONST 
    0xa588: va588 = MLOAD va585(0x40)
    0xa589: va589(0x20) = CONST 
    0xa58d: MSTORE va588, va589(0x20)
    0xa58f: va58f = MLOAD v5b9V169
    0xa592: va592 = ADD va588, va589(0x20)
    0xa593: MSTORE va592, va58f
    0xa595: va595 = MLOAD v5b9V169
    0xa59c: va59c = ADD va588, va585(0x40)
    0xa59f: va59f = ADD v5b9V169, va589(0x20)
    0xa5a4: va5a4(0x0) = CONST 
    0xcea4: vcea4(0x194) = CONST 
    0xcec4: JUMP vcea4(0x194)

    Begin block 0x1940x15d
    prev=[0xa584, 0x19d0x15d], succ=[0x1ac0x15d, 0x19d0x15d]
    =================================
    0x1940x15d_0x0: v19415d_0 = PHI va5a4(0x0), v15d1a7
    0x1970x15d: v15d197 = LT v19415d_0, va595
    0x1980x15d: v15d198 = ISZERO v15d197
    0x1990x15d: v15d199(0x1ac) = CONST 
    0x19c0x15d: JUMPI v15d199(0x1ac), v15d198

    Begin block 0x1ac0x15d
    prev=[0x1940x15d], succ=[0x1c00x15d, 0x1d90x15d]
    =================================
    0x1b50x15d: v15d1b5 = ADD va595, va59c
    0x1b70x15d: v15d1b7(0x1f) = CONST 
    0x1b90x15d: v15d1b9 = AND v15d1b7(0x1f), va595
    0x1bb0x15d: v15d1bb = ISZERO v15d1b9
    0x1bc0x15d: v15d1bc(0x1d9) = CONST 
    0x1bf0x15d: JUMPI v15d1bc(0x1d9), v15d1bb

    Begin block 0x1c00x15d
    prev=[0x1ac0x15d], succ=[0x1d90x15d]
    =================================
    0x1c20x15d: v15d1c2 = SUB v15d1b5, v15d1b9
    0x1c40x15d: v15d1c4 = MLOAD v15d1c2
    0x1c50x15d: v15d1c5(0x1) = CONST 
    0x1c80x15d: v15d1c8(0x20) = CONST 
    0x1ca0x15d: v15d1ca = SUB v15d1c8(0x20), v15d1b9
    0x1cb0x15d: v15d1cb(0x100) = CONST 
    0x1ce0x15d: v15d1ce = EXP v15d1cb(0x100), v15d1ca
    0x1cf0x15d: v15d1cf = SUB v15d1ce, v15d1c5(0x1)
    0x1d00x15d: v15d1d0 = NOT v15d1cf
    0x1d10x15d: v15d1d1 = AND v15d1d0, v15d1c4
    0x1d30x15d: MSTORE v15d1c2, v15d1d1
    0x1d40x15d: v15d1d4(0x20) = CONST 
    0x1d60x15d: v15d1d6 = ADD v15d1d4(0x20), v15d1c2
    0x34920x15d: v15d3492(0x1d9) = CONST 
    0x34b20x15d: JUMP v15d3492(0x1d9)

    Begin block 0x1d90x15d
    prev=[0x1c00x15d, 0x1ac0x15d], succ=[]
    =================================
    0x1d90x15d_0x1: v1d915d_1 = PHI v15d1d6, v15d1b5
    0x1df0x15d: v15d1df(0x40) = CONST 
    0x1e10x15d: v15d1e1 = MLOAD v15d1df(0x40)
    0x1e40x15d: v15d1e4 = SUB v1d915d_1, v15d1e1
    0x1e60x15d: RETURN v15d1e1, v15d1e4

    Begin block 0x19d0x15d
    prev=[0x1940x15d], succ=[0x1940x15d]
    =================================
    0x19d0x15d_0x0: v19d15d_0 = PHI va5a4(0x0), v15d1a7
    0x19f0x15d: v15d19f = ADD v19d15d_0, va59f
    0x1a00x15d: v15d1a0 = MLOAD v15d19f
    0x1a30x15d: v15d1a3 = ADD v19d15d_0, va59c
    0x1a40x15d: MSTORE v15d1a3, v15d1a0
    0x1a50x15d: v15d1a5(0x20) = CONST 
    0x1a70x15d: v15d1a7 = ADD v15d1a5(0x20), v19d15d_0
    0x1a80x15d: v15d1a8(0x194) = CONST 
    0x1ab0x15d: JUMP v15d1a8(0x194)

    Begin block 0x6120x5b1B0x169
    prev=[0x5f7B0x169], succ=[0x6200x5b1B0x169]
    =================================
    0x6140x5b1S0x169: v5b1614V169 = ADD v5eeV169, v5d3V169
    0x6170x5b1S0x169: v5b1617V169(0x0) = CONST 
    0x6190x5b1S0x169: MSTORE v5b1617V169(0x0), v5b2V169(0xa)
    0x61a0x5b1S0x169: v5b161aV169(0x20) = CONST 
    0x61c0x5b1S0x169: v5b161cV169(0x0) = CONST 
    0x61e0x5b1S0x169: v5b161eV169 = SHA3 v5b161cV169(0x0), v5b161aV169(0x20)
    0x3e920x5b1S0x169: v5b13e92V169(0x620) = CONST 
    0x3eb20x5b1S0x169: JUMP v5b13e92V169(0x620)

    Begin block 0x6200x5b1B0x169
    prev=[0x6120x5b1B0x169, 0x6200x5b1B0x169], succ=[0x6200x5b1B0x169, 0x6340x5b1B0x169]
    =================================
    0x6200x5b1_0x0S0x169: v6205b1_0V169 = PHI v5eeV169, v5b162cV169
    0x6200x5b1_0x1S0x169: v6205b1_1V169 = PHI v5b161eV169, v5b1628V169
    0x6220x5b1S0x169: v5b1622V169 = SLOAD v6205b1_1V169
    0x6240x5b1S0x169: MSTORE v6205b1_0V169, v5b1622V169
    0x6260x5b1S0x169: v5b1626V169(0x1) = CONST 
    0x6280x5b1S0x169: v5b1628V169 = ADD v5b1626V169(0x1), v6205b1_1V169
    0x62a0x5b1S0x169: v5b162aV169(0x20) = CONST 
    0x62c0x5b1S0x169: v5b162cV169 = ADD v5b162aV169(0x20), v6205b1_0V169
    0x62f0x5b1S0x169: v5b162fV169 = GT v5b1614V169, v5b162cV169
    0x6300x5b1S0x169: v5b1630V169(0x620) = CONST 
    0x6330x5b1S0x169: JUMPI v5b1630V169(0x620), v5b162fV169

    Begin block 0x6340x5b1B0x169
    prev=[0x6200x5b1B0x169], succ=[0x230050x5b1B0x169]
    =================================
    0x6360x5b1S0x169: v5b1636V169 = SUB v5b162cV169, v5b1614V169
    0x6370x5b1S0x169: v5b1637V169(0x1f) = CONST 
    0x6390x5b1S0x169: v5b1639V169 = AND v5b1637V169(0x1f), v5b1636V169
    0x63b0x5b1S0x169: v5b163bV169 = ADD v5b1614V169, v5b1639V169
    0x48920x5b1S0x169: v5b14892V169(0x23005) = CONST 
    0x48b20x5b1S0x169: JUMP v5b14892V169(0x23005)

    Begin block 0x230050x5b1B0x169
    prev=[0x6340x5b1B0x169], succ=[0xa584]
    =================================
    0x2300e0x5b1S0x169: JUMP v16b(0xa584)

    Begin block 0xfc8cB0x169
    prev=[0x5b1B0x169], succ=[0xa584]
    =================================
    0xfc95S0x169: JUMP v16b(0xa584)

}

function approve(address,uint256)() public {
    Begin block 0x1e7
    prev=[], succ=[0x1ef, 0x1f3]
    =================================
    0x1e8: v1e8 = CALLVALUE 
    0x1ea: v1ea = ISZERO v1e8
    0x1eb: v1eb(0x1f3) = CONST 
    0x1ee: JUMPI v1eb(0x1f3), v1ea

    Begin block 0x1ef
    prev=[0x1e7], succ=[]
    =================================
    0x1ef: v1ef(0x0) = CONST 
    0x1f2: REVERT v1ef(0x0), v1ef(0x0)

    Begin block 0x1f3
    prev=[0x1e7], succ=[0x206, 0x20a]
    =================================
    0x1f5: v1f5(0xcee4) = CONST 
    0x1f8: v1f8(0x4) = CONST 
    0x1fb: v1fb = CALLDATASIZE 
    0x1fc: v1fc = SUB v1fb, v1f8(0x4)
    0x1fd: v1fd(0x40) = CONST 
    0x200: v200 = LT v1fc, v1fd(0x40)
    0x201: v201 = ISZERO v200
    0x202: v202(0x20a) = CONST 
    0x205: JUMPI v202(0x20a), v201

    Begin block 0x206
    prev=[0x1f3], succ=[]
    =================================
    0x206: v206(0x0) = CONST 
    0x209: REVERT v206(0x0), v206(0x0)

    Begin block 0x20a
    prev=[0x1f3], succ=[0x647B0x20a]
    =================================
    0x20c: v20c(0x1) = CONST 
    0x20e: v20e(0xa0) = CONST 
    0x210: v210(0x2) = CONST 
    0x212: v212(0x10000000000000000000000000000000000000000) = EXP v210(0x2), v20e(0xa0)
    0x213: v213(0xffffffffffffffffffffffffffffffffffffffff) = SUB v212(0x10000000000000000000000000000000000000000), v20c(0x1)
    0x215: v215 = CALLDATALOAD v1f8(0x4)
    0x216: v216 = AND v215, v213(0xffffffffffffffffffffffffffffffffffffffff)
    0x218: v218(0x20) = CONST 
    0x21a: v21a(0x24) = ADD v218(0x20), v1f8(0x4)
    0x21b: v21b = CALLDATALOAD v21a(0x24)
    0x21c: v21c(0x647) = CONST 
    0x21f: JUMP v21c(0x647)

    Begin block 0x647B0x20a
    prev=[0x20a], succ=[0xfcdeB0x20a]
    =================================
    0x648S0x20a: v648V20a(0x0) = CONST 
    0x64aS0x20a: v64aV20a(0xfcde) = CONST 
    0x64dS0x20a: v64dV20a = CALLER 
    0x650S0x20a: v650V20a(0xcdd) = CONST 
    0x653S0x20a: CALLPRIVATE v650V20a(0xcdd), v21b, v216, v64dV20a, v64aV20a(0xfcde)

    Begin block 0xfcdeB0x20a
    prev=[0x647B0x20a], succ=[0x23053B0x20a]
    =================================
    0xfce0S0x20a: vfce0V20a(0x1) = CONST 
    0x1491cS0x20a: v1491cV20a(0x23053) = CONST 
    0x1493cS0x20a: JUMP v1491cV20a(0x23053)

    Begin block 0x23053B0x20a
    prev=[0xfcdeB0x20a], succ=[0xcee4]
    =================================
    0x23058S0x20a: JUMP v1f5(0xcee4)

    Begin block 0xcee4
    prev=[0x23053B0x20a], succ=[]
    =================================
    0xcee5: vcee5(0x40) = CONST 
    0xcee8: vcee8 = MLOAD vcee5(0x40)
    0xceea: vceea(0x0) = ISZERO vfce0V20a(0x1)
    0xceeb: vceeb(0x1) = ISZERO vceea(0x0)
    0xceed: MSTORE vcee8, vceeb(0x1)
    0xceee: vceee = MLOAD vcee5(0x40)
    0xcef2: vcef2(0x0) = SUB vcee8, vceee
    0xcef3: vcef3(0x20) = CONST 
    0xcef5: vcef5(0x20) = ADD vcef3(0x20), vcef2(0x0)
    0xcef7: RETURN vceee, vcef5(0x20)

}

function totalSupply()() public {
    Begin block 0x234
    prev=[], succ=[0x23c, 0x240]
    =================================
    0x235: v235 = CALLVALUE 
    0x237: v237 = ISZERO v235
    0x238: v238(0x240) = CONST 
    0x23b: JUMPI v238(0x240), v237

    Begin block 0x23c
    prev=[0x234], succ=[]
    =================================
    0x23c: v23c(0x0) = CONST 
    0x23f: REVERT v23c(0x0), v23c(0x0)

    Begin block 0x240
    prev=[0x234], succ=[0x65e]
    =================================
    0x242: v242(0xcf17) = CONST 
    0x245: v245(0x65e) = CONST 
    0x248: JUMP v245(0x65e)

    Begin block 0x65e
    prev=[0x240], succ=[0xcf17]
    =================================
    0x65f: v65f(0x3) = CONST 
    0x661: v661 = SLOAD v65f(0x3)
    0x663: JUMP v242(0xcf17)

    Begin block 0xcf17
    prev=[0x65e], succ=[]
    =================================
    0xcf18: vcf18(0x40) = CONST 
    0xcf1b: vcf1b = MLOAD vcf18(0x40)
    0xcf1e: MSTORE vcf1b, v661
    0xcf1f: vcf1f = MLOAD vcf18(0x40)
    0xcf23: vcf23(0x0) = SUB vcf1b, vcf1f
    0xcf24: vcf24(0x20) = CONST 
    0xcf26: vcf26(0x20) = ADD vcf24(0x20), vcf23(0x0)
    0xcf28: RETURN vcf1f, vcf26(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x25b
    prev=[], succ=[0x263, 0x267]
    =================================
    0x25c: v25c = CALLVALUE 
    0x25e: v25e = ISZERO v25c
    0x25f: v25f(0x267) = CONST 
    0x262: JUMPI v25f(0x267), v25e

    Begin block 0x263
    prev=[0x25b], succ=[]
    =================================
    0x263: v263(0x0) = CONST 
    0x266: REVERT v263(0x0), v263(0x0)

    Begin block 0x267
    prev=[0x25b], succ=[0x27a, 0x27e]
    =================================
    0x269: v269(0xcf48) = CONST 
    0x26c: v26c(0x4) = CONST 
    0x26f: v26f = CALLDATASIZE 
    0x270: v270 = SUB v26f, v26c(0x4)
    0x271: v271(0x60) = CONST 
    0x274: v274 = LT v270, v271(0x60)
    0x275: v275 = ISZERO v274
    0x276: v276(0x27e) = CONST 
    0x279: JUMPI v276(0x27e), v275

    Begin block 0x27a
    prev=[0x267], succ=[]
    =================================
    0x27a: v27a(0x0) = CONST 
    0x27d: REVERT v27a(0x0), v27a(0x0)

    Begin block 0x27e
    prev=[0x267], succ=[0x664]
    =================================
    0x280: v280(0x1) = CONST 
    0x282: v282(0xa0) = CONST 
    0x284: v284(0x2) = CONST 
    0x286: v286(0x10000000000000000000000000000000000000000) = EXP v284(0x2), v282(0xa0)
    0x287: v287(0xffffffffffffffffffffffffffffffffffffffff) = SUB v286(0x10000000000000000000000000000000000000000), v280(0x1)
    0x289: v289 = CALLDATALOAD v26c(0x4)
    0x28b: v28b = AND v287(0xffffffffffffffffffffffffffffffffffffffff), v289
    0x28d: v28d(0x20) = CONST 
    0x290: v290(0x24) = ADD v26c(0x4), v28d(0x20)
    0x291: v291 = CALLDATALOAD v290(0x24)
    0x294: v294 = AND v287(0xffffffffffffffffffffffffffffffffffffffff), v291
    0x296: v296(0x40) = CONST 
    0x298: v298(0x44) = ADD v296(0x40), v26c(0x4)
    0x299: v299 = CALLDATALOAD v298(0x44)
    0x29a: v29a(0x664) = CONST 
    0x29d: JUMP v29a(0x664)

    Begin block 0x664
    prev=[0x27e], succ=[0x671]
    =================================
    0x665: v665(0x0) = CONST 
    0x667: v667(0x671) = CONST 
    0x66d: v66d(0xe4a) = CONST 
    0x670: CALLPRIVATE v66d(0xe4a), v299, v294, v28b, v667(0x671)

    Begin block 0x671
    prev=[0x664], succ=[0x1495c]
    =================================
    0x672: v672(0x1) = CONST 
    0x674: v674(0xa0) = CONST 
    0x676: v676(0x2) = CONST 
    0x678: v678(0x10000000000000000000000000000000000000000) = EXP v676(0x2), v674(0xa0)
    0x679: v679(0xffffffffffffffffffffffffffffffffffffffff) = SUB v678(0x10000000000000000000000000000000000000000), v672(0x1)
    0x67b: v67b = AND v28b, v679(0xffffffffffffffffffffffffffffffffffffffff)
    0x67c: v67c(0x0) = CONST 
    0x680: MSTORE v67c(0x0), v67b
    0x681: v681(0x2) = CONST 
    0x683: v683(0x20) = CONST 
    0x687: MSTORE v683(0x20), v681(0x2)
    0x688: v688(0x40) = CONST 
    0x68c: v68c = SHA3 v67c(0x0), v688(0x40)
    0x68d: v68d = CALLER 
    0x690: MSTORE v67c(0x0), v68d
    0x692: MSTORE v683(0x20), v68c
    0x695: v695 = SHA3 v67c(0x0), v688(0x40)
    0x696: v696 = SLOAD v695
    0x697: v697(0x6b1) = CONST 
    0x69d: v69d(0x1495c) = CONST 
    0x6a2: v6a2(0xffffffff) = CONST 
    0x6a7: v6a7(0x1010) = CONST 
    0x6aa: v6aa(0x1010) = AND v6a7(0x1010), v6a2(0xffffffff)
    0x6ab: v6ab_0 = CALLPRIVATE v6aa(0x1010), v299, v696, v69d(0x1495c)

    Begin block 0x1495c
    prev=[0x671], succ=[0x6b1]
    =================================
    0x1495d: v1495d(0xcdd) = CONST 
    0x14960: CALLPRIVATE v1495d(0xcdd), v6ab_0, v68d, v28b, v697(0x6b1)

    Begin block 0x6b1
    prev=[0x1495c], succ=[0xcf48]
    =================================
    0x6b3: v6b3(0x1) = CONST 
    0x6ba: JUMP v269(0xcf48)

    Begin block 0xcf48
    prev=[0x6b1], succ=[]
    =================================
    0xcf49: vcf49(0x40) = CONST 
    0xcf4c: vcf4c = MLOAD vcf49(0x40)
    0xcf4e: vcf4e(0x0) = ISZERO v6b3(0x1)
    0xcf4f: vcf4f(0x1) = ISZERO vcf4e(0x0)
    0xcf51: MSTORE vcf4c, vcf4f(0x1)
    0xcf52: vcf52 = MLOAD vcf49(0x40)
    0xcf56: vcf56(0x0) = SUB vcf4c, vcf52
    0xcf57: vcf57(0x20) = CONST 
    0xcf59: vcf59(0x20) = ADD vcf57(0x20), vcf56(0x0)
    0xcf5b: RETURN vcf52, vcf59(0x20)

}

function returnDebt()() public {
    Begin block 0x29e
    prev=[], succ=[0x6bb]
    =================================
    0x29f: v29f(0xcf7b) = CONST 
    0x2a2: v2a2(0x6bb) = CONST 
    0x2a5: JUMP v2a2(0x6bb)

    Begin block 0x6bb
    prev=[0x29e], succ=[0xcf7b]
    =================================
    0x6bc: v6bc(0x6) = CONST 
    0x6bf: v6bf = SLOAD v6bc(0x6)
    0x6c0: v6c0 = CALLVALUE 
    0x6c3: v6c3 = ADD v6c0, v6bf
    0x6c6: SSTORE v6bc(0x6), v6c3
    0x6c7: v6c7(0x40) = CONST 
    0x6ca: v6ca = MLOAD v6c7(0x40)
    0x6cd: MSTORE v6ca, v6c0
    0x6ce: v6ce = MLOAD v6c7(0x40)
    0x6cf: v6cf = CALLER 
    0x6d1: v6d1(0x3bd0807d8e5b205f7750bcc47f0773775b833e979f04c19d21f1523547785b59) = CONST 
    0x6f6: v6f6(0x0) = SUB v6ca, v6ce
    0x6f7: v6f7(0x20) = CONST 
    0x6f9: v6f9(0x20) = ADD v6f7(0x20), v6f6(0x0)
    0x6fb: LOG2 v6ce, v6f9(0x20), v6d1(0x3bd0807d8e5b205f7750bcc47f0773775b833e979f04c19d21f1523547785b59), v6cf
    0x6fc: JUMP v29f(0xcf7b)

    Begin block 0xcf7b
    prev=[0x6bb], succ=[]
    =================================
    0xcf7c: STOP 

}

function rate()() public {
    Begin block 0x2a8
    prev=[], succ=[0x2b0, 0x2b4]
    =================================
    0x2a9: v2a9 = CALLVALUE 
    0x2ab: v2ab = ISZERO v2a9
    0x2ac: v2ac(0x2b4) = CONST 
    0x2af: JUMPI v2ac(0x2b4), v2ab

    Begin block 0x2b0
    prev=[0x2a8], succ=[]
    =================================
    0x2b0: v2b0(0x0) = CONST 
    0x2b3: REVERT v2b0(0x0), v2b0(0x0)

    Begin block 0x2b4
    prev=[0x2a8], succ=[0x6fd]
    =================================
    0x2b6: v2b6(0xcf9c) = CONST 
    0x2b9: v2b9(0x6fd) = CONST 
    0x2bc: JUMP v2b9(0x6fd)

    Begin block 0x6fd
    prev=[0x2b4], succ=[0xcf9c]
    =================================
    0x6fe: v6fe(0x7) = CONST 
    0x700: v700 = SLOAD v6fe(0x7)
    0x702: JUMP v2b6(0xcf9c)

    Begin block 0xcf9c
    prev=[0x6fd], succ=[]
    =================================
    0xcf9d: vcf9d(0x40) = CONST 
    0xcfa0: vcfa0 = MLOAD vcf9d(0x40)
    0xcfa3: MSTORE vcfa0, v700
    0xcfa4: vcfa4 = MLOAD vcf9d(0x40)
    0xcfa8: vcfa8(0x0) = SUB vcfa0, vcfa4
    0xcfa9: vcfa9(0x20) = CONST 
    0xcfab: vcfab(0x20) = ADD vcfa9(0x20), vcfa8(0x0)
    0xcfad: RETURN vcfa4, vcfab(0x20)

}

function withdraw(uint256)() public {
    Begin block 0x2bd
    prev=[], succ=[0x2c5, 0x2c9]
    =================================
    0x2be: v2be = CALLVALUE 
    0x2c0: v2c0 = ISZERO v2be
    0x2c1: v2c1(0x2c9) = CONST 
    0x2c4: JUMPI v2c1(0x2c9), v2c0

    Begin block 0x2c5
    prev=[0x2bd], succ=[]
    =================================
    0x2c5: v2c5(0x0) = CONST 
    0x2c8: REVERT v2c5(0x0), v2c5(0x0)

    Begin block 0x2c9
    prev=[0x2bd], succ=[0x2dc, 0x2e0]
    =================================
    0x2cb: v2cb(0xcfcd) = CONST 
    0x2ce: v2ce(0x4) = CONST 
    0x2d1: v2d1 = CALLDATASIZE 
    0x2d2: v2d2 = SUB v2d1, v2ce(0x4)
    0x2d3: v2d3(0x20) = CONST 
    0x2d6: v2d6 = LT v2d2, v2d3(0x20)
    0x2d7: v2d7 = ISZERO v2d6
    0x2d8: v2d8(0x2e0) = CONST 
    0x2db: JUMPI v2d8(0x2e0), v2d7

    Begin block 0x2dc
    prev=[0x2c9], succ=[]
    =================================
    0x2dc: v2dc(0x0) = CONST 
    0x2df: REVERT v2dc(0x0), v2dc(0x0)

    Begin block 0x2e0
    prev=[0x2c9], succ=[0x703]
    =================================
    0x2e2: v2e2 = CALLDATALOAD v2ce(0x4)
    0x2e3: v2e3(0x703) = CONST 
    0x2e6: JUMP v2e3(0x703)

    Begin block 0x703
    prev=[0x2e0], succ=[0x1070]
    =================================
    0x704: v704(0x0) = CONST 
    0x706: v706(0x72b) = CONST 
    0x709: v709(0x2) = CONST 
    0x70b: v70b(0x71f) = CONST 
    0x70e: v70e(0x7) = CONST 
    0x710: v710 = SLOAD v70e(0x7)
    0x712: v712(0x1070) = CONST 
    0x718: v718(0xffffffff) = CONST 
    0x71d: v71d(0x1070) = AND v718(0xffffffff), v712(0x1070)
    0x71e: JUMP v71d(0x1070)

    Begin block 0x1070
    prev=[0x703], succ=[0x107a, 0x10c9]
    =================================
    0x1071: v1071(0x0) = CONST 
    0x1075: v1075 = GT v710, v1071(0x0)
    0x1076: v1076(0x10c9) = CONST 
    0x1079: JUMPI v1076(0x10c9), v1075

    Begin block 0x107a
    prev=[0x1070], succ=[]
    =================================
    0x107a: v107a(0x40) = CONST 
    0x107d: v107d = MLOAD v107a(0x40)
    0x107e: v107e(0xe5) = CONST 
    0x1080: v1080(0x2) = CONST 
    0x1082: v1082(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1080(0x2), v107e(0xe5)
    0x1083: v1083(0x461bcd) = CONST 
    0x1087: v1087(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1083(0x461bcd), v1082(0x2000000000000000000000000000000000000000000000000000000000)
    0x1089: MSTORE v107d, v1087(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x108a: v108a(0x20) = CONST 
    0x108c: v108c(0x4) = CONST 
    0x108f: v108f = ADD v107d, v108c(0x4)
    0x1090: MSTORE v108f, v108a(0x20)
    0x1091: v1091(0x1a) = CONST 
    0x1093: v1093(0x24) = CONST 
    0x1096: v1096 = ADD v107d, v1093(0x24)
    0x1097: MSTORE v1096, v1091(0x1a)
    0x1098: v1098(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x10b9: v10b9(0x44) = CONST 
    0x10bc: v10bc = ADD v107d, v10b9(0x44)
    0x10bd: MSTORE v10bc, v1098(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x10bf: v10bf = MLOAD v107a(0x40)
    0x10c3: v10c3(0x0) = SUB v107d, v10bf
    0x10c4: v10c4(0x64) = CONST 
    0x10c6: v10c6(0x64) = ADD v10c4(0x64), v10c3(0x0)
    0x10c8: REVERT v10bf, v10c6(0x64)

    Begin block 0x10c9
    prev=[0x1070], succ=[0x10d5, 0x10d6]
    =================================
    0x10ca: v10ca(0x0) = CONST 
    0x10cf: v10cf = ISZERO v710
    0x10d0: v10d0 = ISZERO v10cf
    0x10d1: v10d1(0x10d6) = CONST 
    0x10d4: JUMPI v10d1(0x10d6), v10d0

    Begin block 0x10d5
    prev=[0x10c9], succ=[]
    =================================
    0x10d5: THROW 

    Begin block 0x10d6
    prev=[0x10c9], succ=[0x71f]
    =================================
    0x10d7: v10d7 = DIV v2e2, v710
    0x10de: JUMP v70b(0x71f)

    Begin block 0x71f
    prev=[0x10d6], succ=[0x72b]
    =================================
    0x721: v721(0xffffffff) = CONST 
    0x726: v726(0x10df) = CONST 
    0x729: v729(0x10df) = AND v726(0x10df), v721(0xffffffff)
    0x72a: v72a_0 = CALLPRIVATE v729(0x10df), v709(0x2), v10d7, v706(0x72b)

    Begin block 0x72b
    prev=[0x71f], succ=[0x739, 0x762]
    =================================
    0x72c: v72c(0x6) = CONST 
    0x72e: v72e = SLOAD v72c(0x6)
    0x733: v733 = GT v72a_0, v72e
    0x734: v734 = ISZERO v733
    0x735: v735(0x762) = CONST 
    0x738: JUMPI v735(0x762), v734

    Begin block 0x739
    prev=[0x72b], succ=[]
    =================================
    0x739: v739(0x40) = CONST 
    0x73c: v73c = MLOAD v739(0x40)
    0x73d: v73d(0xe5) = CONST 
    0x73f: v73f(0x2) = CONST 
    0x741: v741(0x2000000000000000000000000000000000000000000000000000000000) = EXP v73f(0x2), v73d(0xe5)
    0x742: v742(0x461bcd) = CONST 
    0x746: v746(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v742(0x461bcd), v741(0x2000000000000000000000000000000000000000000000000000000000)
    0x748: MSTORE v73c, v746(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x749: v749(0x20) = CONST 
    0x74b: v74b(0x4) = CONST 
    0x74e: v74e = ADD v73c, v74b(0x4)
    0x74f: MSTORE v74e, v749(0x20)
    0x750: v750(0x0) = CONST 
    0x752: v752(0x24) = CONST 
    0x755: v755 = ADD v73c, v752(0x24)
    0x756: MSTORE v755, v750(0x0)
    0x758: v758 = MLOAD v739(0x40)
    0x75c: v75c(0x0) = SUB v73c, v758
    0x75d: v75d(0x64) = CONST 
    0x75f: v75f(0x64) = ADD v75d(0x64), v75c(0x0)
    0x761: REVERT v758, v75f(0x64)

    Begin block 0x762
    prev=[0x72b], succ=[0x975B0x762]
    =================================
    0x764: v764(0x76c) = CONST 
    0x767: v767 = CALLER 
    0x768: v768(0x975) = CONST 
    0x76b: JUMP v768(0x975)

    Begin block 0x975B0x762
    prev=[0x762], succ=[0x76c]
    =================================
    0x976S0x762: v976V762(0x1) = CONST 
    0x978S0x762: v978V762(0xa0) = CONST 
    0x97aS0x762: v97aV762(0x2) = CONST 
    0x97cS0x762: v97cV762(0x10000000000000000000000000000000000000000) = EXP v97aV762(0x2), v978V762(0xa0)
    0x97dS0x762: v97dV762(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97cV762(0x10000000000000000000000000000000000000000), v976V762(0x1)
    0x97eS0x762: v97eV762 = AND v97dV762(0xffffffffffffffffffffffffffffffffffffffff), v767
    0x97fS0x762: v97fV762(0x0) = CONST 
    0x983S0x762: MSTORE v97fV762(0x0), v97eV762
    0x984S0x762: v984V762(0x1) = CONST 
    0x986S0x762: v986V762(0x20) = CONST 
    0x988S0x762: MSTORE v986V762(0x20), v984V762(0x1)
    0x989S0x762: v989V762(0x40) = CONST 
    0x98cS0x762: v98cV762 = SHA3 v97fV762(0x0), v989V762(0x40)
    0x98dS0x762: v98dV762 = SLOAD v98cV762
    0x98fS0x762: JUMP v764(0x76c)

    Begin block 0x76c
    prev=[0x975B0x762], succ=[0x773, 0x79c]
    =================================
    0x76d: v76d = LT v98dV762, v2e2
    0x76e: v76e = ISZERO v76d
    0x76f: v76f(0x79c) = CONST 
    0x772: JUMPI v76f(0x79c), v76e

    Begin block 0x773
    prev=[0x76c], succ=[]
    =================================
    0x773: v773(0x40) = CONST 
    0x776: v776 = MLOAD v773(0x40)
    0x777: v777(0xe5) = CONST 
    0x779: v779(0x2) = CONST 
    0x77b: v77b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v779(0x2), v777(0xe5)
    0x77c: v77c(0x461bcd) = CONST 
    0x780: v780(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v77c(0x461bcd), v77b(0x2000000000000000000000000000000000000000000000000000000000)
    0x782: MSTORE v776, v780(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x783: v783(0x20) = CONST 
    0x785: v785(0x4) = CONST 
    0x788: v788 = ADD v776, v785(0x4)
    0x789: MSTORE v788, v783(0x20)
    0x78a: v78a(0x0) = CONST 
    0x78c: v78c(0x24) = CONST 
    0x78f: v78f = ADD v776, v78c(0x24)
    0x790: MSTORE v78f, v78a(0x0)
    0x792: v792 = MLOAD v773(0x40)
    0x796: v796(0x0) = SUB v776, v792
    0x797: v797(0x64) = CONST 
    0x799: v799(0x64) = ADD v797(0x64), v796(0x0)
    0x79b: REVERT v792, v799(0x64)

    Begin block 0x79c
    prev=[0x76c], succ=[0x7c0, 0x7c9]
    =================================
    0x79d: v79d(0x40) = CONST 
    0x79f: v79f = MLOAD v79d(0x40)
    0x7a0: v7a0 = CALLER 
    0x7a3: v7a3 = ISZERO v72a_0
    0x7a4: v7a4(0x8fc) = CONST 
    0x7a7: v7a7 = MUL v7a4(0x8fc), v7a3
    0x7ab: v7ab(0x0) = CONST 
    0x7b3: v7b3 = CALL v7a7, v7a0, v72a_0, v79f, v7ab(0x0), v79f, v7ab(0x0)
    0x7b9: v7b9 = ISZERO v7b3
    0x7bb: v7bb = ISZERO v7b9
    0x7bc: v7bc(0x7c9) = CONST 
    0x7bf: JUMPI v7bc(0x7c9), v7bb

    Begin block 0x7c0
    prev=[0x79c], succ=[]
    =================================
    0x7c0: v7c0 = RETURNDATASIZE 
    0x7c1: v7c1(0x0) = CONST 
    0x7c4: RETURNDATACOPY v7c1(0x0), v7c1(0x0), v7c0
    0x7c5: v7c5 = RETURNDATASIZE 
    0x7c6: v7c6(0x0) = CONST 
    0x7c8: REVERT v7c6(0x0), v7c5

    Begin block 0x7c9
    prev=[0x79c], succ=[0x7dd]
    =================================
    0x7cb: v7cb(0x6) = CONST 
    0x7cd: v7cd = SLOAD v7cb(0x6)
    0x7ce: v7ce(0x7dd) = CONST 
    0x7d3: v7d3(0xffffffff) = CONST 
    0x7d8: v7d8(0x1010) = CONST 
    0x7db: v7db(0x1010) = AND v7d8(0x1010), v7d3(0xffffffff)
    0x7dc: v7dc_0 = CALLPRIVATE v7db(0x1010), v72a_0, v7cd, v7ce(0x7dd)

    Begin block 0x7dd
    prev=[0x7c9], succ=[0x1182]
    =================================
    0x7de: v7de(0x6) = CONST 
    0x7e0: SSTORE v7de(0x6), v7dc_0
    0x7e1: v7e1(0x7ea) = CONST 
    0x7e4: v7e4 = CALLER 
    0x7e6: v7e6(0x1182) = CONST 
    0x7e9: JUMP v7e6(0x1182)

    Begin block 0x1182
    prev=[0x7dd], succ=[0x1193, 0x1208]
    =================================
    0x1183: v1183(0x1) = CONST 
    0x1185: v1185(0xa0) = CONST 
    0x1187: v1187(0x2) = CONST 
    0x1189: v1189(0x10000000000000000000000000000000000000000) = EXP v1187(0x2), v1185(0xa0)
    0x118a: v118a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1189(0x10000000000000000000000000000000000000000), v1183(0x1)
    0x118c: v118c = AND v7e4, v118a(0xffffffffffffffffffffffffffffffffffffffff)
    0x118d: v118d = ISZERO v118c
    0x118e: v118e = ISZERO v118d
    0x118f: v118f(0x1208) = CONST 
    0x1192: JUMPI v118f(0x1208), v118e

    Begin block 0x1193
    prev=[0x1182], succ=[]
    =================================
    0x1193: v1193(0x40) = CONST 
    0x1196: v1196 = MLOAD v1193(0x40)
    0x1197: v1197(0xe5) = CONST 
    0x1199: v1199(0x2) = CONST 
    0x119b: v119b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1199(0x2), v1197(0xe5)
    0x119c: v119c(0x461bcd) = CONST 
    0x11a0: v11a0(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v119c(0x461bcd), v119b(0x2000000000000000000000000000000000000000000000000000000000)
    0x11a2: MSTORE v1196, v11a0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11a3: v11a3(0x20) = CONST 
    0x11a5: v11a5(0x4) = CONST 
    0x11a8: v11a8 = ADD v1196, v11a5(0x4)
    0x11a9: MSTORE v11a8, v11a3(0x20)
    0x11aa: v11aa(0x21) = CONST 
    0x11ac: v11ac(0x24) = CONST 
    0x11af: v11af = ADD v1196, v11ac(0x24)
    0x11b0: MSTORE v11af, v11aa(0x21)
    0x11b1: v11b1(0x45524332303a206275726e2066726f6d20746865207a65726f20616464726573) = CONST 
    0x11d2: v11d2(0x44) = CONST 
    0x11d5: v11d5 = ADD v1196, v11d2(0x44)
    0x11d6: MSTORE v11d5, v11b1(0x45524332303a206275726e2066726f6d20746865207a65726f20616464726573)
    0x11d7: v11d7(0x7300000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11f8: v11f8(0x64) = CONST 
    0x11fb: v11fb = ADD v1196, v11f8(0x64)
    0x11fc: MSTORE v11fb, v11d7(0x7300000000000000000000000000000000000000000000000000000000000000)
    0x11fe: v11fe = MLOAD v1193(0x40)
    0x1202: v1202(0x0) = SUB v1196, v11fe
    0x1203: v1203(0x84) = CONST 
    0x1205: v1205(0x84) = ADD v1203(0x84), v1202(0x0)
    0x1207: REVERT v11fe, v1205(0x84)

    Begin block 0x1208
    prev=[0x1182], succ=[0x1229, 0x122d]
    =================================
    0x1209: v1209(0x1) = CONST 
    0x120b: v120b(0xa0) = CONST 
    0x120d: v120d(0x2) = CONST 
    0x120f: v120f(0x10000000000000000000000000000000000000000) = EXP v120d(0x2), v120b(0xa0)
    0x1210: v1210(0xffffffffffffffffffffffffffffffffffffffff) = SUB v120f(0x10000000000000000000000000000000000000000), v1209(0x1)
    0x1212: v1212 = AND v7e4, v1210(0xffffffffffffffffffffffffffffffffffffffff)
    0x1213: v1213(0x0) = CONST 
    0x1217: MSTORE v1213(0x0), v1212
    0x1218: v1218(0x1) = CONST 
    0x121a: v121a(0x20) = CONST 
    0x121c: MSTORE v121a(0x20), v1218(0x1)
    0x121d: v121d(0x40) = CONST 
    0x1220: v1220 = SHA3 v1213(0x0), v121d(0x40)
    0x1221: v1221 = SLOAD v1220
    0x1223: v1223 = GT v2e2, v1221
    0x1224: v1224 = ISZERO v1223
    0x1225: v1225(0x122d) = CONST 
    0x1228: JUMPI v1225(0x122d), v1224

    Begin block 0x1229
    prev=[0x1208], succ=[]
    =================================
    0x1229: v1229(0x0) = CONST 
    0x122c: REVERT v1229(0x0), v1229(0x0)

    Begin block 0x122d
    prev=[0x1208], succ=[0x1240]
    =================================
    0x122e: v122e(0x3) = CONST 
    0x1230: v1230 = SLOAD v122e(0x3)
    0x1231: v1231(0x1240) = CONST 
    0x1236: v1236(0xffffffff) = CONST 
    0x123b: v123b(0x1010) = CONST 
    0x123e: v123e(0x1010) = AND v123b(0x1010), v1236(0xffffffff)
    0x123f: v123f_0 = CALLPRIVATE v123e(0x1010), v2e2, v1230, v1231(0x1240)

    Begin block 0x1240
    prev=[0x122d], succ=[0x126c]
    =================================
    0x1241: v1241(0x3) = CONST 
    0x1243: SSTORE v1241(0x3), v123f_0
    0x1244: v1244(0x1) = CONST 
    0x1246: v1246(0xa0) = CONST 
    0x1248: v1248(0x2) = CONST 
    0x124a: v124a(0x10000000000000000000000000000000000000000) = EXP v1248(0x2), v1246(0xa0)
    0x124b: v124b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v124a(0x10000000000000000000000000000000000000000), v1244(0x1)
    0x124d: v124d = AND v7e4, v124b(0xffffffffffffffffffffffffffffffffffffffff)
    0x124e: v124e(0x0) = CONST 
    0x1252: MSTORE v124e(0x0), v124d
    0x1253: v1253(0x1) = CONST 
    0x1255: v1255(0x20) = CONST 
    0x1257: MSTORE v1255(0x20), v1253(0x1)
    0x1258: v1258(0x40) = CONST 
    0x125b: v125b = SHA3 v124e(0x0), v1258(0x40)
    0x125c: v125c = SLOAD v125b
    0x125d: v125d(0x126c) = CONST 
    0x1262: v1262(0xffffffff) = CONST 
    0x1267: v1267(0x1010) = CONST 
    0x126a: v126a(0x1010) = AND v1267(0x1010), v1262(0xffffffff)
    0x126b: v126b_0 = CALLPRIVATE v126a(0x1010), v2e2, v125c, v125d(0x126c)

    Begin block 0x126c
    prev=[0x1240], succ=[0x7ea]
    =================================
    0x126d: v126d(0x1) = CONST 
    0x126f: v126f(0xa0) = CONST 
    0x1271: v1271(0x2) = CONST 
    0x1273: v1273(0x10000000000000000000000000000000000000000) = EXP v1271(0x2), v126f(0xa0)
    0x1274: v1274(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1273(0x10000000000000000000000000000000000000000), v126d(0x1)
    0x1276: v1276 = AND v7e4, v1274(0xffffffffffffffffffffffffffffffffffffffff)
    0x1277: v1277(0x0) = CONST 
    0x127b: MSTORE v1277(0x0), v1276
    0x127c: v127c(0x1) = CONST 
    0x127e: v127e(0x20) = CONST 
    0x1282: MSTORE v127e(0x20), v127c(0x1)
    0x1283: v1283(0x40) = CONST 
    0x1287: v1287 = SHA3 v1277(0x0), v1283(0x40)
    0x128b: SSTORE v1287, v126b_0
    0x128d: v128d = MLOAD v1283(0x40)
    0x1290: MSTORE v128d, v2e2
    0x1292: v1292 = MLOAD v1283(0x40)
    0x1295: v1295(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x12ba: v12ba(0x0) = SUB v128d, v1292
    0x12bd: v12bd(0x20) = ADD v127e(0x20), v12ba(0x0)
    0x12bf: LOG3 v1292, v12bd(0x20), v1295(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1276, v1277(0x0)
    0x12c2: JUMP v7e1(0x7ea)

    Begin block 0x7ea
    prev=[0x126c], succ=[0xcfcd]
    =================================
    0x7eb: v7eb(0x40) = CONST 
    0x7ee: v7ee = MLOAD v7eb(0x40)
    0x7f1: MSTORE v7ee, v2e2
    0x7f3: v7f3 = MLOAD v7eb(0x40)
    0x7f4: v7f4 = CALLER 
    0x7f6: v7f6(0xa2bd9fcfcdba69f52bcd9a520846ad4bd685b187483f53efc42d035b2ddebff0) = CONST 
    0x81b: v81b(0x0) = SUB v7ee, v7f3
    0x81c: v81c(0x20) = CONST 
    0x81e: v81e(0x20) = ADD v81c(0x20), v81b(0x0)
    0x820: LOG2 v7f3, v81e(0x20), v7f6(0xa2bd9fcfcdba69f52bcd9a520846ad4bd685b187483f53efc42d035b2ddebff0), v7f4
    0x823: JUMP v2cb(0xcfcd)

    Begin block 0xcfcd
    prev=[0x7ea], succ=[]
    =================================
    0xcfce: STOP 

}

function decimals()() public {
    Begin block 0x2e7
    prev=[], succ=[0x2ef, 0x2f3]
    =================================
    0x2e8: v2e8 = CALLVALUE 
    0x2ea: v2ea = ISZERO v2e8
    0x2eb: v2eb(0x2f3) = CONST 
    0x2ee: JUMPI v2eb(0x2f3), v2ea

    Begin block 0x2ef
    prev=[0x2e7], succ=[]
    =================================
    0x2ef: v2ef(0x0) = CONST 
    0x2f2: REVERT v2ef(0x0), v2ef(0x0)

    Begin block 0x2f3
    prev=[0x2e7], succ=[0x824]
    =================================
    0x2f5: v2f5(0x2fc) = CONST 
    0x2f8: v2f8(0x824) = CONST 
    0x2fb: JUMP v2f8(0x824)

    Begin block 0x824
    prev=[0x2f3], succ=[0x2fc]
    =================================
    0x825: v825(0xc) = CONST 
    0x827: v827 = SLOAD v825(0xc)
    0x828: v828(0xff) = CONST 
    0x82a: v82a = AND v828(0xff), v827
    0x82c: JUMP v2f5(0x2fc)

    Begin block 0x2fc
    prev=[0x824], succ=[]
    =================================
    0x2fd: v2fd(0x40) = CONST 
    0x300: v300 = MLOAD v2fd(0x40)
    0x301: v301(0xff) = CONST 
    0x305: v305 = AND v82a, v301(0xff)
    0x307: MSTORE v300, v305
    0x308: v308 = MLOAD v2fd(0x40)
    0x30c: v30c(0x0) = SUB v300, v308
    0x30d: v30d(0x20) = CONST 
    0x30f: v30f(0x20) = ADD v30d(0x20), v30c(0x0)
    0x311: RETURN v308, v30f(0x20)

}

function loan(uint256)() public {
    Begin block 0x312
    prev=[], succ=[0x31a, 0x31e]
    =================================
    0x313: v313 = CALLVALUE 
    0x315: v315 = ISZERO v313
    0x316: v316(0x31e) = CONST 
    0x319: JUMPI v316(0x31e), v315

    Begin block 0x31a
    prev=[0x312], succ=[]
    =================================
    0x31a: v31a(0x0) = CONST 
    0x31d: REVERT v31a(0x0), v31a(0x0)

    Begin block 0x31e
    prev=[0x312], succ=[0x331, 0x335]
    =================================
    0x320: v320(0xcfee) = CONST 
    0x323: v323(0x4) = CONST 
    0x326: v326 = CALLDATASIZE 
    0x327: v327 = SUB v326, v323(0x4)
    0x328: v328(0x20) = CONST 
    0x32b: v32b = LT v327, v328(0x20)
    0x32c: v32c = ISZERO v32b
    0x32d: v32d(0x335) = CONST 
    0x330: JUMPI v32d(0x335), v32c

    Begin block 0x331
    prev=[0x31e], succ=[]
    =================================
    0x331: v331(0x0) = CONST 
    0x334: REVERT v331(0x0), v331(0x0)

    Begin block 0x335
    prev=[0x31e], succ=[0x82d]
    =================================
    0x337: v337 = CALLDATALOAD v323(0x4)
    0x338: v338(0x82d) = CONST 
    0x33b: JUMP v338(0x82d)

    Begin block 0x82d
    prev=[0x335], succ=[0x840, 0x869]
    =================================
    0x82e: v82e(0x9) = CONST 
    0x830: v830 = SLOAD v82e(0x9)
    0x831: v831(0x1) = CONST 
    0x833: v833(0xa0) = CONST 
    0x835: v835(0x2) = CONST 
    0x837: v837(0x10000000000000000000000000000000000000000) = EXP v835(0x2), v833(0xa0)
    0x838: v838(0xffffffffffffffffffffffffffffffffffffffff) = SUB v837(0x10000000000000000000000000000000000000000), v831(0x1)
    0x839: v839 = AND v838(0xffffffffffffffffffffffffffffffffffffffff), v830
    0x83a: v83a = CALLER 
    0x83b: v83b = EQ v83a, v839
    0x83c: v83c(0x869) = CONST 
    0x83f: JUMPI v83c(0x869), v83b

    Begin block 0x840
    prev=[0x82d], succ=[]
    =================================
    0x840: v840(0x40) = CONST 
    0x843: v843 = MLOAD v840(0x40)
    0x844: v844(0xe5) = CONST 
    0x846: v846(0x2) = CONST 
    0x848: v848(0x2000000000000000000000000000000000000000000000000000000000) = EXP v846(0x2), v844(0xe5)
    0x849: v849(0x461bcd) = CONST 
    0x84d: v84d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v849(0x461bcd), v848(0x2000000000000000000000000000000000000000000000000000000000)
    0x84f: MSTORE v843, v84d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x850: v850(0x20) = CONST 
    0x852: v852(0x4) = CONST 
    0x855: v855 = ADD v843, v852(0x4)
    0x856: MSTORE v855, v850(0x20)
    0x857: v857(0x0) = CONST 
    0x859: v859(0x24) = CONST 
    0x85c: v85c = ADD v843, v859(0x24)
    0x85d: MSTORE v85c, v857(0x0)
    0x85f: v85f = MLOAD v840(0x40)
    0x863: v863(0x0) = SUB v843, v85f
    0x864: v864(0x64) = CONST 
    0x866: v866(0x64) = ADD v864(0x64), v863(0x0)
    0x868: REVERT v85f, v866(0x64)

    Begin block 0x869
    prev=[0x82d], succ=[0x874, 0x89d]
    =================================
    0x86a: v86a(0x5) = CONST 
    0x86c: v86c = SLOAD v86a(0x5)
    0x86e: v86e = GT v337, v86c
    0x86f: v86f = ISZERO v86e
    0x870: v870(0x89d) = CONST 
    0x873: JUMPI v870(0x89d), v86f

    Begin block 0x874
    prev=[0x869], succ=[]
    =================================
    0x874: v874(0x40) = CONST 
    0x877: v877 = MLOAD v874(0x40)
    0x878: v878(0xe5) = CONST 
    0x87a: v87a(0x2) = CONST 
    0x87c: v87c(0x2000000000000000000000000000000000000000000000000000000000) = EXP v87a(0x2), v878(0xe5)
    0x87d: v87d(0x461bcd) = CONST 
    0x881: v881(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v87d(0x461bcd), v87c(0x2000000000000000000000000000000000000000000000000000000000)
    0x883: MSTORE v877, v881(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x884: v884(0x20) = CONST 
    0x886: v886(0x4) = CONST 
    0x889: v889 = ADD v877, v886(0x4)
    0x88a: MSTORE v889, v884(0x20)
    0x88b: v88b(0x0) = CONST 
    0x88d: v88d(0x24) = CONST 
    0x890: v890 = ADD v877, v88d(0x24)
    0x891: MSTORE v890, v88b(0x0)
    0x893: v893 = MLOAD v874(0x40)
    0x897: v897(0x0) = SUB v877, v893
    0x898: v898(0x64) = CONST 
    0x89a: v89a(0x64) = ADD v898(0x64), v897(0x0)
    0x89c: REVERT v893, v89a(0x64)

    Begin block 0x89d
    prev=[0x869], succ=[0x8ce, 0x8d7]
    =================================
    0x89e: v89e(0x9) = CONST 
    0x8a0: v8a0 = SLOAD v89e(0x9)
    0x8a1: v8a1(0x40) = CONST 
    0x8a3: v8a3 = MLOAD v8a1(0x40)
    0x8a4: v8a4(0x1) = CONST 
    0x8a6: v8a6(0xa0) = CONST 
    0x8a8: v8a8(0x2) = CONST 
    0x8aa: v8aa(0x10000000000000000000000000000000000000000) = EXP v8a8(0x2), v8a6(0xa0)
    0x8ab: v8ab(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8aa(0x10000000000000000000000000000000000000000), v8a4(0x1)
    0x8ae: v8ae = AND v8a0, v8ab(0xffffffffffffffffffffffffffffffffffffffff)
    0x8b1: v8b1 = ISZERO v337
    0x8b2: v8b2(0x8fc) = CONST 
    0x8b5: v8b5 = MUL v8b2(0x8fc), v8b1
    0x8b9: v8b9(0x0) = CONST 
    0x8c1: v8c1 = CALL v8b5, v8ae, v337, v8a3, v8b9(0x0), v8a3, v8b9(0x0)
    0x8c7: v8c7 = ISZERO v8c1
    0x8c9: v8c9 = ISZERO v8c7
    0x8ca: v8ca(0x8d7) = CONST 
    0x8cd: JUMPI v8ca(0x8d7), v8c9

    Begin block 0x8ce
    prev=[0x89d], succ=[]
    =================================
    0x8ce: v8ce = RETURNDATASIZE 
    0x8cf: v8cf(0x0) = CONST 
    0x8d2: RETURNDATACOPY v8cf(0x0), v8cf(0x0), v8ce
    0x8d3: v8d3 = RETURNDATASIZE 
    0x8d4: v8d4(0x0) = CONST 
    0x8d6: REVERT v8d4(0x0), v8d3

    Begin block 0x8d7
    prev=[0x89d], succ=[0x8eb]
    =================================
    0x8d9: v8d9(0x5) = CONST 
    0x8db: v8db = SLOAD v8d9(0x5)
    0x8dc: v8dc(0x8eb) = CONST 
    0x8e1: v8e1(0xffffffff) = CONST 
    0x8e6: v8e6(0x1010) = CONST 
    0x8e9: v8e9(0x1010) = AND v8e6(0x1010), v8e1(0xffffffff)
    0x8ea: v8ea_0 = CALLPRIVATE v8e9(0x1010), v337, v8db, v8dc(0x8eb)

    Begin block 0x8eb
    prev=[0x8d7], succ=[0xcfee]
    =================================
    0x8ec: v8ec(0x5) = CONST 
    0x8ee: SSTORE v8ec(0x5), v8ea_0
    0x8ef: v8ef(0x9) = CONST 
    0x8f1: v8f1 = SLOAD v8ef(0x9)
    0x8f2: v8f2(0x40) = CONST 
    0x8f5: v8f5 = MLOAD v8f2(0x40)
    0x8f8: MSTORE v8f5, v337
    0x8fa: v8fa = MLOAD v8f2(0x40)
    0x8fb: v8fb(0x1) = CONST 
    0x8fd: v8fd(0xa0) = CONST 
    0x8ff: v8ff(0x2) = CONST 
    0x901: v901(0x10000000000000000000000000000000000000000) = EXP v8ff(0x2), v8fd(0xa0)
    0x902: v902(0xffffffffffffffffffffffffffffffffffffffff) = SUB v901(0x10000000000000000000000000000000000000000), v8fb(0x1)
    0x905: v905 = AND v8f1, v902(0xffffffffffffffffffffffffffffffffffffffff)
    0x907: v907(0x1db23cf53464267c45324569941e81e23d29c48ff9be2b35af2cc0a2681159d6) = CONST 
    0x92b: v92b(0x0) = SUB v8f5, v8fa
    0x92c: v92c(0x20) = CONST 
    0x92e: v92e(0x20) = ADD v92c(0x20), v92b(0x0)
    0x930: LOG2 v8fa, v92e(0x20), v907(0x1db23cf53464267c45324569941e81e23d29c48ff9be2b35af2cc0a2681159d6), v905
    0x932: JUMP v320(0xcfee)

    Begin block 0xcfee
    prev=[0x8eb], succ=[]
    =================================
    0xcfef: STOP 

}

function increaseAllowance(address,uint256)() public {
    Begin block 0x33c
    prev=[], succ=[0x344, 0x348]
    =================================
    0x33d: v33d = CALLVALUE 
    0x33f: v33f = ISZERO v33d
    0x340: v340(0x348) = CONST 
    0x343: JUMPI v340(0x348), v33f

    Begin block 0x344
    prev=[0x33c], succ=[]
    =================================
    0x344: v344(0x0) = CONST 
    0x347: REVERT v344(0x0), v344(0x0)

    Begin block 0x348
    prev=[0x33c], succ=[0x35b, 0x35f]
    =================================
    0x34a: v34a(0xd00f) = CONST 
    0x34d: v34d(0x4) = CONST 
    0x350: v350 = CALLDATASIZE 
    0x351: v351 = SUB v350, v34d(0x4)
    0x352: v352(0x40) = CONST 
    0x355: v355 = LT v351, v352(0x40)
    0x356: v356 = ISZERO v355
    0x357: v357(0x35f) = CONST 
    0x35a: JUMPI v357(0x35f), v356

    Begin block 0x35b
    prev=[0x348], succ=[]
    =================================
    0x35b: v35b(0x0) = CONST 
    0x35e: REVERT v35b(0x0), v35b(0x0)

    Begin block 0x35f
    prev=[0x348], succ=[0x933B0x35f]
    =================================
    0x361: v361(0x1) = CONST 
    0x363: v363(0xa0) = CONST 
    0x365: v365(0x2) = CONST 
    0x367: v367(0x10000000000000000000000000000000000000000) = EXP v365(0x2), v363(0xa0)
    0x368: v368(0xffffffffffffffffffffffffffffffffffffffff) = SUB v367(0x10000000000000000000000000000000000000000), v361(0x1)
    0x36a: v36a = CALLDATALOAD v34d(0x4)
    0x36b: v36b = AND v36a, v368(0xffffffffffffffffffffffffffffffffffffffff)
    0x36d: v36d(0x20) = CONST 
    0x36f: v36f(0x24) = ADD v36d(0x20), v34d(0x4)
    0x370: v370 = CALLDATALOAD v36f(0x24)
    0x371: v371(0x933) = CONST 
    0x374: JUMP v371(0x933)

    Begin block 0x933B0x35f
    prev=[0x35f], succ=[0x195feB0x35f]
    =================================
    0x934S0x35f: v934V35f = CALLER 
    0x935S0x35f: v935V35f(0x0) = CONST 
    0x939S0x35f: MSTORE v935V35f(0x0), v934V35f
    0x93aS0x35f: v93aV35f(0x2) = CONST 
    0x93cS0x35f: v93cV35f(0x20) = CONST 
    0x940S0x35f: MSTORE v93cV35f(0x20), v93aV35f(0x2)
    0x941S0x35f: v941V35f(0x40) = CONST 
    0x945S0x35f: v945V35f = SHA3 v935V35f(0x0), v941V35f(0x40)
    0x946S0x35f: v946V35f(0x1) = CONST 
    0x948S0x35f: v948V35f(0xa0) = CONST 
    0x94aS0x35f: v94aV35f(0x2) = CONST 
    0x94cS0x35f: v94cV35f(0x10000000000000000000000000000000000000000) = EXP v94aV35f(0x2), v948V35f(0xa0)
    0x94dS0x35f: v94dV35f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v94cV35f(0x10000000000000000000000000000000000000000), v946V35f(0x1)
    0x94fS0x35f: v94fV35f = AND v36b, v94dV35f(0xffffffffffffffffffffffffffffffffffffffff)
    0x951S0x35f: MSTORE v935V35f(0x0), v94fV35f
    0x954S0x35f: MSTORE v93cV35f(0x20), v945V35f
    0x956S0x35f: v956V35f = SHA3 v935V35f(0x0), v941V35f(0x40)
    0x957S0x35f: v957V35f = SLOAD v956V35f
    0x95aS0x35f: v95aV35f(0x14980) = CONST 
    0x960S0x35f: v960V35f(0x195fe) = CONST 
    0x965S0x35f: v965V35f(0xffffffff) = CONST 
    0x96aS0x35f: v96aV35f(0x12c3) = CONST 
    0x96dS0x35f: v96dV35f(0x12c3) = AND v96aV35f(0x12c3), v965V35f(0xffffffff)
    0x96eS0x35f: v96e_0V35f = CALLPRIVATE v96dV35f(0x12c3), v370, v957V35f, v960V35f(0x195fe)

    Begin block 0x195feB0x35f
    prev=[0x933B0x35f], succ=[0x14980B0x35f]
    =================================
    0x195ffS0x35f: v195ffV35f(0xcdd) = CONST 
    0x19602S0x35f: CALLPRIVATE v195ffV35f(0xcdd), v96e_0V35f, v36b, v934V35f, v95aV35f(0x14980)

    Begin block 0x14980B0x35f
    prev=[0x195feB0x35f], succ=[0x23078B0x35f]
    =================================
    0x14982S0x35f: v14982V35f(0x1) = CONST 
    0x195beS0x35f: v195beV35f(0x23078) = CONST 
    0x195deS0x35f: JUMP v195beV35f(0x23078)

    Begin block 0x23078B0x35f
    prev=[0x14980B0x35f], succ=[0xd00f]
    =================================
    0x2307dS0x35f: JUMP v34a(0xd00f)

    Begin block 0xd00f
    prev=[0x23078B0x35f], succ=[]
    =================================
    0xd010: vd010(0x40) = CONST 
    0xd013: vd013 = MLOAD vd010(0x40)
    0xd015: vd015(0x0) = ISZERO v14982V35f(0x1)
    0xd016: vd016(0x1) = ISZERO vd015(0x0)
    0xd018: MSTORE vd013, vd016(0x1)
    0xd019: vd019 = MLOAD vd010(0x40)
    0xd01d: vd01d(0x0) = SUB vd013, vd019
    0xd01e: vd01e(0x20) = CONST 
    0xd020: vd020(0x20) = ADD vd01e(0x20), vd01d(0x0)
    0xd022: RETURN vd019, vd020(0x20)

}

function totalInvested()() public {
    Begin block 0x375
    prev=[], succ=[0x37d, 0x381]
    =================================
    0x376: v376 = CALLVALUE 
    0x378: v378 = ISZERO v376
    0x379: v379(0x381) = CONST 
    0x37c: JUMPI v379(0x381), v378

    Begin block 0x37d
    prev=[0x375], succ=[]
    =================================
    0x37d: v37d(0x0) = CONST 
    0x380: REVERT v37d(0x0), v37d(0x0)

    Begin block 0x381
    prev=[0x375], succ=[0x96f]
    =================================
    0x383: v383(0xd042) = CONST 
    0x386: v386(0x96f) = CONST 
    0x389: JUMP v386(0x96f)

    Begin block 0x96f
    prev=[0x381], succ=[0xd042]
    =================================
    0x970: v970(0x8) = CONST 
    0x972: v972 = SLOAD v970(0x8)
    0x974: JUMP v383(0xd042)

    Begin block 0xd042
    prev=[0x96f], succ=[]
    =================================
    0xd043: vd043(0x40) = CONST 
    0xd046: vd046 = MLOAD vd043(0x40)
    0xd049: MSTORE vd046, v972
    0xd04a: vd04a = MLOAD vd043(0x40)
    0xd04e: vd04e(0x0) = SUB vd046, vd04a
    0xd04f: vd04f(0x20) = CONST 
    0xd051: vd051(0x20) = ADD vd04f(0x20), vd04e(0x0)
    0xd053: RETURN vd04a, vd051(0x20)

}

function balanceOf(address)() public {
    Begin block 0x38a
    prev=[], succ=[0x392, 0x396]
    =================================
    0x38b: v38b = CALLVALUE 
    0x38d: v38d = ISZERO v38b
    0x38e: v38e(0x396) = CONST 
    0x391: JUMPI v38e(0x396), v38d

    Begin block 0x392
    prev=[0x38a], succ=[]
    =================================
    0x392: v392(0x0) = CONST 
    0x395: REVERT v392(0x0), v392(0x0)

    Begin block 0x396
    prev=[0x38a], succ=[0x3a9, 0x3ad]
    =================================
    0x398: v398(0xd073) = CONST 
    0x39b: v39b(0x4) = CONST 
    0x39e: v39e = CALLDATASIZE 
    0x39f: v39f = SUB v39e, v39b(0x4)
    0x3a0: v3a0(0x20) = CONST 
    0x3a3: v3a3 = LT v39f, v3a0(0x20)
    0x3a4: v3a4 = ISZERO v3a3
    0x3a5: v3a5(0x3ad) = CONST 
    0x3a8: JUMPI v3a5(0x3ad), v3a4

    Begin block 0x3a9
    prev=[0x396], succ=[]
    =================================
    0x3a9: v3a9(0x0) = CONST 
    0x3ac: REVERT v3a9(0x0), v3a9(0x0)

    Begin block 0x3ad
    prev=[0x396], succ=[0x975B0x3ad]
    =================================
    0x3af: v3af = CALLDATALOAD v39b(0x4)
    0x3b0: v3b0(0x1) = CONST 
    0x3b2: v3b2(0xa0) = CONST 
    0x3b4: v3b4(0x2) = CONST 
    0x3b6: v3b6(0x10000000000000000000000000000000000000000) = EXP v3b4(0x2), v3b2(0xa0)
    0x3b7: v3b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b6(0x10000000000000000000000000000000000000000), v3b0(0x1)
    0x3b8: v3b8 = AND v3b7(0xffffffffffffffffffffffffffffffffffffffff), v3af
    0x3b9: v3b9(0x975) = CONST 
    0x3bc: JUMP v3b9(0x975)

    Begin block 0x975B0x3ad
    prev=[0x3ad], succ=[0xd073]
    =================================
    0x976S0x3ad: v976V3ad(0x1) = CONST 
    0x978S0x3ad: v978V3ad(0xa0) = CONST 
    0x97aS0x3ad: v97aV3ad(0x2) = CONST 
    0x97cS0x3ad: v97cV3ad(0x10000000000000000000000000000000000000000) = EXP v97aV3ad(0x2), v978V3ad(0xa0)
    0x97dS0x3ad: v97dV3ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97cV3ad(0x10000000000000000000000000000000000000000), v976V3ad(0x1)
    0x97eS0x3ad: v97eV3ad = AND v97dV3ad(0xffffffffffffffffffffffffffffffffffffffff), v3b8
    0x97fS0x3ad: v97fV3ad(0x0) = CONST 
    0x983S0x3ad: MSTORE v97fV3ad(0x0), v97eV3ad
    0x984S0x3ad: v984V3ad(0x1) = CONST 
    0x986S0x3ad: v986V3ad(0x20) = CONST 
    0x988S0x3ad: MSTORE v986V3ad(0x20), v984V3ad(0x1)
    0x989S0x3ad: v989V3ad(0x40) = CONST 
    0x98cS0x3ad: v98cV3ad = SHA3 v97fV3ad(0x0), v989V3ad(0x40)
    0x98dS0x3ad: v98dV3ad = SLOAD v98cV3ad
    0x98fS0x3ad: JUMP v398(0xd073)

    Begin block 0xd073
    prev=[0x975B0x3ad], succ=[]
    =================================
    0xd074: vd074(0x40) = CONST 
    0xd077: vd077 = MLOAD vd074(0x40)
    0xd07a: MSTORE vd077, v98dV3ad
    0xd07b: vd07b = MLOAD vd074(0x40)
    0xd07f: vd07f(0x0) = SUB vd077, vd07b
    0xd080: vd080(0x20) = CONST 
    0xd082: vd082(0x20) = ADD vd080(0x20), vd07f(0x0)
    0xd084: RETURN vd07b, vd082(0x20)

}

function renounceOwnership()() public {
    Begin block 0x3bd
    prev=[], succ=[0x3c5, 0x3c9]
    =================================
    0x3be: v3be = CALLVALUE 
    0x3c0: v3c0 = ISZERO v3be
    0x3c1: v3c1(0x3c9) = CONST 
    0x3c4: JUMPI v3c1(0x3c9), v3c0

    Begin block 0x3c5
    prev=[0x3bd], succ=[]
    =================================
    0x3c5: v3c5(0x0) = CONST 
    0x3c8: REVERT v3c5(0x0), v3c5(0x0)

    Begin block 0x3c9
    prev=[0x3bd], succ=[0x990]
    =================================
    0x3cb: v3cb(0xd0a4) = CONST 
    0x3ce: v3ce(0x990) = CONST 
    0x3d1: JUMP v3ce(0x990)

    Begin block 0x990
    prev=[0x3c9], succ=[0xa75B0x990]
    =================================
    0x991: v991(0x998) = CONST 
    0x994: v994(0xa75) = CONST 
    0x997: JUMP v994(0xa75)

    Begin block 0xa75B0x990
    prev=[0x990], succ=[0x998]
    =================================
    0xa76S0x990: va76V990(0x0) = CONST 
    0xa78S0x990: va78V990 = SLOAD va76V990(0x0)
    0xa79S0x990: va79V990(0x1) = CONST 
    0xa7bS0x990: va7bV990(0xa0) = CONST 
    0xa7dS0x990: va7dV990(0x2) = CONST 
    0xa7fS0x990: va7fV990(0x10000000000000000000000000000000000000000) = EXP va7dV990(0x2), va7bV990(0xa0)
    0xa80S0x990: va80V990(0xffffffffffffffffffffffffffffffffffffffff) = SUB va7fV990(0x10000000000000000000000000000000000000000), va79V990(0x1)
    0xa81S0x990: va81V990 = AND va80V990(0xffffffffffffffffffffffffffffffffffffffff), va78V990
    0xa82S0x990: va82V990 = CALLER 
    0xa83S0x990: va83V990 = EQ va82V990, va81V990
    0xa85S0x990: JUMP v991(0x998)

    Begin block 0x998
    prev=[0xa75B0x990], succ=[0x99f, 0x9ee]
    =================================
    0x999: v999 = ISZERO va83V990
    0x99a: v99a = ISZERO v999
    0x99b: v99b(0x9ee) = CONST 
    0x99e: JUMPI v99b(0x9ee), v99a

    Begin block 0x99f
    prev=[0x998], succ=[]
    =================================
    0x99f: v99f(0x40) = CONST 
    0x9a2: v9a2 = MLOAD v99f(0x40)
    0x9a3: v9a3(0xe5) = CONST 
    0x9a5: v9a5(0x2) = CONST 
    0x9a7: v9a7(0x2000000000000000000000000000000000000000000000000000000000) = EXP v9a5(0x2), v9a3(0xe5)
    0x9a8: v9a8(0x461bcd) = CONST 
    0x9ac: v9ac(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v9a8(0x461bcd), v9a7(0x2000000000000000000000000000000000000000000000000000000000)
    0x9ae: MSTORE v9a2, v9ac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9af: v9af(0x20) = CONST 
    0x9b1: v9b1(0x4) = CONST 
    0x9b4: v9b4 = ADD v9a2, v9b1(0x4)
    0x9b7: MSTORE v9b4, v9af(0x20)
    0x9b8: v9b8(0x24) = CONST 
    0x9bb: v9bb = ADD v9a2, v9b8(0x24)
    0x9bc: MSTORE v9bb, v9af(0x20)
    0x9bd: v9bd(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x9de: v9de(0x44) = CONST 
    0x9e1: v9e1 = ADD v9a2, v9de(0x44)
    0x9e2: MSTORE v9e1, v9bd(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x9e4: v9e4 = MLOAD v99f(0x40)
    0x9e8: v9e8(0x0) = SUB v9a2, v9e4
    0x9e9: v9e9(0x64) = CONST 
    0x9eb: v9eb(0x64) = ADD v9e9(0x64), v9e8(0x0)
    0x9ed: REVERT v9e4, v9eb(0x64)

    Begin block 0x9ee
    prev=[0x998], succ=[0xd0a4]
    =================================
    0x9ef: v9ef(0x0) = CONST 
    0x9f2: v9f2 = SLOAD v9ef(0x0)
    0x9f3: v9f3(0x40) = CONST 
    0x9f5: v9f5 = MLOAD v9f3(0x40)
    0x9f6: v9f6(0x1) = CONST 
    0x9f8: v9f8(0xa0) = CONST 
    0x9fa: v9fa(0x2) = CONST 
    0x9fc: v9fc(0x10000000000000000000000000000000000000000) = EXP v9fa(0x2), v9f8(0xa0)
    0x9fd: v9fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9fc(0x10000000000000000000000000000000000000000), v9f6(0x1)
    0xa00: va00 = AND v9f2, v9fd(0xffffffffffffffffffffffffffffffffffffffff)
    0xa02: va02(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xa26: LOG3 v9f5, v9ef(0x0), va02(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), va00, v9ef(0x0)
    0xa27: va27(0x0) = CONST 
    0xa2a: va2a = SLOAD va27(0x0)
    0xa2b: va2b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa40: va40(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va2b(0xffffffffffffffffffffffffffffffffffffffff)
    0xa41: va41 = AND va40(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va2a
    0xa43: SSTORE va27(0x0), va41
    0xa44: JUMP v3cb(0xd0a4)

    Begin block 0xd0a4
    prev=[0x9ee], succ=[]
    =================================
    0xd0a5: STOP 

}

function loaner()() public {
    Begin block 0x3d2
    prev=[], succ=[0x3da, 0x3de]
    =================================
    0x3d3: v3d3 = CALLVALUE 
    0x3d5: v3d5 = ISZERO v3d3
    0x3d6: v3d6(0x3de) = CONST 
    0x3d9: JUMPI v3d6(0x3de), v3d5

    Begin block 0x3da
    prev=[0x3d2], succ=[]
    =================================
    0x3da: v3da(0x0) = CONST 
    0x3dd: REVERT v3da(0x0), v3da(0x0)

    Begin block 0x3de
    prev=[0x3d2], succ=[0xa45]
    =================================
    0x3e0: v3e0(0xd0c5) = CONST 
    0x3e3: v3e3(0xa45) = CONST 
    0x3e6: JUMP v3e3(0xa45)

    Begin block 0xa45
    prev=[0x3de], succ=[0xd0c5]
    =================================
    0xa46: va46(0x9) = CONST 
    0xa48: va48 = SLOAD va46(0x9)
    0xa49: va49(0x1) = CONST 
    0xa4b: va4b(0xa0) = CONST 
    0xa4d: va4d(0x2) = CONST 
    0xa4f: va4f(0x10000000000000000000000000000000000000000) = EXP va4d(0x2), va4b(0xa0)
    0xa50: va50(0xffffffffffffffffffffffffffffffffffffffff) = SUB va4f(0x10000000000000000000000000000000000000000), va49(0x1)
    0xa51: va51 = AND va50(0xffffffffffffffffffffffffffffffffffffffff), va48
    0xa53: JUMP v3e0(0xd0c5)

    Begin block 0xd0c5
    prev=[0xa45], succ=[]
    =================================
    0xd0c6: vd0c6(0x40) = CONST 
    0xd0c9: vd0c9 = MLOAD vd0c6(0x40)
    0xd0ca: vd0ca(0x1) = CONST 
    0xd0cc: vd0cc(0xa0) = CONST 
    0xd0ce: vd0ce(0x2) = CONST 
    0xd0d0: vd0d0(0x10000000000000000000000000000000000000000) = EXP vd0ce(0x2), vd0cc(0xa0)
    0xd0d1: vd0d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd0d0(0x10000000000000000000000000000000000000000), vd0ca(0x1)
    0xd0d4: vd0d4 = AND va51, vd0d1(0xffffffffffffffffffffffffffffffffffffffff)
    0xd0d6: MSTORE vd0c9, vd0d4
    0xd0d7: vd0d7 = MLOAD vd0c6(0x40)
    0xd0db: vd0db(0x0) = SUB vd0c9, vd0d7
    0xd0dc: vd0dc(0x20) = CONST 
    0xd0de: vd0de(0x20) = ADD vd0dc(0x20), vd0db(0x0)
    0xd0e0: RETURN vd0d7, vd0de(0x20)

}

function withdrawalSize()() public {
    Begin block 0x403
    prev=[], succ=[0x40b, 0x40f]
    =================================
    0x404: v404 = CALLVALUE 
    0x406: v406 = ISZERO v404
    0x407: v407(0x40f) = CONST 
    0x40a: JUMPI v407(0x40f), v406

    Begin block 0x40b
    prev=[0x403], succ=[]
    =================================
    0x40b: v40b(0x0) = CONST 
    0x40e: REVERT v40b(0x0), v40b(0x0)

    Begin block 0x40f
    prev=[0x403], succ=[0xa54]
    =================================
    0x411: v411(0xd100) = CONST 
    0x414: v414(0xa54) = CONST 
    0x417: JUMP v414(0xa54)

    Begin block 0xa54
    prev=[0x40f], succ=[0xd100]
    =================================
    0xa55: va55(0x6) = CONST 
    0xa57: va57 = SLOAD va55(0x6)
    0xa59: JUMP v411(0xd100)

    Begin block 0xd100
    prev=[0xa54], succ=[]
    =================================
    0xd101: vd101(0x40) = CONST 
    0xd104: vd104 = MLOAD vd101(0x40)
    0xd107: MSTORE vd104, va57
    0xd108: vd108 = MLOAD vd101(0x40)
    0xd10c: vd10c(0x0) = SUB vd104, vd108
    0xd10d: vd10d(0x20) = CONST 
    0xd10f: vd10f(0x20) = ADD vd10d(0x20), vd10c(0x0)
    0xd111: RETURN vd108, vd10f(0x20)

}

function minInvestment()() public {
    Begin block 0x418
    prev=[], succ=[0x420, 0x424]
    =================================
    0x419: v419 = CALLVALUE 
    0x41b: v41b = ISZERO v419
    0x41c: v41c(0x424) = CONST 
    0x41f: JUMPI v41c(0x424), v41b

    Begin block 0x420
    prev=[0x418], succ=[]
    =================================
    0x420: v420(0x0) = CONST 
    0x423: REVERT v420(0x0), v420(0x0)

    Begin block 0x424
    prev=[0x418], succ=[0xa5a]
    =================================
    0x426: v426(0xd131) = CONST 
    0x429: v429(0xa5a) = CONST 
    0x42c: JUMP v429(0xa5a)

    Begin block 0xa5a
    prev=[0x424], succ=[0xd131]
    =================================
    0xa5b: va5b(0x4) = CONST 
    0xa5d: va5d = SLOAD va5b(0x4)
    0xa5f: JUMP v426(0xd131)

    Begin block 0xd131
    prev=[0xa5a], succ=[]
    =================================
    0xd132: vd132(0x40) = CONST 
    0xd135: vd135 = MLOAD vd132(0x40)
    0xd138: MSTORE vd135, va5d
    0xd139: vd139 = MLOAD vd132(0x40)
    0xd13d: vd13d(0x0) = SUB vd135, vd139
    0xd13e: vd13e(0x20) = CONST 
    0xd140: vd140(0x20) = ADD vd13e(0x20), vd13d(0x0)
    0xd142: RETURN vd139, vd140(0x20)

}

function loanSize()() public {
    Begin block 0x42d
    prev=[], succ=[0x435, 0x439]
    =================================
    0x42e: v42e = CALLVALUE 
    0x430: v430 = ISZERO v42e
    0x431: v431(0x439) = CONST 
    0x434: JUMPI v431(0x439), v430

    Begin block 0x435
    prev=[0x42d], succ=[]
    =================================
    0x435: v435(0x0) = CONST 
    0x438: REVERT v435(0x0), v435(0x0)

    Begin block 0x439
    prev=[0x42d], succ=[0xa60]
    =================================
    0x43b: v43b(0xd162) = CONST 
    0x43e: v43e(0xa60) = CONST 
    0x441: JUMP v43e(0xa60)

    Begin block 0xa60
    prev=[0x439], succ=[0xd162]
    =================================
    0xa61: va61(0x5) = CONST 
    0xa63: va63 = SLOAD va61(0x5)
    0xa65: JUMP v43b(0xd162)

    Begin block 0xd162
    prev=[0xa60], succ=[]
    =================================
    0xd163: vd163(0x40) = CONST 
    0xd166: vd166 = MLOAD vd163(0x40)
    0xd169: MSTORE vd166, va63
    0xd16a: vd16a = MLOAD vd163(0x40)
    0xd16e: vd16e(0x0) = SUB vd166, vd16a
    0xd16f: vd16f(0x20) = CONST 
    0xd171: vd171(0x20) = ADD vd16f(0x20), vd16e(0x0)
    0xd173: RETURN vd16a, vd171(0x20)

}

function owner()() public {
    Begin block 0x442
    prev=[], succ=[0x44a, 0x44e]
    =================================
    0x443: v443 = CALLVALUE 
    0x445: v445 = ISZERO v443
    0x446: v446(0x44e) = CONST 
    0x449: JUMPI v446(0x44e), v445

    Begin block 0x44a
    prev=[0x442], succ=[]
    =================================
    0x44a: v44a(0x0) = CONST 
    0x44d: REVERT v44a(0x0), v44a(0x0)

    Begin block 0x44e
    prev=[0x442], succ=[0xa66]
    =================================
    0x450: v450(0xd193) = CONST 
    0x453: v453(0xa66) = CONST 
    0x456: JUMP v453(0xa66)

    Begin block 0xa66
    prev=[0x44e], succ=[0xd193]
    =================================
    0xa67: va67(0x0) = CONST 
    0xa69: va69 = SLOAD va67(0x0)
    0xa6a: va6a(0x1) = CONST 
    0xa6c: va6c(0xa0) = CONST 
    0xa6e: va6e(0x2) = CONST 
    0xa70: va70(0x10000000000000000000000000000000000000000) = EXP va6e(0x2), va6c(0xa0)
    0xa71: va71(0xffffffffffffffffffffffffffffffffffffffff) = SUB va70(0x10000000000000000000000000000000000000000), va6a(0x1)
    0xa72: va72 = AND va71(0xffffffffffffffffffffffffffffffffffffffff), va69
    0xa74: JUMP v450(0xd193)

    Begin block 0xd193
    prev=[0xa66], succ=[]
    =================================
    0xd194: vd194(0x40) = CONST 
    0xd197: vd197 = MLOAD vd194(0x40)
    0xd198: vd198(0x1) = CONST 
    0xd19a: vd19a(0xa0) = CONST 
    0xd19c: vd19c(0x2) = CONST 
    0xd19e: vd19e(0x10000000000000000000000000000000000000000) = EXP vd19c(0x2), vd19a(0xa0)
    0xd19f: vd19f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd19e(0x10000000000000000000000000000000000000000), vd198(0x1)
    0xd1a2: vd1a2 = AND va72, vd19f(0xffffffffffffffffffffffffffffffffffffffff)
    0xd1a4: MSTORE vd197, vd1a2
    0xd1a5: vd1a5 = MLOAD vd194(0x40)
    0xd1a9: vd1a9(0x0) = SUB vd197, vd1a5
    0xd1aa: vd1aa(0x20) = CONST 
    0xd1ac: vd1ac(0x20) = ADD vd1aa(0x20), vd1a9(0x0)
    0xd1ae: RETURN vd1a5, vd1ac(0x20)

}

function isOwner()() public {
    Begin block 0x457
    prev=[], succ=[0x45f, 0x463]
    =================================
    0x458: v458 = CALLVALUE 
    0x45a: v45a = ISZERO v458
    0x45b: v45b(0x463) = CONST 
    0x45e: JUMPI v45b(0x463), v45a

    Begin block 0x45f
    prev=[0x457], succ=[]
    =================================
    0x45f: v45f(0x0) = CONST 
    0x462: REVERT v45f(0x0), v45f(0x0)

    Begin block 0x463
    prev=[0x457], succ=[0xa75B0x463]
    =================================
    0x465: v465(0xd1ce) = CONST 
    0x468: v468(0xa75) = CONST 
    0x46b: JUMP v468(0xa75)

    Begin block 0xa75B0x463
    prev=[0x463], succ=[0xd1ce]
    =================================
    0xa76S0x463: va76V463(0x0) = CONST 
    0xa78S0x463: va78V463 = SLOAD va76V463(0x0)
    0xa79S0x463: va79V463(0x1) = CONST 
    0xa7bS0x463: va7bV463(0xa0) = CONST 
    0xa7dS0x463: va7dV463(0x2) = CONST 
    0xa7fS0x463: va7fV463(0x10000000000000000000000000000000000000000) = EXP va7dV463(0x2), va7bV463(0xa0)
    0xa80S0x463: va80V463(0xffffffffffffffffffffffffffffffffffffffff) = SUB va7fV463(0x10000000000000000000000000000000000000000), va79V463(0x1)
    0xa81S0x463: va81V463 = AND va80V463(0xffffffffffffffffffffffffffffffffffffffff), va78V463
    0xa82S0x463: va82V463 = CALLER 
    0xa83S0x463: va83V463 = EQ va82V463, va81V463
    0xa85S0x463: JUMP v465(0xd1ce)

    Begin block 0xd1ce
    prev=[0xa75B0x463], succ=[]
    =================================
    0xd1cf: vd1cf(0x40) = CONST 
    0xd1d2: vd1d2 = MLOAD vd1cf(0x40)
    0xd1d4: vd1d4 = ISZERO va83V463
    0xd1d5: vd1d5 = ISZERO vd1d4
    0xd1d7: MSTORE vd1d2, vd1d5
    0xd1d8: vd1d8 = MLOAD vd1cf(0x40)
    0xd1dc: vd1dc(0x0) = SUB vd1d2, vd1d8
    0xd1dd: vd1dd(0x20) = CONST 
    0xd1df: vd1df(0x20) = ADD vd1dd(0x20), vd1dc(0x0)
    0xd1e1: RETURN vd1d8, vd1df(0x20)

}

function symbol()() public {
    Begin block 0x46c
    prev=[], succ=[0x474, 0x478]
    =================================
    0x46d: v46d = CALLVALUE 
    0x46f: v46f = ISZERO v46d
    0x470: v470(0x478) = CONST 
    0x473: JUMPI v470(0x478), v46f

    Begin block 0x474
    prev=[0x46c], succ=[]
    =================================
    0x474: v474(0x0) = CONST 
    0x477: REVERT v474(0x0), v474(0x0)

    Begin block 0x478
    prev=[0x46c], succ=[0xa86B0x478]
    =================================
    0x47a: v47a(0xd201) = CONST 
    0x47d: v47d(0xa86) = CONST 
    0x480: JUMP v47d(0xa86)

    Begin block 0xa86B0x478
    prev=[0x478], succ=[0xaccB0x478, 0x19622B0x478]
    =================================
    0xa87S0x478: va87V478(0xb) = CONST 
    0xa8aS0x478: va8aV478 = SLOAD va87V478(0xb)
    0xa8bS0x478: va8bV478(0x40) = CONST 
    0xa8eS0x478: va8eV478 = MLOAD va8bV478(0x40)
    0xa8fS0x478: va8fV478(0x20) = CONST 
    0xa91S0x478: va91V478(0x1f) = CONST 
    0xa93S0x478: va93V478(0x2) = CONST 
    0xa95S0x478: va95V478(0x0) = CONST 
    0xa97S0x478: va97V478(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT va95V478(0x0)
    0xa98S0x478: va98V478(0x100) = CONST 
    0xa9bS0x478: va9bV478(0x1) = CONST 
    0xa9eS0x478: va9eV478 = AND va8aV478, va9bV478(0x1)
    0xa9fS0x478: va9fV478 = ISZERO va9eV478
    0xaa0S0x478: vaa0V478 = MUL va9fV478, va98V478(0x100)
    0xaa1S0x478: vaa1V478 = ADD vaa0V478, va97V478(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xaa4S0x478: vaa4V478 = AND va8aV478, vaa1V478
    0xaa8S0x478: vaa8V478 = DIV vaa4V478, va93V478(0x2)
    0xaabS0x478: vaabV478 = ADD vaa8V478, va91V478(0x1f)
    0xaaeS0x478: vaaeV478 = DIV vaabV478, va8fV478(0x20)
    0xab0S0x478: vab0V478 = MUL va8fV478(0x20), vaaeV478
    0xab2S0x478: vab2V478 = ADD va8eV478, vab0V478
    0xab4S0x478: vab4V478 = ADD va8fV478(0x20), vab2V478
    0xab7S0x478: MSTORE va8bV478(0x40), vab4V478
    0xabaS0x478: MSTORE va8eV478, vaa8V478
    0xabbS0x478: vabbV478(0x60) = CONST 
    0xac3S0x478: vac3V478 = ADD va8eV478, va8fV478(0x20)
    0xac7S0x478: vac7V478 = ISZERO vaa8V478
    0xac8S0x478: vac8V478(0x19622) = CONST 
    0xacbS0x478: JUMPI vac8V478(0x19622), vac7V478

    Begin block 0xaccB0x478
    prev=[0xa86B0x478], succ=[0xad4B0x478, 0x6120xa86B0x478]
    =================================
    0xacdS0x478: vacdV478(0x1f) = CONST 
    0xacfS0x478: vacfV478 = LT vacdV478(0x1f), vaa8V478
    0xad0S0x478: vad0V478(0x612) = CONST 
    0xad3S0x478: JUMPI vad0V478(0x612), vacfV478

    Begin block 0xad4B0x478
    prev=[0xaccB0x478], succ=[0x1964bB0x478]
    =================================
    0xad4S0x478: vad4V478(0x100) = CONST 
    0xad9S0x478: vad9V478 = SLOAD va87V478(0xb)
    0xadaS0x478: vadaV478 = DIV vad9V478, vad4V478(0x100)
    0xadbS0x478: vadbV478 = MUL vadaV478, vad4V478(0x100)
    0xaddS0x478: MSTORE vac3V478, vadbV478
    0xadfS0x478: vadfV478(0x20) = CONST 
    0xae1S0x478: vae1V478 = ADD vadfV478(0x20), vac3V478
    0xae3S0x478: vae3V478(0x1964b) = CONST 
    0xae6S0x478: JUMP vae3V478(0x1964b)

    Begin block 0x1964bB0x478
    prev=[0xad4B0x478], succ=[0xd201]
    =================================
    0x19654S0x478: JUMP v47a(0xd201)

    Begin block 0xd201
    prev=[0x19622B0x478, 0x1964bB0x478, 0x230050xa86B0x478], succ=[0x1940x46c]
    =================================
    0xd202: vd202(0x40) = CONST 
    0xd205: vd205 = MLOAD vd202(0x40)
    0xd206: vd206(0x20) = CONST 
    0xd20a: MSTORE vd205, vd206(0x20)
    0xd20c: vd20c = MLOAD va8eV478
    0xd20f: vd20f = ADD vd205, vd206(0x20)
    0xd210: MSTORE vd20f, vd20c
    0xd212: vd212 = MLOAD va8eV478
    0xd219: vd219 = ADD vd205, vd202(0x40)
    0xd21c: vd21c = ADD va8eV478, vd206(0x20)
    0xd221: vd221(0x0) = CONST 
    0xfb21: vfb21(0x194) = CONST 
    0xfb41: JUMP vfb21(0x194)

    Begin block 0x1940x46c
    prev=[0xd201, 0x19d0x46c], succ=[0x1ac0x46c, 0x19d0x46c]
    =================================
    0x1940x46c_0x0: v19446c_0 = PHI vd221(0x0), v46c1a7
    0x1970x46c: v46c197 = LT v19446c_0, vd212
    0x1980x46c: v46c198 = ISZERO v46c197
    0x1990x46c: v46c199(0x1ac) = CONST 
    0x19c0x46c: JUMPI v46c199(0x1ac), v46c198

    Begin block 0x1ac0x46c
    prev=[0x1940x46c], succ=[0x1c00x46c, 0x1d90x46c]
    =================================
    0x1b50x46c: v46c1b5 = ADD vd212, vd219
    0x1b70x46c: v46c1b7(0x1f) = CONST 
    0x1b90x46c: v46c1b9 = AND v46c1b7(0x1f), vd212
    0x1bb0x46c: v46c1bb = ISZERO v46c1b9
    0x1bc0x46c: v46c1bc(0x1d9) = CONST 
    0x1bf0x46c: JUMPI v46c1bc(0x1d9), v46c1bb

    Begin block 0x1c00x46c
    prev=[0x1ac0x46c], succ=[0x1d90x46c]
    =================================
    0x1c20x46c: v46c1c2 = SUB v46c1b5, v46c1b9
    0x1c40x46c: v46c1c4 = MLOAD v46c1c2
    0x1c50x46c: v46c1c5(0x1) = CONST 
    0x1c80x46c: v46c1c8(0x20) = CONST 
    0x1ca0x46c: v46c1ca = SUB v46c1c8(0x20), v46c1b9
    0x1cb0x46c: v46c1cb(0x100) = CONST 
    0x1ce0x46c: v46c1ce = EXP v46c1cb(0x100), v46c1ca
    0x1cf0x46c: v46c1cf = SUB v46c1ce, v46c1c5(0x1)
    0x1d00x46c: v46c1d0 = NOT v46c1cf
    0x1d10x46c: v46c1d1 = AND v46c1d0, v46c1c4
    0x1d30x46c: MSTORE v46c1c2, v46c1d1
    0x1d40x46c: v46c1d4(0x20) = CONST 
    0x1d60x46c: v46c1d6 = ADD v46c1d4(0x20), v46c1c2
    0x34920x46c: v46c3492(0x1d9) = CONST 
    0x34b20x46c: JUMP v46c3492(0x1d9)

    Begin block 0x1d90x46c
    prev=[0x1c00x46c, 0x1ac0x46c], succ=[]
    =================================
    0x1d90x46c_0x1: v1d946c_1 = PHI v46c1d6, v46c1b5
    0x1df0x46c: v46c1df(0x40) = CONST 
    0x1e10x46c: v46c1e1 = MLOAD v46c1df(0x40)
    0x1e40x46c: v46c1e4 = SUB v1d946c_1, v46c1e1
    0x1e60x46c: RETURN v46c1e1, v46c1e4

    Begin block 0x19d0x46c
    prev=[0x1940x46c], succ=[0x1940x46c]
    =================================
    0x19d0x46c_0x0: v19d46c_0 = PHI vd221(0x0), v46c1a7
    0x19f0x46c: v46c19f = ADD v19d46c_0, vd21c
    0x1a00x46c: v46c1a0 = MLOAD v46c19f
    0x1a30x46c: v46c1a3 = ADD v19d46c_0, vd219
    0x1a40x46c: MSTORE v46c1a3, v46c1a0
    0x1a50x46c: v46c1a5(0x20) = CONST 
    0x1a70x46c: v46c1a7 = ADD v46c1a5(0x20), v19d46c_0
    0x1a80x46c: v46c1a8(0x194) = CONST 
    0x1ab0x46c: JUMP v46c1a8(0x194)

    Begin block 0x6120xa86B0x478
    prev=[0xaccB0x478], succ=[0x6200xa86B0x478]
    =================================
    0x6140xa86S0x478: va86614V478 = ADD vac3V478, vaa8V478
    0x6170xa86S0x478: va86617V478(0x0) = CONST 
    0x6190xa86S0x478: MSTORE va86617V478(0x0), va87V478(0xb)
    0x61a0xa86S0x478: va8661aV478(0x20) = CONST 
    0x61c0xa86S0x478: va8661cV478(0x0) = CONST 
    0x61e0xa86S0x478: va8661eV478 = SHA3 va8661cV478(0x0), va8661aV478(0x20)
    0x3e920xa86S0x478: va863e92V478(0x620) = CONST 
    0x3eb20xa86S0x478: JUMP va863e92V478(0x620)

    Begin block 0x6200xa86B0x478
    prev=[0x6120xa86B0x478, 0x6200xa86B0x478], succ=[0x6200xa86B0x478, 0x6340xa86B0x478]
    =================================
    0x6200xa86_0x0S0x478: v620a86_0V478 = PHI vac3V478, va8662cV478
    0x6200xa86_0x1S0x478: v620a86_1V478 = PHI va8661eV478, va86628V478
    0x6220xa86S0x478: va86622V478 = SLOAD v620a86_1V478
    0x6240xa86S0x478: MSTORE v620a86_0V478, va86622V478
    0x6260xa86S0x478: va86626V478(0x1) = CONST 
    0x6280xa86S0x478: va86628V478 = ADD va86626V478(0x1), v620a86_1V478
    0x62a0xa86S0x478: va8662aV478(0x20) = CONST 
    0x62c0xa86S0x478: va8662cV478 = ADD va8662aV478(0x20), v620a86_0V478
    0x62f0xa86S0x478: va8662fV478 = GT va86614V478, va8662cV478
    0x6300xa86S0x478: va86630V478(0x620) = CONST 
    0x6330xa86S0x478: JUMPI va86630V478(0x620), va8662fV478

    Begin block 0x6340xa86B0x478
    prev=[0x6200xa86B0x478], succ=[0x230050xa86B0x478]
    =================================
    0x6360xa86S0x478: va86636V478 = SUB va8662cV478, va86614V478
    0x6370xa86S0x478: va86637V478(0x1f) = CONST 
    0x6390xa86S0x478: va86639V478 = AND va86637V478(0x1f), va86636V478
    0x63b0xa86S0x478: va8663bV478 = ADD va86614V478, va86639V478
    0x48920xa86S0x478: va864892V478(0x23005) = CONST 
    0x48b20xa86S0x478: JUMP va864892V478(0x23005)

    Begin block 0x230050xa86B0x478
    prev=[0x6340xa86B0x478], succ=[0xd201]
    =================================
    0x2300e0xa86S0x478: JUMP v47a(0xd201)

    Begin block 0x19622B0x478
    prev=[0xa86B0x478], succ=[0xd201]
    =================================
    0x1962bS0x478: JUMP v47a(0xd201)

}

function decreaseAllowance(address,uint256)() public {
    Begin block 0x481
    prev=[], succ=[0x489, 0x48d]
    =================================
    0x482: v482 = CALLVALUE 
    0x484: v484 = ISZERO v482
    0x485: v485(0x48d) = CONST 
    0x488: JUMPI v485(0x48d), v484

    Begin block 0x489
    prev=[0x481], succ=[]
    =================================
    0x489: v489(0x0) = CONST 
    0x48c: REVERT v489(0x0), v489(0x0)

    Begin block 0x48d
    prev=[0x481], succ=[0x4a0, 0x4a4]
    =================================
    0x48f: v48f(0xfb61) = CONST 
    0x492: v492(0x4) = CONST 
    0x495: v495 = CALLDATASIZE 
    0x496: v496 = SUB v495, v492(0x4)
    0x497: v497(0x40) = CONST 
    0x49a: v49a = LT v496, v497(0x40)
    0x49b: v49b = ISZERO v49a
    0x49c: v49c(0x4a4) = CONST 
    0x49f: JUMPI v49c(0x4a4), v49b

    Begin block 0x4a0
    prev=[0x48d], succ=[]
    =================================
    0x4a0: v4a0(0x0) = CONST 
    0x4a3: REVERT v4a0(0x0), v4a0(0x0)

    Begin block 0x4a4
    prev=[0x48d], succ=[0xae7B0x4a4]
    =================================
    0x4a6: v4a6(0x1) = CONST 
    0x4a8: v4a8(0xa0) = CONST 
    0x4aa: v4aa(0x2) = CONST 
    0x4ac: v4ac(0x10000000000000000000000000000000000000000) = EXP v4aa(0x2), v4a8(0xa0)
    0x4ad: v4ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ac(0x10000000000000000000000000000000000000000), v4a6(0x1)
    0x4af: v4af = CALLDATALOAD v492(0x4)
    0x4b0: v4b0 = AND v4af, v4ad(0xffffffffffffffffffffffffffffffffffffffff)
    0x4b2: v4b2(0x20) = CONST 
    0x4b4: v4b4(0x24) = ADD v4b2(0x20), v492(0x4)
    0x4b5: v4b5 = CALLDATALOAD v4b4(0x24)
    0x4b6: v4b6(0xae7) = CONST 
    0x4b9: JUMP v4b6(0xae7)

    Begin block 0xae7B0x4a4
    prev=[0x4a4], succ=[0x1e2f2B0x4a4]
    =================================
    0xae8S0x4a4: vae8V4a4 = CALLER 
    0xae9S0x4a4: vae9V4a4(0x0) = CONST 
    0xaedS0x4a4: MSTORE vae9V4a4(0x0), vae8V4a4
    0xaeeS0x4a4: vaeeV4a4(0x2) = CONST 
    0xaf0S0x4a4: vaf0V4a4(0x20) = CONST 
    0xaf4S0x4a4: MSTORE vaf0V4a4(0x20), vaeeV4a4(0x2)
    0xaf5S0x4a4: vaf5V4a4(0x40) = CONST 
    0xaf9S0x4a4: vaf9V4a4 = SHA3 vae9V4a4(0x0), vaf5V4a4(0x40)
    0xafaS0x4a4: vafaV4a4(0x1) = CONST 
    0xafcS0x4a4: vafcV4a4(0xa0) = CONST 
    0xafeS0x4a4: vafeV4a4(0x2) = CONST 
    0xb00S0x4a4: vb00V4a4(0x10000000000000000000000000000000000000000) = EXP vafeV4a4(0x2), vafcV4a4(0xa0)
    0xb01S0x4a4: vb01V4a4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb00V4a4(0x10000000000000000000000000000000000000000), vafaV4a4(0x1)
    0xb03S0x4a4: vb03V4a4 = AND v4b0, vb01V4a4(0xffffffffffffffffffffffffffffffffffffffff)
    0xb05S0x4a4: MSTORE vae9V4a4(0x0), vb03V4a4
    0xb08S0x4a4: MSTORE vaf0V4a4(0x20), vaf9V4a4
    0xb0aS0x4a4: vb0aV4a4 = SHA3 vae9V4a4(0x0), vaf5V4a4(0x40)
    0xb0bS0x4a4: vb0bV4a4 = SLOAD vb0aV4a4
    0xb0eS0x4a4: vb0eV4a4(0x19674) = CONST 
    0xb14S0x4a4: vb14V4a4(0x1e2f2) = CONST 
    0xb19S0x4a4: vb19V4a4(0xffffffff) = CONST 
    0xb1eS0x4a4: vb1eV4a4(0x1010) = CONST 
    0xb21S0x4a4: vb21V4a4(0x1010) = AND vb1eV4a4(0x1010), vb19V4a4(0xffffffff)
    0xb22S0x4a4: vb22_0V4a4 = CALLPRIVATE vb21V4a4(0x1010), v4b5, vb0bV4a4, vb14V4a4(0x1e2f2)

    Begin block 0x1e2f2B0x4a4
    prev=[0xae7B0x4a4], succ=[0x19674B0x4a4]
    =================================
    0x1e2f3S0x4a4: v1e2f3V4a4(0xcdd) = CONST 
    0x1e2f6S0x4a4: CALLPRIVATE v1e2f3V4a4(0xcdd), vb22_0V4a4, v4b0, vae8V4a4, vb0eV4a4(0x19674)

    Begin block 0x19674B0x4a4
    prev=[0x1e2f2B0x4a4], succ=[0x2309dB0x4a4]
    =================================
    0x19676S0x4a4: v19676V4a4(0x1) = CONST 
    0x1e2b2S0x4a4: v1e2b2V4a4(0x2309d) = CONST 
    0x1e2d2S0x4a4: JUMP v1e2b2V4a4(0x2309d)

    Begin block 0x2309dB0x4a4
    prev=[0x19674B0x4a4], succ=[0xfb61]
    =================================
    0x230a2S0x4a4: JUMP v48f(0xfb61)

    Begin block 0xfb61
    prev=[0x2309dB0x4a4], succ=[]
    =================================
    0xfb62: vfb62(0x40) = CONST 
    0xfb65: vfb65 = MLOAD vfb62(0x40)
    0xfb67: vfb67(0x0) = ISZERO v19676V4a4(0x1)
    0xfb68: vfb68(0x1) = ISZERO vfb67(0x0)
    0xfb6a: MSTORE vfb65, vfb68(0x1)
    0xfb6b: vfb6b = MLOAD vfb62(0x40)
    0xfb6f: vfb6f(0x0) = SUB vfb65, vfb6b
    0xfb70: vfb70(0x20) = CONST 
    0xfb72: vfb72(0x20) = ADD vfb70(0x20), vfb6f(0x0)
    0xfb74: RETURN vfb6b, vfb72(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x4ba
    prev=[], succ=[0x4c2, 0x4c6]
    =================================
    0x4bb: v4bb = CALLVALUE 
    0x4bd: v4bd = ISZERO v4bb
    0x4be: v4be(0x4c6) = CONST 
    0x4c1: JUMPI v4be(0x4c6), v4bd

    Begin block 0x4c2
    prev=[0x4ba], succ=[]
    =================================
    0x4c2: v4c2(0x0) = CONST 
    0x4c5: REVERT v4c2(0x0), v4c2(0x0)

    Begin block 0x4c6
    prev=[0x4ba], succ=[0x4d9, 0x4dd]
    =================================
    0x4c8: v4c8(0xfb94) = CONST 
    0x4cb: v4cb(0x4) = CONST 
    0x4ce: v4ce = CALLDATASIZE 
    0x4cf: v4cf = SUB v4ce, v4cb(0x4)
    0x4d0: v4d0(0x40) = CONST 
    0x4d3: v4d3 = LT v4cf, v4d0(0x40)
    0x4d4: v4d4 = ISZERO v4d3
    0x4d5: v4d5(0x4dd) = CONST 
    0x4d8: JUMPI v4d5(0x4dd), v4d4

    Begin block 0x4d9
    prev=[0x4c6], succ=[]
    =================================
    0x4d9: v4d9(0x0) = CONST 
    0x4dc: REVERT v4d9(0x0), v4d9(0x0)

    Begin block 0x4dd
    prev=[0x4c6], succ=[0xb23B0x4dd]
    =================================
    0x4df: v4df(0x1) = CONST 
    0x4e1: v4e1(0xa0) = CONST 
    0x4e3: v4e3(0x2) = CONST 
    0x4e5: v4e5(0x10000000000000000000000000000000000000000) = EXP v4e3(0x2), v4e1(0xa0)
    0x4e6: v4e6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e5(0x10000000000000000000000000000000000000000), v4df(0x1)
    0x4e8: v4e8 = CALLDATALOAD v4cb(0x4)
    0x4e9: v4e9 = AND v4e8, v4e6(0xffffffffffffffffffffffffffffffffffffffff)
    0x4eb: v4eb(0x20) = CONST 
    0x4ed: v4ed(0x24) = ADD v4eb(0x20), v4cb(0x4)
    0x4ee: v4ee = CALLDATALOAD v4ed(0x24)
    0x4ef: v4ef(0xb23) = CONST 
    0x4f2: JUMP v4ef(0xb23)

    Begin block 0xb23B0x4dd
    prev=[0x4dd], succ=[0x1e316B0x4dd]
    =================================
    0xb24S0x4dd: vb24V4dd(0x0) = CONST 
    0xb26S0x4dd: vb26V4dd(0x1e316) = CONST 
    0xb29S0x4dd: vb29V4dd = CALLER 
    0xb2cS0x4dd: vb2cV4dd(0xe4a) = CONST 
    0xb2fS0x4dd: CALLPRIVATE vb2cV4dd(0xe4a), v4ee, v4e9, vb29V4dd, vb26V4dd(0x1e316)

    Begin block 0x1e316B0x4dd
    prev=[0xb23B0x4dd], succ=[0x230c2B0x4dd]
    =================================
    0x1e318S0x4dd: v1e318V4dd(0x1) = CONST 
    0x22f54S0x4dd: v22f54V4dd(0x230c2) = CONST 
    0x22f74S0x4dd: JUMP v22f54V4dd(0x230c2)

    Begin block 0x230c2B0x4dd
    prev=[0x1e316B0x4dd], succ=[0xfb94]
    =================================
    0x230c7S0x4dd: JUMP v4c8(0xfb94)

    Begin block 0xfb94
    prev=[0x230c2B0x4dd], succ=[]
    =================================
    0xfb95: vfb95(0x40) = CONST 
    0xfb98: vfb98 = MLOAD vfb95(0x40)
    0xfb9a: vfb9a(0x0) = ISZERO v1e318V4dd(0x1)
    0xfb9b: vfb9b(0x1) = ISZERO vfb9a(0x0)
    0xfb9d: MSTORE vfb98, vfb9b(0x1)
    0xfb9e: vfb9e = MLOAD vfb95(0x40)
    0xfba2: vfba2(0x0) = SUB vfb98, vfb9e
    0xfba3: vfba3(0x20) = CONST 
    0xfba5: vfba5(0x20) = ADD vfba3(0x20), vfba2(0x0)
    0xfba7: RETURN vfb9e, vfba5(0x20)

}

function getLoanSize()() public {
    Begin block 0x4f3
    prev=[], succ=[0x4fb, 0x4ff]
    =================================
    0x4f4: v4f4 = CALLVALUE 
    0x4f6: v4f6 = ISZERO v4f4
    0x4f7: v4f7(0x4ff) = CONST 
    0x4fa: JUMPI v4f7(0x4ff), v4f6

    Begin block 0x4fb
    prev=[0x4f3], succ=[]
    =================================
    0x4fb: v4fb(0x0) = CONST 
    0x4fe: REVERT v4fb(0x0), v4fb(0x0)

    Begin block 0x4ff
    prev=[0x4f3], succ=[0xb30]
    =================================
    0x501: v501(0xfbc7) = CONST 
    0x504: v504(0xb30) = CONST 
    0x507: JUMP v504(0xb30)

    Begin block 0xb30
    prev=[0x4ff], succ=[0xfbc7]
    =================================
    0xb31: vb31(0x5) = CONST 
    0xb33: vb33 = SLOAD vb31(0x5)
    0xb35: JUMP v501(0xfbc7)

    Begin block 0xfbc7
    prev=[0xb30], succ=[]
    =================================
    0xfbc8: vfbc8(0x40) = CONST 
    0xfbcb: vfbcb = MLOAD vfbc8(0x40)
    0xfbce: MSTORE vfbcb, vb33
    0xfbcf: vfbcf = MLOAD vfbc8(0x40)
    0xfbd3: vfbd3(0x0) = SUB vfbcb, vfbcf
    0xfbd4: vfbd4(0x20) = CONST 
    0xfbd6: vfbd6(0x20) = ADD vfbd4(0x20), vfbd3(0x0)
    0xfbd8: RETURN vfbcf, vfbd6(0x20)

}

function buyTokens()() public {
    Begin block 0x508
    prev=[], succ=[0xb36]
    =================================
    0x509: v509(0xfbf8) = CONST 
    0x50c: v50c(0xb36) = CONST 
    0x50f: JUMP v50c(0xb36)

    Begin block 0xb36
    prev=[0x508], succ=[0xb40, 0xb69]
    =================================
    0xb37: vb37(0x4) = CONST 
    0xb39: vb39 = SLOAD vb37(0x4)
    0xb3a: vb3a = CALLVALUE 
    0xb3b: vb3b = GT vb3a, vb39
    0xb3c: vb3c(0xb69) = CONST 
    0xb3f: JUMPI vb3c(0xb69), vb3b

    Begin block 0xb40
    prev=[0xb36], succ=[]
    =================================
    0xb40: vb40(0x40) = CONST 
    0xb43: vb43 = MLOAD vb40(0x40)
    0xb44: vb44(0xe5) = CONST 
    0xb46: vb46(0x2) = CONST 
    0xb48: vb48(0x2000000000000000000000000000000000000000000000000000000000) = EXP vb46(0x2), vb44(0xe5)
    0xb49: vb49(0x461bcd) = CONST 
    0xb4d: vb4d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vb49(0x461bcd), vb48(0x2000000000000000000000000000000000000000000000000000000000)
    0xb4f: MSTORE vb43, vb4d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb50: vb50(0x20) = CONST 
    0xb52: vb52(0x4) = CONST 
    0xb55: vb55 = ADD vb43, vb52(0x4)
    0xb56: MSTORE vb55, vb50(0x20)
    0xb57: vb57(0x0) = CONST 
    0xb59: vb59(0x24) = CONST 
    0xb5c: vb5c = ADD vb43, vb59(0x24)
    0xb5d: MSTORE vb5c, vb57(0x0)
    0xb5f: vb5f = MLOAD vb40(0x40)
    0xb63: vb63(0x0) = SUB vb43, vb5f
    0xb64: vb64(0x64) = CONST 
    0xb66: vb66(0x64) = ADD vb64(0x64), vb63(0x0)
    0xb68: REVERT vb5f, vb66(0x64)

    Begin block 0xb69
    prev=[0xb36], succ=[0xb80]
    =================================
    0xb6a: vb6a(0x0) = CONST 
    0xb6c: vb6c(0xb80) = CONST 
    0xb6f: vb6f(0x7) = CONST 
    0xb71: vb71 = SLOAD vb6f(0x7)
    0xb72: vb72 = CALLVALUE 
    0xb73: vb73(0x10df) = CONST 
    0xb79: vb79(0xffffffff) = CONST 
    0xb7e: vb7e(0x10df) = AND vb79(0xffffffff), vb73(0x10df)
    0xb7f: vb7f_0 = CALLPRIVATE vb7e(0x10df), vb71, vb72, vb6c(0xb80)

    Begin block 0xb80
    prev=[0xb69], succ=[0xb8c]
    =================================
    0xb83: vb83(0xb8c) = CONST 
    0xb86: vb86 = CALLER 
    0xb88: vb88(0x1320) = CONST 
    0xb8b: CALLPRIVATE vb88(0x1320), vb7f_0, vb86, vb83(0xb8c)

    Begin block 0xb8c
    prev=[0xb80], succ=[0xb9f]
    =================================
    0xb8d: vb8d(0x5) = CONST 
    0xb8f: vb8f = SLOAD vb8d(0x5)
    0xb90: vb90(0xb9f) = CONST 
    0xb94: vb94 = CALLVALUE 
    0xb95: vb95(0xffffffff) = CONST 
    0xb9a: vb9a(0x12c3) = CONST 
    0xb9d: vb9d(0x12c3) = AND vb9a(0x12c3), vb95(0xffffffff)
    0xb9e: vb9e_0 = CALLPRIVATE vb9d(0x12c3), vb94, vb8f, vb90(0xb9f)

    Begin block 0xb9f
    prev=[0xb8c], succ=[0xbb5]
    =================================
    0xba0: vba0(0x5) = CONST 
    0xba2: SSTORE vba0(0x5), vb9e_0
    0xba3: vba3(0x8) = CONST 
    0xba5: vba5 = SLOAD vba3(0x8)
    0xba6: vba6(0xbb5) = CONST 
    0xbaa: vbaa = CALLVALUE 
    0xbab: vbab(0xffffffff) = CONST 
    0xbb0: vbb0(0x12c3) = CONST 
    0xbb3: vbb3(0x12c3) = AND vbb0(0x12c3), vbab(0xffffffff)
    0xbb4: vbb4_0 = CALLPRIVATE vbb3(0x12c3), vbaa, vba5, vba6(0xbb5)

    Begin block 0xbb5
    prev=[0xb9f], succ=[0xfbf8]
    =================================
    0xbb6: vbb6(0x8) = CONST 
    0xbb8: SSTORE vbb6(0x8), vbb4_0
    0xbba: JUMP v509(0xfbf8)

    Begin block 0xfbf8
    prev=[0xbb5], succ=[]
    =================================
    0xfbf9: STOP 

}

function allowance(address,address)() public {
    Begin block 0x510
    prev=[], succ=[0x518, 0x51c]
    =================================
    0x511: v511 = CALLVALUE 
    0x513: v513 = ISZERO v511
    0x514: v514(0x51c) = CONST 
    0x517: JUMPI v514(0x51c), v513

    Begin block 0x518
    prev=[0x510], succ=[]
    =================================
    0x518: v518(0x0) = CONST 
    0x51b: REVERT v518(0x0), v518(0x0)

    Begin block 0x51c
    prev=[0x510], succ=[0x52f, 0x533]
    =================================
    0x51e: v51e(0xfc19) = CONST 
    0x521: v521(0x4) = CONST 
    0x524: v524 = CALLDATASIZE 
    0x525: v525 = SUB v524, v521(0x4)
    0x526: v526(0x40) = CONST 
    0x529: v529 = LT v525, v526(0x40)
    0x52a: v52a = ISZERO v529
    0x52b: v52b(0x533) = CONST 
    0x52e: JUMPI v52b(0x533), v52a

    Begin block 0x52f
    prev=[0x51c], succ=[]
    =================================
    0x52f: v52f(0x0) = CONST 
    0x532: REVERT v52f(0x0), v52f(0x0)

    Begin block 0x533
    prev=[0x51c], succ=[0xbbb]
    =================================
    0x535: v535(0x1) = CONST 
    0x537: v537(0xa0) = CONST 
    0x539: v539(0x2) = CONST 
    0x53b: v53b(0x10000000000000000000000000000000000000000) = EXP v539(0x2), v537(0xa0)
    0x53c: v53c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53b(0x10000000000000000000000000000000000000000), v535(0x1)
    0x53e: v53e = CALLDATALOAD v521(0x4)
    0x540: v540 = AND v53c(0xffffffffffffffffffffffffffffffffffffffff), v53e
    0x542: v542(0x20) = CONST 
    0x544: v544(0x24) = ADD v542(0x20), v521(0x4)
    0x545: v545 = CALLDATALOAD v544(0x24)
    0x546: v546 = AND v545, v53c(0xffffffffffffffffffffffffffffffffffffffff)
    0x547: v547(0xbbb) = CONST 
    0x54a: JUMP v547(0xbbb)

    Begin block 0xbbb
    prev=[0x533], succ=[0xfc19]
    =================================
    0xbbc: vbbc(0x1) = CONST 
    0xbbe: vbbe(0xa0) = CONST 
    0xbc0: vbc0(0x2) = CONST 
    0xbc2: vbc2(0x10000000000000000000000000000000000000000) = EXP vbc0(0x2), vbbe(0xa0)
    0xbc3: vbc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbc2(0x10000000000000000000000000000000000000000), vbbc(0x1)
    0xbc6: vbc6 = AND vbc3(0xffffffffffffffffffffffffffffffffffffffff), v540
    0xbc7: vbc7(0x0) = CONST 
    0xbcb: MSTORE vbc7(0x0), vbc6
    0xbcc: vbcc(0x2) = CONST 
    0xbce: vbce(0x20) = CONST 
    0xbd2: MSTORE vbce(0x20), vbcc(0x2)
    0xbd3: vbd3(0x40) = CONST 
    0xbd7: vbd7 = SHA3 vbc7(0x0), vbd3(0x40)
    0xbdb: vbdb = AND vbc3(0xffffffffffffffffffffffffffffffffffffffff), v546
    0xbdd: MSTORE vbc7(0x0), vbdb
    0xbe1: MSTORE vbce(0x20), vbd7
    0xbe2: vbe2 = SHA3 vbc7(0x0), vbd3(0x40)
    0xbe3: vbe3 = SLOAD vbe2
    0xbe5: JUMP v51e(0xfc19)

    Begin block 0xfc19
    prev=[0xbbb], succ=[]
    =================================
    0xfc1a: vfc1a(0x40) = CONST 
    0xfc1d: vfc1d = MLOAD vfc1a(0x40)
    0xfc20: MSTORE vfc1d, vbe3
    0xfc21: vfc21 = MLOAD vfc1a(0x40)
    0xfc25: vfc25(0x0) = SUB vfc1d, vfc21
    0xfc26: vfc26(0x20) = CONST 
    0xfc28: vfc28(0x20) = ADD vfc26(0x20), vfc25(0x0)
    0xfc2a: RETURN vfc21, vfc28(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x54b
    prev=[], succ=[0x553, 0x557]
    =================================
    0x54c: v54c = CALLVALUE 
    0x54e: v54e = ISZERO v54c
    0x54f: v54f(0x557) = CONST 
    0x552: JUMPI v54f(0x557), v54e

    Begin block 0x553
    prev=[0x54b], succ=[]
    =================================
    0x553: v553(0x0) = CONST 
    0x556: REVERT v553(0x0), v553(0x0)

    Begin block 0x557
    prev=[0x54b], succ=[0x56a, 0x56e]
    =================================
    0x559: v559(0xfc4a) = CONST 
    0x55c: v55c(0x4) = CONST 
    0x55f: v55f = CALLDATASIZE 
    0x560: v560 = SUB v55f, v55c(0x4)
    0x561: v561(0x20) = CONST 
    0x564: v564 = LT v560, v561(0x20)
    0x565: v565 = ISZERO v564
    0x566: v566(0x56e) = CONST 
    0x569: JUMPI v566(0x56e), v565

    Begin block 0x56a
    prev=[0x557], succ=[]
    =================================
    0x56a: v56a(0x0) = CONST 
    0x56d: REVERT v56a(0x0), v56a(0x0)

    Begin block 0x56e
    prev=[0x557], succ=[0xbe6B0x56e]
    =================================
    0x570: v570 = CALLDATALOAD v55c(0x4)
    0x571: v571(0x1) = CONST 
    0x573: v573(0xa0) = CONST 
    0x575: v575(0x2) = CONST 
    0x577: v577(0x10000000000000000000000000000000000000000) = EXP v575(0x2), v573(0xa0)
    0x578: v578(0xffffffffffffffffffffffffffffffffffffffff) = SUB v577(0x10000000000000000000000000000000000000000), v571(0x1)
    0x579: v579 = AND v578(0xffffffffffffffffffffffffffffffffffffffff), v570
    0x57a: v57a(0xbe6) = CONST 
    0x57d: JUMP v57a(0xbe6)

    Begin block 0xbe6B0x56e
    prev=[0x56e], succ=[0xa75B0xbe6B0x56e]
    =================================
    0xbe7S0x56e: vbe7V56e(0xbee) = CONST 
    0xbeaS0x56e: vbeaV56e(0xa75) = CONST 
    0xbedS0x56e: JUMP vbeaV56e(0xa75)

    Begin block 0xa75B0xbe6B0x56e
    prev=[0xbe6B0x56e], succ=[0xbeeB0x56e]
    =================================
    0xa76S0xbe6S0x56e: va76Vbe6V56e(0x0) = CONST 
    0xa78S0xbe6S0x56e: va78Vbe6V56e = SLOAD va76Vbe6V56e(0x0)
    0xa79S0xbe6S0x56e: va79Vbe6V56e(0x1) = CONST 
    0xa7bS0xbe6S0x56e: va7bVbe6V56e(0xa0) = CONST 
    0xa7dS0xbe6S0x56e: va7dVbe6V56e(0x2) = CONST 
    0xa7fS0xbe6S0x56e: va7fVbe6V56e(0x10000000000000000000000000000000000000000) = EXP va7dVbe6V56e(0x2), va7bVbe6V56e(0xa0)
    0xa80S0xbe6S0x56e: va80Vbe6V56e(0xffffffffffffffffffffffffffffffffffffffff) = SUB va7fVbe6V56e(0x10000000000000000000000000000000000000000), va79Vbe6V56e(0x1)
    0xa81S0xbe6S0x56e: va81Vbe6V56e = AND va80Vbe6V56e(0xffffffffffffffffffffffffffffffffffffffff), va78Vbe6V56e
    0xa82S0xbe6S0x56e: va82Vbe6V56e = CALLER 
    0xa83S0xbe6S0x56e: va83Vbe6V56e = EQ va82Vbe6V56e, va81Vbe6V56e
    0xa85S0xbe6S0x56e: JUMP vbe7V56e(0xbee)

    Begin block 0xbeeB0x56e
    prev=[0xa75B0xbe6B0x56e], succ=[0xbf5B0x56e, 0xc44B0x56e]
    =================================
    0xbefS0x56e: vbefV56e = ISZERO va83Vbe6V56e
    0xbf0S0x56e: vbf0V56e = ISZERO vbefV56e
    0xbf1S0x56e: vbf1V56e(0xc44) = CONST 
    0xbf4S0x56e: JUMPI vbf1V56e(0xc44), vbf0V56e

    Begin block 0xbf5B0x56e
    prev=[0xbeeB0x56e], succ=[]
    =================================
    0xbf5S0x56e: vbf5V56e(0x40) = CONST 
    0xbf8S0x56e: vbf8V56e = MLOAD vbf5V56e(0x40)
    0xbf9S0x56e: vbf9V56e(0xe5) = CONST 
    0xbfbS0x56e: vbfbV56e(0x2) = CONST 
    0xbfdS0x56e: vbfdV56e(0x2000000000000000000000000000000000000000000000000000000000) = EXP vbfbV56e(0x2), vbf9V56e(0xe5)
    0xbfeS0x56e: vbfeV56e(0x461bcd) = CONST 
    0xc02S0x56e: vc02V56e(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vbfeV56e(0x461bcd), vbfdV56e(0x2000000000000000000000000000000000000000000000000000000000)
    0xc04S0x56e: MSTORE vbf8V56e, vc02V56e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc05S0x56e: vc05V56e(0x20) = CONST 
    0xc07S0x56e: vc07V56e(0x4) = CONST 
    0xc0aS0x56e: vc0aV56e = ADD vbf8V56e, vc07V56e(0x4)
    0xc0dS0x56e: MSTORE vc0aV56e, vc05V56e(0x20)
    0xc0eS0x56e: vc0eV56e(0x24) = CONST 
    0xc11S0x56e: vc11V56e = ADD vbf8V56e, vc0eV56e(0x24)
    0xc12S0x56e: MSTORE vc11V56e, vc05V56e(0x20)
    0xc13S0x56e: vc13V56e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xc34S0x56e: vc34V56e(0x44) = CONST 
    0xc37S0x56e: vc37V56e = ADD vbf8V56e, vc34V56e(0x44)
    0xc38S0x56e: MSTORE vc37V56e, vc13V56e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xc3aS0x56e: vc3aV56e = MLOAD vbf5V56e(0x40)
    0xc3eS0x56e: vc3eV56e(0x0) = SUB vbf8V56e, vc3aV56e
    0xc3fS0x56e: vc3fV56e(0x64) = CONST 
    0xc41S0x56e: vc41V56e(0x64) = ADD vc3fV56e(0x64), vc3eV56e(0x0)
    0xc43S0x56e: REVERT vc3aV56e, vc41V56e(0x64)

    Begin block 0xc44B0x56e
    prev=[0xbeeB0x56e], succ=[0x132eB0x56e]
    =================================
    0xc45S0x56e: vc45V56e(0xc4d) = CONST 
    0xc49S0x56e: vc49V56e(0x132e) = CONST 
    0xc4cS0x56e: JUMP vc49V56e(0x132e)

    Begin block 0x132eB0x56e
    prev=[0xc44B0x56e], succ=[0x133fB0x56e, 0x13b4B0x56e]
    =================================
    0x132fS0x56e: v132fV56e(0x1) = CONST 
    0x1331S0x56e: v1331V56e(0xa0) = CONST 
    0x1333S0x56e: v1333V56e(0x2) = CONST 
    0x1335S0x56e: v1335V56e(0x10000000000000000000000000000000000000000) = EXP v1333V56e(0x2), v1331V56e(0xa0)
    0x1336S0x56e: v1336V56e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1335V56e(0x10000000000000000000000000000000000000000), v132fV56e(0x1)
    0x1338S0x56e: v1338V56e = AND v579, v1336V56e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1339S0x56e: v1339V56e = ISZERO v1338V56e
    0x133aS0x56e: v133aV56e = ISZERO v1339V56e
    0x133bS0x56e: v133bV56e(0x13b4) = CONST 
    0x133eS0x56e: JUMPI v133bV56e(0x13b4), v133aV56e

    Begin block 0x133fB0x56e
    prev=[0x132eB0x56e], succ=[]
    =================================
    0x133fS0x56e: v133fV56e(0x40) = CONST 
    0x1342S0x56e: v1342V56e = MLOAD v133fV56e(0x40)
    0x1343S0x56e: v1343V56e(0xe5) = CONST 
    0x1345S0x56e: v1345V56e(0x2) = CONST 
    0x1347S0x56e: v1347V56e(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1345V56e(0x2), v1343V56e(0xe5)
    0x1348S0x56e: v1348V56e(0x461bcd) = CONST 
    0x134cS0x56e: v134cV56e(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1348V56e(0x461bcd), v1347V56e(0x2000000000000000000000000000000000000000000000000000000000)
    0x134eS0x56e: MSTORE v1342V56e, v134cV56e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x134fS0x56e: v134fV56e(0x20) = CONST 
    0x1351S0x56e: v1351V56e(0x4) = CONST 
    0x1354S0x56e: v1354V56e = ADD v1342V56e, v1351V56e(0x4)
    0x1355S0x56e: MSTORE v1354V56e, v134fV56e(0x20)
    0x1356S0x56e: v1356V56e(0x26) = CONST 
    0x1358S0x56e: v1358V56e(0x24) = CONST 
    0x135bS0x56e: v135bV56e = ADD v1342V56e, v1358V56e(0x24)
    0x135cS0x56e: MSTORE v135bV56e, v1356V56e(0x26)
    0x135dS0x56e: v135dV56e(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061) = CONST 
    0x137eS0x56e: v137eV56e(0x44) = CONST 
    0x1381S0x56e: v1381V56e = ADD v1342V56e, v137eV56e(0x44)
    0x1382S0x56e: MSTORE v1381V56e, v135dV56e(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061)
    0x1383S0x56e: v1383V56e(0x6464726573730000000000000000000000000000000000000000000000000000) = CONST 
    0x13a4S0x56e: v13a4V56e(0x64) = CONST 
    0x13a7S0x56e: v13a7V56e = ADD v1342V56e, v13a4V56e(0x64)
    0x13a8S0x56e: MSTORE v13a7V56e, v1383V56e(0x6464726573730000000000000000000000000000000000000000000000000000)
    0x13aaS0x56e: v13aaV56e = MLOAD v133fV56e(0x40)
    0x13aeS0x56e: v13aeV56e(0x0) = SUB v1342V56e, v13aaV56e
    0x13afS0x56e: v13afV56e(0x84) = CONST 
    0x13b1S0x56e: v13b1V56e(0x84) = ADD v13afV56e(0x84), v13aeV56e(0x0)
    0x13b3S0x56e: REVERT v13aaV56e, v13b1V56e(0x84)

    Begin block 0x13b4B0x56e
    prev=[0x132eB0x56e], succ=[0xc4dB0x56e]
    =================================
    0x13b5S0x56e: v13b5V56e(0x0) = CONST 
    0x13b8S0x56e: v13b8V56e = SLOAD v13b5V56e(0x0)
    0x13b9S0x56e: v13b9V56e(0x40) = CONST 
    0x13bbS0x56e: v13bbV56e = MLOAD v13b9V56e(0x40)
    0x13bcS0x56e: v13bcV56e(0x1) = CONST 
    0x13beS0x56e: v13beV56e(0xa0) = CONST 
    0x13c0S0x56e: v13c0V56e(0x2) = CONST 
    0x13c2S0x56e: v13c2V56e(0x10000000000000000000000000000000000000000) = EXP v13c0V56e(0x2), v13beV56e(0xa0)
    0x13c3S0x56e: v13c3V56e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13c2V56e(0x10000000000000000000000000000000000000000), v13bcV56e(0x1)
    0x13c6S0x56e: v13c6V56e = AND v579, v13c3V56e(0xffffffffffffffffffffffffffffffffffffffff)
    0x13c9S0x56e: v13c9V56e = AND v13b8V56e, v13c3V56e(0xffffffffffffffffffffffffffffffffffffffff)
    0x13cbS0x56e: v13cbV56e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x13edS0x56e: LOG3 v13bbV56e, v13b5V56e(0x0), v13cbV56e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v13c9V56e, v13c6V56e
    0x13eeS0x56e: v13eeV56e(0x0) = CONST 
    0x13f1S0x56e: v13f1V56e = SLOAD v13eeV56e(0x0)
    0x13f2S0x56e: v13f2V56e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1407S0x56e: v1407V56e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v13f2V56e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1408S0x56e: v1408V56e = AND v1407V56e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v13f1V56e
    0x1409S0x56e: v1409V56e(0x1) = CONST 
    0x140bS0x56e: v140bV56e(0xa0) = CONST 
    0x140dS0x56e: v140dV56e(0x2) = CONST 
    0x140fS0x56e: v140fV56e(0x10000000000000000000000000000000000000000) = EXP v140dV56e(0x2), v140bV56e(0xa0)
    0x1410S0x56e: v1410V56e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v140fV56e(0x10000000000000000000000000000000000000000), v1409V56e(0x1)
    0x1414S0x56e: v1414V56e = AND v1410V56e(0xffffffffffffffffffffffffffffffffffffffff), v579
    0x1418S0x56e: v1418V56e = OR v1414V56e, v1408V56e
    0x141aS0x56e: SSTORE v13eeV56e(0x0), v1418V56e
    0x141bS0x56e: JUMP vc45V56e(0xc4d)

    Begin block 0xc4dB0x56e
    prev=[0x13b4B0x56e], succ=[0xfc4a]
    =================================
    0xc4fS0x56e: JUMP v559(0xfc4a)

    Begin block 0xfc4a
    prev=[0xc4dB0x56e], succ=[]
    =================================
    0xfc4b: STOP 

}

function setLoaner(address)() public {
    Begin block 0x57e
    prev=[], succ=[0x586, 0x58a]
    =================================
    0x57f: v57f = CALLVALUE 
    0x581: v581 = ISZERO v57f
    0x582: v582(0x58a) = CONST 
    0x585: JUMPI v582(0x58a), v581

    Begin block 0x586
    prev=[0x57e], succ=[]
    =================================
    0x586: v586(0x0) = CONST 
    0x589: REVERT v586(0x0), v586(0x0)

    Begin block 0x58a
    prev=[0x57e], succ=[0x59d, 0x5a1]
    =================================
    0x58c: v58c(0xfc6b) = CONST 
    0x58f: v58f(0x4) = CONST 
    0x592: v592 = CALLDATASIZE 
    0x593: v593 = SUB v592, v58f(0x4)
    0x594: v594(0x20) = CONST 
    0x597: v597 = LT v593, v594(0x20)
    0x598: v598 = ISZERO v597
    0x599: v599(0x5a1) = CONST 
    0x59c: JUMPI v599(0x5a1), v598

    Begin block 0x59d
    prev=[0x58a], succ=[]
    =================================
    0x59d: v59d(0x0) = CONST 
    0x5a0: REVERT v59d(0x0), v59d(0x0)

    Begin block 0x5a1
    prev=[0x58a], succ=[0xc50]
    =================================
    0x5a3: v5a3 = CALLDATALOAD v58f(0x4)
    0x5a4: v5a4(0x1) = CONST 
    0x5a6: v5a6(0xa0) = CONST 
    0x5a8: v5a8(0x2) = CONST 
    0x5aa: v5aa(0x10000000000000000000000000000000000000000) = EXP v5a8(0x2), v5a6(0xa0)
    0x5ab: v5ab(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5aa(0x10000000000000000000000000000000000000000), v5a4(0x1)
    0x5ac: v5ac = AND v5ab(0xffffffffffffffffffffffffffffffffffffffff), v5a3
    0x5ad: v5ad(0xc50) = CONST 
    0x5b0: JUMP v5ad(0xc50)

    Begin block 0xc50
    prev=[0x5a1], succ=[0xa75B0xc50]
    =================================
    0xc51: vc51(0xc58) = CONST 
    0xc54: vc54(0xa75) = CONST 
    0xc57: JUMP vc54(0xa75)

    Begin block 0xa75B0xc50
    prev=[0xc50], succ=[0xc58]
    =================================
    0xa76S0xc50: va76Vc50(0x0) = CONST 
    0xa78S0xc50: va78Vc50 = SLOAD va76Vc50(0x0)
    0xa79S0xc50: va79Vc50(0x1) = CONST 
    0xa7bS0xc50: va7bVc50(0xa0) = CONST 
    0xa7dS0xc50: va7dVc50(0x2) = CONST 
    0xa7fS0xc50: va7fVc50(0x10000000000000000000000000000000000000000) = EXP va7dVc50(0x2), va7bVc50(0xa0)
    0xa80S0xc50: va80Vc50(0xffffffffffffffffffffffffffffffffffffffff) = SUB va7fVc50(0x10000000000000000000000000000000000000000), va79Vc50(0x1)
    0xa81S0xc50: va81Vc50 = AND va80Vc50(0xffffffffffffffffffffffffffffffffffffffff), va78Vc50
    0xa82S0xc50: va82Vc50 = CALLER 
    0xa83S0xc50: va83Vc50 = EQ va82Vc50, va81Vc50
    0xa85S0xc50: JUMP vc51(0xc58)

    Begin block 0xc58
    prev=[0xa75B0xc50], succ=[0xc5f, 0xcae]
    =================================
    0xc59: vc59 = ISZERO va83Vc50
    0xc5a: vc5a = ISZERO vc59
    0xc5b: vc5b(0xcae) = CONST 
    0xc5e: JUMPI vc5b(0xcae), vc5a

    Begin block 0xc5f
    prev=[0xc58], succ=[]
    =================================
    0xc5f: vc5f(0x40) = CONST 
    0xc62: vc62 = MLOAD vc5f(0x40)
    0xc63: vc63(0xe5) = CONST 
    0xc65: vc65(0x2) = CONST 
    0xc67: vc67(0x2000000000000000000000000000000000000000000000000000000000) = EXP vc65(0x2), vc63(0xe5)
    0xc68: vc68(0x461bcd) = CONST 
    0xc6c: vc6c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vc68(0x461bcd), vc67(0x2000000000000000000000000000000000000000000000000000000000)
    0xc6e: MSTORE vc62, vc6c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc6f: vc6f(0x20) = CONST 
    0xc71: vc71(0x4) = CONST 
    0xc74: vc74 = ADD vc62, vc71(0x4)
    0xc77: MSTORE vc74, vc6f(0x20)
    0xc78: vc78(0x24) = CONST 
    0xc7b: vc7b = ADD vc62, vc78(0x24)
    0xc7c: MSTORE vc7b, vc6f(0x20)
    0xc7d: vc7d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xc9e: vc9e(0x44) = CONST 
    0xca1: vca1 = ADD vc62, vc9e(0x44)
    0xca2: MSTORE vca1, vc7d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xca4: vca4 = MLOAD vc5f(0x40)
    0xca8: vca8(0x0) = SUB vc62, vca4
    0xca9: vca9(0x64) = CONST 
    0xcab: vcab(0x64) = ADD vca9(0x64), vca8(0x0)
    0xcad: REVERT vca4, vcab(0x64)

    Begin block 0xcae
    prev=[0xc58], succ=[0xfc6b]
    =================================
    0xcaf: vcaf(0x9) = CONST 
    0xcb2: vcb2 = SLOAD vcaf(0x9)
    0xcb3: vcb3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcc8: vcc8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vcb3(0xffffffffffffffffffffffffffffffffffffffff)
    0xcc9: vcc9 = AND vcc8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vcb2
    0xcca: vcca(0x1) = CONST 
    0xccc: vccc(0xa0) = CONST 
    0xcce: vcce(0x2) = CONST 
    0xcd0: vcd0(0x10000000000000000000000000000000000000000) = EXP vcce(0x2), vccc(0xa0)
    0xcd1: vcd1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcd0(0x10000000000000000000000000000000000000000), vcca(0x1)
    0xcd5: vcd5 = AND vcd1(0xffffffffffffffffffffffffffffffffffffffff), v5ac
    0xcd9: vcd9 = OR vcd5, vcc9
    0xcdb: SSTORE vcaf(0x9), vcd9
    0xcdc: JUMP v58c(0xfc6b)

    Begin block 0xfc6b
    prev=[0xcae], succ=[]
    =================================
    0xfc6c: STOP 

}

function 0xcdd(vcddarg0, vcddarg1, vcddarg2, vcddarg3) private {
    Begin block 0xcdd
    prev=[], succ=[0xcee, 0xd62]
    =================================
    0xcde: vcde(0x1) = CONST 
    0xce0: vce0(0xa0) = CONST 
    0xce2: vce2(0x2) = CONST 
    0xce4: vce4(0x10000000000000000000000000000000000000000) = EXP vce2(0x2), vce0(0xa0)
    0xce5: vce5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce4(0x10000000000000000000000000000000000000000), vcde(0x1)
    0xce7: vce7 = AND vcddarg2, vce5(0xffffffffffffffffffffffffffffffffffffffff)
    0xce8: vce8 = ISZERO vce7
    0xce9: vce9 = ISZERO vce8
    0xcea: vcea(0xd62) = CONST 
    0xced: JUMPI vcea(0xd62), vce9

    Begin block 0xcee
    prev=[0xcdd], succ=[]
    =================================
    0xcee: vcee(0x40) = CONST 
    0xcf1: vcf1 = MLOAD vcee(0x40)
    0xcf2: vcf2(0xe5) = CONST 
    0xcf4: vcf4(0x2) = CONST 
    0xcf6: vcf6(0x2000000000000000000000000000000000000000000000000000000000) = EXP vcf4(0x2), vcf2(0xe5)
    0xcf7: vcf7(0x461bcd) = CONST 
    0xcfb: vcfb(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vcf7(0x461bcd), vcf6(0x2000000000000000000000000000000000000000000000000000000000)
    0xcfd: MSTORE vcf1, vcfb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xcfe: vcfe(0x20) = CONST 
    0xd00: vd00(0x4) = CONST 
    0xd03: vd03 = ADD vcf1, vd00(0x4)
    0xd04: MSTORE vd03, vcfe(0x20)
    0xd05: vd05(0x24) = CONST 
    0xd09: vd09 = ADD vcf1, vd05(0x24)
    0xd0a: MSTORE vd09, vd05(0x24)
    0xd0b: vd0b(0x45524332303a20617070726f76652066726f6d20746865207a65726f20616464) = CONST 
    0xd2c: vd2c(0x44) = CONST 
    0xd2f: vd2f = ADD vcf1, vd2c(0x44)
    0xd30: MSTORE vd2f, vd0b(0x45524332303a20617070726f76652066726f6d20746865207a65726f20616464)
    0xd31: vd31(0x7265737300000000000000000000000000000000000000000000000000000000) = CONST 
    0xd52: vd52(0x64) = CONST 
    0xd55: vd55 = ADD vcf1, vd52(0x64)
    0xd56: MSTORE vd55, vd31(0x7265737300000000000000000000000000000000000000000000000000000000)
    0xd58: vd58 = MLOAD vcee(0x40)
    0xd5c: vd5c(0x0) = SUB vcf1, vd58
    0xd5d: vd5d(0x84) = CONST 
    0xd5f: vd5f(0x84) = ADD vd5d(0x84), vd5c(0x0)
    0xd61: REVERT vd58, vd5f(0x84)

    Begin block 0xd62
    prev=[0xcdd], succ=[0xd73, 0xde8]
    =================================
    0xd63: vd63(0x1) = CONST 
    0xd65: vd65(0xa0) = CONST 
    0xd67: vd67(0x2) = CONST 
    0xd69: vd69(0x10000000000000000000000000000000000000000) = EXP vd67(0x2), vd65(0xa0)
    0xd6a: vd6a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd69(0x10000000000000000000000000000000000000000), vd63(0x1)
    0xd6c: vd6c = AND vcddarg1, vd6a(0xffffffffffffffffffffffffffffffffffffffff)
    0xd6d: vd6d = ISZERO vd6c
    0xd6e: vd6e = ISZERO vd6d
    0xd6f: vd6f(0xde8) = CONST 
    0xd72: JUMPI vd6f(0xde8), vd6e

    Begin block 0xd73
    prev=[0xd62], succ=[]
    =================================
    0xd73: vd73(0x40) = CONST 
    0xd76: vd76 = MLOAD vd73(0x40)
    0xd77: vd77(0xe5) = CONST 
    0xd79: vd79(0x2) = CONST 
    0xd7b: vd7b(0x2000000000000000000000000000000000000000000000000000000000) = EXP vd79(0x2), vd77(0xe5)
    0xd7c: vd7c(0x461bcd) = CONST 
    0xd80: vd80(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vd7c(0x461bcd), vd7b(0x2000000000000000000000000000000000000000000000000000000000)
    0xd82: MSTORE vd76, vd80(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd83: vd83(0x20) = CONST 
    0xd85: vd85(0x4) = CONST 
    0xd88: vd88 = ADD vd76, vd85(0x4)
    0xd89: MSTORE vd88, vd83(0x20)
    0xd8a: vd8a(0x22) = CONST 
    0xd8c: vd8c(0x24) = CONST 
    0xd8f: vd8f = ADD vd76, vd8c(0x24)
    0xd90: MSTORE vd8f, vd8a(0x22)
    0xd91: vd91(0x45524332303a20617070726f766520746f20746865207a65726f206164647265) = CONST 
    0xdb2: vdb2(0x44) = CONST 
    0xdb5: vdb5 = ADD vd76, vdb2(0x44)
    0xdb6: MSTORE vdb5, vd91(0x45524332303a20617070726f766520746f20746865207a65726f206164647265)
    0xdb7: vdb7(0x7373000000000000000000000000000000000000000000000000000000000000) = CONST 
    0xdd8: vdd8(0x64) = CONST 
    0xddb: vddb = ADD vd76, vdd8(0x64)
    0xddc: MSTORE vddb, vdb7(0x7373000000000000000000000000000000000000000000000000000000000000)
    0xdde: vdde = MLOAD vd73(0x40)
    0xde2: vde2(0x0) = SUB vd76, vdde
    0xde3: vde3(0x84) = CONST 
    0xde5: vde5(0x84) = ADD vde3(0x84), vde2(0x0)
    0xde7: REVERT vdde, vde5(0x84)

    Begin block 0xde8
    prev=[0xd62], succ=[]
    =================================
    0xde9: vde9(0x1) = CONST 
    0xdeb: vdeb(0xa0) = CONST 
    0xded: vded(0x2) = CONST 
    0xdef: vdef(0x10000000000000000000000000000000000000000) = EXP vded(0x2), vdeb(0xa0)
    0xdf0: vdf0(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdef(0x10000000000000000000000000000000000000000), vde9(0x1)
    0xdf3: vdf3 = AND vcddarg2, vdf0(0xffffffffffffffffffffffffffffffffffffffff)
    0xdf4: vdf4(0x0) = CONST 
    0xdf8: MSTORE vdf4(0x0), vdf3
    0xdf9: vdf9(0x2) = CONST 
    0xdfb: vdfb(0x20) = CONST 
    0xdff: MSTORE vdfb(0x20), vdf9(0x2)
    0xe00: ve00(0x40) = CONST 
    0xe04: ve04 = SHA3 vdf4(0x0), ve00(0x40)
    0xe07: ve07 = AND vcddarg1, vdf0(0xffffffffffffffffffffffffffffffffffffffff)
    0xe0a: MSTORE vdf4(0x0), ve07
    0xe0d: MSTORE vdfb(0x20), ve04
    0xe11: ve11 = SHA3 vdf4(0x0), ve00(0x40)
    0xe14: SSTORE ve11, vcddarg0
    0xe16: ve16 = MLOAD ve00(0x40)
    0xe19: MSTORE ve16, vcddarg0
    0xe1b: ve1b = MLOAD ve00(0x40)
    0xe1c: ve1c(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xe40: ve40(0x0) = SUB ve16, ve1b
    0xe43: ve43(0x20) = ADD vdfb(0x20), ve40(0x0)
    0xe45: LOG3 ve1b, ve43(0x20), ve1c(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vdf3, ve07
    0xe49: RETURNPRIVATE vcddarg3

}

function 0xe4a(ve4aarg0, ve4aarg1, ve4aarg2, ve4aarg3) private {
    Begin block 0xe4a
    prev=[], succ=[0xe5b, 0xed0]
    =================================
    0xe4b: ve4b(0x1) = CONST 
    0xe4d: ve4d(0xa0) = CONST 
    0xe4f: ve4f(0x2) = CONST 
    0xe51: ve51(0x10000000000000000000000000000000000000000) = EXP ve4f(0x2), ve4d(0xa0)
    0xe52: ve52(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve51(0x10000000000000000000000000000000000000000), ve4b(0x1)
    0xe54: ve54 = AND ve4aarg2, ve52(0xffffffffffffffffffffffffffffffffffffffff)
    0xe55: ve55 = ISZERO ve54
    0xe56: ve56 = ISZERO ve55
    0xe57: ve57(0xed0) = CONST 
    0xe5a: JUMPI ve57(0xed0), ve56

    Begin block 0xe5b
    prev=[0xe4a], succ=[]
    =================================
    0xe5b: ve5b(0x40) = CONST 
    0xe5e: ve5e = MLOAD ve5b(0x40)
    0xe5f: ve5f(0xe5) = CONST 
    0xe61: ve61(0x2) = CONST 
    0xe63: ve63(0x2000000000000000000000000000000000000000000000000000000000) = EXP ve61(0x2), ve5f(0xe5)
    0xe64: ve64(0x461bcd) = CONST 
    0xe68: ve68(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL ve64(0x461bcd), ve63(0x2000000000000000000000000000000000000000000000000000000000)
    0xe6a: MSTORE ve5e, ve68(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe6b: ve6b(0x20) = CONST 
    0xe6d: ve6d(0x4) = CONST 
    0xe70: ve70 = ADD ve5e, ve6d(0x4)
    0xe71: MSTORE ve70, ve6b(0x20)
    0xe72: ve72(0x25) = CONST 
    0xe74: ve74(0x24) = CONST 
    0xe77: ve77 = ADD ve5e, ve74(0x24)
    0xe78: MSTORE ve77, ve72(0x25)
    0xe79: ve79(0x45524332303a207472616e736665722066726f6d20746865207a65726f206164) = CONST 
    0xe9a: ve9a(0x44) = CONST 
    0xe9d: ve9d = ADD ve5e, ve9a(0x44)
    0xe9e: MSTORE ve9d, ve79(0x45524332303a207472616e736665722066726f6d20746865207a65726f206164)
    0xe9f: ve9f(0x6472657373000000000000000000000000000000000000000000000000000000) = CONST 
    0xec0: vec0(0x64) = CONST 
    0xec3: vec3 = ADD ve5e, vec0(0x64)
    0xec4: MSTORE vec3, ve9f(0x6472657373000000000000000000000000000000000000000000000000000000)
    0xec6: vec6 = MLOAD ve5b(0x40)
    0xeca: veca(0x0) = SUB ve5e, vec6
    0xecb: vecb(0x84) = CONST 
    0xecd: vecd(0x84) = ADD vecb(0x84), veca(0x0)
    0xecf: REVERT vec6, vecd(0x84)

    Begin block 0xed0
    prev=[0xe4a], succ=[0xee1, 0xf56]
    =================================
    0xed1: ved1(0x1) = CONST 
    0xed3: ved3(0xa0) = CONST 
    0xed5: ved5(0x2) = CONST 
    0xed7: ved7(0x10000000000000000000000000000000000000000) = EXP ved5(0x2), ved3(0xa0)
    0xed8: ved8(0xffffffffffffffffffffffffffffffffffffffff) = SUB ved7(0x10000000000000000000000000000000000000000), ved1(0x1)
    0xeda: veda = AND ve4aarg1, ved8(0xffffffffffffffffffffffffffffffffffffffff)
    0xedb: vedb = ISZERO veda
    0xedc: vedc = ISZERO vedb
    0xedd: vedd(0xf56) = CONST 
    0xee0: JUMPI vedd(0xf56), vedc

    Begin block 0xee1
    prev=[0xed0], succ=[]
    =================================
    0xee1: vee1(0x40) = CONST 
    0xee4: vee4 = MLOAD vee1(0x40)
    0xee5: vee5(0xe5) = CONST 
    0xee7: vee7(0x2) = CONST 
    0xee9: vee9(0x2000000000000000000000000000000000000000000000000000000000) = EXP vee7(0x2), vee5(0xe5)
    0xeea: veea(0x461bcd) = CONST 
    0xeee: veee(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL veea(0x461bcd), vee9(0x2000000000000000000000000000000000000000000000000000000000)
    0xef0: MSTORE vee4, veee(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xef1: vef1(0x20) = CONST 
    0xef3: vef3(0x4) = CONST 
    0xef6: vef6 = ADD vee4, vef3(0x4)
    0xef7: MSTORE vef6, vef1(0x20)
    0xef8: vef8(0x23) = CONST 
    0xefa: vefa(0x24) = CONST 
    0xefd: vefd = ADD vee4, vefa(0x24)
    0xefe: MSTORE vefd, vef8(0x23)
    0xeff: veff(0x45524332303a207472616e7366657220746f20746865207a65726f2061646472) = CONST 
    0xf20: vf20(0x44) = CONST 
    0xf23: vf23 = ADD vee4, vf20(0x44)
    0xf24: MSTORE vf23, veff(0x45524332303a207472616e7366657220746f20746865207a65726f2061646472)
    0xf25: vf25(0x6573730000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf46: vf46(0x64) = CONST 
    0xf49: vf49 = ADD vee4, vf46(0x64)
    0xf4a: MSTORE vf49, vf25(0x6573730000000000000000000000000000000000000000000000000000000000)
    0xf4c: vf4c = MLOAD vee1(0x40)
    0xf50: vf50(0x0) = SUB vee4, vf4c
    0xf51: vf51(0x84) = CONST 
    0xf53: vf53(0x84) = ADD vf51(0x84), vf50(0x0)
    0xf55: REVERT vf4c, vf53(0x84)

    Begin block 0xf56
    prev=[0xed0], succ=[0xf7f]
    =================================
    0xf57: vf57(0x1) = CONST 
    0xf59: vf59(0xa0) = CONST 
    0xf5b: vf5b(0x2) = CONST 
    0xf5d: vf5d(0x10000000000000000000000000000000000000000) = EXP vf5b(0x2), vf59(0xa0)
    0xf5e: vf5e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf5d(0x10000000000000000000000000000000000000000), vf57(0x1)
    0xf60: vf60 = AND ve4aarg2, vf5e(0xffffffffffffffffffffffffffffffffffffffff)
    0xf61: vf61(0x0) = CONST 
    0xf65: MSTORE vf61(0x0), vf60
    0xf66: vf66(0x1) = CONST 
    0xf68: vf68(0x20) = CONST 
    0xf6a: MSTORE vf68(0x20), vf66(0x1)
    0xf6b: vf6b(0x40) = CONST 
    0xf6e: vf6e = SHA3 vf61(0x0), vf6b(0x40)
    0xf6f: vf6f = SLOAD vf6e
    0xf70: vf70(0xf7f) = CONST 
    0xf75: vf75(0xffffffff) = CONST 
    0xf7a: vf7a(0x1010) = CONST 
    0xf7d: vf7d(0x1010) = AND vf7a(0x1010), vf75(0xffffffff)
    0xf7e: vf7e_0 = CALLPRIVATE vf7d(0x1010), ve4aarg0, vf6f, vf70(0xf7f)

    Begin block 0xf7f
    prev=[0xf56], succ=[0xfb4]
    =================================
    0xf80: vf80(0x1) = CONST 
    0xf82: vf82(0xa0) = CONST 
    0xf84: vf84(0x2) = CONST 
    0xf86: vf86(0x10000000000000000000000000000000000000000) = EXP vf84(0x2), vf82(0xa0)
    0xf87: vf87(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf86(0x10000000000000000000000000000000000000000), vf80(0x1)
    0xf8a: vf8a = AND ve4aarg2, vf87(0xffffffffffffffffffffffffffffffffffffffff)
    0xf8b: vf8b(0x0) = CONST 
    0xf8f: MSTORE vf8b(0x0), vf8a
    0xf90: vf90(0x1) = CONST 
    0xf92: vf92(0x20) = CONST 
    0xf94: MSTORE vf92(0x20), vf90(0x1)
    0xf95: vf95(0x40) = CONST 
    0xf99: vf99 = SHA3 vf8b(0x0), vf95(0x40)
    0xf9d: SSTORE vf99, vf7e_0
    0xfa0: vfa0 = AND ve4aarg1, vf87(0xffffffffffffffffffffffffffffffffffffffff)
    0xfa2: MSTORE vf8b(0x0), vfa0
    0xfa3: vfa3 = SHA3 vf8b(0x0), vf95(0x40)
    0xfa4: vfa4 = SLOAD vfa3
    0xfa5: vfa5(0xfb4) = CONST 
    0xfaa: vfaa(0xffffffff) = CONST 
    0xfaf: vfaf(0x12c3) = CONST 
    0xfb2: vfb2(0x12c3) = AND vfaf(0x12c3), vfaa(0xffffffff)
    0xfb3: vfb3_0 = CALLPRIVATE vfb2(0x12c3), ve4aarg0, vfa4, vfa5(0xfb4)

    Begin block 0xfb4
    prev=[0xf7f], succ=[]
    =================================
    0xfb5: vfb5(0x1) = CONST 
    0xfb7: vfb7(0xa0) = CONST 
    0xfb9: vfb9(0x2) = CONST 
    0xfbb: vfbb(0x10000000000000000000000000000000000000000) = EXP vfb9(0x2), vfb7(0xa0)
    0xfbc: vfbc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfbb(0x10000000000000000000000000000000000000000), vfb5(0x1)
    0xfbf: vfbf = AND ve4aarg1, vfbc(0xffffffffffffffffffffffffffffffffffffffff)
    0xfc0: vfc0(0x0) = CONST 
    0xfc4: MSTORE vfc0(0x0), vfbf
    0xfc5: vfc5(0x1) = CONST 
    0xfc7: vfc7(0x20) = CONST 
    0xfcb: MSTORE vfc7(0x20), vfc5(0x1)
    0xfcc: vfcc(0x40) = CONST 
    0xfd1: vfd1 = SHA3 vfc0(0x0), vfcc(0x40)
    0xfd5: SSTORE vfd1, vfb3_0
    0xfd7: vfd7 = MLOAD vfcc(0x40)
    0xfda: MSTORE vfd7, ve4aarg0
    0xfdc: vfdc = MLOAD vfcc(0x40)
    0xfe1: vfe1 = AND ve4aarg2, vfbc(0xffffffffffffffffffffffffffffffffffffffff)
    0xfe3: vfe3(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1008: v1008(0x0) = SUB vfd7, vfdc
    0x1009: v1009(0x20) = ADD v1008(0x0), vfc7(0x20)
    0x100b: LOG3 vfdc, v1009(0x20), vfe3(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vfe1, vfbf
    0x100f: RETURNPRIVATE ve4aarg3

}

