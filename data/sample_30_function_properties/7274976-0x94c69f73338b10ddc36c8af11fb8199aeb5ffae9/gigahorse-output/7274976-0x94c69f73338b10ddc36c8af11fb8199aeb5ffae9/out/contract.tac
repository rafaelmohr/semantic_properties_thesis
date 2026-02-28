function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x63a8]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x13a8: v13a8(0x63a8) = CONST 
    0x13c8: JUMPI v13a8(0x63a8), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x6da8]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0xb0f7743) = CONST 
    0x3b: v3b = EQ v34, v35(0xb0f7743)
    0x1da8: v1da8(0x6da8) = CONST 
    0x1dc8: JUMPI v1da8(0x6da8), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x77a8, 0x4b]
    =================================
    0x41: v41(0x867904b4) = CONST 
    0x46: v46 = EQ v41(0x867904b4), v34
    0x27a8: v27a8(0x77a8) = CONST 
    0x27c8: JUMPI v27a8(0x77a8), v46

    Begin block 0x77a8
    prev=[0x40], succ=[]
    =================================
    0x77c8: v77c8(0xae) = CONST 
    0x77e8: CALLPRIVATE v77c8(0xae)

    Begin block 0x4b
    prev=[0x40], succ=[0x81a8, 0x56]
    =================================
    0x4c: v4c(0x8da5cb5b) = CONST 
    0x51: v51 = EQ v4c(0x8da5cb5b), v34
    0x31a8: v31a8(0x81a8) = CONST 
    0x31c8: JUMPI v31a8(0x81a8), v51

    Begin block 0x81a8
    prev=[0x4b], succ=[]
    =================================
    0x81c8: v81c8(0xe1) = CONST 
    0x81e8: CALLPRIVATE v81c8(0xe1)

    Begin block 0x56
    prev=[0x4b], succ=[0x8ba8, 0x61]
    =================================
    0x57: v57(0xdd449a83) = CONST 
    0x5c: v5c = EQ v57(0xdd449a83), v34
    0x3ba8: v3ba8(0x8ba8) = CONST 
    0x3bc8: JUMPI v3ba8(0x8ba8), v5c

    Begin block 0x8ba8
    prev=[0x56], succ=[]
    =================================
    0x8bc8: v8bc8(0x11f) = CONST 
    0x8be8: CALLPRIVATE v8bc8(0x11f)

    Begin block 0x61
    prev=[0x56], succ=[0x95a8, 0x6c]
    =================================
    0x62: v62(0xf02d7ef0) = CONST 
    0x67: v67 = EQ v62(0xf02d7ef0), v34
    0x45a8: v45a8(0x95a8) = CONST 
    0x45c8: JUMPI v45a8(0x95a8), v67

    Begin block 0x95a8
    prev=[0x61], succ=[]
    =================================
    0x95c8: v95c8(0x134) = CONST 
    0x95e8: CALLPRIVATE v95c8(0x134)

    Begin block 0x6c
    prev=[0x61], succ=[0x9fa8, 0x77]
    =================================
    0x6d: v6d(0xf2fde38b) = CONST 
    0x72: v72 = EQ v6d(0xf2fde38b), v34
    0x4fa8: v4fa8(0x9fa8) = CONST 
    0x4fc8: JUMPI v4fa8(0x9fa8), v72

    Begin block 0x9fa8
    prev=[0x6c], succ=[]
    =================================
    0x9fc8: v9fc8(0x176) = CONST 
    0x9fe8: CALLPRIVATE v9fc8(0x176)

    Begin block 0x77
    prev=[0x6c], succ=[0x63a8, 0xa9a8]
    =================================
    0x78: v78(0xfc0c546a) = CONST 
    0x7d: v7d = EQ v78(0xfc0c546a), v34
    0x59a8: v59a8(0xa9a8) = CONST 
    0x59c8: JUMPI v59a8(0xa9a8), v7d

    Begin block 0x63a8
    prev=[0x0, 0x77], succ=[]
    =================================
    0x63c8: v63c8(0x82) = CONST 
    0x63e8: CALLPRIVATE v63c8(0x82)

    Begin block 0xa9a8
    prev=[0x77], succ=[]
    =================================
    0xa9c8: va9c8(0x1a4) = CONST 
    0xa9e8: CALLPRIVATE va9c8(0x1a4)

    Begin block 0x6da8
    prev=[0xd], succ=[]
    =================================
    0x6dc8: v6dc8(0x87) = CONST 
    0x6de8: CALLPRIVATE v6dc8(0x87)

}

function allower()() public {
    Begin block 0x11f
    prev=[], succ=[0x127, 0x12b]
    =================================
    0x120: v120 = CALLVALUE 
    0x122: v122 = ISZERO v120
    0x123: v123(0x12b) = CONST 
    0x126: JUMPI v123(0x12b), v122

    Begin block 0x127
    prev=[0x11f], succ=[]
    =================================
    0x127: v127(0x0) = CONST 
    0x12a: REVERT v127(0x0), v127(0x0)

    Begin block 0x12b
    prev=[0x11f], succ=[0x324]
    =================================
    0x12d: v12d(0x933) = CONST 
    0x130: v130(0x324) = CONST 
    0x133: JUMP v130(0x324)

    Begin block 0x324
    prev=[0x12b], succ=[0x933]
    =================================
    0x325: v325(0x3) = CONST 
    0x327: v327 = SLOAD v325(0x3)
    0x328: v328(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33d: v33d = AND v328(0xffffffffffffffffffffffffffffffffffffffff), v327
    0x33f: JUMP v12d(0x933)

    Begin block 0x933
    prev=[0x324], succ=[]
    =================================
    0x934: v934(0x40) = CONST 
    0x937: v937 = MLOAD v934(0x40)
    0x938: v938(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x94f: v94f = AND v33d, v938(0xffffffffffffffffffffffffffffffffffffffff)
    0x951: MSTORE v937, v94f
    0x952: v952 = MLOAD v934(0x40)
    0x956: v956(0x0) = SUB v937, v952
    0x957: v957(0x20) = CONST 
    0x959: v959(0x20) = ADD v957(0x20), v956(0x0)
    0x95b: RETURN v952, v959(0x20)

}

function issued(address)() public {
    Begin block 0x134
    prev=[], succ=[0x13c, 0x140]
    =================================
    0x135: v135 = CALLVALUE 
    0x137: v137 = ISZERO v135
    0x138: v138(0x140) = CONST 
    0x13b: JUMPI v138(0x140), v137

    Begin block 0x13c
    prev=[0x134], succ=[]
    =================================
    0x13c: v13c(0x0) = CONST 
    0x13f: REVERT v13c(0x0), v13c(0x0)

    Begin block 0x140
    prev=[0x134], succ=[0x340]
    =================================
    0x142: v142(0x162) = CONST 
    0x145: v145(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15a: v15a(0x4) = CONST 
    0x15c: v15c = CALLDATALOAD v15a(0x4)
    0x15d: v15d = AND v15c, v145(0xffffffffffffffffffffffffffffffffffffffff)
    0x15e: v15e(0x340) = CONST 
    0x161: JUMP v15e(0x340)

    Begin block 0x340
    prev=[0x140], succ=[0x162]
    =================================
    0x341: v341(0x1) = CONST 
    0x343: v343(0x20) = CONST 
    0x345: MSTORE v343(0x20), v341(0x1)
    0x346: v346(0x0) = CONST 
    0x34a: MSTORE v346(0x0), v15d
    0x34b: v34b(0x40) = CONST 
    0x34e: v34e = SHA3 v346(0x0), v34b(0x40)
    0x34f: v34f = SLOAD v34e
    0x350: v350(0xff) = CONST 
    0x352: v352 = AND v350(0xff), v34f
    0x354: JUMP v142(0x162)

    Begin block 0x162
    prev=[0x340], succ=[]
    =================================
    0x163: v163(0x40) = CONST 
    0x166: v166 = MLOAD v163(0x40)
    0x168: v168 = ISZERO v352
    0x169: v169 = ISZERO v168
    0x16b: MSTORE v166, v169
    0x16c: v16c = MLOAD v163(0x40)
    0x170: v170(0x0) = SUB v166, v16c
    0x171: v171(0x20) = CONST 
    0x173: v173(0x20) = ADD v171(0x20), v170(0x0)
    0x175: RETURN v16c, v173(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x176
    prev=[], succ=[0x17e, 0x182]
    =================================
    0x177: v177 = CALLVALUE 
    0x179: v179 = ISZERO v177
    0x17a: v17a(0x182) = CONST 
    0x17d: JUMPI v17a(0x182), v179

    Begin block 0x17e
    prev=[0x176], succ=[]
    =================================
    0x17e: v17e(0x0) = CONST 
    0x181: REVERT v17e(0x0), v17e(0x0)

    Begin block 0x182
    prev=[0x176], succ=[0x355]
    =================================
    0x184: v184(0x97b) = CONST 
    0x187: v187(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19c: v19c(0x4) = CONST 
    0x19e: v19e = CALLDATALOAD v19c(0x4)
    0x19f: v19f = AND v19e, v187(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a0: v1a0(0x355) = CONST 
    0x1a3: JUMP v1a0(0x355)

    Begin block 0x355
    prev=[0x182], succ=[0x375, 0x379]
    =================================
    0x356: v356(0x0) = CONST 
    0x358: v358 = SLOAD v356(0x0)
    0x359: v359(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36e: v36e = AND v359(0xffffffffffffffffffffffffffffffffffffffff), v358
    0x36f: v36f = CALLER 
    0x370: v370 = EQ v36f, v36e
    0x371: v371(0x379) = CONST 
    0x374: JUMPI v371(0x379), v370

    Begin block 0x375
    prev=[0x355], succ=[]
    =================================
    0x375: v375(0x0) = CONST 
    0x378: REVERT v375(0x0), v375(0x0)

    Begin block 0x379
    prev=[0x355], succ=[0x397, 0x39b]
    =================================
    0x37a: v37a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x390: v390 = AND v19f, v37a(0xffffffffffffffffffffffffffffffffffffffff)
    0x391: v391 = ISZERO v390
    0x392: v392 = ISZERO v391
    0x393: v393(0x39b) = CONST 
    0x396: JUMPI v393(0x39b), v392

    Begin block 0x397
    prev=[0x379], succ=[]
    =================================
    0x397: v397(0x0) = CONST 
    0x39a: REVERT v397(0x0), v397(0x0)

    Begin block 0x39b
    prev=[0x379], succ=[0x97b]
    =================================
    0x39c: v39c(0x0) = CONST 
    0x39f: v39f = SLOAD v39c(0x0)
    0x3a0: v3a0(0x40) = CONST 
    0x3a2: v3a2 = MLOAD v3a0(0x40)
    0x3a3: v3a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ba: v3ba = AND v19f, v3a3(0xffffffffffffffffffffffffffffffffffffffff)
    0x3bd: v3bd = AND v39f, v3a3(0xffffffffffffffffffffffffffffffffffffffff)
    0x3bf: v3bf(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x3e1: LOG3 v3a2, v39c(0x0), v3bf(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v3bd, v3ba
    0x3e2: v3e2(0x0) = CONST 
    0x3e5: v3e5 = SLOAD v3e2(0x0)
    0x3e6: v3e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3fb: v3fb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3e6(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fc: v3fc = AND v3fb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3e5
    0x3fd: v3fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x415: v415 = AND v3fd(0xffffffffffffffffffffffffffffffffffffffff), v19f
    0x419: v419 = OR v415, v3fc
    0x41b: SSTORE v3e2(0x0), v419
    0x41c: JUMP v184(0x97b)

    Begin block 0x97b
    prev=[0x39b], succ=[]
    =================================
    0x97c: STOP 

}

function token()() public {
    Begin block 0x1a4
    prev=[], succ=[0x1ac, 0x1b0]
    =================================
    0x1a5: v1a5 = CALLVALUE 
    0x1a7: v1a7 = ISZERO v1a5
    0x1a8: v1a8(0x1b0) = CONST 
    0x1ab: JUMPI v1a8(0x1b0), v1a7

    Begin block 0x1ac
    prev=[0x1a4], succ=[]
    =================================
    0x1ac: v1ac(0x0) = CONST 
    0x1af: REVERT v1ac(0x0), v1ac(0x0)

    Begin block 0x1b0
    prev=[0x1a4], succ=[0x41d]
    =================================
    0x1b2: v1b2(0x99c) = CONST 
    0x1b5: v1b5(0x41d) = CONST 
    0x1b8: JUMP v1b5(0x41d)

    Begin block 0x41d
    prev=[0x1b0], succ=[0x99c]
    =================================
    0x41e: v41e(0x2) = CONST 
    0x420: v420 = SLOAD v41e(0x2)
    0x421: v421(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x436: v436 = AND v421(0xffffffffffffffffffffffffffffffffffffffff), v420
    0x438: JUMP v1b2(0x99c)

    Begin block 0x99c
    prev=[0x41d], succ=[]
    =================================
    0x99d: v99d(0x40) = CONST 
    0x9a0: v9a0 = MLOAD v99d(0x40)
    0x9a1: v9a1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9b8: v9b8 = AND v436, v9a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x9ba: MSTORE v9a0, v9b8
    0x9bb: v9bb = MLOAD v99d(0x40)
    0x9bf: v9bf(0x0) = SUB v9a0, v9bb
    0x9c0: v9c0(0x20) = CONST 
    0x9c2: v9c2(0x20) = ADD v9c0(0x20), v9bf(0x0)
    0x9c4: RETURN v9bb, v9c2(0x20)

}

function fallback()() public {
    Begin block 0x82
    prev=[], succ=[]
    =================================
    0x83: v83(0x0) = CONST 
    0x86: REVERT v83(0x0), v83(0x0)

}

function issuedCount()() public {
    Begin block 0x87
    prev=[], succ=[0x8f, 0x93]
    =================================
    0x88: v88 = CALLVALUE 
    0x8a: v8a = ISZERO v88
    0x8b: v8b(0x93) = CONST 
    0x8e: JUMPI v8b(0x93), v8a

    Begin block 0x8f
    prev=[0x87], succ=[]
    =================================
    0x8f: v8f(0x0) = CONST 
    0x92: REVERT v8f(0x0), v8f(0x0)

    Begin block 0x93
    prev=[0x87], succ=[0x1b9]
    =================================
    0x95: v95(0x9c) = CONST 
    0x98: v98(0x1b9) = CONST 
    0x9b: JUMP v98(0x1b9)

    Begin block 0x1b9
    prev=[0x93], succ=[0x9c]
    =================================
    0x1ba: v1ba(0x4) = CONST 
    0x1bc: v1bc = SLOAD v1ba(0x4)
    0x1be: JUMP v95(0x9c)

    Begin block 0x9c
    prev=[0x1b9], succ=[]
    =================================
    0x9d: v9d(0x40) = CONST 
    0xa0: va0 = MLOAD v9d(0x40)
    0xa3: MSTORE va0, v1bc
    0xa4: va4 = MLOAD v9d(0x40)
    0xa8: va8(0x0) = SUB va0, va4
    0xa9: va9(0x20) = CONST 
    0xab: vab(0x20) = ADD va9(0x20), va8(0x0)
    0xad: RETURN va4, vab(0x20)

}

function issue(address,uint256)() public {
    Begin block 0xae
    prev=[], succ=[0xb6, 0xba]
    =================================
    0xaf: vaf = CALLVALUE 
    0xb1: vb1 = ISZERO vaf
    0xb2: vb2(0xba) = CONST 
    0xb5: JUMPI vb2(0xba), vb1

    Begin block 0xb6
    prev=[0xae], succ=[]
    =================================
    0xb6: vb6(0x0) = CONST 
    0xb9: REVERT vb6(0x0), vb6(0x0)

    Begin block 0xba
    prev=[0xae], succ=[0x1bf]
    =================================
    0xbc: vbc(0x8ca) = CONST 
    0xbf: vbf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd4: vd4(0x4) = CONST 
    0xd6: vd6 = CALLDATALOAD vd4(0x4)
    0xd7: vd7 = AND vd6, vbf(0xffffffffffffffffffffffffffffffffffffffff)
    0xd8: vd8(0x24) = CONST 
    0xda: vda = CALLDATALOAD vd8(0x24)
    0xdb: vdb(0x1bf) = CONST 
    0xde: JUMP vdb(0x1bf)

    Begin block 0x1bf
    prev=[0xba], succ=[0x1df, 0x1e3]
    =================================
    0x1c0: v1c0(0x0) = CONST 
    0x1c2: v1c2 = SLOAD v1c0(0x0)
    0x1c3: v1c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d8: v1d8 = AND v1c3(0xffffffffffffffffffffffffffffffffffffffff), v1c2
    0x1d9: v1d9 = CALLER 
    0x1da: v1da = EQ v1d9, v1d8
    0x1db: v1db(0x1e3) = CONST 
    0x1de: JUMPI v1db(0x1e3), v1da

    Begin block 0x1df
    prev=[0x1bf], succ=[]
    =================================
    0x1df: v1df(0x0) = CONST 
    0x1e2: REVERT v1df(0x0), v1df(0x0)

    Begin block 0x1e3
    prev=[0x1bf], succ=[0x212, 0x216]
    =================================
    0x1e4: v1e4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1fa: v1fa = AND vd7, v1e4(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fb: v1fb(0x0) = CONST 
    0x1ff: MSTORE v1fb(0x0), v1fa
    0x200: v200(0x1) = CONST 
    0x202: v202(0x20) = CONST 
    0x204: MSTORE v202(0x20), v200(0x1)
    0x205: v205(0x40) = CONST 
    0x208: v208 = SHA3 v1fb(0x0), v205(0x40)
    0x209: v209 = SLOAD v208
    0x20a: v20a(0xff) = CONST 
    0x20c: v20c = AND v20a(0xff), v209
    0x20d: v20d = ISZERO v20c
    0x20e: v20e(0x216) = CONST 
    0x211: JUMPI v20e(0x216), v20d

    Begin block 0x212
    prev=[0x1e3], succ=[]
    =================================
    0x212: v212(0x0) = CONST 
    0x215: REVERT v212(0x0), v212(0x0)

    Begin block 0x216
    prev=[0x1e3], succ=[0x299, 0x29d]
    =================================
    0x217: v217(0x2) = CONST 
    0x219: v219 = SLOAD v217(0x2)
    0x21a: v21a(0x3) = CONST 
    0x21c: v21c = SLOAD v21a(0x3)
    0x21d: v21d(0x40) = CONST 
    0x220: v220 = MLOAD v21d(0x40)
    0x221: v221(0x23b872dd00000000000000000000000000000000000000000000000000000000) = CONST 
    0x243: MSTORE v220, v221(0x23b872dd00000000000000000000000000000000000000000000000000000000)
    0x244: v244(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25b: v25b = AND v244(0xffffffffffffffffffffffffffffffffffffffff), v21c
    0x25c: v25c(0x4) = CONST 
    0x25f: v25f = ADD v220, v25c(0x4)
    0x260: MSTORE v25f, v25b
    0x263: v263 = AND v244(0xffffffffffffffffffffffffffffffffffffffff), vd7
    0x264: v264(0x24) = CONST 
    0x267: v267 = ADD v220, v264(0x24)
    0x268: MSTORE v267, v263
    0x269: v269(0x44) = CONST 
    0x26c: v26c = ADD v220, v269(0x44)
    0x26f: MSTORE v26c, vda
    0x271: v271 = MLOAD v21d(0x40)
    0x275: v275 = AND v219, v244(0xffffffffffffffffffffffffffffffffffffffff)
    0x277: v277(0x23b872dd) = CONST 
    0x27d: v27d(0x64) = CONST 
    0x281: v281 = ADD v220, v27d(0x64)
    0x283: v283(0x20) = CONST 
    0x28a: v28a(0x0) = SUB v220, v271
    0x28b: v28b(0x64) = ADD v28a(0x0), v27d(0x64)
    0x28d: v28d(0x0) = CONST 
    0x291: v291 = EXTCODESIZE v275
    0x292: v292 = ISZERO v291
    0x294: v294 = ISZERO v292
    0x295: v295(0x29d) = CONST 
    0x298: JUMPI v295(0x29d), v294

    Begin block 0x299
    prev=[0x216], succ=[]
    =================================
    0x299: v299(0x0) = CONST 
    0x29c: REVERT v299(0x0), v299(0x0)

    Begin block 0x29d
    prev=[0x216], succ=[0x2a8, 0x2b1]
    =================================
    0x29f: v29f = GAS 
    0x2a0: v2a0 = CALL v29f, v275, v28d(0x0), v271, v28b(0x64), v271, v283(0x20)
    0x2a1: v2a1 = ISZERO v2a0
    0x2a3: v2a3 = ISZERO v2a1
    0x2a4: v2a4(0x2b1) = CONST 
    0x2a7: JUMPI v2a4(0x2b1), v2a3

    Begin block 0x2a8
    prev=[0x29d], succ=[]
    =================================
    0x2a8: v2a8 = RETURNDATASIZE 
    0x2a9: v2a9(0x0) = CONST 
    0x2ac: RETURNDATACOPY v2a9(0x0), v2a9(0x0), v2a8
    0x2ad: v2ad = RETURNDATASIZE 
    0x2ae: v2ae(0x0) = CONST 
    0x2b0: REVERT v2ae(0x0), v2ad

    Begin block 0x2b1
    prev=[0x29d], succ=[0x2c3, 0x2c7]
    =================================
    0x2b6: v2b6(0x40) = CONST 
    0x2b8: v2b8 = MLOAD v2b6(0x40)
    0x2b9: v2b9 = RETURNDATASIZE 
    0x2ba: v2ba(0x20) = CONST 
    0x2bd: v2bd = LT v2b9, v2ba(0x20)
    0x2be: v2be = ISZERO v2bd
    0x2bf: v2bf(0x2c7) = CONST 
    0x2c2: JUMPI v2bf(0x2c7), v2be

    Begin block 0x2c3
    prev=[0x2b1], succ=[]
    =================================
    0x2c3: v2c3(0x0) = CONST 
    0x2c6: REVERT v2c3(0x0), v2c3(0x0)

    Begin block 0x2c7
    prev=[0x2b1], succ=[0x8ca]
    =================================
    0x2ca: v2ca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e1: v2e1 = AND vd7, v2ca(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e2: v2e2(0x0) = CONST 
    0x2e6: MSTORE v2e2(0x0), v2e1
    0x2e7: v2e7(0x1) = CONST 
    0x2e9: v2e9(0x20) = CONST 
    0x2ed: MSTORE v2e9(0x20), v2e7(0x1)
    0x2ee: v2ee(0x40) = CONST 
    0x2f2: v2f2 = SHA3 v2e2(0x0), v2ee(0x40)
    0x2f4: v2f4 = SLOAD v2f2
    0x2f5: v2f5(0xff) = CONST 
    0x2f7: v2f7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2f5(0xff)
    0x2f8: v2f8 = AND v2f7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2f4
    0x2fb: v2fb = OR v2e7(0x1), v2f8
    0x2fd: SSTORE v2f2, v2fb
    0x2fe: v2fe(0x4) = CONST 
    0x301: v301 = SLOAD v2fe(0x4)
    0x304: v304 = ADD vda, v301
    0x306: SSTORE v2fe(0x4), v304
    0x307: JUMP vbc(0x8ca)

    Begin block 0x8ca
    prev=[0x2c7], succ=[]
    =================================
    0x8cb: STOP 

}

function owner()() public {
    Begin block 0xe1
    prev=[], succ=[0xe9, 0xed]
    =================================
    0xe2: ve2 = CALLVALUE 
    0xe4: ve4 = ISZERO ve2
    0xe5: ve5(0xed) = CONST 
    0xe8: JUMPI ve5(0xed), ve4

    Begin block 0xe9
    prev=[0xe1], succ=[]
    =================================
    0xe9: ve9(0x0) = CONST 
    0xec: REVERT ve9(0x0), ve9(0x0)

    Begin block 0xed
    prev=[0xe1], succ=[0x308]
    =================================
    0xef: vef(0x8eb) = CONST 
    0xf2: vf2(0x308) = CONST 
    0xf5: JUMP vf2(0x308)

    Begin block 0x308
    prev=[0xed], succ=[0x8eb]
    =================================
    0x309: v309(0x0) = CONST 
    0x30b: v30b = SLOAD v309(0x0)
    0x30c: v30c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x321: v321 = AND v30c(0xffffffffffffffffffffffffffffffffffffffff), v30b
    0x323: JUMP vef(0x8eb)

    Begin block 0x8eb
    prev=[0x308], succ=[]
    =================================
    0x8ec: v8ec(0x40) = CONST 
    0x8ef: v8ef = MLOAD v8ec(0x40)
    0x8f0: v8f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x907: v907 = AND v321, v8f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x909: MSTORE v8ef, v907
    0x90a: v90a = MLOAD v8ec(0x40)
    0x90e: v90e(0x0) = SUB v8ef, v90a
    0x90f: v90f(0x20) = CONST 
    0x911: v911(0x20) = ADD v90f(0x20), v90e(0x0)
    0x913: RETURN v90a, v911(0x20)

}

