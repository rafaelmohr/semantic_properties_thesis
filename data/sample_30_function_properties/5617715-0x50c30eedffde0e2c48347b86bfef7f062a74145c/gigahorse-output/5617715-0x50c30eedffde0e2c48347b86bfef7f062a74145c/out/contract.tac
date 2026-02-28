function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x784c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x324c: v324c(0x784c) = CONST 
    0x326c: JUMPI v324c(0x784c), v8

    Begin block 0xd
    prev=[0x0], succ=[0x824c, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x16cc9022) = CONST 
    0x3c: v3c = EQ v37(0x16cc9022), v35
    0x3c4c: v3c4c(0x824c) = CONST 
    0x3c6c: JUMPI v3c4c(0x824c), v3c

    Begin block 0x824c
    prev=[0xd], succ=[]
    =================================
    0x826c: v826c(0x83) = CONST 
    0x828c: CALLPRIVATE v826c(0x83)

    Begin block 0x41
    prev=[0xd], succ=[0x8c4c, 0x4c]
    =================================
    0x42: v42(0x2c4e722e) = CONST 
    0x47: v47 = EQ v42(0x2c4e722e), v35
    0x464c: v464c(0x8c4c) = CONST 
    0x466c: JUMPI v464c(0x8c4c), v47

    Begin block 0x8c4c
    prev=[0x41], succ=[]
    =================================
    0x8c6c: v8c6c(0xc6) = CONST 
    0x8c8c: CALLPRIVATE v8c6c(0xc6)

    Begin block 0x4c
    prev=[0x41], succ=[0x964c, 0x57]
    =================================
    0x4d: v4d(0x4042b66f) = CONST 
    0x52: v52 = EQ v4d(0x4042b66f), v35
    0x504c: v504c(0x964c) = CONST 
    0x506c: JUMPI v504c(0x964c), v52

    Begin block 0x964c
    prev=[0x4c], succ=[]
    =================================
    0x966c: v966c(0xf1) = CONST 
    0x968c: CALLPRIVATE v966c(0xf1)

    Begin block 0x57
    prev=[0x4c], succ=[0xa04c, 0x62]
    =================================
    0x58: v58(0x521eb273) = CONST 
    0x5d: v5d = EQ v58(0x521eb273), v35
    0x5a4c: v5a4c(0xa04c) = CONST 
    0x5a6c: JUMPI v5a4c(0xa04c), v5d

    Begin block 0xa04c
    prev=[0x57], succ=[]
    =================================
    0xa06c: va06c(0x11c) = CONST 
    0xa08c: CALLPRIVATE va06c(0x11c)

    Begin block 0x62
    prev=[0x57], succ=[0xaa4c, 0x6d]
    =================================
    0x63: v63(0xec8ac4d8) = CONST 
    0x68: v68 = EQ v63(0xec8ac4d8), v35
    0x644c: v644c(0xaa4c) = CONST 
    0x646c: JUMPI v644c(0xaa4c), v68

    Begin block 0xaa4c
    prev=[0x62], succ=[]
    =================================
    0xaa6c: vaa6c(0x173) = CONST 
    0xaa8c: CALLPRIVATE vaa6c(0x173)

    Begin block 0x6d
    prev=[0x62], succ=[0x784c, 0xb44c]
    =================================
    0x6e: v6e(0xfc0c546a) = CONST 
    0x73: v73 = EQ v6e(0xfc0c546a), v35
    0x6e4c: v6e4c(0xb44c) = CONST 
    0x6e6c: JUMPI v6e4c(0xb44c), v73

    Begin block 0x784c
    prev=[0x0, 0x6d], succ=[]
    =================================
    0x786c: v786c(0x78) = CONST 
    0x788c: CALLPRIVATE v786c(0x78)

    Begin block 0xb44c
    prev=[0x6d], succ=[]
    =================================
    0xb46c: vb46c(0x1a9) = CONST 
    0xb48c: CALLPRIVATE vb46c(0x1a9)

}

function wallet()() public {
    Begin block 0x11c
    prev=[], succ=[0x124, 0x128]
    =================================
    0x11d: v11d = CALLVALUE 
    0x11f: v11f = ISZERO v11d
    0x120: v120(0x128) = CONST 
    0x123: JUMPI v120(0x128), v11f

    Begin block 0x124
    prev=[0x11c], succ=[]
    =================================
    0x124: v124(0x0) = CONST 
    0x127: REVERT v124(0x0), v124(0x0)

    Begin block 0x128
    prev=[0x11c], succ=[0x366]
    =================================
    0x12a: v12a(0x131) = CONST 
    0x12d: v12d(0x366) = CONST 
    0x130: JUMP v12d(0x366)

    Begin block 0x366
    prev=[0x128], succ=[0x131]
    =================================
    0x367: v367(0x1) = CONST 
    0x369: v369(0x0) = CONST 
    0x36c: v36c = SLOAD v367(0x1)
    0x36e: v36e(0x100) = CONST 
    0x371: v371(0x1) = EXP v36e(0x100), v369(0x0)
    0x373: v373 = DIV v36c, v371(0x1)
    0x374: v374(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x389: v389 = AND v374(0xffffffffffffffffffffffffffffffffffffffff), v373
    0x38b: JUMP v12a(0x131)

    Begin block 0x131
    prev=[0x366], succ=[]
    =================================
    0x132: v132(0x40) = CONST 
    0x134: v134 = MLOAD v132(0x40)
    0x137: v137(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14c: v14c = AND v137(0xffffffffffffffffffffffffffffffffffffffff), v389
    0x14d: v14d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x162: v162 = AND v14d(0xffffffffffffffffffffffffffffffffffffffff), v14c
    0x164: MSTORE v134, v162
    0x165: v165(0x20) = CONST 
    0x167: v167 = ADD v165(0x20), v134
    0x16b: v16b(0x40) = CONST 
    0x16d: v16d = MLOAD v16b(0x40)
    0x170: v170(0x20) = SUB v167, v16d
    0x172: RETURN v16d, v170(0x20)

}

function buyTokens(address)() public {
    Begin block 0x173
    prev=[], succ=[0x1a7]
    =================================
    0x174: v174(0x1a7) = CONST 
    0x177: v177(0x4) = CONST 
    0x17a: v17a = CALLDATASIZE 
    0x17b: v17b = SUB v17a, v177(0x4)
    0x17d: v17d = ADD v177(0x4), v17b
    0x181: v181 = CALLDATALOAD v177(0x4)
    0x182: v182(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x197: v197 = AND v182(0xffffffffffffffffffffffffffffffffffffffff), v181
    0x199: v199(0x20) = CONST 
    0x19b: v19b(0x24) = ADD v199(0x20), v177(0x4)
    0x1a3: v1a3(0x200) = CONST 
    0x1a6: CALLPRIVATE v1a3(0x200), v197, v174(0x1a7)

    Begin block 0x1a7
    prev=[0x173], succ=[]
    =================================
    0x1a8: STOP 

}

function token()() public {
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
    prev=[0x1a9], succ=[0x38c]
    =================================
    0x1b7: v1b7(0x1be) = CONST 
    0x1ba: v1ba(0x38c) = CONST 
    0x1bd: JUMP v1ba(0x38c)

    Begin block 0x38c
    prev=[0x1b5], succ=[0x1be]
    =================================
    0x38d: v38d(0x0) = CONST 
    0x391: v391 = SLOAD v38d(0x0)
    0x393: v393(0x100) = CONST 
    0x396: v396(0x1) = EXP v393(0x100), v38d(0x0)
    0x398: v398 = DIV v391, v396(0x1)
    0x399: v399(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ae: v3ae = AND v399(0xffffffffffffffffffffffffffffffffffffffff), v398
    0x3b0: JUMP v1b7(0x1be)

    Begin block 0x1be
    prev=[0x38c], succ=[]
    =================================
    0x1bf: v1bf(0x40) = CONST 
    0x1c1: v1c1 = MLOAD v1bf(0x40)
    0x1c4: v1c4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d9: v1d9 = AND v1c4(0xffffffffffffffffffffffffffffffffffffffff), v3ae
    0x1da: v1da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ef: v1ef = AND v1da(0xffffffffffffffffffffffffffffffffffffffff), v1d9
    0x1f1: MSTORE v1c1, v1ef
    0x1f2: v1f2(0x20) = CONST 
    0x1f4: v1f4 = ADD v1f2(0x20), v1c1
    0x1f8: v1f8(0x40) = CONST 
    0x1fa: v1fa = MLOAD v1f8(0x40)
    0x1fd: v1fd(0x20) = SUB v1f4, v1fa
    0x1ff: RETURN v1fa, v1fd(0x20)

}

function 0x200(v200arg0, v200arg1) private {
    Begin block 0x200
    prev=[], succ=[0x210]
    =================================
    0x201: v201(0x0) = CONST 
    0x204: v204 = CALLVALUE 
    0x207: v207(0x210) = CONST 
    0x20c: v20c(0x3b1) = CONST 
    0x20f: CALLPRIVATE v20c(0x3b1), v204, v200arg0, v207(0x210)

    Begin block 0x210
    prev=[0x200], succ=[0x219]
    =================================
    0x211: v211(0x219) = CONST 
    0x215: v215(0x401) = CONST 
    0x218: v218_0 = CALLPRIVATE v215(0x401), v204, v211(0x219)

    Begin block 0x219
    prev=[0x210], succ=[0x230]
    =================================
    0x21c: v21c(0x230) = CONST 
    0x220: v220(0x3) = CONST 
    0x222: v222 = SLOAD v220(0x3)
    0x223: v223(0x41f) = CONST 
    0x229: v229(0xffffffff) = CONST 
    0x22e: v22e(0x41f) = AND v229(0xffffffff), v223(0x41f)
    0x22f: v22f_0 = CALLPRIVATE v22e(0x41f), v204, v222, v21c(0x230)

    Begin block 0x230
    prev=[0x219], succ=[0x240]
    =================================
    0x231: v231(0x3) = CONST 
    0x235: SSTORE v231(0x3), v22f_0
    0x237: v237(0x240) = CONST 
    0x23c: v23c(0x43b) = CONST 
    0x23f: CALLPRIVATE v23c(0x43b), v218_0, v200arg0, v237(0x240)

    Begin block 0x240
    prev=[0x230], succ=[0x2b5]
    =================================
    0x242: v242(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x257: v257 = AND v242(0xffffffffffffffffffffffffffffffffffffffff), v200arg0
    0x258: v258 = CALLER 
    0x259: v259(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26e: v26e = AND v259(0xffffffffffffffffffffffffffffffffffffffff), v258
    0x26f: v26f(0x623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18) = CONST 
    0x292: v292(0x40) = CONST 
    0x294: v294 = MLOAD v292(0x40)
    0x298: MSTORE v294, v204
    0x299: v299(0x20) = CONST 
    0x29b: v29b = ADD v299(0x20), v294
    0x29e: MSTORE v29b, v218_0
    0x29f: v29f(0x20) = CONST 
    0x2a1: v2a1 = ADD v29f(0x20), v29b
    0x2a6: v2a6(0x40) = CONST 
    0x2a8: v2a8 = MLOAD v2a6(0x40)
    0x2ab: v2ab(0x40) = SUB v2a1, v2a8
    0x2ad: LOG3 v2a8, v2ab(0x40), v26f(0x623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18), v26e, v257
    0x2ae: v2ae(0x2b5) = CONST 
    0x2b1: v2b1(0x549) = CONST 
    0x2b4: CALLPRIVATE v2b1(0x549), v2ae(0x2b5)

    Begin block 0x2b5
    prev=[0x240], succ=[]
    =================================
    0x2b9: RETURNPRIVATE v200arg1

}

function 0x3b1(v3b1arg0, v3b1arg1, v3b1arg2) private {
    Begin block 0x3b1
    prev=[], succ=[0x3e9, 0x3ed]
    =================================
    0x3b2: v3b2(0x0) = CONST 
    0x3b4: v3b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c9: v3c9(0x0) = AND v3b4(0xffffffffffffffffffffffffffffffffffffffff), v3b2(0x0)
    0x3cb: v3cb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3e0: v3e0 = AND v3cb(0xffffffffffffffffffffffffffffffffffffffff), v3b1arg1
    0x3e1: v3e1 = EQ v3e0, v3c9(0x0)
    0x3e2: v3e2 = ISZERO v3e1
    0x3e3: v3e3 = ISZERO v3e2
    0x3e4: v3e4 = ISZERO v3e3
    0x3e5: v3e5(0x3ed) = CONST 
    0x3e8: JUMPI v3e5(0x3ed), v3e4

    Begin block 0x3e9
    prev=[0x3b1], succ=[]
    =================================
    0x3e9: v3e9(0x0) = CONST 
    0x3ec: REVERT v3e9(0x0), v3e9(0x0)

    Begin block 0x3ed
    prev=[0x3b1], succ=[0x3f9, 0x3fd]
    =================================
    0x3ee: v3ee(0x0) = CONST 
    0x3f1: v3f1 = EQ v3b1arg0, v3ee(0x0)
    0x3f2: v3f2 = ISZERO v3f1
    0x3f3: v3f3 = ISZERO v3f2
    0x3f4: v3f4 = ISZERO v3f3
    0x3f5: v3f5(0x3fd) = CONST 
    0x3f8: JUMPI v3f5(0x3fd), v3f4

    Begin block 0x3f9
    prev=[0x3ed], succ=[]
    =================================
    0x3f9: v3f9(0x0) = CONST 
    0x3fc: REVERT v3f9(0x0), v3f9(0x0)

    Begin block 0x3fd
    prev=[0x3ed], succ=[]
    =================================
    0x400: RETURNPRIVATE v3b1arg2

}

function 0x401(v401arg0, v401arg1) private {
    Begin block 0x401
    prev=[], succ=[0x5b4B0x401]
    =================================
    0x402: v402(0x0) = CONST 
    0x404: v404(0x418) = CONST 
    0x407: v407(0x2) = CONST 
    0x409: v409 = SLOAD v407(0x2)
    0x40b: v40b(0x5b4) = CONST 
    0x411: v411(0xffffffff) = CONST 
    0x416: v416(0x5b4) = AND v411(0xffffffff), v40b(0x5b4)
    0x417: JUMP v416(0x5b4)

    Begin block 0x5b4B0x401
    prev=[0x401], succ=[0x5bfB0x401, 0x5c7B0x401]
    =================================
    0x5b5S0x401: v5b5V401(0x0) = CONST 
    0x5b9S0x401: v5b9V401 = EQ v401arg0, v5b5V401(0x0)
    0x5baS0x401: v5baV401 = ISZERO v5b9V401
    0x5bbS0x401: v5bbV401(0x5c7) = CONST 
    0x5beS0x401: JUMPI v5bbV401(0x5c7), v5baV401

    Begin block 0x5bfB0x401
    prev=[0x5b4B0x401], succ=[0x18ecB0x401]
    =================================
    0x5bfS0x401: v5bfV401(0x0) = CONST 
    0x5c3S0x401: v5c3V401(0x18ec) = CONST 
    0x5c6S0x401: JUMP v5c3V401(0x18ec)

    Begin block 0x18ecB0x401
    prev=[0x5bfB0x401], succ=[0x418]
    =================================
    0x18f1S0x401: JUMP v404(0x418)

    Begin block 0x418
    prev=[0x18ecB0x401, 0x1911B0x401], succ=[]
    =================================
    0x401S0x418_0: v417_0V418_0 = PHI v5bfV401(0x0), v5caV401
    0x41e: RETURNPRIVATE v401arg1, v417_0V418_0

    Begin block 0x5c7B0x401
    prev=[0x5b4B0x401], succ=[0x5d8B0x401, 0x5d7B0x401]
    =================================
    0x5caS0x401: v5caV401 = MUL v401arg0, v409
    0x5d1S0x401: v5d1V401 = ISZERO v401arg0
    0x5d2S0x401: v5d2V401 = ISZERO v5d1V401
    0x5d3S0x401: v5d3V401(0x5d8) = CONST 
    0x5d6S0x401: JUMPI v5d3V401(0x5d8), v5d2V401

    Begin block 0x5d8B0x401
    prev=[0x5c7B0x401], succ=[0x5e2B0x401, 0x5e1B0x401]
    =================================
    0x5d9S0x401: v5d9V401 = DIV v5caV401, v401arg0
    0x5daS0x401: v5daV401 = EQ v5d9V401, v409
    0x5dbS0x401: v5dbV401 = ISZERO v5daV401
    0x5dcS0x401: v5dcV401 = ISZERO v5dbV401
    0x5ddS0x401: v5ddV401(0x5e2) = CONST 
    0x5e0S0x401: JUMPI v5ddV401(0x5e2), v5dcV401

    Begin block 0x5e2B0x401
    prev=[0x5d8B0x401], succ=[0x1911B0x401]
    =================================
    0xc46S0x401: vc46V401(0x1911) = CONST 
    0xc66S0x401: JUMP vc46V401(0x1911)

    Begin block 0x1911B0x401
    prev=[0x5e2B0x401], succ=[0x418]
    =================================
    0x1916S0x401: JUMP v404(0x418)

    Begin block 0x5e1B0x401
    prev=[0x5d8B0x401], succ=[]
    =================================
    0x5e1S0x401: THROW 

    Begin block 0x5d7B0x401
    prev=[0x5c7B0x401], succ=[]
    =================================
    0x5d7S0x401: THROW 

}

function 0x41f(v41farg0, v41farg1, v41farg2) private {
    Begin block 0x41f
    prev=[], succ=[0x431, 0x432]
    =================================
    0x420: v420(0x0) = CONST 
    0x424: v424 = ADD v41farg1, v41farg0
    0x429: v429 = LT v424, v41farg1
    0x42a: v42a = ISZERO v429
    0x42b: v42b = ISZERO v42a
    0x42c: v42c = ISZERO v42b
    0x42d: v42d(0x432) = CONST 
    0x430: JUMPI v42d(0x432), v42c

    Begin block 0x431
    prev=[0x41f], succ=[]
    =================================
    0x431: THROW 

    Begin block 0x432
    prev=[0x41f], succ=[]
    =================================
    0x43a: RETURNPRIVATE v41farg2, v424

}

function 0x43b(v43barg0, v43barg1, v43barg2) private {
    Begin block 0x43b
    prev=[], succ=[0x4fb, 0x4ff]
    =================================
    0x43c: v43c(0x0) = CONST 
    0x440: v440 = SLOAD v43c(0x0)
    0x442: v442(0x100) = CONST 
    0x445: v445(0x1) = EXP v442(0x100), v43c(0x0)
    0x447: v447 = DIV v440, v445(0x1)
    0x448: v448(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x45d: v45d = AND v448(0xffffffffffffffffffffffffffffffffffffffff), v447
    0x45e: v45e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x473: v473 = AND v45e(0xffffffffffffffffffffffffffffffffffffffff), v45d
    0x474: v474(0x40c10f19) = CONST 
    0x47b: v47b(0x40) = CONST 
    0x47d: v47d = MLOAD v47b(0x40)
    0x47f: v47f(0xffffffff) = CONST 
    0x484: v484(0x40c10f19) = AND v47f(0xffffffff), v474(0x40c10f19)
    0x485: v485(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x4a3: v4a3(0x40c10f1900000000000000000000000000000000000000000000000000000000) = MUL v485(0x100000000000000000000000000000000000000000000000000000000), v484(0x40c10f19)
    0x4a5: MSTORE v47d, v4a3(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0x4a6: v4a6(0x4) = CONST 
    0x4a8: v4a8 = ADD v4a6(0x4), v47d
    0x4ab: v4ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4c0: v4c0 = AND v4ab(0xffffffffffffffffffffffffffffffffffffffff), v43barg1
    0x4c1: v4c1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4d6: v4d6 = AND v4c1(0xffffffffffffffffffffffffffffffffffffffff), v4c0
    0x4d8: MSTORE v4a8, v4d6
    0x4d9: v4d9(0x20) = CONST 
    0x4db: v4db = ADD v4d9(0x20), v4a8
    0x4de: MSTORE v4db, v43barg0
    0x4df: v4df(0x20) = CONST 
    0x4e1: v4e1 = ADD v4df(0x20), v4db
    0x4e6: v4e6(0x20) = CONST 
    0x4e8: v4e8(0x40) = CONST 
    0x4ea: v4ea = MLOAD v4e8(0x40)
    0x4ed: v4ed(0x44) = SUB v4e1, v4ea
    0x4ef: v4ef(0x0) = CONST 
    0x4f3: v4f3 = EXTCODESIZE v473
    0x4f4: v4f4 = ISZERO v4f3
    0x4f6: v4f6 = ISZERO v4f4
    0x4f7: v4f7(0x4ff) = CONST 
    0x4fa: JUMPI v4f7(0x4ff), v4f6

    Begin block 0x4fb
    prev=[0x43b], succ=[]
    =================================
    0x4fb: v4fb(0x0) = CONST 
    0x4fe: REVERT v4fb(0x0), v4fb(0x0)

    Begin block 0x4ff
    prev=[0x43b], succ=[0x50a, 0x513]
    =================================
    0x501: v501 = GAS 
    0x502: v502 = CALL v501, v473, v4ef(0x0), v4ea, v4ed(0x44), v4ea, v4e6(0x20)
    0x503: v503 = ISZERO v502
    0x505: v505 = ISZERO v503
    0x506: v506(0x513) = CONST 
    0x509: JUMPI v506(0x513), v505

    Begin block 0x50a
    prev=[0x4ff], succ=[]
    =================================
    0x50a: v50a = RETURNDATASIZE 
    0x50b: v50b(0x0) = CONST 
    0x50e: RETURNDATACOPY v50b(0x0), v50b(0x0), v50a
    0x50f: v50f = RETURNDATASIZE 
    0x510: v510(0x0) = CONST 
    0x512: REVERT v510(0x0), v50f

    Begin block 0x513
    prev=[0x4ff], succ=[0x525, 0x529]
    =================================
    0x518: v518(0x40) = CONST 
    0x51a: v51a = MLOAD v518(0x40)
    0x51b: v51b = RETURNDATASIZE 
    0x51c: v51c(0x20) = CONST 
    0x51f: v51f = LT v51b, v51c(0x20)
    0x520: v520 = ISZERO v51f
    0x521: v521(0x529) = CONST 
    0x524: JUMPI v521(0x529), v520

    Begin block 0x525
    prev=[0x513], succ=[]
    =================================
    0x525: v525(0x0) = CONST 
    0x528: REVERT v525(0x0), v525(0x0)

    Begin block 0x529
    prev=[0x513], succ=[0x541, 0x545]
    =================================
    0x52b: v52b = ADD v51a, v51b
    0x52f: v52f = MLOAD v51a
    0x531: v531(0x20) = CONST 
    0x533: v533 = ADD v531(0x20), v51a
    0x53b: v53b = ISZERO v52f
    0x53c: v53c = ISZERO v53b
    0x53d: v53d(0x545) = CONST 
    0x540: JUMPI v53d(0x545), v53c

    Begin block 0x541
    prev=[0x529], succ=[]
    =================================
    0x541: v541(0x0) = CONST 
    0x544: REVERT v541(0x0), v541(0x0)

    Begin block 0x545
    prev=[0x529], succ=[]
    =================================
    0x548: RETURNPRIVATE v43barg2

}

function 0x549(v549arg0) private {
    Begin block 0x549
    prev=[], succ=[0x5a8, 0x5b1]
    =================================
    0x54a: v54a(0x1) = CONST 
    0x54c: v54c(0x0) = CONST 
    0x54f: v54f = SLOAD v54a(0x1)
    0x551: v551(0x100) = CONST 
    0x554: v554(0x1) = EXP v551(0x100), v54c(0x0)
    0x556: v556 = DIV v54f, v554(0x1)
    0x557: v557(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x56c: v56c = AND v557(0xffffffffffffffffffffffffffffffffffffffff), v556
    0x56d: v56d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x582: v582 = AND v56d(0xffffffffffffffffffffffffffffffffffffffff), v56c
    0x583: v583(0x8fc) = CONST 
    0x586: v586 = CALLVALUE 
    0x589: v589 = ISZERO v586
    0x58a: v58a = MUL v589, v583(0x8fc)
    0x58c: v58c(0x40) = CONST 
    0x58e: v58e = MLOAD v58c(0x40)
    0x58f: v58f(0x0) = CONST 
    0x591: v591(0x40) = CONST 
    0x593: v593 = MLOAD v591(0x40)
    0x596: v596(0x0) = SUB v58e, v593
    0x59b: v59b = CALL v58a, v582, v586, v593, v596(0x0), v593, v58f(0x0)
    0x5a1: v5a1 = ISZERO v59b
    0x5a3: v5a3 = ISZERO v5a1
    0x5a4: v5a4(0x5b1) = CONST 
    0x5a7: JUMPI v5a4(0x5b1), v5a3

    Begin block 0x5a8
    prev=[0x549], succ=[]
    =================================
    0x5a8: v5a8 = RETURNDATASIZE 
    0x5a9: v5a9(0x0) = CONST 
    0x5ac: RETURNDATACOPY v5a9(0x0), v5a9(0x0), v5a8
    0x5ad: v5ad = RETURNDATASIZE 
    0x5ae: v5ae(0x0) = CONST 
    0x5b0: REVERT v5ae(0x0), v5ad

    Begin block 0x5b1
    prev=[0x549], succ=[]
    =================================
    0x5b3: RETURNPRIVATE v549arg0

}

function fallback()() public {
    Begin block 0x78
    prev=[], succ=[0x81]
    =================================
    0x79: v79(0x81) = CONST 
    0x7c: v7c = CALLER 
    0x7d: v7d(0x200) = CONST 
    0x80: CALLPRIVATE v7d(0x200), v7c, v79(0x81)

    Begin block 0x81
    prev=[0x78], succ=[]
    =================================
    0x82: STOP 

}

function _newWallet(address)() public {
    Begin block 0x83
    prev=[], succ=[0x8b, 0x8f]
    =================================
    0x84: v84 = CALLVALUE 
    0x86: v86 = ISZERO v84
    0x87: v87(0x8f) = CONST 
    0x8a: JUMPI v87(0x8f), v86

    Begin block 0x8b
    prev=[0x83], succ=[]
    =================================
    0x8b: v8b(0x0) = CONST 
    0x8e: REVERT v8b(0x0), v8b(0x0)

    Begin block 0x8f
    prev=[0x83], succ=[0x2ba]
    =================================
    0x91: v91(0xc4) = CONST 
    0x94: v94(0x4) = CONST 
    0x97: v97 = CALLDATASIZE 
    0x98: v98 = SUB v97, v94(0x4)
    0x9a: v9a = ADD v94(0x4), v98
    0x9e: v9e = CALLDATALOAD v94(0x4)
    0x9f: v9f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb4: vb4 = AND v9f(0xffffffffffffffffffffffffffffffffffffffff), v9e
    0xb6: vb6(0x20) = CONST 
    0xb8: vb8(0x24) = ADD vb6(0x20), v94(0x4)
    0xc0: vc0(0x2ba) = CONST 
    0xc3: JUMP vc0(0x2ba)

    Begin block 0x2ba
    prev=[0x8f], succ=[0x312, 0x316]
    =================================
    0x2bb: v2bb(0x1) = CONST 
    0x2bd: v2bd(0x0) = CONST 
    0x2c0: v2c0 = SLOAD v2bb(0x1)
    0x2c2: v2c2(0x100) = CONST 
    0x2c5: v2c5(0x1) = EXP v2c2(0x100), v2bd(0x0)
    0x2c7: v2c7 = DIV v2c0, v2c5(0x1)
    0x2c8: v2c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2dd: v2dd = AND v2c8(0xffffffffffffffffffffffffffffffffffffffff), v2c7
    0x2de: v2de(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f3: v2f3 = AND v2de(0xffffffffffffffffffffffffffffffffffffffff), v2dd
    0x2f4: v2f4 = CALLER 
    0x2f5: v2f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30a: v30a = AND v2f5(0xffffffffffffffffffffffffffffffffffffffff), v2f4
    0x30b: v30b = EQ v30a, v2f3
    0x30c: v30c = ISZERO v30b
    0x30d: v30d = ISZERO v30c
    0x30e: v30e(0x316) = CONST 
    0x311: JUMPI v30e(0x316), v30d

    Begin block 0x312
    prev=[0x2ba], succ=[]
    =================================
    0x312: v312(0x0) = CONST 
    0x315: REVERT v312(0x0), v312(0x0)

    Begin block 0x316
    prev=[0x2ba], succ=[0xc4]
    =================================
    0x318: v318(0x1) = CONST 
    0x31a: v31a(0x0) = CONST 
    0x31c: v31c(0x100) = CONST 
    0x31f: v31f(0x1) = EXP v31c(0x100), v31a(0x0)
    0x321: v321 = SLOAD v318(0x1)
    0x323: v323(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x338: v338(0xffffffffffffffffffffffffffffffffffffffff) = MUL v323(0xffffffffffffffffffffffffffffffffffffffff), v31f(0x1)
    0x339: v339(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v338(0xffffffffffffffffffffffffffffffffffffffff)
    0x33a: v33a = AND v339(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v321
    0x33d: v33d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x352: v352 = AND v33d(0xffffffffffffffffffffffffffffffffffffffff), vb4
    0x353: v353 = MUL v352, v31f(0x1)
    0x354: v354 = OR v353, v33a
    0x356: SSTORE v318(0x1), v354
    0x359: JUMP v91(0xc4)

    Begin block 0xc4
    prev=[0x316], succ=[]
    =================================
    0xc5: STOP 

}

function rate()() public {
    Begin block 0xc6
    prev=[], succ=[0xce, 0xd2]
    =================================
    0xc7: vc7 = CALLVALUE 
    0xc9: vc9 = ISZERO vc7
    0xca: vca(0xd2) = CONST 
    0xcd: JUMPI vca(0xd2), vc9

    Begin block 0xce
    prev=[0xc6], succ=[]
    =================================
    0xce: vce(0x0) = CONST 
    0xd1: REVERT vce(0x0), vce(0x0)

    Begin block 0xd2
    prev=[0xc6], succ=[0x35a]
    =================================
    0xd4: vd4(0xdb) = CONST 
    0xd7: vd7(0x35a) = CONST 
    0xda: JUMP vd7(0x35a)

    Begin block 0x35a
    prev=[0xd2], succ=[0xdb]
    =================================
    0x35b: v35b(0x2) = CONST 
    0x35d: v35d = SLOAD v35b(0x2)
    0x35f: JUMP vd4(0xdb)

    Begin block 0xdb
    prev=[0x35a], succ=[]
    =================================
    0xdc: vdc(0x40) = CONST 
    0xde: vde = MLOAD vdc(0x40)
    0xe2: MSTORE vde, v35d
    0xe3: ve3(0x20) = CONST 
    0xe5: ve5 = ADD ve3(0x20), vde
    0xe9: ve9(0x40) = CONST 
    0xeb: veb = MLOAD ve9(0x40)
    0xee: vee(0x20) = SUB ve5, veb
    0xf0: RETURN veb, vee(0x20)

}

function weiRaised()() public {
    Begin block 0xf1
    prev=[], succ=[0xf9, 0xfd]
    =================================
    0xf2: vf2 = CALLVALUE 
    0xf4: vf4 = ISZERO vf2
    0xf5: vf5(0xfd) = CONST 
    0xf8: JUMPI vf5(0xfd), vf4

    Begin block 0xf9
    prev=[0xf1], succ=[]
    =================================
    0xf9: vf9(0x0) = CONST 
    0xfc: REVERT vf9(0x0), vf9(0x0)

    Begin block 0xfd
    prev=[0xf1], succ=[0x360]
    =================================
    0xff: vff(0x106) = CONST 
    0x102: v102(0x360) = CONST 
    0x105: JUMP v102(0x360)

    Begin block 0x360
    prev=[0xfd], succ=[0x106]
    =================================
    0x361: v361(0x3) = CONST 
    0x363: v363 = SLOAD v361(0x3)
    0x365: JUMP vff(0x106)

    Begin block 0x106
    prev=[0x360], succ=[]
    =================================
    0x107: v107(0x40) = CONST 
    0x109: v109 = MLOAD v107(0x40)
    0x10d: MSTORE v109, v363
    0x10e: v10e(0x20) = CONST 
    0x110: v110 = ADD v10e(0x20), v109
    0x114: v114(0x40) = CONST 
    0x116: v116 = MLOAD v114(0x40)
    0x119: v119(0x20) = SUB v110, v116
    0x11b: RETURN v116, v119(0x20)

}

