function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x3416c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x2c96c: v2c96c(0x3416c) = CONST 
    0x2c98c: JUMPI v2c96c(0x3416c), v8

    Begin block 0xd
    prev=[0x0], succ=[0x34b6c, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x2d36c: v2d36c(0x34b6c) = CONST 
    0x2d38c: JUMPI v2d36c(0x34b6c), v3c

    Begin block 0x34b6c
    prev=[0xd], succ=[]
    =================================
    0x34b8c: v34b8c(0xb4) = CONST 
    0x34bac: CALLPRIVATE v34b8c(0xb4)

    Begin block 0x41
    prev=[0xd], succ=[0x3556c, 0x4c]
    =================================
    0x42: v42(0x95ea7b3) = CONST 
    0x47: v47 = EQ v42(0x95ea7b3), v35
    0x2dd6c: v2dd6c(0x3556c) = CONST 
    0x2dd8c: JUMPI v2dd6c(0x3556c), v47

    Begin block 0x3556c
    prev=[0x41], succ=[]
    =================================
    0x3558c: v3558c(0x144) = CONST 
    0x355ac: CALLPRIVATE v3558c(0x144)

    Begin block 0x4c
    prev=[0x41], succ=[0x35f6c, 0x57]
    =================================
    0x4d: v4d(0x18160ddd) = CONST 
    0x52: v52 = EQ v4d(0x18160ddd), v35
    0x2e76c: v2e76c(0x35f6c) = CONST 
    0x2e78c: JUMPI v2e76c(0x35f6c), v52

    Begin block 0x35f6c
    prev=[0x4c], succ=[]
    =================================
    0x35f8c: v35f8c(0x1a9) = CONST 
    0x35fac: CALLPRIVATE v35f8c(0x1a9)

    Begin block 0x57
    prev=[0x4c], succ=[0x3696c, 0x62]
    =================================
    0x58: v58(0x23b872dd) = CONST 
    0x5d: v5d = EQ v58(0x23b872dd), v35
    0x2f16c: v2f16c(0x3696c) = CONST 
    0x2f18c: JUMPI v2f16c(0x3696c), v5d

    Begin block 0x3696c
    prev=[0x57], succ=[]
    =================================
    0x3698c: v3698c(0x1d4) = CONST 
    0x369ac: CALLPRIVATE v3698c(0x1d4)

    Begin block 0x62
    prev=[0x57], succ=[0x3736c, 0x6d]
    =================================
    0x63: v63(0x2ff2e9dc) = CONST 
    0x68: v68 = EQ v63(0x2ff2e9dc), v35
    0x2fb6c: v2fb6c(0x3736c) = CONST 
    0x2fb8c: JUMPI v2fb6c(0x3736c), v68

    Begin block 0x3736c
    prev=[0x62], succ=[]
    =================================
    0x3738c: v3738c(0x259) = CONST 
    0x373ac: CALLPRIVATE v3738c(0x259)

    Begin block 0x6d
    prev=[0x62], succ=[0x37d6c, 0x78]
    =================================
    0x6e: v6e(0x313ce567) = CONST 
    0x73: v73 = EQ v6e(0x313ce567), v35
    0x3056c: v3056c(0x37d6c) = CONST 
    0x3058c: JUMPI v3056c(0x37d6c), v73

    Begin block 0x37d6c
    prev=[0x6d], succ=[]
    =================================
    0x37d8c: v37d8c(0x284) = CONST 
    0x37dac: CALLPRIVATE v37d8c(0x284)

    Begin block 0x78
    prev=[0x6d], succ=[0x3876c, 0x83]
    =================================
    0x79: v79(0x70a08231) = CONST 
    0x7e: v7e = EQ v79(0x70a08231), v35
    0x30f6c: v30f6c(0x3876c) = CONST 
    0x30f8c: JUMPI v30f6c(0x3876c), v7e

    Begin block 0x3876c
    prev=[0x78], succ=[]
    =================================
    0x3878c: v3878c(0x2b5) = CONST 
    0x387ac: CALLPRIVATE v3878c(0x2b5)

    Begin block 0x83
    prev=[0x78], succ=[0x3916c, 0x8e]
    =================================
    0x84: v84(0x95d89b41) = CONST 
    0x89: v89 = EQ v84(0x95d89b41), v35
    0x3196c: v3196c(0x3916c) = CONST 
    0x3198c: JUMPI v3196c(0x3916c), v89

    Begin block 0x3916c
    prev=[0x83], succ=[]
    =================================
    0x3918c: v3918c(0x30c) = CONST 
    0x391ac: CALLPRIVATE v3918c(0x30c)

    Begin block 0x8e
    prev=[0x83], succ=[0x39b6c, 0x99]
    =================================
    0x8f: v8f(0xa9059cbb) = CONST 
    0x94: v94 = EQ v8f(0xa9059cbb), v35
    0x3236c: v3236c(0x39b6c) = CONST 
    0x3238c: JUMPI v3236c(0x39b6c), v94

    Begin block 0x39b6c
    prev=[0x8e], succ=[]
    =================================
    0x39b8c: v39b8c(0x39c) = CONST 
    0x39bac: CALLPRIVATE v39b8c(0x39c)

    Begin block 0x99
    prev=[0x8e], succ=[0x3a56c, 0xa4]
    =================================
    0x9a: v9a(0xcae9ca51) = CONST 
    0x9f: v9f = EQ v9a(0xcae9ca51), v35
    0x32d6c: v32d6c(0x3a56c) = CONST 
    0x32d8c: JUMPI v32d6c(0x3a56c), v9f

    Begin block 0x3a56c
    prev=[0x99], succ=[]
    =================================
    0x3a58c: v3a58c(0x401) = CONST 
    0x3a5ac: CALLPRIVATE v3a58c(0x401)

    Begin block 0xa4
    prev=[0x99], succ=[0x3416c, 0x3af6c]
    =================================
    0xa5: va5(0xdd62ed3e) = CONST 
    0xaa: vaa = EQ va5(0xdd62ed3e), v35
    0x3376c: v3376c(0x3af6c) = CONST 
    0x3378c: JUMPI v3376c(0x3af6c), vaa

    Begin block 0x3416c
    prev=[0x0, 0xa4], succ=[]
    =================================
    0x3418c: v3418c(0xaf) = CONST 
    0x341ac: CALLPRIVATE v3418c(0xaf)

    Begin block 0x3af6c
    prev=[0xa4], succ=[]
    =================================
    0x3af8c: v3af8c(0x4ac) = CONST 
    0x3afac: CALLPRIVATE v3af8c(0x4ac)

}

function 0x126d(v126darg0, v126darg1, v126darg2) private {
    Begin block 0x126d
    prev=[], succ=[0x1280, 0x1281]
    =================================
    0x126e: v126e(0x0) = CONST 
    0x1273: v1273 = ADD v126darg1, v126darg0
    0x1278: v1278 = LT v1273, v126darg1
    0x1279: v1279 = ISZERO v1278
    0x127a: v127a = ISZERO v1279
    0x127b: v127b = ISZERO v127a
    0x127c: v127c(0x1281) = CONST 
    0x127f: JUMPI v127c(0x1281), v127b

    Begin block 0x1280
    prev=[0x126d], succ=[]
    =================================
    0x1280: THROW 

    Begin block 0x1281
    prev=[0x126d], succ=[]
    =================================
    0x128a: RETURNPRIVATE v126darg2, v1273

}

function 0x128b(v128barg0, v128barg1, v128barg2) private {
    Begin block 0x128b
    prev=[], succ=[0x1298, 0x1299]
    =================================
    0x128c: v128c(0x0) = CONST 
    0x1290: v1290 = GT v128barg0, v128barg1
    0x1291: v1291 = ISZERO v1290
    0x1292: v1292 = ISZERO v1291
    0x1293: v1293 = ISZERO v1292
    0x1294: v1294(0x1299) = CONST 
    0x1297: JUMPI v1294(0x1299), v1293

    Begin block 0x1298
    prev=[0x128b], succ=[]
    =================================
    0x1298: THROW 

    Begin block 0x1299
    prev=[0x128b], succ=[]
    =================================
    0x129c: v129c = SUB v128barg1, v128barg0
    0x12a3: RETURNPRIVATE v128barg2, v129c

}

function approve(address,uint256)() public {
    Begin block 0x144
    prev=[], succ=[0x14c, 0x150]
    =================================
    0x145: v145 = CALLVALUE 
    0x147: v147 = ISZERO v145
    0x148: v148(0x150) = CONST 
    0x14b: JUMPI v148(0x150), v147

    Begin block 0x14c
    prev=[0x144], succ=[]
    =================================
    0x14c: v14c(0x0) = CONST 
    0x14f: REVERT v14c(0x0), v14c(0x0)

    Begin block 0x150
    prev=[0x144], succ=[0x5c1]
    =================================
    0x152: v152(0x18f) = CONST 
    0x155: v155(0x4) = CONST 
    0x158: v158 = CALLDATASIZE 
    0x159: v159 = SUB v158, v155(0x4)
    0x15b: v15b = ADD v155(0x4), v159
    0x15f: v15f = CALLDATALOAD v155(0x4)
    0x160: v160(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x175: v175 = AND v160(0xffffffffffffffffffffffffffffffffffffffff), v15f
    0x177: v177(0x20) = CONST 
    0x179: v179(0x24) = ADD v177(0x20), v155(0x4)
    0x17f: v17f = CALLDATALOAD v179(0x24)
    0x181: v181(0x20) = CONST 
    0x183: v183(0x44) = ADD v181(0x20), v179(0x24)
    0x18b: v18b(0x5c1) = CONST 
    0x18e: JUMP v18b(0x5c1)

    Begin block 0x5c1
    prev=[0x150], succ=[0x64d, 0x5cc]
    =================================
    0x5c2: v5c2(0x0) = CONST 
    0x5c6: v5c6 = EQ v17f, v5c2(0x0)
    0x5c8: v5c8(0x64d) = CONST 
    0x5cb: JUMPI v5c8(0x64d), v5c6

    Begin block 0x64d
    prev=[0x5c1, 0x5cc], succ=[0x654, 0x658]
    =================================
    0x64d_0x0: v64d_0 = PHI v5c6, v64c
    0x64e: v64e = ISZERO v64d_0
    0x64f: v64f = ISZERO v64e
    0x650: v650(0x658) = CONST 
    0x653: JUMPI v650(0x658), v64f

    Begin block 0x654
    prev=[0x64d], succ=[]
    =================================
    0x654: v654(0x0) = CONST 
    0x657: REVERT v654(0x0), v654(0x0)

    Begin block 0x658
    prev=[0x64d], succ=[0x18f]
    =================================
    0x65a: v65a(0x2) = CONST 
    0x65c: v65c(0x0) = CONST 
    0x65e: v65e = CALLER 
    0x65f: v65f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x674: v674 = AND v65f(0xffffffffffffffffffffffffffffffffffffffff), v65e
    0x675: v675(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68a: v68a = AND v675(0xffffffffffffffffffffffffffffffffffffffff), v674
    0x68c: MSTORE v65c(0x0), v68a
    0x68d: v68d(0x20) = CONST 
    0x68f: v68f(0x20) = ADD v68d(0x20), v65c(0x0)
    0x692: MSTORE v68f(0x20), v65a(0x2)
    0x693: v693(0x20) = CONST 
    0x695: v695(0x40) = ADD v693(0x20), v68f(0x20)
    0x696: v696(0x0) = CONST 
    0x698: v698 = SHA3 v696(0x0), v695(0x40)
    0x699: v699(0x0) = CONST 
    0x69c: v69c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6b1: v6b1 = AND v69c(0xffffffffffffffffffffffffffffffffffffffff), v175
    0x6b2: v6b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6c7: v6c7 = AND v6b2(0xffffffffffffffffffffffffffffffffffffffff), v6b1
    0x6c9: MSTORE v699(0x0), v6c7
    0x6ca: v6ca(0x20) = CONST 
    0x6cc: v6cc(0x20) = ADD v6ca(0x20), v699(0x0)
    0x6cf: MSTORE v6cc(0x20), v698
    0x6d0: v6d0(0x20) = CONST 
    0x6d2: v6d2(0x40) = ADD v6d0(0x20), v6cc(0x20)
    0x6d3: v6d3(0x0) = CONST 
    0x6d5: v6d5 = SHA3 v6d3(0x0), v6d2(0x40)
    0x6d8: SSTORE v6d5, v17f
    0x6db: v6db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6f0: v6f0 = AND v6db(0xffffffffffffffffffffffffffffffffffffffff), v175
    0x6f1: v6f1 = CALLER 
    0x6f2: v6f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x707: v707 = AND v6f2(0xffffffffffffffffffffffffffffffffffffffff), v6f1
    0x708: v708(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x72a: v72a(0x40) = CONST 
    0x72c: v72c = MLOAD v72a(0x40)
    0x730: MSTORE v72c, v17f
    0x731: v731(0x20) = CONST 
    0x733: v733 = ADD v731(0x20), v72c
    0x737: v737(0x40) = CONST 
    0x739: v739 = MLOAD v737(0x40)
    0x73c: v73c(0x20) = SUB v733, v739
    0x73e: LOG3 v739, v73c(0x20), v708(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v707, v6f0
    0x73f: v73f(0x1) = CONST 
    0x747: JUMP v152(0x18f)

    Begin block 0x18f
    prev=[0x658], succ=[]
    =================================
    0x190: v190(0x40) = CONST 
    0x192: v192 = MLOAD v190(0x40)
    0x195: v195(0x0) = ISZERO v73f(0x1)
    0x196: v196(0x1) = ISZERO v195(0x0)
    0x197: v197(0x0) = ISZERO v196(0x1)
    0x198: v198(0x1) = ISZERO v197(0x0)
    0x19a: MSTORE v192, v198(0x1)
    0x19b: v19b(0x20) = CONST 
    0x19d: v19d = ADD v19b(0x20), v192
    0x1a1: v1a1(0x40) = CONST 
    0x1a3: v1a3 = MLOAD v1a1(0x40)
    0x1a6: v1a6(0x20) = SUB v19d, v1a3
    0x1a8: RETURN v1a3, v1a6(0x20)

    Begin block 0x5cc
    prev=[0x5c1], succ=[0x64d]
    =================================
    0x5cd: v5cd(0x0) = CONST 
    0x5cf: v5cf(0x2) = CONST 
    0x5d1: v5d1(0x0) = CONST 
    0x5d3: v5d3 = CALLER 
    0x5d4: v5d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5e9: v5e9 = AND v5d4(0xffffffffffffffffffffffffffffffffffffffff), v5d3
    0x5ea: v5ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ff: v5ff = AND v5ea(0xffffffffffffffffffffffffffffffffffffffff), v5e9
    0x601: MSTORE v5d1(0x0), v5ff
    0x602: v602(0x20) = CONST 
    0x604: v604(0x20) = ADD v602(0x20), v5d1(0x0)
    0x607: MSTORE v604(0x20), v5cf(0x2)
    0x608: v608(0x20) = CONST 
    0x60a: v60a(0x40) = ADD v608(0x20), v604(0x20)
    0x60b: v60b(0x0) = CONST 
    0x60d: v60d = SHA3 v60b(0x0), v60a(0x40)
    0x60e: v60e(0x0) = CONST 
    0x611: v611(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x626: v626 = AND v611(0xffffffffffffffffffffffffffffffffffffffff), v175
    0x627: v627(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x63c: v63c = AND v627(0xffffffffffffffffffffffffffffffffffffffff), v626
    0x63e: MSTORE v60e(0x0), v63c
    0x63f: v63f(0x20) = CONST 
    0x641: v641(0x20) = ADD v63f(0x20), v60e(0x0)
    0x644: MSTORE v641(0x20), v60d
    0x645: v645(0x20) = CONST 
    0x647: v647(0x40) = ADD v645(0x20), v641(0x20)
    0x648: v648(0x0) = CONST 
    0x64a: v64a = SHA3 v648(0x0), v647(0x40)
    0x64b: v64b = SLOAD v64a
    0x64c: v64c = EQ v64b, v5cd(0x0)
    0x61be: v61be(0x64d) = CONST 
    0x61de: JUMP v61be(0x64d)

}

function totalSupply()() public {
    Begin block 0x1a9
    prev=[], succ=[0x1b1, 0x1b5]
    =================================
    0x1aa: v1aa = CALLVALUE 
    0x1ac: v1ac = ISZERO v1aa
    0x1ad: v1ad(0x1b5) = CONST 
    0x1b0: JUMPI v1ad(0x1b5), v1ac

    Begin block 0x1b1
    prev=[0x1a9], succ=[]
    =================================
    0x1b1: v1b1(0x0) = CONST 
    0x1b4: REVERT v1b1(0x0), v1b1(0x0)

    Begin block 0x1b5
    prev=[0x1a9], succ=[0x748]
    =================================
    0x1b7: v1b7(0x1be) = CONST 
    0x1ba: v1ba(0x748) = CONST 
    0x1bd: JUMP v1ba(0x748)

    Begin block 0x748
    prev=[0x1b5], succ=[0x1be]
    =================================
    0x749: v749(0x0) = CONST 
    0x74b: v74b = SLOAD v749(0x0)
    0x74d: JUMP v1b7(0x1be)

    Begin block 0x1be
    prev=[0x748], succ=[]
    =================================
    0x1bf: v1bf(0x40) = CONST 
    0x1c1: v1c1 = MLOAD v1bf(0x40)
    0x1c5: MSTORE v1c1, v74b
    0x1c6: v1c6(0x20) = CONST 
    0x1c8: v1c8 = ADD v1c6(0x20), v1c1
    0x1cc: v1cc(0x40) = CONST 
    0x1ce: v1ce = MLOAD v1cc(0x40)
    0x1d1: v1d1(0x20) = SUB v1c8, v1ce
    0x1d3: RETURN v1ce, v1d1(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x1d4
    prev=[], succ=[0x1dc, 0x1e0]
    =================================
    0x1d5: v1d5 = CALLVALUE 
    0x1d7: v1d7 = ISZERO v1d5
    0x1d8: v1d8(0x1e0) = CONST 
    0x1db: JUMPI v1d8(0x1e0), v1d7

    Begin block 0x1dc
    prev=[0x1d4], succ=[]
    =================================
    0x1dc: v1dc(0x0) = CONST 
    0x1df: REVERT v1dc(0x0), v1dc(0x0)

    Begin block 0x1e0
    prev=[0x1d4], succ=[0x74e]
    =================================
    0x1e2: v1e2(0x23f) = CONST 
    0x1e5: v1e5(0x4) = CONST 
    0x1e8: v1e8 = CALLDATASIZE 
    0x1e9: v1e9 = SUB v1e8, v1e5(0x4)
    0x1eb: v1eb = ADD v1e5(0x4), v1e9
    0x1ef: v1ef = CALLDATALOAD v1e5(0x4)
    0x1f0: v1f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x205: v205 = AND v1f0(0xffffffffffffffffffffffffffffffffffffffff), v1ef
    0x207: v207(0x20) = CONST 
    0x209: v209(0x24) = ADD v207(0x20), v1e5(0x4)
    0x20f: v20f = CALLDATALOAD v209(0x24)
    0x210: v210(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x225: v225 = AND v210(0xffffffffffffffffffffffffffffffffffffffff), v20f
    0x227: v227(0x20) = CONST 
    0x229: v229(0x44) = ADD v227(0x20), v209(0x24)
    0x22f: v22f = CALLDATALOAD v229(0x44)
    0x231: v231(0x20) = CONST 
    0x233: v233(0x64) = ADD v231(0x20), v229(0x44)
    0x23b: v23b(0x74e) = CONST 
    0x23e: JUMP v23b(0x74e)

    Begin block 0x74e
    prev=[0x1e0], succ=[0x787, 0x78b]
    =================================
    0x74f: v74f(0x0) = CONST 
    0x752: v752(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x767: v767(0x0) = AND v752(0xffffffffffffffffffffffffffffffffffffffff), v74f(0x0)
    0x769: v769(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x77e: v77e = AND v769(0xffffffffffffffffffffffffffffffffffffffff), v225
    0x77f: v77f = EQ v77e, v767(0x0)
    0x780: v780 = ISZERO v77f
    0x781: v781 = ISZERO v780
    0x782: v782 = ISZERO v781
    0x783: v783(0x78b) = CONST 
    0x786: JUMPI v783(0x78b), v782

    Begin block 0x787
    prev=[0x74e], succ=[]
    =================================
    0x787: v787(0x0) = CONST 
    0x78a: REVERT v787(0x0), v787(0x0)

    Begin block 0x78b
    prev=[0x74e], succ=[0x856, 0x7d5]
    =================================
    0x78d: v78d(0x1) = CONST 
    0x78f: v78f(0x0) = CONST 
    0x792: v792(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7a7: v7a7 = AND v792(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x7a8: v7a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7bd: v7bd = AND v7a8(0xffffffffffffffffffffffffffffffffffffffff), v7a7
    0x7bf: MSTORE v78f(0x0), v7bd
    0x7c0: v7c0(0x20) = CONST 
    0x7c2: v7c2(0x20) = ADD v7c0(0x20), v78f(0x0)
    0x7c5: MSTORE v7c2(0x20), v78d(0x1)
    0x7c6: v7c6(0x20) = CONST 
    0x7c8: v7c8(0x40) = ADD v7c6(0x20), v7c2(0x20)
    0x7c9: v7c9(0x0) = CONST 
    0x7cb: v7cb = SHA3 v7c9(0x0), v7c8(0x40)
    0x7cc: v7cc = SLOAD v7cb
    0x7cd: v7cd = LT v7cc, v22f
    0x7ce: v7ce = ISZERO v7cd
    0x7d0: v7d0 = ISZERO v7ce
    0x7d1: v7d1(0x856) = CONST 
    0x7d4: JUMPI v7d1(0x856), v7d0

    Begin block 0x856
    prev=[0x78b, 0x7d5], succ=[0x85d, 0x861]
    =================================
    0x856_0x0: v856_0 = PHI v7ce, v855
    0x857: v857 = ISZERO v856_0
    0x858: v858 = ISZERO v857
    0x859: v859(0x861) = CONST 
    0x85c: JUMPI v859(0x861), v858

    Begin block 0x85d
    prev=[0x856], succ=[]
    =================================
    0x85d: v85d(0x0) = CONST 
    0x860: REVERT v85d(0x0), v85d(0x0)

    Begin block 0x861
    prev=[0x856], succ=[0x8b3]
    =================================
    0x862: v862(0x8b3) = CONST 
    0x866: v866(0x1) = CONST 
    0x868: v868(0x0) = CONST 
    0x86b: v86b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x880: v880 = AND v86b(0xffffffffffffffffffffffffffffffffffffffff), v225
    0x881: v881(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x896: v896 = AND v881(0xffffffffffffffffffffffffffffffffffffffff), v880
    0x898: MSTORE v868(0x0), v896
    0x899: v899(0x20) = CONST 
    0x89b: v89b(0x20) = ADD v899(0x20), v868(0x0)
    0x89e: MSTORE v89b(0x20), v866(0x1)
    0x89f: v89f(0x20) = CONST 
    0x8a1: v8a1(0x40) = ADD v89f(0x20), v89b(0x20)
    0x8a2: v8a2(0x0) = CONST 
    0x8a4: v8a4 = SHA3 v8a2(0x0), v8a1(0x40)
    0x8a5: v8a5 = SLOAD v8a4
    0x8a6: v8a6(0x126d) = CONST 
    0x8ac: v8ac(0xffffffff) = CONST 
    0x8b1: v8b1(0x126d) = AND v8ac(0xffffffff), v8a6(0x126d)
    0x8b2: v8b2_0 = CALLPRIVATE v8b1(0x126d), v22f, v8a5, v862(0x8b3)

    Begin block 0x8b3
    prev=[0x861], succ=[0x948]
    =================================
    0x8b4: v8b4(0x1) = CONST 
    0x8b6: v8b6(0x0) = CONST 
    0x8b9: v8b9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8ce: v8ce = AND v8b9(0xffffffffffffffffffffffffffffffffffffffff), v225
    0x8cf: v8cf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8e4: v8e4 = AND v8cf(0xffffffffffffffffffffffffffffffffffffffff), v8ce
    0x8e6: MSTORE v8b6(0x0), v8e4
    0x8e7: v8e7(0x20) = CONST 
    0x8e9: v8e9(0x20) = ADD v8e7(0x20), v8b6(0x0)
    0x8ec: MSTORE v8e9(0x20), v8b4(0x1)
    0x8ed: v8ed(0x20) = CONST 
    0x8ef: v8ef(0x40) = ADD v8ed(0x20), v8e9(0x20)
    0x8f0: v8f0(0x0) = CONST 
    0x8f2: v8f2 = SHA3 v8f0(0x0), v8ef(0x40)
    0x8f5: SSTORE v8f2, v8b2_0
    0x8f7: v8f7(0x948) = CONST 
    0x8fb: v8fb(0x1) = CONST 
    0x8fd: v8fd(0x0) = CONST 
    0x900: v900(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x915: v915 = AND v900(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x916: v916(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x92b: v92b = AND v916(0xffffffffffffffffffffffffffffffffffffffff), v915
    0x92d: MSTORE v8fd(0x0), v92b
    0x92e: v92e(0x20) = CONST 
    0x930: v930(0x20) = ADD v92e(0x20), v8fd(0x0)
    0x933: MSTORE v930(0x20), v8fb(0x1)
    0x934: v934(0x20) = CONST 
    0x936: v936(0x40) = ADD v934(0x20), v930(0x20)
    0x937: v937(0x0) = CONST 
    0x939: v939 = SHA3 v937(0x0), v936(0x40)
    0x93a: v93a = SLOAD v939
    0x93b: v93b(0x128b) = CONST 
    0x941: v941(0xffffffff) = CONST 
    0x946: v946(0x128b) = AND v941(0xffffffff), v93b(0x128b)
    0x947: v947_0 = CALLPRIVATE v946(0x128b), v22f, v93a, v8f7(0x948)

    Begin block 0x948
    prev=[0x8b3], succ=[0xa1a]
    =================================
    0x949: v949(0x1) = CONST 
    0x94b: v94b(0x0) = CONST 
    0x94e: v94e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x963: v963 = AND v94e(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x964: v964(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x979: v979 = AND v964(0xffffffffffffffffffffffffffffffffffffffff), v963
    0x97b: MSTORE v94b(0x0), v979
    0x97c: v97c(0x20) = CONST 
    0x97e: v97e(0x20) = ADD v97c(0x20), v94b(0x0)
    0x981: MSTORE v97e(0x20), v949(0x1)
    0x982: v982(0x20) = CONST 
    0x984: v984(0x40) = ADD v982(0x20), v97e(0x20)
    0x985: v985(0x0) = CONST 
    0x987: v987 = SHA3 v985(0x0), v984(0x40)
    0x98a: SSTORE v987, v947_0
    0x98c: v98c(0xa1a) = CONST 
    0x990: v990(0x2) = CONST 
    0x992: v992(0x0) = CONST 
    0x995: v995(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9aa: v9aa = AND v995(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x9ab: v9ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9c0: v9c0 = AND v9ab(0xffffffffffffffffffffffffffffffffffffffff), v9aa
    0x9c2: MSTORE v992(0x0), v9c0
    0x9c3: v9c3(0x20) = CONST 
    0x9c5: v9c5(0x20) = ADD v9c3(0x20), v992(0x0)
    0x9c8: MSTORE v9c5(0x20), v990(0x2)
    0x9c9: v9c9(0x20) = CONST 
    0x9cb: v9cb(0x40) = ADD v9c9(0x20), v9c5(0x20)
    0x9cc: v9cc(0x0) = CONST 
    0x9ce: v9ce = SHA3 v9cc(0x0), v9cb(0x40)
    0x9cf: v9cf(0x0) = CONST 
    0x9d1: v9d1 = CALLER 
    0x9d2: v9d2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9e7: v9e7 = AND v9d2(0xffffffffffffffffffffffffffffffffffffffff), v9d1
    0x9e8: v9e8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9fd: v9fd = AND v9e8(0xffffffffffffffffffffffffffffffffffffffff), v9e7
    0x9ff: MSTORE v9cf(0x0), v9fd
    0xa00: va00(0x20) = CONST 
    0xa02: va02(0x20) = ADD va00(0x20), v9cf(0x0)
    0xa05: MSTORE va02(0x20), v9ce
    0xa06: va06(0x20) = CONST 
    0xa08: va08(0x40) = ADD va06(0x20), va02(0x20)
    0xa09: va09(0x0) = CONST 
    0xa0b: va0b = SHA3 va09(0x0), va08(0x40)
    0xa0c: va0c = SLOAD va0b
    0xa0d: va0d(0x128b) = CONST 
    0xa13: va13(0xffffffff) = CONST 
    0xa18: va18(0x128b) = AND va13(0xffffffff), va0d(0x128b)
    0xa19: va19_0 = CALLPRIVATE va18(0x128b), v22f, va0c, v98c(0xa1a)

    Begin block 0xa1a
    prev=[0x948], succ=[0x23f]
    =================================
    0xa1b: va1b(0x2) = CONST 
    0xa1d: va1d(0x0) = CONST 
    0xa20: va20(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa35: va35 = AND va20(0xffffffffffffffffffffffffffffffffffffffff), v205
    0xa36: va36(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa4b: va4b = AND va36(0xffffffffffffffffffffffffffffffffffffffff), va35
    0xa4d: MSTORE va1d(0x0), va4b
    0xa4e: va4e(0x20) = CONST 
    0xa50: va50(0x20) = ADD va4e(0x20), va1d(0x0)
    0xa53: MSTORE va50(0x20), va1b(0x2)
    0xa54: va54(0x20) = CONST 
    0xa56: va56(0x40) = ADD va54(0x20), va50(0x20)
    0xa57: va57(0x0) = CONST 
    0xa59: va59 = SHA3 va57(0x0), va56(0x40)
    0xa5a: va5a(0x0) = CONST 
    0xa5c: va5c = CALLER 
    0xa5d: va5d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa72: va72 = AND va5d(0xffffffffffffffffffffffffffffffffffffffff), va5c
    0xa73: va73(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa88: va88 = AND va73(0xffffffffffffffffffffffffffffffffffffffff), va72
    0xa8a: MSTORE va5a(0x0), va88
    0xa8b: va8b(0x20) = CONST 
    0xa8d: va8d(0x20) = ADD va8b(0x20), va5a(0x0)
    0xa90: MSTORE va8d(0x20), va59
    0xa91: va91(0x20) = CONST 
    0xa93: va93(0x40) = ADD va91(0x20), va8d(0x20)
    0xa94: va94(0x0) = CONST 
    0xa96: va96 = SHA3 va94(0x0), va93(0x40)
    0xa99: SSTORE va96, va19_0
    0xa9c: va9c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xab1: vab1 = AND va9c(0xffffffffffffffffffffffffffffffffffffffff), v225
    0xab3: vab3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xac8: vac8 = AND vab3(0xffffffffffffffffffffffffffffffffffffffff), v205
    0xac9: vac9(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xaeb: vaeb(0x40) = CONST 
    0xaed: vaed = MLOAD vaeb(0x40)
    0xaf1: MSTORE vaed, v22f
    0xaf2: vaf2(0x20) = CONST 
    0xaf4: vaf4 = ADD vaf2(0x20), vaed
    0xaf8: vaf8(0x40) = CONST 
    0xafa: vafa = MLOAD vaf8(0x40)
    0xafd: vafd(0x20) = SUB vaf4, vafa
    0xaff: LOG3 vafa, vafd(0x20), vac9(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vac8, vab1
    0xb00: vb00(0x1) = CONST 
    0xb09: JUMP v1e2(0x23f)

    Begin block 0x23f
    prev=[0xa1a], succ=[]
    =================================
    0x240: v240(0x40) = CONST 
    0x242: v242 = MLOAD v240(0x40)
    0x245: v245(0x0) = ISZERO vb00(0x1)
    0x246: v246(0x1) = ISZERO v245(0x0)
    0x247: v247(0x0) = ISZERO v246(0x1)
    0x248: v248(0x1) = ISZERO v247(0x0)
    0x24a: MSTORE v242, v248(0x1)
    0x24b: v24b(0x20) = CONST 
    0x24d: v24d = ADD v24b(0x20), v242
    0x251: v251(0x40) = CONST 
    0x253: v253 = MLOAD v251(0x40)
    0x256: v256(0x20) = SUB v24d, v253
    0x258: RETURN v253, v256(0x20)

    Begin block 0x7d5
    prev=[0x78b], succ=[0x856]
    =================================
    0x7d7: v7d7(0x2) = CONST 
    0x7d9: v7d9(0x0) = CONST 
    0x7dc: v7dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7f1: v7f1 = AND v7dc(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x7f2: v7f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x807: v807 = AND v7f2(0xffffffffffffffffffffffffffffffffffffffff), v7f1
    0x809: MSTORE v7d9(0x0), v807
    0x80a: v80a(0x20) = CONST 
    0x80c: v80c(0x20) = ADD v80a(0x20), v7d9(0x0)
    0x80f: MSTORE v80c(0x20), v7d7(0x2)
    0x810: v810(0x20) = CONST 
    0x812: v812(0x40) = ADD v810(0x20), v80c(0x20)
    0x813: v813(0x0) = CONST 
    0x815: v815 = SHA3 v813(0x0), v812(0x40)
    0x816: v816(0x0) = CONST 
    0x818: v818 = CALLER 
    0x819: v819(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x82e: v82e = AND v819(0xffffffffffffffffffffffffffffffffffffffff), v818
    0x82f: v82f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x844: v844 = AND v82f(0xffffffffffffffffffffffffffffffffffffffff), v82e
    0x846: MSTORE v816(0x0), v844
    0x847: v847(0x20) = CONST 
    0x849: v849(0x20) = ADD v847(0x20), v816(0x0)
    0x84c: MSTORE v849(0x20), v815
    0x84d: v84d(0x20) = CONST 
    0x84f: v84f(0x40) = ADD v84d(0x20), v849(0x20)
    0x850: v850(0x0) = CONST 
    0x852: v852 = SHA3 v850(0x0), v84f(0x40)
    0x853: v853 = SLOAD v852
    0x854: v854 = LT v853, v22f
    0x855: v855 = ISZERO v854
    0x6bbe: v6bbe(0x856) = CONST 
    0x6bde: JUMP v6bbe(0x856)

}

function INITIAL_SUPPLY()() public {
    Begin block 0x259
    prev=[], succ=[0x261, 0x265]
    =================================
    0x25a: v25a = CALLVALUE 
    0x25c: v25c = ISZERO v25a
    0x25d: v25d(0x265) = CONST 
    0x260: JUMPI v25d(0x265), v25c

    Begin block 0x261
    prev=[0x259], succ=[]
    =================================
    0x261: v261(0x0) = CONST 
    0x264: REVERT v261(0x0), v261(0x0)

    Begin block 0x265
    prev=[0x259], succ=[0xb0a]
    =================================
    0x267: v267(0x26e) = CONST 
    0x26a: v26a(0xb0a) = CONST 
    0x26d: JUMP v26a(0xb0a)

    Begin block 0xb0a
    prev=[0x265], succ=[0x26e]
    =================================
    0xb0b: vb0b(0x6) = CONST 
    0xb0d: vb0d = SLOAD vb0b(0x6)
    0xb0f: JUMP v267(0x26e)

    Begin block 0x26e
    prev=[0xb0a], succ=[]
    =================================
    0x26f: v26f(0x40) = CONST 
    0x271: v271 = MLOAD v26f(0x40)
    0x275: MSTORE v271, vb0d
    0x276: v276(0x20) = CONST 
    0x278: v278 = ADD v276(0x20), v271
    0x27c: v27c(0x40) = CONST 
    0x27e: v27e = MLOAD v27c(0x40)
    0x281: v281(0x20) = SUB v278, v27e
    0x283: RETURN v27e, v281(0x20)

}

function decimals()() public {
    Begin block 0x284
    prev=[], succ=[0x28c, 0x290]
    =================================
    0x285: v285 = CALLVALUE 
    0x287: v287 = ISZERO v285
    0x288: v288(0x290) = CONST 
    0x28b: JUMPI v288(0x290), v287

    Begin block 0x28c
    prev=[0x284], succ=[]
    =================================
    0x28c: v28c(0x0) = CONST 
    0x28f: REVERT v28c(0x0), v28c(0x0)

    Begin block 0x290
    prev=[0x284], succ=[0xb10]
    =================================
    0x292: v292(0x299) = CONST 
    0x295: v295(0xb10) = CONST 
    0x298: JUMP v295(0xb10)

    Begin block 0xb10
    prev=[0x290], succ=[0x299]
    =================================
    0xb11: vb11(0x5) = CONST 
    0xb13: vb13(0x0) = CONST 
    0xb16: vb16 = SLOAD vb11(0x5)
    0xb18: vb18(0x100) = CONST 
    0xb1b: vb1b(0x1) = EXP vb18(0x100), vb13(0x0)
    0xb1d: vb1d = DIV vb16, vb1b(0x1)
    0xb1e: vb1e(0xff) = CONST 
    0xb20: vb20 = AND vb1e(0xff), vb1d
    0xb22: JUMP v292(0x299)

    Begin block 0x299
    prev=[0xb10], succ=[]
    =================================
    0x29a: v29a(0x40) = CONST 
    0x29c: v29c = MLOAD v29a(0x40)
    0x29f: v29f(0xff) = CONST 
    0x2a1: v2a1 = AND v29f(0xff), vb20
    0x2a2: v2a2(0xff) = CONST 
    0x2a4: v2a4 = AND v2a2(0xff), v2a1
    0x2a6: MSTORE v29c, v2a4
    0x2a7: v2a7(0x20) = CONST 
    0x2a9: v2a9 = ADD v2a7(0x20), v29c
    0x2ad: v2ad(0x40) = CONST 
    0x2af: v2af = MLOAD v2ad(0x40)
    0x2b2: v2b2(0x20) = SUB v2a9, v2af
    0x2b4: RETURN v2af, v2b2(0x20)

}

function balanceOf(address)() public {
    Begin block 0x2b5
    prev=[], succ=[0x2bd, 0x2c1]
    =================================
    0x2b6: v2b6 = CALLVALUE 
    0x2b8: v2b8 = ISZERO v2b6
    0x2b9: v2b9(0x2c1) = CONST 
    0x2bc: JUMPI v2b9(0x2c1), v2b8

    Begin block 0x2bd
    prev=[0x2b5], succ=[]
    =================================
    0x2bd: v2bd(0x0) = CONST 
    0x2c0: REVERT v2bd(0x0), v2bd(0x0)

    Begin block 0x2c1
    prev=[0x2b5], succ=[0xb23]
    =================================
    0x2c3: v2c3(0x2f6) = CONST 
    0x2c6: v2c6(0x4) = CONST 
    0x2c9: v2c9 = CALLDATASIZE 
    0x2ca: v2ca = SUB v2c9, v2c6(0x4)
    0x2cc: v2cc = ADD v2c6(0x4), v2ca
    0x2d0: v2d0 = CALLDATALOAD v2c6(0x4)
    0x2d1: v2d1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e6: v2e6 = AND v2d1(0xffffffffffffffffffffffffffffffffffffffff), v2d0
    0x2e8: v2e8(0x20) = CONST 
    0x2ea: v2ea(0x24) = ADD v2e8(0x20), v2c6(0x4)
    0x2f2: v2f2(0xb23) = CONST 
    0x2f5: JUMP v2f2(0xb23)

    Begin block 0xb23
    prev=[0x2c1], succ=[0x2f6]
    =================================
    0xb24: vb24(0x0) = CONST 
    0xb26: vb26(0x1) = CONST 
    0xb28: vb28(0x0) = CONST 
    0xb2b: vb2b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb40: vb40 = AND vb2b(0xffffffffffffffffffffffffffffffffffffffff), v2e6
    0xb41: vb41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb56: vb56 = AND vb41(0xffffffffffffffffffffffffffffffffffffffff), vb40
    0xb58: MSTORE vb28(0x0), vb56
    0xb59: vb59(0x20) = CONST 
    0xb5b: vb5b(0x20) = ADD vb59(0x20), vb28(0x0)
    0xb5e: MSTORE vb5b(0x20), vb26(0x1)
    0xb5f: vb5f(0x20) = CONST 
    0xb61: vb61(0x40) = ADD vb5f(0x20), vb5b(0x20)
    0xb62: vb62(0x0) = CONST 
    0xb64: vb64 = SHA3 vb62(0x0), vb61(0x40)
    0xb65: vb65 = SLOAD vb64
    0xb6b: JUMP v2c3(0x2f6)

    Begin block 0x2f6
    prev=[0xb23], succ=[]
    =================================
    0x2f7: v2f7(0x40) = CONST 
    0x2f9: v2f9 = MLOAD v2f7(0x40)
    0x2fd: MSTORE v2f9, vb65
    0x2fe: v2fe(0x20) = CONST 
    0x300: v300 = ADD v2fe(0x20), v2f9
    0x304: v304(0x40) = CONST 
    0x306: v306 = MLOAD v304(0x40)
    0x309: v309(0x20) = SUB v300, v306
    0x30b: RETURN v306, v309(0x20)

}

function symbol()() public {
    Begin block 0x30c
    prev=[], succ=[0x314, 0x318]
    =================================
    0x30d: v30d = CALLVALUE 
    0x30f: v30f = ISZERO v30d
    0x310: v310(0x318) = CONST 
    0x313: JUMPI v310(0x318), v30f

    Begin block 0x314
    prev=[0x30c], succ=[]
    =================================
    0x314: v314(0x0) = CONST 
    0x317: REVERT v314(0x0), v314(0x0)

    Begin block 0x318
    prev=[0x30c], succ=[0xb6cB0x318]
    =================================
    0x31a: v31a(0x321) = CONST 
    0x31d: v31d(0xb6c) = CONST 
    0x320: JUMP v31d(0xb6c)

    Begin block 0xb6cB0x318
    prev=[0x318], succ=[0xbbcB0x318, 0x1642aB0x318]
    =================================
    0xb6dS0x318: vb6dV318(0x4) = CONST 
    0xb70S0x318: vb70V318 = SLOAD vb6dV318(0x4)
    0xb71S0x318: vb71V318(0x1) = CONST 
    0xb74S0x318: vb74V318(0x1) = CONST 
    0xb76S0x318: vb76V318 = AND vb74V318(0x1), vb70V318
    0xb77S0x318: vb77V318 = ISZERO vb76V318
    0xb78S0x318: vb78V318(0x100) = CONST 
    0xb7bS0x318: vb7bV318 = MUL vb78V318(0x100), vb77V318
    0xb7cS0x318: vb7cV318 = SUB vb7bV318, vb71V318(0x1)
    0xb7dS0x318: vb7dV318 = AND vb7cV318, vb70V318
    0xb7eS0x318: vb7eV318(0x2) = CONST 
    0xb81S0x318: vb81V318 = DIV vb7dV318, vb7eV318(0x2)
    0xb83S0x318: vb83V318(0x1f) = CONST 
    0xb85S0x318: vb85V318 = ADD vb83V318(0x1f), vb81V318
    0xb86S0x318: vb86V318(0x20) = CONST 
    0xb8aS0x318: vb8aV318 = DIV vb85V318, vb86V318(0x20)
    0xb8bS0x318: vb8bV318 = MUL vb8aV318, vb86V318(0x20)
    0xb8cS0x318: vb8cV318(0x20) = CONST 
    0xb8eS0x318: vb8eV318 = ADD vb8cV318(0x20), vb8bV318
    0xb8fS0x318: vb8fV318(0x40) = CONST 
    0xb91S0x318: vb91V318 = MLOAD vb8fV318(0x40)
    0xb94S0x318: vb94V318 = ADD vb91V318, vb8eV318
    0xb95S0x318: vb95V318(0x40) = CONST 
    0xb97S0x318: MSTORE vb95V318(0x40), vb94V318
    0xb9eS0x318: MSTORE vb91V318, vb81V318
    0xb9fS0x318: vb9fV318(0x20) = CONST 
    0xba1S0x318: vba1V318 = ADD vb9fV318(0x20), vb91V318
    0xba4S0x318: vba4V318 = SLOAD vb6dV318(0x4)
    0xba5S0x318: vba5V318(0x1) = CONST 
    0xba8S0x318: vba8V318(0x1) = CONST 
    0xbaaS0x318: vbaaV318 = AND vba8V318(0x1), vba4V318
    0xbabS0x318: vbabV318 = ISZERO vbaaV318
    0xbacS0x318: vbacV318(0x100) = CONST 
    0xbafS0x318: vbafV318 = MUL vbacV318(0x100), vbabV318
    0xbb0S0x318: vbb0V318 = SUB vbafV318, vba5V318(0x1)
    0xbb1S0x318: vbb1V318 = AND vbb0V318, vba4V318
    0xbb2S0x318: vbb2V318(0x2) = CONST 
    0xbb5S0x318: vbb5V318 = DIV vbb1V318, vbb2V318(0x2)
    0xbb7S0x318: vbb7V318 = ISZERO vbb5V318
    0xbb8S0x318: vbb8V318(0x1642a) = CONST 
    0xbbbS0x318: JUMPI vbb8V318(0x1642a), vbb7V318

    Begin block 0xbbcB0x318
    prev=[0xb6cB0x318], succ=[0xbc4B0x318, 0xbd7B0x318]
    =================================
    0xbbdS0x318: vbbdV318(0x1f) = CONST 
    0xbbfS0x318: vbbfV318 = LT vbbdV318(0x1f), vbb5V318
    0xbc0S0x318: vbc0V318(0xbd7) = CONST 
    0xbc3S0x318: JUMPI vbc0V318(0xbd7), vbbfV318

    Begin block 0xbc4B0x318
    prev=[0xbbcB0x318], succ=[0x16451B0x318]
    =================================
    0xbc4S0x318: vbc4V318(0x100) = CONST 
    0xbc9S0x318: vbc9V318 = SLOAD vb6dV318(0x4)
    0xbcaS0x318: vbcaV318 = DIV vbc9V318, vbc4V318(0x100)
    0xbcbS0x318: vbcbV318 = MUL vbcaV318, vbc4V318(0x100)
    0xbcdS0x318: MSTORE vba1V318, vbcbV318
    0xbcfS0x318: vbcfV318(0x20) = CONST 
    0xbd1S0x318: vbd1V318 = ADD vbcfV318(0x20), vba1V318
    0xbd3S0x318: vbd3V318(0x16451) = CONST 
    0xbd6S0x318: JUMP vbd3V318(0x16451)

    Begin block 0x16451B0x318
    prev=[0xbc4B0x318], succ=[0x321]
    =================================
    0x16458S0x318: JUMP v31a(0x321)

    Begin block 0x321
    prev=[0x1642aB0x318, 0x16451B0x318, 0x1649fB0x318], succ=[0x346]
    =================================
    0x322: v322(0x40) = CONST 
    0x324: v324 = MLOAD v322(0x40)
    0x327: v327(0x20) = CONST 
    0x329: v329 = ADD v327(0x20), v324
    0x32c: v32c(0x20) = SUB v329, v324
    0x32e: MSTORE v324, v32c(0x20)
    0x332: v332 = MLOAD vb91V318
    0x334: MSTORE v329, v332
    0x335: v335(0x20) = CONST 
    0x337: v337 = ADD v335(0x20), v329
    0x33b: v33b = MLOAD vb91V318
    0x33d: v33d(0x20) = CONST 
    0x33f: v33f = ADD v33d(0x20), vb91V318
    0x344: v344(0x0) = CONST 
    0x39be: v39be(0x346) = CONST 
    0x39de: JUMP v39be(0x346)

    Begin block 0x346
    prev=[0x321, 0x34f], succ=[0x361, 0x34f]
    =================================
    0x346_0x0: v346_0 = PHI v344(0x0), v35a
    0x349: v349 = LT v346_0, v33b
    0x34a: v34a = ISZERO v349
    0x34b: v34b(0x361) = CONST 
    0x34e: JUMPI v34b(0x361), v34a

    Begin block 0x361
    prev=[0x346], succ=[0x38e, 0x375]
    =================================
    0x36a: v36a = ADD v33b, v337
    0x36c: v36c(0x1f) = CONST 
    0x36e: v36e = AND v36c(0x1f), v33b
    0x370: v370 = ISZERO v36e
    0x371: v371(0x38e) = CONST 
    0x374: JUMPI v371(0x38e), v370

    Begin block 0x38e
    prev=[0x361, 0x375], succ=[]
    =================================
    0x38e_0x1: v38e_1 = PHI v36a, v38b
    0x394: v394(0x40) = CONST 
    0x396: v396 = MLOAD v394(0x40)
    0x399: v399 = SUB v38e_1, v396
    0x39b: RETURN v396, v399

    Begin block 0x375
    prev=[0x361], succ=[0x38e]
    =================================
    0x377: v377 = SUB v36a, v36e
    0x379: v379 = MLOAD v377
    0x37a: v37a(0x1) = CONST 
    0x37d: v37d(0x20) = CONST 
    0x37f: v37f = SUB v37d(0x20), v36e
    0x380: v380(0x100) = CONST 
    0x383: v383 = EXP v380(0x100), v37f
    0x384: v384 = SUB v383, v37a(0x1)
    0x385: v385 = NOT v384
    0x386: v386 = AND v385, v379
    0x388: MSTORE v377, v386
    0x389: v389(0x20) = CONST 
    0x38b: v38b = ADD v389(0x20), v377
    0x43be: v43be(0x38e) = CONST 
    0x43de: JUMP v43be(0x38e)

    Begin block 0x34f
    prev=[0x346], succ=[0x346]
    =================================
    0x34f_0x0: v34f_0 = PHI v344(0x0), v35a
    0x351: v351 = ADD v33f, v34f_0
    0x352: v352 = MLOAD v351
    0x355: v355 = ADD v337, v34f_0
    0x356: MSTORE v355, v352
    0x357: v357(0x20) = CONST 
    0x35a: v35a = ADD v34f_0, v357(0x20)
    0x35d: v35d(0x346) = CONST 
    0x360: JUMP v35d(0x346)

    Begin block 0xbd7B0x318
    prev=[0xbbcB0x318], succ=[0xbe5B0x318]
    =================================
    0xbd9S0x318: vbd9V318 = ADD vba1V318, vbb5V318
    0xbdcS0x318: vbdcV318(0x0) = CONST 
    0xbdeS0x318: MSTORE vbdcV318(0x0), vb6dV318(0x4)
    0xbdfS0x318: vbdfV318(0x20) = CONST 
    0xbe1S0x318: vbe1V318(0x0) = CONST 
    0xbe3S0x318: vbe3V318 = SHA3 vbe1V318(0x0), vbdfV318(0x20)
    0x75beS0x318: v75beV318(0xbe5) = CONST 
    0x75deS0x318: JUMP v75beV318(0xbe5)

    Begin block 0xbe5B0x318
    prev=[0xbd7B0x318, 0xbe5B0x318], succ=[0xbe5B0x318, 0xbf9B0x318]
    =================================
    0xbe5_0x0S0x318: vbe5_0V318 = PHI vba1V318, vbf1V318
    0xbe5_0x1S0x318: vbe5_1V318 = PHI vbe3V318, vbedV318
    0xbe7S0x318: vbe7V318 = SLOAD vbe5_1V318
    0xbe9S0x318: MSTORE vbe5_0V318, vbe7V318
    0xbebS0x318: vbebV318(0x1) = CONST 
    0xbedS0x318: vbedV318 = ADD vbebV318(0x1), vbe5_1V318
    0xbefS0x318: vbefV318(0x20) = CONST 
    0xbf1S0x318: vbf1V318 = ADD vbefV318(0x20), vbe5_0V318
    0xbf4S0x318: vbf4V318 = GT vbd9V318, vbf1V318
    0xbf5S0x318: vbf5V318(0xbe5) = CONST 
    0xbf8S0x318: JUMPI vbf5V318(0xbe5), vbf4V318

    Begin block 0xbf9B0x318
    prev=[0xbe5B0x318], succ=[0x1649fB0x318]
    =================================
    0xbfbS0x318: vbfbV318 = SUB vbf1V318, vbd9V318
    0xbfcS0x318: vbfcV318(0x1f) = CONST 
    0xbfeS0x318: vbfeV318 = AND vbfcV318(0x1f), vbfbV318
    0xc00S0x318: vc00V318 = ADD vbd9V318, vbfeV318
    0x7fbeS0x318: v7fbeV318(0x1649f) = CONST 
    0x7fdeS0x318: JUMP v7fbeV318(0x1649f)

    Begin block 0x1649fB0x318
    prev=[0xbf9B0x318], succ=[0x321]
    =================================
    0x164a6S0x318: JUMP v31a(0x321)

    Begin block 0x1642aB0x318
    prev=[0xb6cB0x318], succ=[0x321]
    =================================
    0x16431S0x318: JUMP v31a(0x321)

}

function transfer(address,uint256)() public {
    Begin block 0x39c
    prev=[], succ=[0x3a4, 0x3a8]
    =================================
    0x39d: v39d = CALLVALUE 
    0x39f: v39f = ISZERO v39d
    0x3a0: v3a0(0x3a8) = CONST 
    0x3a3: JUMPI v3a0(0x3a8), v39f

    Begin block 0x3a4
    prev=[0x39c], succ=[]
    =================================
    0x3a4: v3a4(0x0) = CONST 
    0x3a7: REVERT v3a4(0x0), v3a4(0x0)

    Begin block 0x3a8
    prev=[0x39c], succ=[0xc0a]
    =================================
    0x3aa: v3aa(0x3e7) = CONST 
    0x3ad: v3ad(0x4) = CONST 
    0x3b0: v3b0 = CALLDATASIZE 
    0x3b1: v3b1 = SUB v3b0, v3ad(0x4)
    0x3b3: v3b3 = ADD v3ad(0x4), v3b1
    0x3b7: v3b7 = CALLDATALOAD v3ad(0x4)
    0x3b8: v3b8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3cd: v3cd = AND v3b8(0xffffffffffffffffffffffffffffffffffffffff), v3b7
    0x3cf: v3cf(0x20) = CONST 
    0x3d1: v3d1(0x24) = ADD v3cf(0x20), v3ad(0x4)
    0x3d7: v3d7 = CALLDATALOAD v3d1(0x24)
    0x3d9: v3d9(0x20) = CONST 
    0x3db: v3db(0x44) = ADD v3d9(0x20), v3d1(0x24)
    0x3e3: v3e3(0xc0a) = CONST 
    0x3e6: JUMP v3e3(0xc0a)

    Begin block 0xc0a
    prev=[0x3a8], succ=[0xc43, 0xc47]
    =================================
    0xc0b: vc0b(0x0) = CONST 
    0xc0e: vc0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc23: vc23(0x0) = AND vc0e(0xffffffffffffffffffffffffffffffffffffffff), vc0b(0x0)
    0xc25: vc25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc3a: vc3a = AND vc25(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0xc3b: vc3b = EQ vc3a, vc23(0x0)
    0xc3c: vc3c = ISZERO vc3b
    0xc3d: vc3d = ISZERO vc3c
    0xc3e: vc3e = ISZERO vc3d
    0xc3f: vc3f(0xc47) = CONST 
    0xc42: JUMPI vc3f(0xc47), vc3e

    Begin block 0xc43
    prev=[0xc0a], succ=[]
    =================================
    0xc43: vc43(0x0) = CONST 
    0xc46: REVERT vc43(0x0), vc43(0x0)

    Begin block 0xc47
    prev=[0xc0a], succ=[0xc91, 0xc95]
    =================================
    0xc49: vc49(0x1) = CONST 
    0xc4b: vc4b(0x0) = CONST 
    0xc4d: vc4d = CALLER 
    0xc4e: vc4e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc63: vc63 = AND vc4e(0xffffffffffffffffffffffffffffffffffffffff), vc4d
    0xc64: vc64(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc79: vc79 = AND vc64(0xffffffffffffffffffffffffffffffffffffffff), vc63
    0xc7b: MSTORE vc4b(0x0), vc79
    0xc7c: vc7c(0x20) = CONST 
    0xc7e: vc7e(0x20) = ADD vc7c(0x20), vc4b(0x0)
    0xc81: MSTORE vc7e(0x20), vc49(0x1)
    0xc82: vc82(0x20) = CONST 
    0xc84: vc84(0x40) = ADD vc82(0x20), vc7e(0x20)
    0xc85: vc85(0x0) = CONST 
    0xc87: vc87 = SHA3 vc85(0x0), vc84(0x40)
    0xc88: vc88 = SLOAD vc87
    0xc89: vc89 = LT vc88, v3d7
    0xc8a: vc8a = ISZERO vc89
    0xc8b: vc8b = ISZERO vc8a
    0xc8c: vc8c = ISZERO vc8b
    0xc8d: vc8d(0xc95) = CONST 
    0xc90: JUMPI vc8d(0xc95), vc8c

    Begin block 0xc91
    prev=[0xc47], succ=[]
    =================================
    0xc91: vc91(0x0) = CONST 
    0xc94: REVERT vc91(0x0), vc91(0x0)

    Begin block 0xc95
    prev=[0xc47], succ=[0xce7]
    =================================
    0xc96: vc96(0xce7) = CONST 
    0xc9a: vc9a(0x1) = CONST 
    0xc9c: vc9c(0x0) = CONST 
    0xc9e: vc9e = CALLER 
    0xc9f: vc9f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcb4: vcb4 = AND vc9f(0xffffffffffffffffffffffffffffffffffffffff), vc9e
    0xcb5: vcb5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcca: vcca = AND vcb5(0xffffffffffffffffffffffffffffffffffffffff), vcb4
    0xccc: MSTORE vc9c(0x0), vcca
    0xccd: vccd(0x20) = CONST 
    0xccf: vccf(0x20) = ADD vccd(0x20), vc9c(0x0)
    0xcd2: MSTORE vccf(0x20), vc9a(0x1)
    0xcd3: vcd3(0x20) = CONST 
    0xcd5: vcd5(0x40) = ADD vcd3(0x20), vccf(0x20)
    0xcd6: vcd6(0x0) = CONST 
    0xcd8: vcd8 = SHA3 vcd6(0x0), vcd5(0x40)
    0xcd9: vcd9 = SLOAD vcd8
    0xcda: vcda(0x128b) = CONST 
    0xce0: vce0(0xffffffff) = CONST 
    0xce5: vce5(0x128b) = AND vce0(0xffffffff), vcda(0x128b)
    0xce6: vce6_0 = CALLPRIVATE vce5(0x128b), v3d7, vcd9, vc96(0xce7)

    Begin block 0xce7
    prev=[0xc95], succ=[0xd7c]
    =================================
    0xce8: vce8(0x1) = CONST 
    0xcea: vcea(0x0) = CONST 
    0xcec: vcec = CALLER 
    0xced: vced(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd02: vd02 = AND vced(0xffffffffffffffffffffffffffffffffffffffff), vcec
    0xd03: vd03(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd18: vd18 = AND vd03(0xffffffffffffffffffffffffffffffffffffffff), vd02
    0xd1a: MSTORE vcea(0x0), vd18
    0xd1b: vd1b(0x20) = CONST 
    0xd1d: vd1d(0x20) = ADD vd1b(0x20), vcea(0x0)
    0xd20: MSTORE vd1d(0x20), vce8(0x1)
    0xd21: vd21(0x20) = CONST 
    0xd23: vd23(0x40) = ADD vd21(0x20), vd1d(0x20)
    0xd24: vd24(0x0) = CONST 
    0xd26: vd26 = SHA3 vd24(0x0), vd23(0x40)
    0xd29: SSTORE vd26, vce6_0
    0xd2b: vd2b(0xd7c) = CONST 
    0xd2f: vd2f(0x1) = CONST 
    0xd31: vd31(0x0) = CONST 
    0xd34: vd34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd49: vd49 = AND vd34(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0xd4a: vd4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd5f: vd5f = AND vd4a(0xffffffffffffffffffffffffffffffffffffffff), vd49
    0xd61: MSTORE vd31(0x0), vd5f
    0xd62: vd62(0x20) = CONST 
    0xd64: vd64(0x20) = ADD vd62(0x20), vd31(0x0)
    0xd67: MSTORE vd64(0x20), vd2f(0x1)
    0xd68: vd68(0x20) = CONST 
    0xd6a: vd6a(0x40) = ADD vd68(0x20), vd64(0x20)
    0xd6b: vd6b(0x0) = CONST 
    0xd6d: vd6d = SHA3 vd6b(0x0), vd6a(0x40)
    0xd6e: vd6e = SLOAD vd6d
    0xd6f: vd6f(0x126d) = CONST 
    0xd75: vd75(0xffffffff) = CONST 
    0xd7a: vd7a(0x126d) = AND vd75(0xffffffff), vd6f(0x126d)
    0xd7b: vd7b_0 = CALLPRIVATE vd7a(0x126d), v3d7, vd6e, vd2b(0xd7c)

    Begin block 0xd7c
    prev=[0xce7], succ=[0x3e7]
    =================================
    0xd7d: vd7d(0x1) = CONST 
    0xd7f: vd7f(0x0) = CONST 
    0xd82: vd82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd97: vd97 = AND vd82(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0xd98: vd98(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdad: vdad = AND vd98(0xffffffffffffffffffffffffffffffffffffffff), vd97
    0xdaf: MSTORE vd7f(0x0), vdad
    0xdb0: vdb0(0x20) = CONST 
    0xdb2: vdb2(0x20) = ADD vdb0(0x20), vd7f(0x0)
    0xdb5: MSTORE vdb2(0x20), vd7d(0x1)
    0xdb6: vdb6(0x20) = CONST 
    0xdb8: vdb8(0x40) = ADD vdb6(0x20), vdb2(0x20)
    0xdb9: vdb9(0x0) = CONST 
    0xdbb: vdbb = SHA3 vdb9(0x0), vdb8(0x40)
    0xdbe: SSTORE vdbb, vd7b_0
    0xdc1: vdc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdd6: vdd6 = AND vdc1(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0xdd7: vdd7 = CALLER 
    0xdd8: vdd8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xded: vded = AND vdd8(0xffffffffffffffffffffffffffffffffffffffff), vdd7
    0xdee: vdee(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xe10: ve10(0x40) = CONST 
    0xe12: ve12 = MLOAD ve10(0x40)
    0xe16: MSTORE ve12, v3d7
    0xe17: ve17(0x20) = CONST 
    0xe19: ve19 = ADD ve17(0x20), ve12
    0xe1d: ve1d(0x40) = CONST 
    0xe1f: ve1f = MLOAD ve1d(0x40)
    0xe22: ve22(0x20) = SUB ve19, ve1f
    0xe24: LOG3 ve1f, ve22(0x20), vdee(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vded, vdd6
    0xe25: ve25(0x1) = CONST 
    0xe2d: JUMP v3aa(0x3e7)

    Begin block 0x3e7
    prev=[0xd7c], succ=[]
    =================================
    0x3e8: v3e8(0x40) = CONST 
    0x3ea: v3ea = MLOAD v3e8(0x40)
    0x3ed: v3ed(0x0) = ISZERO ve25(0x1)
    0x3ee: v3ee(0x1) = ISZERO v3ed(0x0)
    0x3ef: v3ef(0x0) = ISZERO v3ee(0x1)
    0x3f0: v3f0(0x1) = ISZERO v3ef(0x0)
    0x3f2: MSTORE v3ea, v3f0(0x1)
    0x3f3: v3f3(0x20) = CONST 
    0x3f5: v3f5 = ADD v3f3(0x20), v3ea
    0x3f9: v3f9(0x40) = CONST 
    0x3fb: v3fb = MLOAD v3f9(0x40)
    0x3fe: v3fe(0x20) = SUB v3f5, v3fb
    0x400: RETURN v3fb, v3fe(0x20)

}

function approveAndCall(address,uint256,bytes)() public {
    Begin block 0x401
    prev=[], succ=[0x409, 0x40d]
    =================================
    0x402: v402 = CALLVALUE 
    0x404: v404 = ISZERO v402
    0x405: v405(0x40d) = CONST 
    0x408: JUMPI v405(0x40d), v404

    Begin block 0x409
    prev=[0x401], succ=[]
    =================================
    0x409: v409(0x0) = CONST 
    0x40c: REVERT v409(0x0), v409(0x0)

    Begin block 0x40d
    prev=[0x401], succ=[0xe2e]
    =================================
    0x40f: v40f(0x492) = CONST 
    0x412: v412(0x4) = CONST 
    0x415: v415 = CALLDATASIZE 
    0x416: v416 = SUB v415, v412(0x4)
    0x418: v418 = ADD v412(0x4), v416
    0x41c: v41c = CALLDATALOAD v412(0x4)
    0x41d: v41d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x432: v432 = AND v41d(0xffffffffffffffffffffffffffffffffffffffff), v41c
    0x434: v434(0x20) = CONST 
    0x436: v436(0x24) = ADD v434(0x20), v412(0x4)
    0x43c: v43c = CALLDATALOAD v436(0x24)
    0x43e: v43e(0x20) = CONST 
    0x440: v440(0x44) = ADD v43e(0x20), v436(0x24)
    0x446: v446 = CALLDATALOAD v440(0x44)
    0x448: v448(0x20) = CONST 
    0x44a: v44a(0x64) = ADD v448(0x20), v440(0x44)
    0x44d: v44d = ADD v412(0x4), v446
    0x44f: v44f = CALLDATALOAD v44d
    0x451: v451(0x20) = CONST 
    0x453: v453 = ADD v451(0x20), v44d
    0x457: v457(0x1f) = CONST 
    0x459: v459 = ADD v457(0x1f), v44f
    0x45a: v45a(0x20) = CONST 
    0x45e: v45e = DIV v459, v45a(0x20)
    0x45f: v45f = MUL v45e, v45a(0x20)
    0x460: v460(0x20) = CONST 
    0x462: v462 = ADD v460(0x20), v45f
    0x463: v463(0x40) = CONST 
    0x465: v465 = MLOAD v463(0x40)
    0x468: v468 = ADD v465, v462
    0x469: v469(0x40) = CONST 
    0x46b: MSTORE v469(0x40), v468
    0x473: MSTORE v465, v44f
    0x474: v474(0x20) = CONST 
    0x476: v476 = ADD v474(0x20), v465
    0x47c: CALLDATACOPY v476, v453, v44f
    0x47e: v47e = ADD v476, v44f
    0x48e: v48e(0xe2e) = CONST 
    0x491: JUMP v48e(0xe2e)

    Begin block 0xe2e
    prev=[0x40d], succ=[0xeba, 0xe39]
    =================================
    0xe2f: ve2f(0x0) = CONST 
    0xe33: ve33 = EQ v43c, ve2f(0x0)
    0xe35: ve35(0xeba) = CONST 
    0xe38: JUMPI ve35(0xeba), ve33

    Begin block 0xeba
    prev=[0xe2e, 0xe39], succ=[0xec1, 0xec5]
    =================================
    0xeba_0x0: veba_0 = PHI ve33, veb9
    0xebb: vebb = ISZERO veba_0
    0xebc: vebc = ISZERO vebb
    0xebd: vebd(0xec5) = CONST 
    0xec0: JUMPI vebd(0xec5), vebc

    Begin block 0xec1
    prev=[0xeba], succ=[]
    =================================
    0xec1: vec1(0x0) = CONST 
    0xec4: REVERT vec1(0x0), vec1(0x0)

    Begin block 0xec5
    prev=[0xeba], succ=[0x10b4]
    =================================
    0xec7: vec7(0x2) = CONST 
    0xec9: vec9(0x0) = CONST 
    0xecb: vecb = CALLER 
    0xecc: vecc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xee1: vee1 = AND vecc(0xffffffffffffffffffffffffffffffffffffffff), vecb
    0xee2: vee2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xef7: vef7 = AND vee2(0xffffffffffffffffffffffffffffffffffffffff), vee1
    0xef9: MSTORE vec9(0x0), vef7
    0xefa: vefa(0x20) = CONST 
    0xefc: vefc(0x20) = ADD vefa(0x20), vec9(0x0)
    0xeff: MSTORE vefc(0x20), vec7(0x2)
    0xf00: vf00(0x20) = CONST 
    0xf02: vf02(0x40) = ADD vf00(0x20), vefc(0x20)
    0xf03: vf03(0x0) = CONST 
    0xf05: vf05 = SHA3 vf03(0x0), vf02(0x40)
    0xf06: vf06(0x0) = CONST 
    0xf09: vf09(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf1e: vf1e = AND vf09(0xffffffffffffffffffffffffffffffffffffffff), v432
    0xf1f: vf1f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf34: vf34 = AND vf1f(0xffffffffffffffffffffffffffffffffffffffff), vf1e
    0xf36: MSTORE vf06(0x0), vf34
    0xf37: vf37(0x20) = CONST 
    0xf39: vf39(0x20) = ADD vf37(0x20), vf06(0x0)
    0xf3c: MSTORE vf39(0x20), vf05
    0xf3d: vf3d(0x20) = CONST 
    0xf3f: vf3f(0x40) = ADD vf3d(0x20), vf39(0x20)
    0xf40: vf40(0x0) = CONST 
    0xf42: vf42 = SHA3 vf40(0x0), vf3f(0x40)
    0xf45: SSTORE vf42, v43c
    0xf48: vf48(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf5d: vf5d = AND vf48(0xffffffffffffffffffffffffffffffffffffffff), v432
    0xf5e: vf5e = CALLER 
    0xf5f: vf5f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf74: vf74 = AND vf5f(0xffffffffffffffffffffffffffffffffffffffff), vf5e
    0xf75: vf75(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xf97: vf97(0x40) = CONST 
    0xf99: vf99 = MLOAD vf97(0x40)
    0xf9d: MSTORE vf99, v43c
    0xf9e: vf9e(0x20) = CONST 
    0xfa0: vfa0 = ADD vf9e(0x20), vf99
    0xfa4: vfa4(0x40) = CONST 
    0xfa6: vfa6 = MLOAD vfa4(0x40)
    0xfa9: vfa9(0x20) = SUB vfa0, vfa6
    0xfab: LOG3 vfa6, vfa9(0x20), vf75(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vf74, vf5d
    0xfad: vfad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfc2: vfc2 = AND vfad(0xffffffffffffffffffffffffffffffffffffffff), v432
    0xfc3: vfc3(0x40) = CONST 
    0xfc5: vfc5 = MLOAD vfc3(0x40)
    0xfc8: vfc8(0x72656365697665417070726f76616c28616464726573732c75696e743235362c) = CONST 
    0xfea: MSTORE vfc5, vfc8(0x72656365697665417070726f76616c28616464726573732c75696e743235362c)
    0xfeb: vfeb(0x20) = CONST 
    0xfed: vfed = ADD vfeb(0x20), vfc5
    0xfee: vfee(0x616464726573732c627974657329000000000000000000000000000000000000) = CONST 
    0x1010: MSTORE vfed, vfee(0x616464726573732c627974657329000000000000000000000000000000000000)
    0x1012: v1012(0x2e) = CONST 
    0x1014: v1014 = ADD v1012(0x2e), vfc5
    0x1017: v1017(0x40) = CONST 
    0x1019: v1019 = MLOAD v1017(0x40)
    0x101c: v101c(0x2e) = SUB v1014, v1019
    0x101e: v101e = SHA3 v1019, v101c(0x2e)
    0x101f: v101f = CALLER 
    0x1021: v1021 = ADDRESS 
    0x1023: v1023(0x40) = CONST 
    0x1025: v1025 = MLOAD v1023(0x40)
    0x1026: v1026(0x24) = CONST 
    0x1028: v1028 = ADD v1026(0x24), v1025
    0x102b: v102b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1040: v1040 = AND v102b(0xffffffffffffffffffffffffffffffffffffffff), v101f
    0x1041: v1041(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1056: v1056 = AND v1041(0xffffffffffffffffffffffffffffffffffffffff), v1040
    0x1058: MSTORE v1028, v1056
    0x1059: v1059(0x20) = CONST 
    0x105b: v105b = ADD v1059(0x20), v1028
    0x105e: MSTORE v105b, v43c
    0x105f: v105f(0x20) = CONST 
    0x1061: v1061 = ADD v105f(0x20), v105b
    0x1063: v1063(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1078: v1078 = AND v1063(0xffffffffffffffffffffffffffffffffffffffff), v1021
    0x1079: v1079(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x108e: v108e = AND v1079(0xffffffffffffffffffffffffffffffffffffffff), v1078
    0x1090: MSTORE v1061, v108e
    0x1091: v1091(0x20) = CONST 
    0x1093: v1093 = ADD v1091(0x20), v1061
    0x1095: v1095(0x20) = CONST 
    0x1097: v1097 = ADD v1095(0x20), v1093
    0x109a: v109a(0x80) = SUB v1097, v1028
    0x109c: MSTORE v1093, v109a(0x80)
    0x10a0: v10a0 = MLOAD v465
    0x10a2: MSTORE v1097, v10a0
    0x10a3: v10a3(0x20) = CONST 
    0x10a5: v10a5 = ADD v10a3(0x20), v1097
    0x10a9: v10a9 = MLOAD v465
    0x10ab: v10ab(0x20) = CONST 
    0x10ad: v10ad = ADD v10ab(0x20), v465
    0x10b2: v10b2(0x0) = CONST 
    0x93be: v93be(0x10b4) = CONST 
    0x93de: JUMP v93be(0x10b4)

    Begin block 0x10b4
    prev=[0xec5, 0x10bd], succ=[0x10cf, 0x10bd]
    =================================
    0x10b4_0x0: v10b4_0 = PHI v10b2(0x0), v10c8
    0x10b7: v10b7 = LT v10b4_0, v10a9
    0x10b8: v10b8 = ISZERO v10b7
    0x10b9: v10b9(0x10cf) = CONST 
    0x10bc: JUMPI v10b9(0x10cf), v10b8

    Begin block 0x10cf
    prev=[0x10b4], succ=[0x10fc, 0x10e3]
    =================================
    0x10d8: v10d8 = ADD v10a9, v10a5
    0x10da: v10da(0x1f) = CONST 
    0x10dc: v10dc = AND v10da(0x1f), v10a9
    0x10de: v10de = ISZERO v10dc
    0x10df: v10df(0x10fc) = CONST 
    0x10e2: JUMPI v10df(0x10fc), v10de

    Begin block 0x10fc
    prev=[0x10cf, 0x10e3], succ=[0x1173]
    =================================
    0x10fc_0x1: v10fc_1 = PHI v10d8, v10f9
    0x1105: v1105(0x40) = CONST 
    0x1107: v1107 = MLOAD v1105(0x40)
    0x1108: v1108(0x20) = CONST 
    0x110c: v110c = SUB v10fc_1, v1107
    0x110d: v110d = SUB v110c, v1108(0x20)
    0x110f: MSTORE v1107, v110d
    0x1111: v1111(0x40) = CONST 
    0x1113: MSTORE v1111(0x40), v10fc_1
    0x1115: v1115(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1132: v1132(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1115(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1133: v1133 = AND v1132(0xffffffff00000000000000000000000000000000000000000000000000000000), v101e
    0x1134: v1134(0x20) = CONST 
    0x1137: v1137 = ADD v1107, v1134(0x20)
    0x1139: v1139 = MLOAD v1137
    0x113a: v113a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x115a: v115a = AND v1139, v113a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x115b: v115b = OR v115a, v1133
    0x115d: MSTORE v1137, v115b
    0x1162: v1162(0x40) = CONST 
    0x1164: v1164 = MLOAD v1162(0x40)
    0x1168: v1168 = MLOAD v1107
    0x116a: v116a(0x20) = CONST 
    0x116c: v116c = ADD v116a(0x20), v1107
    0x1171: v1171(0x0) = CONST 
    0xa7be: va7be(0x1173) = CONST 
    0xa7de: JUMP va7be(0x1173)

    Begin block 0x1173
    prev=[0x10fc, 0x117c], succ=[0x118e, 0x117c]
    =================================
    0x1173_0x0: v1173_0 = PHI v1171(0x0), v1187
    0x1176: v1176 = LT v1173_0, v1168
    0x1177: v1177 = ISZERO v1176
    0x1178: v1178(0x118e) = CONST 
    0x117b: JUMPI v1178(0x118e), v1177

    Begin block 0x118e
    prev=[0x1173], succ=[0x11bb, 0x11a2]
    =================================
    0x1197: v1197 = ADD v1168, v1164
    0x1199: v1199(0x1f) = CONST 
    0x119b: v119b = AND v1199(0x1f), v1168
    0x119d: v119d = ISZERO v119b
    0x119e: v119e(0x11bb) = CONST 
    0x11a1: JUMPI v119e(0x11bb), v119d

    Begin block 0x11bb
    prev=[0x118e, 0x11a2], succ=[0x11d7, 0x11db]
    =================================
    0x11bb_0x1: v11bb_1 = PHI v1197, v11b8
    0x11c0: v11c0(0x0) = CONST 
    0x11c2: v11c2(0x40) = CONST 
    0x11c4: v11c4 = MLOAD v11c2(0x40)
    0x11c7: v11c7 = SUB v11bb_1, v11c4
    0x11c9: v11c9(0x0) = CONST 
    0x11cc: v11cc = GAS 
    0x11cd: v11cd = CALL v11cc, vfc2, v11c9(0x0), v11c4, v11c7, v11c4, v11c0(0x0)
    0x11d1: v11d1 = ISZERO v11cd
    0x11d2: v11d2 = ISZERO v11d1
    0x11d3: v11d3(0x11db) = CONST 
    0x11d6: JUMPI v11d3(0x11db), v11d2

    Begin block 0x11d7
    prev=[0x11bb], succ=[]
    =================================
    0x11d7: v11d7(0x0) = CONST 
    0x11da: REVERT v11d7(0x0), v11d7(0x0)

    Begin block 0x11db
    prev=[0x11bb], succ=[0x492]
    =================================
    0x11dc: v11dc(0x1) = CONST 
    0x11e5: JUMP v40f(0x492)

    Begin block 0x492
    prev=[0x11db], succ=[]
    =================================
    0x493: v493(0x40) = CONST 
    0x495: v495 = MLOAD v493(0x40)
    0x498: v498(0x0) = ISZERO v11dc(0x1)
    0x499: v499(0x1) = ISZERO v498(0x0)
    0x49a: v49a(0x0) = ISZERO v499(0x1)
    0x49b: v49b(0x1) = ISZERO v49a(0x0)
    0x49d: MSTORE v495, v49b(0x1)
    0x49e: v49e(0x20) = CONST 
    0x4a0: v4a0 = ADD v49e(0x20), v495
    0x4a4: v4a4(0x40) = CONST 
    0x4a6: v4a6 = MLOAD v4a4(0x40)
    0x4a9: v4a9(0x20) = SUB v4a0, v4a6
    0x4ab: RETURN v4a6, v4a9(0x20)

    Begin block 0x11a2
    prev=[0x118e], succ=[0x11bb]
    =================================
    0x11a4: v11a4 = SUB v1197, v119b
    0x11a6: v11a6 = MLOAD v11a4
    0x11a7: v11a7(0x1) = CONST 
    0x11aa: v11aa(0x20) = CONST 
    0x11ac: v11ac = SUB v11aa(0x20), v119b
    0x11ad: v11ad(0x100) = CONST 
    0x11b0: v11b0 = EXP v11ad(0x100), v11ac
    0x11b1: v11b1 = SUB v11b0, v11a7(0x1)
    0x11b2: v11b2 = NOT v11b1
    0x11b3: v11b3 = AND v11b2, v11a6
    0x11b5: MSTORE v11a4, v11b3
    0x11b6: v11b6(0x20) = CONST 
    0x11b8: v11b8 = ADD v11b6(0x20), v11a4
    0xb1be: vb1be(0x11bb) = CONST 
    0xb1de: JUMP vb1be(0x11bb)

    Begin block 0x117c
    prev=[0x1173], succ=[0x1173]
    =================================
    0x117c_0x0: v117c_0 = PHI v1171(0x0), v1187
    0x117e: v117e = ADD v116c, v117c_0
    0x117f: v117f = MLOAD v117e
    0x1182: v1182 = ADD v1164, v117c_0
    0x1183: MSTORE v1182, v117f
    0x1184: v1184(0x20) = CONST 
    0x1187: v1187 = ADD v117c_0, v1184(0x20)
    0x118a: v118a(0x1173) = CONST 
    0x118d: JUMP v118a(0x1173)

    Begin block 0x10e3
    prev=[0x10cf], succ=[0x10fc]
    =================================
    0x10e5: v10e5 = SUB v10d8, v10dc
    0x10e7: v10e7 = MLOAD v10e5
    0x10e8: v10e8(0x1) = CONST 
    0x10eb: v10eb(0x20) = CONST 
    0x10ed: v10ed = SUB v10eb(0x20), v10dc
    0x10ee: v10ee(0x100) = CONST 
    0x10f1: v10f1 = EXP v10ee(0x100), v10ed
    0x10f2: v10f2 = SUB v10f1, v10e8(0x1)
    0x10f3: v10f3 = NOT v10f2
    0x10f4: v10f4 = AND v10f3, v10e7
    0x10f6: MSTORE v10e5, v10f4
    0x10f7: v10f7(0x20) = CONST 
    0x10f9: v10f9 = ADD v10f7(0x20), v10e5
    0x9dbe: v9dbe(0x10fc) = CONST 
    0x9dde: JUMP v9dbe(0x10fc)

    Begin block 0x10bd
    prev=[0x10b4], succ=[0x10b4]
    =================================
    0x10bd_0x0: v10bd_0 = PHI v10b2(0x0), v10c8
    0x10bf: v10bf = ADD v10ad, v10bd_0
    0x10c0: v10c0 = MLOAD v10bf
    0x10c3: v10c3 = ADD v10a5, v10bd_0
    0x10c4: MSTORE v10c3, v10c0
    0x10c5: v10c5(0x20) = CONST 
    0x10c8: v10c8 = ADD v10bd_0, v10c5(0x20)
    0x10cb: v10cb(0x10b4) = CONST 
    0x10ce: JUMP v10cb(0x10b4)

    Begin block 0xe39
    prev=[0xe2e], succ=[0xeba]
    =================================
    0xe3a: ve3a(0x0) = CONST 
    0xe3c: ve3c(0x2) = CONST 
    0xe3e: ve3e(0x0) = CONST 
    0xe40: ve40 = CALLER 
    0xe41: ve41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe56: ve56 = AND ve41(0xffffffffffffffffffffffffffffffffffffffff), ve40
    0xe57: ve57(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe6c: ve6c = AND ve57(0xffffffffffffffffffffffffffffffffffffffff), ve56
    0xe6e: MSTORE ve3e(0x0), ve6c
    0xe6f: ve6f(0x20) = CONST 
    0xe71: ve71(0x20) = ADD ve6f(0x20), ve3e(0x0)
    0xe74: MSTORE ve71(0x20), ve3c(0x2)
    0xe75: ve75(0x20) = CONST 
    0xe77: ve77(0x40) = ADD ve75(0x20), ve71(0x20)
    0xe78: ve78(0x0) = CONST 
    0xe7a: ve7a = SHA3 ve78(0x0), ve77(0x40)
    0xe7b: ve7b(0x0) = CONST 
    0xe7e: ve7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe93: ve93 = AND ve7e(0xffffffffffffffffffffffffffffffffffffffff), v432
    0xe94: ve94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xea9: vea9 = AND ve94(0xffffffffffffffffffffffffffffffffffffffff), ve93
    0xeab: MSTORE ve7b(0x0), vea9
    0xeac: veac(0x20) = CONST 
    0xeae: veae(0x20) = ADD veac(0x20), ve7b(0x0)
    0xeb1: MSTORE veae(0x20), ve7a
    0xeb2: veb2(0x20) = CONST 
    0xeb4: veb4(0x40) = ADD veb2(0x20), veae(0x20)
    0xeb5: veb5(0x0) = CONST 
    0xeb7: veb7 = SHA3 veb5(0x0), veb4(0x40)
    0xeb8: veb8 = SLOAD veb7
    0xeb9: veb9 = EQ veb8, ve3a(0x0)
    0x89be: v89be(0xeba) = CONST 
    0x89de: JUMP v89be(0xeba)

}

function allowance(address,address)() public {
    Begin block 0x4ac
    prev=[], succ=[0x4b4, 0x4b8]
    =================================
    0x4ad: v4ad = CALLVALUE 
    0x4af: v4af = ISZERO v4ad
    0x4b0: v4b0(0x4b8) = CONST 
    0x4b3: JUMPI v4b0(0x4b8), v4af

    Begin block 0x4b4
    prev=[0x4ac], succ=[]
    =================================
    0x4b4: v4b4(0x0) = CONST 
    0x4b7: REVERT v4b4(0x0), v4b4(0x0)

    Begin block 0x4b8
    prev=[0x4ac], succ=[0x11e6]
    =================================
    0x4ba: v4ba(0x50d) = CONST 
    0x4bd: v4bd(0x4) = CONST 
    0x4c0: v4c0 = CALLDATASIZE 
    0x4c1: v4c1 = SUB v4c0, v4bd(0x4)
    0x4c3: v4c3 = ADD v4bd(0x4), v4c1
    0x4c7: v4c7 = CALLDATALOAD v4bd(0x4)
    0x4c8: v4c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4dd: v4dd = AND v4c8(0xffffffffffffffffffffffffffffffffffffffff), v4c7
    0x4df: v4df(0x20) = CONST 
    0x4e1: v4e1(0x24) = ADD v4df(0x20), v4bd(0x4)
    0x4e7: v4e7 = CALLDATALOAD v4e1(0x24)
    0x4e8: v4e8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4fd: v4fd = AND v4e8(0xffffffffffffffffffffffffffffffffffffffff), v4e7
    0x4ff: v4ff(0x20) = CONST 
    0x501: v501(0x44) = ADD v4ff(0x20), v4e1(0x24)
    0x509: v509(0x11e6) = CONST 
    0x50c: JUMP v509(0x11e6)

    Begin block 0x11e6
    prev=[0x4b8], succ=[0x50d]
    =================================
    0x11e7: v11e7(0x0) = CONST 
    0x11e9: v11e9(0x2) = CONST 
    0x11eb: v11eb(0x0) = CONST 
    0x11ee: v11ee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1203: v1203 = AND v11ee(0xffffffffffffffffffffffffffffffffffffffff), v4dd
    0x1204: v1204(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1219: v1219 = AND v1204(0xffffffffffffffffffffffffffffffffffffffff), v1203
    0x121b: MSTORE v11eb(0x0), v1219
    0x121c: v121c(0x20) = CONST 
    0x121e: v121e(0x20) = ADD v121c(0x20), v11eb(0x0)
    0x1221: MSTORE v121e(0x20), v11e9(0x2)
    0x1222: v1222(0x20) = CONST 
    0x1224: v1224(0x40) = ADD v1222(0x20), v121e(0x20)
    0x1225: v1225(0x0) = CONST 
    0x1227: v1227 = SHA3 v1225(0x0), v1224(0x40)
    0x1228: v1228(0x0) = CONST 
    0x122b: v122b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1240: v1240 = AND v122b(0xffffffffffffffffffffffffffffffffffffffff), v4fd
    0x1241: v1241(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1256: v1256 = AND v1241(0xffffffffffffffffffffffffffffffffffffffff), v1240
    0x1258: MSTORE v1228(0x0), v1256
    0x1259: v1259(0x20) = CONST 
    0x125b: v125b(0x20) = ADD v1259(0x20), v1228(0x0)
    0x125e: MSTORE v125b(0x20), v1227
    0x125f: v125f(0x20) = CONST 
    0x1261: v1261(0x40) = ADD v125f(0x20), v125b(0x20)
    0x1262: v1262(0x0) = CONST 
    0x1264: v1264 = SHA3 v1262(0x0), v1261(0x40)
    0x1265: v1265 = SLOAD v1264
    0x126c: JUMP v4ba(0x50d)

    Begin block 0x50d
    prev=[0x11e6], succ=[]
    =================================
    0x50e: v50e(0x40) = CONST 
    0x510: v510 = MLOAD v50e(0x40)
    0x514: MSTORE v510, v1265
    0x515: v515(0x20) = CONST 
    0x517: v517 = ADD v515(0x20), v510
    0x51b: v51b(0x40) = CONST 
    0x51d: v51d = MLOAD v51b(0x40)
    0x520: v520(0x20) = SUB v517, v51d
    0x522: RETURN v51d, v520(0x20)

}

function fallback()() public {
    Begin block 0xaf
    prev=[], succ=[]
    =================================
    0xb0: vb0(0x0) = CONST 
    0xb3: REVERT vb0(0x0), vb0(0x0)

}

function name()() public {
    Begin block 0xb4
    prev=[], succ=[0xbc, 0xc0]
    =================================
    0xb5: vb5 = CALLVALUE 
    0xb7: vb7 = ISZERO vb5
    0xb8: vb8(0xc0) = CONST 
    0xbb: JUMPI vb8(0xc0), vb7

    Begin block 0xbc
    prev=[0xb4], succ=[]
    =================================
    0xbc: vbc(0x0) = CONST 
    0xbf: REVERT vbc(0x0), vbc(0x0)

    Begin block 0xc0
    prev=[0xb4], succ=[0x523B0xc0]
    =================================
    0xc2: vc2(0xc9) = CONST 
    0xc5: vc5(0x523) = CONST 
    0xc8: JUMP vc5(0x523)

    Begin block 0x523B0xc0
    prev=[0xc0], succ=[0x573B0xc0, 0x163dcB0xc0]
    =================================
    0x524S0xc0: v524Vc0(0x3) = CONST 
    0x527S0xc0: v527Vc0 = SLOAD v524Vc0(0x3)
    0x528S0xc0: v528Vc0(0x1) = CONST 
    0x52bS0xc0: v52bVc0(0x1) = CONST 
    0x52dS0xc0: v52dVc0 = AND v52bVc0(0x1), v527Vc0
    0x52eS0xc0: v52eVc0 = ISZERO v52dVc0
    0x52fS0xc0: v52fVc0(0x100) = CONST 
    0x532S0xc0: v532Vc0 = MUL v52fVc0(0x100), v52eVc0
    0x533S0xc0: v533Vc0 = SUB v532Vc0, v528Vc0(0x1)
    0x534S0xc0: v534Vc0 = AND v533Vc0, v527Vc0
    0x535S0xc0: v535Vc0(0x2) = CONST 
    0x538S0xc0: v538Vc0 = DIV v534Vc0, v535Vc0(0x2)
    0x53aS0xc0: v53aVc0(0x1f) = CONST 
    0x53cS0xc0: v53cVc0 = ADD v53aVc0(0x1f), v538Vc0
    0x53dS0xc0: v53dVc0(0x20) = CONST 
    0x541S0xc0: v541Vc0 = DIV v53cVc0, v53dVc0(0x20)
    0x542S0xc0: v542Vc0 = MUL v541Vc0, v53dVc0(0x20)
    0x543S0xc0: v543Vc0(0x20) = CONST 
    0x545S0xc0: v545Vc0 = ADD v543Vc0(0x20), v542Vc0
    0x546S0xc0: v546Vc0(0x40) = CONST 
    0x548S0xc0: v548Vc0 = MLOAD v546Vc0(0x40)
    0x54bS0xc0: v54bVc0 = ADD v548Vc0, v545Vc0
    0x54cS0xc0: v54cVc0(0x40) = CONST 
    0x54eS0xc0: MSTORE v54cVc0(0x40), v54bVc0
    0x555S0xc0: MSTORE v548Vc0, v538Vc0
    0x556S0xc0: v556Vc0(0x20) = CONST 
    0x558S0xc0: v558Vc0 = ADD v556Vc0(0x20), v548Vc0
    0x55bS0xc0: v55bVc0 = SLOAD v524Vc0(0x3)
    0x55cS0xc0: v55cVc0(0x1) = CONST 
    0x55fS0xc0: v55fVc0(0x1) = CONST 
    0x561S0xc0: v561Vc0 = AND v55fVc0(0x1), v55bVc0
    0x562S0xc0: v562Vc0 = ISZERO v561Vc0
    0x563S0xc0: v563Vc0(0x100) = CONST 
    0x566S0xc0: v566Vc0 = MUL v563Vc0(0x100), v562Vc0
    0x567S0xc0: v567Vc0 = SUB v566Vc0, v55cVc0(0x1)
    0x568S0xc0: v568Vc0 = AND v567Vc0, v55bVc0
    0x569S0xc0: v569Vc0(0x2) = CONST 
    0x56cS0xc0: v56cVc0 = DIV v568Vc0, v569Vc0(0x2)
    0x56eS0xc0: v56eVc0 = ISZERO v56cVc0
    0x56fS0xc0: v56fVc0(0x163dc) = CONST 
    0x572S0xc0: JUMPI v56fVc0(0x163dc), v56eVc0

    Begin block 0x573B0xc0
    prev=[0x523B0xc0], succ=[0x57bB0xc0, 0x58eB0xc0]
    =================================
    0x574S0xc0: v574Vc0(0x1f) = CONST 
    0x576S0xc0: v576Vc0 = LT v574Vc0(0x1f), v56cVc0
    0x577S0xc0: v577Vc0(0x58e) = CONST 
    0x57aS0xc0: JUMPI v577Vc0(0x58e), v576Vc0

    Begin block 0x57bB0xc0
    prev=[0x573B0xc0], succ=[0x16403B0xc0]
    =================================
    0x57bS0xc0: v57bVc0(0x100) = CONST 
    0x580S0xc0: v580Vc0 = SLOAD v524Vc0(0x3)
    0x581S0xc0: v581Vc0 = DIV v580Vc0, v57bVc0(0x100)
    0x582S0xc0: v582Vc0 = MUL v581Vc0, v57bVc0(0x100)
    0x584S0xc0: MSTORE v558Vc0, v582Vc0
    0x586S0xc0: v586Vc0(0x20) = CONST 
    0x588S0xc0: v588Vc0 = ADD v586Vc0(0x20), v558Vc0
    0x58aS0xc0: v58aVc0(0x16403) = CONST 
    0x58dS0xc0: JUMP v58aVc0(0x16403)

    Begin block 0x16403B0xc0
    prev=[0x57bB0xc0], succ=[0xc9]
    =================================
    0x1640aS0xc0: JUMP vc2(0xc9)

    Begin block 0xc9
    prev=[0x163dcB0xc0, 0x16403B0xc0, 0x16478B0xc0], succ=[0xee]
    =================================
    0xca: vca(0x40) = CONST 
    0xcc: vcc = MLOAD vca(0x40)
    0xcf: vcf(0x20) = CONST 
    0xd1: vd1 = ADD vcf(0x20), vcc
    0xd4: vd4(0x20) = SUB vd1, vcc
    0xd6: MSTORE vcc, vd4(0x20)
    0xda: vda = MLOAD v548Vc0
    0xdc: MSTORE vd1, vda
    0xdd: vdd(0x20) = CONST 
    0xdf: vdf = ADD vdd(0x20), vd1
    0xe3: ve3 = MLOAD v548Vc0
    0xe5: ve5(0x20) = CONST 
    0xe7: ve7 = ADD ve5(0x20), v548Vc0
    0xec: vec(0x0) = CONST 
    0x25be: v25be(0xee) = CONST 
    0x25de: JUMP v25be(0xee)

    Begin block 0xee
    prev=[0xc9, 0xf7], succ=[0x109, 0xf7]
    =================================
    0xee_0x0: vee_0 = PHI vec(0x0), v102
    0xf1: vf1 = LT vee_0, ve3
    0xf2: vf2 = ISZERO vf1
    0xf3: vf3(0x109) = CONST 
    0xf6: JUMPI vf3(0x109), vf2

    Begin block 0x109
    prev=[0xee], succ=[0x136, 0x11d]
    =================================
    0x112: v112 = ADD ve3, vdf
    0x114: v114(0x1f) = CONST 
    0x116: v116 = AND v114(0x1f), ve3
    0x118: v118 = ISZERO v116
    0x119: v119(0x136) = CONST 
    0x11c: JUMPI v119(0x136), v118

    Begin block 0x136
    prev=[0x109, 0x11d], succ=[]
    =================================
    0x136_0x1: v136_1 = PHI v112, v133
    0x13c: v13c(0x40) = CONST 
    0x13e: v13e = MLOAD v13c(0x40)
    0x141: v141 = SUB v136_1, v13e
    0x143: RETURN v13e, v141

    Begin block 0x11d
    prev=[0x109], succ=[0x136]
    =================================
    0x11f: v11f = SUB v112, v116
    0x121: v121 = MLOAD v11f
    0x122: v122(0x1) = CONST 
    0x125: v125(0x20) = CONST 
    0x127: v127 = SUB v125(0x20), v116
    0x128: v128(0x100) = CONST 
    0x12b: v12b = EXP v128(0x100), v127
    0x12c: v12c = SUB v12b, v122(0x1)
    0x12d: v12d = NOT v12c
    0x12e: v12e = AND v12d, v121
    0x130: MSTORE v11f, v12e
    0x131: v131(0x20) = CONST 
    0x133: v133 = ADD v131(0x20), v11f
    0x2fbe: v2fbe(0x136) = CONST 
    0x2fde: JUMP v2fbe(0x136)

    Begin block 0xf7
    prev=[0xee], succ=[0xee]
    =================================
    0xf7_0x0: vf7_0 = PHI vec(0x0), v102
    0xf9: vf9 = ADD ve7, vf7_0
    0xfa: vfa = MLOAD vf9
    0xfd: vfd = ADD vdf, vf7_0
    0xfe: MSTORE vfd, vfa
    0xff: vff(0x20) = CONST 
    0x102: v102 = ADD vf7_0, vff(0x20)
    0x105: v105(0xee) = CONST 
    0x108: JUMP v105(0xee)

    Begin block 0x58eB0xc0
    prev=[0x573B0xc0], succ=[0x59cB0xc0]
    =================================
    0x590S0xc0: v590Vc0 = ADD v558Vc0, v56cVc0
    0x593S0xc0: v593Vc0(0x0) = CONST 
    0x595S0xc0: MSTORE v593Vc0(0x0), v524Vc0(0x3)
    0x596S0xc0: v596Vc0(0x20) = CONST 
    0x598S0xc0: v598Vc0(0x0) = CONST 
    0x59aS0xc0: v59aVc0 = SHA3 v598Vc0(0x0), v596Vc0(0x20)
    0x4dbeS0xc0: v4dbeVc0(0x59c) = CONST 
    0x4ddeS0xc0: JUMP v4dbeVc0(0x59c)

    Begin block 0x59cB0xc0
    prev=[0x58eB0xc0, 0x59cB0xc0], succ=[0x59cB0xc0, 0x5b0B0xc0]
    =================================
    0x59c_0x0S0xc0: v59c_0Vc0 = PHI v558Vc0, v5a8Vc0
    0x59c_0x1S0xc0: v59c_1Vc0 = PHI v59aVc0, v5a4Vc0
    0x59eS0xc0: v59eVc0 = SLOAD v59c_1Vc0
    0x5a0S0xc0: MSTORE v59c_0Vc0, v59eVc0
    0x5a2S0xc0: v5a2Vc0(0x1) = CONST 
    0x5a4S0xc0: v5a4Vc0 = ADD v5a2Vc0(0x1), v59c_1Vc0
    0x5a6S0xc0: v5a6Vc0(0x20) = CONST 
    0x5a8S0xc0: v5a8Vc0 = ADD v5a6Vc0(0x20), v59c_0Vc0
    0x5abS0xc0: v5abVc0 = GT v590Vc0, v5a8Vc0
    0x5acS0xc0: v5acVc0(0x59c) = CONST 
    0x5afS0xc0: JUMPI v5acVc0(0x59c), v5abVc0

    Begin block 0x5b0B0xc0
    prev=[0x59cB0xc0], succ=[0x16478B0xc0]
    =================================
    0x5b2S0xc0: v5b2Vc0 = SUB v5a8Vc0, v590Vc0
    0x5b3S0xc0: v5b3Vc0(0x1f) = CONST 
    0x5b5S0xc0: v5b5Vc0 = AND v5b3Vc0(0x1f), v5b2Vc0
    0x5b7S0xc0: v5b7Vc0 = ADD v590Vc0, v5b5Vc0
    0x57beS0xc0: v57beVc0(0x16478) = CONST 
    0x57deS0xc0: JUMP v57beVc0(0x16478)

    Begin block 0x16478B0xc0
    prev=[0x5b0B0xc0], succ=[0xc9]
    =================================
    0x1647fS0xc0: JUMP vc2(0xc9)

    Begin block 0x163dcB0xc0
    prev=[0x523B0xc0], succ=[0xc9]
    =================================
    0x163e3S0xc0: JUMP vc2(0xc9)

}

