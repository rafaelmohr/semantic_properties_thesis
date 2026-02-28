function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2fda]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x7da: v7da(0x2fda) = CONST 
    0x7fa: JUMPI v7da(0x2fda), v8

    Begin block 0xd
    prev=[0x0], succ=[0x39da, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x41725ce9) = CONST 
    0x3c: v3c = EQ v37(0x41725ce9), v35
    0x11da: v11da(0x39da) = CONST 
    0x11fa: JUMPI v11da(0x39da), v3c

    Begin block 0x39da
    prev=[0xd], succ=[]
    =================================
    0x39fa: v39fa(0x250) = CONST 
    0x3a1a: CALLPRIVATE v39fa(0x250)

    Begin block 0x41
    prev=[0xd], succ=[0x43da, 0x4c]
    =================================
    0x42: v42(0x70a08231) = CONST 
    0x47: v47 = EQ v42(0x70a08231), v35
    0x1bda: v1bda(0x43da) = CONST 
    0x1bfa: JUMPI v1bda(0x43da), v47

    Begin block 0x43da
    prev=[0x41], succ=[]
    =================================
    0x43fa: v43fa(0x2a7) = CONST 
    0x441a: CALLPRIVATE v43fa(0x2a7)

    Begin block 0x4c
    prev=[0x41], succ=[0x2fda, 0x4dda]
    =================================
    0x4d: v4d(0xc23697a8) = CONST 
    0x52: v52 = EQ v4d(0xc23697a8), v35
    0x25da: v25da(0x4dda) = CONST 
    0x25fa: JUMPI v25da(0x4dda), v52

    Begin block 0x2fda
    prev=[0x0, 0x4c], succ=[]
    =================================
    0x2ffa: v2ffa(0x57) = CONST 
    0x301a: CALLPRIVATE v2ffa(0x57)

    Begin block 0x4dda
    prev=[0x4c], succ=[]
    =================================
    0x4dfa: v4dfa(0x2fe) = CONST 
    0x4e1a: CALLPRIVATE v4dfa(0x2fe)

}

function swapaddress()() public {
    Begin block 0x250
    prev=[], succ=[0x258, 0x25c]
    =================================
    0x251: v251 = CALLVALUE 
    0x253: v253 = ISZERO v251
    0x254: v254(0x25c) = CONST 
    0x257: JUMPI v254(0x25c), v253

    Begin block 0x258
    prev=[0x250], succ=[]
    =================================
    0x258: v258(0x0) = CONST 
    0x25b: REVERT v258(0x0), v258(0x0)

    Begin block 0x25c
    prev=[0x250], succ=[0x359]
    =================================
    0x25e: v25e(0x265) = CONST 
    0x261: v261(0x359) = CONST 
    0x264: JUMP v261(0x359)

    Begin block 0x359
    prev=[0x25c], succ=[0x265]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35e: v35e = SLOAD v35a(0x0)
    0x360: v360(0x100) = CONST 
    0x363: v363(0x1) = EXP v360(0x100), v35a(0x0)
    0x365: v365 = DIV v35e, v363(0x1)
    0x366: v366(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x37b: v37b = AND v366(0xffffffffffffffffffffffffffffffffffffffff), v365
    0x37d: JUMP v25e(0x265)

    Begin block 0x265
    prev=[0x359], succ=[]
    =================================
    0x266: v266(0x40) = CONST 
    0x268: v268 = MLOAD v266(0x40)
    0x26b: v26b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x280: v280 = AND v26b(0xffffffffffffffffffffffffffffffffffffffff), v37b
    0x281: v281(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x296: v296 = AND v281(0xffffffffffffffffffffffffffffffffffffffff), v280
    0x298: MSTORE v268, v296
    0x299: v299(0x20) = CONST 
    0x29b: v29b = ADD v299(0x20), v268
    0x29f: v29f(0x40) = CONST 
    0x2a1: v2a1 = MLOAD v29f(0x40)
    0x2a4: v2a4(0x20) = SUB v29b, v2a1
    0x2a6: RETURN v2a1, v2a4(0x20)

}

function balanceOf(address)() public {
    Begin block 0x2a7
    prev=[], succ=[0x2af, 0x2b3]
    =================================
    0x2a8: v2a8 = CALLVALUE 
    0x2aa: v2aa = ISZERO v2a8
    0x2ab: v2ab(0x2b3) = CONST 
    0x2ae: JUMPI v2ab(0x2b3), v2aa

    Begin block 0x2af
    prev=[0x2a7], succ=[]
    =================================
    0x2af: v2af(0x0) = CONST 
    0x2b2: REVERT v2af(0x0), v2af(0x0)

    Begin block 0x2b3
    prev=[0x2a7], succ=[0x37e]
    =================================
    0x2b5: v2b5(0x2e8) = CONST 
    0x2b8: v2b8(0x4) = CONST 
    0x2bb: v2bb = CALLDATASIZE 
    0x2bc: v2bc = SUB v2bb, v2b8(0x4)
    0x2be: v2be = ADD v2b8(0x4), v2bc
    0x2c2: v2c2 = CALLDATALOAD v2b8(0x4)
    0x2c3: v2c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d8: v2d8 = AND v2c3(0xffffffffffffffffffffffffffffffffffffffff), v2c2
    0x2da: v2da(0x20) = CONST 
    0x2dc: v2dc(0x24) = ADD v2da(0x20), v2b8(0x4)
    0x2e4: v2e4(0x37e) = CONST 
    0x2e7: JUMP v2e4(0x37e)

    Begin block 0x37e
    prev=[0x2b3], succ=[0x2e8]
    =================================
    0x37f: v37f(0x1) = CONST 
    0x381: v381(0x20) = CONST 
    0x383: MSTORE v381(0x20), v37f(0x1)
    0x385: v385(0x0) = CONST 
    0x387: MSTORE v385(0x0), v2d8
    0x388: v388(0x40) = CONST 
    0x38a: v38a(0x0) = CONST 
    0x38c: v38c = SHA3 v38a(0x0), v388(0x40)
    0x38d: v38d(0x0) = CONST 
    0x393: v393 = SLOAD v38c
    0x395: JUMP v2b5(0x2e8)

    Begin block 0x2e8
    prev=[0x37e], succ=[]
    =================================
    0x2e9: v2e9(0x40) = CONST 
    0x2eb: v2eb = MLOAD v2e9(0x40)
    0x2ef: MSTORE v2eb, v393
    0x2f0: v2f0(0x20) = CONST 
    0x2f2: v2f2 = ADD v2f0(0x20), v2eb
    0x2f6: v2f6(0x40) = CONST 
    0x2f8: v2f8 = MLOAD v2f6(0x40)
    0x2fb: v2fb(0x20) = SUB v2f2, v2f8
    0x2fd: RETURN v2f8, v2fb(0x20)

}

function check(address)() public {
    Begin block 0x2fe
    prev=[], succ=[0x306, 0x30a]
    =================================
    0x2ff: v2ff = CALLVALUE 
    0x301: v301 = ISZERO v2ff
    0x302: v302(0x30a) = CONST 
    0x305: JUMPI v302(0x30a), v301

    Begin block 0x306
    prev=[0x2fe], succ=[]
    =================================
    0x306: v306(0x0) = CONST 
    0x309: REVERT v306(0x0), v306(0x0)

    Begin block 0x30a
    prev=[0x2fe], succ=[0x396]
    =================================
    0x30c: v30c(0x33f) = CONST 
    0x30f: v30f(0x4) = CONST 
    0x312: v312 = CALLDATASIZE 
    0x313: v313 = SUB v312, v30f(0x4)
    0x315: v315 = ADD v30f(0x4), v313
    0x319: v319 = CALLDATALOAD v30f(0x4)
    0x31a: v31a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x32f: v32f = AND v31a(0xffffffffffffffffffffffffffffffffffffffff), v319
    0x331: v331(0x20) = CONST 
    0x333: v333(0x24) = ADD v331(0x20), v30f(0x4)
    0x33b: v33b(0x396) = CONST 
    0x33e: JUMP v33b(0x396)

    Begin block 0x396
    prev=[0x30a], succ=[0x33f]
    =================================
    0x397: v397(0x2) = CONST 
    0x399: v399(0x20) = CONST 
    0x39b: MSTORE v399(0x20), v397(0x2)
    0x39d: v39d(0x0) = CONST 
    0x39f: MSTORE v39d(0x0), v32f
    0x3a0: v3a0(0x40) = CONST 
    0x3a2: v3a2(0x0) = CONST 
    0x3a4: v3a4 = SHA3 v3a2(0x0), v3a0(0x40)
    0x3a5: v3a5(0x0) = CONST 
    0x3a9: v3a9 = SLOAD v3a4
    0x3ab: v3ab(0x100) = CONST 
    0x3ae: v3ae(0x1) = EXP v3ab(0x100), v3a5(0x0)
    0x3b0: v3b0 = DIV v3a9, v3ae(0x1)
    0x3b1: v3b1(0xff) = CONST 
    0x3b3: v3b3 = AND v3b1(0xff), v3b0
    0x3b5: JUMP v30c(0x33f)

    Begin block 0x33f
    prev=[0x396], succ=[]
    =================================
    0x340: v340(0x40) = CONST 
    0x342: v342 = MLOAD v340(0x40)
    0x345: v345 = ISZERO v3b3
    0x346: v346 = ISZERO v345
    0x347: v347 = ISZERO v346
    0x348: v348 = ISZERO v347
    0x34a: MSTORE v342, v348
    0x34b: v34b(0x20) = CONST 
    0x34d: v34d = ADD v34b(0x20), v342
    0x351: v351(0x40) = CONST 
    0x353: v353 = MLOAD v351(0x40)
    0x356: v356(0x20) = SUB v34d, v353
    0x358: RETURN v353, v356(0x20)

}

function fallback()() public {
    Begin block 0x57
    prev=[], succ=[0xb2, 0xb6]
    =================================
    0x58: v58(0x0) = CONST 
    0x5a: v5a(0x1) = ISZERO v58(0x0)
    0x5b: v5b(0x0) = ISZERO v5a(0x1)
    0x5c: v5c(0x2) = CONST 
    0x5e: v5e(0x0) = CONST 
    0x60: v60 = CALLER 
    0x61: v61(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x76: v76 = AND v61(0xffffffffffffffffffffffffffffffffffffffff), v60
    0x77: v77(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8c: v8c = AND v77(0xffffffffffffffffffffffffffffffffffffffff), v76
    0x8e: MSTORE v5e(0x0), v8c
    0x8f: v8f(0x20) = CONST 
    0x91: v91(0x20) = ADD v8f(0x20), v5e(0x0)
    0x94: MSTORE v91(0x20), v5c(0x2)
    0x95: v95(0x20) = CONST 
    0x97: v97(0x40) = ADD v95(0x20), v91(0x20)
    0x98: v98(0x0) = CONST 
    0x9a: v9a = SHA3 v98(0x0), v97(0x40)
    0x9b: v9b(0x0) = CONST 
    0x9e: v9e = SLOAD v9a
    0xa0: va0(0x100) = CONST 
    0xa3: va3(0x1) = EXP va0(0x100), v9b(0x0)
    0xa5: va5 = DIV v9e, va3(0x1)
    0xa6: va6(0xff) = CONST 
    0xa8: va8 = AND va6(0xff), va5
    0xa9: va9 = ISZERO va8
    0xaa: vaa = ISZERO va9
    0xab: vab = EQ vaa, v5b(0x0)
    0xac: vac = ISZERO vab
    0xad: vad = ISZERO vac
    0xae: vae(0xb6) = CONST 
    0xb1: JUMPI vae(0xb6), vad

    Begin block 0xb2
    prev=[0x57], succ=[]
    =================================
    0xb2: vb2(0x0) = CONST 
    0xb5: REVERT vb2(0x0), vb2(0x0)

    Begin block 0xb6
    prev=[0x57], succ=[0xc1, 0xc5]
    =================================
    0xb7: vb7(0x0) = CONST 
    0xb9: vb9 = CALLVALUE 
    0xba: vba = EQ vb9, vb7(0x0)
    0xbb: vbb = ISZERO vba
    0xbc: vbc = ISZERO vbb
    0xbd: vbd(0xc5) = CONST 
    0xc0: JUMPI vbd(0xc5), vbc

    Begin block 0xc1
    prev=[0xb6], succ=[]
    =================================
    0xc1: vc1(0x0) = CONST 
    0xc4: REVERT vc1(0x0), vc1(0x0)

    Begin block 0xc5
    prev=[0xb6], succ=[0x1da, 0x1de]
    =================================
    0xc6: vc6(0x2faf080) = CONST 
    0xcb: vcb(0x1) = CONST 
    0xcd: vcd(0x0) = CONST 
    0xcf: vcf = CALLER 
    0xd0: vd0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe5: ve5 = AND vd0(0xffffffffffffffffffffffffffffffffffffffff), vcf
    0xe6: ve6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfb: vfb = AND ve6(0xffffffffffffffffffffffffffffffffffffffff), ve5
    0xfd: MSTORE vcd(0x0), vfb
    0xfe: vfe(0x20) = CONST 
    0x100: v100(0x20) = ADD vfe(0x20), vcd(0x0)
    0x103: MSTORE v100(0x20), vcb(0x1)
    0x104: v104(0x20) = CONST 
    0x106: v106(0x40) = ADD v104(0x20), v100(0x20)
    0x107: v107(0x0) = CONST 
    0x109: v109 = SHA3 v107(0x0), v106(0x40)
    0x10a: v10a(0x0) = CONST 
    0x10e: v10e = SLOAD v109
    0x10f: v10f = ADD v10e, vc6(0x2faf080)
    0x115: SSTORE v109, v10f
    0x117: v117(0x0) = CONST 
    0x11b: v11b = SLOAD v117(0x0)
    0x11d: v11d(0x100) = CONST 
    0x120: v120(0x1) = EXP v11d(0x100), v117(0x0)
    0x122: v122 = DIV v11b, v120(0x1)
    0x123: v123(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x138: v138 = AND v123(0xffffffffffffffffffffffffffffffffffffffff), v122
    0x139: v139(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14e: v14e = AND v139(0xffffffffffffffffffffffffffffffffffffffff), v138
    0x14f: v14f(0xa9059cbb) = CONST 
    0x154: v154 = CALLER 
    0x155: v155(0x2faf080) = CONST 
    0x15a: v15a(0x40) = CONST 
    0x15c: v15c = MLOAD v15a(0x40)
    0x15e: v15e(0xffffffff) = CONST 
    0x163: v163(0xa9059cbb) = AND v15e(0xffffffff), v14f(0xa9059cbb)
    0x164: v164(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x182: v182(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = MUL v164(0x100000000000000000000000000000000000000000000000000000000), v163(0xa9059cbb)
    0x184: MSTORE v15c, v182(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x185: v185(0x4) = CONST 
    0x187: v187 = ADD v185(0x4), v15c
    0x18a: v18a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19f: v19f = AND v18a(0xffffffffffffffffffffffffffffffffffffffff), v154
    0x1a0: v1a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b5: v1b5 = AND v1a0(0xffffffffffffffffffffffffffffffffffffffff), v19f
    0x1b7: MSTORE v187, v1b5
    0x1b8: v1b8(0x20) = CONST 
    0x1ba: v1ba = ADD v1b8(0x20), v187
    0x1bd: MSTORE v1ba, v155(0x2faf080)
    0x1be: v1be(0x20) = CONST 
    0x1c0: v1c0 = ADD v1be(0x20), v1ba
    0x1c5: v1c5(0x0) = CONST 
    0x1c7: v1c7(0x40) = CONST 
    0x1c9: v1c9 = MLOAD v1c7(0x40)
    0x1cc: v1cc(0x44) = SUB v1c0, v1c9
    0x1ce: v1ce(0x0) = CONST 
    0x1d2: v1d2 = EXTCODESIZE v14e
    0x1d3: v1d3 = ISZERO v1d2
    0x1d5: v1d5 = ISZERO v1d3
    0x1d6: v1d6(0x1de) = CONST 
    0x1d9: JUMPI v1d6(0x1de), v1d5

    Begin block 0x1da
    prev=[0xc5], succ=[]
    =================================
    0x1da: v1da(0x0) = CONST 
    0x1dd: REVERT v1da(0x0), v1da(0x0)

    Begin block 0x1de
    prev=[0xc5], succ=[0x1e9, 0x1f2]
    =================================
    0x1e0: v1e0 = GAS 
    0x1e1: v1e1 = CALL v1e0, v14e, v1ce(0x0), v1c9, v1cc(0x44), v1c9, v1c5(0x0)
    0x1e2: v1e2 = ISZERO v1e1
    0x1e4: v1e4 = ISZERO v1e2
    0x1e5: v1e5(0x1f2) = CONST 
    0x1e8: JUMPI v1e5(0x1f2), v1e4

    Begin block 0x1e9
    prev=[0x1de], succ=[]
    =================================
    0x1e9: v1e9 = RETURNDATASIZE 
    0x1ea: v1ea(0x0) = CONST 
    0x1ed: RETURNDATACOPY v1ea(0x0), v1ea(0x0), v1e9
    0x1ee: v1ee = RETURNDATASIZE 
    0x1ef: v1ef(0x0) = CONST 
    0x1f1: REVERT v1ef(0x0), v1ee

    Begin block 0x1f2
    prev=[0x1de], succ=[]
    =================================
    0x1f7: v1f7(0x1) = CONST 
    0x1f9: v1f9(0x2) = CONST 
    0x1fb: v1fb(0x0) = CONST 
    0x1fd: v1fd = CALLER 
    0x1fe: v1fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x213: v213 = AND v1fe(0xffffffffffffffffffffffffffffffffffffffff), v1fd
    0x214: v214(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x229: v229 = AND v214(0xffffffffffffffffffffffffffffffffffffffff), v213
    0x22b: MSTORE v1fb(0x0), v229
    0x22c: v22c(0x20) = CONST 
    0x22e: v22e(0x20) = ADD v22c(0x20), v1fb(0x0)
    0x231: MSTORE v22e(0x20), v1f9(0x2)
    0x232: v232(0x20) = CONST 
    0x234: v234(0x40) = ADD v232(0x20), v22e(0x20)
    0x235: v235(0x0) = CONST 
    0x237: v237 = SHA3 v235(0x0), v234(0x40)
    0x238: v238(0x0) = CONST 
    0x23a: v23a(0x100) = CONST 
    0x23d: v23d(0x1) = EXP v23a(0x100), v238(0x0)
    0x23f: v23f = SLOAD v237
    0x241: v241(0xff) = CONST 
    0x243: v243(0xff) = MUL v241(0xff), v23d(0x1)
    0x244: v244(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v243(0xff)
    0x245: v245 = AND v244(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v23f
    0x248: v248(0x0) = ISZERO v1f7(0x1)
    0x249: v249(0x1) = ISZERO v248(0x0)
    0x24a: v24a(0x1) = MUL v249(0x1), v23d(0x1)
    0x24b: v24b = OR v24a(0x1), v245
    0x24d: SSTORE v237, v24b
    0x24f: STOP 

}

