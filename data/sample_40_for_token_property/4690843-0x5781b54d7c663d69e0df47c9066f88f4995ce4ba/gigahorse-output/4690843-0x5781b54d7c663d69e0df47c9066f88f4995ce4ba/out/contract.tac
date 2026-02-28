function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xe, 0x6e410]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x64410: v64410(0x6e410) = CONST 
    0x64430: JUMPI v64410(0x6e410), v8

    Begin block 0xe
    prev=[0x0], succ=[0x6ee10, 0x43]
    =================================
    0xe: ve(0x0) = CONST 
    0x10: v10 = CALLDATALOAD ve(0x0)
    0x11: v11(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30 = DIV v10, v11(0x100000000000000000000000000000000000000000000000000000000)
    0x31: v31(0xffffffff) = CONST 
    0x36: v36 = AND v31(0xffffffff), v30
    0x38: v38(0x1905fbf6) = CONST 
    0x3d: v3d = EQ v38(0x1905fbf6), v36
    0x64e10: v64e10(0x6ee10) = CONST 
    0x64e30: JUMPI v64e10(0x6ee10), v3d

    Begin block 0x6ee10
    prev=[0xe], succ=[]
    =================================
    0x6ee30: v6ee30(0xf8) = CONST 
    0x6ee50: CALLPRIVATE v6ee30(0xf8)

    Begin block 0x43
    prev=[0xe], succ=[0x6f810, 0x4f]
    =================================
    0x44: v44(0x1c624d19) = CONST 
    0x49: v49 = EQ v44(0x1c624d19), v36
    0x65810: v65810(0x6f810) = CONST 
    0x65830: JUMPI v65810(0x6f810), v49

    Begin block 0x6f810
    prev=[0x43], succ=[]
    =================================
    0x6f830: v6f830(0x134) = CONST 
    0x6f850: CALLPRIVATE v6f830(0x134)

    Begin block 0x4f
    prev=[0x43], succ=[0x70210, 0x5b]
    =================================
    0x50: v50(0x2a11ced0) = CONST 
    0x55: v55 = EQ v50(0x2a11ced0), v36
    0x66210: v66210(0x70210) = CONST 
    0x66230: JUMPI v66210(0x70210), v55

    Begin block 0x70210
    prev=[0x4f], succ=[]
    =================================
    0x70230: v70230(0x179) = CONST 
    0x70250: CALLPRIVATE v70230(0x179)

    Begin block 0x5b
    prev=[0x4f], succ=[0x70c10, 0x67]
    =================================
    0x5c: v5c(0x4042b66f) = CONST 
    0x61: v61 = EQ v5c(0x4042b66f), v36
    0x66c10: v66c10(0x70c10) = CONST 
    0x66c30: JUMPI v66c10(0x70c10), v61

    Begin block 0x70c10
    prev=[0x5b], succ=[]
    =================================
    0x70c30: v70c30(0x1df) = CONST 
    0x70c50: CALLPRIVATE v70c30(0x1df)

    Begin block 0x67
    prev=[0x5b], succ=[0x71610, 0x73]
    =================================
    0x68: v68(0x521eb273) = CONST 
    0x6d: v6d = EQ v68(0x521eb273), v36
    0x67610: v67610(0x71610) = CONST 
    0x67630: JUMPI v67610(0x71610), v6d

    Begin block 0x71610
    prev=[0x67], succ=[]
    =================================
    0x71630: v71630(0x20b) = CONST 
    0x71650: CALLPRIVATE v71630(0x20b)

    Begin block 0x73
    prev=[0x67], succ=[0x72010, 0x7f]
    =================================
    0x74: v74(0x71a8270a) = CONST 
    0x79: v79 = EQ v74(0x71a8270a), v36
    0x68010: v68010(0x72010) = CONST 
    0x68030: JUMPI v68010(0x72010), v79

    Begin block 0x72010
    prev=[0x73], succ=[]
    =================================
    0x72030: v72030(0x263) = CONST 
    0x72050: CALLPRIVATE v72030(0x263)

    Begin block 0x7f
    prev=[0x73], succ=[0x72a10, 0x8b]
    =================================
    0x80: v80(0x8832243a) = CONST 
    0x85: v85 = EQ v80(0x8832243a), v36
    0x68a10: v68a10(0x72a10) = CONST 
    0x68a30: JUMPI v68a10(0x72a10), v85

    Begin block 0x72a10
    prev=[0x7f], succ=[]
    =================================
    0x72a30: v72a30(0x293) = CONST 
    0x72a50: CALLPRIVATE v72a30(0x293)

    Begin block 0x8b
    prev=[0x7f], succ=[0x73410, 0x97]
    =================================
    0x8c: v8c(0x8ac27f5f) = CONST 
    0x91: v91 = EQ v8c(0x8ac27f5f), v36
    0x69410: v69410(0x73410) = CONST 
    0x69430: JUMPI v69410(0x73410), v91

    Begin block 0x73410
    prev=[0x8b], succ=[]
    =================================
    0x73430: v73430(0x29f) = CONST 
    0x73450: CALLPRIVATE v73430(0x29f)

    Begin block 0x97
    prev=[0x8b], succ=[0x73e10, 0xa3]
    =================================
    0x98: v98(0x8da5cb5b) = CONST 
    0x9d: v9d = EQ v98(0x8da5cb5b), v36
    0x69e10: v69e10(0x73e10) = CONST 
    0x69e30: JUMPI v69e10(0x73e10), v9d

    Begin block 0x73e10
    prev=[0x97], succ=[]
    =================================
    0x73e30: v73e30(0x2cb) = CONST 
    0x73e50: CALLPRIVATE v73e30(0x2cb)

    Begin block 0xa3
    prev=[0x97], succ=[0x74810, 0xaf]
    =================================
    0xa4: va4(0xaf3f12bc) = CONST 
    0xa9: va9 = EQ va4(0xaf3f12bc), v36
    0x6a810: v6a810(0x74810) = CONST 
    0x6a830: JUMPI v6a810(0x74810), va9

    Begin block 0x74810
    prev=[0xa3], succ=[]
    =================================
    0x74830: v74830(0x323) = CONST 
    0x74850: CALLPRIVATE v74830(0x323)

    Begin block 0xaf
    prev=[0xa3], succ=[0x75210, 0xbb]
    =================================
    0xb0: vb0(0xd06f887b) = CONST 
    0xb5: vb5 = EQ vb0(0xd06f887b), v36
    0x6b210: v6b210(0x75210) = CONST 
    0x6b230: JUMPI v6b210(0x75210), vb5

    Begin block 0x75210
    prev=[0xaf], succ=[]
    =================================
    0x75230: v75230(0x37b) = CONST 
    0x75250: CALLPRIVATE v75230(0x37b)

    Begin block 0xbb
    prev=[0xaf], succ=[0x75c10, 0xc7]
    =================================
    0xbc: vbc(0xec8ac4d8) = CONST 
    0xc1: vc1 = EQ vbc(0xec8ac4d8), v36
    0x6bc10: v6bc10(0x75c10) = CONST 
    0x6bc30: JUMPI v6bc10(0x75c10), vc1

    Begin block 0x75c10
    prev=[0xbb], succ=[]
    =================================
    0x75c30: v75c30(0x3a1) = CONST 
    0x75c50: CALLPRIVATE v75c30(0x3a1)

    Begin block 0xc7
    prev=[0xbb], succ=[0x76610, 0xd3]
    =================================
    0xc8: vc8(0xecb70fb7) = CONST 
    0xcd: vcd = EQ vc8(0xecb70fb7), v36
    0x6c610: v6c610(0x76610) = CONST 
    0x6c630: JUMPI v6c610(0x76610), vcd

    Begin block 0x76610
    prev=[0xc7], succ=[]
    =================================
    0x76630: v76630(0x3d1) = CONST 
    0x76650: CALLPRIVATE v76630(0x3d1)

    Begin block 0xd3
    prev=[0xc7], succ=[0x77010, 0xdf]
    =================================
    0xd4: vd4(0xf2fde38b) = CONST 
    0xd9: vd9 = EQ vd4(0xf2fde38b), v36
    0x6d010: v6d010(0x77010) = CONST 
    0x6d030: JUMPI v6d010(0x77010), vd9

    Begin block 0x77010
    prev=[0xd3], succ=[]
    =================================
    0x77030: v77030(0x401) = CONST 
    0x77050: CALLPRIVATE v77030(0x401)

    Begin block 0xdf
    prev=[0xd3], succ=[0x6e410, 0x77a10]
    =================================
    0xe0: ve0(0xfc0c546a) = CONST 
    0xe5: ve5 = EQ ve0(0xfc0c546a), v36
    0x6da10: v6da10(0x77a10) = CONST 
    0x6da30: JUMPI v6da10(0x77a10), ve5

    Begin block 0x6e410
    prev=[0x0, 0xdf], succ=[]
    =================================
    0x6e430: v6e430(0xeb) = CONST 
    0x6e450: CALLPRIVATE v6e430(0xeb)

    Begin block 0x77a10
    prev=[0xdf], succ=[]
    =================================
    0x77a30: v77a30(0x43d) = CONST 
    0x77a50: CALLPRIVATE v77a30(0x43d)

}

function 0x1098(v1098arg0, v1098arg1, v1098arg2) private {
    Begin block 0x1098
    prev=[], succ=[0x10a60x1098, 0x10a70x1098]
    =================================
    0x1099: v1099(0x0) = CONST 
    0x109f: v109f = ISZERO v1098arg0
    0x10a0: v10a0 = ISZERO v109f
    0x10a1: v10a1(0x10a7) = CONST 
    0x10a5: JUMPI v10a1(0x10a7), v10a0

    Begin block 0x10a60x1098
    prev=[0x1098], succ=[]
    =================================
    0x10a60x1098: THROW 

    Begin block 0x10a70x1098
    prev=[0x1098], succ=[]
    =================================
    0x10a80x1098: v109810a8 = DIV v1098arg1, v1098arg0
    0x10b30x1098: RETURNPRIVATE v1098arg2, v109810a8

}

function 0x10bf(v10bfarg0, v10bfarg1, v10bfarg2) private {
    Begin block 0x10bf
    prev=[], succ=[0x10d3, 0x10d4]
    =================================
    0x10c0: v10c0(0x0) = CONST 
    0x10c5: v10c5 = ADD v10bfarg1, v10bfarg0
    0x10ca: v10ca = LT v10c5, v10bfarg1
    0x10cb: v10cb = ISZERO v10ca
    0x10cc: v10cc = ISZERO v10cb
    0x10cd: v10cd = ISZERO v10cc
    0x10ce: v10ce(0x10d4) = CONST 
    0x10d2: JUMPI v10ce(0x10d4), v10cd

    Begin block 0x10d3
    prev=[0x10bf], succ=[]
    =================================
    0x10d3: THROW 

    Begin block 0x10d4
    prev=[0x10bf], succ=[]
    =================================
    0x10dd: RETURNPRIVATE v10bfarg2, v10c5

}

function 0x10de(v10dearg0, v10dearg1) private {
    Begin block 0x10de
    prev=[], succ=[0x1133, 0x32090]
    =================================
    0x10df: v10df(0xc) = CONST 
    0x10e1: v10e1(0x0) = CONST 
    0x10e4: v10e4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10f9: v10f9 = AND v10e4(0xffffffffffffffffffffffffffffffffffffffff), v10dearg0
    0x10fa: v10fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x110f: v110f = AND v10fa(0xffffffffffffffffffffffffffffffffffffffff), v10f9
    0x1111: MSTORE v10e1(0x0), v110f
    0x1112: v1112(0x20) = CONST 
    0x1114: v1114(0x20) = ADD v1112(0x20), v10e1(0x0)
    0x1117: MSTORE v1114(0x20), v10df(0xc)
    0x1118: v1118(0x20) = CONST 
    0x111a: v111a(0x40) = ADD v1118(0x20), v1114(0x20)
    0x111b: v111b(0x0) = CONST 
    0x111d: v111d = SHA3 v111b(0x0), v111a(0x40)
    0x111e: v111e(0x0) = CONST 
    0x1121: v1121 = SLOAD v111d
    0x1123: v1123(0x100) = CONST 
    0x1126: v1126(0x1) = EXP v1123(0x100), v111e(0x0)
    0x1128: v1128 = DIV v1121, v1126(0x1)
    0x1129: v1129(0xff) = CONST 
    0x112b: v112b = AND v1129(0xff), v1128
    0x112c: v112c = ISZERO v112b
    0x112d: v112d = ISZERO v112c
    0x112e: v112e(0x32090) = CONST 
    0x1132: JUMPI v112e(0x32090), v112d

    Begin block 0x1133
    prev=[0x10de], succ=[0x1258B0x1133]
    =================================
    0x1133: v1133(0xd) = CONST 
    0x1136: v1136 = SLOAD v1133(0xd)
    0x1138: v1138(0x1) = CONST 
    0x113a: v113a = ADD v1138(0x1), v1136
    0x113d: v113d(0x1148) = CONST 
    0x1143: v1143(0x1258) = CONST 
    0x1147: JUMP v1143(0x1258)

    Begin block 0x1258B0x1133
    prev=[0x1133], succ=[0x1267B0x1133, 0x320b2B0x1133]
    =================================
    0x125aS0x1133: v125aV1133 = SLOAD v1133(0xd)
    0x125dS0x1133: SSTORE v1133(0xd), v113a
    0x1260S0x1133: v1260V1133 = ISZERO v125aV1133
    0x1261S0x1133: v1261V1133 = GT v1260V1133, v113a
    0x1262S0x1133: v1262V1133(0x320b2) = CONST 
    0x1266S0x1133: JUMPI v1262V1133(0x320b2), v1261V1133

    Begin block 0x1267B0x1133
    prev=[0x1258B0x1133], succ=[0x1287B0x1267B0x1133]
    =================================
    0x1269S0x1133: v1269V1133(0x0) = CONST 
    0x126bS0x1133: MSTORE v1269V1133(0x0), v1133(0xd)
    0x126cS0x1133: v126cV1133(0x20) = CONST 
    0x126eS0x1133: v126eV1133(0x0) = CONST 
    0x1270S0x1133: v1270V1133 = SHA3 v126eV1133(0x0), v126cV1133(0x20)
    0x1273S0x1133: v1273V1133 = ADD v1270V1133, v125aV1133
    0x1275S0x1133: v1275V1133 = ADD v1270V1133, v113a
    0x1276S0x1133: v1276V1133(0x1281) = CONST 
    0x127cS0x1133: v127cV1133(0x1287) = CONST 
    0x1280S0x1133: JUMP v127cV1133(0x1287)

    Begin block 0x1287B0x1267B0x1133
    prev=[0x1267B0x1133], succ=[0x128eB0x1287B0x1267B0x1133]
    =================================
    0x1288S0x1267S0x1133: v1288V1267V1133(0x12ac) = CONST 
    0xf9e2S0x1267S0x1133: vf9e2V1267V1133(0x128e) = CONST 
    0xfa02S0x1267S0x1133: JUMP vf9e2V1267V1133(0x128e)

    Begin block 0x128eB0x1287B0x1267B0x1133
    prev=[0x1287B0x1267B0x1133, 0x1298B0x1287B0x1267B0x1133], succ=[0x1298B0x1287B0x1267B0x1133, 0x12a8B0x1287B0x1267B0x1133]
    =================================
    0x128e_0x0S0x1287S0x1267S0x1133: v128e_0V1287V1267V1133 = PHI v1275V1133, v12a2V1287V1267V1133
    0x1291S0x1287S0x1267S0x1133: v1291V1287V1267V1133 = GT v1273V1133, v128e_0V1287V1267V1133
    0x1292S0x1287S0x1267S0x1133: v1292V1287V1267V1133 = ISZERO v1291V1287V1267V1133
    0x1293S0x1287S0x1267S0x1133: v1293V1287V1267V1133(0x12a8) = CONST 
    0x1297S0x1287S0x1267S0x1133: JUMPI v1293V1287V1267V1133(0x12a8), v1292V1287V1267V1133

    Begin block 0x1298B0x1287B0x1267B0x1133
    prev=[0x128eB0x1287B0x1267B0x1133], succ=[0x128eB0x1287B0x1267B0x1133]
    =================================
    0x1298S0x1287S0x1267S0x1133: v1298V1287V1267V1133(0x0) = CONST 
    0x1298_0x0S0x1287S0x1267S0x1133: v1298_0V1287V1267V1133 = PHI v1275V1133, v12a2V1287V1267V1133
    0x129bS0x1287S0x1267S0x1133: v129bV1287V1267V1133(0x0) = CONST 
    0x129eS0x1287S0x1267S0x1133: SSTORE v1298_0V1287V1267V1133, v129bV1287V1267V1133(0x0)
    0x12a0S0x1287S0x1267S0x1133: v12a0V1287V1267V1133(0x1) = CONST 
    0x12a2S0x1287S0x1267S0x1133: v12a2V1287V1267V1133 = ADD v12a0V1287V1267V1133(0x1), v1298_0V1287V1267V1133
    0x12a3S0x1287S0x1267S0x1133: v12a3V1287V1267V1133(0x128e) = CONST 
    0x12a7S0x1287S0x1267S0x1133: JUMP v12a3V1287V1267V1133(0x128e)

    Begin block 0x12a8B0x1287B0x1267B0x1133
    prev=[0x128eB0x1287B0x1267B0x1133], succ=[0x12acB0x1267B0x1133]
    =================================
    0x12abS0x1287S0x1267S0x1133: JUMP v1288V1267V1133(0x12ac)

    Begin block 0x12acB0x1267B0x1133
    prev=[0x12a8B0x1287B0x1267B0x1133], succ=[0x1281B0x1133]
    =================================
    0x12aeS0x1267S0x1133: JUMP v1276V1133(0x1281)

    Begin block 0x1281B0x1133
    prev=[0x12acB0x1267B0x1133], succ=[0x321f4B0x1133]
    =================================
    0xefe2S0x1133: vefe2V1133(0x321f4) = CONST 
    0xf002S0x1133: JUMP vefe2V1133(0x321f4)

    Begin block 0x321f4B0x1133
    prev=[0x1281B0x1133], succ=[0x1148]
    =================================
    0x321f8S0x1133: JUMP v113d(0x1148)

    Begin block 0x1148
    prev=[0x320b2B0x1133, 0x321f4B0x1133], succ=[0x321d2]
    =================================
    0x114a: v114a(0x0) = CONST 
    0x114c: MSTORE v114a(0x0), v1133(0xd)
    0x114d: v114d(0x20) = CONST 
    0x114f: v114f(0x0) = CONST 
    0x1151: v1151 = SHA3 v114f(0x0), v114d(0x20)
    0x1153: v1153 = ADD v1136, v1151
    0x1154: v1154(0x0) = CONST 
    0x115b: v115b(0x100) = CONST 
    0x115e: v115e(0x1) = EXP v115b(0x100), v1154(0x0)
    0x1160: v1160 = SLOAD v1153
    0x1162: v1162(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1177: v1177(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1162(0xffffffffffffffffffffffffffffffffffffffff), v115e(0x1)
    0x1178: v1178(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1177(0xffffffffffffffffffffffffffffffffffffffff)
    0x1179: v1179 = AND v1178(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1160
    0x117c: v117c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1191: v1191 = AND v117c(0xffffffffffffffffffffffffffffffffffffffff), v10dearg0
    0x1192: v1192 = MUL v1191, v115e(0x1)
    0x1193: v1193 = OR v1192, v1179
    0x1195: SSTORE v1153, v1193
    0x1198: v1198(0x1) = CONST 
    0x119a: v119a(0xc) = CONST 
    0x119c: v119c(0x0) = CONST 
    0x119f: v119f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11b4: v11b4 = AND v119f(0xffffffffffffffffffffffffffffffffffffffff), v10dearg0
    0x11b5: v11b5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11ca: v11ca = AND v11b5(0xffffffffffffffffffffffffffffffffffffffff), v11b4
    0x11cc: MSTORE v119c(0x0), v11ca
    0x11cd: v11cd(0x20) = CONST 
    0x11cf: v11cf(0x20) = ADD v11cd(0x20), v119c(0x0)
    0x11d2: MSTORE v11cf(0x20), v119a(0xc)
    0x11d3: v11d3(0x20) = CONST 
    0x11d5: v11d5(0x40) = ADD v11d3(0x20), v11cf(0x20)
    0x11d6: v11d6(0x0) = CONST 
    0x11d8: v11d8 = SHA3 v11d6(0x0), v11d5(0x40)
    0x11d9: v11d9(0x0) = CONST 
    0x11db: v11db(0x100) = CONST 
    0x11de: v11de(0x1) = EXP v11db(0x100), v11d9(0x0)
    0x11e0: v11e0 = SLOAD v11d8
    0x11e2: v11e2(0xff) = CONST 
    0x11e4: v11e4(0xff) = MUL v11e2(0xff), v11de(0x1)
    0x11e5: v11e5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v11e4(0xff)
    0x11e6: v11e6 = AND v11e5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v11e0
    0x11e9: v11e9(0x0) = ISZERO v1198(0x1)
    0x11ea: v11ea(0x1) = ISZERO v11e9(0x0)
    0x11eb: v11eb(0x1) = MUL v11ea(0x1), v11de(0x1)
    0x11ec: v11ec = OR v11eb(0x1), v11e6
    0x11ee: SSTORE v11d8, v11ec
    0xe5e2: ve5e2(0x321d2) = CONST 
    0xe602: JUMP ve5e2(0x321d2)

    Begin block 0x321d2
    prev=[0x1148], succ=[]
    =================================
    0x321d4: RETURNPRIVATE v10dearg1

    Begin block 0x320b2B0x1133
    prev=[0x1258B0x1133], succ=[0x1148]
    =================================
    0x320b6S0x1133: JUMP v113d(0x1148)

    Begin block 0x32090
    prev=[0x10de], succ=[]
    =================================
    0x32092: RETURNPRIVATE v10dearg1

}

function 0x11f3(v11f3arg0) private {
    Begin block 0x11f3
    prev=[], succ=[0x1252, 0x1256]
    =================================
    0x11f4: v11f4(0x2) = CONST 
    0x11f6: v11f6(0x0) = CONST 
    0x11f9: v11f9 = SLOAD v11f4(0x2)
    0x11fb: v11fb(0x100) = CONST 
    0x11fe: v11fe(0x1) = EXP v11fb(0x100), v11f6(0x0)
    0x1200: v1200 = DIV v11f9, v11fe(0x1)
    0x1201: v1201(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1216: v1216 = AND v1201(0xffffffffffffffffffffffffffffffffffffffff), v1200
    0x1217: v1217(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x122c: v122c = AND v1217(0xffffffffffffffffffffffffffffffffffffffff), v1216
    0x122d: v122d(0x8fc) = CONST 
    0x1230: v1230 = CALLVALUE 
    0x1233: v1233 = ISZERO v1230
    0x1234: v1234 = MUL v1233, v122d(0x8fc)
    0x1236: v1236(0x40) = CONST 
    0x1238: v1238 = MLOAD v1236(0x40)
    0x1239: v1239(0x0) = CONST 
    0x123b: v123b(0x40) = CONST 
    0x123d: v123d = MLOAD v123b(0x40)
    0x1240: v1240(0x0) = SUB v1238, v123d
    0x1245: v1245 = CALL v1234, v122c, v1230, v123d, v1240(0x0), v123d, v1239(0x0)
    0x124b: v124b = ISZERO v1245
    0x124c: v124c = ISZERO v124b
    0x124d: v124d(0x1256) = CONST 
    0x1251: JUMPI v124d(0x1256), v124c

    Begin block 0x1252
    prev=[0x11f3], succ=[]
    =================================
    0x1252: v1252(0x0) = CONST 
    0x1255: REVERT v1252(0x0), v1252(0x0)

    Begin block 0x1256
    prev=[0x11f3], succ=[]
    =================================
    0x1257: RETURNPRIVATE v11f3arg0

}

function mintObizcoinTokens(address,uint256)() public {
    Begin block 0x134
    prev=[], succ=[0x13c, 0x140]
    =================================
    0x135: v135 = CALLVALUE 
    0x136: v136 = ISZERO v135
    0x137: v137(0x140) = CONST 
    0x13b: JUMPI v137(0x140), v136

    Begin block 0x13c
    prev=[0x134], succ=[]
    =================================
    0x13c: v13c(0x0) = CONST 
    0x13f: REVERT v13c(0x0), v13c(0x0)

    Begin block 0x140
    prev=[0x134], succ=[0x57cB0x140]
    =================================
    0x141: v141(0x177) = CONST 
    0x145: v145(0x4) = CONST 
    0x149: v149 = CALLDATALOAD v145(0x4)
    0x14a: v14a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15f: v15f = AND v14a(0xffffffffffffffffffffffffffffffffffffffff), v149
    0x161: v161(0x20) = CONST 
    0x163: v163(0x24) = ADD v161(0x20), v145(0x4)
    0x168: v168 = CALLDATALOAD v163(0x24)
    0x16a: v16a(0x20) = CONST 
    0x16c: v16c(0x44) = ADD v16a(0x20), v163(0x24)
    0x172: v172(0x57c) = CONST 
    0x176: JUMP v172(0x57c)

    Begin block 0x57cB0x140
    prev=[0x140], succ=[0x5d4B0x140, 0x5d8B0x140]
    =================================
    0x57dS0x140: v57dV140(0x0) = CONST 
    0x581S0x140: v581V140 = SLOAD v57dV140(0x0)
    0x583S0x140: v583V140(0x100) = CONST 
    0x586S0x140: v586V140(0x1) = EXP v583V140(0x100), v57dV140(0x0)
    0x588S0x140: v588V140 = DIV v581V140, v586V140(0x1)
    0x589S0x140: v589V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x59eS0x140: v59eV140 = AND v589V140(0xffffffffffffffffffffffffffffffffffffffff), v588V140
    0x59fS0x140: v59fV140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b4S0x140: v5b4V140 = AND v59fV140(0xffffffffffffffffffffffffffffffffffffffff), v59eV140
    0x5b5S0x140: v5b5V140 = CALLER 
    0x5b6S0x140: v5b6V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5cbS0x140: v5cbV140 = AND v5b6V140(0xffffffffffffffffffffffffffffffffffffffff), v5b5V140
    0x5ccS0x140: v5ccV140 = EQ v5cbV140, v5b4V140
    0x5cdS0x140: v5cdV140 = ISZERO v5ccV140
    0x5ceS0x140: v5ceV140 = ISZERO v5cdV140
    0x5cfS0x140: v5cfV140(0x5d8) = CONST 
    0x5d3S0x140: JUMPI v5cfV140(0x5d8), v5ceV140

    Begin block 0x5d4B0x140
    prev=[0x57cB0x140], succ=[]
    =================================
    0x5d4S0x140: v5d4V140(0x0) = CONST 
    0x5d7S0x140: REVERT v5d4V140(0x0), v5d4V140(0x0)

    Begin block 0x5d8B0x140
    prev=[0x57cB0x140], succ=[0x60cB0x140]
    =================================
    0x5d9S0x140: v5d9V140(0xe) = CONST 
    0x5dbS0x140: v5dbV140(0x0) = CONST 
    0x5deS0x140: v5deV140 = SLOAD v5d9V140(0xe)
    0x5e3S0x140: v5e3V140(0x1) = CONST 
    0x5e5S0x140: v5e5V140 = ADD v5e3V140(0x1), v5deV140
    0x5e9S0x140: SSTORE v5d9V140(0xe), v5e5V140
    0x5ebS0x140: v5ebV140(0x612) = CONST 
    0x5f0S0x140: v5f0V140(0x60c) = CONST 
    0x5f4S0x140: v5f4V140(0xde0b6b3a7640000) = CONST 
    0x5feS0x140: v5feV140(0xe5d) = CONST 
    0x605S0x140: v605V140(0xffffffff) = CONST 
    0x60aS0x140: v60aV140(0xe5d) = AND v605V140(0xffffffff), v5feV140(0xe5d)
    0x60bS0x140: v60b_0V140 = CALLPRIVATE v60aV140(0xe5d), v5f4V140(0xde0b6b3a7640000), v168, v5f0V140(0x60c)

    Begin block 0x60cB0x140
    prev=[0x5d8B0x140], succ=[0xe9cB0x140]
    =================================
    0x60dS0x140: v60dV140(0xe9c) = CONST 
    0x611S0x140: JUMP v60dV140(0xe9c)

    Begin block 0xe9cB0x140
    prev=[0x60cB0x140], succ=[0xeb2B0x140, 0xeacB0x140]
    =================================
    0xe9dS0x140: ve9dV140(0x0) = CONST 
    0xe9fS0x140: ve9fV140(0x4) = CONST 
    0xea1S0x140: vea1V140 = SLOAD ve9fV140(0x4)
    0xea2S0x140: vea2V140 = TIMESTAMP 
    0xea3S0x140: vea3V140 = LT vea2V140, vea1V140
    0xea4S0x140: vea4V140 = ISZERO vea3V140
    0xea6S0x140: vea6V140 = ISZERO vea4V140
    0xea7S0x140: vea7V140(0xeb2) = CONST 
    0xeabS0x140: JUMPI vea7V140(0xeb2), vea6V140

    Begin block 0xeb2B0x140
    prev=[0xe9cB0x140, 0xeacB0x140], succ=[0xeb9B0x140, 0xed7B0x140]
    =================================
    0xeb2_0x0S0x140: veb2_0V140 = PHI vea4V140, veb1V140
    0xeb3S0x140: veb3V140 = ISZERO veb2_0V140
    0xeb4S0x140: veb4V140(0xed7) = CONST 
    0xeb8S0x140: JUMPI veb4V140(0xed7), veb3V140

    Begin block 0xeb9B0x140
    prev=[0xeb2B0x140], succ=[0xecfB0x140]
    =================================
    0xeb9S0x140: veb9V140(0xecf) = CONST 
    0xebdS0x140: vebdV140(0x2af8) = CONST 
    0xec1S0x140: vec1V140(0x1098) = CONST 
    0xec8S0x140: vec8V140(0xffffffff) = CONST 
    0xecdS0x140: vecdV140(0x1098) = AND vec8V140(0xffffffff), vec1V140(0x1098)
    0xeceS0x140: vece_0V140 = CALLPRIVATE vecdV140(0x1098), vebdV140(0x2af8), v60b_0V140, veb9V140(0xecf)

    Begin block 0xecfB0x140
    prev=[0xeb9B0x140], succ=[0xf0cB0x140]
    =================================
    0xed2S0x140: ved2V140(0xf0c) = CONST 
    0xed6S0x140: JUMP ved2V140(0xf0c)

    Begin block 0xf0cB0x140
    prev=[0xecfB0x140, 0xf0bB0x140], succ=[0xf23B0x140]
    =================================
    0xf0c_0x0S0x140: vf0c_0V140 = PHI vece_0V140, vf07_0V140, ve9dV140(0x0)
    0xf0dS0x140: vf0dV140(0xf23) = CONST 
    0xf12S0x140: vf12V140(0x3) = CONST 
    0xf14S0x140: vf14V140 = SLOAD vf12V140(0x3)
    0xf15S0x140: vf15V140(0x10bf) = CONST 
    0xf1cS0x140: vf1cV140(0xffffffff) = CONST 
    0xf21S0x140: vf21V140(0x10bf) = AND vf1cV140(0xffffffff), vf15V140(0x10bf)
    0xf22S0x140: vf22_0V140 = CALLPRIVATE vf21V140(0x10bf), vf0c_0V140, vf14V140, vf0dV140(0xf23)

    Begin block 0xf23B0x140
    prev=[0xf0cB0x140], succ=[0xff3B0x140, 0xff7B0x140]
    =================================
    0xf24S0x140: vf24V140(0x3) = CONST 
    0xf28S0x140: SSTORE vf24V140(0x3), vf22_0V140
    0xf2aS0x140: vf2aV140(0x1) = CONST 
    0xf2cS0x140: vf2cV140(0x0) = CONST 
    0xf2fS0x140: vf2fV140 = SLOAD vf2aV140(0x1)
    0xf31S0x140: vf31V140(0x100) = CONST 
    0xf34S0x140: vf34V140(0x1) = EXP vf31V140(0x100), vf2cV140(0x0)
    0xf36S0x140: vf36V140 = DIV vf2fV140, vf34V140(0x1)
    0xf37S0x140: vf37V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf4cS0x140: vf4cV140 = AND vf37V140(0xffffffffffffffffffffffffffffffffffffffff), vf36V140
    0xf4dS0x140: vf4dV140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf62S0x140: vf62V140 = AND vf4dV140(0xffffffffffffffffffffffffffffffffffffffff), vf4cV140
    0xf63S0x140: vf63V140(0x40c10f19) = CONST 
    0xf6aS0x140: vf6aV140(0x0) = CONST 
    0xf6cS0x140: vf6cV140(0x40) = CONST 
    0xf6eS0x140: vf6eV140 = MLOAD vf6cV140(0x40)
    0xf6fS0x140: vf6fV140(0x20) = CONST 
    0xf71S0x140: vf71V140 = ADD vf6fV140(0x20), vf6eV140
    0xf72S0x140: MSTORE vf71V140, vf6aV140(0x0)
    0xf73S0x140: vf73V140(0x40) = CONST 
    0xf75S0x140: vf75V140 = MLOAD vf73V140(0x40)
    0xf77S0x140: vf77V140(0xffffffff) = CONST 
    0xf7cS0x140: vf7cV140(0x40c10f19) = AND vf77V140(0xffffffff), vf63V140(0x40c10f19)
    0xf7dS0x140: vf7dV140(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xf9bS0x140: vf9bV140(0x40c10f1900000000000000000000000000000000000000000000000000000000) = MUL vf7dV140(0x100000000000000000000000000000000000000000000000000000000), vf7cV140(0x40c10f19)
    0xf9dS0x140: MSTORE vf75V140, vf9bV140(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0xf9eS0x140: vf9eV140(0x4) = CONST 
    0xfa0S0x140: vfa0V140 = ADD vf9eV140(0x4), vf75V140
    0xfa3S0x140: vfa3V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfb8S0x140: vfb8V140 = AND vfa3V140(0xffffffffffffffffffffffffffffffffffffffff), v15f
    0xfb9S0x140: vfb9V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfceS0x140: vfceV140 = AND vfb9V140(0xffffffffffffffffffffffffffffffffffffffff), vfb8V140
    0xfd0S0x140: MSTORE vfa0V140, vfceV140
    0xfd1S0x140: vfd1V140(0x20) = CONST 
    0xfd3S0x140: vfd3V140 = ADD vfd1V140(0x20), vfa0V140
    0xfd6S0x140: MSTORE vfd3V140, v60b_0V140
    0xfd7S0x140: vfd7V140(0x20) = CONST 
    0xfd9S0x140: vfd9V140 = ADD vfd7V140(0x20), vfd3V140
    0xfdeS0x140: vfdeV140(0x20) = CONST 
    0xfe0S0x140: vfe0V140(0x40) = CONST 
    0xfe2S0x140: vfe2V140 = MLOAD vfe0V140(0x40)
    0xfe5S0x140: vfe5V140(0x44) = SUB vfd9V140, vfe2V140
    0xfe7S0x140: vfe7V140(0x0) = CONST 
    0xfebS0x140: vfebV140 = EXTCODESIZE vf62V140
    0xfecS0x140: vfecV140 = ISZERO vfebV140
    0xfedS0x140: vfedV140 = ISZERO vfecV140
    0xfeeS0x140: vfeeV140(0xff7) = CONST 
    0xff2S0x140: JUMPI vfeeV140(0xff7), vfedV140

    Begin block 0xff3B0x140
    prev=[0xf23B0x140], succ=[]
    =================================
    0xff3S0x140: vff3V140(0x0) = CONST 
    0xff6S0x140: REVERT vff3V140(0x0), vff3V140(0x0)

    Begin block 0xff7B0x140
    prev=[0xf23B0x140], succ=[0x1005B0x140, 0x1009B0x140]
    =================================
    0xff8S0x140: vff8V140(0x2c6) = CONST 
    0xffbS0x140: vffbV140 = GAS 
    0xffcS0x140: vffcV140 = SUB vffbV140, vff8V140(0x2c6)
    0xffdS0x140: vffdV140 = CALL vffcV140, vf62V140, vfe7V140(0x0), vfe2V140, vfe5V140(0x44), vfe2V140, vfdeV140(0x20)
    0xffeS0x140: vffeV140 = ISZERO vffdV140
    0xfffS0x140: vfffV140 = ISZERO vffeV140
    0x1000S0x140: v1000V140(0x1009) = CONST 
    0x1004S0x140: JUMPI v1000V140(0x1009), vfffV140

    Begin block 0x1005B0x140
    prev=[0xff7B0x140], succ=[]
    =================================
    0x1005S0x140: v1005V140(0x0) = CONST 
    0x1008S0x140: REVERT v1005V140(0x0), v1005V140(0x0)

    Begin block 0x1009B0x140
    prev=[0xff7B0x140], succ=[0x101fB0x140]
    =================================
    0x100dS0x140: v100dV140(0x40) = CONST 
    0x100fS0x140: v100fV140 = MLOAD v100dV140(0x40)
    0x1011S0x140: v1011V140 = MLOAD v100fV140
    0x1015S0x140: v1015V140(0x101f) = CONST 
    0x101aS0x140: v101aV140(0x10de) = CONST 
    0x101eS0x140: CALLPRIVATE v101aV140(0x10de), v15f, v1015V140(0x101f)

    Begin block 0x101fB0x140
    prev=[0x1009B0x140], succ=[0x612B0x140]
    =================================
    0x101f_0x0S0x140: v101f_0V140 = PHI vece_0V140, vf07_0V140, ve9dV140(0x0)
    0x1021S0x140: v1021V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1036S0x140: v1036V140 = AND v1021V140(0xffffffffffffffffffffffffffffffffffffffff), v15f
    0x1037S0x140: v1037V140 = CALLER 
    0x1038S0x140: v1038V140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x104dS0x140: v104dV140 = AND v1038V140(0xffffffffffffffffffffffffffffffffffffffff), v1037V140
    0x104eS0x140: v104eV140(0xfe0e12b43090c1fc19a34aefa5cc138a4eeafc60ab800f855c730b3fb9480e) = CONST 
    0x1070S0x140: v1070V140 = TIMESTAMP 
    0x1071S0x140: v1071V140(0x40) = CONST 
    0x1073S0x140: v1073V140 = MLOAD v1071V140(0x40)
    0x1077S0x140: MSTORE v1073V140, v101f_0V140
    0x1078S0x140: v1078V140(0x20) = CONST 
    0x107aS0x140: v107aV140 = ADD v1078V140(0x20), v1073V140
    0x107dS0x140: MSTORE v107aV140, v60b_0V140
    0x107eS0x140: v107eV140(0x20) = CONST 
    0x1080S0x140: v1080V140 = ADD v107eV140(0x20), v107aV140
    0x1083S0x140: MSTORE v1080V140, v1070V140
    0x1084S0x140: v1084V140(0x20) = CONST 
    0x1086S0x140: v1086V140 = ADD v1084V140(0x20), v1080V140
    0x108cS0x140: v108cV140(0x40) = CONST 
    0x108eS0x140: v108eV140 = MLOAD v108cV140(0x40)
    0x1091S0x140: v1091V140(0x60) = SUB v1086V140, v108eV140
    0x1093S0x140: LOG3 v108eV140, v1091V140(0x60), v104eV140(0xfe0e12b43090c1fc19a34aefa5cc138a4eeafc60ab800f855c730b3fb9480e), v104dV140, v1036V140
    0x1097S0x140: JUMP v5ebV140(0x612)

    Begin block 0x612B0x140
    prev=[0x101fB0x140], succ=[0x177]
    =================================
    0x615S0x140: JUMP v141(0x177)

    Begin block 0x177
    prev=[0x612B0x140], succ=[]
    =================================
    0x178: STOP 

    Begin block 0xed7B0x140
    prev=[0xeb2B0x140], succ=[0xeebB0x140, 0xee5B0x140]
    =================================
    0xed8S0x140: ved8V140(0x7) = CONST 
    0xedaS0x140: vedaV140 = SLOAD ved8V140(0x7)
    0xedbS0x140: vedbV140 = TIMESTAMP 
    0xedcS0x140: vedcV140 = LT vedbV140, vedaV140
    0xeddS0x140: veddV140 = ISZERO vedcV140
    0xedfS0x140: vedfV140 = ISZERO veddV140
    0xee0S0x140: vee0V140(0xeeb) = CONST 
    0xee4S0x140: JUMPI vee0V140(0xeeb), vedfV140

    Begin block 0xeebB0x140
    prev=[0xed7B0x140, 0xee5B0x140], succ=[0xef2B0x140, 0xf0bB0x140]
    =================================
    0xeeb_0x0S0x140: veeb_0V140 = PHI veddV140, veeaV140
    0xeecS0x140: veecV140 = ISZERO veeb_0V140
    0xeedS0x140: veedV140(0xf0b) = CONST 
    0xef1S0x140: JUMPI veedV140(0xf0b), veecV140

    Begin block 0xef2B0x140
    prev=[0xeebB0x140], succ=[0xf08B0x140]
    =================================
    0xef2S0x140: vef2V140(0xf08) = CONST 
    0xef6S0x140: vef6V140(0x2710) = CONST 
    0xefaS0x140: vefaV140(0x1098) = CONST 
    0xf01S0x140: vf01V140(0xffffffff) = CONST 
    0xf06S0x140: vf06V140(0x1098) = AND vf01V140(0xffffffff), vefaV140(0x1098)
    0xf07S0x140: vf07_0V140 = CALLPRIVATE vf06V140(0x1098), vef6V140(0x2710), v60b_0V140, vef2V140(0xf08)

    Begin block 0xf08B0x140
    prev=[0xef2B0x140], succ=[0xf0bB0x140]
    =================================
    0xd1e2S0x140: vd1e2V140(0xf0b) = CONST 
    0xd202S0x140: JUMP vd1e2V140(0xf0b)

    Begin block 0xf0bB0x140
    prev=[0xeebB0x140, 0xf08B0x140], succ=[0xf0cB0x140]
    =================================
    0xdbe2S0x140: vdbe2V140(0xf0c) = CONST 
    0xdc02S0x140: JUMP vdbe2V140(0xf0c)

    Begin block 0xee5B0x140
    prev=[0xed7B0x140], succ=[0xeebB0x140]
    =================================
    0xee6S0x140: vee6V140(0xb) = CONST 
    0xee8S0x140: vee8V140 = SLOAD vee6V140(0xb)
    0xee9S0x140: vee9V140 = TIMESTAMP 
    0xeeaS0x140: veeaV140 = LT vee9V140, vee8V140
    0xc7e2S0x140: vc7e2V140(0xeeb) = CONST 
    0xc802S0x140: JUMP vc7e2V140(0xeeb)

    Begin block 0xeacB0x140
    prev=[0xe9cB0x140], succ=[0xeb2B0x140]
    =================================
    0xeadS0x140: veadV140(0x6) = CONST 
    0xeafS0x140: veafV140 = SLOAD veadV140(0x6)
    0xeb0S0x140: veb0V140 = TIMESTAMP 
    0xeb1S0x140: veb1V140 = LT veb0V140, veafV140
    0xbde2S0x140: vbde2V140(0xeb2) = CONST 
    0xbe02S0x140: JUMP vbde2V140(0xeb2)

}

function holders(uint256)() public {
    Begin block 0x179
    prev=[], succ=[0x181, 0x185]
    =================================
    0x17a: v17a = CALLVALUE 
    0x17b: v17b = ISZERO v17a
    0x17c: v17c(0x185) = CONST 
    0x180: JUMPI v17c(0x185), v17b

    Begin block 0x181
    prev=[0x179], succ=[]
    =================================
    0x181: v181(0x0) = CONST 
    0x184: REVERT v181(0x0), v181(0x0)

    Begin block 0x185
    prev=[0x179], succ=[0x616]
    =================================
    0x186: v186(0x19d) = CONST 
    0x18a: v18a(0x4) = CONST 
    0x18e: v18e = CALLDATALOAD v18a(0x4)
    0x190: v190(0x20) = CONST 
    0x192: v192(0x24) = ADD v190(0x20), v18a(0x4)
    0x198: v198(0x616) = CONST 
    0x19c: JUMP v198(0x616)

    Begin block 0x616
    prev=[0x185], succ=[0x625, 0x626]
    =================================
    0x617: v617(0xd) = CONST 
    0x61b: v61b = SLOAD v617(0xd)
    0x61d: v61d = LT v18e, v61b
    0x61e: v61e = ISZERO v61d
    0x61f: v61f = ISZERO v61e
    0x620: v620(0x626) = CONST 
    0x624: JUMPI v620(0x626), v61f

    Begin block 0x625
    prev=[0x616], succ=[]
    =================================
    0x625: THROW 

    Begin block 0x626
    prev=[0x616], succ=[0x19d]
    =================================
    0x628: v628(0x0) = CONST 
    0x62a: MSTORE v628(0x0), v617(0xd)
    0x62b: v62b(0x20) = CONST 
    0x62d: v62d(0x0) = CONST 
    0x62f: v62f = SHA3 v62d(0x0), v62b(0x20)
    0x631: v631 = ADD v18e, v62f
    0x632: v632(0x0) = CONST 
    0x636: v636 = SLOAD v631
    0x638: v638(0x100) = CONST 
    0x63b: v63b(0x1) = EXP v638(0x100), v632(0x0)
    0x63d: v63d = DIV v636, v63b(0x1)
    0x63e: v63e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x653: v653 = AND v63e(0xffffffffffffffffffffffffffffffffffffffff), v63d
    0x655: JUMP v186(0x19d)

    Begin block 0x19d
    prev=[0x626], succ=[]
    =================================
    0x19e: v19e(0x40) = CONST 
    0x1a0: v1a0 = MLOAD v19e(0x40)
    0x1a3: v1a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b8: v1b8 = AND v1a3(0xffffffffffffffffffffffffffffffffffffffff), v653
    0x1b9: v1b9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ce: v1ce = AND v1b9(0xffffffffffffffffffffffffffffffffffffffff), v1b8
    0x1d0: MSTORE v1a0, v1ce
    0x1d1: v1d1(0x20) = CONST 
    0x1d3: v1d3 = ADD v1d1(0x20), v1a0
    0x1d7: v1d7(0x40) = CONST 
    0x1d9: v1d9 = MLOAD v1d7(0x40)
    0x1dc: v1dc(0x20) = SUB v1d3, v1d9
    0x1de: RETURN v1d9, v1dc(0x20)

}

function weiRaised()() public {
    Begin block 0x1df
    prev=[], succ=[0x1e7, 0x1eb]
    =================================
    0x1e0: v1e0 = CALLVALUE 
    0x1e1: v1e1 = ISZERO v1e0
    0x1e2: v1e2(0x1eb) = CONST 
    0x1e6: JUMPI v1e2(0x1eb), v1e1

    Begin block 0x1e7
    prev=[0x1df], succ=[]
    =================================
    0x1e7: v1e7(0x0) = CONST 
    0x1ea: REVERT v1e7(0x0), v1e7(0x0)

    Begin block 0x1eb
    prev=[0x1df], succ=[0x656]
    =================================
    0x1ec: v1ec(0x1f5) = CONST 
    0x1f0: v1f0(0x656) = CONST 
    0x1f4: JUMP v1f0(0x656)

    Begin block 0x656
    prev=[0x1eb], succ=[0x1f5]
    =================================
    0x657: v657(0x3) = CONST 
    0x659: v659 = SLOAD v657(0x3)
    0x65b: JUMP v1ec(0x1f5)

    Begin block 0x1f5
    prev=[0x656], succ=[]
    =================================
    0x1f6: v1f6(0x40) = CONST 
    0x1f8: v1f8 = MLOAD v1f6(0x40)
    0x1fc: MSTORE v1f8, v659
    0x1fd: v1fd(0x20) = CONST 
    0x1ff: v1ff = ADD v1fd(0x20), v1f8
    0x203: v203(0x40) = CONST 
    0x205: v205 = MLOAD v203(0x40)
    0x208: v208(0x20) = SUB v1ff, v205
    0x20a: RETURN v205, v208(0x20)

}

function wallet()() public {
    Begin block 0x20b
    prev=[], succ=[0x213, 0x217]
    =================================
    0x20c: v20c = CALLVALUE 
    0x20d: v20d = ISZERO v20c
    0x20e: v20e(0x217) = CONST 
    0x212: JUMPI v20e(0x217), v20d

    Begin block 0x213
    prev=[0x20b], succ=[]
    =================================
    0x213: v213(0x0) = CONST 
    0x216: REVERT v213(0x0), v213(0x0)

    Begin block 0x217
    prev=[0x20b], succ=[0x65c]
    =================================
    0x218: v218(0x221) = CONST 
    0x21c: v21c(0x65c) = CONST 
    0x220: JUMP v21c(0x65c)

    Begin block 0x65c
    prev=[0x217], succ=[0x221]
    =================================
    0x65d: v65d(0x2) = CONST 
    0x65f: v65f(0x0) = CONST 
    0x662: v662 = SLOAD v65d(0x2)
    0x664: v664(0x100) = CONST 
    0x667: v667(0x1) = EXP v664(0x100), v65f(0x0)
    0x669: v669 = DIV v662, v667(0x1)
    0x66a: v66a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x67f: v67f = AND v66a(0xffffffffffffffffffffffffffffffffffffffff), v669
    0x681: JUMP v218(0x221)

    Begin block 0x221
    prev=[0x65c], succ=[]
    =================================
    0x222: v222(0x40) = CONST 
    0x224: v224 = MLOAD v222(0x40)
    0x227: v227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23c: v23c = AND v227(0xffffffffffffffffffffffffffffffffffffffff), v67f
    0x23d: v23d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x252: v252 = AND v23d(0xffffffffffffffffffffffffffffffffffffffff), v23c
    0x254: MSTORE v224, v252
    0x255: v255(0x20) = CONST 
    0x257: v257 = ADD v255(0x20), v224
    0x25b: v25b(0x40) = CONST 
    0x25d: v25d = MLOAD v25b(0x40)
    0x260: v260(0x20) = SUB v257, v25d
    0x262: RETURN v25d, v260(0x20)

}

function buyObizcoinTokens(address)() public {
    Begin block 0x263
    prev=[], succ=[0x495B0x263]
    =================================
    0x264: v264(0x291) = CONST 
    0x268: v268(0x4) = CONST 
    0x26c: v26c = CALLDATALOAD v268(0x4)
    0x26d: v26d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x282: v282 = AND v26d(0xffffffffffffffffffffffffffffffffffffffff), v26c
    0x284: v284(0x20) = CONST 
    0x286: v286(0x24) = ADD v284(0x20), v268(0x4)
    0x28c: v28c(0x495) = CONST 
    0x290: JUMP v28c(0x495)

    Begin block 0x495B0x263
    prev=[0x263], succ=[0x4b2B0x263]
    =================================
    0x496S0x263: v496V263(0xe) = CONST 
    0x498S0x263: v498V263(0x0) = CONST 
    0x49bS0x263: v49bV263 = SLOAD v496V263(0xe)
    0x4a0S0x263: v4a0V263(0x1) = CONST 
    0x4a2S0x263: v4a2V263 = ADD v4a0V263(0x1), v49bV263
    0x4a6S0x263: SSTORE v496V263(0xe), v4a2V263
    0x4a8S0x263: v4a8V263(0x4b2) = CONST 
    0x4adS0x263: v4adV263(0xace) = CONST 
    0x4b1S0x263: CALLPRIVATE v4adV263(0xace), v282, v4a8V263(0x4b2)

    Begin block 0x4b2B0x263
    prev=[0x495B0x263], succ=[0x291]
    =================================
    0x4b4S0x263: JUMP v264(0x291)

    Begin block 0x291
    prev=[0x4b2B0x263], succ=[]
    =================================
    0x292: STOP 

}

function profitSharing()() public {
    Begin block 0x293
    prev=[], succ=[0x682B0x293]
    =================================
    0x294: v294(0x29d) = CONST 
    0x298: v298(0x682) = CONST 
    0x29c: JUMP v298(0x682)

    Begin block 0x682B0x293
    prev=[0x293], succ=[0x68fB0x293]
    =================================
    0x683S0x293: v683V293(0x0) = CONST 
    0x686S0x293: v686V293(0x0) = CONST 
    0x688S0x293: v688V293 = CALLVALUE 
    0x68bS0x293: v68bV293(0x0) = CONST 
    0x4fe2S0x293: v4fe2V293(0x68f) = CONST 
    0x5002S0x293: JUMP v4fe2V293(0x68f)

    Begin block 0x68fB0x293
    prev=[0x682B0x293, 0x915B0x293], succ=[0x69eB0x293, 0x923B0x293]
    =================================
    0x68f_0x0S0x293: v68f_0V293 = PHI v68bV293(0x0), v91aV293
    0x690S0x293: v690V293(0xd) = CONST 
    0x693S0x293: v693V293 = SLOAD v690V293(0xd)
    0x697S0x293: v697V293 = LT v68f_0V293, v693V293
    0x698S0x293: v698V293 = ISZERO v697V293
    0x699S0x293: v699V293(0x923) = CONST 
    0x69dS0x293: JUMPI v699V293(0x923), v698V293

    Begin block 0x69eB0x293
    prev=[0x68fB0x293], succ=[0x6ebB0x293, 0x6eaB0x293]
    =================================
    0x69eS0x293: v69eV293(0x1) = CONST 
    0x69e_0x0S0x293: v69e_0V293 = PHI v68bV293(0x0), v91aV293
    0x6a0S0x293: v6a0V293(0x0) = CONST 
    0x6a3S0x293: v6a3V293 = SLOAD v69eV293(0x1)
    0x6a5S0x293: v6a5V293(0x100) = CONST 
    0x6a8S0x293: v6a8V293(0x1) = EXP v6a5V293(0x100), v6a0V293(0x0)
    0x6aaS0x293: v6aaV293 = DIV v6a3V293, v6a8V293(0x1)
    0x6abS0x293: v6abV293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6c0S0x293: v6c0V293 = AND v6abV293(0xffffffffffffffffffffffffffffffffffffffff), v6aaV293
    0x6c1S0x293: v6c1V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6d6S0x293: v6d6V293 = AND v6c1V293(0xffffffffffffffffffffffffffffffffffffffff), v6c0V293
    0x6d7S0x293: v6d7V293(0x70a08231) = CONST 
    0x6dcS0x293: v6dcV293(0xd) = CONST 
    0x6e0S0x293: v6e0V293 = SLOAD v6dcV293(0xd)
    0x6e2S0x293: v6e2V293 = LT v69e_0V293, v6e0V293
    0x6e3S0x293: v6e3V293 = ISZERO v6e2V293
    0x6e4S0x293: v6e4V293 = ISZERO v6e3V293
    0x6e5S0x293: v6e5V293(0x6eb) = CONST 
    0x6e9S0x293: JUMPI v6e5V293(0x6eb), v6e4V293

    Begin block 0x6ebB0x293
    prev=[0x69eB0x293], succ=[0x79aB0x293, 0x79eB0x293]
    =================================
    0x6eb_0x0S0x293: v6eb_0V293 = PHI v68bV293(0x0), v91aV293
    0x6edS0x293: v6edV293(0x0) = CONST 
    0x6efS0x293: MSTORE v6edV293(0x0), v6dcV293(0xd)
    0x6f0S0x293: v6f0V293(0x20) = CONST 
    0x6f2S0x293: v6f2V293(0x0) = CONST 
    0x6f4S0x293: v6f4V293 = SHA3 v6f2V293(0x0), v6f0V293(0x20)
    0x6f6S0x293: v6f6V293 = ADD v6eb_0V293, v6f4V293
    0x6f7S0x293: v6f7V293(0x0) = CONST 
    0x6faS0x293: v6faV293 = SLOAD v6f6V293
    0x6fcS0x293: v6fcV293(0x100) = CONST 
    0x6ffS0x293: v6ffV293(0x1) = EXP v6fcV293(0x100), v6f7V293(0x0)
    0x701S0x293: v701V293 = DIV v6faV293, v6ffV293(0x1)
    0x702S0x293: v702V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x717S0x293: v717V293 = AND v702V293(0xffffffffffffffffffffffffffffffffffffffff), v701V293
    0x718S0x293: v718V293(0x0) = CONST 
    0x71aS0x293: v71aV293(0x40) = CONST 
    0x71cS0x293: v71cV293 = MLOAD v71aV293(0x40)
    0x71dS0x293: v71dV293(0x20) = CONST 
    0x71fS0x293: v71fV293 = ADD v71dV293(0x20), v71cV293
    0x720S0x293: MSTORE v71fV293, v718V293(0x0)
    0x721S0x293: v721V293(0x40) = CONST 
    0x723S0x293: v723V293 = MLOAD v721V293(0x40)
    0x725S0x293: v725V293(0xffffffff) = CONST 
    0x72aS0x293: v72aV293(0x70a08231) = AND v725V293(0xffffffff), v6d7V293(0x70a08231)
    0x72bS0x293: v72bV293(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x749S0x293: v749V293(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL v72bV293(0x100000000000000000000000000000000000000000000000000000000), v72aV293(0x70a08231)
    0x74bS0x293: MSTORE v723V293, v749V293(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x74cS0x293: v74cV293(0x4) = CONST 
    0x74eS0x293: v74eV293 = ADD v74cV293(0x4), v723V293
    0x751S0x293: v751V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x766S0x293: v766V293 = AND v751V293(0xffffffffffffffffffffffffffffffffffffffff), v717V293
    0x767S0x293: v767V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x77cS0x293: v77cV293 = AND v767V293(0xffffffffffffffffffffffffffffffffffffffff), v766V293
    0x77eS0x293: MSTORE v74eV293, v77cV293
    0x77fS0x293: v77fV293(0x20) = CONST 
    0x781S0x293: v781V293 = ADD v77fV293(0x20), v74eV293
    0x785S0x293: v785V293(0x20) = CONST 
    0x787S0x293: v787V293(0x40) = CONST 
    0x789S0x293: v789V293 = MLOAD v787V293(0x40)
    0x78cS0x293: v78cV293(0x24) = SUB v781V293, v789V293
    0x78eS0x293: v78eV293(0x0) = CONST 
    0x792S0x293: v792V293 = EXTCODESIZE v6d6V293
    0x793S0x293: v793V293 = ISZERO v792V293
    0x794S0x293: v794V293 = ISZERO v793V293
    0x795S0x293: v795V293(0x79e) = CONST 
    0x799S0x293: JUMPI v795V293(0x79e), v794V293

    Begin block 0x79aB0x293
    prev=[0x6ebB0x293], succ=[]
    =================================
    0x79aS0x293: v79aV293(0x0) = CONST 
    0x79dS0x293: REVERT v79aV293(0x0), v79aV293(0x0)

    Begin block 0x79eB0x293
    prev=[0x6ebB0x293], succ=[0x7acB0x293, 0x7b0B0x293]
    =================================
    0x79fS0x293: v79fV293(0x2c6) = CONST 
    0x7a2S0x293: v7a2V293 = GAS 
    0x7a3S0x293: v7a3V293 = SUB v7a2V293, v79fV293(0x2c6)
    0x7a4S0x293: v7a4V293 = CALL v7a3V293, v6d6V293, v78eV293(0x0), v789V293, v78cV293(0x24), v789V293, v785V293(0x20)
    0x7a5S0x293: v7a5V293 = ISZERO v7a4V293
    0x7a6S0x293: v7a6V293 = ISZERO v7a5V293
    0x7a7S0x293: v7a7V293(0x7b0) = CONST 
    0x7abS0x293: JUMPI v7a7V293(0x7b0), v7a6V293

    Begin block 0x7acB0x293
    prev=[0x79eB0x293], succ=[]
    =================================
    0x7acS0x293: v7acV293(0x0) = CONST 
    0x7afS0x293: REVERT v7acV293(0x0), v7acV293(0x0)

    Begin block 0x7b0B0x293
    prev=[0x79eB0x293], succ=[0x7c7B0x293, 0x915B0x293]
    =================================
    0x7b4S0x293: v7b4V293(0x40) = CONST 
    0x7b6S0x293: v7b6V293 = MLOAD v7b4V293(0x40)
    0x7b8S0x293: v7b8V293 = MLOAD v7b6V293
    0x7bdS0x293: v7bdV293(0x0) = CONST 
    0x7c0S0x293: v7c0V293 = GT v7b8V293, v7bdV293(0x0)
    0x7c1S0x293: v7c1V293 = ISZERO v7c0V293
    0x7c2S0x293: v7c2V293(0x915) = CONST 
    0x7c6S0x293: JUMPI v7c2V293(0x915), v7c1V293

    Begin block 0x7c7B0x293
    prev=[0x7b0B0x293], succ=[0x7d6B0x293, 0x7d5B0x293]
    =================================
    0x7c7S0x293: v7c7V293(0xd) = CONST 
    0x7c7_0x0S0x293: v7c7_0V293 = PHI v68bV293(0x0), v91aV293
    0x7cbS0x293: v7cbV293 = SLOAD v7c7V293(0xd)
    0x7cdS0x293: v7cdV293 = LT v7c7_0V293, v7cbV293
    0x7ceS0x293: v7ceV293 = ISZERO v7cdV293
    0x7cfS0x293: v7cfV293 = ISZERO v7ceV293
    0x7d0S0x293: v7d0V293(0x7d6) = CONST 
    0x7d4S0x293: JUMPI v7d0V293(0x7d6), v7cfV293

    Begin block 0x7d6B0x293
    prev=[0x7c7B0x293], succ=[0x8aaB0x293, 0x8aeB0x293]
    =================================
    0x7d6_0x0S0x293: v7d6_0V293 = PHI v68bV293(0x0), v91aV293
    0x7d8S0x293: v7d8V293(0x0) = CONST 
    0x7daS0x293: MSTORE v7d8V293(0x0), v7c7V293(0xd)
    0x7dbS0x293: v7dbV293(0x20) = CONST 
    0x7ddS0x293: v7ddV293(0x0) = CONST 
    0x7dfS0x293: v7dfV293 = SHA3 v7ddV293(0x0), v7dbV293(0x20)
    0x7e1S0x293: v7e1V293 = ADD v7d6_0V293, v7dfV293
    0x7e2S0x293: v7e2V293(0x0) = CONST 
    0x7e5S0x293: v7e5V293 = SLOAD v7e1V293
    0x7e7S0x293: v7e7V293(0x100) = CONST 
    0x7eaS0x293: v7eaV293(0x1) = EXP v7e7V293(0x100), v7e2V293(0x0)
    0x7ecS0x293: v7ecV293 = DIV v7e5V293, v7eaV293(0x1)
    0x7edS0x293: v7edV293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x802S0x293: v802V293 = AND v7edV293(0xffffffffffffffffffffffffffffffffffffffff), v7ecV293
    0x803S0x293: v803V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x818S0x293: v818V293 = AND v803V293(0xffffffffffffffffffffffffffffffffffffffff), v802V293
    0x819S0x293: v819V293(0x8fc) = CONST 
    0x81cS0x293: v81cV293(0x8ee) = CONST 
    0x820S0x293: v820V293(0x1) = CONST 
    0x822S0x293: v822V293(0x0) = CONST 
    0x825S0x293: v825V293 = SLOAD v820V293(0x1)
    0x827S0x293: v827V293(0x100) = CONST 
    0x82aS0x293: v82aV293(0x1) = EXP v827V293(0x100), v822V293(0x0)
    0x82cS0x293: v82cV293 = DIV v825V293, v82aV293(0x1)
    0x82dS0x293: v82dV293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x842S0x293: v842V293 = AND v82dV293(0xffffffffffffffffffffffffffffffffffffffff), v82cV293
    0x843S0x293: v843V293(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x858S0x293: v858V293 = AND v843V293(0xffffffffffffffffffffffffffffffffffffffff), v842V293
    0x859S0x293: v859V293(0x18160ddd) = CONST 
    0x85eS0x293: v85eV293(0x0) = CONST 
    0x860S0x293: v860V293(0x40) = CONST 
    0x862S0x293: v862V293 = MLOAD v860V293(0x40)
    0x863S0x293: v863V293(0x20) = CONST 
    0x865S0x293: v865V293 = ADD v863V293(0x20), v862V293
    0x866S0x293: MSTORE v865V293, v85eV293(0x0)
    0x867S0x293: v867V293(0x40) = CONST 
    0x869S0x293: v869V293 = MLOAD v867V293(0x40)
    0x86bS0x293: v86bV293(0xffffffff) = CONST 
    0x870S0x293: v870V293(0x18160ddd) = AND v86bV293(0xffffffff), v859V293(0x18160ddd)
    0x871S0x293: v871V293(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x88fS0x293: v88fV293(0x18160ddd00000000000000000000000000000000000000000000000000000000) = MUL v871V293(0x100000000000000000000000000000000000000000000000000000000), v870V293(0x18160ddd)
    0x891S0x293: MSTORE v869V293, v88fV293(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x892S0x293: v892V293(0x4) = CONST 
    0x894S0x293: v894V293 = ADD v892V293(0x4), v869V293
    0x895S0x293: v895V293(0x20) = CONST 
    0x897S0x293: v897V293(0x40) = CONST 
    0x899S0x293: v899V293 = MLOAD v897V293(0x40)
    0x89cS0x293: v89cV293(0x4) = SUB v894V293, v899V293
    0x89eS0x293: v89eV293(0x0) = CONST 
    0x8a2S0x293: v8a2V293 = EXTCODESIZE v858V293
    0x8a3S0x293: v8a3V293 = ISZERO v8a2V293
    0x8a4S0x293: v8a4V293 = ISZERO v8a3V293
    0x8a5S0x293: v8a5V293(0x8ae) = CONST 
    0x8a9S0x293: JUMPI v8a5V293(0x8ae), v8a4V293

    Begin block 0x8aaB0x293
    prev=[0x7d6B0x293], succ=[]
    =================================
    0x8aaS0x293: v8aaV293(0x0) = CONST 
    0x8adS0x293: REVERT v8aaV293(0x0), v8aaV293(0x0)

    Begin block 0x8aeB0x293
    prev=[0x7d6B0x293], succ=[0x8bcB0x293, 0x8c0B0x293]
    =================================
    0x8afS0x293: v8afV293(0x2c6) = CONST 
    0x8b2S0x293: v8b2V293 = GAS 
    0x8b3S0x293: v8b3V293 = SUB v8b2V293, v8afV293(0x2c6)
    0x8b4S0x293: v8b4V293 = CALL v8b3V293, v858V293, v89eV293(0x0), v899V293, v89cV293(0x4), v899V293, v895V293(0x20)
    0x8b5S0x293: v8b5V293 = ISZERO v8b4V293
    0x8b6S0x293: v8b6V293 = ISZERO v8b5V293
    0x8b7S0x293: v8b7V293(0x8c0) = CONST 
    0x8bbS0x293: JUMPI v8b7V293(0x8c0), v8b6V293

    Begin block 0x8bcB0x293
    prev=[0x8aeB0x293], succ=[]
    =================================
    0x8bcS0x293: v8bcV293(0x0) = CONST 
    0x8bfS0x293: REVERT v8bcV293(0x0), v8bcV293(0x0)

    Begin block 0x8c0B0x293
    prev=[0x8aeB0x293], succ=[0x8dfB0x293]
    =================================
    0x8c4S0x293: v8c4V293(0x40) = CONST 
    0x8c6S0x293: v8c6V293 = MLOAD v8c4V293(0x40)
    0x8c8S0x293: v8c8V293 = MLOAD v8c6V293
    0x8cbS0x293: v8cbV293(0x8df) = CONST 
    0x8d1S0x293: v8d1V293(0xe5d) = CONST 
    0x8d8S0x293: v8d8V293(0xffffffff) = CONST 
    0x8ddS0x293: v8ddV293(0xe5d) = AND v8d8V293(0xffffffff), v8d1V293(0xe5d)
    0x8deS0x293: v8de_0V293 = CALLPRIVATE v8ddV293(0xe5d), v688V293, v7b8V293, v8cbV293(0x8df)

    Begin block 0x8dfB0x293
    prev=[0x8c0B0x293], succ=[0x10980x682B0x293]
    =================================
    0x8e0S0x293: v8e0V293(0x1098) = CONST 
    0x8e7S0x293: v8e7V293(0xffffffff) = CONST 
    0x8ecS0x293: v8ecV293(0x1098) = AND v8e7V293(0xffffffff), v8e0V293(0x1098)
    0x8edS0x293: JUMP v8ecV293(0x1098)

    Begin block 0x10980x682B0x293
    prev=[0x8dfB0x293], succ=[0x10a70x682B0x293, 0x10a60x682B0x293]
    =================================
    0x10990x682S0x293: v6821099V293(0x0) = CONST 
    0x109f0x682S0x293: v682109fV293 = ISZERO v8c8V293
    0x10a00x682S0x293: v68210a0V293 = ISZERO v682109fV293
    0x10a10x682S0x293: v68210a1V293(0x10a7) = CONST 
    0x10a50x682S0x293: JUMPI v68210a1V293(0x10a7), v68210a0V293

    Begin block 0x10a70x682B0x293
    prev=[0x10980x682B0x293], succ=[0x8eeB0x293]
    =================================
    0x10a80x682S0x293: v68210a8V293 = DIV v8de_0V293, v8c8V293
    0x10b30x682S0x293: JUMP v81cV293(0x8ee)

    Begin block 0x8eeB0x293
    prev=[0x10a70x682B0x293], succ=[0x910B0x293, 0x914B0x293]
    =================================
    0x8f1S0x293: v8f1V293 = ISZERO v68210a8V293
    0x8f2S0x293: v8f2V293 = MUL v8f1V293, v819V293(0x8fc)
    0x8f4S0x293: v8f4V293(0x40) = CONST 
    0x8f6S0x293: v8f6V293 = MLOAD v8f4V293(0x40)
    0x8f7S0x293: v8f7V293(0x0) = CONST 
    0x8f9S0x293: v8f9V293(0x40) = CONST 
    0x8fbS0x293: v8fbV293 = MLOAD v8f9V293(0x40)
    0x8feS0x293: v8feV293(0x0) = SUB v8f6V293, v8fbV293
    0x903S0x293: v903V293 = CALL v8f2V293, v818V293, v68210a8V293, v8fbV293, v8feV293(0x0), v8fbV293, v8f7V293(0x0)
    0x909S0x293: v909V293 = ISZERO v903V293
    0x90aS0x293: v90aV293 = ISZERO v909V293
    0x90bS0x293: v90bV293(0x914) = CONST 
    0x90fS0x293: JUMPI v90bV293(0x914), v90aV293

    Begin block 0x910B0x293
    prev=[0x8eeB0x293], succ=[]
    =================================
    0x910S0x293: v910V293(0x0) = CONST 
    0x913S0x293: REVERT v910V293(0x0), v910V293(0x0)

    Begin block 0x914B0x293
    prev=[0x8eeB0x293], succ=[0x915B0x293]
    =================================
    0x59e2S0x293: v59e2V293(0x915) = CONST 
    0x5a02S0x293: JUMP v59e2V293(0x915)

    Begin block 0x915B0x293
    prev=[0x7b0B0x293, 0x914B0x293], succ=[0x68fB0x293]
    =================================
    0x915_0x0S0x293: v915_0V293 = PHI v68bV293(0x0), v91aV293
    0x918S0x293: v918V293(0x1) = CONST 
    0x91aS0x293: v91aV293 = ADD v918V293(0x1), v915_0V293
    0x91eS0x293: v91eV293(0x68f) = CONST 
    0x922S0x293: JUMP v91eV293(0x68f)

    Begin block 0x10a60x682B0x293
    prev=[0x10980x682B0x293], succ=[]
    =================================
    0x10a60x682S0x293: THROW 

    Begin block 0x7d5B0x293
    prev=[0x7c7B0x293], succ=[]
    =================================
    0x7d5S0x293: THROW 

    Begin block 0x6eaB0x293
    prev=[0x69eB0x293], succ=[]
    =================================
    0x6eaS0x293: THROW 

    Begin block 0x923B0x293
    prev=[0x68fB0x293], succ=[0x29d]
    =================================
    0x927S0x293: JUMP v294(0x29d)

    Begin block 0x29d
    prev=[0x923B0x293], succ=[]
    =================================
    0x29e: STOP 

}

function investors()() public {
    Begin block 0x29f
    prev=[], succ=[0x2a7, 0x2ab]
    =================================
    0x2a0: v2a0 = CALLVALUE 
    0x2a1: v2a1 = ISZERO v2a0
    0x2a2: v2a2(0x2ab) = CONST 
    0x2a6: JUMPI v2a2(0x2ab), v2a1

    Begin block 0x2a7
    prev=[0x29f], succ=[]
    =================================
    0x2a7: v2a7(0x0) = CONST 
    0x2aa: REVERT v2a7(0x0), v2a7(0x0)

    Begin block 0x2ab
    prev=[0x29f], succ=[0x928]
    =================================
    0x2ac: v2ac(0x2b5) = CONST 
    0x2b0: v2b0(0x928) = CONST 
    0x2b4: JUMP v2b0(0x928)

    Begin block 0x928
    prev=[0x2ab], succ=[0x2b5]
    =================================
    0x929: v929(0xe) = CONST 
    0x92b: v92b = SLOAD v929(0xe)
    0x92d: JUMP v2ac(0x2b5)

    Begin block 0x2b5
    prev=[0x928], succ=[]
    =================================
    0x2b6: v2b6(0x40) = CONST 
    0x2b8: v2b8 = MLOAD v2b6(0x40)
    0x2bc: MSTORE v2b8, v92b
    0x2bd: v2bd(0x20) = CONST 
    0x2bf: v2bf = ADD v2bd(0x20), v2b8
    0x2c3: v2c3(0x40) = CONST 
    0x2c5: v2c5 = MLOAD v2c3(0x40)
    0x2c8: v2c8(0x20) = SUB v2bf, v2c5
    0x2ca: RETURN v2c5, v2c8(0x20)

}

function owner()() public {
    Begin block 0x2cb
    prev=[], succ=[0x2d3, 0x2d7]
    =================================
    0x2cc: v2cc = CALLVALUE 
    0x2cd: v2cd = ISZERO v2cc
    0x2ce: v2ce(0x2d7) = CONST 
    0x2d2: JUMPI v2ce(0x2d7), v2cd

    Begin block 0x2d3
    prev=[0x2cb], succ=[]
    =================================
    0x2d3: v2d3(0x0) = CONST 
    0x2d6: REVERT v2d3(0x0), v2d3(0x0)

    Begin block 0x2d7
    prev=[0x2cb], succ=[0x92e]
    =================================
    0x2d8: v2d8(0x2e1) = CONST 
    0x2dc: v2dc(0x92e) = CONST 
    0x2e0: JUMP v2dc(0x92e)

    Begin block 0x92e
    prev=[0x2d7], succ=[0x2e1]
    =================================
    0x92f: v92f(0x0) = CONST 
    0x933: v933 = SLOAD v92f(0x0)
    0x935: v935(0x100) = CONST 
    0x938: v938(0x1) = EXP v935(0x100), v92f(0x0)
    0x93a: v93a = DIV v933, v938(0x1)
    0x93b: v93b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x950: v950 = AND v93b(0xffffffffffffffffffffffffffffffffffffffff), v93a
    0x952: JUMP v2d8(0x2e1)

    Begin block 0x2e1
    prev=[0x92e], succ=[]
    =================================
    0x2e2: v2e2(0x40) = CONST 
    0x2e4: v2e4 = MLOAD v2e2(0x40)
    0x2e7: v2e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fc: v2fc = AND v2e7(0xffffffffffffffffffffffffffffffffffffffff), v950
    0x2fd: v2fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x312: v312 = AND v2fd(0xffffffffffffffffffffffffffffffffffffffff), v2fc
    0x314: MSTORE v2e4, v312
    0x315: v315(0x20) = CONST 
    0x317: v317 = ADD v315(0x20), v2e4
    0x31b: v31b(0x40) = CONST 
    0x31d: v31d = MLOAD v31b(0x40)
    0x320: v320(0x20) = SUB v317, v31d
    0x322: RETURN v31d, v320(0x20)

}

function profitSharingContract()() public {
    Begin block 0x323
    prev=[], succ=[0x32b, 0x32f]
    =================================
    0x324: v324 = CALLVALUE 
    0x325: v325 = ISZERO v324
    0x326: v326(0x32f) = CONST 
    0x32a: JUMPI v326(0x32f), v325

    Begin block 0x32b
    prev=[0x323], succ=[]
    =================================
    0x32b: v32b(0x0) = CONST 
    0x32e: REVERT v32b(0x0), v32b(0x0)

    Begin block 0x32f
    prev=[0x323], succ=[0x953]
    =================================
    0x330: v330(0x339) = CONST 
    0x334: v334(0x953) = CONST 
    0x338: JUMP v334(0x953)

    Begin block 0x953
    prev=[0x32f], succ=[0x339]
    =================================
    0x954: v954(0xf) = CONST 
    0x956: v956(0x0) = CONST 
    0x959: v959 = SLOAD v954(0xf)
    0x95b: v95b(0x100) = CONST 
    0x95e: v95e(0x1) = EXP v95b(0x100), v956(0x0)
    0x960: v960 = DIV v959, v95e(0x1)
    0x961: v961(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x976: v976 = AND v961(0xffffffffffffffffffffffffffffffffffffffff), v960
    0x978: JUMP v330(0x339)

    Begin block 0x339
    prev=[0x953], succ=[]
    =================================
    0x33a: v33a(0x40) = CONST 
    0x33c: v33c = MLOAD v33a(0x40)
    0x33f: v33f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x354: v354 = AND v33f(0xffffffffffffffffffffffffffffffffffffffff), v976
    0x355: v355(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36a: v36a = AND v355(0xffffffffffffffffffffffffffffffffffffffff), v354
    0x36c: MSTORE v33c, v36a
    0x36d: v36d(0x20) = CONST 
    0x36f: v36f = ADD v36d(0x20), v33c
    0x373: v373(0x40) = CONST 
    0x375: v375 = MLOAD v373(0x40)
    0x378: v378(0x20) = SUB v36f, v375
    0x37a: RETURN v375, v378(0x20)

}

function destroyMyToken(uint256)() public {
    Begin block 0x37b
    prev=[], succ=[0x383, 0x387]
    =================================
    0x37c: v37c = CALLVALUE 
    0x37d: v37d = ISZERO v37c
    0x37e: v37e(0x387) = CONST 
    0x382: JUMPI v37e(0x387), v37d

    Begin block 0x383
    prev=[0x37b], succ=[]
    =================================
    0x383: v383(0x0) = CONST 
    0x386: REVERT v383(0x0), v383(0x0)

    Begin block 0x387
    prev=[0x37b], succ=[0x979B0x387]
    =================================
    0x388: v388(0x39f) = CONST 
    0x38c: v38c(0x4) = CONST 
    0x390: v390 = CALLDATALOAD v38c(0x4)
    0x392: v392(0x20) = CONST 
    0x394: v394(0x24) = ADD v392(0x20), v38c(0x4)
    0x39a: v39a(0x979) = CONST 
    0x39e: JUMP v39a(0x979)

    Begin block 0x979B0x387
    prev=[0x387], succ=[0x9d1B0x387, 0x9d5B0x387]
    =================================
    0x97aS0x387: v97aV387(0x0) = CONST 
    0x97eS0x387: v97eV387 = SLOAD v97aV387(0x0)
    0x980S0x387: v980V387(0x100) = CONST 
    0x983S0x387: v983V387(0x1) = EXP v980V387(0x100), v97aV387(0x0)
    0x985S0x387: v985V387 = DIV v97eV387, v983V387(0x1)
    0x986S0x387: v986V387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x99bS0x387: v99bV387 = AND v986V387(0xffffffffffffffffffffffffffffffffffffffff), v985V387
    0x99cS0x387: v99cV387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9b1S0x387: v9b1V387 = AND v99cV387(0xffffffffffffffffffffffffffffffffffffffff), v99bV387
    0x9b2S0x387: v9b2V387 = CALLER 
    0x9b3S0x387: v9b3V387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9c8S0x387: v9c8V387 = AND v9b3V387(0xffffffffffffffffffffffffffffffffffffffff), v9b2V387
    0x9c9S0x387: v9c9V387 = EQ v9c8V387, v9b1V387
    0x9caS0x387: v9caV387 = ISZERO v9c9V387
    0x9cbS0x387: v9cbV387 = ISZERO v9caV387
    0x9ccS0x387: v9ccV387(0x9d5) = CONST 
    0x9d0S0x387: JUMPI v9ccV387(0x9d5), v9cbV387

    Begin block 0x9d1B0x387
    prev=[0x979B0x387], succ=[]
    =================================
    0x9d1S0x387: v9d1V387(0x0) = CONST 
    0x9d4S0x387: REVERT v9d1V387(0x0), v9d1V387(0x0)

    Begin block 0x9d5B0x387
    prev=[0x979B0x387], succ=[0xa30B0x387]
    =================================
    0x9d6S0x387: v9d6V387(0x1) = CONST 
    0x9d8S0x387: v9d8V387(0x0) = CONST 
    0x9dbS0x387: v9dbV387 = SLOAD v9d6V387(0x1)
    0x9ddS0x387: v9ddV387(0x100) = CONST 
    0x9e0S0x387: v9e0V387(0x1) = EXP v9ddV387(0x100), v9d8V387(0x0)
    0x9e2S0x387: v9e2V387 = DIV v9dbV387, v9e0V387(0x1)
    0x9e3S0x387: v9e3V387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9f8S0x387: v9f8V387 = AND v9e3V387(0xffffffffffffffffffffffffffffffffffffffff), v9e2V387
    0x9f9S0x387: v9f9V387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa0eS0x387: va0eV387 = AND v9f9V387(0xffffffffffffffffffffffffffffffffffffffff), v9f8V387
    0xa0fS0x387: va0fV387(0x8dec3daa) = CONST 
    0xa14S0x387: va14V387(0xa30) = CONST 
    0xa18S0x387: va18V387(0xde0b6b3a7640000) = CONST 
    0xa22S0x387: va22V387(0xe5d) = CONST 
    0xa29S0x387: va29V387(0xffffffff) = CONST 
    0xa2eS0x387: va2eV387(0xe5d) = AND va29V387(0xffffffff), va22V387(0xe5d)
    0xa2fS0x387: va2f_0V387 = CALLPRIVATE va2eV387(0xe5d), va18V387(0xde0b6b3a7640000), v390, va14V387(0xa30)

    Begin block 0xa30B0x387
    prev=[0x9d5B0x387], succ=[0xab2B0x387, 0xab6B0x387]
    =================================
    0xa31S0x387: va31V387 = CALLER 
    0xa32S0x387: va32V387(0x40) = CONST 
    0xa34S0x387: va34V387 = MLOAD va32V387(0x40)
    0xa36S0x387: va36V387(0xffffffff) = CONST 
    0xa3bS0x387: va3bV387(0x8dec3daa) = AND va36V387(0xffffffff), va0fV387(0x8dec3daa)
    0xa3cS0x387: va3cV387(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xa5aS0x387: va5aV387(0x8dec3daa00000000000000000000000000000000000000000000000000000000) = MUL va3cV387(0x100000000000000000000000000000000000000000000000000000000), va3bV387(0x8dec3daa)
    0xa5cS0x387: MSTORE va34V387, va5aV387(0x8dec3daa00000000000000000000000000000000000000000000000000000000)
    0xa5dS0x387: va5dV387(0x4) = CONST 
    0xa5fS0x387: va5fV387 = ADD va5dV387(0x4), va34V387
    0xa63S0x387: MSTORE va5fV387, va2f_0V387
    0xa64S0x387: va64V387(0x20) = CONST 
    0xa66S0x387: va66V387 = ADD va64V387(0x20), va5fV387
    0xa68S0x387: va68V387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa7dS0x387: va7dV387 = AND va68V387(0xffffffffffffffffffffffffffffffffffffffff), va31V387
    0xa7eS0x387: va7eV387(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa93S0x387: va93V387 = AND va7eV387(0xffffffffffffffffffffffffffffffffffffffff), va7dV387
    0xa95S0x387: MSTORE va66V387, va93V387
    0xa96S0x387: va96V387(0x20) = CONST 
    0xa98S0x387: va98V387 = ADD va96V387(0x20), va66V387
    0xa9dS0x387: va9dV387(0x0) = CONST 
    0xa9fS0x387: va9fV387(0x40) = CONST 
    0xaa1S0x387: vaa1V387 = MLOAD va9fV387(0x40)
    0xaa4S0x387: vaa4V387(0x44) = SUB va98V387, vaa1V387
    0xaa6S0x387: vaa6V387(0x0) = CONST 
    0xaaaS0x387: vaaaV387 = EXTCODESIZE va0eV387
    0xaabS0x387: vaabV387 = ISZERO vaaaV387
    0xaacS0x387: vaacV387 = ISZERO vaabV387
    0xaadS0x387: vaadV387(0xab6) = CONST 
    0xab1S0x387: JUMPI vaadV387(0xab6), vaacV387

    Begin block 0xab2B0x387
    prev=[0xa30B0x387], succ=[]
    =================================
    0xab2S0x387: vab2V387(0x0) = CONST 
    0xab5S0x387: REVERT vab2V387(0x0), vab2V387(0x0)

    Begin block 0xab6B0x387
    prev=[0xa30B0x387], succ=[0xac4B0x387, 0xac8B0x387]
    =================================
    0xab7S0x387: vab7V387(0x2c6) = CONST 
    0xabaS0x387: vabaV387 = GAS 
    0xabbS0x387: vabbV387 = SUB vabaV387, vab7V387(0x2c6)
    0xabcS0x387: vabcV387 = CALL vabbV387, va0eV387, vaa6V387(0x0), vaa1V387, vaa4V387(0x44), vaa1V387, va9dV387(0x0)
    0xabdS0x387: vabdV387 = ISZERO vabcV387
    0xabeS0x387: vabeV387 = ISZERO vabdV387
    0xabfS0x387: vabfV387(0xac8) = CONST 
    0xac3S0x387: JUMPI vabfV387(0xac8), vabeV387

    Begin block 0xac4B0x387
    prev=[0xab6B0x387], succ=[]
    =================================
    0xac4S0x387: vac4V387(0x0) = CONST 
    0xac7S0x387: REVERT vac4V387(0x0), vac4V387(0x0)

    Begin block 0xac8B0x387
    prev=[0xab6B0x387], succ=[0x39f]
    =================================
    0xacdS0x387: JUMP v388(0x39f)

    Begin block 0x39f
    prev=[0xac8B0x387], succ=[]
    =================================
    0x3a0: STOP 

}

function buyTokens(address)() public {
    Begin block 0x3a1
    prev=[], succ=[0x3cf]
    =================================
    0x3a2: v3a2(0x3cf) = CONST 
    0x3a6: v3a6(0x4) = CONST 
    0x3aa: v3aa = CALLDATALOAD v3a6(0x4)
    0x3ab: v3ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c0: v3c0 = AND v3ab(0xffffffffffffffffffffffffffffffffffffffff), v3aa
    0x3c2: v3c2(0x20) = CONST 
    0x3c4: v3c4(0x24) = ADD v3c2(0x20), v3a6(0x4)
    0x3ca: v3ca(0xace) = CONST 
    0x3ce: CALLPRIVATE v3ca(0xace), v3c0, v3a2(0x3cf)

    Begin block 0x3cf
    prev=[0x3a1], succ=[]
    =================================
    0x3d0: STOP 

}

function hasEnded()() public {
    Begin block 0x3d1
    prev=[], succ=[0x3d9, 0x3dd]
    =================================
    0x3d2: v3d2 = CALLVALUE 
    0x3d3: v3d3 = ISZERO v3d2
    0x3d4: v3d4(0x3dd) = CONST 
    0x3d8: JUMPI v3d4(0x3dd), v3d3

    Begin block 0x3d9
    prev=[0x3d1], succ=[]
    =================================
    0x3d9: v3d9(0x0) = CONST 
    0x3dc: REVERT v3d9(0x0), v3d9(0x0)

    Begin block 0x3dd
    prev=[0x3d1], succ=[0x3e7]
    =================================
    0x3de: v3de(0x3e7) = CONST 
    0x3e2: v3e2(0xd2c) = CONST 
    0x3e6: v3e6_0 = CALLPRIVATE v3e2(0xd2c), v3de(0x3e7)

    Begin block 0x3e7
    prev=[0x3dd], succ=[]
    =================================
    0x3e8: v3e8(0x40) = CONST 
    0x3ea: v3ea = MLOAD v3e8(0x40)
    0x3ed: v3ed = ISZERO v3e6_0
    0x3ee: v3ee = ISZERO v3ed
    0x3ef: v3ef = ISZERO v3ee
    0x3f0: v3f0 = ISZERO v3ef
    0x3f2: MSTORE v3ea, v3f0
    0x3f3: v3f3(0x20) = CONST 
    0x3f5: v3f5 = ADD v3f3(0x20), v3ea
    0x3f9: v3f9(0x40) = CONST 
    0x3fb: v3fb = MLOAD v3f9(0x40)
    0x3fe: v3fe(0x20) = SUB v3f5, v3fb
    0x400: RETURN v3fb, v3fe(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x401
    prev=[], succ=[0x409, 0x40d]
    =================================
    0x402: v402 = CALLVALUE 
    0x403: v403 = ISZERO v402
    0x404: v404(0x40d) = CONST 
    0x408: JUMPI v404(0x40d), v403

    Begin block 0x409
    prev=[0x401], succ=[]
    =================================
    0x409: v409(0x0) = CONST 
    0x40c: REVERT v409(0x0), v409(0x0)

    Begin block 0x40d
    prev=[0x401], succ=[0xd60B0x40d]
    =================================
    0x40e: v40e(0x43b) = CONST 
    0x412: v412(0x4) = CONST 
    0x416: v416 = CALLDATALOAD v412(0x4)
    0x417: v417(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42c: v42c = AND v417(0xffffffffffffffffffffffffffffffffffffffff), v416
    0x42e: v42e(0x20) = CONST 
    0x430: v430(0x24) = ADD v42e(0x20), v412(0x4)
    0x436: v436(0xd60) = CONST 
    0x43a: JUMP v436(0xd60)

    Begin block 0xd60B0x40d
    prev=[0x40d], succ=[0xdb8B0x40d, 0xdbcB0x40d]
    =================================
    0xd61S0x40d: vd61V40d(0x0) = CONST 
    0xd65S0x40d: vd65V40d = SLOAD vd61V40d(0x0)
    0xd67S0x40d: vd67V40d(0x100) = CONST 
    0xd6aS0x40d: vd6aV40d(0x1) = EXP vd67V40d(0x100), vd61V40d(0x0)
    0xd6cS0x40d: vd6cV40d = DIV vd65V40d, vd6aV40d(0x1)
    0xd6dS0x40d: vd6dV40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd82S0x40d: vd82V40d = AND vd6dV40d(0xffffffffffffffffffffffffffffffffffffffff), vd6cV40d
    0xd83S0x40d: vd83V40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd98S0x40d: vd98V40d = AND vd83V40d(0xffffffffffffffffffffffffffffffffffffffff), vd82V40d
    0xd99S0x40d: vd99V40d = CALLER 
    0xd9aS0x40d: vd9aV40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdafS0x40d: vdafV40d = AND vd9aV40d(0xffffffffffffffffffffffffffffffffffffffff), vd99V40d
    0xdb0S0x40d: vdb0V40d = EQ vdafV40d, vd98V40d
    0xdb1S0x40d: vdb1V40d = ISZERO vdb0V40d
    0xdb2S0x40d: vdb2V40d = ISZERO vdb1V40d
    0xdb3S0x40d: vdb3V40d(0xdbc) = CONST 
    0xdb7S0x40d: JUMPI vdb3V40d(0xdbc), vdb2V40d

    Begin block 0xdb8B0x40d
    prev=[0xd60B0x40d], succ=[]
    =================================
    0xdb8S0x40d: vdb8V40d(0x0) = CONST 
    0xdbbS0x40d: REVERT vdb8V40d(0x0), vdb8V40d(0x0)

    Begin block 0xdbcB0x40d
    prev=[0xd60B0x40d], succ=[0xdf4B0x40d, 0x32048B0x40d]
    =================================
    0xdbdS0x40d: vdbdV40d(0x0) = CONST 
    0xdbfS0x40d: vdbfV40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdd4S0x40d: vdd4V40d(0x0) = AND vdbfV40d(0xffffffffffffffffffffffffffffffffffffffff), vdbdV40d(0x0)
    0xdd6S0x40d: vdd6V40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdebS0x40d: vdebV40d = AND vdd6V40d(0xffffffffffffffffffffffffffffffffffffffff), v42c
    0xdecS0x40d: vdecV40d = EQ vdebV40d, vdd4V40d(0x0)
    0xdedS0x40d: vdedV40d = ISZERO vdecV40d
    0xdeeS0x40d: vdeeV40d = ISZERO vdedV40d
    0xdefS0x40d: vdefV40d(0x32048) = CONST 
    0xdf3S0x40d: JUMPI vdefV40d(0x32048), vdeeV40d

    Begin block 0xdf4B0x40d
    prev=[0xdbcB0x40d], succ=[0x3218aB0x40d]
    =================================
    0xdf5S0x40d: vdf5V40d(0x0) = CONST 
    0xdf8S0x40d: vdf8V40d(0x100) = CONST 
    0xdfbS0x40d: vdfbV40d(0x1) = EXP vdf8V40d(0x100), vdf5V40d(0x0)
    0xdfdS0x40d: vdfdV40d = SLOAD vdf5V40d(0x0)
    0xdffS0x40d: vdffV40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe14S0x40d: ve14V40d(0xffffffffffffffffffffffffffffffffffffffff) = MUL vdffV40d(0xffffffffffffffffffffffffffffffffffffffff), vdfbV40d(0x1)
    0xe15S0x40d: ve15V40d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT ve14V40d(0xffffffffffffffffffffffffffffffffffffffff)
    0xe16S0x40d: ve16V40d = AND ve15V40d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdfdV40d
    0xe19S0x40d: ve19V40d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe2eS0x40d: ve2eV40d = AND ve19V40d(0xffffffffffffffffffffffffffffffffffffffff), v42c
    0xe2fS0x40d: ve2fV40d = MUL ve2eV40d, vdfbV40d(0x1)
    0xe30S0x40d: ve30V40d = OR ve2fV40d, ve16V40d
    0xe32S0x40d: SSTORE vdf5V40d(0x0), ve30V40d
    0xa9e2S0x40d: va9e2V40d(0x3218a) = CONST 
    0xaa02S0x40d: JUMP va9e2V40d(0x3218a)

    Begin block 0x3218aB0x40d
    prev=[0xdf4B0x40d], succ=[0x43b]
    =================================
    0x3218cS0x40d: JUMP v40e(0x43b)

    Begin block 0x43b
    prev=[0x32048B0x40d, 0x3218aB0x40d], succ=[]
    =================================
    0x43c: STOP 

    Begin block 0x32048B0x40d
    prev=[0xdbcB0x40d], succ=[0x43b]
    =================================
    0x3204aS0x40d: JUMP v40e(0x43b)

}

function token()() public {
    Begin block 0x43d
    prev=[], succ=[0x445, 0x449]
    =================================
    0x43e: v43e = CALLVALUE 
    0x43f: v43f = ISZERO v43e
    0x440: v440(0x449) = CONST 
    0x444: JUMPI v440(0x449), v43f

    Begin block 0x445
    prev=[0x43d], succ=[]
    =================================
    0x445: v445(0x0) = CONST 
    0x448: REVERT v445(0x0), v445(0x0)

    Begin block 0x449
    prev=[0x43d], succ=[0xe37]
    =================================
    0x44a: v44a(0x453) = CONST 
    0x44e: v44e(0xe37) = CONST 
    0x452: JUMP v44e(0xe37)

    Begin block 0xe37
    prev=[0x449], succ=[0x453]
    =================================
    0xe38: ve38(0x1) = CONST 
    0xe3a: ve3a(0x0) = CONST 
    0xe3d: ve3d = SLOAD ve38(0x1)
    0xe3f: ve3f(0x100) = CONST 
    0xe42: ve42(0x1) = EXP ve3f(0x100), ve3a(0x0)
    0xe44: ve44 = DIV ve3d, ve42(0x1)
    0xe45: ve45(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe5a: ve5a = AND ve45(0xffffffffffffffffffffffffffffffffffffffff), ve44
    0xe5c: JUMP v44a(0x453)

    Begin block 0x453
    prev=[0xe37], succ=[]
    =================================
    0x454: v454(0x40) = CONST 
    0x456: v456 = MLOAD v454(0x40)
    0x459: v459(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x46e: v46e = AND v459(0xffffffffffffffffffffffffffffffffffffffff), ve5a
    0x46f: v46f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x484: v484 = AND v46f(0xffffffffffffffffffffffffffffffffffffffff), v46e
    0x486: MSTORE v456, v484
    0x487: v487(0x20) = CONST 
    0x489: v489 = ADD v487(0x20), v456
    0x48d: v48d(0x40) = CONST 
    0x48f: v48f = MLOAD v48d(0x40)
    0x492: v492(0x20) = SUB v489, v48f
    0x494: RETURN v48f, v492(0x20)

}

function 0xace(vacearg0, vacearg1) private {
    Begin block 0xace
    prev=[], succ=[0xaf4, 0xaf8]
    =================================
    0xacf: vacf(0x0) = CONST 
    0xad2: vad2(0x0) = CONST 
    0xad5: vad5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaea: vaea = AND vad5(0xffffffffffffffffffffffffffffffffffffffff), vacearg0
    0xaeb: vaeb = EQ vaea, vad2(0x0)
    0xaec: vaec = ISZERO vaeb
    0xaed: vaed = ISZERO vaec
    0xaee: vaee = ISZERO vaed
    0xaef: vaef(0xaf8) = CONST 
    0xaf3: JUMPI vaef(0xaf8), vaee

    Begin block 0xaf4
    prev=[0xace], succ=[]
    =================================
    0xaf4: vaf4(0x0) = CONST 
    0xaf7: REVERT vaf4(0x0), vaf4(0x0)

    Begin block 0xaf8
    prev=[0xace], succ=[0x10b4]
    =================================
    0xaf9: vaf9(0xb02) = CONST 
    0xafd: vafd(0x10b4) = CONST 
    0xb01: JUMP vafd(0x10b4)

    Begin block 0x10b4
    prev=[0xaf8], succ=[0xb02]
    =================================
    0x10b5: v10b5(0x0) = CONST 
    0x10b8: v10b8 = CALLVALUE 
    0x10b9: v10b9 = EQ v10b8, v10b5(0x0)
    0x10ba: v10ba = ISZERO v10b9
    0x10be: JUMP vaf9(0xb02)

    Begin block 0xb02
    prev=[0x10b4], succ=[0xb0a, 0xb0e]
    =================================
    0xb03: vb03 = ISZERO v10ba
    0xb04: vb04 = ISZERO vb03
    0xb05: vb05(0xb0e) = CONST 
    0xb09: JUMPI vb05(0xb0e), vb04

    Begin block 0xb0a
    prev=[0xb02], succ=[]
    =================================
    0xb0a: vb0a(0x0) = CONST 
    0xb0d: REVERT vb0a(0x0), vb0a(0x0)

    Begin block 0xb0e
    prev=[0xb02], succ=[0xb18]
    =================================
    0xb0f: vb0f(0xb18) = CONST 
    0xb13: vb13(0xd2c) = CONST 
    0xb17: vb17_0 = CALLPRIVATE vb13(0xd2c), vb0f(0xb18)

    Begin block 0xb18
    prev=[0xb0e], succ=[0xb21, 0xb25]
    =================================
    0xb19: vb19 = ISZERO vb17_0
    0xb1a: vb1a = ISZERO vb19
    0xb1b: vb1b = ISZERO vb1a
    0xb1c: vb1c(0xb25) = CONST 
    0xb20: JUMPI vb1c(0xb25), vb1b

    Begin block 0xb21
    prev=[0xb18], succ=[]
    =================================
    0xb21: vb21(0x0) = CONST 
    0xb24: REVERT vb21(0x0), vb21(0x0)

    Begin block 0xb25
    prev=[0xb18], succ=[0xb3c, 0xb36]
    =================================
    0xb26: vb26 = CALLVALUE 
    0xb29: vb29(0x4) = CONST 
    0xb2b: vb2b = SLOAD vb29(0x4)
    0xb2c: vb2c = TIMESTAMP 
    0xb2d: vb2d = LT vb2c, vb2b
    0xb2e: vb2e = ISZERO vb2d
    0xb30: vb30 = ISZERO vb2e
    0xb31: vb31(0xb3c) = CONST 
    0xb35: JUMPI vb31(0xb3c), vb30

    Begin block 0xb3c
    prev=[0xb25, 0xb36], succ=[0xb43, 0xb61]
    =================================
    0xb3c_0x0: vb3c_0 = PHI vb2e, vb3b
    0xb3d: vb3d = ISZERO vb3c_0
    0xb3e: vb3e(0xb61) = CONST 
    0xb42: JUMPI vb3e(0xb61), vb3d

    Begin block 0xb43
    prev=[0xb3c], succ=[0xb59]
    =================================
    0xb43: vb43(0xb59) = CONST 
    0xb47: vb47(0x2af8) = CONST 
    0xb4b: vb4b(0xe5d) = CONST 
    0xb52: vb52(0xffffffff) = CONST 
    0xb57: vb57(0xe5d) = AND vb52(0xffffffff), vb4b(0xe5d)
    0xb58: vb58_0 = CALLPRIVATE vb57(0xe5d), vb47(0x2af8), vb26, vb43(0xb59)

    Begin block 0xb59
    prev=[0xb43], succ=[0xb96]
    =================================
    0xb5c: vb5c(0xb96) = CONST 
    0xb60: JUMP vb5c(0xb96)

    Begin block 0xb96
    prev=[0xb59, 0xb95], succ=[0xbad]
    =================================
    0xb97: vb97(0xbad) = CONST 
    0xb9c: vb9c(0x3) = CONST 
    0xb9e: vb9e = SLOAD vb9c(0x3)
    0xb9f: vb9f(0x10bf) = CONST 
    0xba6: vba6(0xffffffff) = CONST 
    0xbab: vbab(0x10bf) = AND vba6(0xffffffff), vb9f(0x10bf)
    0xbac: vbac_0 = CALLPRIVATE vbab(0x10bf), vb26, vb9e, vb97(0xbad)

    Begin block 0xbad
    prev=[0xb96], succ=[0xc7d, 0xc81]
    =================================
    0xbad_0x1: vbad_1 = PHI vacf(0x0), vb58_0, vb91_0
    0xbae: vbae(0x3) = CONST 
    0xbb2: SSTORE vbae(0x3), vbac_0
    0xbb4: vbb4(0x1) = CONST 
    0xbb6: vbb6(0x0) = CONST 
    0xbb9: vbb9 = SLOAD vbb4(0x1)
    0xbbb: vbbb(0x100) = CONST 
    0xbbe: vbbe(0x1) = EXP vbbb(0x100), vbb6(0x0)
    0xbc0: vbc0 = DIV vbb9, vbbe(0x1)
    0xbc1: vbc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbd6: vbd6 = AND vbc1(0xffffffffffffffffffffffffffffffffffffffff), vbc0
    0xbd7: vbd7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbec: vbec = AND vbd7(0xffffffffffffffffffffffffffffffffffffffff), vbd6
    0xbed: vbed(0x40c10f19) = CONST 
    0xbf4: vbf4(0x0) = CONST 
    0xbf6: vbf6(0x40) = CONST 
    0xbf8: vbf8 = MLOAD vbf6(0x40)
    0xbf9: vbf9(0x20) = CONST 
    0xbfb: vbfb = ADD vbf9(0x20), vbf8
    0xbfc: MSTORE vbfb, vbf4(0x0)
    0xbfd: vbfd(0x40) = CONST 
    0xbff: vbff = MLOAD vbfd(0x40)
    0xc01: vc01(0xffffffff) = CONST 
    0xc06: vc06(0x40c10f19) = AND vc01(0xffffffff), vbed(0x40c10f19)
    0xc07: vc07(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xc25: vc25(0x40c10f1900000000000000000000000000000000000000000000000000000000) = MUL vc07(0x100000000000000000000000000000000000000000000000000000000), vc06(0x40c10f19)
    0xc27: MSTORE vbff, vc25(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0xc28: vc28(0x4) = CONST 
    0xc2a: vc2a = ADD vc28(0x4), vbff
    0xc2d: vc2d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc42: vc42 = AND vc2d(0xffffffffffffffffffffffffffffffffffffffff), vacearg0
    0xc43: vc43(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc58: vc58 = AND vc43(0xffffffffffffffffffffffffffffffffffffffff), vc42
    0xc5a: MSTORE vc2a, vc58
    0xc5b: vc5b(0x20) = CONST 
    0xc5d: vc5d = ADD vc5b(0x20), vc2a
    0xc60: MSTORE vc5d, vbad_1
    0xc61: vc61(0x20) = CONST 
    0xc63: vc63 = ADD vc61(0x20), vc5d
    0xc68: vc68(0x20) = CONST 
    0xc6a: vc6a(0x40) = CONST 
    0xc6c: vc6c = MLOAD vc6a(0x40)
    0xc6f: vc6f(0x44) = SUB vc63, vc6c
    0xc71: vc71(0x0) = CONST 
    0xc75: vc75 = EXTCODESIZE vbec
    0xc76: vc76 = ISZERO vc75
    0xc77: vc77 = ISZERO vc76
    0xc78: vc78(0xc81) = CONST 
    0xc7c: JUMPI vc78(0xc81), vc77

    Begin block 0xc7d
    prev=[0xbad], succ=[]
    =================================
    0xc7d: vc7d(0x0) = CONST 
    0xc80: REVERT vc7d(0x0), vc7d(0x0)

    Begin block 0xc81
    prev=[0xbad], succ=[0xc8f, 0xc93]
    =================================
    0xc82: vc82(0x2c6) = CONST 
    0xc85: vc85 = GAS 
    0xc86: vc86 = SUB vc85, vc82(0x2c6)
    0xc87: vc87 = CALL vc86, vbec, vc71(0x0), vc6c, vc6f(0x44), vc6c, vc68(0x20)
    0xc88: vc88 = ISZERO vc87
    0xc89: vc89 = ISZERO vc88
    0xc8a: vc8a(0xc93) = CONST 
    0xc8e: JUMPI vc8a(0xc93), vc89

    Begin block 0xc8f
    prev=[0xc81], succ=[]
    =================================
    0xc8f: vc8f(0x0) = CONST 
    0xc92: REVERT vc8f(0x0), vc8f(0x0)

    Begin block 0xc93
    prev=[0xc81], succ=[0xca9]
    =================================
    0xc97: vc97(0x40) = CONST 
    0xc99: vc99 = MLOAD vc97(0x40)
    0xc9b: vc9b = MLOAD vc99
    0xc9f: vc9f(0xca9) = CONST 
    0xca4: vca4(0x10de) = CONST 
    0xca8: CALLPRIVATE vca4(0x10de), vacearg0, vc9f(0xca9)

    Begin block 0xca9
    prev=[0xc93], succ=[0xd27]
    =================================
    0xca9_0x0: vca9_0 = PHI vacf(0x0), vb58_0, vb91_0
    0xcab: vcab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcc0: vcc0 = AND vcab(0xffffffffffffffffffffffffffffffffffffffff), vacearg0
    0xcc1: vcc1 = CALLER 
    0xcc2: vcc2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcd7: vcd7 = AND vcc2(0xffffffffffffffffffffffffffffffffffffffff), vcc1
    0xcd8: vcd8(0xfe0e12b43090c1fc19a34aefa5cc138a4eeafc60ab800f855c730b3fb9480e) = CONST 
    0xcfa: vcfa = TIMESTAMP 
    0xcfb: vcfb(0x40) = CONST 
    0xcfd: vcfd = MLOAD vcfb(0x40)
    0xd01: MSTORE vcfd, vb26
    0xd02: vd02(0x20) = CONST 
    0xd04: vd04 = ADD vd02(0x20), vcfd
    0xd07: MSTORE vd04, vca9_0
    0xd08: vd08(0x20) = CONST 
    0xd0a: vd0a = ADD vd08(0x20), vd04
    0xd0d: MSTORE vd0a, vcfa
    0xd0e: vd0e(0x20) = CONST 
    0xd10: vd10 = ADD vd0e(0x20), vd0a
    0xd16: vd16(0x40) = CONST 
    0xd18: vd18 = MLOAD vd16(0x40)
    0xd1b: vd1b(0x60) = SUB vd10, vd18
    0xd1d: LOG3 vd18, vd1b(0x60), vcd8(0xfe0e12b43090c1fc19a34aefa5cc138a4eeafc60ab800f855c730b3fb9480e), vcd7, vcc0
    0xd1e: vd1e(0xd27) = CONST 
    0xd22: vd22(0x11f3) = CONST 
    0xd26: CALLPRIVATE vd22(0x11f3), vd1e(0xd27)

    Begin block 0xd27
    prev=[0xca9], succ=[]
    =================================
    0xd2b: RETURNPRIVATE vacearg1

    Begin block 0xb61
    prev=[0xb3c], succ=[0xb75, 0xb6f]
    =================================
    0xb62: vb62(0x7) = CONST 
    0xb64: vb64 = SLOAD vb62(0x7)
    0xb65: vb65 = TIMESTAMP 
    0xb66: vb66 = LT vb65, vb64
    0xb67: vb67 = ISZERO vb66
    0xb69: vb69 = ISZERO vb67
    0xb6a: vb6a(0xb75) = CONST 
    0xb6e: JUMPI vb6a(0xb75), vb69

    Begin block 0xb75
    prev=[0xb61, 0xb6f], succ=[0xb7c, 0xb95]
    =================================
    0xb75_0x0: vb75_0 = PHI vb67, vb74
    0xb76: vb76 = ISZERO vb75_0
    0xb77: vb77(0xb95) = CONST 
    0xb7b: JUMPI vb77(0xb95), vb76

    Begin block 0xb7c
    prev=[0xb75], succ=[0xb92]
    =================================
    0xb7c: vb7c(0xb92) = CONST 
    0xb80: vb80(0x2710) = CONST 
    0xb84: vb84(0xe5d) = CONST 
    0xb8b: vb8b(0xffffffff) = CONST 
    0xb90: vb90(0xe5d) = AND vb8b(0xffffffff), vb84(0xe5d)
    0xb91: vb91_0 = CALLPRIVATE vb90(0xe5d), vb80(0x2710), vb26, vb7c(0xb92)

    Begin block 0xb92
    prev=[0xb7c], succ=[0xb95]
    =================================
    0x77e2: v77e2(0xb95) = CONST 
    0x7802: JUMP v77e2(0xb95)

    Begin block 0xb95
    prev=[0xb75, 0xb92], succ=[0xb96]
    =================================
    0x81e2: v81e2(0xb96) = CONST 
    0x8202: JUMP v81e2(0xb96)

    Begin block 0xb6f
    prev=[0xb61], succ=[0xb75]
    =================================
    0xb70: vb70(0xb) = CONST 
    0xb72: vb72 = SLOAD vb70(0xb)
    0xb73: vb73 = TIMESTAMP 
    0xb74: vb74 = LT vb73, vb72
    0x6de2: v6de2(0xb75) = CONST 
    0x6e02: JUMP v6de2(0xb75)

    Begin block 0xb36
    prev=[0xb25], succ=[0xb3c]
    =================================
    0xb37: vb37(0x6) = CONST 
    0xb39: vb39 = SLOAD vb37(0x6)
    0xb3a: vb3a = TIMESTAMP 
    0xb3b: vb3b = LT vb3a, vb39
    0x63e2: v63e2(0xb3c) = CONST 
    0x6402: JUMP v63e2(0xb3c)

}

function 0xd2c(vd2carg0) private {
    Begin block 0xd2c
    prev=[], succ=[0xd4e, 0xd3a]
    =================================
    0xd2d: vd2d(0x0) = CONST 
    0xd2f: vd2f(0x4) = CONST 
    0xd31: vd31 = SLOAD vd2f(0x4)
    0xd32: vd32 = TIMESTAMP 
    0xd33: vd33 = LT vd32, vd31
    0xd35: vd35(0xd4e) = CONST 
    0xd39: JUMPI vd35(0xd4e), vd33

    Begin block 0xd4e
    prev=[0xd2c, 0xd4d], succ=[0x32024, 0xd55]
    =================================
    0xd4e_0x0: vd4e_0 = PHI vd33, vd3f, vd4c
    0xd50: vd50(0x32024) = CONST 
    0xd54: JUMPI vd50(0x32024), vd4e_0

    Begin block 0x32024
    prev=[0xd4e], succ=[]
    =================================
    0x32024_0x0: v32024_0 = PHI vd33, vd3f, vd4c
    0x32028: RETURNPRIVATE vd2carg0, v32024_0

    Begin block 0xd55
    prev=[0xd4e], succ=[0x32166]
    =================================
    0xd56: vd56(0xb) = CONST 
    0xd58: vd58 = SLOAD vd56(0xb)
    0xd59: vd59 = TIMESTAMP 
    0xd5a: vd5a = GT vd59, vd58
    0x9fe2: v9fe2(0x32166) = CONST 
    0xa002: JUMP v9fe2(0x32166)

    Begin block 0x32166
    prev=[0xd55], succ=[]
    =================================
    0x3216a: RETURNPRIVATE vd2carg0, vd5a

    Begin block 0xd3a
    prev=[0xd2c], succ=[0xd4d, 0xd47]
    =================================
    0xd3b: vd3b(0x6) = CONST 
    0xd3d: vd3d = SLOAD vd3b(0x6)
    0xd3e: vd3e = TIMESTAMP 
    0xd3f: vd3f = GT vd3e, vd3d
    0xd41: vd41 = ISZERO vd3f
    0xd42: vd42(0xd4d) = CONST 
    0xd46: JUMPI vd42(0xd4d), vd41

    Begin block 0xd4d
    prev=[0xd3a, 0xd47], succ=[0xd4e]
    =================================
    0x95e2: v95e2(0xd4e) = CONST 
    0x9602: JUMP v95e2(0xd4e)

    Begin block 0xd47
    prev=[0xd3a], succ=[0xd4d]
    =================================
    0xd48: vd48(0x7) = CONST 
    0xd4a: vd4a = SLOAD vd48(0x7)
    0xd4b: vd4b = TIMESTAMP 
    0xd4c: vd4c = LT vd4b, vd4a
    0x8be2: v8be2(0xd4d) = CONST 
    0x8c02: JUMP v8be2(0xd4d)

}

function 0xe5d(ve5darg0, ve5darg1, ve5darg2) private {
    Begin block 0xe5d
    prev=[], succ=[0xe6b, 0xe74]
    =================================
    0xe5e: ve5e(0x0) = CONST 
    0xe61: ve61(0x0) = CONST 
    0xe64: ve64 = EQ ve5darg1, ve61(0x0)
    0xe65: ve65 = ISZERO ve64
    0xe66: ve66(0xe74) = CONST 
    0xe6a: JUMPI ve66(0xe74), ve65

    Begin block 0xe6b
    prev=[0xe5d], succ=[0x3206a]
    =================================
    0xe6b: ve6b(0x0) = CONST 
    0xe6f: ve6f(0x3206a) = CONST 
    0xe73: JUMP ve6f(0x3206a)

    Begin block 0x3206a
    prev=[0xe6b], succ=[]
    =================================
    0x32070: RETURNPRIVATE ve5darg2, ve6b(0x0)

    Begin block 0xe74
    prev=[0xe5d], succ=[0xe85, 0xe86]
    =================================
    0xe77: ve77 = MUL ve5darg1, ve5darg0
    0xe7e: ve7e = ISZERO ve5darg1
    0xe7f: ve7f = ISZERO ve7e
    0xe80: ve80(0xe86) = CONST 
    0xe84: JUMPI ve80(0xe86), ve7f

    Begin block 0xe85
    prev=[0xe74], succ=[]
    =================================
    0xe85: THROW 

    Begin block 0xe86
    prev=[0xe74], succ=[0xe90, 0xe91]
    =================================
    0xe87: ve87 = DIV ve77, ve5darg1
    0xe88: ve88 = EQ ve87, ve5darg0
    0xe89: ve89 = ISZERO ve88
    0xe8a: ve8a = ISZERO ve89
    0xe8b: ve8b(0xe91) = CONST 
    0xe8f: JUMPI ve8b(0xe91), ve8a

    Begin block 0xe90
    prev=[0xe86], succ=[]
    =================================
    0xe90: THROW 

    Begin block 0xe91
    prev=[0xe86], succ=[0x321ac]
    =================================
    0xb3e2: vb3e2(0x321ac) = CONST 
    0xb402: JUMP vb3e2(0x321ac)

    Begin block 0x321ac
    prev=[0xe91], succ=[]
    =================================
    0x321b2: RETURNPRIVATE ve5darg2, ve77

}

function fallback()() public {
    Begin block 0xeb
    prev=[], succ=[0x495B0xeb]
    =================================
    0xec: vec(0xf6) = CONST 
    0xf0: vf0 = CALLER 
    0xf1: vf1(0x495) = CONST 
    0xf5: JUMP vf1(0x495)

    Begin block 0x495B0xeb
    prev=[0xeb], succ=[0x4b2B0xeb]
    =================================
    0x496S0xeb: v496Veb(0xe) = CONST 
    0x498S0xeb: v498Veb(0x0) = CONST 
    0x49bS0xeb: v49bVeb = SLOAD v496Veb(0xe)
    0x4a0S0xeb: v4a0Veb(0x1) = CONST 
    0x4a2S0xeb: v4a2Veb = ADD v4a0Veb(0x1), v49bVeb
    0x4a6S0xeb: SSTORE v496Veb(0xe), v4a2Veb
    0x4a8S0xeb: v4a8Veb(0x4b2) = CONST 
    0x4adS0xeb: v4adVeb(0xace) = CONST 
    0x4b1S0xeb: CALLPRIVATE v4adVeb(0xace), vf0, v4a8Veb(0x4b2)

    Begin block 0x4b2B0xeb
    prev=[0x495B0xeb], succ=[0xf6]
    =================================
    0x4b4S0xeb: JUMP vec(0xf6)

    Begin block 0xf6
    prev=[0x4b2B0xeb], succ=[]
    =================================
    0xf7: STOP 

}

function setNewWallet(address)() public {
    Begin block 0xf8
    prev=[], succ=[0x100, 0x104]
    =================================
    0xf9: vf9 = CALLVALUE 
    0xfa: vfa = ISZERO vf9
    0xfb: vfb(0x104) = CONST 
    0xff: JUMPI vfb(0x104), vfa

    Begin block 0x100
    prev=[0xf8], succ=[]
    =================================
    0x100: v100(0x0) = CONST 
    0x103: REVERT v100(0x0), v100(0x0)

    Begin block 0x104
    prev=[0xf8], succ=[0x4b5]
    =================================
    0x105: v105(0x132) = CONST 
    0x109: v109(0x4) = CONST 
    0x10d: v10d = CALLDATALOAD v109(0x4)
    0x10e: v10e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x123: v123 = AND v10e(0xffffffffffffffffffffffffffffffffffffffff), v10d
    0x125: v125(0x20) = CONST 
    0x127: v127(0x24) = ADD v125(0x20), v109(0x4)
    0x12d: v12d(0x4b5) = CONST 
    0x131: JUMP v12d(0x4b5)

    Begin block 0x4b5
    prev=[0x104], succ=[0x50d, 0x511]
    =================================
    0x4b6: v4b6(0x0) = CONST 
    0x4ba: v4ba = SLOAD v4b6(0x0)
    0x4bc: v4bc(0x100) = CONST 
    0x4bf: v4bf(0x1) = EXP v4bc(0x100), v4b6(0x0)
    0x4c1: v4c1 = DIV v4ba, v4bf(0x1)
    0x4c2: v4c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4d7: v4d7 = AND v4c2(0xffffffffffffffffffffffffffffffffffffffff), v4c1
    0x4d8: v4d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4ed: v4ed = AND v4d8(0xffffffffffffffffffffffffffffffffffffffff), v4d7
    0x4ee: v4ee = CALLER 
    0x4ef: v4ef(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x504: v504 = AND v4ef(0xffffffffffffffffffffffffffffffffffffffff), v4ee
    0x505: v505 = EQ v504, v4ed
    0x506: v506 = ISZERO v505
    0x507: v507 = ISZERO v506
    0x508: v508(0x511) = CONST 
    0x50c: JUMPI v508(0x511), v507

    Begin block 0x50d
    prev=[0x4b5], succ=[]
    =================================
    0x50d: v50d(0x0) = CONST 
    0x510: REVERT v50d(0x0), v50d(0x0)

    Begin block 0x511
    prev=[0x4b5], succ=[0x534, 0x538]
    =================================
    0x512: v512(0x0) = CONST 
    0x515: v515(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x52a: v52a = AND v515(0xffffffffffffffffffffffffffffffffffffffff), v123
    0x52b: v52b = EQ v52a, v512(0x0)
    0x52c: v52c = ISZERO v52b
    0x52d: v52d = ISZERO v52c
    0x52e: v52e = ISZERO v52d
    0x52f: v52f(0x538) = CONST 
    0x533: JUMPI v52f(0x538), v52e

    Begin block 0x534
    prev=[0x511], succ=[]
    =================================
    0x534: v534(0x0) = CONST 
    0x537: REVERT v534(0x0), v534(0x0)

    Begin block 0x538
    prev=[0x511], succ=[0x132]
    =================================
    0x53a: v53a(0x2) = CONST 
    0x53c: v53c(0x0) = CONST 
    0x53e: v53e(0x100) = CONST 
    0x541: v541(0x1) = EXP v53e(0x100), v53c(0x0)
    0x543: v543 = SLOAD v53a(0x2)
    0x545: v545(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x55a: v55a(0xffffffffffffffffffffffffffffffffffffffff) = MUL v545(0xffffffffffffffffffffffffffffffffffffffff), v541(0x1)
    0x55b: v55b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v55a(0xffffffffffffffffffffffffffffffffffffffff)
    0x55c: v55c = AND v55b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v543
    0x55f: v55f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x574: v574 = AND v55f(0xffffffffffffffffffffffffffffffffffffffff), v123
    0x575: v575 = MUL v574, v541(0x1)
    0x576: v576 = OR v575, v55c
    0x578: SSTORE v53a(0x2), v576
    0x57b: JUMP v105(0x132)

    Begin block 0x132
    prev=[0x538], succ=[]
    =================================
    0x133: STOP 

}

