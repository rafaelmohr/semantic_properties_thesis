function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x3577c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x2677c: v2677c(0x3577c) = CONST 
    0x2679c: JUMPI v2677c(0x3577c), v8

    Begin block 0xd
    prev=[0x0], succ=[0x3617c, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x2717c: v2717c(0x3617c) = CONST 
    0x2719c: JUMPI v2717c(0x3617c), v3c

    Begin block 0x3617c
    prev=[0xd], succ=[]
    =================================
    0x3619c: v3619c(0x4d1) = CONST 
    0x361bc: CALLPRIVATE v3619c(0x4d1)

    Begin block 0x41
    prev=[0xd], succ=[0x36b7c, 0x4c]
    =================================
    0x42: v42(0x95ea7b3) = CONST 
    0x47: v47 = EQ v42(0x95ea7b3), v35
    0x27b7c: v27b7c(0x36b7c) = CONST 
    0x27b9c: JUMPI v27b7c(0x36b7c), v47

    Begin block 0x36b7c
    prev=[0x41], succ=[]
    =================================
    0x36b9c: v36b9c(0x561) = CONST 
    0x36bbc: CALLPRIVATE v36b9c(0x561)

    Begin block 0x4c
    prev=[0x41], succ=[0x3757c, 0x57]
    =================================
    0x4d: v4d(0x18160ddd) = CONST 
    0x52: v52 = EQ v4d(0x18160ddd), v35
    0x2857c: v2857c(0x3757c) = CONST 
    0x2859c: JUMPI v2857c(0x3757c), v52

    Begin block 0x3757c
    prev=[0x4c], succ=[]
    =================================
    0x3759c: v3759c(0x5c6) = CONST 
    0x375bc: CALLPRIVATE v3759c(0x5c6)

    Begin block 0x57
    prev=[0x4c], succ=[0x37f7c, 0x62]
    =================================
    0x58: v58(0x23b872dd) = CONST 
    0x5d: v5d = EQ v58(0x23b872dd), v35
    0x28f7c: v28f7c(0x37f7c) = CONST 
    0x28f9c: JUMPI v28f7c(0x37f7c), v5d

    Begin block 0x37f7c
    prev=[0x57], succ=[]
    =================================
    0x37f9c: v37f9c(0x5f1) = CONST 
    0x37fbc: CALLPRIVATE v37f9c(0x5f1)

    Begin block 0x62
    prev=[0x57], succ=[0x3897c, 0x6d]
    =================================
    0x63: v63(0x253a96e9) = CONST 
    0x68: v68 = EQ v63(0x253a96e9), v35
    0x2997c: v2997c(0x3897c) = CONST 
    0x2999c: JUMPI v2997c(0x3897c), v68

    Begin block 0x3897c
    prev=[0x62], succ=[]
    =================================
    0x3899c: v3899c(0x676) = CONST 
    0x389bc: CALLPRIVATE v3899c(0x676)

    Begin block 0x6d
    prev=[0x62], succ=[0x3937c, 0x78]
    =================================
    0x6e: v6e(0x313ce567) = CONST 
    0x73: v73 = EQ v6e(0x313ce567), v35
    0x2a37c: v2a37c(0x3937c) = CONST 
    0x2a39c: JUMPI v2a37c(0x3937c), v73

    Begin block 0x3937c
    prev=[0x6d], succ=[]
    =================================
    0x3939c: v3939c(0x680) = CONST 
    0x393bc: CALLPRIVATE v3939c(0x680)

    Begin block 0x78
    prev=[0x6d], succ=[0x39d7c, 0x83]
    =================================
    0x79: v79(0x355274ea) = CONST 
    0x7e: v7e = EQ v79(0x355274ea), v35
    0x2ad7c: v2ad7c(0x39d7c) = CONST 
    0x2ad9c: JUMPI v2ad7c(0x39d7c), v7e

    Begin block 0x39d7c
    prev=[0x78], succ=[]
    =================================
    0x39d9c: v39d9c(0x6b7) = CONST 
    0x39dbc: CALLPRIVATE v39d9c(0x6b7)

    Begin block 0x83
    prev=[0x78], succ=[0x3a77c, 0x8e]
    =================================
    0x84: v84(0x518ab2a8) = CONST 
    0x89: v89 = EQ v84(0x518ab2a8), v35
    0x2b77c: v2b77c(0x3a77c) = CONST 
    0x2b79c: JUMPI v2b77c(0x3a77c), v89

    Begin block 0x3a77c
    prev=[0x83], succ=[]
    =================================
    0x3a79c: v3a79c(0x6e2) = CONST 
    0x3a7bc: CALLPRIVATE v3a79c(0x6e2)

    Begin block 0x8e
    prev=[0x83], succ=[0x3b17c, 0x99]
    =================================
    0x8f: v8f(0x66188463) = CONST 
    0x94: v94 = EQ v8f(0x66188463), v35
    0x2c17c: v2c17c(0x3b17c) = CONST 
    0x2c19c: JUMPI v2c17c(0x3b17c), v94

    Begin block 0x3b17c
    prev=[0x8e], succ=[]
    =================================
    0x3b19c: v3b19c(0x70d) = CONST 
    0x3b1bc: CALLPRIVATE v3b19c(0x70d)

    Begin block 0x99
    prev=[0x8e], succ=[0x3bb7c, 0xa4]
    =================================
    0x9a: v9a(0x70a08231) = CONST 
    0x9f: v9f = EQ v9a(0x70a08231), v35
    0x2cb7c: v2cb7c(0x3bb7c) = CONST 
    0x2cb9c: JUMPI v2cb7c(0x3bb7c), v9f

    Begin block 0x3bb7c
    prev=[0x99], succ=[]
    =================================
    0x3bb9c: v3bb9c(0x772) = CONST 
    0x3bbbc: CALLPRIVATE v3bb9c(0x772)

    Begin block 0xa4
    prev=[0x99], succ=[0x3c57c, 0xaf]
    =================================
    0xa5: va5(0x89311e6f) = CONST 
    0xaa: vaa = EQ va5(0x89311e6f), v35
    0x2d57c: v2d57c(0x3c57c) = CONST 
    0x2d59c: JUMPI v2d57c(0x3c57c), vaa

    Begin block 0x3c57c
    prev=[0xa4], succ=[]
    =================================
    0x3c59c: v3c59c(0x7c9) = CONST 
    0x3c5bc: CALLPRIVATE v3c59c(0x7c9)

    Begin block 0xaf
    prev=[0xa4], succ=[0x3cf7c, 0xba]
    =================================
    0xb0: vb0(0x8b7afe2e) = CONST 
    0xb5: vb5 = EQ vb0(0x8b7afe2e), v35
    0x2df7c: v2df7c(0x3cf7c) = CONST 
    0x2df9c: JUMPI v2df7c(0x3cf7c), vb5

    Begin block 0x3cf7c
    prev=[0xaf], succ=[]
    =================================
    0x3cf9c: v3cf9c(0x7e0) = CONST 
    0x3cfbc: CALLPRIVATE v3cf9c(0x7e0)

    Begin block 0xba
    prev=[0xaf], succ=[0x3d97c, 0xc5]
    =================================
    0xbb: vbb(0x8da5cb5b) = CONST 
    0xc0: vc0 = EQ vbb(0x8da5cb5b), v35
    0x2e97c: v2e97c(0x3d97c) = CONST 
    0x2e99c: JUMPI v2e97c(0x3d97c), vc0

    Begin block 0x3d97c
    prev=[0xba], succ=[]
    =================================
    0x3d99c: v3d99c(0x80b) = CONST 
    0x3d9bc: CALLPRIVATE v3d99c(0x80b)

    Begin block 0xc5
    prev=[0xba], succ=[0x3e37c, 0xd0]
    =================================
    0xc6: vc6(0x903a3ef6) = CONST 
    0xcb: vcb = EQ vc6(0x903a3ef6), v35
    0x2f37c: v2f37c(0x3e37c) = CONST 
    0x2f39c: JUMPI v2f37c(0x3e37c), vcb

    Begin block 0x3e37c
    prev=[0xc5], succ=[]
    =================================
    0x3e39c: v3e39c(0x862) = CONST 
    0x3e3bc: CALLPRIVATE v3e39c(0x862)

    Begin block 0xd0
    prev=[0xc5], succ=[0x3ed7c, 0xdb]
    =================================
    0xd1: vd1(0x95d89b41) = CONST 
    0xd6: vd6 = EQ vd1(0x95d89b41), v35
    0x2fd7c: v2fd7c(0x3ed7c) = CONST 
    0x2fd9c: JUMPI v2fd7c(0x3ed7c), vd6

    Begin block 0x3ed7c
    prev=[0xd0], succ=[]
    =================================
    0x3ed9c: v3ed9c(0x879) = CONST 
    0x3edbc: CALLPRIVATE v3ed9c(0x879)

    Begin block 0xdb
    prev=[0xd0], succ=[0x3f77c, 0xe6]
    =================================
    0xdc: vdc(0xa9059cbb) = CONST 
    0xe1: ve1 = EQ vdc(0xa9059cbb), v35
    0x3077c: v3077c(0x3f77c) = CONST 
    0x3079c: JUMPI v3077c(0x3f77c), ve1

    Begin block 0x3f77c
    prev=[0xdb], succ=[]
    =================================
    0x3f79c: v3f79c(0x909) = CONST 
    0x3f7bc: CALLPRIVATE v3f79c(0x909)

    Begin block 0xe6
    prev=[0xdb], succ=[0x4017c, 0xf1]
    =================================
    0xe7: ve7(0xbf583903) = CONST 
    0xec: vec = EQ ve7(0xbf583903), v35
    0x3117c: v3117c(0x4017c) = CONST 
    0x3119c: JUMPI v3117c(0x4017c), vec

    Begin block 0x4017c
    prev=[0xe6], succ=[]
    =================================
    0x4019c: v4019c(0x96e) = CONST 
    0x401bc: CALLPRIVATE v4019c(0x96e)

    Begin block 0xf1
    prev=[0xe6], succ=[0x40b7c, 0xfc]
    =================================
    0xf2: vf2(0xc7876ea4) = CONST 
    0xf7: vf7 = EQ vf2(0xc7876ea4), v35
    0x31b7c: v31b7c(0x40b7c) = CONST 
    0x31b9c: JUMPI v31b7c(0x40b7c), vf7

    Begin block 0x40b7c
    prev=[0xf1], succ=[]
    =================================
    0x40b9c: v40b9c(0x999) = CONST 
    0x40bbc: CALLPRIVATE v40b9c(0x999)

    Begin block 0xfc
    prev=[0xf1], succ=[0x4157c, 0x107]
    =================================
    0xfd: vfd(0xcbcb3171) = CONST 
    0x102: v102 = EQ vfd(0xcbcb3171), v35
    0x3257c: v3257c(0x4157c) = CONST 
    0x3259c: JUMPI v3257c(0x4157c), v102

    Begin block 0x4157c
    prev=[0xfc], succ=[]
    =================================
    0x4159c: v4159c(0x9c4) = CONST 
    0x415bc: CALLPRIVATE v4159c(0x9c4)

    Begin block 0x107
    prev=[0xfc], succ=[0x41f7c, 0x112]
    =================================
    0x108: v108(0xd73dd623) = CONST 
    0x10d: v10d = EQ v108(0xd73dd623), v35
    0x32f7c: v32f7c(0x41f7c) = CONST 
    0x32f9c: JUMPI v32f7c(0x41f7c), v10d

    Begin block 0x41f7c
    prev=[0x107], succ=[]
    =================================
    0x41f9c: v41f9c(0x9ef) = CONST 
    0x41fbc: CALLPRIVATE v41f9c(0x9ef)

    Begin block 0x112
    prev=[0x107], succ=[0x4297c, 0x11d]
    =================================
    0x113: v113(0xdb35132c) = CONST 
    0x118: v118 = EQ v113(0xdb35132c), v35
    0x3397c: v3397c(0x4297c) = CONST 
    0x3399c: JUMPI v3397c(0x4297c), v118

    Begin block 0x4297c
    prev=[0x112], succ=[]
    =================================
    0x4299c: v4299c(0xa54) = CONST 
    0x429bc: CALLPRIVATE v4299c(0xa54)

    Begin block 0x11d
    prev=[0x112], succ=[0x4337c, 0x128]
    =================================
    0x11e: v11e(0xdd62ed3e) = CONST 
    0x123: v123 = EQ v11e(0xdd62ed3e), v35
    0x3437c: v3437c(0x4337c) = CONST 
    0x3439c: JUMPI v3437c(0x4337c), v123

    Begin block 0x4337c
    prev=[0x11d], succ=[]
    =================================
    0x4339c: v4339c(0xaa1) = CONST 
    0x433bc: CALLPRIVATE v4339c(0xaa1)

    Begin block 0x128
    prev=[0x11d], succ=[0x3577c, 0x43d7c]
    =================================
    0x129: v129(0xf2fde38b) = CONST 
    0x12e: v12e = EQ v129(0xf2fde38b), v35
    0x34d7c: v34d7c(0x43d7c) = CONST 
    0x34d9c: JUMPI v34d7c(0x43d7c), v12e

    Begin block 0x3577c
    prev=[0x0, 0x128], succ=[]
    =================================
    0x3579c: v3579c(0x133) = CONST 
    0x357bc: CALLPRIVATE v3579c(0x133)

    Begin block 0x43d7c
    prev=[0x128], succ=[]
    =================================
    0x43d9c: v43d9c(0xb18) = CONST 
    0x43dbc: CALLPRIVATE v43d9c(0xb18)

}

function fallback()() public {
    Begin block 0x133
    prev=[], succ=[0x147, 0x148]
    =================================
    0x134: v134(0x0) = CONST 
    0x137: v137(0x0) = CONST 
    0x13a: v13a(0x0) = CONST 
    0x13c: v13c(0x1) = CONST 
    0x13e: v13e(0x2) = CONST 
    0x141: v141(0x0) = GT v13c(0x1), v13e(0x2)
    0x142: v142(0x1) = ISZERO v141(0x0)
    0x143: v143(0x148) = CONST 
    0x146: JUMPI v143(0x148), v142(0x1)

    Begin block 0x147
    prev=[0x133], succ=[]
    =================================
    0x147: THROW 

    Begin block 0x148
    prev=[0x133], succ=[0x162, 0x163]
    =================================
    0x149: v149(0x7) = CONST 
    0x14b: v14b(0x14) = CONST 
    0x14e: v14e = SLOAD v149(0x7)
    0x150: v150(0x100) = CONST 
    0x153: v153(0x10000000000000000000000000000000000000000) = EXP v150(0x100), v14b(0x14)
    0x155: v155 = DIV v14e, v153(0x10000000000000000000000000000000000000000)
    0x156: v156(0xff) = CONST 
    0x158: v158 = AND v156(0xff), v155
    0x159: v159(0x2) = CONST 
    0x15c: v15c = GT v158, v159(0x2)
    0x15d: v15d = ISZERO v15c
    0x15e: v15e(0x163) = CONST 
    0x161: JUMPI v15e(0x163), v15d

    Begin block 0x162
    prev=[0x148], succ=[]
    =================================
    0x162: THROW 

    Begin block 0x163
    prev=[0x148], succ=[0x16b, 0x16f]
    =================================
    0x164: v164 = EQ v158, v13c(0x1)
    0x165: v165 = ISZERO v164
    0x166: v166 = ISZERO v165
    0x167: v167(0x16f) = CONST 
    0x16a: JUMPI v167(0x16f), v166

    Begin block 0x16b
    prev=[0x163], succ=[]
    =================================
    0x16b: v16b(0x0) = CONST 
    0x16e: REVERT v16b(0x0), v16b(0x0)

    Begin block 0x16f
    prev=[0x163], succ=[0x17a, 0x17e]
    =================================
    0x170: v170(0x0) = CONST 
    0x172: v172 = CALLVALUE 
    0x173: v173 = GT v172, v170(0x0)
    0x174: v174 = ISZERO v173
    0x175: v175 = ISZERO v174
    0x176: v176(0x17e) = CONST 
    0x179: JUMPI v176(0x17e), v175

    Begin block 0x17a
    prev=[0x16f], succ=[]
    =================================
    0x17a: v17a(0x0) = CONST 
    0x17d: REVERT v17a(0x0), v17a(0x0)

    Begin block 0x17e
    prev=[0x16f], succ=[0x18b, 0x18f]
    =================================
    0x17f: v17f(0x0) = CONST 
    0x181: v181(0x6) = CONST 
    0x183: v183 = SLOAD v181(0x6)
    0x184: v184 = GT v183, v17f(0x0)
    0x185: v185 = ISZERO v184
    0x186: v186 = ISZERO v185
    0x187: v187(0x18f) = CONST 
    0x18a: JUMPI v187(0x18f), v186

    Begin block 0x18b
    prev=[0x17e], succ=[]
    =================================
    0x18b: v18b(0x0) = CONST 
    0x18e: REVERT v18b(0x0), v18b(0x0)

    Begin block 0x18f
    prev=[0x17e], succ=[0x1b6]
    =================================
    0x190: v190 = CALLVALUE 
    0x193: v193(0x1c4) = CONST 
    0x196: v196(0xde0b6b3a7640000) = CONST 
    0x19f: v19f(0x1b6) = CONST 
    0x1a2: v1a2(0x2540be400) = CONST 
    0x1a9: v1a9(0xb5b) = CONST 
    0x1af: v1af(0xffffffff) = CONST 
    0x1b4: v1b4(0xb5b) = AND v1af(0xffffffff), v1a9(0xb5b)
    0x1b5: v1b5_0 = CALLPRIVATE v1b4(0xb5b), v1a2(0x2540be400), v190, v19f(0x1b6)

    Begin block 0x1b6
    prev=[0x18f], succ=[0x1c4]
    =================================
    0x1b7: v1b7(0xb93) = CONST 
    0x1bd: v1bd(0xffffffff) = CONST 
    0x1c2: v1c2(0xb93) = AND v1bd(0xffffffff), v1b7(0xb93)
    0x1c3: v1c3_0 = CALLPRIVATE v1c2(0xb93), v196(0xde0b6b3a7640000), v1b5_0, v193(0x1c4)

    Begin block 0x1c4
    prev=[0x1b6], succ=[0x1e7]
    =================================
    0x1c7: v1c7(0x0) = CONST 
    0x1cb: v1cb(0x2386f26fc10000) = CONST 
    0x1d3: v1d3(0x1e7) = CONST 
    0x1d7: v1d7(0x5) = CONST 
    0x1d9: v1d9 = SLOAD v1d7(0x5)
    0x1da: v1da(0xba9) = CONST 
    0x1e0: v1e0(0xffffffff) = CONST 
    0x1e5: v1e5(0xba9) = AND v1e0(0xffffffff), v1da(0xba9)
    0x1e6: v1e6_0 = CALLPRIVATE v1e5(0xba9), v1c3_0, v1d9, v1d3(0x1e7)

    Begin block 0x1e7
    prev=[0x1c4], succ=[0x1ee, 0x25b]
    =================================
    0x1e8: v1e8 = GT v1e6_0, v1cb(0x2386f26fc10000)
    0x1e9: v1e9 = ISZERO v1e8
    0x1ea: v1ea(0x25b) = CONST 
    0x1ed: JUMPI v1ea(0x25b), v1e9

    Begin block 0x1ee
    prev=[0x1e7], succ=[0x209]
    =================================
    0x1ee: v1ee(0x209) = CONST 
    0x1f1: v1f1(0x5) = CONST 
    0x1f3: v1f3 = SLOAD v1f1(0x5)
    0x1f4: v1f4(0x2386f26fc10000) = CONST 
    0x1fc: v1fc(0xbc5) = CONST 
    0x202: v202(0xffffffff) = CONST 
    0x207: v207(0xbc5) = AND v202(0xffffffff), v1fc(0xbc5)
    0x208: v208_0 = CALLPRIVATE v207(0xbc5), v1f3, v1f4(0x2386f26fc10000), v1ee(0x209)

    Begin block 0x209
    prev=[0x1ee], succ=[0x22f]
    =================================
    0x20c: v20c(0x23d) = CONST 
    0x20f: v20f(0xde0b6b3a7640000) = CONST 
    0x218: v218(0x22f) = CONST 
    0x21b: v21b(0x2540be400) = CONST 
    0x222: v222(0xb93) = CONST 
    0x228: v228(0xffffffff) = CONST 
    0x22d: v22d(0xb93) = AND v228(0xffffffff), v222(0xb93)
    0x22e: v22e_0 = CALLPRIVATE v22d(0xb93), v21b(0x2540be400), v208_0, v218(0x22f)

    Begin block 0x22f
    prev=[0x209], succ=[0x23d]
    =================================
    0x230: v230(0xb5b) = CONST 
    0x236: v236(0xffffffff) = CONST 
    0x23b: v23b(0xb5b) = AND v236(0xffffffff), v230(0xb5b)
    0x23c: v23c_0 = CALLPRIVATE v23b(0xb5b), v20f(0xde0b6b3a7640000), v22e_0, v20c(0x23d)

    Begin block 0x23d
    prev=[0x22f], succ=[0x252]
    =================================
    0x240: v240(0x252) = CONST 
    0x245: v245(0xbc5) = CONST 
    0x24b: v24b(0xffffffff) = CONST 
    0x250: v250(0xbc5) = AND v24b(0xffffffff), v245(0xbc5)
    0x251: v251_0 = CALLPRIVATE v250(0xbc5), v23c_0, v190, v240(0x252)

    Begin block 0x252
    prev=[0x23d], succ=[0x25b]
    =================================
    0x3f92: v3f92(0x25b) = CONST 
    0x3fb2: JUMP v3f92(0x25b)

    Begin block 0x25b
    prev=[0x1e7, 0x252], succ=[0x270]
    =================================
    0x25b_0x3: v25b_3 = PHI v1c3_0, v208_0
    0x25c: v25c(0x270) = CONST 
    0x260: v260(0x5) = CONST 
    0x262: v262 = SLOAD v260(0x5)
    0x263: v263(0xba9) = CONST 
    0x269: v269(0xffffffff) = CONST 
    0x26e: v26e(0xba9) = AND v269(0xffffffff), v263(0xba9)
    0x26f: v26f_0 = CALLPRIVATE v26e(0xba9), v25b_3, v262, v25c(0x270)

    Begin block 0x270
    prev=[0x25b], succ=[0x292]
    =================================
    0x271: v271(0x5) = CONST 
    0x275: SSTORE v271(0x5), v26f_0
    0x277: v277(0x292) = CONST 
    0x27a: v27a(0x5) = CONST 
    0x27c: v27c = SLOAD v27a(0x5)
    0x27d: v27d(0x2386f26fc10000) = CONST 
    0x285: v285(0xbc5) = CONST 
    0x28b: v28b(0xffffffff) = CONST 
    0x290: v290(0xbc5) = AND v28b(0xffffffff), v285(0xbc5)
    0x291: v291_0 = CALLPRIVATE v290(0xbc5), v27c, v27d(0x2386f26fc10000), v277(0x292)

    Begin block 0x292
    prev=[0x270], succ=[0x2a2, 0x34e]
    =================================
    0x292_0x3: v292_3 = PHI v1c7(0x0), v251_0
    0x293: v293(0x6) = CONST 
    0x297: SSTORE v293(0x6), v291_0
    0x299: v299(0x0) = CONST 
    0x29c: v29c = GT v292_3, v299(0x0)
    0x29d: v29d = ISZERO v29c
    0x29e: v29e(0x34e) = CONST 
    0x2a1: JUMPI v29e(0x34e), v29d

    Begin block 0x2a2
    prev=[0x292], succ=[0x2de, 0x2e7]
    =================================
    0x2a2: v2a2 = CALLER 
    0x2a2_0x2: v2a2_2 = PHI v1c7(0x0), v251_0
    0x2a3: v2a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b8: v2b8 = AND v2a3(0xffffffffffffffffffffffffffffffffffffffff), v2a2
    0x2b9: v2b9(0x8fc) = CONST 
    0x2bf: v2bf = ISZERO v2a2_2
    0x2c0: v2c0 = MUL v2bf, v2b9(0x8fc)
    0x2c2: v2c2(0x40) = CONST 
    0x2c4: v2c4 = MLOAD v2c2(0x40)
    0x2c5: v2c5(0x0) = CONST 
    0x2c7: v2c7(0x40) = CONST 
    0x2c9: v2c9 = MLOAD v2c7(0x40)
    0x2cc: v2cc(0x0) = SUB v2c4, v2c9
    0x2d1: v2d1 = CALL v2c0, v2b8, v2a2_2, v2c9, v2cc(0x0), v2c9, v2c5(0x0)
    0x2d7: v2d7 = ISZERO v2d1
    0x2d9: v2d9 = ISZERO v2d7
    0x2da: v2da(0x2e7) = CONST 
    0x2dd: JUMPI v2da(0x2e7), v2d9

    Begin block 0x2de
    prev=[0x2a2], succ=[]
    =================================
    0x2de: v2de = RETURNDATASIZE 
    0x2df: v2df(0x0) = CONST 
    0x2e2: RETURNDATACOPY v2df(0x0), v2df(0x0), v2de
    0x2e3: v2e3 = RETURNDATASIZE 
    0x2e4: v2e4(0x0) = CONST 
    0x2e6: REVERT v2e4(0x0), v2e3

    Begin block 0x2e7
    prev=[0x2a2], succ=[0x34e]
    =================================
    0x2e7_0x3: v2e7_3 = PHI v1c7(0x0), v251_0
    0x2e9: v2e9 = CALLER 
    0x2ea: v2ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ff: v2ff = AND v2ea(0xffffffffffffffffffffffffffffffffffffffff), v2e9
    0x300: v300 = ADDRESS 
    0x301: v301(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x316: v316 = AND v301(0xffffffffffffffffffffffffffffffffffffffff), v300
    0x317: v317(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x339: v339(0x40) = CONST 
    0x33b: v33b = MLOAD v339(0x40)
    0x33f: MSTORE v33b, v2e7_3
    0x340: v340(0x20) = CONST 
    0x342: v342 = ADD v340(0x20), v33b
    0x346: v346(0x40) = CONST 
    0x348: v348 = MLOAD v346(0x40)
    0x34b: v34b(0x20) = SUB v342, v348
    0x34d: LOG3 v348, v34b(0x20), v317(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v316, v2ff
    0x4992: v4992(0x34e) = CONST 
    0x49b2: JUMP v4992(0x34e)

    Begin block 0x34e
    prev=[0x292, 0x2e7], succ=[0x39f]
    =================================
    0x34e_0x3: v34e_3 = PHI v1c3_0, v208_0
    0x34f: v34f(0x39f) = CONST 
    0x353: v353(0x0) = CONST 
    0x356: v356 = CALLER 
    0x357: v357(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36c: v36c = AND v357(0xffffffffffffffffffffffffffffffffffffffff), v356
    0x36d: v36d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x382: v382 = AND v36d(0xffffffffffffffffffffffffffffffffffffffff), v36c
    0x384: MSTORE v353(0x0), v382
    0x385: v385(0x20) = CONST 
    0x387: v387(0x20) = ADD v385(0x20), v353(0x0)
    0x38a: MSTORE v387(0x20), v353(0x0)
    0x38b: v38b(0x20) = CONST 
    0x38d: v38d(0x40) = ADD v38b(0x20), v387(0x20)
    0x38e: v38e(0x0) = CONST 
    0x390: v390 = SHA3 v38e(0x0), v38d(0x40)
    0x391: v391 = SLOAD v390
    0x392: v392(0xba9) = CONST 
    0x398: v398(0xffffffff) = CONST 
    0x39d: v39d(0xba9) = AND v398(0xffffffff), v392(0xba9)
    0x39e: v39e_0 = CALLPRIVATE v39d(0xba9), v34e_3, v391, v34f(0x39f)

    Begin block 0x39f
    prev=[0x34e], succ=[0x45b]
    =================================
    0x39f_0x4: v39f_4 = PHI v1c3_0, v208_0
    0x3a0: v3a0(0x0) = CONST 
    0x3a3: v3a3 = CALLER 
    0x3a4: v3a4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b9: v3b9 = AND v3a4(0xffffffffffffffffffffffffffffffffffffffff), v3a3
    0x3ba: v3ba(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3cf: v3cf = AND v3ba(0xffffffffffffffffffffffffffffffffffffffff), v3b9
    0x3d1: MSTORE v3a0(0x0), v3cf
    0x3d2: v3d2(0x20) = CONST 
    0x3d4: v3d4(0x20) = ADD v3d2(0x20), v3a0(0x0)
    0x3d7: MSTORE v3d4(0x20), v3a0(0x0)
    0x3d8: v3d8(0x20) = CONST 
    0x3da: v3da(0x40) = ADD v3d8(0x20), v3d4(0x20)
    0x3db: v3db(0x0) = CONST 
    0x3dd: v3dd = SHA3 v3db(0x0), v3da(0x40)
    0x3e0: SSTORE v3dd, v39e_0
    0x3e2: v3e2 = CALLER 
    0x3e3: v3e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3f8: v3f8 = AND v3e3(0xffffffffffffffffffffffffffffffffffffffff), v3e2
    0x3f9: v3f9 = ADDRESS 
    0x3fa: v3fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x40f: v40f = AND v3fa(0xffffffffffffffffffffffffffffffffffffffff), v3f9
    0x410: v410(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x432: v432(0x40) = CONST 
    0x434: v434 = MLOAD v432(0x40)
    0x438: MSTORE v434, v39f_4
    0x439: v439(0x20) = CONST 
    0x43b: v43b = ADD v439(0x20), v434
    0x43f: v43f(0x40) = CONST 
    0x441: v441 = MLOAD v43f(0x40)
    0x444: v444(0x20) = SUB v43b, v441
    0x446: LOG3 v441, v444(0x20), v410(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v40f, v3f8
    0x447: v447(0x45b) = CONST 
    0x44b: v44b(0x1) = CONST 
    0x44d: v44d = SLOAD v44b(0x1)
    0x44e: v44e(0xba9) = CONST 
    0x454: v454(0xffffffff) = CONST 
    0x459: v459(0xba9) = AND v454(0xffffffff), v44e(0xba9)
    0x45a: v45a_0 = CALLPRIVATE v459(0xba9), v39f_4, v44d, v447(0x45b)

    Begin block 0x45b
    prev=[0x39f], succ=[0x4c0, 0x4c9]
    =================================
    0x45b_0x5: v45b_5 = PHI v190, v23c_0
    0x45c: v45c(0x1) = CONST 
    0x460: SSTORE v45c(0x1), v45a_0
    0x462: v462(0x7) = CONST 
    0x464: v464(0x0) = CONST 
    0x467: v467 = SLOAD v462(0x7)
    0x469: v469(0x100) = CONST 
    0x46c: v46c(0x1) = EXP v469(0x100), v464(0x0)
    0x46e: v46e = DIV v467, v46c(0x1)
    0x46f: v46f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x484: v484 = AND v46f(0xffffffffffffffffffffffffffffffffffffffff), v46e
    0x485: v485(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x49a: v49a = AND v485(0xffffffffffffffffffffffffffffffffffffffff), v484
    0x49b: v49b(0x8fc) = CONST 
    0x4a1: v4a1 = ISZERO v45b_5
    0x4a2: v4a2 = MUL v4a1, v49b(0x8fc)
    0x4a4: v4a4(0x40) = CONST 
    0x4a6: v4a6 = MLOAD v4a4(0x40)
    0x4a7: v4a7(0x0) = CONST 
    0x4a9: v4a9(0x40) = CONST 
    0x4ab: v4ab = MLOAD v4a9(0x40)
    0x4ae: v4ae(0x0) = SUB v4a6, v4ab
    0x4b3: v4b3 = CALL v4a2, v49a, v45b_5, v4ab, v4ae(0x0), v4ab, v4a7(0x0)
    0x4b9: v4b9 = ISZERO v4b3
    0x4bb: v4bb = ISZERO v4b9
    0x4bc: v4bc(0x4c9) = CONST 
    0x4bf: JUMPI v4bc(0x4c9), v4bb

    Begin block 0x4c0
    prev=[0x45b], succ=[]
    =================================
    0x4c0: v4c0 = RETURNDATASIZE 
    0x4c1: v4c1(0x0) = CONST 
    0x4c4: RETURNDATACOPY v4c1(0x0), v4c1(0x0), v4c0
    0x4c5: v4c5 = RETURNDATASIZE 
    0x4c6: v4c6(0x0) = CONST 
    0x4c8: REVERT v4c6(0x0), v4c5

    Begin block 0x4c9
    prev=[0x45b], succ=[]
    =================================
    0x4d0: STOP 

}

function name()() public {
    Begin block 0x4d1
    prev=[], succ=[0x4d9, 0x4dd]
    =================================
    0x4d2: v4d2 = CALLVALUE 
    0x4d4: v4d4 = ISZERO v4d2
    0x4d5: v4d5(0x4dd) = CONST 
    0x4d8: JUMPI v4d5(0x4dd), v4d4

    Begin block 0x4d9
    prev=[0x4d1], succ=[]
    =================================
    0x4d9: v4d9(0x0) = CONST 
    0x4dc: REVERT v4d9(0x0), v4d9(0x0)

    Begin block 0x4dd
    prev=[0x4d1], succ=[0xbde]
    =================================
    0x4df: v4df(0x4e6) = CONST 
    0x4e2: v4e2(0xbde) = CONST 
    0x4e5: JUMP v4e2(0xbde)

    Begin block 0xbde
    prev=[0x4dd], succ=[0x4e6]
    =================================
    0xbdf: vbdf(0x40) = CONST 
    0xbe2: vbe2 = MLOAD vbdf(0x40)
    0xbe5: vbe5 = ADD vbe2, vbdf(0x40)
    0xbe6: vbe6(0x40) = CONST 
    0xbe8: MSTORE vbe6(0x40), vbe5
    0xbea: vbea(0x6) = CONST 
    0xbed: MSTORE vbe2, vbea(0x6)
    0xbee: vbee(0x20) = CONST 
    0xbf0: vbf0 = ADD vbee(0x20), vbe2
    0xbf1: vbf1(0x4e65746965780000000000000000000000000000000000000000000000000000) = CONST 
    0xc13: MSTORE vbf0, vbf1(0x4e65746965780000000000000000000000000000000000000000000000000000)
    0xc16: JUMP v4df(0x4e6)

    Begin block 0x4e6
    prev=[0xbde], succ=[0x50b]
    =================================
    0x4e7: v4e7(0x40) = CONST 
    0x4e9: v4e9 = MLOAD v4e7(0x40)
    0x4ec: v4ec(0x20) = CONST 
    0x4ee: v4ee = ADD v4ec(0x20), v4e9
    0x4f1: v4f1(0x20) = SUB v4ee, v4e9
    0x4f3: MSTORE v4e9, v4f1(0x20)
    0x4f7: v4f7(0x6) = MLOAD vbe2
    0x4f9: MSTORE v4ee, v4f7(0x6)
    0x4fa: v4fa(0x20) = CONST 
    0x4fc: v4fc = ADD v4fa(0x20), v4ee
    0x500: v500(0x6) = MLOAD vbe2
    0x502: v502(0x20) = CONST 
    0x504: v504 = ADD v502(0x20), vbe2
    0x509: v509(0x0) = CONST 
    0x5392: v5392(0x50b) = CONST 
    0x53b2: JUMP v5392(0x50b)

    Begin block 0x50b
    prev=[0x4e6, 0x514], succ=[0x526, 0x514]
    =================================
    0x50b_0x0: v50b_0 = PHI v509(0x0), v51f
    0x50e: v50e = LT v50b_0, v500(0x6)
    0x50f: v50f = ISZERO v50e
    0x510: v510(0x526) = CONST 
    0x513: JUMPI v510(0x526), v50f

    Begin block 0x526
    prev=[0x50b], succ=[0x553, 0x53a]
    =================================
    0x52f: v52f = ADD v500(0x6), v4fc
    0x531: v531(0x1f) = CONST 
    0x533: v533(0x6) = AND v531(0x1f), v500(0x6)
    0x535: v535(0x0) = ISZERO v533(0x6)
    0x536: v536(0x553) = CONST 
    0x539: JUMPI v536(0x553), v535(0x0)

    Begin block 0x553
    prev=[0x526, 0x53a], succ=[]
    =================================
    0x553_0x1: v553_1 = PHI v52f, v550
    0x559: v559(0x40) = CONST 
    0x55b: v55b = MLOAD v559(0x40)
    0x55e: v55e = SUB v553_1, v55b
    0x560: RETURN v55b, v55e

    Begin block 0x53a
    prev=[0x526], succ=[0x553]
    =================================
    0x53c: v53c = SUB v52f, v533(0x6)
    0x53e: v53e = MLOAD v53c
    0x53f: v53f(0x1) = CONST 
    0x542: v542(0x20) = CONST 
    0x544: v544(0x1a) = SUB v542(0x20), v533(0x6)
    0x545: v545(0x100) = CONST 
    0x548: v548(0x10000000000000000000000000000000000000000000000000000) = EXP v545(0x100), v544(0x1a)
    0x549: v549(0xffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v548(0x10000000000000000000000000000000000000000000000000000), v53f(0x1)
    0x54a: v54a(0xffffffffffff0000000000000000000000000000000000000000000000000000) = NOT v549(0xffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x54b: v54b = AND v54a(0xffffffffffff0000000000000000000000000000000000000000000000000000), v53e
    0x54d: MSTORE v53c, v54b
    0x54e: v54e(0x20) = CONST 
    0x550: v550 = ADD v54e(0x20), v53c
    0x5d92: v5d92(0x553) = CONST 
    0x5db2: JUMP v5d92(0x553)

    Begin block 0x514
    prev=[0x50b], succ=[0x50b]
    =================================
    0x514_0x0: v514_0 = PHI v509(0x0), v51f
    0x516: v516 = ADD v504, v514_0
    0x517: v517 = MLOAD v516
    0x51a: v51a = ADD v4fc, v514_0
    0x51b: MSTORE v51a, v517
    0x51c: v51c(0x20) = CONST 
    0x51f: v51f = ADD v514_0, v51c(0x20)
    0x522: v522(0x50b) = CONST 
    0x525: JUMP v522(0x50b)

}

function approve(address,uint256)() public {
    Begin block 0x561
    prev=[], succ=[0x569, 0x56d]
    =================================
    0x562: v562 = CALLVALUE 
    0x564: v564 = ISZERO v562
    0x565: v565(0x56d) = CONST 
    0x568: JUMPI v565(0x56d), v564

    Begin block 0x569
    prev=[0x561], succ=[]
    =================================
    0x569: v569(0x0) = CONST 
    0x56c: REVERT v569(0x0), v569(0x0)

    Begin block 0x56d
    prev=[0x561], succ=[0xc17]
    =================================
    0x56f: v56f(0x5ac) = CONST 
    0x572: v572(0x4) = CONST 
    0x575: v575 = CALLDATASIZE 
    0x576: v576 = SUB v575, v572(0x4)
    0x578: v578 = ADD v572(0x4), v576
    0x57c: v57c = CALLDATALOAD v572(0x4)
    0x57d: v57d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x592: v592 = AND v57d(0xffffffffffffffffffffffffffffffffffffffff), v57c
    0x594: v594(0x20) = CONST 
    0x596: v596(0x24) = ADD v594(0x20), v572(0x4)
    0x59c: v59c = CALLDATALOAD v596(0x24)
    0x59e: v59e(0x20) = CONST 
    0x5a0: v5a0(0x44) = ADD v59e(0x20), v596(0x24)
    0x5a8: v5a8(0xc17) = CONST 
    0x5ab: JUMP v5a8(0xc17)

    Begin block 0xc17
    prev=[0x56d], succ=[0x5ac]
    =================================
    0xc18: vc18(0x0) = CONST 
    0xc1b: vc1b(0x2) = CONST 
    0xc1d: vc1d(0x0) = CONST 
    0xc1f: vc1f = CALLER 
    0xc20: vc20(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc35: vc35 = AND vc20(0xffffffffffffffffffffffffffffffffffffffff), vc1f
    0xc36: vc36(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc4b: vc4b = AND vc36(0xffffffffffffffffffffffffffffffffffffffff), vc35
    0xc4d: MSTORE vc1d(0x0), vc4b
    0xc4e: vc4e(0x20) = CONST 
    0xc50: vc50(0x20) = ADD vc4e(0x20), vc1d(0x0)
    0xc53: MSTORE vc50(0x20), vc1b(0x2)
    0xc54: vc54(0x20) = CONST 
    0xc56: vc56(0x40) = ADD vc54(0x20), vc50(0x20)
    0xc57: vc57(0x0) = CONST 
    0xc59: vc59 = SHA3 vc57(0x0), vc56(0x40)
    0xc5a: vc5a(0x0) = CONST 
    0xc5d: vc5d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc72: vc72 = AND vc5d(0xffffffffffffffffffffffffffffffffffffffff), v592
    0xc73: vc73(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc88: vc88 = AND vc73(0xffffffffffffffffffffffffffffffffffffffff), vc72
    0xc8a: MSTORE vc5a(0x0), vc88
    0xc8b: vc8b(0x20) = CONST 
    0xc8d: vc8d(0x20) = ADD vc8b(0x20), vc5a(0x0)
    0xc90: MSTORE vc8d(0x20), vc59
    0xc91: vc91(0x20) = CONST 
    0xc93: vc93(0x40) = ADD vc91(0x20), vc8d(0x20)
    0xc94: vc94(0x0) = CONST 
    0xc96: vc96 = SHA3 vc94(0x0), vc93(0x40)
    0xc99: SSTORE vc96, v59c
    0xc9c: vc9c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcb1: vcb1 = AND vc9c(0xffffffffffffffffffffffffffffffffffffffff), v592
    0xcb2: vcb2 = CALLER 
    0xcb3: vcb3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcc8: vcc8 = AND vcb3(0xffffffffffffffffffffffffffffffffffffffff), vcb2
    0xcc9: vcc9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xceb: vceb(0x40) = CONST 
    0xced: vced = MLOAD vceb(0x40)
    0xcf1: MSTORE vced, v59c
    0xcf2: vcf2(0x20) = CONST 
    0xcf4: vcf4 = ADD vcf2(0x20), vced
    0xcf8: vcf8(0x40) = CONST 
    0xcfa: vcfa = MLOAD vcf8(0x40)
    0xcfd: vcfd(0x20) = SUB vcf4, vcfa
    0xcff: LOG3 vcfa, vcfd(0x20), vcc9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vcc8, vcb1
    0xd00: vd00(0x1) = CONST 
    0xd08: JUMP v56f(0x5ac)

    Begin block 0x5ac
    prev=[0xc17], succ=[]
    =================================
    0x5ad: v5ad(0x40) = CONST 
    0x5af: v5af = MLOAD v5ad(0x40)
    0x5b2: v5b2(0x0) = ISZERO vd00(0x1)
    0x5b3: v5b3(0x1) = ISZERO v5b2(0x0)
    0x5b4: v5b4(0x0) = ISZERO v5b3(0x1)
    0x5b5: v5b5(0x1) = ISZERO v5b4(0x0)
    0x5b7: MSTORE v5af, v5b5(0x1)
    0x5b8: v5b8(0x20) = CONST 
    0x5ba: v5ba = ADD v5b8(0x20), v5af
    0x5be: v5be(0x40) = CONST 
    0x5c0: v5c0 = MLOAD v5be(0x40)
    0x5c3: v5c3(0x20) = SUB v5ba, v5c0
    0x5c5: RETURN v5c0, v5c3(0x20)

}

function totalSupply()() public {
    Begin block 0x5c6
    prev=[], succ=[0x5ce, 0x5d2]
    =================================
    0x5c7: v5c7 = CALLVALUE 
    0x5c9: v5c9 = ISZERO v5c7
    0x5ca: v5ca(0x5d2) = CONST 
    0x5cd: JUMPI v5ca(0x5d2), v5c9

    Begin block 0x5ce
    prev=[0x5c6], succ=[]
    =================================
    0x5ce: v5ce(0x0) = CONST 
    0x5d1: REVERT v5ce(0x0), v5ce(0x0)

    Begin block 0x5d2
    prev=[0x5c6], succ=[0xd09]
    =================================
    0x5d4: v5d4(0x5db) = CONST 
    0x5d7: v5d7(0xd09) = CONST 
    0x5da: JUMP v5d7(0xd09)

    Begin block 0xd09
    prev=[0x5d2], succ=[0x5db]
    =================================
    0xd0a: vd0a(0x0) = CONST 
    0xd0c: vd0c(0x1) = CONST 
    0xd0e: vd0e = SLOAD vd0c(0x1)
    0xd12: JUMP v5d4(0x5db)

    Begin block 0x5db
    prev=[0xd09], succ=[]
    =================================
    0x5dc: v5dc(0x40) = CONST 
    0x5de: v5de = MLOAD v5dc(0x40)
    0x5e2: MSTORE v5de, vd0e
    0x5e3: v5e3(0x20) = CONST 
    0x5e5: v5e5 = ADD v5e3(0x20), v5de
    0x5e9: v5e9(0x40) = CONST 
    0x5eb: v5eb = MLOAD v5e9(0x40)
    0x5ee: v5ee(0x20) = SUB v5e5, v5eb
    0x5f0: RETURN v5eb, v5ee(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x5f1
    prev=[], succ=[0x5f9, 0x5fd]
    =================================
    0x5f2: v5f2 = CALLVALUE 
    0x5f4: v5f4 = ISZERO v5f2
    0x5f5: v5f5(0x5fd) = CONST 
    0x5f8: JUMPI v5f5(0x5fd), v5f4

    Begin block 0x5f9
    prev=[0x5f1], succ=[]
    =================================
    0x5f9: v5f9(0x0) = CONST 
    0x5fc: REVERT v5f9(0x0), v5f9(0x0)

    Begin block 0x5fd
    prev=[0x5f1], succ=[0xd13]
    =================================
    0x5ff: v5ff(0x65c) = CONST 
    0x602: v602(0x4) = CONST 
    0x605: v605 = CALLDATASIZE 
    0x606: v606 = SUB v605, v602(0x4)
    0x608: v608 = ADD v602(0x4), v606
    0x60c: v60c = CALLDATALOAD v602(0x4)
    0x60d: v60d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x622: v622 = AND v60d(0xffffffffffffffffffffffffffffffffffffffff), v60c
    0x624: v624(0x20) = CONST 
    0x626: v626(0x24) = ADD v624(0x20), v602(0x4)
    0x62c: v62c = CALLDATALOAD v626(0x24)
    0x62d: v62d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x642: v642 = AND v62d(0xffffffffffffffffffffffffffffffffffffffff), v62c
    0x644: v644(0x20) = CONST 
    0x646: v646(0x44) = ADD v644(0x20), v626(0x24)
    0x64c: v64c = CALLDATALOAD v646(0x44)
    0x64e: v64e(0x20) = CONST 
    0x650: v650(0x64) = ADD v64e(0x20), v646(0x44)
    0x658: v658(0xd13) = CONST 
    0x65b: JUMP v658(0xd13)

    Begin block 0xd13
    prev=[0x5fd], succ=[0xd4c, 0xd50]
    =================================
    0xd14: vd14(0x0) = CONST 
    0xd17: vd17(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd2c: vd2c(0x0) = AND vd17(0xffffffffffffffffffffffffffffffffffffffff), vd14(0x0)
    0xd2e: vd2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd43: vd43 = AND vd2e(0xffffffffffffffffffffffffffffffffffffffff), v642
    0xd44: vd44 = EQ vd43, vd2c(0x0)
    0xd45: vd45 = ISZERO vd44
    0xd46: vd46 = ISZERO vd45
    0xd47: vd47 = ISZERO vd46
    0xd48: vd48(0xd50) = CONST 
    0xd4b: JUMPI vd48(0xd50), vd47

    Begin block 0xd4c
    prev=[0xd13], succ=[]
    =================================
    0xd4c: vd4c(0x0) = CONST 
    0xd4f: REVERT vd4c(0x0), vd4c(0x0)

    Begin block 0xd50
    prev=[0xd13], succ=[0xd99, 0xd9d]
    =================================
    0xd51: vd51(0x0) = CONST 
    0xd55: vd55(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd6a: vd6a = AND vd55(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xd6b: vd6b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd80: vd80 = AND vd6b(0xffffffffffffffffffffffffffffffffffffffff), vd6a
    0xd82: MSTORE vd51(0x0), vd80
    0xd83: vd83(0x20) = CONST 
    0xd85: vd85(0x20) = ADD vd83(0x20), vd51(0x0)
    0xd88: MSTORE vd85(0x20), vd51(0x0)
    0xd89: vd89(0x20) = CONST 
    0xd8b: vd8b(0x40) = ADD vd89(0x20), vd85(0x20)
    0xd8c: vd8c(0x0) = CONST 
    0xd8e: vd8e = SHA3 vd8c(0x0), vd8b(0x40)
    0xd8f: vd8f = SLOAD vd8e
    0xd91: vd91 = GT v64c, vd8f
    0xd92: vd92 = ISZERO vd91
    0xd93: vd93 = ISZERO vd92
    0xd94: vd94 = ISZERO vd93
    0xd95: vd95(0xd9d) = CONST 
    0xd98: JUMPI vd95(0xd9d), vd94

    Begin block 0xd99
    prev=[0xd50], succ=[]
    =================================
    0xd99: vd99(0x0) = CONST 
    0xd9c: REVERT vd99(0x0), vd99(0x0)

    Begin block 0xd9d
    prev=[0xd50], succ=[0xe24, 0xe28]
    =================================
    0xd9e: vd9e(0x2) = CONST 
    0xda0: vda0(0x0) = CONST 
    0xda3: vda3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdb8: vdb8 = AND vda3(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xdb9: vdb9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdce: vdce = AND vdb9(0xffffffffffffffffffffffffffffffffffffffff), vdb8
    0xdd0: MSTORE vda0(0x0), vdce
    0xdd1: vdd1(0x20) = CONST 
    0xdd3: vdd3(0x20) = ADD vdd1(0x20), vda0(0x0)
    0xdd6: MSTORE vdd3(0x20), vd9e(0x2)
    0xdd7: vdd7(0x20) = CONST 
    0xdd9: vdd9(0x40) = ADD vdd7(0x20), vdd3(0x20)
    0xdda: vdda(0x0) = CONST 
    0xddc: vddc = SHA3 vdda(0x0), vdd9(0x40)
    0xddd: vddd(0x0) = CONST 
    0xddf: vddf = CALLER 
    0xde0: vde0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf5: vdf5 = AND vde0(0xffffffffffffffffffffffffffffffffffffffff), vddf
    0xdf6: vdf6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe0b: ve0b = AND vdf6(0xffffffffffffffffffffffffffffffffffffffff), vdf5
    0xe0d: MSTORE vddd(0x0), ve0b
    0xe0e: ve0e(0x20) = CONST 
    0xe10: ve10(0x20) = ADD ve0e(0x20), vddd(0x0)
    0xe13: MSTORE ve10(0x20), vddc
    0xe14: ve14(0x20) = CONST 
    0xe16: ve16(0x40) = ADD ve14(0x20), ve10(0x20)
    0xe17: ve17(0x0) = CONST 
    0xe19: ve19 = SHA3 ve17(0x0), ve16(0x40)
    0xe1a: ve1a = SLOAD ve19
    0xe1c: ve1c = GT v64c, ve1a
    0xe1d: ve1d = ISZERO ve1c
    0xe1e: ve1e = ISZERO ve1d
    0xe1f: ve1f = ISZERO ve1e
    0xe20: ve20(0xe28) = CONST 
    0xe23: JUMPI ve20(0xe28), ve1f

    Begin block 0xe24
    prev=[0xd9d], succ=[]
    =================================
    0xe24: ve24(0x0) = CONST 
    0xe27: REVERT ve24(0x0), ve24(0x0)

    Begin block 0xe28
    prev=[0xd9d], succ=[0xe79]
    =================================
    0xe29: ve29(0xe79) = CONST 
    0xe2d: ve2d(0x0) = CONST 
    0xe31: ve31(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe46: ve46 = AND ve31(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xe47: ve47(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe5c: ve5c = AND ve47(0xffffffffffffffffffffffffffffffffffffffff), ve46
    0xe5e: MSTORE ve2d(0x0), ve5c
    0xe5f: ve5f(0x20) = CONST 
    0xe61: ve61(0x20) = ADD ve5f(0x20), ve2d(0x0)
    0xe64: MSTORE ve61(0x20), ve2d(0x0)
    0xe65: ve65(0x20) = CONST 
    0xe67: ve67(0x40) = ADD ve65(0x20), ve61(0x20)
    0xe68: ve68(0x0) = CONST 
    0xe6a: ve6a = SHA3 ve68(0x0), ve67(0x40)
    0xe6b: ve6b = SLOAD ve6a
    0xe6c: ve6c(0xbc5) = CONST 
    0xe72: ve72(0xffffffff) = CONST 
    0xe77: ve77(0xbc5) = AND ve72(0xffffffff), ve6c(0xbc5)
    0xe78: ve78_0 = CALLPRIVATE ve77(0xbc5), v64c, ve6b, ve29(0xe79)

    Begin block 0xe79
    prev=[0xe28], succ=[0xf0c]
    =================================
    0xe7a: ve7a(0x0) = CONST 
    0xe7e: ve7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe93: ve93 = AND ve7e(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xe94: ve94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xea9: vea9 = AND ve94(0xffffffffffffffffffffffffffffffffffffffff), ve93
    0xeab: MSTORE ve7a(0x0), vea9
    0xeac: veac(0x20) = CONST 
    0xeae: veae(0x20) = ADD veac(0x20), ve7a(0x0)
    0xeb1: MSTORE veae(0x20), ve7a(0x0)
    0xeb2: veb2(0x20) = CONST 
    0xeb4: veb4(0x40) = ADD veb2(0x20), veae(0x20)
    0xeb5: veb5(0x0) = CONST 
    0xeb7: veb7 = SHA3 veb5(0x0), veb4(0x40)
    0xeba: SSTORE veb7, ve78_0
    0xebc: vebc(0xf0c) = CONST 
    0xec0: vec0(0x0) = CONST 
    0xec4: vec4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xed9: ved9 = AND vec4(0xffffffffffffffffffffffffffffffffffffffff), v642
    0xeda: veda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeef: veef = AND veda(0xffffffffffffffffffffffffffffffffffffffff), ved9
    0xef1: MSTORE vec0(0x0), veef
    0xef2: vef2(0x20) = CONST 
    0xef4: vef4(0x20) = ADD vef2(0x20), vec0(0x0)
    0xef7: MSTORE vef4(0x20), vec0(0x0)
    0xef8: vef8(0x20) = CONST 
    0xefa: vefa(0x40) = ADD vef8(0x20), vef4(0x20)
    0xefb: vefb(0x0) = CONST 
    0xefd: vefd = SHA3 vefb(0x0), vefa(0x40)
    0xefe: vefe = SLOAD vefd
    0xeff: veff(0xba9) = CONST 
    0xf05: vf05(0xffffffff) = CONST 
    0xf0a: vf0a(0xba9) = AND vf05(0xffffffff), veff(0xba9)
    0xf0b: vf0b_0 = CALLPRIVATE vf0a(0xba9), v64c, vefe, vebc(0xf0c)

    Begin block 0xf0c
    prev=[0xe79], succ=[0xfdd]
    =================================
    0xf0d: vf0d(0x0) = CONST 
    0xf11: vf11(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf26: vf26 = AND vf11(0xffffffffffffffffffffffffffffffffffffffff), v642
    0xf27: vf27(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf3c: vf3c = AND vf27(0xffffffffffffffffffffffffffffffffffffffff), vf26
    0xf3e: MSTORE vf0d(0x0), vf3c
    0xf3f: vf3f(0x20) = CONST 
    0xf41: vf41(0x20) = ADD vf3f(0x20), vf0d(0x0)
    0xf44: MSTORE vf41(0x20), vf0d(0x0)
    0xf45: vf45(0x20) = CONST 
    0xf47: vf47(0x40) = ADD vf45(0x20), vf41(0x20)
    0xf48: vf48(0x0) = CONST 
    0xf4a: vf4a = SHA3 vf48(0x0), vf47(0x40)
    0xf4d: SSTORE vf4a, vf0b_0
    0xf4f: vf4f(0xfdd) = CONST 
    0xf53: vf53(0x2) = CONST 
    0xf55: vf55(0x0) = CONST 
    0xf58: vf58(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf6d: vf6d = AND vf58(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xf6e: vf6e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf83: vf83 = AND vf6e(0xffffffffffffffffffffffffffffffffffffffff), vf6d
    0xf85: MSTORE vf55(0x0), vf83
    0xf86: vf86(0x20) = CONST 
    0xf88: vf88(0x20) = ADD vf86(0x20), vf55(0x0)
    0xf8b: MSTORE vf88(0x20), vf53(0x2)
    0xf8c: vf8c(0x20) = CONST 
    0xf8e: vf8e(0x40) = ADD vf8c(0x20), vf88(0x20)
    0xf8f: vf8f(0x0) = CONST 
    0xf91: vf91 = SHA3 vf8f(0x0), vf8e(0x40)
    0xf92: vf92(0x0) = CONST 
    0xf94: vf94 = CALLER 
    0xf95: vf95(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfaa: vfaa = AND vf95(0xffffffffffffffffffffffffffffffffffffffff), vf94
    0xfab: vfab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfc0: vfc0 = AND vfab(0xffffffffffffffffffffffffffffffffffffffff), vfaa
    0xfc2: MSTORE vf92(0x0), vfc0
    0xfc3: vfc3(0x20) = CONST 
    0xfc5: vfc5(0x20) = ADD vfc3(0x20), vf92(0x0)
    0xfc8: MSTORE vfc5(0x20), vf91
    0xfc9: vfc9(0x20) = CONST 
    0xfcb: vfcb(0x40) = ADD vfc9(0x20), vfc5(0x20)
    0xfcc: vfcc(0x0) = CONST 
    0xfce: vfce = SHA3 vfcc(0x0), vfcb(0x40)
    0xfcf: vfcf = SLOAD vfce
    0xfd0: vfd0(0xbc5) = CONST 
    0xfd6: vfd6(0xffffffff) = CONST 
    0xfdb: vfdb(0xbc5) = AND vfd6(0xffffffff), vfd0(0xbc5)
    0xfdc: vfdc_0 = CALLPRIVATE vfdb(0xbc5), v64c, vfcf, vf4f(0xfdd)

    Begin block 0xfdd
    prev=[0xf0c], succ=[0x65c]
    =================================
    0xfde: vfde(0x2) = CONST 
    0xfe0: vfe0(0x0) = CONST 
    0xfe3: vfe3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xff8: vff8 = AND vfe3(0xffffffffffffffffffffffffffffffffffffffff), v622
    0xff9: vff9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x100e: v100e = AND vff9(0xffffffffffffffffffffffffffffffffffffffff), vff8
    0x1010: MSTORE vfe0(0x0), v100e
    0x1011: v1011(0x20) = CONST 
    0x1013: v1013(0x20) = ADD v1011(0x20), vfe0(0x0)
    0x1016: MSTORE v1013(0x20), vfde(0x2)
    0x1017: v1017(0x20) = CONST 
    0x1019: v1019(0x40) = ADD v1017(0x20), v1013(0x20)
    0x101a: v101a(0x0) = CONST 
    0x101c: v101c = SHA3 v101a(0x0), v1019(0x40)
    0x101d: v101d(0x0) = CONST 
    0x101f: v101f = CALLER 
    0x1020: v1020(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1035: v1035 = AND v1020(0xffffffffffffffffffffffffffffffffffffffff), v101f
    0x1036: v1036(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x104b: v104b = AND v1036(0xffffffffffffffffffffffffffffffffffffffff), v1035
    0x104d: MSTORE v101d(0x0), v104b
    0x104e: v104e(0x20) = CONST 
    0x1050: v1050(0x20) = ADD v104e(0x20), v101d(0x0)
    0x1053: MSTORE v1050(0x20), v101c
    0x1054: v1054(0x20) = CONST 
    0x1056: v1056(0x40) = ADD v1054(0x20), v1050(0x20)
    0x1057: v1057(0x0) = CONST 
    0x1059: v1059 = SHA3 v1057(0x0), v1056(0x40)
    0x105c: SSTORE v1059, vfdc_0
    0x105f: v105f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1074: v1074 = AND v105f(0xffffffffffffffffffffffffffffffffffffffff), v642
    0x1076: v1076(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x108b: v108b = AND v1076(0xffffffffffffffffffffffffffffffffffffffff), v622
    0x108c: v108c(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x10ae: v10ae(0x40) = CONST 
    0x10b0: v10b0 = MLOAD v10ae(0x40)
    0x10b4: MSTORE v10b0, v64c
    0x10b5: v10b5(0x20) = CONST 
    0x10b7: v10b7 = ADD v10b5(0x20), v10b0
    0x10bb: v10bb(0x40) = CONST 
    0x10bd: v10bd = MLOAD v10bb(0x40)
    0x10c0: v10c0(0x20) = SUB v10b7, v10bd
    0x10c2: LOG3 v10bd, v10c0(0x20), v108c(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v108b, v1074
    0x10c3: v10c3(0x1) = CONST 
    0x10cc: JUMP v5ff(0x65c)

    Begin block 0x65c
    prev=[0xfdd], succ=[]
    =================================
    0x65d: v65d(0x40) = CONST 
    0x65f: v65f = MLOAD v65d(0x40)
    0x662: v662(0x0) = ISZERO v10c3(0x1)
    0x663: v663(0x1) = ISZERO v662(0x0)
    0x664: v664(0x0) = ISZERO v663(0x1)
    0x665: v665(0x1) = ISZERO v664(0x0)
    0x667: MSTORE v65f, v665(0x1)
    0x668: v668(0x20) = CONST 
    0x66a: v66a = ADD v668(0x20), v65f
    0x66e: v66e(0x40) = CONST 
    0x670: v670 = MLOAD v66e(0x40)
    0x673: v673(0x20) = SUB v66a, v670
    0x675: RETURN v670, v673(0x20)

}

function DepositEther()() public {
    Begin block 0x676
    prev=[], succ=[0x10cd]
    =================================
    0x677: v677(0x67e) = CONST 
    0x67a: v67a(0x10cd) = CONST 
    0x67d: JUMP v67a(0x10cd)

    Begin block 0x10cd
    prev=[0x676], succ=[0x10f2, 0x115f]
    =================================
    0x10ce: v10ce(0x0) = CONST 
    0x10d0: v10d0 = CALLVALUE 
    0x10d3: v10d3 = CALLER 
    0x10d4: v10d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10e9: v10e9 = AND v10d4(0xffffffffffffffffffffffffffffffffffffffff), v10d3
    0x10ea: v10ea = BALANCE v10e9
    0x10ec: v10ec = GT v10d0, v10ea
    0x10ed: v10ed = ISZERO v10ec
    0x10ee: v10ee(0x115f) = CONST 
    0x10f1: JUMPI v10ee(0x115f), v10ed

    Begin block 0x10f2
    prev=[0x10cd], succ=[]
    =================================
    0x10f2: v10f2(0x40) = CONST 
    0x10f4: v10f4 = MLOAD v10f2(0x40)
    0x10f5: v10f5(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1117: MSTORE v10f4, v10f5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1118: v1118(0x4) = CONST 
    0x111a: v111a = ADD v1118(0x4), v10f4
    0x111d: v111d(0x20) = CONST 
    0x111f: v111f = ADD v111d(0x20), v111a
    0x1122: v1122(0x20) = SUB v111f, v111a
    0x1124: MSTORE v111a, v1122(0x20)
    0x1125: v1125(0x10) = CONST 
    0x1128: MSTORE v111f, v1125(0x10)
    0x1129: v1129(0x20) = CONST 
    0x112b: v112b = ADD v1129(0x20), v111f
    0x112d: v112d(0x416d6f756e7420756e6d61746368656400000000000000000000000000000000) = CONST 
    0x114f: MSTORE v112b, v112d(0x416d6f756e7420756e6d61746368656400000000000000000000000000000000)
    0x1151: v1151(0x20) = CONST 
    0x1153: v1153 = ADD v1151(0x20), v112b
    0x1157: v1157(0x40) = CONST 
    0x1159: v1159 = MLOAD v1157(0x40)
    0x115c: v115c(0x64) = SUB v1153, v1159
    0x115e: REVERT v1159, v115c(0x64)

    Begin block 0x115f
    prev=[0x10cd], succ=[0x11a8]
    =================================
    0x1160: v1160(0x11a8) = CONST 
    0x1163: v1163(0x4) = CONST 
    0x1165: v1165(0x0) = CONST 
    0x1167: v1167 = ADDRESS 
    0x1168: v1168(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x117d: v117d = AND v1168(0xffffffffffffffffffffffffffffffffffffffff), v1167
    0x117e: v117e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1193: v1193 = AND v117e(0xffffffffffffffffffffffffffffffffffffffff), v117d
    0x1195: MSTORE v1165(0x0), v1193
    0x1196: v1196(0x20) = CONST 
    0x1198: v1198(0x20) = ADD v1196(0x20), v1165(0x0)
    0x119b: MSTORE v1198(0x20), v1163(0x4)
    0x119c: v119c(0x20) = CONST 
    0x119e: v119e(0x40) = ADD v119c(0x20), v1198(0x20)
    0x119f: v119f(0x0) = CONST 
    0x11a1: v11a1 = SHA3 v119f(0x0), v119e(0x40)
    0x11a2: v11a2 = SLOAD v11a1
    0x11a4: v11a4(0xba9) = CONST 
    0x11a7: v11a7_0 = CALLPRIVATE v11a4(0xba9), v10d0, v11a2, v1160(0x11a8)

    Begin block 0x11a8
    prev=[0x115f], succ=[0x67e]
    =================================
    0x11a9: v11a9(0x4) = CONST 
    0x11ab: v11ab(0x0) = CONST 
    0x11ad: v11ad = ADDRESS 
    0x11ae: v11ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11c3: v11c3 = AND v11ae(0xffffffffffffffffffffffffffffffffffffffff), v11ad
    0x11c4: v11c4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11d9: v11d9 = AND v11c4(0xffffffffffffffffffffffffffffffffffffffff), v11c3
    0x11db: MSTORE v11ab(0x0), v11d9
    0x11dc: v11dc(0x20) = CONST 
    0x11de: v11de(0x20) = ADD v11dc(0x20), v11ab(0x0)
    0x11e1: MSTORE v11de(0x20), v11a9(0x4)
    0x11e2: v11e2(0x20) = CONST 
    0x11e4: v11e4(0x40) = ADD v11e2(0x20), v11de(0x20)
    0x11e5: v11e5(0x0) = CONST 
    0x11e7: v11e7 = SHA3 v11e5(0x0), v11e4(0x40)
    0x11ea: SSTORE v11e7, v11a7_0
    0x11ed: JUMP v677(0x67e)

    Begin block 0x67e
    prev=[0x11a8], succ=[]
    =================================
    0x67f: STOP 

}

function decimals()() public {
    Begin block 0x680
    prev=[], succ=[0x688, 0x68c]
    =================================
    0x681: v681 = CALLVALUE 
    0x683: v683 = ISZERO v681
    0x684: v684(0x68c) = CONST 
    0x687: JUMPI v684(0x68c), v683

    Begin block 0x688
    prev=[0x680], succ=[]
    =================================
    0x688: v688(0x0) = CONST 
    0x68b: REVERT v688(0x0), v688(0x0)

    Begin block 0x68c
    prev=[0x680], succ=[0x11ee]
    =================================
    0x68e: v68e(0x695) = CONST 
    0x691: v691(0x11ee) = CONST 
    0x694: JUMP v691(0x11ee)

    Begin block 0x11ee
    prev=[0x68c], succ=[0x695]
    =================================
    0x11ef: v11ef(0x8) = CONST 
    0x11f2: JUMP v68e(0x695)

    Begin block 0x695
    prev=[0x11ee], succ=[]
    =================================
    0x696: v696(0x40) = CONST 
    0x698: v698 = MLOAD v696(0x40)
    0x69b: v69b(0xffffffff) = CONST 
    0x6a0: v6a0(0x8) = AND v69b(0xffffffff), v11ef(0x8)
    0x6a1: v6a1(0xffffffff) = CONST 
    0x6a6: v6a6(0x8) = AND v6a1(0xffffffff), v6a0(0x8)
    0x6a8: MSTORE v698, v6a6(0x8)
    0x6a9: v6a9(0x20) = CONST 
    0x6ab: v6ab = ADD v6a9(0x20), v698
    0x6af: v6af(0x40) = CONST 
    0x6b1: v6b1 = MLOAD v6af(0x40)
    0x6b4: v6b4(0x20) = SUB v6ab, v6b1
    0x6b6: RETURN v6b1, v6b4(0x20)

}

function cap()() public {
    Begin block 0x6b7
    prev=[], succ=[0x6bf, 0x6c3]
    =================================
    0x6b8: v6b8 = CALLVALUE 
    0x6ba: v6ba = ISZERO v6b8
    0x6bb: v6bb(0x6c3) = CONST 
    0x6be: JUMPI v6bb(0x6c3), v6ba

    Begin block 0x6bf
    prev=[0x6b7], succ=[]
    =================================
    0x6bf: v6bf(0x0) = CONST 
    0x6c2: REVERT v6bf(0x0), v6bf(0x0)

    Begin block 0x6c3
    prev=[0x6b7], succ=[0x11f3]
    =================================
    0x6c5: v6c5(0x6cc) = CONST 
    0x6c8: v6c8(0x11f3) = CONST 
    0x6cb: JUMP v6c8(0x11f3)

    Begin block 0x11f3
    prev=[0x6c3], succ=[0x6cc]
    =================================
    0x11f4: v11f4(0x2386f26fc10000) = CONST 
    0x11fd: JUMP v6c5(0x6cc)

    Begin block 0x6cc
    prev=[0x11f3], succ=[]
    =================================
    0x6cd: v6cd(0x40) = CONST 
    0x6cf: v6cf = MLOAD v6cd(0x40)
    0x6d3: MSTORE v6cf, v11f4(0x2386f26fc10000)
    0x6d4: v6d4(0x20) = CONST 
    0x6d6: v6d6 = ADD v6d4(0x20), v6cf
    0x6da: v6da(0x40) = CONST 
    0x6dc: v6dc = MLOAD v6da(0x40)
    0x6df: v6df(0x20) = SUB v6d6, v6dc
    0x6e1: RETURN v6dc, v6df(0x20)

}

function tokensSold()() public {
    Begin block 0x6e2
    prev=[], succ=[0x6ea, 0x6ee]
    =================================
    0x6e3: v6e3 = CALLVALUE 
    0x6e5: v6e5 = ISZERO v6e3
    0x6e6: v6e6(0x6ee) = CONST 
    0x6e9: JUMPI v6e6(0x6ee), v6e5

    Begin block 0x6ea
    prev=[0x6e2], succ=[]
    =================================
    0x6ea: v6ea(0x0) = CONST 
    0x6ed: REVERT v6ea(0x0), v6ea(0x0)

    Begin block 0x6ee
    prev=[0x6e2], succ=[0x11fe]
    =================================
    0x6f0: v6f0(0x6f7) = CONST 
    0x6f3: v6f3(0x11fe) = CONST 
    0x6f6: JUMP v6f3(0x11fe)

    Begin block 0x11fe
    prev=[0x6ee], succ=[0x6f7]
    =================================
    0x11ff: v11ff(0x5) = CONST 
    0x1201: v1201 = SLOAD v11ff(0x5)
    0x1203: JUMP v6f0(0x6f7)

    Begin block 0x6f7
    prev=[0x11fe], succ=[]
    =================================
    0x6f8: v6f8(0x40) = CONST 
    0x6fa: v6fa = MLOAD v6f8(0x40)
    0x6fe: MSTORE v6fa, v1201
    0x6ff: v6ff(0x20) = CONST 
    0x701: v701 = ADD v6ff(0x20), v6fa
    0x705: v705(0x40) = CONST 
    0x707: v707 = MLOAD v705(0x40)
    0x70a: v70a(0x20) = SUB v701, v707
    0x70c: RETURN v707, v70a(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x70d
    prev=[], succ=[0x715, 0x719]
    =================================
    0x70e: v70e = CALLVALUE 
    0x710: v710 = ISZERO v70e
    0x711: v711(0x719) = CONST 
    0x714: JUMPI v711(0x719), v710

    Begin block 0x715
    prev=[0x70d], succ=[]
    =================================
    0x715: v715(0x0) = CONST 
    0x718: REVERT v715(0x0), v715(0x0)

    Begin block 0x719
    prev=[0x70d], succ=[0x1204]
    =================================
    0x71b: v71b(0x758) = CONST 
    0x71e: v71e(0x4) = CONST 
    0x721: v721 = CALLDATASIZE 
    0x722: v722 = SUB v721, v71e(0x4)
    0x724: v724 = ADD v71e(0x4), v722
    0x728: v728 = CALLDATALOAD v71e(0x4)
    0x729: v729(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x73e: v73e = AND v729(0xffffffffffffffffffffffffffffffffffffffff), v728
    0x740: v740(0x20) = CONST 
    0x742: v742(0x24) = ADD v740(0x20), v71e(0x4)
    0x748: v748 = CALLDATALOAD v742(0x24)
    0x74a: v74a(0x20) = CONST 
    0x74c: v74c(0x44) = ADD v74a(0x20), v742(0x24)
    0x754: v754(0x1204) = CONST 
    0x757: JUMP v754(0x1204)

    Begin block 0x1204
    prev=[0x719], succ=[0x128f, 0x1315]
    =================================
    0x1205: v1205(0x0) = CONST 
    0x1208: v1208(0x2) = CONST 
    0x120a: v120a(0x0) = CONST 
    0x120c: v120c = CALLER 
    0x120d: v120d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1222: v1222 = AND v120d(0xffffffffffffffffffffffffffffffffffffffff), v120c
    0x1223: v1223(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1238: v1238 = AND v1223(0xffffffffffffffffffffffffffffffffffffffff), v1222
    0x123a: MSTORE v120a(0x0), v1238
    0x123b: v123b(0x20) = CONST 
    0x123d: v123d(0x20) = ADD v123b(0x20), v120a(0x0)
    0x1240: MSTORE v123d(0x20), v1208(0x2)
    0x1241: v1241(0x20) = CONST 
    0x1243: v1243(0x40) = ADD v1241(0x20), v123d(0x20)
    0x1244: v1244(0x0) = CONST 
    0x1246: v1246 = SHA3 v1244(0x0), v1243(0x40)
    0x1247: v1247(0x0) = CONST 
    0x124a: v124a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x125f: v125f = AND v124a(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x1260: v1260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1275: v1275 = AND v1260(0xffffffffffffffffffffffffffffffffffffffff), v125f
    0x1277: MSTORE v1247(0x0), v1275
    0x1278: v1278(0x20) = CONST 
    0x127a: v127a(0x20) = ADD v1278(0x20), v1247(0x0)
    0x127d: MSTORE v127a(0x20), v1246
    0x127e: v127e(0x20) = CONST 
    0x1280: v1280(0x40) = ADD v127e(0x20), v127a(0x20)
    0x1281: v1281(0x0) = CONST 
    0x1283: v1283 = SHA3 v1281(0x0), v1280(0x40)
    0x1284: v1284 = SLOAD v1283
    0x1289: v1289 = GT v748, v1284
    0x128a: v128a = ISZERO v1289
    0x128b: v128b(0x1315) = CONST 
    0x128e: JUMPI v128b(0x1315), v128a

    Begin block 0x128f
    prev=[0x1204], succ=[0x13a9]
    =================================
    0x128f: v128f(0x0) = CONST 
    0x1291: v1291(0x2) = CONST 
    0x1293: v1293(0x0) = CONST 
    0x1295: v1295 = CALLER 
    0x1296: v1296(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12ab: v12ab = AND v1296(0xffffffffffffffffffffffffffffffffffffffff), v1295
    0x12ac: v12ac(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12c1: v12c1 = AND v12ac(0xffffffffffffffffffffffffffffffffffffffff), v12ab
    0x12c3: MSTORE v1293(0x0), v12c1
    0x12c4: v12c4(0x20) = CONST 
    0x12c6: v12c6(0x20) = ADD v12c4(0x20), v1293(0x0)
    0x12c9: MSTORE v12c6(0x20), v1291(0x2)
    0x12ca: v12ca(0x20) = CONST 
    0x12cc: v12cc(0x40) = ADD v12ca(0x20), v12c6(0x20)
    0x12cd: v12cd(0x0) = CONST 
    0x12cf: v12cf = SHA3 v12cd(0x0), v12cc(0x40)
    0x12d0: v12d0(0x0) = CONST 
    0x12d3: v12d3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12e8: v12e8 = AND v12d3(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x12e9: v12e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12fe: v12fe = AND v12e9(0xffffffffffffffffffffffffffffffffffffffff), v12e8
    0x1300: MSTORE v12d0(0x0), v12fe
    0x1301: v1301(0x20) = CONST 
    0x1303: v1303(0x20) = ADD v1301(0x20), v12d0(0x0)
    0x1306: MSTORE v1303(0x20), v12cf
    0x1307: v1307(0x20) = CONST 
    0x1309: v1309(0x40) = ADD v1307(0x20), v1303(0x20)
    0x130a: v130a(0x0) = CONST 
    0x130c: v130c = SHA3 v130a(0x0), v1309(0x40)
    0x130f: SSTORE v130c, v128f(0x0)
    0x1311: v1311(0x13a9) = CONST 
    0x1314: JUMP v1311(0x13a9)

    Begin block 0x13a9
    prev=[0x128f, 0x1328], succ=[0x758]
    =================================
    0x13ab: v13ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13c0: v13c0 = AND v13ab(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x13c1: v13c1 = CALLER 
    0x13c2: v13c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13d7: v13d7 = AND v13c2(0xffffffffffffffffffffffffffffffffffffffff), v13c1
    0x13d8: v13d8(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x13f9: v13f9(0x2) = CONST 
    0x13fb: v13fb(0x0) = CONST 
    0x13fd: v13fd = CALLER 
    0x13fe: v13fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1413: v1413 = AND v13fe(0xffffffffffffffffffffffffffffffffffffffff), v13fd
    0x1414: v1414(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1429: v1429 = AND v1414(0xffffffffffffffffffffffffffffffffffffffff), v1413
    0x142b: MSTORE v13fb(0x0), v1429
    0x142c: v142c(0x20) = CONST 
    0x142e: v142e(0x20) = ADD v142c(0x20), v13fb(0x0)
    0x1431: MSTORE v142e(0x20), v13f9(0x2)
    0x1432: v1432(0x20) = CONST 
    0x1434: v1434(0x40) = ADD v1432(0x20), v142e(0x20)
    0x1435: v1435(0x0) = CONST 
    0x1437: v1437 = SHA3 v1435(0x0), v1434(0x40)
    0x1438: v1438(0x0) = CONST 
    0x143b: v143b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1450: v1450 = AND v143b(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x1451: v1451(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1466: v1466 = AND v1451(0xffffffffffffffffffffffffffffffffffffffff), v1450
    0x1468: MSTORE v1438(0x0), v1466
    0x1469: v1469(0x20) = CONST 
    0x146b: v146b(0x20) = ADD v1469(0x20), v1438(0x0)
    0x146e: MSTORE v146b(0x20), v1437
    0x146f: v146f(0x20) = CONST 
    0x1471: v1471(0x40) = ADD v146f(0x20), v146b(0x20)
    0x1472: v1472(0x0) = CONST 
    0x1474: v1474 = SHA3 v1472(0x0), v1471(0x40)
    0x1475: v1475 = SLOAD v1474
    0x1476: v1476(0x40) = CONST 
    0x1478: v1478 = MLOAD v1476(0x40)
    0x147c: MSTORE v1478, v1475
    0x147d: v147d(0x20) = CONST 
    0x147f: v147f = ADD v147d(0x20), v1478
    0x1483: v1483(0x40) = CONST 
    0x1485: v1485 = MLOAD v1483(0x40)
    0x1488: v1488(0x20) = SUB v147f, v1485
    0x148a: LOG3 v1485, v1488(0x20), v13d8(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v13d7, v13c0
    0x148b: v148b(0x1) = CONST 
    0x1494: JUMP v71b(0x758)

    Begin block 0x758
    prev=[0x13a9], succ=[]
    =================================
    0x759: v759(0x40) = CONST 
    0x75b: v75b = MLOAD v759(0x40)
    0x75e: v75e(0x0) = ISZERO v148b(0x1)
    0x75f: v75f(0x1) = ISZERO v75e(0x0)
    0x760: v760(0x0) = ISZERO v75f(0x1)
    0x761: v761(0x1) = ISZERO v760(0x0)
    0x763: MSTORE v75b, v761(0x1)
    0x764: v764(0x20) = CONST 
    0x766: v766 = ADD v764(0x20), v75b
    0x76a: v76a(0x40) = CONST 
    0x76c: v76c = MLOAD v76a(0x40)
    0x76f: v76f(0x20) = SUB v766, v76c
    0x771: RETURN v76c, v76f(0x20)

    Begin block 0x1315
    prev=[0x1204], succ=[0x1328]
    =================================
    0x1316: v1316(0x1328) = CONST 
    0x131b: v131b(0xbc5) = CONST 
    0x1321: v1321(0xffffffff) = CONST 
    0x1326: v1326(0xbc5) = AND v1321(0xffffffff), v131b(0xbc5)
    0x1327: v1327_0 = CALLPRIVATE v1326(0xbc5), v748, v1284, v1316(0x1328)

    Begin block 0x1328
    prev=[0x1315], succ=[0x13a9]
    =================================
    0x1329: v1329(0x2) = CONST 
    0x132b: v132b(0x0) = CONST 
    0x132d: v132d = CALLER 
    0x132e: v132e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1343: v1343 = AND v132e(0xffffffffffffffffffffffffffffffffffffffff), v132d
    0x1344: v1344(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1359: v1359 = AND v1344(0xffffffffffffffffffffffffffffffffffffffff), v1343
    0x135b: MSTORE v132b(0x0), v1359
    0x135c: v135c(0x20) = CONST 
    0x135e: v135e(0x20) = ADD v135c(0x20), v132b(0x0)
    0x1361: MSTORE v135e(0x20), v1329(0x2)
    0x1362: v1362(0x20) = CONST 
    0x1364: v1364(0x40) = ADD v1362(0x20), v135e(0x20)
    0x1365: v1365(0x0) = CONST 
    0x1367: v1367 = SHA3 v1365(0x0), v1364(0x40)
    0x1368: v1368(0x0) = CONST 
    0x136b: v136b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1380: v1380 = AND v136b(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x1381: v1381(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1396: v1396 = AND v1381(0xffffffffffffffffffffffffffffffffffffffff), v1380
    0x1398: MSTORE v1368(0x0), v1396
    0x1399: v1399(0x20) = CONST 
    0x139b: v139b(0x20) = ADD v1399(0x20), v1368(0x0)
    0x139e: MSTORE v139b(0x20), v1367
    0x139f: v139f(0x20) = CONST 
    0x13a1: v13a1(0x40) = ADD v139f(0x20), v139b(0x20)
    0x13a2: v13a2(0x0) = CONST 
    0x13a4: v13a4 = SHA3 v13a2(0x0), v13a1(0x40)
    0x13a7: SSTORE v13a4, v1327_0
    0x8592: v8592(0x13a9) = CONST 
    0x85b2: JUMP v8592(0x13a9)

}

function balanceOf(address)() public {
    Begin block 0x772
    prev=[], succ=[0x77a, 0x77e]
    =================================
    0x773: v773 = CALLVALUE 
    0x775: v775 = ISZERO v773
    0x776: v776(0x77e) = CONST 
    0x779: JUMPI v776(0x77e), v775

    Begin block 0x77a
    prev=[0x772], succ=[]
    =================================
    0x77a: v77a(0x0) = CONST 
    0x77d: REVERT v77a(0x0), v77a(0x0)

    Begin block 0x77e
    prev=[0x772], succ=[0x1495]
    =================================
    0x780: v780(0x7b3) = CONST 
    0x783: v783(0x4) = CONST 
    0x786: v786 = CALLDATASIZE 
    0x787: v787 = SUB v786, v783(0x4)
    0x789: v789 = ADD v783(0x4), v787
    0x78d: v78d = CALLDATALOAD v783(0x4)
    0x78e: v78e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7a3: v7a3 = AND v78e(0xffffffffffffffffffffffffffffffffffffffff), v78d
    0x7a5: v7a5(0x20) = CONST 
    0x7a7: v7a7(0x24) = ADD v7a5(0x20), v783(0x4)
    0x7af: v7af(0x1495) = CONST 
    0x7b2: JUMP v7af(0x1495)

    Begin block 0x1495
    prev=[0x77e], succ=[0x7b3]
    =================================
    0x1496: v1496(0x0) = CONST 
    0x1499: v1499(0x0) = CONST 
    0x149c: v149c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14b1: v14b1 = AND v149c(0xffffffffffffffffffffffffffffffffffffffff), v7a3
    0x14b2: v14b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14c7: v14c7 = AND v14b2(0xffffffffffffffffffffffffffffffffffffffff), v14b1
    0x14c9: MSTORE v1499(0x0), v14c7
    0x14ca: v14ca(0x20) = CONST 
    0x14cc: v14cc(0x20) = ADD v14ca(0x20), v1499(0x0)
    0x14cf: MSTORE v14cc(0x20), v1496(0x0)
    0x14d0: v14d0(0x20) = CONST 
    0x14d2: v14d2(0x40) = ADD v14d0(0x20), v14cc(0x20)
    0x14d3: v14d3(0x0) = CONST 
    0x14d5: v14d5 = SHA3 v14d3(0x0), v14d2(0x40)
    0x14d6: v14d6 = SLOAD v14d5
    0x14dc: JUMP v780(0x7b3)

    Begin block 0x7b3
    prev=[0x1495], succ=[]
    =================================
    0x7b4: v7b4(0x40) = CONST 
    0x7b6: v7b6 = MLOAD v7b4(0x40)
    0x7ba: MSTORE v7b6, v14d6
    0x7bb: v7bb(0x20) = CONST 
    0x7bd: v7bd = ADD v7bb(0x20), v7b6
    0x7c1: v7c1(0x40) = CONST 
    0x7c3: v7c3 = MLOAD v7c1(0x40)
    0x7c6: v7c6(0x20) = SUB v7bd, v7c3
    0x7c8: RETURN v7c3, v7c6(0x20)

}

function startIco()() public {
    Begin block 0x7c9
    prev=[], succ=[0x7d1, 0x7d5]
    =================================
    0x7ca: v7ca = CALLVALUE 
    0x7cc: v7cc = ISZERO v7ca
    0x7cd: v7cd(0x7d5) = CONST 
    0x7d0: JUMPI v7cd(0x7d5), v7cc

    Begin block 0x7d1
    prev=[0x7c9], succ=[]
    =================================
    0x7d1: v7d1(0x0) = CONST 
    0x7d4: REVERT v7d1(0x0), v7d1(0x0)

    Begin block 0x7d5
    prev=[0x7c9], succ=[0x14dd]
    =================================
    0x7d7: v7d7(0x7de) = CONST 
    0x7da: v7da(0x14dd) = CONST 
    0x7dd: JUMP v7da(0x14dd)

    Begin block 0x14dd
    prev=[0x7d5], succ=[0x1535, 0x1539]
    =================================
    0x14de: v14de(0x7) = CONST 
    0x14e0: v14e0(0x0) = CONST 
    0x14e3: v14e3 = SLOAD v14de(0x7)
    0x14e5: v14e5(0x100) = CONST 
    0x14e8: v14e8(0x1) = EXP v14e5(0x100), v14e0(0x0)
    0x14ea: v14ea = DIV v14e3, v14e8(0x1)
    0x14eb: v14eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1500: v1500 = AND v14eb(0xffffffffffffffffffffffffffffffffffffffff), v14ea
    0x1501: v1501(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1516: v1516 = AND v1501(0xffffffffffffffffffffffffffffffffffffffff), v1500
    0x1517: v1517 = CALLER 
    0x1518: v1518(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x152d: v152d = AND v1518(0xffffffffffffffffffffffffffffffffffffffff), v1517
    0x152e: v152e = EQ v152d, v1516
    0x152f: v152f = ISZERO v152e
    0x1530: v1530 = ISZERO v152f
    0x1531: v1531(0x1539) = CONST 
    0x1534: JUMPI v1531(0x1539), v1530

    Begin block 0x1535
    prev=[0x14dd], succ=[]
    =================================
    0x1535: v1535(0x0) = CONST 
    0x1538: REVERT v1535(0x0), v1535(0x0)

    Begin block 0x1539
    prev=[0x14dd], succ=[0x1544, 0x1545]
    =================================
    0x153a: v153a(0x2) = CONST 
    0x153e: v153e(0x0) = GT v153a(0x2), v153a(0x2)
    0x153f: v153f(0x1) = ISZERO v153e(0x0)
    0x1540: v1540(0x1545) = CONST 
    0x1543: JUMPI v1540(0x1545), v153f(0x1)

    Begin block 0x1544
    prev=[0x1539], succ=[]
    =================================
    0x1544: THROW 

    Begin block 0x1545
    prev=[0x1539], succ=[0x155f, 0x1560]
    =================================
    0x1546: v1546(0x7) = CONST 
    0x1548: v1548(0x14) = CONST 
    0x154b: v154b = SLOAD v1546(0x7)
    0x154d: v154d(0x100) = CONST 
    0x1550: v1550(0x10000000000000000000000000000000000000000) = EXP v154d(0x100), v1548(0x14)
    0x1552: v1552 = DIV v154b, v1550(0x10000000000000000000000000000000000000000)
    0x1553: v1553(0xff) = CONST 
    0x1555: v1555 = AND v1553(0xff), v1552
    0x1556: v1556(0x2) = CONST 
    0x1559: v1559 = GT v1555, v1556(0x2)
    0x155a: v155a = ISZERO v1559
    0x155b: v155b(0x1560) = CONST 
    0x155e: JUMPI v155b(0x1560), v155a

    Begin block 0x155f
    prev=[0x1545], succ=[]
    =================================
    0x155f: THROW 

    Begin block 0x1560
    prev=[0x1545], succ=[0x1569, 0x156d]
    =================================
    0x1561: v1561 = EQ v1555, v153a(0x2)
    0x1562: v1562 = ISZERO v1561
    0x1563: v1563 = ISZERO v1562
    0x1564: v1564 = ISZERO v1563
    0x1565: v1565(0x156d) = CONST 
    0x1568: JUMPI v1565(0x156d), v1564

    Begin block 0x1569
    prev=[0x1560], succ=[]
    =================================
    0x1569: v1569(0x0) = CONST 
    0x156c: REVERT v1569(0x0), v1569(0x0)

    Begin block 0x156d
    prev=[0x1560], succ=[0x158b, 0x158c]
    =================================
    0x156e: v156e(0x1) = CONST 
    0x1570: v1570(0x7) = CONST 
    0x1572: v1572(0x14) = CONST 
    0x1574: v1574(0x100) = CONST 
    0x1577: v1577(0x10000000000000000000000000000000000000000) = EXP v1574(0x100), v1572(0x14)
    0x1579: v1579 = SLOAD v1570(0x7)
    0x157b: v157b(0xff) = CONST 
    0x157d: v157d(0xff0000000000000000000000000000000000000000) = MUL v157b(0xff), v1577(0x10000000000000000000000000000000000000000)
    0x157e: v157e(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v157d(0xff0000000000000000000000000000000000000000)
    0x157f: v157f = AND v157e(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1579
    0x1582: v1582(0x2) = CONST 
    0x1585: v1585(0x0) = GT v156e(0x1), v1582(0x2)
    0x1586: v1586(0x1) = ISZERO v1585(0x0)
    0x1587: v1587(0x158c) = CONST 
    0x158a: JUMPI v1587(0x158c), v1586(0x1)

    Begin block 0x158b
    prev=[0x156d], succ=[]
    =================================
    0x158b: THROW 

    Begin block 0x158c
    prev=[0x156d], succ=[0x7de]
    =================================
    0x158d: v158d(0x10000000000000000000000000000000000000000) = MUL v156e(0x1), v1577(0x10000000000000000000000000000000000000000)
    0x158e: v158e = OR v158d(0x10000000000000000000000000000000000000000), v157f
    0x1590: SSTORE v1570(0x7), v158e
    0x1592: JUMP v7d7(0x7de)

    Begin block 0x7de
    prev=[0x158c], succ=[]
    =================================
    0x7df: STOP 

}

function contractBalance()() public {
    Begin block 0x7e0
    prev=[], succ=[0x7e8, 0x7ec]
    =================================
    0x7e1: v7e1 = CALLVALUE 
    0x7e3: v7e3 = ISZERO v7e1
    0x7e4: v7e4(0x7ec) = CONST 
    0x7e7: JUMPI v7e4(0x7ec), v7e3

    Begin block 0x7e8
    prev=[0x7e0], succ=[]
    =================================
    0x7e8: v7e8(0x0) = CONST 
    0x7eb: REVERT v7e8(0x0), v7e8(0x0)

    Begin block 0x7ec
    prev=[0x7e0], succ=[0x1593]
    =================================
    0x7ee: v7ee(0x7f5) = CONST 
    0x7f1: v7f1(0x1593) = CONST 
    0x7f4: JUMP v7f1(0x1593)

    Begin block 0x1593
    prev=[0x7ec], succ=[0x7f5]
    =================================
    0x1594: v1594(0x0) = CONST 
    0x1596: v1596 = ADDRESS 
    0x1597: v1597(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15ac: v15ac = AND v1597(0xffffffffffffffffffffffffffffffffffffffff), v1596
    0x15ad: v15ad = BALANCE v15ac
    0x15b1: JUMP v7ee(0x7f5)

    Begin block 0x7f5
    prev=[0x1593], succ=[]
    =================================
    0x7f6: v7f6(0x40) = CONST 
    0x7f8: v7f8 = MLOAD v7f6(0x40)
    0x7fc: MSTORE v7f8, v15ad
    0x7fd: v7fd(0x20) = CONST 
    0x7ff: v7ff = ADD v7fd(0x20), v7f8
    0x803: v803(0x40) = CONST 
    0x805: v805 = MLOAD v803(0x40)
    0x808: v808(0x20) = SUB v7ff, v805
    0x80a: RETURN v805, v808(0x20)

}

function owner()() public {
    Begin block 0x80b
    prev=[], succ=[0x813, 0x817]
    =================================
    0x80c: v80c = CALLVALUE 
    0x80e: v80e = ISZERO v80c
    0x80f: v80f(0x817) = CONST 
    0x812: JUMPI v80f(0x817), v80e

    Begin block 0x813
    prev=[0x80b], succ=[]
    =================================
    0x813: v813(0x0) = CONST 
    0x816: REVERT v813(0x0), v813(0x0)

    Begin block 0x817
    prev=[0x80b], succ=[0x15b2]
    =================================
    0x819: v819(0x820) = CONST 
    0x81c: v81c(0x15b2) = CONST 
    0x81f: JUMP v81c(0x15b2)

    Begin block 0x15b2
    prev=[0x817], succ=[0x820]
    =================================
    0x15b3: v15b3(0x7) = CONST 
    0x15b5: v15b5(0x0) = CONST 
    0x15b8: v15b8 = SLOAD v15b3(0x7)
    0x15ba: v15ba(0x100) = CONST 
    0x15bd: v15bd(0x1) = EXP v15ba(0x100), v15b5(0x0)
    0x15bf: v15bf = DIV v15b8, v15bd(0x1)
    0x15c0: v15c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15d5: v15d5 = AND v15c0(0xffffffffffffffffffffffffffffffffffffffff), v15bf
    0x15d7: JUMP v819(0x820)

    Begin block 0x820
    prev=[0x15b2], succ=[]
    =================================
    0x821: v821(0x40) = CONST 
    0x823: v823 = MLOAD v821(0x40)
    0x826: v826(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x83b: v83b = AND v826(0xffffffffffffffffffffffffffffffffffffffff), v15d5
    0x83c: v83c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x851: v851 = AND v83c(0xffffffffffffffffffffffffffffffffffffffff), v83b
    0x853: MSTORE v823, v851
    0x854: v854(0x20) = CONST 
    0x856: v856 = ADD v854(0x20), v823
    0x85a: v85a(0x40) = CONST 
    0x85c: v85c = MLOAD v85a(0x40)
    0x85f: v85f(0x20) = SUB v856, v85c
    0x861: RETURN v85c, v85f(0x20)

}

function finalizeIco()() public {
    Begin block 0x862
    prev=[], succ=[0x86a, 0x86e]
    =================================
    0x863: v863 = CALLVALUE 
    0x865: v865 = ISZERO v863
    0x866: v866(0x86e) = CONST 
    0x869: JUMPI v866(0x86e), v865

    Begin block 0x86a
    prev=[0x862], succ=[]
    =================================
    0x86a: v86a(0x0) = CONST 
    0x86d: REVERT v86a(0x0), v86a(0x0)

    Begin block 0x86e
    prev=[0x862], succ=[0x15d8B0x86e]
    =================================
    0x870: v870(0x877) = CONST 
    0x873: v873(0x15d8) = CONST 
    0x876: JUMP v873(0x15d8)

    Begin block 0x15d8B0x86e
    prev=[0x86e], succ=[0x1630B0x86e, 0x1634B0x86e]
    =================================
    0x15d9S0x86e: v15d9V86e(0x7) = CONST 
    0x15dbS0x86e: v15dbV86e(0x0) = CONST 
    0x15deS0x86e: v15deV86e = SLOAD v15d9V86e(0x7)
    0x15e0S0x86e: v15e0V86e(0x100) = CONST 
    0x15e3S0x86e: v15e3V86e(0x1) = EXP v15e0V86e(0x100), v15dbV86e(0x0)
    0x15e5S0x86e: v15e5V86e = DIV v15deV86e, v15e3V86e(0x1)
    0x15e6S0x86e: v15e6V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15fbS0x86e: v15fbV86e = AND v15e6V86e(0xffffffffffffffffffffffffffffffffffffffff), v15e5V86e
    0x15fcS0x86e: v15fcV86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1611S0x86e: v1611V86e = AND v15fcV86e(0xffffffffffffffffffffffffffffffffffffffff), v15fbV86e
    0x1612S0x86e: v1612V86e = CALLER 
    0x1613S0x86e: v1613V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1628S0x86e: v1628V86e = AND v1613V86e(0xffffffffffffffffffffffffffffffffffffffff), v1612V86e
    0x1629S0x86e: v1629V86e = EQ v1628V86e, v1611V86e
    0x162aS0x86e: v162aV86e = ISZERO v1629V86e
    0x162bS0x86e: v162bV86e = ISZERO v162aV86e
    0x162cS0x86e: v162cV86e(0x1634) = CONST 
    0x162fS0x86e: JUMPI v162cV86e(0x1634), v162bV86e

    Begin block 0x1630B0x86e
    prev=[0x15d8B0x86e], succ=[]
    =================================
    0x1630S0x86e: v1630V86e(0x0) = CONST 
    0x1633S0x86e: REVERT v1630V86e(0x0), v1630V86e(0x0)

    Begin block 0x1634B0x86e
    prev=[0x15d8B0x86e], succ=[0x1640B0x86e, 0x163fB0x86e]
    =================================
    0x1635S0x86e: v1635V86e(0x2) = CONST 
    0x1639S0x86e: v1639V86e(0x0) = GT v1635V86e(0x2), v1635V86e(0x2)
    0x163aS0x86e: v163aV86e(0x1) = ISZERO v1639V86e(0x0)
    0x163bS0x86e: v163bV86e(0x1640) = CONST 
    0x163eS0x86e: JUMPI v163bV86e(0x1640), v163aV86e(0x1)

    Begin block 0x1640B0x86e
    prev=[0x1634B0x86e], succ=[0x165bB0x86e, 0x165aB0x86e]
    =================================
    0x1641S0x86e: v1641V86e(0x7) = CONST 
    0x1643S0x86e: v1643V86e(0x14) = CONST 
    0x1646S0x86e: v1646V86e = SLOAD v1641V86e(0x7)
    0x1648S0x86e: v1648V86e(0x100) = CONST 
    0x164bS0x86e: v164bV86e(0x10000000000000000000000000000000000000000) = EXP v1648V86e(0x100), v1643V86e(0x14)
    0x164dS0x86e: v164dV86e = DIV v1646V86e, v164bV86e(0x10000000000000000000000000000000000000000)
    0x164eS0x86e: v164eV86e(0xff) = CONST 
    0x1650S0x86e: v1650V86e = AND v164eV86e(0xff), v164dV86e
    0x1651S0x86e: v1651V86e(0x2) = CONST 
    0x1654S0x86e: v1654V86e = GT v1650V86e, v1651V86e(0x2)
    0x1655S0x86e: v1655V86e = ISZERO v1654V86e
    0x1656S0x86e: v1656V86e(0x165b) = CONST 
    0x1659S0x86e: JUMPI v1656V86e(0x165b), v1655V86e

    Begin block 0x165bB0x86e
    prev=[0x1640B0x86e], succ=[0x1664B0x86e, 0x1668B0x86e]
    =================================
    0x165cS0x86e: v165cV86e = EQ v1650V86e, v1635V86e(0x2)
    0x165dS0x86e: v165dV86e = ISZERO v165cV86e
    0x165eS0x86e: v165eV86e = ISZERO v165dV86e
    0x165fS0x86e: v165fV86e = ISZERO v165eV86e
    0x1660S0x86e: v1660V86e(0x1668) = CONST 
    0x1663S0x86e: JUMPI v1660V86e(0x1668), v165fV86e

    Begin block 0x1664B0x86e
    prev=[0x165bB0x86e], succ=[]
    =================================
    0x1664S0x86e: v1664V86e(0x0) = CONST 
    0x1667S0x86e: REVERT v1664V86e(0x0), v1664V86e(0x0)

    Begin block 0x1668B0x86e
    prev=[0x165bB0x86e], succ=[0x1e07B0x1668B0x86e]
    =================================
    0x1669S0x86e: v1669V86e(0x1670) = CONST 
    0x166cS0x86e: v166cV86e(0x1e07) = CONST 
    0x166fS0x86e: JUMP v166cV86e(0x1e07)

    Begin block 0x1e07B0x1668B0x86e
    prev=[0x1668B0x86e], succ=[0x1e26B0x1668B0x86e, 0x1e25B0x1668B0x86e]
    =================================
    0x1e08S0x1668S0x86e: v1e08V1668V86e(0x2) = CONST 
    0x1e0aS0x1668S0x86e: v1e0aV1668V86e(0x7) = CONST 
    0x1e0cS0x1668S0x86e: v1e0cV1668V86e(0x14) = CONST 
    0x1e0eS0x1668S0x86e: v1e0eV1668V86e(0x100) = CONST 
    0x1e11S0x1668S0x86e: v1e11V1668V86e(0x10000000000000000000000000000000000000000) = EXP v1e0eV1668V86e(0x100), v1e0cV1668V86e(0x14)
    0x1e13S0x1668S0x86e: v1e13V1668V86e = SLOAD v1e0aV1668V86e(0x7)
    0x1e15S0x1668S0x86e: v1e15V1668V86e(0xff) = CONST 
    0x1e17S0x1668S0x86e: v1e17V1668V86e(0xff0000000000000000000000000000000000000000) = MUL v1e15V1668V86e(0xff), v1e11V1668V86e(0x10000000000000000000000000000000000000000)
    0x1e18S0x1668S0x86e: v1e18V1668V86e(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v1e17V1668V86e(0xff0000000000000000000000000000000000000000)
    0x1e19S0x1668S0x86e: v1e19V1668V86e = AND v1e18V1668V86e(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1e13V1668V86e
    0x1e1cS0x1668S0x86e: v1e1cV1668V86e(0x2) = CONST 
    0x1e1fS0x1668S0x86e: v1e1fV1668V86e(0x0) = GT v1e08V1668V86e(0x2), v1e1cV1668V86e(0x2)
    0x1e20S0x1668S0x86e: v1e20V1668V86e(0x1) = ISZERO v1e1fV1668V86e(0x0)
    0x1e21S0x1668S0x86e: v1e21V1668V86e(0x1e26) = CONST 
    0x1e24S0x1668S0x86e: JUMPI v1e21V1668V86e(0x1e26), v1e20V1668V86e(0x1)

    Begin block 0x1e26B0x1668B0x86e
    prev=[0x1e07B0x1668B0x86e], succ=[0x1e37B0x1668B0x86e, 0x1f10B0x1668B0x86e]
    =================================
    0x1e27S0x1668S0x86e: v1e27V1668V86e(0x20000000000000000000000000000000000000000) = MUL v1e08V1668V86e(0x2), v1e11V1668V86e(0x10000000000000000000000000000000000000000)
    0x1e28S0x1668S0x86e: v1e28V1668V86e = OR v1e27V1668V86e(0x20000000000000000000000000000000000000000), v1e19V1668V86e
    0x1e2aS0x1668S0x86e: SSTORE v1e0aV1668V86e(0x7), v1e28V1668V86e
    0x1e2cS0x1668S0x86e: v1e2cV1668V86e(0x0) = CONST 
    0x1e2eS0x1668S0x86e: v1e2eV1668V86e(0x6) = CONST 
    0x1e30S0x1668S0x86e: v1e30V1668V86e = SLOAD v1e2eV1668V86e(0x6)
    0x1e31S0x1668S0x86e: v1e31V1668V86e = GT v1e30V1668V86e, v1e2cV1668V86e(0x0)
    0x1e32S0x1668S0x86e: v1e32V1668V86e = ISZERO v1e31V1668V86e
    0x1e33S0x1668S0x86e: v1e33V1668V86e(0x1f10) = CONST 
    0x1e36S0x1668S0x86e: JUMPI v1e33V1668V86e(0x1f10), v1e32V1668V86e

    Begin block 0x1e37B0x1668B0x86e
    prev=[0x1e26B0x1668B0x86e], succ=[0x1eabB0x1668B0x86e]
    =================================
    0x1e37S0x1668S0x86e: v1e37V1668V86e(0x1eab) = CONST 
    0x1e3aS0x1668S0x86e: v1e3aV1668V86e(0x6) = CONST 
    0x1e3cS0x1668S0x86e: v1e3cV1668V86e = SLOAD v1e3aV1668V86e(0x6)
    0x1e3dS0x1668S0x86e: v1e3dV1668V86e(0x0) = CONST 
    0x1e40S0x1668S0x86e: v1e40V1668V86e(0x7) = CONST 
    0x1e42S0x1668S0x86e: v1e42V1668V86e(0x0) = CONST 
    0x1e45S0x1668S0x86e: v1e45V1668V86e = SLOAD v1e40V1668V86e(0x7)
    0x1e47S0x1668S0x86e: v1e47V1668V86e(0x100) = CONST 
    0x1e4aS0x1668S0x86e: v1e4aV1668V86e(0x1) = EXP v1e47V1668V86e(0x100), v1e42V1668V86e(0x0)
    0x1e4cS0x1668S0x86e: v1e4cV1668V86e = DIV v1e45V1668V86e, v1e4aV1668V86e(0x1)
    0x1e4dS0x1668S0x86e: v1e4dV1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e62S0x1668S0x86e: v1e62V1668V86e = AND v1e4dV1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1e4cV1668V86e
    0x1e63S0x1668S0x86e: v1e63V1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e78S0x1668S0x86e: v1e78V1668V86e = AND v1e63V1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1e62V1668V86e
    0x1e79S0x1668S0x86e: v1e79V1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e8eS0x1668S0x86e: v1e8eV1668V86e = AND v1e79V1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1e78V1668V86e
    0x1e90S0x1668S0x86e: MSTORE v1e3dV1668V86e(0x0), v1e8eV1668V86e
    0x1e91S0x1668S0x86e: v1e91V1668V86e(0x20) = CONST 
    0x1e93S0x1668S0x86e: v1e93V1668V86e(0x20) = ADD v1e91V1668V86e(0x20), v1e3dV1668V86e(0x0)
    0x1e96S0x1668S0x86e: MSTORE v1e93V1668V86e(0x20), v1e3dV1668V86e(0x0)
    0x1e97S0x1668S0x86e: v1e97V1668V86e(0x20) = CONST 
    0x1e99S0x1668S0x86e: v1e99V1668V86e(0x40) = ADD v1e97V1668V86e(0x20), v1e93V1668V86e(0x20)
    0x1e9aS0x1668S0x86e: v1e9aV1668V86e(0x0) = CONST 
    0x1e9cS0x1668S0x86e: v1e9cV1668V86e = SHA3 v1e9aV1668V86e(0x0), v1e99V1668V86e(0x40)
    0x1e9dS0x1668S0x86e: v1e9dV1668V86e = SLOAD v1e9cV1668V86e
    0x1e9eS0x1668S0x86e: v1e9eV1668V86e(0xba9) = CONST 
    0x1ea4S0x1668S0x86e: v1ea4V1668V86e(0xffffffff) = CONST 
    0x1ea9S0x1668S0x86e: v1ea9V1668V86e(0xba9) = AND v1ea4V1668V86e(0xffffffff), v1e9eV1668V86e(0xba9)
    0x1eaaS0x1668S0x86e: v1eaa_0V1668V86e = CALLPRIVATE v1ea9V1668V86e(0xba9), v1e3cV1668V86e, v1e9dV1668V86e, v1e37V1668V86e(0x1eab)

    Begin block 0x1eabB0x1668B0x86e
    prev=[0x1e37B0x1668B0x86e], succ=[0x1f10B0x1668B0x86e]
    =================================
    0x1eacS0x1668S0x86e: v1eacV1668V86e(0x0) = CONST 
    0x1eafS0x1668S0x86e: v1eafV1668V86e(0x7) = CONST 
    0x1eb1S0x1668S0x86e: v1eb1V1668V86e(0x0) = CONST 
    0x1eb4S0x1668S0x86e: v1eb4V1668V86e = SLOAD v1eafV1668V86e(0x7)
    0x1eb6S0x1668S0x86e: v1eb6V1668V86e(0x100) = CONST 
    0x1eb9S0x1668S0x86e: v1eb9V1668V86e(0x1) = EXP v1eb6V1668V86e(0x100), v1eb1V1668V86e(0x0)
    0x1ebbS0x1668S0x86e: v1ebbV1668V86e = DIV v1eb4V1668V86e, v1eb9V1668V86e(0x1)
    0x1ebcS0x1668S0x86e: v1ebcV1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ed1S0x1668S0x86e: v1ed1V1668V86e = AND v1ebcV1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1ebbV1668V86e
    0x1ed2S0x1668S0x86e: v1ed2V1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ee7S0x1668S0x86e: v1ee7V1668V86e = AND v1ed2V1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1ed1V1668V86e
    0x1ee8S0x1668S0x86e: v1ee8V1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1efdS0x1668S0x86e: v1efdV1668V86e = AND v1ee8V1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1ee7V1668V86e
    0x1effS0x1668S0x86e: MSTORE v1eacV1668V86e(0x0), v1efdV1668V86e
    0x1f00S0x1668S0x86e: v1f00V1668V86e(0x20) = CONST 
    0x1f02S0x1668S0x86e: v1f02V1668V86e(0x20) = ADD v1f00V1668V86e(0x20), v1eacV1668V86e(0x0)
    0x1f05S0x1668S0x86e: MSTORE v1f02V1668V86e(0x20), v1eacV1668V86e(0x0)
    0x1f06S0x1668S0x86e: v1f06V1668V86e(0x20) = CONST 
    0x1f08S0x1668S0x86e: v1f08V1668V86e(0x40) = ADD v1f06V1668V86e(0x20), v1f02V1668V86e(0x20)
    0x1f09S0x1668S0x86e: v1f09V1668V86e(0x0) = CONST 
    0x1f0bS0x1668S0x86e: v1f0bV1668V86e = SHA3 v1f09V1668V86e(0x0), v1f08V1668V86e(0x40)
    0x1f0eS0x1668S0x86e: SSTORE v1f0bV1668V86e, v1eaa_0V1668V86e
    0x9992S0x1668S0x86e: v9992V1668V86e(0x1f10) = CONST 
    0x99b2S0x1668S0x86e: JUMP v9992V1668V86e(0x1f10)

    Begin block 0x1f10B0x1668B0x86e
    prev=[0x1e26B0x1668B0x86e, 0x1eabB0x1668B0x86e], succ=[0x1f86B0x1668B0x86e, 0x1f8fB0x1668B0x86e]
    =================================
    0x1f11S0x1668S0x86e: v1f11V1668V86e(0x7) = CONST 
    0x1f13S0x1668S0x86e: v1f13V1668V86e(0x0) = CONST 
    0x1f16S0x1668S0x86e: v1f16V1668V86e = SLOAD v1f11V1668V86e(0x7)
    0x1f18S0x1668S0x86e: v1f18V1668V86e(0x100) = CONST 
    0x1f1bS0x1668S0x86e: v1f1bV1668V86e(0x1) = EXP v1f18V1668V86e(0x100), v1f13V1668V86e(0x0)
    0x1f1dS0x1668S0x86e: v1f1dV1668V86e = DIV v1f16V1668V86e, v1f1bV1668V86e(0x1)
    0x1f1eS0x1668S0x86e: v1f1eV1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f33S0x1668S0x86e: v1f33V1668V86e = AND v1f1eV1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1f1dV1668V86e
    0x1f34S0x1668S0x86e: v1f34V1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f49S0x1668S0x86e: v1f49V1668V86e = AND v1f34V1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1f33V1668V86e
    0x1f4aS0x1668S0x86e: v1f4aV1668V86e(0x8fc) = CONST 
    0x1f4dS0x1668S0x86e: v1f4dV1668V86e = ADDRESS 
    0x1f4eS0x1668S0x86e: v1f4eV1668V86e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f63S0x1668S0x86e: v1f63V1668V86e = AND v1f4eV1668V86e(0xffffffffffffffffffffffffffffffffffffffff), v1f4dV1668V86e
    0x1f64S0x1668S0x86e: v1f64V1668V86e = BALANCE v1f63V1668V86e
    0x1f67S0x1668S0x86e: v1f67V1668V86e = ISZERO v1f64V1668V86e
    0x1f68S0x1668S0x86e: v1f68V1668V86e = MUL v1f67V1668V86e, v1f4aV1668V86e(0x8fc)
    0x1f6aS0x1668S0x86e: v1f6aV1668V86e(0x40) = CONST 
    0x1f6cS0x1668S0x86e: v1f6cV1668V86e = MLOAD v1f6aV1668V86e(0x40)
    0x1f6dS0x1668S0x86e: v1f6dV1668V86e(0x0) = CONST 
    0x1f6fS0x1668S0x86e: v1f6fV1668V86e(0x40) = CONST 
    0x1f71S0x1668S0x86e: v1f71V1668V86e = MLOAD v1f6fV1668V86e(0x40)
    0x1f74S0x1668S0x86e: v1f74V1668V86e(0x0) = SUB v1f6cV1668V86e, v1f71V1668V86e
    0x1f79S0x1668S0x86e: v1f79V1668V86e = CALL v1f68V1668V86e, v1f49V1668V86e, v1f64V1668V86e, v1f71V1668V86e, v1f74V1668V86e(0x0), v1f71V1668V86e, v1f6dV1668V86e(0x0)
    0x1f7fS0x1668S0x86e: v1f7fV1668V86e = ISZERO v1f79V1668V86e
    0x1f81S0x1668S0x86e: v1f81V1668V86e = ISZERO v1f7fV1668V86e
    0x1f82S0x1668S0x86e: v1f82V1668V86e(0x1f8f) = CONST 
    0x1f85S0x1668S0x86e: JUMPI v1f82V1668V86e(0x1f8f), v1f81V1668V86e

    Begin block 0x1f86B0x1668B0x86e
    prev=[0x1f10B0x1668B0x86e], succ=[]
    =================================
    0x1f86S0x1668S0x86e: v1f86V1668V86e = RETURNDATASIZE 
    0x1f87S0x1668S0x86e: v1f87V1668V86e(0x0) = CONST 
    0x1f8aS0x1668S0x86e: RETURNDATACOPY v1f87V1668V86e(0x0), v1f87V1668V86e(0x0), v1f86V1668V86e
    0x1f8bS0x1668S0x86e: v1f8bV1668V86e = RETURNDATASIZE 
    0x1f8cS0x1668S0x86e: v1f8cV1668V86e(0x0) = CONST 
    0x1f8eS0x1668S0x86e: REVERT v1f8cV1668V86e(0x0), v1f8bV1668V86e

    Begin block 0x1f8fB0x1668B0x86e
    prev=[0x1f10B0x1668B0x86e], succ=[0x1670B0x86e]
    =================================
    0x1f91S0x1668S0x86e: JUMP v1669V86e(0x1670)

    Begin block 0x1670B0x86e
    prev=[0x1f8fB0x1668B0x86e], succ=[0x877]
    =================================
    0x1671S0x86e: JUMP v870(0x877)

    Begin block 0x877
    prev=[0x1670B0x86e], succ=[]
    =================================
    0x878: STOP 

    Begin block 0x1e25B0x1668B0x86e
    prev=[0x1e07B0x1668B0x86e], succ=[]
    =================================
    0x1e25S0x1668S0x86e: THROW 

    Begin block 0x165aB0x86e
    prev=[0x1640B0x86e], succ=[]
    =================================
    0x165aS0x86e: THROW 

    Begin block 0x163fB0x86e
    prev=[0x1634B0x86e], succ=[]
    =================================
    0x163fS0x86e: THROW 

}

function symbol()() public {
    Begin block 0x879
    prev=[], succ=[0x881, 0x885]
    =================================
    0x87a: v87a = CALLVALUE 
    0x87c: v87c = ISZERO v87a
    0x87d: v87d(0x885) = CONST 
    0x880: JUMPI v87d(0x885), v87c

    Begin block 0x881
    prev=[0x879], succ=[]
    =================================
    0x881: v881(0x0) = CONST 
    0x884: REVERT v881(0x0), v881(0x0)

    Begin block 0x885
    prev=[0x879], succ=[0x1672]
    =================================
    0x887: v887(0x88e) = CONST 
    0x88a: v88a(0x1672) = CONST 
    0x88d: JUMP v88a(0x1672)

    Begin block 0x1672
    prev=[0x885], succ=[0x88e]
    =================================
    0x1673: v1673(0x40) = CONST 
    0x1676: v1676 = MLOAD v1673(0x40)
    0x1679: v1679 = ADD v1676, v1673(0x40)
    0x167a: v167a(0x40) = CONST 
    0x167c: MSTORE v167a(0x40), v1679
    0x167e: v167e(0x3) = CONST 
    0x1681: MSTORE v1676, v167e(0x3)
    0x1682: v1682(0x20) = CONST 
    0x1684: v1684 = ADD v1682(0x20), v1676
    0x1685: v1685(0x4e54580000000000000000000000000000000000000000000000000000000000) = CONST 
    0x16a7: MSTORE v1684, v1685(0x4e54580000000000000000000000000000000000000000000000000000000000)
    0x16aa: JUMP v887(0x88e)

    Begin block 0x88e
    prev=[0x1672], succ=[0x8b3]
    =================================
    0x88f: v88f(0x40) = CONST 
    0x891: v891 = MLOAD v88f(0x40)
    0x894: v894(0x20) = CONST 
    0x896: v896 = ADD v894(0x20), v891
    0x899: v899(0x20) = SUB v896, v891
    0x89b: MSTORE v891, v899(0x20)
    0x89f: v89f(0x3) = MLOAD v1676
    0x8a1: MSTORE v896, v89f(0x3)
    0x8a2: v8a2(0x20) = CONST 
    0x8a4: v8a4 = ADD v8a2(0x20), v896
    0x8a8: v8a8(0x3) = MLOAD v1676
    0x8aa: v8aa(0x20) = CONST 
    0x8ac: v8ac = ADD v8aa(0x20), v1676
    0x8b1: v8b1(0x0) = CONST 
    0x6792: v6792(0x8b3) = CONST 
    0x67b2: JUMP v6792(0x8b3)

    Begin block 0x8b3
    prev=[0x88e, 0x8bc], succ=[0x8ce, 0x8bc]
    =================================
    0x8b3_0x0: v8b3_0 = PHI v8b1(0x0), v8c7
    0x8b6: v8b6 = LT v8b3_0, v8a8(0x3)
    0x8b7: v8b7 = ISZERO v8b6
    0x8b8: v8b8(0x8ce) = CONST 
    0x8bb: JUMPI v8b8(0x8ce), v8b7

    Begin block 0x8ce
    prev=[0x8b3], succ=[0x8fb, 0x8e2]
    =================================
    0x8d7: v8d7 = ADD v8a8(0x3), v8a4
    0x8d9: v8d9(0x1f) = CONST 
    0x8db: v8db(0x3) = AND v8d9(0x1f), v8a8(0x3)
    0x8dd: v8dd(0x0) = ISZERO v8db(0x3)
    0x8de: v8de(0x8fb) = CONST 
    0x8e1: JUMPI v8de(0x8fb), v8dd(0x0)

    Begin block 0x8fb
    prev=[0x8ce, 0x8e2], succ=[]
    =================================
    0x8fb_0x1: v8fb_1 = PHI v8d7, v8f8
    0x901: v901(0x40) = CONST 
    0x903: v903 = MLOAD v901(0x40)
    0x906: v906 = SUB v8fb_1, v903
    0x908: RETURN v903, v906

    Begin block 0x8e2
    prev=[0x8ce], succ=[0x8fb]
    =================================
    0x8e4: v8e4 = SUB v8d7, v8db(0x3)
    0x8e6: v8e6 = MLOAD v8e4
    0x8e7: v8e7(0x1) = CONST 
    0x8ea: v8ea(0x20) = CONST 
    0x8ec: v8ec(0x1d) = SUB v8ea(0x20), v8db(0x3)
    0x8ed: v8ed(0x100) = CONST 
    0x8f0: v8f0(0x10000000000000000000000000000000000000000000000000000000000) = EXP v8ed(0x100), v8ec(0x1d)
    0x8f1: v8f1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v8f0(0x10000000000000000000000000000000000000000000000000000000000), v8e7(0x1)
    0x8f2: v8f2(0xffffff0000000000000000000000000000000000000000000000000000000000) = NOT v8f1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x8f3: v8f3 = AND v8f2(0xffffff0000000000000000000000000000000000000000000000000000000000), v8e6
    0x8f5: MSTORE v8e4, v8f3
    0x8f6: v8f6(0x20) = CONST 
    0x8f8: v8f8 = ADD v8f6(0x20), v8e4
    0x7192: v7192(0x8fb) = CONST 
    0x71b2: JUMP v7192(0x8fb)

    Begin block 0x8bc
    prev=[0x8b3], succ=[0x8b3]
    =================================
    0x8bc_0x0: v8bc_0 = PHI v8b1(0x0), v8c7
    0x8be: v8be = ADD v8ac, v8bc_0
    0x8bf: v8bf = MLOAD v8be
    0x8c2: v8c2 = ADD v8a4, v8bc_0
    0x8c3: MSTORE v8c2, v8bf
    0x8c4: v8c4(0x20) = CONST 
    0x8c7: v8c7 = ADD v8bc_0, v8c4(0x20)
    0x8ca: v8ca(0x8b3) = CONST 
    0x8cd: JUMP v8ca(0x8b3)

}

function transfer(address,uint256)() public {
    Begin block 0x909
    prev=[], succ=[0x911, 0x915]
    =================================
    0x90a: v90a = CALLVALUE 
    0x90c: v90c = ISZERO v90a
    0x90d: v90d(0x915) = CONST 
    0x910: JUMPI v90d(0x915), v90c

    Begin block 0x911
    prev=[0x909], succ=[]
    =================================
    0x911: v911(0x0) = CONST 
    0x914: REVERT v911(0x0), v911(0x0)

    Begin block 0x915
    prev=[0x909], succ=[0x16ab]
    =================================
    0x917: v917(0x954) = CONST 
    0x91a: v91a(0x4) = CONST 
    0x91d: v91d = CALLDATASIZE 
    0x91e: v91e = SUB v91d, v91a(0x4)
    0x920: v920 = ADD v91a(0x4), v91e
    0x924: v924 = CALLDATALOAD v91a(0x4)
    0x925: v925(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x93a: v93a = AND v925(0xffffffffffffffffffffffffffffffffffffffff), v924
    0x93c: v93c(0x20) = CONST 
    0x93e: v93e(0x24) = ADD v93c(0x20), v91a(0x4)
    0x944: v944 = CALLDATALOAD v93e(0x24)
    0x946: v946(0x20) = CONST 
    0x948: v948(0x44) = ADD v946(0x20), v93e(0x24)
    0x950: v950(0x16ab) = CONST 
    0x953: JUMP v950(0x16ab)

    Begin block 0x16ab
    prev=[0x915], succ=[0x16e4, 0x16e8]
    =================================
    0x16ac: v16ac(0x0) = CONST 
    0x16af: v16af(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16c4: v16c4(0x0) = AND v16af(0xffffffffffffffffffffffffffffffffffffffff), v16ac(0x0)
    0x16c6: v16c6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16db: v16db = AND v16c6(0xffffffffffffffffffffffffffffffffffffffff), v93a
    0x16dc: v16dc = EQ v16db, v16c4(0x0)
    0x16dd: v16dd = ISZERO v16dc
    0x16de: v16de = ISZERO v16dd
    0x16df: v16df = ISZERO v16de
    0x16e0: v16e0(0x16e8) = CONST 
    0x16e3: JUMPI v16e0(0x16e8), v16df

    Begin block 0x16e4
    prev=[0x16ab], succ=[]
    =================================
    0x16e4: v16e4(0x0) = CONST 
    0x16e7: REVERT v16e4(0x0), v16e4(0x0)

    Begin block 0x16e8
    prev=[0x16ab], succ=[0x1731, 0x1735]
    =================================
    0x16e9: v16e9(0x0) = CONST 
    0x16ec: v16ec = CALLER 
    0x16ed: v16ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1702: v1702 = AND v16ed(0xffffffffffffffffffffffffffffffffffffffff), v16ec
    0x1703: v1703(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1718: v1718 = AND v1703(0xffffffffffffffffffffffffffffffffffffffff), v1702
    0x171a: MSTORE v16e9(0x0), v1718
    0x171b: v171b(0x20) = CONST 
    0x171d: v171d(0x20) = ADD v171b(0x20), v16e9(0x0)
    0x1720: MSTORE v171d(0x20), v16e9(0x0)
    0x1721: v1721(0x20) = CONST 
    0x1723: v1723(0x40) = ADD v1721(0x20), v171d(0x20)
    0x1724: v1724(0x0) = CONST 
    0x1726: v1726 = SHA3 v1724(0x0), v1723(0x40)
    0x1727: v1727 = SLOAD v1726
    0x1729: v1729 = GT v944, v1727
    0x172a: v172a = ISZERO v1729
    0x172b: v172b = ISZERO v172a
    0x172c: v172c = ISZERO v172b
    0x172d: v172d(0x1735) = CONST 
    0x1730: JUMPI v172d(0x1735), v172c

    Begin block 0x1731
    prev=[0x16e8], succ=[]
    =================================
    0x1731: v1731(0x0) = CONST 
    0x1734: REVERT v1731(0x0), v1731(0x0)

    Begin block 0x1735
    prev=[0x16e8], succ=[0x1786]
    =================================
    0x1736: v1736(0x1786) = CONST 
    0x173a: v173a(0x0) = CONST 
    0x173d: v173d = CALLER 
    0x173e: v173e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1753: v1753 = AND v173e(0xffffffffffffffffffffffffffffffffffffffff), v173d
    0x1754: v1754(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1769: v1769 = AND v1754(0xffffffffffffffffffffffffffffffffffffffff), v1753
    0x176b: MSTORE v173a(0x0), v1769
    0x176c: v176c(0x20) = CONST 
    0x176e: v176e(0x20) = ADD v176c(0x20), v173a(0x0)
    0x1771: MSTORE v176e(0x20), v173a(0x0)
    0x1772: v1772(0x20) = CONST 
    0x1774: v1774(0x40) = ADD v1772(0x20), v176e(0x20)
    0x1775: v1775(0x0) = CONST 
    0x1777: v1777 = SHA3 v1775(0x0), v1774(0x40)
    0x1778: v1778 = SLOAD v1777
    0x1779: v1779(0xbc5) = CONST 
    0x177f: v177f(0xffffffff) = CONST 
    0x1784: v1784(0xbc5) = AND v177f(0xffffffff), v1779(0xbc5)
    0x1785: v1785_0 = CALLPRIVATE v1784(0xbc5), v944, v1778, v1736(0x1786)

    Begin block 0x1786
    prev=[0x1735], succ=[0x1819]
    =================================
    0x1787: v1787(0x0) = CONST 
    0x178a: v178a = CALLER 
    0x178b: v178b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17a0: v17a0 = AND v178b(0xffffffffffffffffffffffffffffffffffffffff), v178a
    0x17a1: v17a1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17b6: v17b6 = AND v17a1(0xffffffffffffffffffffffffffffffffffffffff), v17a0
    0x17b8: MSTORE v1787(0x0), v17b6
    0x17b9: v17b9(0x20) = CONST 
    0x17bb: v17bb(0x20) = ADD v17b9(0x20), v1787(0x0)
    0x17be: MSTORE v17bb(0x20), v1787(0x0)
    0x17bf: v17bf(0x20) = CONST 
    0x17c1: v17c1(0x40) = ADD v17bf(0x20), v17bb(0x20)
    0x17c2: v17c2(0x0) = CONST 
    0x17c4: v17c4 = SHA3 v17c2(0x0), v17c1(0x40)
    0x17c7: SSTORE v17c4, v1785_0
    0x17c9: v17c9(0x1819) = CONST 
    0x17cd: v17cd(0x0) = CONST 
    0x17d1: v17d1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17e6: v17e6 = AND v17d1(0xffffffffffffffffffffffffffffffffffffffff), v93a
    0x17e7: v17e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17fc: v17fc = AND v17e7(0xffffffffffffffffffffffffffffffffffffffff), v17e6
    0x17fe: MSTORE v17cd(0x0), v17fc
    0x17ff: v17ff(0x20) = CONST 
    0x1801: v1801(0x20) = ADD v17ff(0x20), v17cd(0x0)
    0x1804: MSTORE v1801(0x20), v17cd(0x0)
    0x1805: v1805(0x20) = CONST 
    0x1807: v1807(0x40) = ADD v1805(0x20), v1801(0x20)
    0x1808: v1808(0x0) = CONST 
    0x180a: v180a = SHA3 v1808(0x0), v1807(0x40)
    0x180b: v180b = SLOAD v180a
    0x180c: v180c(0xba9) = CONST 
    0x1812: v1812(0xffffffff) = CONST 
    0x1817: v1817(0xba9) = AND v1812(0xffffffff), v180c(0xba9)
    0x1818: v1818_0 = CALLPRIVATE v1817(0xba9), v944, v180b, v17c9(0x1819)

    Begin block 0x1819
    prev=[0x1786], succ=[0x954]
    =================================
    0x181a: v181a(0x0) = CONST 
    0x181e: v181e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1833: v1833 = AND v181e(0xffffffffffffffffffffffffffffffffffffffff), v93a
    0x1834: v1834(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1849: v1849 = AND v1834(0xffffffffffffffffffffffffffffffffffffffff), v1833
    0x184b: MSTORE v181a(0x0), v1849
    0x184c: v184c(0x20) = CONST 
    0x184e: v184e(0x20) = ADD v184c(0x20), v181a(0x0)
    0x1851: MSTORE v184e(0x20), v181a(0x0)
    0x1852: v1852(0x20) = CONST 
    0x1854: v1854(0x40) = ADD v1852(0x20), v184e(0x20)
    0x1855: v1855(0x0) = CONST 
    0x1857: v1857 = SHA3 v1855(0x0), v1854(0x40)
    0x185a: SSTORE v1857, v1818_0
    0x185d: v185d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1872: v1872 = AND v185d(0xffffffffffffffffffffffffffffffffffffffff), v93a
    0x1873: v1873 = CALLER 
    0x1874: v1874(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1889: v1889 = AND v1874(0xffffffffffffffffffffffffffffffffffffffff), v1873
    0x188a: v188a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x18ac: v18ac(0x40) = CONST 
    0x18ae: v18ae = MLOAD v18ac(0x40)
    0x18b2: MSTORE v18ae, v944
    0x18b3: v18b3(0x20) = CONST 
    0x18b5: v18b5 = ADD v18b3(0x20), v18ae
    0x18b9: v18b9(0x40) = CONST 
    0x18bb: v18bb = MLOAD v18b9(0x40)
    0x18be: v18be(0x20) = SUB v18b5, v18bb
    0x18c0: LOG3 v18bb, v18be(0x20), v188a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1889, v1872
    0x18c1: v18c1(0x1) = CONST 
    0x18c9: JUMP v917(0x954)

    Begin block 0x954
    prev=[0x1819], succ=[]
    =================================
    0x955: v955(0x40) = CONST 
    0x957: v957 = MLOAD v955(0x40)
    0x95a: v95a(0x0) = ISZERO v18c1(0x1)
    0x95b: v95b(0x1) = ISZERO v95a(0x0)
    0x95c: v95c(0x0) = ISZERO v95b(0x1)
    0x95d: v95d(0x1) = ISZERO v95c(0x0)
    0x95f: MSTORE v957, v95d(0x1)
    0x960: v960(0x20) = CONST 
    0x962: v962 = ADD v960(0x20), v957
    0x966: v966(0x40) = CONST 
    0x968: v968 = MLOAD v966(0x40)
    0x96b: v96b(0x20) = SUB v962, v968
    0x96d: RETURN v968, v96b(0x20)

}

function remainingTokens()() public {
    Begin block 0x96e
    prev=[], succ=[0x976, 0x97a]
    =================================
    0x96f: v96f = CALLVALUE 
    0x971: v971 = ISZERO v96f
    0x972: v972(0x97a) = CONST 
    0x975: JUMPI v972(0x97a), v971

    Begin block 0x976
    prev=[0x96e], succ=[]
    =================================
    0x976: v976(0x0) = CONST 
    0x979: REVERT v976(0x0), v976(0x0)

    Begin block 0x97a
    prev=[0x96e], succ=[0x18ca]
    =================================
    0x97c: v97c(0x983) = CONST 
    0x97f: v97f(0x18ca) = CONST 
    0x982: JUMP v97f(0x18ca)

    Begin block 0x18ca
    prev=[0x97a], succ=[0x983]
    =================================
    0x18cb: v18cb(0x6) = CONST 
    0x18cd: v18cd = SLOAD v18cb(0x6)
    0x18cf: JUMP v97c(0x983)

    Begin block 0x983
    prev=[0x18ca], succ=[]
    =================================
    0x984: v984(0x40) = CONST 
    0x986: v986 = MLOAD v984(0x40)
    0x98a: MSTORE v986, v18cd
    0x98b: v98b(0x20) = CONST 
    0x98d: v98d = ADD v98b(0x20), v986
    0x991: v991(0x40) = CONST 
    0x993: v993 = MLOAD v991(0x40)
    0x996: v996(0x20) = SUB v98d, v993
    0x998: RETURN v993, v996(0x20)

}

function basePrice()() public {
    Begin block 0x999
    prev=[], succ=[0x9a1, 0x9a5]
    =================================
    0x99a: v99a = CALLVALUE 
    0x99c: v99c = ISZERO v99a
    0x99d: v99d(0x9a5) = CONST 
    0x9a0: JUMPI v99d(0x9a5), v99c

    Begin block 0x9a1
    prev=[0x999], succ=[]
    =================================
    0x9a1: v9a1(0x0) = CONST 
    0x9a4: REVERT v9a1(0x0), v9a1(0x0)

    Begin block 0x9a5
    prev=[0x999], succ=[0x18d0]
    =================================
    0x9a7: v9a7(0x9ae) = CONST 
    0x9aa: v9aa(0x18d0) = CONST 
    0x9ad: JUMP v9aa(0x18d0)

    Begin block 0x18d0
    prev=[0x9a5], succ=[0x9ae]
    =================================
    0x18d1: v18d1(0x2540be400) = CONST 
    0x18d8: JUMP v9a7(0x9ae)

    Begin block 0x9ae
    prev=[0x18d0], succ=[]
    =================================
    0x9af: v9af(0x40) = CONST 
    0x9b1: v9b1 = MLOAD v9af(0x40)
    0x9b5: MSTORE v9b1, v18d1(0x2540be400)
    0x9b6: v9b6(0x20) = CONST 
    0x9b8: v9b8 = ADD v9b6(0x20), v9b1
    0x9bc: v9bc(0x40) = CONST 
    0x9be: v9be = MLOAD v9bc(0x40)
    0x9c1: v9c1(0x20) = SUB v9b8, v9be
    0x9c3: RETURN v9be, v9c1(0x20)

}

function tokenReserve()() public {
    Begin block 0x9c4
    prev=[], succ=[0x9cc, 0x9d0]
    =================================
    0x9c5: v9c5 = CALLVALUE 
    0x9c7: v9c7 = ISZERO v9c5
    0x9c8: v9c8(0x9d0) = CONST 
    0x9cb: JUMPI v9c8(0x9d0), v9c7

    Begin block 0x9cc
    prev=[0x9c4], succ=[]
    =================================
    0x9cc: v9cc(0x0) = CONST 
    0x9cf: REVERT v9cc(0x0), v9cc(0x0)

    Begin block 0x9d0
    prev=[0x9c4], succ=[0x18d9]
    =================================
    0x9d2: v9d2(0x9d9) = CONST 
    0x9d5: v9d5(0x18d9) = CONST 
    0x9d8: JUMP v9d5(0x18d9)

    Begin block 0x18d9
    prev=[0x9d0], succ=[0x9d9]
    =================================
    0x18da: v18da(0x2386f26fc10000) = CONST 
    0x18e3: JUMP v9d2(0x9d9)

    Begin block 0x9d9
    prev=[0x18d9], succ=[]
    =================================
    0x9da: v9da(0x40) = CONST 
    0x9dc: v9dc = MLOAD v9da(0x40)
    0x9e0: MSTORE v9dc, v18da(0x2386f26fc10000)
    0x9e1: v9e1(0x20) = CONST 
    0x9e3: v9e3 = ADD v9e1(0x20), v9dc
    0x9e7: v9e7(0x40) = CONST 
    0x9e9: v9e9 = MLOAD v9e7(0x40)
    0x9ec: v9ec(0x20) = SUB v9e3, v9e9
    0x9ee: RETURN v9e9, v9ec(0x20)

}

function increaseApproval(address,uint256)() public {
    Begin block 0x9ef
    prev=[], succ=[0x9f7, 0x9fb]
    =================================
    0x9f0: v9f0 = CALLVALUE 
    0x9f2: v9f2 = ISZERO v9f0
    0x9f3: v9f3(0x9fb) = CONST 
    0x9f6: JUMPI v9f3(0x9fb), v9f2

    Begin block 0x9f7
    prev=[0x9ef], succ=[]
    =================================
    0x9f7: v9f7(0x0) = CONST 
    0x9fa: REVERT v9f7(0x0), v9f7(0x0)

    Begin block 0x9fb
    prev=[0x9ef], succ=[0x18e4]
    =================================
    0x9fd: v9fd(0xa3a) = CONST 
    0xa00: va00(0x4) = CONST 
    0xa03: va03 = CALLDATASIZE 
    0xa04: va04 = SUB va03, va00(0x4)
    0xa06: va06 = ADD va00(0x4), va04
    0xa0a: va0a = CALLDATALOAD va00(0x4)
    0xa0b: va0b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa20: va20 = AND va0b(0xffffffffffffffffffffffffffffffffffffffff), va0a
    0xa22: va22(0x20) = CONST 
    0xa24: va24(0x24) = ADD va22(0x20), va00(0x4)
    0xa2a: va2a = CALLDATALOAD va24(0x24)
    0xa2c: va2c(0x20) = CONST 
    0xa2e: va2e(0x44) = ADD va2c(0x20), va24(0x24)
    0xa36: va36(0x18e4) = CONST 
    0xa39: JUMP va36(0x18e4)

    Begin block 0x18e4
    prev=[0x9fb], succ=[0x1975]
    =================================
    0x18e5: v18e5(0x0) = CONST 
    0x18e7: v18e7(0x1975) = CONST 
    0x18eb: v18eb(0x2) = CONST 
    0x18ed: v18ed(0x0) = CONST 
    0x18ef: v18ef = CALLER 
    0x18f0: v18f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1905: v1905 = AND v18f0(0xffffffffffffffffffffffffffffffffffffffff), v18ef
    0x1906: v1906(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x191b: v191b = AND v1906(0xffffffffffffffffffffffffffffffffffffffff), v1905
    0x191d: MSTORE v18ed(0x0), v191b
    0x191e: v191e(0x20) = CONST 
    0x1920: v1920(0x20) = ADD v191e(0x20), v18ed(0x0)
    0x1923: MSTORE v1920(0x20), v18eb(0x2)
    0x1924: v1924(0x20) = CONST 
    0x1926: v1926(0x40) = ADD v1924(0x20), v1920(0x20)
    0x1927: v1927(0x0) = CONST 
    0x1929: v1929 = SHA3 v1927(0x0), v1926(0x40)
    0x192a: v192a(0x0) = CONST 
    0x192d: v192d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1942: v1942 = AND v192d(0xffffffffffffffffffffffffffffffffffffffff), va20
    0x1943: v1943(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1958: v1958 = AND v1943(0xffffffffffffffffffffffffffffffffffffffff), v1942
    0x195a: MSTORE v192a(0x0), v1958
    0x195b: v195b(0x20) = CONST 
    0x195d: v195d(0x20) = ADD v195b(0x20), v192a(0x0)
    0x1960: MSTORE v195d(0x20), v1929
    0x1961: v1961(0x20) = CONST 
    0x1963: v1963(0x40) = ADD v1961(0x20), v195d(0x20)
    0x1964: v1964(0x0) = CONST 
    0x1966: v1966 = SHA3 v1964(0x0), v1963(0x40)
    0x1967: v1967 = SLOAD v1966
    0x1968: v1968(0xba9) = CONST 
    0x196e: v196e(0xffffffff) = CONST 
    0x1973: v1973(0xba9) = AND v196e(0xffffffff), v1968(0xba9)
    0x1974: v1974_0 = CALLPRIVATE v1973(0xba9), va2a, v1967, v18e7(0x1975)

    Begin block 0x1975
    prev=[0x18e4], succ=[0xa3a]
    =================================
    0x1976: v1976(0x2) = CONST 
    0x1978: v1978(0x0) = CONST 
    0x197a: v197a = CALLER 
    0x197b: v197b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1990: v1990 = AND v197b(0xffffffffffffffffffffffffffffffffffffffff), v197a
    0x1991: v1991(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19a6: v19a6 = AND v1991(0xffffffffffffffffffffffffffffffffffffffff), v1990
    0x19a8: MSTORE v1978(0x0), v19a6
    0x19a9: v19a9(0x20) = CONST 
    0x19ab: v19ab(0x20) = ADD v19a9(0x20), v1978(0x0)
    0x19ae: MSTORE v19ab(0x20), v1976(0x2)
    0x19af: v19af(0x20) = CONST 
    0x19b1: v19b1(0x40) = ADD v19af(0x20), v19ab(0x20)
    0x19b2: v19b2(0x0) = CONST 
    0x19b4: v19b4 = SHA3 v19b2(0x0), v19b1(0x40)
    0x19b5: v19b5(0x0) = CONST 
    0x19b8: v19b8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19cd: v19cd = AND v19b8(0xffffffffffffffffffffffffffffffffffffffff), va20
    0x19ce: v19ce(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19e3: v19e3 = AND v19ce(0xffffffffffffffffffffffffffffffffffffffff), v19cd
    0x19e5: MSTORE v19b5(0x0), v19e3
    0x19e6: v19e6(0x20) = CONST 
    0x19e8: v19e8(0x20) = ADD v19e6(0x20), v19b5(0x0)
    0x19eb: MSTORE v19e8(0x20), v19b4
    0x19ec: v19ec(0x20) = CONST 
    0x19ee: v19ee(0x40) = ADD v19ec(0x20), v19e8(0x20)
    0x19ef: v19ef(0x0) = CONST 
    0x19f1: v19f1 = SHA3 v19ef(0x0), v19ee(0x40)
    0x19f4: SSTORE v19f1, v1974_0
    0x19f7: v19f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a0c: v1a0c = AND v19f7(0xffffffffffffffffffffffffffffffffffffffff), va20
    0x1a0d: v1a0d = CALLER 
    0x1a0e: v1a0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a23: v1a23 = AND v1a0e(0xffffffffffffffffffffffffffffffffffffffff), v1a0d
    0x1a24: v1a24(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x1a45: v1a45(0x2) = CONST 
    0x1a47: v1a47(0x0) = CONST 
    0x1a49: v1a49 = CALLER 
    0x1a4a: v1a4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a5f: v1a5f = AND v1a4a(0xffffffffffffffffffffffffffffffffffffffff), v1a49
    0x1a60: v1a60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a75: v1a75 = AND v1a60(0xffffffffffffffffffffffffffffffffffffffff), v1a5f
    0x1a77: MSTORE v1a47(0x0), v1a75
    0x1a78: v1a78(0x20) = CONST 
    0x1a7a: v1a7a(0x20) = ADD v1a78(0x20), v1a47(0x0)
    0x1a7d: MSTORE v1a7a(0x20), v1a45(0x2)
    0x1a7e: v1a7e(0x20) = CONST 
    0x1a80: v1a80(0x40) = ADD v1a7e(0x20), v1a7a(0x20)
    0x1a81: v1a81(0x0) = CONST 
    0x1a83: v1a83 = SHA3 v1a81(0x0), v1a80(0x40)
    0x1a84: v1a84(0x0) = CONST 
    0x1a87: v1a87(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a9c: v1a9c = AND v1a87(0xffffffffffffffffffffffffffffffffffffffff), va20
    0x1a9d: v1a9d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ab2: v1ab2 = AND v1a9d(0xffffffffffffffffffffffffffffffffffffffff), v1a9c
    0x1ab4: MSTORE v1a84(0x0), v1ab2
    0x1ab5: v1ab5(0x20) = CONST 
    0x1ab7: v1ab7(0x20) = ADD v1ab5(0x20), v1a84(0x0)
    0x1aba: MSTORE v1ab7(0x20), v1a83
    0x1abb: v1abb(0x20) = CONST 
    0x1abd: v1abd(0x40) = ADD v1abb(0x20), v1ab7(0x20)
    0x1abe: v1abe(0x0) = CONST 
    0x1ac0: v1ac0 = SHA3 v1abe(0x0), v1abd(0x40)
    0x1ac1: v1ac1 = SLOAD v1ac0
    0x1ac2: v1ac2(0x40) = CONST 
    0x1ac4: v1ac4 = MLOAD v1ac2(0x40)
    0x1ac8: MSTORE v1ac4, v1ac1
    0x1ac9: v1ac9(0x20) = CONST 
    0x1acb: v1acb = ADD v1ac9(0x20), v1ac4
    0x1acf: v1acf(0x40) = CONST 
    0x1ad1: v1ad1 = MLOAD v1acf(0x40)
    0x1ad4: v1ad4(0x20) = SUB v1acb, v1ad1
    0x1ad6: LOG3 v1ad1, v1ad4(0x20), v1a24(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v1a23, v1a0c
    0x1ad7: v1ad7(0x1) = CONST 
    0x1adf: JUMP v9fd(0xa3a)

    Begin block 0xa3a
    prev=[0x1975], succ=[]
    =================================
    0xa3b: va3b(0x40) = CONST 
    0xa3d: va3d = MLOAD va3b(0x40)
    0xa40: va40(0x0) = ISZERO v1ad7(0x1)
    0xa41: va41(0x1) = ISZERO va40(0x0)
    0xa42: va42(0x0) = ISZERO va41(0x1)
    0xa43: va43(0x1) = ISZERO va42(0x0)
    0xa45: MSTORE va3d, va43(0x1)
    0xa46: va46(0x20) = CONST 
    0xa48: va48 = ADD va46(0x20), va3d
    0xa4c: va4c(0x40) = CONST 
    0xa4e: va4e = MLOAD va4c(0x40)
    0xa51: va51(0x20) = SUB va48, va4e
    0xa53: RETURN va4e, va51(0x20)

}

function WithdrawEther(address,uint256)() public {
    Begin block 0xa54
    prev=[], succ=[0xa5c, 0xa60]
    =================================
    0xa55: va55 = CALLVALUE 
    0xa57: va57 = ISZERO va55
    0xa58: va58(0xa60) = CONST 
    0xa5b: JUMPI va58(0xa60), va57

    Begin block 0xa5c
    prev=[0xa54], succ=[]
    =================================
    0xa5c: va5c(0x0) = CONST 
    0xa5f: REVERT va5c(0x0), va5c(0x0)

    Begin block 0xa60
    prev=[0xa54], succ=[0x1ae0B0xa60]
    =================================
    0xa62: va62(0xa9f) = CONST 
    0xa65: va65(0x4) = CONST 
    0xa68: va68 = CALLDATASIZE 
    0xa69: va69 = SUB va68, va65(0x4)
    0xa6b: va6b = ADD va65(0x4), va69
    0xa6f: va6f = CALLDATALOAD va65(0x4)
    0xa70: va70(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa85: va85 = AND va70(0xffffffffffffffffffffffffffffffffffffffff), va6f
    0xa87: va87(0x20) = CONST 
    0xa89: va89(0x24) = ADD va87(0x20), va65(0x4)
    0xa8f: va8f = CALLDATALOAD va89(0x24)
    0xa91: va91(0x20) = CONST 
    0xa93: va93(0x44) = ADD va91(0x20), va89(0x24)
    0xa9b: va9b(0x1ae0) = CONST 
    0xa9e: JUMP va9b(0x1ae0)

    Begin block 0x1ae0B0xa60
    prev=[0xa60], succ=[0x1b6aB0xa60, 0x1b17B0xa60]
    =================================
    0x1ae1S0xa60: v1ae1Va60 = ADDRESS 
    0x1ae2S0xa60: v1ae2Va60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1af7S0xa60: v1af7Va60 = AND v1ae2Va60(0xffffffffffffffffffffffffffffffffffffffff), v1ae1Va60
    0x1af8S0xa60: v1af8Va60 = CALLER 
    0x1af9S0xa60: v1af9Va60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b0eS0xa60: v1b0eVa60 = AND v1af9Va60(0xffffffffffffffffffffffffffffffffffffffff), v1af8Va60
    0x1b0fS0xa60: v1b0fVa60 = EQ v1b0eVa60, v1af7Va60
    0x1b10S0xa60: v1b10Va60 = ISZERO v1b0fVa60
    0x1b12S0xa60: v1b12Va60 = ISZERO v1b10Va60
    0x1b13S0xa60: v1b13Va60(0x1b6a) = CONST 
    0x1b16S0xa60: JUMPI v1b13Va60(0x1b6a), v1b12Va60

    Begin block 0x1b6aB0xa60
    prev=[0x1ae0B0xa60, 0x1b17B0xa60], succ=[0x1b70B0xa60, 0x1bddB0xa60]
    =================================
    0x1b6a_0x0S0xa60: v1b6a_0Va60 = PHI v1b10Va60, v1b69Va60
    0x1b6bS0xa60: v1b6bVa60 = ISZERO v1b6a_0Va60
    0x1b6cS0xa60: v1b6cVa60(0x1bdd) = CONST 
    0x1b6fS0xa60: JUMPI v1b6cVa60(0x1bdd), v1b6bVa60

    Begin block 0x1b70B0xa60
    prev=[0x1b6aB0xa60], succ=[]
    =================================
    0x1b70S0xa60: v1b70Va60(0x40) = CONST 
    0x1b72S0xa60: v1b72Va60 = MLOAD v1b70Va60(0x40)
    0x1b73S0xa60: v1b73Va60(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1b95S0xa60: MSTORE v1b72Va60, v1b73Va60(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b96S0xa60: v1b96Va60(0x4) = CONST 
    0x1b98S0xa60: v1b98Va60 = ADD v1b96Va60(0x4), v1b72Va60
    0x1b9bS0xa60: v1b9bVa60(0x20) = CONST 
    0x1b9dS0xa60: v1b9dVa60 = ADD v1b9bVa60(0x20), v1b98Va60
    0x1ba0S0xa60: v1ba0Va60(0x20) = SUB v1b9dVa60, v1b98Va60
    0x1ba2S0xa60: MSTORE v1b98Va60, v1ba0Va60(0x20)
    0x1ba3S0xa60: v1ba3Va60(0x16) = CONST 
    0x1ba6S0xa60: MSTORE v1b9dVa60, v1ba3Va60(0x16)
    0x1ba7S0xa60: v1ba7Va60(0x20) = CONST 
    0x1ba9S0xa60: v1ba9Va60 = ADD v1ba7Va60(0x20), v1b9dVa60
    0x1babS0xa60: v1babVa60(0x496e76616c69642053656e646572204164647265737300000000000000000000) = CONST 
    0x1bcdS0xa60: MSTORE v1ba9Va60, v1babVa60(0x496e76616c69642053656e646572204164647265737300000000000000000000)
    0x1bcfS0xa60: v1bcfVa60(0x20) = CONST 
    0x1bd1S0xa60: v1bd1Va60 = ADD v1bcfVa60(0x20), v1ba9Va60
    0x1bd5S0xa60: v1bd5Va60(0x40) = CONST 
    0x1bd7S0xa60: v1bd7Va60 = MLOAD v1bd5Va60(0x40)
    0x1bdaS0xa60: v1bdaVa60(0x64) = SUB v1bd1Va60, v1bd7Va60
    0x1bdcS0xa60: REVERT v1bd7Va60, v1bdaVa60(0x64)

    Begin block 0x1bddB0xa60
    prev=[0x1b6aB0xa60], succ=[0x1c1aB0xa60, 0x1c23B0xa60]
    =================================
    0x1bdfS0xa60: v1bdfVa60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bf4S0xa60: v1bf4Va60 = AND v1bdfVa60(0xffffffffffffffffffffffffffffffffffffffff), va85
    0x1bf5S0xa60: v1bf5Va60(0x8fc) = CONST 
    0x1bfbS0xa60: v1bfbVa60 = ISZERO va8f
    0x1bfcS0xa60: v1bfcVa60 = MUL v1bfbVa60, v1bf5Va60(0x8fc)
    0x1bfeS0xa60: v1bfeVa60(0x40) = CONST 
    0x1c00S0xa60: v1c00Va60 = MLOAD v1bfeVa60(0x40)
    0x1c01S0xa60: v1c01Va60(0x0) = CONST 
    0x1c03S0xa60: v1c03Va60(0x40) = CONST 
    0x1c05S0xa60: v1c05Va60 = MLOAD v1c03Va60(0x40)
    0x1c08S0xa60: v1c08Va60(0x0) = SUB v1c00Va60, v1c05Va60
    0x1c0dS0xa60: v1c0dVa60 = CALL v1bfcVa60, v1bf4Va60, va8f, v1c05Va60, v1c08Va60(0x0), v1c05Va60, v1c01Va60(0x0)
    0x1c13S0xa60: v1c13Va60 = ISZERO v1c0dVa60
    0x1c15S0xa60: v1c15Va60 = ISZERO v1c13Va60
    0x1c16S0xa60: v1c16Va60(0x1c23) = CONST 
    0x1c19S0xa60: JUMPI v1c16Va60(0x1c23), v1c15Va60

    Begin block 0x1c1aB0xa60
    prev=[0x1bddB0xa60], succ=[]
    =================================
    0x1c1aS0xa60: v1c1aVa60 = RETURNDATASIZE 
    0x1c1bS0xa60: v1c1bVa60(0x0) = CONST 
    0x1c1eS0xa60: RETURNDATACOPY v1c1bVa60(0x0), v1c1bVa60(0x0), v1c1aVa60
    0x1c1fS0xa60: v1c1fVa60 = RETURNDATASIZE 
    0x1c20S0xa60: v1c20Va60(0x0) = CONST 
    0x1c22S0xa60: REVERT v1c20Va60(0x0), v1c1fVa60

    Begin block 0x1c23B0xa60
    prev=[0x1bddB0xa60], succ=[0xa9f]
    =================================
    0x1c27S0xa60: JUMP va62(0xa9f)

    Begin block 0xa9f
    prev=[0x1c23B0xa60], succ=[]
    =================================
    0xaa0: STOP 

    Begin block 0x1b17B0xa60
    prev=[0x1ae0B0xa60], succ=[0x1b6aB0xa60]
    =================================
    0x1b18S0xa60: v1b18Va60(0x3) = CONST 
    0x1b1aS0xa60: v1b1aVa60(0x0) = CONST 
    0x1b1dS0xa60: v1b1dVa60 = SLOAD v1b18Va60(0x3)
    0x1b1fS0xa60: v1b1fVa60(0x100) = CONST 
    0x1b22S0xa60: v1b22Va60(0x1) = EXP v1b1fVa60(0x100), v1b1aVa60(0x0)
    0x1b24S0xa60: v1b24Va60 = DIV v1b1dVa60, v1b22Va60(0x1)
    0x1b25S0xa60: v1b25Va60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b3aS0xa60: v1b3aVa60 = AND v1b25Va60(0xffffffffffffffffffffffffffffffffffffffff), v1b24Va60
    0x1b3bS0xa60: v1b3bVa60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b50S0xa60: v1b50Va60 = AND v1b3bVa60(0xffffffffffffffffffffffffffffffffffffffff), v1b3aVa60
    0x1b51S0xa60: v1b51Va60 = CALLER 
    0x1b52S0xa60: v1b52Va60(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b67S0xa60: v1b67Va60 = AND v1b52Va60(0xffffffffffffffffffffffffffffffffffffffff), v1b51Va60
    0x1b68S0xa60: v1b68Va60 = EQ v1b67Va60, v1b50Va60
    0x1b69S0xa60: v1b69Va60 = ISZERO v1b68Va60
    0x8f92S0xa60: v8f92Va60(0x1b6a) = CONST 
    0x8fb2S0xa60: JUMP v8f92Va60(0x1b6a)

}

function allowance(address,address)() public {
    Begin block 0xaa1
    prev=[], succ=[0xaa9, 0xaad]
    =================================
    0xaa2: vaa2 = CALLVALUE 
    0xaa4: vaa4 = ISZERO vaa2
    0xaa5: vaa5(0xaad) = CONST 
    0xaa8: JUMPI vaa5(0xaad), vaa4

    Begin block 0xaa9
    prev=[0xaa1], succ=[]
    =================================
    0xaa9: vaa9(0x0) = CONST 
    0xaac: REVERT vaa9(0x0), vaa9(0x0)

    Begin block 0xaad
    prev=[0xaa1], succ=[0x1c28]
    =================================
    0xaaf: vaaf(0xb02) = CONST 
    0xab2: vab2(0x4) = CONST 
    0xab5: vab5 = CALLDATASIZE 
    0xab6: vab6 = SUB vab5, vab2(0x4)
    0xab8: vab8 = ADD vab2(0x4), vab6
    0xabc: vabc = CALLDATALOAD vab2(0x4)
    0xabd: vabd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xad2: vad2 = AND vabd(0xffffffffffffffffffffffffffffffffffffffff), vabc
    0xad4: vad4(0x20) = CONST 
    0xad6: vad6(0x24) = ADD vad4(0x20), vab2(0x4)
    0xadc: vadc = CALLDATALOAD vad6(0x24)
    0xadd: vadd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf2: vaf2 = AND vadd(0xffffffffffffffffffffffffffffffffffffffff), vadc
    0xaf4: vaf4(0x20) = CONST 
    0xaf6: vaf6(0x44) = ADD vaf4(0x20), vad6(0x24)
    0xafe: vafe(0x1c28) = CONST 
    0xb01: JUMP vafe(0x1c28)

    Begin block 0x1c28
    prev=[0xaad], succ=[0xb02]
    =================================
    0x1c29: v1c29(0x0) = CONST 
    0x1c2b: v1c2b(0x2) = CONST 
    0x1c2d: v1c2d(0x0) = CONST 
    0x1c30: v1c30(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c45: v1c45 = AND v1c30(0xffffffffffffffffffffffffffffffffffffffff), vad2
    0x1c46: v1c46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c5b: v1c5b = AND v1c46(0xffffffffffffffffffffffffffffffffffffffff), v1c45
    0x1c5d: MSTORE v1c2d(0x0), v1c5b
    0x1c5e: v1c5e(0x20) = CONST 
    0x1c60: v1c60(0x20) = ADD v1c5e(0x20), v1c2d(0x0)
    0x1c63: MSTORE v1c60(0x20), v1c2b(0x2)
    0x1c64: v1c64(0x20) = CONST 
    0x1c66: v1c66(0x40) = ADD v1c64(0x20), v1c60(0x20)
    0x1c67: v1c67(0x0) = CONST 
    0x1c69: v1c69 = SHA3 v1c67(0x0), v1c66(0x40)
    0x1c6a: v1c6a(0x0) = CONST 
    0x1c6d: v1c6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c82: v1c82 = AND v1c6d(0xffffffffffffffffffffffffffffffffffffffff), vaf2
    0x1c83: v1c83(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c98: v1c98 = AND v1c83(0xffffffffffffffffffffffffffffffffffffffff), v1c82
    0x1c9a: MSTORE v1c6a(0x0), v1c98
    0x1c9b: v1c9b(0x20) = CONST 
    0x1c9d: v1c9d(0x20) = ADD v1c9b(0x20), v1c6a(0x0)
    0x1ca0: MSTORE v1c9d(0x20), v1c69
    0x1ca1: v1ca1(0x20) = CONST 
    0x1ca3: v1ca3(0x40) = ADD v1ca1(0x20), v1c9d(0x20)
    0x1ca4: v1ca4(0x0) = CONST 
    0x1ca6: v1ca6 = SHA3 v1ca4(0x0), v1ca3(0x40)
    0x1ca7: v1ca7 = SLOAD v1ca6
    0x1cae: JUMP vaaf(0xb02)

    Begin block 0xb02
    prev=[0x1c28], succ=[]
    =================================
    0xb03: vb03(0x40) = CONST 
    0xb05: vb05 = MLOAD vb03(0x40)
    0xb09: MSTORE vb05, v1ca7
    0xb0a: vb0a(0x20) = CONST 
    0xb0c: vb0c = ADD vb0a(0x20), vb05
    0xb10: vb10(0x40) = CONST 
    0xb12: vb12 = MLOAD vb10(0x40)
    0xb15: vb15(0x20) = SUB vb0c, vb12
    0xb17: RETURN vb12, vb15(0x20)

}

function transferOwnership(address)() public {
    Begin block 0xb18
    prev=[], succ=[0xb20, 0xb24]
    =================================
    0xb19: vb19 = CALLVALUE 
    0xb1b: vb1b = ISZERO vb19
    0xb1c: vb1c(0xb24) = CONST 
    0xb1f: JUMPI vb1c(0xb24), vb1b

    Begin block 0xb20
    prev=[0xb18], succ=[]
    =================================
    0xb20: vb20(0x0) = CONST 
    0xb23: REVERT vb20(0x0), vb20(0x0)

    Begin block 0xb24
    prev=[0xb18], succ=[0x1caf]
    =================================
    0xb26: vb26(0xb59) = CONST 
    0xb29: vb29(0x4) = CONST 
    0xb2c: vb2c = CALLDATASIZE 
    0xb2d: vb2d = SUB vb2c, vb29(0x4)
    0xb2f: vb2f = ADD vb29(0x4), vb2d
    0xb33: vb33 = CALLDATALOAD vb29(0x4)
    0xb34: vb34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb49: vb49 = AND vb34(0xffffffffffffffffffffffffffffffffffffffff), vb33
    0xb4b: vb4b(0x20) = CONST 
    0xb4d: vb4d(0x24) = ADD vb4b(0x20), vb29(0x4)
    0xb55: vb55(0x1caf) = CONST 
    0xb58: JUMP vb55(0x1caf)

    Begin block 0x1caf
    prev=[0xb24], succ=[0x1d07, 0x1d0b]
    =================================
    0x1cb0: v1cb0(0x7) = CONST 
    0x1cb2: v1cb2(0x0) = CONST 
    0x1cb5: v1cb5 = SLOAD v1cb0(0x7)
    0x1cb7: v1cb7(0x100) = CONST 
    0x1cba: v1cba(0x1) = EXP v1cb7(0x100), v1cb2(0x0)
    0x1cbc: v1cbc = DIV v1cb5, v1cba(0x1)
    0x1cbd: v1cbd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cd2: v1cd2 = AND v1cbd(0xffffffffffffffffffffffffffffffffffffffff), v1cbc
    0x1cd3: v1cd3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ce8: v1ce8 = AND v1cd3(0xffffffffffffffffffffffffffffffffffffffff), v1cd2
    0x1ce9: v1ce9 = CALLER 
    0x1cea: v1cea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cff: v1cff = AND v1cea(0xffffffffffffffffffffffffffffffffffffffff), v1ce9
    0x1d00: v1d00 = EQ v1cff, v1ce8
    0x1d01: v1d01 = ISZERO v1d00
    0x1d02: v1d02 = ISZERO v1d01
    0x1d03: v1d03(0x1d0b) = CONST 
    0x1d06: JUMPI v1d03(0x1d0b), v1d02

    Begin block 0x1d07
    prev=[0x1caf], succ=[]
    =================================
    0x1d07: v1d07(0x0) = CONST 
    0x1d0a: REVERT v1d07(0x0), v1d07(0x0)

    Begin block 0x1d0b
    prev=[0x1caf], succ=[0x1d43, 0x1d47]
    =================================
    0x1d0c: v1d0c(0x0) = CONST 
    0x1d0e: v1d0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d23: v1d23(0x0) = AND v1d0e(0xffffffffffffffffffffffffffffffffffffffff), v1d0c(0x0)
    0x1d25: v1d25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d3a: v1d3a = AND v1d25(0xffffffffffffffffffffffffffffffffffffffff), vb49
    0x1d3b: v1d3b = EQ v1d3a, v1d23(0x0)
    0x1d3c: v1d3c = ISZERO v1d3b
    0x1d3d: v1d3d = ISZERO v1d3c
    0x1d3e: v1d3e = ISZERO v1d3d
    0x1d3f: v1d3f(0x1d47) = CONST 
    0x1d42: JUMPI v1d3f(0x1d47), v1d3e

    Begin block 0x1d43
    prev=[0x1d0b], succ=[]
    =================================
    0x1d43: v1d43(0x0) = CONST 
    0x1d46: REVERT v1d43(0x0), v1d43(0x0)

    Begin block 0x1d47
    prev=[0x1d0b], succ=[0xb59]
    =================================
    0x1d49: v1d49(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d5e: v1d5e = AND v1d49(0xffffffffffffffffffffffffffffffffffffffff), vb49
    0x1d5f: v1d5f(0x7) = CONST 
    0x1d61: v1d61(0x0) = CONST 
    0x1d64: v1d64 = SLOAD v1d5f(0x7)
    0x1d66: v1d66(0x100) = CONST 
    0x1d69: v1d69(0x1) = EXP v1d66(0x100), v1d61(0x0)
    0x1d6b: v1d6b = DIV v1d64, v1d69(0x1)
    0x1d6c: v1d6c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d81: v1d81 = AND v1d6c(0xffffffffffffffffffffffffffffffffffffffff), v1d6b
    0x1d82: v1d82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d97: v1d97 = AND v1d82(0xffffffffffffffffffffffffffffffffffffffff), v1d81
    0x1d98: v1d98(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1db9: v1db9(0x40) = CONST 
    0x1dbb: v1dbb = MLOAD v1db9(0x40)
    0x1dbc: v1dbc(0x40) = CONST 
    0x1dbe: v1dbe = MLOAD v1dbc(0x40)
    0x1dc1: v1dc1(0x0) = SUB v1dbb, v1dbe
    0x1dc3: LOG3 v1dbe, v1dc1(0x0), v1d98(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1d97, v1d5e
    0x1dc5: v1dc5(0x7) = CONST 
    0x1dc7: v1dc7(0x0) = CONST 
    0x1dc9: v1dc9(0x100) = CONST 
    0x1dcc: v1dcc(0x1) = EXP v1dc9(0x100), v1dc7(0x0)
    0x1dce: v1dce = SLOAD v1dc5(0x7)
    0x1dd0: v1dd0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1de5: v1de5(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1dd0(0xffffffffffffffffffffffffffffffffffffffff), v1dcc(0x1)
    0x1de6: v1de6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1de5(0xffffffffffffffffffffffffffffffffffffffff)
    0x1de7: v1de7 = AND v1de6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1dce
    0x1dea: v1dea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dff: v1dff = AND v1dea(0xffffffffffffffffffffffffffffffffffffffff), vb49
    0x1e00: v1e00 = MUL v1dff, v1dcc(0x1)
    0x1e01: v1e01 = OR v1e00, v1de7
    0x1e03: SSTORE v1dc5(0x7), v1e01
    0x1e06: JUMP vb26(0xb59)

    Begin block 0xb59
    prev=[0x1d47], succ=[]
    =================================
    0xb5a: STOP 

}

function 0xb5b(vb5barg0, vb5barg1, vb5barg2) private {
    Begin block 0xb5b
    prev=[], succ=[0xb66, 0xb6e]
    =================================
    0xb5c: vb5c(0x0) = CONST 
    0xb60: vb60 = EQ vb5barg1, vb5c(0x0)
    0xb61: vb61 = ISZERO vb60
    0xb62: vb62(0xb6e) = CONST 
    0xb65: JUMPI vb62(0xb6e), vb61

    Begin block 0xb66
    prev=[0xb5b], succ=[0x13384]
    =================================
    0xb66: vb66(0x0) = CONST 
    0xb6a: vb6a(0x13384) = CONST 
    0xb6d: JUMP vb6a(0x13384)

    Begin block 0x13384
    prev=[0xb66], succ=[]
    =================================
    0x13389: RETURNPRIVATE vb5barg2, vb66(0x0)

    Begin block 0xb6e
    prev=[0xb5b], succ=[0xb7e, 0xb7f]
    =================================
    0xb71: vb71 = MUL vb5barg1, vb5barg0
    0xb78: vb78 = ISZERO vb5barg1
    0xb79: vb79 = ISZERO vb78
    0xb7a: vb7a(0xb7f) = CONST 
    0xb7d: JUMPI vb7a(0xb7f), vb79

    Begin block 0xb7e
    prev=[0xb6e], succ=[]
    =================================
    0xb7e: THROW 

    Begin block 0xb7f
    prev=[0xb6e], succ=[0xb88, 0xb89]
    =================================
    0xb80: vb80 = DIV vb71, vb5barg1
    0xb81: vb81 = EQ vb80, vb5barg0
    0xb82: vb82 = ISZERO vb81
    0xb83: vb83 = ISZERO vb82
    0xb84: vb84(0xb89) = CONST 
    0xb87: JUMPI vb84(0xb89), vb83

    Begin block 0xb88
    prev=[0xb7f], succ=[]
    =================================
    0xb88: THROW 

    Begin block 0xb89
    prev=[0xb7f], succ=[0x133a9]
    =================================
    0x7b92: v7b92(0x133a9) = CONST 
    0x7bb2: JUMP v7b92(0x133a9)

    Begin block 0x133a9
    prev=[0xb89], succ=[]
    =================================
    0x133ae: RETURNPRIVATE vb5barg2, vb71

}

function 0xb93(vb93arg0, vb93arg1, vb93arg2) private {
    Begin block 0xb93
    prev=[], succ=[0xb9f, 0xba0]
    =================================
    0xb94: vb94(0x0) = CONST 
    0xb99: vb99 = ISZERO vb93arg0
    0xb9a: vb9a = ISZERO vb99
    0xb9b: vb9b(0xba0) = CONST 
    0xb9e: JUMPI vb9b(0xba0), vb9a

    Begin block 0xb9f
    prev=[0xb93], succ=[]
    =================================
    0xb9f: THROW 

    Begin block 0xba0
    prev=[0xb93], succ=[]
    =================================
    0xba1: vba1 = DIV vb93arg1, vb93arg0
    0xba8: RETURNPRIVATE vb93arg2, vba1

}

function 0xba9(vba9arg0, vba9arg1, vba9arg2) private {
    Begin block 0xba9
    prev=[], succ=[0xbbb, 0xbbc]
    =================================
    0xbaa: vbaa(0x0) = CONST 
    0xbae: vbae = ADD vba9arg1, vba9arg0
    0xbb3: vbb3 = LT vbae, vba9arg1
    0xbb4: vbb4 = ISZERO vbb3
    0xbb5: vbb5 = ISZERO vbb4
    0xbb6: vbb6 = ISZERO vbb5
    0xbb7: vbb7(0xbbc) = CONST 
    0xbba: JUMPI vbb7(0xbbc), vbb6

    Begin block 0xbbb
    prev=[0xba9], succ=[]
    =================================
    0xbbb: THROW 

    Begin block 0xbbc
    prev=[0xba9], succ=[]
    =================================
    0xbc4: RETURNPRIVATE vba9arg2, vbae

}

function 0xbc5(vbc5arg0, vbc5arg1, vbc5arg2) private {
    Begin block 0xbc5
    prev=[], succ=[0xbd2, 0xbd3]
    =================================
    0xbc6: vbc6(0x0) = CONST 
    0xbca: vbca = GT vbc5arg0, vbc5arg1
    0xbcb: vbcb = ISZERO vbca
    0xbcc: vbcc = ISZERO vbcb
    0xbcd: vbcd = ISZERO vbcc
    0xbce: vbce(0xbd3) = CONST 
    0xbd1: JUMPI vbce(0xbd3), vbcd

    Begin block 0xbd2
    prev=[0xbc5], succ=[]
    =================================
    0xbd2: THROW 

    Begin block 0xbd3
    prev=[0xbc5], succ=[]
    =================================
    0xbd6: vbd6 = SUB vbc5arg1, vbc5arg0
    0xbdd: RETURNPRIVATE vbc5arg2, vbd6

}

