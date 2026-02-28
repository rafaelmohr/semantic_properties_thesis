function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x8a) = CONST 
    0xc: JUMPI v9(0x8a), v8

    Begin block 0xd
    prev=[0x0], succ=[0x59, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x7565ce0c) = CONST 
    0x19: v19 = GT v14(0x7565ce0c), v12
    0x1a: v1a(0x59) = CONST 
    0x1d: JUMPI v1a(0x59), v19

    Begin block 0x59
    prev=[0xd], succ=[0x1e764, 0x65]
    =================================
    0x5b: v5b(0x217e98d1) = CONST 
    0x60: v60 = EQ v5b(0x217e98d1), v12
    0x1b564: v1b564(0x1e764) = CONST 
    0x1b584: JUMPI v1b564(0x1e764), v60

    Begin block 0x1e764
    prev=[0x59], succ=[]
    =================================
    0x1e784: v1e784(0x96) = CONST 
    0x1e7a4: CALLPRIVATE v1e784(0x96)

    Begin block 0x65
    prev=[0x59], succ=[0x1f164, 0x70]
    =================================
    0x66: v66(0x2bc31ca4) = CONST 
    0x6b: v6b = EQ v66(0x2bc31ca4), v12
    0x1bf64: v1bf64(0x1f164) = CONST 
    0x1bf84: JUMPI v1bf64(0x1f164), v6b

    Begin block 0x1f164
    prev=[0x65], succ=[]
    =================================
    0x1f184: v1f184(0xe5) = CONST 
    0x1f1a4: CALLPRIVATE v1f184(0xe5)

    Begin block 0x70
    prev=[0x65], succ=[0x1fb64, 0x7b]
    =================================
    0x71: v71(0x51c6590a) = CONST 
    0x76: v76 = EQ v71(0x51c6590a), v12
    0x1c964: v1c964(0x1fb64) = CONST 
    0x1c984: JUMPI v1c964(0x1fb64), v76

    Begin block 0x1fb64
    prev=[0x70], succ=[]
    =================================
    0x1fb84: v1fb84(0x126) = CONST 
    0x1fba4: CALLPRIVATE v1fb84(0x126)

    Begin block 0x7b
    prev=[0x70], succ=[0x86, 0x20564]
    =================================
    0x7c: v7c(0x715018a6) = CONST 
    0x81: v81 = EQ v7c(0x715018a6), v12
    0x1d364: v1d364(0x20564) = CONST 
    0x1d384: JUMPI v1d364(0x20564), v81

    Begin block 0x86
    prev=[0x7b], succ=[0x260e]
    =================================
    0x86: v86(0x260e) = CONST 
    0x89: JUMP v86(0x260e)

    Begin block 0x260e
    prev=[0x86], succ=[]
    =================================
    0x260f: v260f(0x0) = CONST 
    0x2612: REVERT v260f(0x0), v260f(0x0)

    Begin block 0x20564
    prev=[0x7b], succ=[]
    =================================
    0x20584: v20584(0x168) = CONST 
    0x205a4: CALLPRIVATE v20584(0x168)

    Begin block 0x1e
    prev=[0xd], succ=[0x20f64, 0x29]
    =================================
    0x1f: v1f(0x7565ce0c) = CONST 
    0x24: v24 = EQ v1f(0x7565ce0c), v12
    0x18364: v18364(0x20f64) = CONST 
    0x18384: JUMPI v18364(0x20f64), v24

    Begin block 0x20f64
    prev=[0x1e], succ=[]
    =================================
    0x20f84: v20f84(0x17f) = CONST 
    0x20fa4: CALLPRIVATE v20f84(0x17f)

    Begin block 0x29
    prev=[0x1e], succ=[0x21964, 0x34]
    =================================
    0x2a: v2a(0x8da5cb5b) = CONST 
    0x2f: v2f = EQ v2a(0x8da5cb5b), v12
    0x18d64: v18d64(0x21964) = CONST 
    0x18d84: JUMPI v18d64(0x21964), v2f

    Begin block 0x21964
    prev=[0x29], succ=[]
    =================================
    0x21984: v21984(0x196) = CONST 
    0x219a4: CALLPRIVATE v21984(0x196)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x22364]
    =================================
    0x35: v35(0xad5c4648) = CONST 
    0x3a: v3a = EQ v35(0xad5c4648), v12
    0x19764: v19764(0x22364) = CONST 
    0x19784: JUMPI v19764(0x22364), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x22d64, 0x4a]
    =================================
    0x40: v40(0xf2fde38b) = CONST 
    0x45: v45 = EQ v40(0xf2fde38b), v12
    0x1a164: v1a164(0x22d64) = CONST 
    0x1a184: JUMPI v1a164(0x22d64), v45

    Begin block 0x22d64
    prev=[0x3f], succ=[]
    =================================
    0x22d84: v22d84(0x218) = CONST 
    0x22da4: CALLPRIVATE v22d84(0x218)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0x23764]
    =================================
    0x4b: v4b(0xf8c587ac) = CONST 
    0x50: v50 = EQ v4b(0xf8c587ac), v12
    0x1ab64: v1ab64(0x23764) = CONST 
    0x1ab84: JUMPI v1ab64(0x23764), v50

    Begin block 0x55
    prev=[0x4a], succ=[0x25ea]
    =================================
    0x55: v55(0x25ea) = CONST 
    0x58: JUMP v55(0x25ea)

    Begin block 0x25ea
    prev=[0x55], succ=[]
    =================================
    0x25eb: v25eb(0x0) = CONST 
    0x25ee: REVERT v25eb(0x0), v25eb(0x0)

    Begin block 0x23764
    prev=[0x4a], succ=[]
    =================================
    0x23784: v23784(0x269) = CONST 
    0x237a4: CALLPRIVATE v23784(0x269)

    Begin block 0x22364
    prev=[0x34], succ=[]
    =================================
    0x22384: v22384(0x1d7) = CONST 
    0x223a4: CALLPRIVATE v22384(0x1d7)

    Begin block 0x8a
    prev=[0x0], succ=[0x1dd64, 0x2632]
    =================================
    0x8b: v8b = CALLDATASIZE 
    0x8c: v8c(0x2632) = CONST 
    0x8f: JUMPI v8c(0x2632), v8b

    Begin block 0x1dd64
    prev=[0x8a], succ=[]
    =================================
    0x1dd64: v1dd64(0x1dda4) = CONST 
    0x1dd84: CALLPRIVATE v1dd64(0x1dda4)

    Begin block 0x2632
    prev=[0x8a], succ=[]
    =================================
    0x2633: v2633(0x0) = CONST 
    0x2636: REVERT v2633(0x0), v2633(0x0)

}

function 0x10cb(v10cbarg0, v10cbarg1, v10cbarg2) private {
    Begin block 0x10cb
    prev=[], succ=[0x11a30x10cb]
    =================================
    0x10cc: v10cc(0x0) = CONST 
    0x10ce: v10ce(0x110d) = CONST 
    0x10d3: v10d3(0x40) = CONST 
    0x10d5: v10d5 = MLOAD v10d3(0x40)
    0x10d7: v10d7(0x40) = CONST 
    0x10d9: v10d9 = ADD v10d7(0x40), v10d5
    0x10da: v10da(0x40) = CONST 
    0x10dc: MSTORE v10da(0x40), v10d9
    0x10de: v10de(0x1a) = CONST 
    0x10e1: MSTORE v10d5, v10de(0x1a)
    0x10e2: v10e2(0x20) = CONST 
    0x10e4: v10e4 = ADD v10e2(0x20), v10d5
    0x10e5: v10e5(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1107: MSTORE v10e4, v10e5(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1109: v1109(0x11a3) = CONST 
    0x110c: JUMP v1109(0x11a3)

    Begin block 0x11a30x10cb
    prev=[0x10cb], succ=[0x11af0x10cb, 0x124f0x10cb]
    =================================
    0x11a40x10cb: v10cb11a4(0x0) = CONST 
    0x11a80x10cb: v10cb11a8 = GT v10cbarg0, v10cb11a4(0x0)
    0x11ab0x10cb: v10cb11ab(0x124f) = CONST 
    0x11ae0x10cb: JUMPI v10cb11ab(0x124f), v10cb11a8

    Begin block 0x11af0x10cb
    prev=[0x11a30x10cb], succ=[0x11f90x10cb]
    =================================
    0x11af0x10cb: v10cb11af(0x40) = CONST 
    0x11b10x10cb: v10cb11b1 = MLOAD v10cb11af(0x40)
    0x11b20x10cb: v10cb11b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11d40x10cb: MSTORE v10cb11b1, v10cb11b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11d50x10cb: v10cb11d5(0x4) = CONST 
    0x11d70x10cb: v10cb11d7 = ADD v10cb11d5(0x4), v10cb11b1
    0x11da0x10cb: v10cb11da(0x20) = CONST 
    0x11dc0x10cb: v10cb11dc = ADD v10cb11da(0x20), v10cb11d7
    0x11df0x10cb: v10cb11df(0x20) = SUB v10cb11dc, v10cb11d7
    0x11e10x10cb: MSTORE v10cb11d7, v10cb11df(0x20)
    0x11e50x10cb: v10cb11e5(0x1a) = MLOAD v10d5
    0x11e70x10cb: MSTORE v10cb11dc, v10cb11e5(0x1a)
    0x11e80x10cb: v10cb11e8(0x20) = CONST 
    0x11ea0x10cb: v10cb11ea = ADD v10cb11e8(0x20), v10cb11dc
    0x11ee0x10cb: v10cb11ee(0x1a) = MLOAD v10d5
    0x11f00x10cb: v10cb11f0(0x20) = CONST 
    0x11f20x10cb: v10cb11f2 = ADD v10cb11f0(0x20), v10d5
    0x11f70x10cb: v10cb11f7(0x0) = CONST 
    0x568c0x10cb: v10cb568c(0x11f9) = CONST 
    0x56ac0x10cb: JUMP v10cb568c(0x11f9)

    Begin block 0x11f90x10cb
    prev=[0x11af0x10cb, 0x12020x10cb], succ=[0x12140x10cb, 0x12020x10cb]
    =================================
    0x11f90x10cb_0x0: v11f910cb_0 = PHI v10cb120d, v10cb11f7(0x0)
    0x11fc0x10cb: v10cb11fc = LT v11f910cb_0, v10cb11ee(0x1a)
    0x11fd0x10cb: v10cb11fd = ISZERO v10cb11fc
    0x11fe0x10cb: v10cb11fe(0x1214) = CONST 
    0x12010x10cb: JUMPI v10cb11fe(0x1214), v10cb11fd

    Begin block 0x12140x10cb
    prev=[0x11f90x10cb], succ=[0x12280x10cb, 0x12410x10cb]
    =================================
    0x121d0x10cb: v10cb121d = ADD v10cb11ee(0x1a), v10cb11ea
    0x121f0x10cb: v10cb121f(0x1f) = CONST 
    0x12210x10cb: v10cb1221(0x1a) = AND v10cb121f(0x1f), v10cb11ee(0x1a)
    0x12230x10cb: v10cb1223(0x0) = ISZERO v10cb1221(0x1a)
    0x12240x10cb: v10cb1224(0x1241) = CONST 
    0x12270x10cb: JUMPI v10cb1224(0x1241), v10cb1223(0x0)

    Begin block 0x12280x10cb
    prev=[0x12140x10cb], succ=[0x12410x10cb]
    =================================
    0x122a0x10cb: v10cb122a = SUB v10cb121d, v10cb1221(0x1a)
    0x122c0x10cb: v10cb122c = MLOAD v10cb122a
    0x122d0x10cb: v10cb122d(0x1) = CONST 
    0x12300x10cb: v10cb1230(0x20) = CONST 
    0x12320x10cb: v10cb1232(0x6) = SUB v10cb1230(0x20), v10cb1221(0x1a)
    0x12330x10cb: v10cb1233(0x100) = CONST 
    0x12360x10cb: v10cb1236(0x1000000000000) = EXP v10cb1233(0x100), v10cb1232(0x6)
    0x12370x10cb: v10cb1237(0xffffffffffff) = SUB v10cb1236(0x1000000000000), v10cb122d(0x1)
    0x12380x10cb: v10cb1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffff000000000000) = NOT v10cb1237(0xffffffffffff)
    0x12390x10cb: v10cb1239 = AND v10cb1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffff000000000000), v10cb122c
    0x123b0x10cb: MSTORE v10cb122a, v10cb1239
    0x123c0x10cb: v10cb123c(0x20) = CONST 
    0x123e0x10cb: v10cb123e = ADD v10cb123c(0x20), v10cb122a
    0x608c0x10cb: v10cb608c(0x1241) = CONST 
    0x60ac0x10cb: JUMP v10cb608c(0x1241)

    Begin block 0x12410x10cb
    prev=[0x12280x10cb, 0x12140x10cb], succ=[]
    =================================
    0x12410x10cb_0x1: v124110cb_1 = PHI v10cb123e, v10cb121d
    0x12470x10cb: v10cb1247(0x40) = CONST 
    0x12490x10cb: v10cb1249 = MLOAD v10cb1247(0x40)
    0x124c0x10cb: v10cb124c = SUB v124110cb_1, v10cb1249
    0x124e0x10cb: REVERT v10cb1249, v10cb124c

    Begin block 0x12020x10cb
    prev=[0x11f90x10cb], succ=[0x11f90x10cb]
    =================================
    0x12020x10cb_0x0: v120210cb_0 = PHI v10cb120d, v10cb11f7(0x0)
    0x12040x10cb: v10cb1204 = ADD v10cb11f2, v120210cb_0
    0x12050x10cb: v10cb1205 = MLOAD v10cb1204
    0x12080x10cb: v10cb1208 = ADD v10cb11ea, v120210cb_0
    0x12090x10cb: MSTORE v10cb1208, v10cb1205
    0x120a0x10cb: v10cb120a(0x20) = CONST 
    0x120d0x10cb: v10cb120d = ADD v120210cb_0, v10cb120a(0x20)
    0x12100x10cb: v10cb1210(0x11f9) = CONST 
    0x12130x10cb: JUMP v10cb1210(0x11f9)

    Begin block 0x124f0x10cb
    prev=[0x11a30x10cb], succ=[0x125a0x10cb, 0x125b0x10cb]
    =================================
    0x12510x10cb: v10cb1251(0x0) = CONST 
    0x12560x10cb: v10cb1256(0x125b) = CONST 
    0x12590x10cb: JUMPI v10cb1256(0x125b), v10cbarg0

    Begin block 0x125a0x10cb
    prev=[0x124f0x10cb], succ=[]
    =================================
    0x125a0x10cb: THROW 

    Begin block 0x125b0x10cb
    prev=[0x124f0x10cb], succ=[0x110d0x10cb]
    =================================
    0x125c0x10cb: v10cb125c = DIV v10cbarg1, v10cbarg0
    0x12680x10cb: JUMP v10ce(0x110d)

    Begin block 0x110d0x10cb
    prev=[0x125b0x10cb], succ=[]
    =================================
    0x11140x10cb: RETURNPRIVATE v10cbarg2, v10cb125c

}

function 0x1115(v1115arg0, v1115arg1, v1115arg2) private {
    Begin block 0x1115
    prev=[], succ=[0x11200x1115, 0x11280x1115]
    =================================
    0x1116: v1116(0x0) = CONST 
    0x111a: v111a = EQ v1115arg1, v1116(0x0)
    0x111b: v111b = ISZERO v111a
    0x111c: v111c(0x1128) = CONST 
    0x111f: JUMPI v111c(0x1128), v111b

    Begin block 0x11200x1115
    prev=[0x1115], succ=[0xc1780x1115]
    =================================
    0x11200x1115: v11151120(0x0) = CONST 
    0x11240x1115: v11151124(0xc178) = CONST 
    0x11270x1115: JUMP v11151124(0xc178)

    Begin block 0xc1780x1115
    prev=[0x11200x1115], succ=[]
    =================================
    0xc17d0x1115: RETURNPRIVATE v1115arg2, v11151120(0x0)

    Begin block 0x11280x1115
    prev=[0x1115], succ=[0x11380x1115, 0x11390x1115]
    =================================
    0x11290x1115: v11151129(0x0) = CONST 
    0x112d0x1115: v1115112d = MUL v1115arg1, v1115arg0
    0x11340x1115: v11151134(0x1139) = CONST 
    0x11370x1115: JUMPI v11151134(0x1139), v1115arg1

    Begin block 0x11380x1115
    prev=[0x11280x1115], succ=[]
    =================================
    0x11380x1115: THROW 

    Begin block 0x11390x1115
    prev=[0x11280x1115], succ=[0x11400x1115, 0x11900x1115]
    =================================
    0x113a0x1115: v1115113a = DIV v1115112d, v1115arg1
    0x113b0x1115: v1115113b = EQ v1115113a, v1115arg0
    0x113c0x1115: v1115113c(0x1190) = CONST 
    0x113f0x1115: JUMPI v1115113c(0x1190), v1115113b

    Begin block 0x11400x1115
    prev=[0x11390x1115], succ=[]
    =================================
    0x11400x1115: v11151140(0x40) = CONST 
    0x11420x1115: v11151142 = MLOAD v11151140(0x40)
    0x11430x1115: v11151143(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11650x1115: MSTORE v11151142, v11151143(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11660x1115: v11151166(0x4) = CONST 
    0x11680x1115: v11151168 = ADD v11151166(0x4), v11151142
    0x116b0x1115: v1115116b(0x20) = CONST 
    0x116d0x1115: v1115116d = ADD v1115116b(0x20), v11151168
    0x11700x1115: v11151170(0x20) = SUB v1115116d, v11151168
    0x11720x1115: MSTORE v11151168, v11151170(0x20)
    0x11730x1115: v11151173(0x21) = CONST 
    0x11760x1115: MSTORE v1115116d, v11151173(0x21)
    0x11770x1115: v11151177(0x20) = CONST 
    0x11790x1115: v11151179 = ADD v11151177(0x20), v1115116d
    0x117b0x1115: v1115117b(0x1290) = CONST 
    0x117e0x1115: v1115117e(0x21) = CONST 
    0x11810x1115: CODECOPY v11151179, v1115117b(0x1290), v1115117e(0x21)
    0x11820x1115: v11151182(0x40) = CONST 
    0x11840x1115: v11151184 = ADD v11151182(0x40), v11151179
    0x11880x1115: v11151188(0x40) = CONST 
    0x118a0x1115: v1115118a = MLOAD v11151188(0x40)
    0x118d0x1115: v1115118d(0x84) = SUB v11151184, v1115118a
    0x118f0x1115: REVERT v1115118a, v1115118d(0x84)

    Begin block 0x11900x1115
    prev=[0x11390x1115], succ=[0xc19d0x1115]
    =================================
    0x4c8c0x1115: v11154c8c(0xc19d) = CONST 
    0x4cac0x1115: JUMP v11154c8c(0xc19d)

    Begin block 0xc19d0x1115
    prev=[0x11900x1115], succ=[]
    =================================
    0xc1a20x1115: RETURNPRIVATE v1115arg2, v1115112d

}

function addLiquidity(uint256)() public {
    Begin block 0x126
    prev=[], succ=[0x138, 0x13c]
    =================================
    0x127: v127(0x152) = CONST 
    0x12a: v12a(0x4) = CONST 
    0x12d: v12d = CALLDATASIZE 
    0x12e: v12e = SUB v12d, v12a(0x4)
    0x12f: v12f(0x20) = CONST 
    0x132: v132 = LT v12e, v12f(0x20)
    0x133: v133 = ISZERO v132
    0x134: v134(0x13c) = CONST 
    0x137: JUMPI v134(0x13c), v133

    Begin block 0x138
    prev=[0x126], succ=[]
    =================================
    0x138: v138(0x0) = CONST 
    0x13b: REVERT v138(0x0), v138(0x0)

    Begin block 0x13c
    prev=[0x126], succ=[0x4c8]
    =================================
    0x13e: v13e = ADD v12a(0x4), v12e
    0x142: v142 = CALLDATALOAD v12a(0x4)
    0x144: v144(0x20) = CONST 
    0x146: v146(0x24) = ADD v144(0x20), v12a(0x4)
    0x14e: v14e(0x4c8) = CONST 
    0x151: JUMP v14e(0x4c8)

    Begin block 0x4c8
    prev=[0x13c], succ=[0x119bB0x4c8]
    =================================
    0x4c9: v4c9(0x0) = CONST 
    0x4cb: v4cb(0x4d2) = CONST 
    0x4ce: v4ce(0x119b) = CONST 
    0x4d1: JUMP v4ce(0x119b)

    Begin block 0x119bB0x4c8
    prev=[0x4c8], succ=[0x4d2]
    =================================
    0x119cS0x4c8: v119cV4c8(0x0) = CONST 
    0x119eS0x4c8: v119eV4c8 = CALLER 
    0x11a2S0x4c8: JUMP v4cb(0x4d2)

    Begin block 0x4d2
    prev=[0x119bB0x4c8], succ=[0x525, 0x592]
    =================================
    0x4d3: v4d3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4e8: v4e8 = AND v4d3(0xffffffffffffffffffffffffffffffffffffffff), v119eV4c8
    0x4e9: v4e9(0x0) = CONST 
    0x4ec: v4ec = SLOAD v4e9(0x0)
    0x4ee: v4ee(0x100) = CONST 
    0x4f1: v4f1(0x1) = EXP v4ee(0x100), v4e9(0x0)
    0x4f3: v4f3 = DIV v4ec, v4f1(0x1)
    0x4f4: v4f4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x509: v509 = AND v4f4(0xffffffffffffffffffffffffffffffffffffffff), v4f3
    0x50a: v50a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x51f: v51f = AND v50a(0xffffffffffffffffffffffffffffffffffffffff), v509
    0x520: v520 = EQ v51f, v4e8
    0x521: v521(0x592) = CONST 
    0x524: JUMPI v521(0x592), v520

    Begin block 0x525
    prev=[0x4d2], succ=[]
    =================================
    0x525: v525(0x40) = CONST 
    0x527: v527 = MLOAD v525(0x40)
    0x528: v528(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x54a: MSTORE v527, v528(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x54b: v54b(0x4) = CONST 
    0x54d: v54d = ADD v54b(0x4), v527
    0x550: v550(0x20) = CONST 
    0x552: v552 = ADD v550(0x20), v54d
    0x555: v555(0x20) = SUB v552, v54d
    0x557: MSTORE v54d, v555(0x20)
    0x558: v558(0x20) = CONST 
    0x55b: MSTORE v552, v558(0x20)
    0x55c: v55c(0x20) = CONST 
    0x55e: v55e = ADD v55c(0x20), v552
    0x560: v560(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x582: MSTORE v55e, v560(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x584: v584(0x20) = CONST 
    0x586: v586 = ADD v584(0x20), v55e
    0x58a: v58a(0x40) = CONST 
    0x58c: v58c = MLOAD v58a(0x40)
    0x58f: v58f(0x64) = SUB v586, v58c
    0x591: REVERT v58c, v58f(0x64)

    Begin block 0x592
    prev=[0x4d2], succ=[0x59b]
    =================================
    0x593: v593(0x59b) = CONST 
    0x596: v596 = CALLVALUE 
    0x597: v597(0x2aa) = CONST 
    0x59a: v59a_0 = CALLPRIVATE v597(0x2aa), v596, v593(0x59b)

    Begin block 0x59b
    prev=[0x592], succ=[0x5a6, 0x613]
    =================================
    0x59e: v59e(0x0) = CONST 
    0x5a1: v5a1 = GT v59a_0, v59e(0x0)
    0x5a2: v5a2(0x613) = CONST 
    0x5a5: JUMPI v5a2(0x613), v5a1

    Begin block 0x5a6
    prev=[0x59b], succ=[]
    =================================
    0x5a6: v5a6(0x40) = CONST 
    0x5a8: v5a8 = MLOAD v5a6(0x40)
    0x5a9: v5a9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x5cb: MSTORE v5a8, v5a9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5cc: v5cc(0x4) = CONST 
    0x5ce: v5ce = ADD v5cc(0x4), v5a8
    0x5d1: v5d1(0x20) = CONST 
    0x5d3: v5d3 = ADD v5d1(0x20), v5ce
    0x5d6: v5d6(0x20) = SUB v5d3, v5ce
    0x5d8: MSTORE v5ce, v5d6(0x20)
    0x5d9: v5d9(0x1d) = CONST 
    0x5dc: MSTORE v5d3, v5d9(0x1d)
    0x5dd: v5dd(0x20) = CONST 
    0x5df: v5df = ADD v5dd(0x20), v5d3
    0x5e1: v5e1(0x416464726573733a20696e73756666696369656e742062616c616e6365000000) = CONST 
    0x603: MSTORE v5df, v5e1(0x416464726573733a20696e73756666696369656e742062616c616e6365000000)
    0x605: v605(0x20) = CONST 
    0x607: v607 = ADD v605(0x20), v5df
    0x60b: v60b(0x40) = CONST 
    0x60d: v60d = MLOAD v60b(0x40)
    0x610: v610(0x64) = SUB v607, v60d
    0x612: REVERT v60d, v610(0x64)

    Begin block 0x613
    prev=[0x59b], succ=[0x6a2, 0x6a6]
    =================================
    0x614: v614(0x1) = CONST 
    0x616: v616(0x0) = CONST 
    0x619: v619 = SLOAD v614(0x1)
    0x61b: v61b(0x100) = CONST 
    0x61e: v61e(0x1) = EXP v61b(0x100), v616(0x0)
    0x620: v620 = DIV v619, v61e(0x1)
    0x621: v621(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x636: v636 = AND v621(0xffffffffffffffffffffffffffffffffffffffff), v620
    0x637: v637(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x64c: v64c = AND v637(0xffffffffffffffffffffffffffffffffffffffff), v636
    0x64d: v64d(0xd1550b10) = CONST 
    0x652: v652 = ADDRESS 
    0x654: v654(0x40) = CONST 
    0x656: v656 = MLOAD v654(0x40)
    0x658: v658(0xffffffff) = CONST 
    0x65d: v65d(0xd1550b10) = AND v658(0xffffffff), v64d(0xd1550b10)
    0x65e: v65e(0xe0) = CONST 
    0x660: v660(0xd1550b1000000000000000000000000000000000000000000000000000000000) = SHL v65e(0xe0), v65d(0xd1550b10)
    0x662: MSTORE v656, v660(0xd1550b1000000000000000000000000000000000000000000000000000000000)
    0x663: v663(0x4) = CONST 
    0x665: v665 = ADD v663(0x4), v656
    0x668: v668(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x67d: v67d = AND v668(0xffffffffffffffffffffffffffffffffffffffff), v652
    0x67f: MSTORE v665, v67d
    0x680: v680(0x20) = CONST 
    0x682: v682 = ADD v680(0x20), v665
    0x685: MSTORE v682, v59a_0
    0x686: v686(0x20) = CONST 
    0x688: v688 = ADD v686(0x20), v682
    0x68d: v68d(0x20) = CONST 
    0x68f: v68f(0x40) = CONST 
    0x691: v691 = MLOAD v68f(0x40)
    0x694: v694(0x44) = SUB v688, v691
    0x696: v696(0x0) = CONST 
    0x69a: v69a = EXTCODESIZE v64c
    0x69b: v69b = ISZERO v69a
    0x69d: v69d = ISZERO v69b
    0x69e: v69e(0x6a6) = CONST 
    0x6a1: JUMPI v69e(0x6a6), v69d

    Begin block 0x6a2
    prev=[0x613], succ=[]
    =================================
    0x6a2: v6a2(0x0) = CONST 
    0x6a5: REVERT v6a2(0x0), v6a2(0x0)

    Begin block 0x6a6
    prev=[0x613], succ=[0x6b1, 0x6ba]
    =================================
    0x6a8: v6a8 = GAS 
    0x6a9: v6a9 = CALL v6a8, v64c, v696(0x0), v691, v694(0x44), v691, v68d(0x20)
    0x6aa: v6aa = ISZERO v6a9
    0x6ac: v6ac = ISZERO v6aa
    0x6ad: v6ad(0x6ba) = CONST 
    0x6b0: JUMPI v6ad(0x6ba), v6ac

    Begin block 0x6b1
    prev=[0x6a6], succ=[]
    =================================
    0x6b1: v6b1 = RETURNDATASIZE 
    0x6b2: v6b2(0x0) = CONST 
    0x6b5: RETURNDATACOPY v6b2(0x0), v6b2(0x0), v6b1
    0x6b6: v6b6 = RETURNDATASIZE 
    0x6b7: v6b7(0x0) = CONST 
    0x6b9: REVERT v6b7(0x0), v6b6

    Begin block 0x6ba
    prev=[0x6a6], succ=[0x6cc, 0x6d0]
    =================================
    0x6bf: v6bf(0x40) = CONST 
    0x6c1: v6c1 = MLOAD v6bf(0x40)
    0x6c2: v6c2 = RETURNDATASIZE 
    0x6c3: v6c3(0x20) = CONST 
    0x6c6: v6c6 = LT v6c2, v6c3(0x20)
    0x6c7: v6c7 = ISZERO v6c6
    0x6c8: v6c8(0x6d0) = CONST 
    0x6cb: JUMPI v6c8(0x6d0), v6c7

    Begin block 0x6cc
    prev=[0x6ba], succ=[]
    =================================
    0x6cc: v6cc(0x0) = CONST 
    0x6cf: REVERT v6cc(0x0), v6cc(0x0)

    Begin block 0x6d0
    prev=[0x6ba], succ=[0x757]
    =================================
    0x6d2: v6d2 = ADD v6c1, v6c2
    0x6d6: v6d6 = MLOAD v6c1
    0x6d8: v6d8(0x20) = CONST 
    0x6da: v6da = ADD v6d8(0x20), v6c1
    0x6e3: v6e3(0x1) = CONST 
    0x6e5: v6e5(0x0) = CONST 
    0x6e8: v6e8 = SLOAD v6e3(0x1)
    0x6ea: v6ea(0x100) = CONST 
    0x6ed: v6ed(0x1) = EXP v6ea(0x100), v6e5(0x0)
    0x6ef: v6ef = DIV v6e8, v6ed(0x1)
    0x6f0: v6f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x705: v705 = AND v6f0(0xffffffffffffffffffffffffffffffffffffffff), v6ef
    0x706: v706(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x71b: v71b = AND v706(0xffffffffffffffffffffffffffffffffffffffff), v705
    0x71c: v71c(0xd1550b10) = CONST 
    0x721: v721(0x5) = CONST 
    0x723: v723(0x0) = CONST 
    0x726: v726 = SLOAD v721(0x5)
    0x728: v728(0x100) = CONST 
    0x72b: v72b(0x1) = EXP v728(0x100), v723(0x0)
    0x72d: v72d = DIV v726, v72b(0x1)
    0x72e: v72e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x743: v743 = AND v72e(0xffffffffffffffffffffffffffffffffffffffff), v72d
    0x744: v744(0x757) = CONST 
    0x747: v747(0xa) = CONST 
    0x74a: v74a(0x10cb) = CONST 
    0x750: v750(0xffffffff) = CONST 
    0x755: v755(0x10cb) = AND v750(0xffffffff), v74a(0x10cb)
    0x756: v756_0 = CALLPRIVATE v755(0x10cb), v747(0xa), v59a_0, v744(0x757)

    Begin block 0x757
    prev=[0x6d0], succ=[0x7a6, 0x7aa]
    =================================
    0x758: v758(0x40) = CONST 
    0x75a: v75a = MLOAD v758(0x40)
    0x75c: v75c(0xffffffff) = CONST 
    0x761: v761(0xd1550b10) = AND v75c(0xffffffff), v71c(0xd1550b10)
    0x762: v762(0xe0) = CONST 
    0x764: v764(0xd1550b1000000000000000000000000000000000000000000000000000000000) = SHL v762(0xe0), v761(0xd1550b10)
    0x766: MSTORE v75a, v764(0xd1550b1000000000000000000000000000000000000000000000000000000000)
    0x767: v767(0x4) = CONST 
    0x769: v769 = ADD v767(0x4), v75a
    0x76c: v76c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x781: v781 = AND v76c(0xffffffffffffffffffffffffffffffffffffffff), v743
    0x783: MSTORE v769, v781
    0x784: v784(0x20) = CONST 
    0x786: v786 = ADD v784(0x20), v769
    0x789: MSTORE v786, v756_0
    0x78a: v78a(0x20) = CONST 
    0x78c: v78c = ADD v78a(0x20), v786
    0x791: v791(0x20) = CONST 
    0x793: v793(0x40) = CONST 
    0x795: v795 = MLOAD v793(0x40)
    0x798: v798(0x44) = SUB v78c, v795
    0x79a: v79a(0x0) = CONST 
    0x79e: v79e = EXTCODESIZE v71b
    0x79f: v79f = ISZERO v79e
    0x7a1: v7a1 = ISZERO v79f
    0x7a2: v7a2(0x7aa) = CONST 
    0x7a5: JUMPI v7a2(0x7aa), v7a1

    Begin block 0x7a6
    prev=[0x757], succ=[]
    =================================
    0x7a6: v7a6(0x0) = CONST 
    0x7a9: REVERT v7a6(0x0), v7a6(0x0)

    Begin block 0x7aa
    prev=[0x757], succ=[0x7b5, 0x7be]
    =================================
    0x7ac: v7ac = GAS 
    0x7ad: v7ad = CALL v7ac, v71b, v79a(0x0), v795, v798(0x44), v795, v791(0x20)
    0x7ae: v7ae = ISZERO v7ad
    0x7b0: v7b0 = ISZERO v7ae
    0x7b1: v7b1(0x7be) = CONST 
    0x7b4: JUMPI v7b1(0x7be), v7b0

    Begin block 0x7b5
    prev=[0x7aa], succ=[]
    =================================
    0x7b5: v7b5 = RETURNDATASIZE 
    0x7b6: v7b6(0x0) = CONST 
    0x7b9: RETURNDATACOPY v7b6(0x0), v7b6(0x0), v7b5
    0x7ba: v7ba = RETURNDATASIZE 
    0x7bb: v7bb(0x0) = CONST 
    0x7bd: REVERT v7bb(0x0), v7ba

    Begin block 0x7be
    prev=[0x7aa], succ=[0x7d0, 0x7d4]
    =================================
    0x7c3: v7c3(0x40) = CONST 
    0x7c5: v7c5 = MLOAD v7c3(0x40)
    0x7c6: v7c6 = RETURNDATASIZE 
    0x7c7: v7c7(0x20) = CONST 
    0x7ca: v7ca = LT v7c6, v7c7(0x20)
    0x7cb: v7cb = ISZERO v7ca
    0x7cc: v7cc(0x7d4) = CONST 
    0x7cf: JUMPI v7cc(0x7d4), v7cb

    Begin block 0x7d0
    prev=[0x7be], succ=[]
    =================================
    0x7d0: v7d0(0x0) = CONST 
    0x7d3: REVERT v7d0(0x0), v7d0(0x0)

    Begin block 0x7d4
    prev=[0x7be], succ=[0x864]
    =================================
    0x7d6: v7d6 = ADD v7c5, v7c6
    0x7da: v7da = MLOAD v7c5
    0x7dc: v7dc(0x20) = CONST 
    0x7de: v7de = ADD v7dc(0x20), v7c5
    0x7e7: v7e7(0x3) = CONST 
    0x7e9: v7e9(0x0) = CONST 
    0x7ec: v7ec = SLOAD v7e7(0x3)
    0x7ee: v7ee(0x100) = CONST 
    0x7f1: v7f1(0x1) = EXP v7ee(0x100), v7e9(0x0)
    0x7f3: v7f3 = DIV v7ec, v7f1(0x1)
    0x7f4: v7f4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x809: v809 = AND v7f4(0xffffffffffffffffffffffffffffffffffffffff), v7f3
    0x80a: v80a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x81f: v81f = AND v80a(0xffffffffffffffffffffffffffffffffffffffff), v809
    0x820: v820(0xf305d719) = CONST 
    0x825: v825 = CALLVALUE 
    0x826: v826(0x1) = CONST 
    0x828: v828(0x0) = CONST 
    0x82b: v82b = SLOAD v826(0x1)
    0x82d: v82d(0x100) = CONST 
    0x830: v830(0x1) = EXP v82d(0x100), v828(0x0)
    0x832: v832 = DIV v82b, v830(0x1)
    0x833: v833(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x848: v848 = AND v833(0xffffffffffffffffffffffffffffffffffffffff), v832
    0x84a: v84a(0x872) = CONST 
    0x84d: v84d(0x64) = CONST 
    0x84f: v84f(0x864) = CONST 
    0x853: v853(0x64) = CONST 
    0x855: v855 = SUB v853(0x64), v142
    0x857: v857(0x1115) = CONST 
    0x85d: v85d(0xffffffff) = CONST 
    0x862: v862(0x1115) = AND v85d(0xffffffff), v857(0x1115)
    0x863: v863_0 = CALLPRIVATE v862(0x1115), v855, v59a_0, v84f(0x864)

    Begin block 0x864
    prev=[0x7d4], succ=[0x872]
    =================================
    0x865: v865(0x10cb) = CONST 
    0x86b: v86b(0xffffffff) = CONST 
    0x870: v870(0x10cb) = AND v86b(0xffffffff), v865(0x10cb)
    0x871: v871_0 = CALLPRIVATE v870(0x10cb), v84d(0x64), v863_0, v84a(0x872)

    Begin block 0x872
    prev=[0x864], succ=[0x88d]
    =================================
    0x873: v873(0x89b) = CONST 
    0x876: v876(0x64) = CONST 
    0x878: v878(0x88d) = CONST 
    0x87c: v87c(0x64) = CONST 
    0x87e: v87e = SUB v87c(0x64), v142
    0x87f: v87f = CALLVALUE 
    0x880: v880(0x1115) = CONST 
    0x886: v886(0xffffffff) = CONST 
    0x88b: v88b(0x1115) = AND v886(0xffffffff), v880(0x1115)
    0x88c: v88c_0 = CALLPRIVATE v88b(0x1115), v87e, v87f, v878(0x88d)

    Begin block 0x88d
    prev=[0x872], succ=[0x89b]
    =================================
    0x88e: v88e(0x10cb) = CONST 
    0x894: v894(0xffffffff) = CONST 
    0x899: v899(0x10cb) = AND v894(0xffffffff), v88e(0x10cb)
    0x89a: v89a_0 = CALLPRIVATE v899(0x10cb), v876(0x64), v88c_0, v873(0x89b)

    Begin block 0x89b
    prev=[0x88d], succ=[0x943, 0x947]
    =================================
    0x89c: v89c(0x5) = CONST 
    0x89e: v89e(0x0) = CONST 
    0x8a1: v8a1 = SLOAD v89c(0x5)
    0x8a3: v8a3(0x100) = CONST 
    0x8a6: v8a6(0x1) = EXP v8a3(0x100), v89e(0x0)
    0x8a8: v8a8 = DIV v8a1, v8a6(0x1)
    0x8a9: v8a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8be: v8be = AND v8a9(0xffffffffffffffffffffffffffffffffffffffff), v8a8
    0x8bf: v8bf(0x4b0) = CONST 
    0x8c2: v8c2 = TIMESTAMP 
    0x8c3: v8c3 = ADD v8c2, v8bf(0x4b0)
    0x8c4: v8c4(0x40) = CONST 
    0x8c6: v8c6 = MLOAD v8c4(0x40)
    0x8c8: v8c8(0xffffffff) = CONST 
    0x8cd: v8cd(0xf305d719) = AND v8c8(0xffffffff), v820(0xf305d719)
    0x8ce: v8ce(0xe0) = CONST 
    0x8d0: v8d0(0xf305d71900000000000000000000000000000000000000000000000000000000) = SHL v8ce(0xe0), v8cd(0xf305d719)
    0x8d2: MSTORE v8c6, v8d0(0xf305d71900000000000000000000000000000000000000000000000000000000)
    0x8d3: v8d3(0x4) = CONST 
    0x8d5: v8d5 = ADD v8d3(0x4), v8c6
    0x8d8: v8d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8ed: v8ed = AND v8d8(0xffffffffffffffffffffffffffffffffffffffff), v848
    0x8ef: MSTORE v8d5, v8ed
    0x8f0: v8f0(0x20) = CONST 
    0x8f2: v8f2 = ADD v8f0(0x20), v8d5
    0x8f5: MSTORE v8f2, v59a_0
    0x8f6: v8f6(0x20) = CONST 
    0x8f8: v8f8 = ADD v8f6(0x20), v8f2
    0x8fb: MSTORE v8f8, v871_0
    0x8fc: v8fc(0x20) = CONST 
    0x8fe: v8fe = ADD v8fc(0x20), v8f8
    0x901: MSTORE v8fe, v89a_0
    0x902: v902(0x20) = CONST 
    0x904: v904 = ADD v902(0x20), v8fe
    0x906: v906(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x91b: v91b = AND v906(0xffffffffffffffffffffffffffffffffffffffff), v8be
    0x91d: MSTORE v904, v91b
    0x91e: v91e(0x20) = CONST 
    0x920: v920 = ADD v91e(0x20), v904
    0x923: MSTORE v920, v8c3
    0x924: v924(0x20) = CONST 
    0x926: v926 = ADD v924(0x20), v920
    0x92f: v92f(0x60) = CONST 
    0x931: v931(0x40) = CONST 
    0x933: v933 = MLOAD v931(0x40)
    0x936: v936(0xc4) = SUB v926, v933
    0x93b: v93b = EXTCODESIZE v81f
    0x93c: v93c = ISZERO v93b
    0x93e: v93e = ISZERO v93c
    0x93f: v93f(0x947) = CONST 
    0x942: JUMPI v93f(0x947), v93e

    Begin block 0x943
    prev=[0x89b], succ=[]
    =================================
    0x943: v943(0x0) = CONST 
    0x946: REVERT v943(0x0), v943(0x0)

    Begin block 0x947
    prev=[0x89b], succ=[0x952, 0x95b]
    =================================
    0x949: v949 = GAS 
    0x94a: v94a = CALL v949, v81f, v825, v933, v936(0xc4), v933, v92f(0x60)
    0x94b: v94b = ISZERO v94a
    0x94d: v94d = ISZERO v94b
    0x94e: v94e(0x95b) = CONST 
    0x951: JUMPI v94e(0x95b), v94d

    Begin block 0x952
    prev=[0x947], succ=[]
    =================================
    0x952: v952 = RETURNDATASIZE 
    0x953: v953(0x0) = CONST 
    0x956: RETURNDATACOPY v953(0x0), v953(0x0), v952
    0x957: v957 = RETURNDATASIZE 
    0x958: v958(0x0) = CONST 
    0x95a: REVERT v958(0x0), v957

    Begin block 0x95b
    prev=[0x947], succ=[0x96e, 0x972]
    =================================
    0x961: v961(0x40) = CONST 
    0x963: v963 = MLOAD v961(0x40)
    0x964: v964 = RETURNDATASIZE 
    0x965: v965(0x60) = CONST 
    0x968: v968 = LT v964, v965(0x60)
    0x969: v969 = ISZERO v968
    0x96a: v96a(0x972) = CONST 
    0x96d: JUMPI v96a(0x972), v969

    Begin block 0x96e
    prev=[0x95b], succ=[]
    =================================
    0x96e: v96e(0x0) = CONST 
    0x971: REVERT v96e(0x0), v96e(0x0)

    Begin block 0x972
    prev=[0x95b], succ=[0x152]
    =================================
    0x974: v974 = ADD v963, v964
    0x978: v978 = MLOAD v963
    0x97a: v97a(0x20) = CONST 
    0x97c: v97c = ADD v97a(0x20), v963
    0x982: v982 = MLOAD v97c
    0x984: v984(0x20) = CONST 
    0x986: v986 = ADD v984(0x20), v97c
    0x98c: v98c = MLOAD v986
    0x98e: v98e(0x20) = CONST 
    0x990: v990 = ADD v98e(0x20), v986
    0x99b: v99b(0x4f32e21ffe815036d86a63960777b4cb6faa90dc830d1d42d86624412cfd19e9) = CONST 
    0x9bc: v9bc = CALLVALUE 
    0x9be: v9be(0x40) = CONST 
    0x9c0: v9c0 = MLOAD v9be(0x40)
    0x9c4: MSTORE v9c0, v9bc
    0x9c5: v9c5(0x20) = CONST 
    0x9c7: v9c7 = ADD v9c5(0x20), v9c0
    0x9ca: MSTORE v9c7, v59a_0
    0x9cb: v9cb(0x20) = CONST 
    0x9cd: v9cd = ADD v9cb(0x20), v9c7
    0x9d2: v9d2(0x40) = CONST 
    0x9d4: v9d4 = MLOAD v9d2(0x40)
    0x9d7: v9d7(0x40) = SUB v9cd, v9d4
    0x9d9: LOG1 v9d4, v9d7(0x40), v99b(0x4f32e21ffe815036d86a63960777b4cb6faa90dc830d1d42d86624412cfd19e9)
    0x9dd: JUMP v127(0x152)

    Begin block 0x152
    prev=[0x972], succ=[]
    =================================
    0x153: v153(0x40) = CONST 
    0x155: v155 = MLOAD v153(0x40)
    0x159: MSTORE v155, v59a_0
    0x15a: v15a(0x20) = CONST 
    0x15c: v15c = ADD v15a(0x20), v155
    0x160: v160(0x40) = CONST 
    0x162: v162 = MLOAD v160(0x40)
    0x165: v165(0x20) = SUB v15c, v162
    0x167: RETURN v162, v165(0x20)

}

function renounceOwnership()() public {
    Begin block 0x168
    prev=[], succ=[0x170, 0x174]
    =================================
    0x169: v169 = CALLVALUE 
    0x16b: v16b = ISZERO v169
    0x16c: v16c(0x174) = CONST 
    0x16f: JUMPI v16c(0x174), v16b

    Begin block 0x170
    prev=[0x168], succ=[]
    =================================
    0x170: v170(0x0) = CONST 
    0x173: REVERT v170(0x0), v170(0x0)

    Begin block 0x174
    prev=[0x168], succ=[0x9de]
    =================================
    0x176: v176(0x17d) = CONST 
    0x179: v179(0x9de) = CONST 
    0x17c: JUMP v179(0x9de)

    Begin block 0x9de
    prev=[0x174], succ=[0x119bB0x9de]
    =================================
    0x9df: v9df(0x9e6) = CONST 
    0x9e2: v9e2(0x119b) = CONST 
    0x9e5: JUMP v9e2(0x119b)

    Begin block 0x119bB0x9de
    prev=[0x9de], succ=[0x9e6]
    =================================
    0x119cS0x9de: v119cV9de(0x0) = CONST 
    0x119eS0x9de: v119eV9de = CALLER 
    0x11a2S0x9de: JUMP v9df(0x9e6)

    Begin block 0x9e6
    prev=[0x119bB0x9de], succ=[0xa39, 0xaa6]
    =================================
    0x9e7: v9e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9fc: v9fc = AND v9e7(0xffffffffffffffffffffffffffffffffffffffff), v119eV9de
    0x9fd: v9fd(0x0) = CONST 
    0xa00: va00 = SLOAD v9fd(0x0)
    0xa02: va02(0x100) = CONST 
    0xa05: va05(0x1) = EXP va02(0x100), v9fd(0x0)
    0xa07: va07 = DIV va00, va05(0x1)
    0xa08: va08(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa1d: va1d = AND va08(0xffffffffffffffffffffffffffffffffffffffff), va07
    0xa1e: va1e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa33: va33 = AND va1e(0xffffffffffffffffffffffffffffffffffffffff), va1d
    0xa34: va34 = EQ va33, v9fc
    0xa35: va35(0xaa6) = CONST 
    0xa38: JUMPI va35(0xaa6), va34

    Begin block 0xa39
    prev=[0x9e6], succ=[]
    =================================
    0xa39: va39(0x40) = CONST 
    0xa3b: va3b = MLOAD va39(0x40)
    0xa3c: va3c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa5e: MSTORE va3b, va3c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa5f: va5f(0x4) = CONST 
    0xa61: va61 = ADD va5f(0x4), va3b
    0xa64: va64(0x20) = CONST 
    0xa66: va66 = ADD va64(0x20), va61
    0xa69: va69(0x20) = SUB va66, va61
    0xa6b: MSTORE va61, va69(0x20)
    0xa6c: va6c(0x20) = CONST 
    0xa6f: MSTORE va66, va6c(0x20)
    0xa70: va70(0x20) = CONST 
    0xa72: va72 = ADD va70(0x20), va66
    0xa74: va74(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xa96: MSTORE va72, va74(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xa98: va98(0x20) = CONST 
    0xa9a: va9a = ADD va98(0x20), va72
    0xa9e: va9e(0x40) = CONST 
    0xaa0: vaa0 = MLOAD va9e(0x40)
    0xaa3: vaa3(0x64) = SUB va9a, vaa0
    0xaa5: REVERT vaa0, vaa3(0x64)

    Begin block 0xaa6
    prev=[0x9e6], succ=[0x17d]
    =================================
    0xaa7: vaa7(0x0) = CONST 
    0xaa9: vaa9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xabe: vabe(0x0) = AND vaa9(0xffffffffffffffffffffffffffffffffffffffff), vaa7(0x0)
    0xabf: vabf(0x0) = CONST 
    0xac2: vac2 = SLOAD vabf(0x0)
    0xac4: vac4(0x100) = CONST 
    0xac7: vac7(0x1) = EXP vac4(0x100), vabf(0x0)
    0xac9: vac9 = DIV vac2, vac7(0x1)
    0xaca: vaca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xadf: vadf = AND vaca(0xffffffffffffffffffffffffffffffffffffffff), vac9
    0xae0: vae0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf5: vaf5 = AND vae0(0xffffffffffffffffffffffffffffffffffffffff), vadf
    0xaf6: vaf6(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xb17: vb17(0x40) = CONST 
    0xb19: vb19 = MLOAD vb17(0x40)
    0xb1a: vb1a(0x40) = CONST 
    0xb1c: vb1c = MLOAD vb1a(0x40)
    0xb1f: vb1f(0x0) = SUB vb19, vb1c
    0xb21: LOG3 vb1c, vb1f(0x0), vaf6(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vaf5, vabe(0x0)
    0xb22: vb22(0x0) = CONST 
    0xb25: vb25(0x0) = CONST 
    0xb27: vb27(0x100) = CONST 
    0xb2a: vb2a(0x1) = EXP vb27(0x100), vb25(0x0)
    0xb2c: vb2c = SLOAD vb22(0x0)
    0xb2e: vb2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb43: vb43(0xffffffffffffffffffffffffffffffffffffffff) = MUL vb2e(0xffffffffffffffffffffffffffffffffffffffff), vb2a(0x1)
    0xb44: vb44(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vb43(0xffffffffffffffffffffffffffffffffffffffff)
    0xb45: vb45 = AND vb44(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb2c
    0xb48: vb48(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb5d: vb5d(0x0) = AND vb48(0xffffffffffffffffffffffffffffffffffffffff), vb22(0x0)
    0xb5e: vb5e(0x0) = MUL vb5d(0x0), vb2a(0x1)
    0xb5f: vb5f = OR vb5e(0x0), vb45
    0xb61: SSTORE vb22(0x0), vb5f
    0xb63: JUMP v176(0x17d)

    Begin block 0x17d
    prev=[0xaa6], succ=[]
    =================================
    0x17e: STOP 

}

function releaseBalances()() public {
    Begin block 0x17f
    prev=[], succ=[0x187, 0x18b]
    =================================
    0x180: v180 = CALLVALUE 
    0x182: v182 = ISZERO v180
    0x183: v183(0x18b) = CONST 
    0x186: JUMPI v183(0x18b), v182

    Begin block 0x187
    prev=[0x17f], succ=[]
    =================================
    0x187: v187(0x0) = CONST 
    0x18a: REVERT v187(0x0), v187(0x0)

    Begin block 0x18b
    prev=[0x17f], succ=[0xb64]
    =================================
    0x18d: v18d(0x194) = CONST 
    0x190: v190(0xb64) = CONST 
    0x193: JUMP v190(0xb64)

    Begin block 0xb64
    prev=[0x18b], succ=[0x119bB0xb64]
    =================================
    0xb65: vb65(0xb6c) = CONST 
    0xb68: vb68(0x119b) = CONST 
    0xb6b: JUMP vb68(0x119b)

    Begin block 0x119bB0xb64
    prev=[0xb64], succ=[0xb6c]
    =================================
    0x119cS0xb64: v119cVb64(0x0) = CONST 
    0x119eS0xb64: v119eVb64 = CALLER 
    0x11a2S0xb64: JUMP vb65(0xb6c)

    Begin block 0xb6c
    prev=[0x119bB0xb64], succ=[0xbbf, 0xc2c]
    =================================
    0xb6d: vb6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb82: vb82 = AND vb6d(0xffffffffffffffffffffffffffffffffffffffff), v119eVb64
    0xb83: vb83(0x0) = CONST 
    0xb86: vb86 = SLOAD vb83(0x0)
    0xb88: vb88(0x100) = CONST 
    0xb8b: vb8b(0x1) = EXP vb88(0x100), vb83(0x0)
    0xb8d: vb8d = DIV vb86, vb8b(0x1)
    0xb8e: vb8e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xba3: vba3 = AND vb8e(0xffffffffffffffffffffffffffffffffffffffff), vb8d
    0xba4: vba4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbb9: vbb9 = AND vba4(0xffffffffffffffffffffffffffffffffffffffff), vba3
    0xbba: vbba = EQ vbb9, vb82
    0xbbb: vbbb(0xc2c) = CONST 
    0xbbe: JUMPI vbbb(0xc2c), vbba

    Begin block 0xbbf
    prev=[0xb6c], succ=[]
    =================================
    0xbbf: vbbf(0x40) = CONST 
    0xbc1: vbc1 = MLOAD vbbf(0x40)
    0xbc2: vbc2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xbe4: MSTORE vbc1, vbc2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xbe5: vbe5(0x4) = CONST 
    0xbe7: vbe7 = ADD vbe5(0x4), vbc1
    0xbea: vbea(0x20) = CONST 
    0xbec: vbec = ADD vbea(0x20), vbe7
    0xbef: vbef(0x20) = SUB vbec, vbe7
    0xbf1: MSTORE vbe7, vbef(0x20)
    0xbf2: vbf2(0x20) = CONST 
    0xbf5: MSTORE vbec, vbf2(0x20)
    0xbf6: vbf6(0x20) = CONST 
    0xbf8: vbf8 = ADD vbf6(0x20), vbec
    0xbfa: vbfa(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xc1c: MSTORE vbf8, vbfa(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xc1e: vc1e(0x20) = CONST 
    0xc20: vc20 = ADD vc1e(0x20), vbf8
    0xc24: vc24(0x40) = CONST 
    0xc26: vc26 = MLOAD vc24(0x40)
    0xc29: vc29(0x64) = SUB vc20, vc26
    0xc2b: REVERT vc26, vc29(0x64)

    Begin block 0xc2c
    prev=[0xb6c], succ=[0xc8b, 0xc94]
    =================================
    0xc2d: vc2d(0x5) = CONST 
    0xc2f: vc2f(0x0) = CONST 
    0xc32: vc32 = SLOAD vc2d(0x5)
    0xc34: vc34(0x100) = CONST 
    0xc37: vc37(0x1) = EXP vc34(0x100), vc2f(0x0)
    0xc39: vc39 = DIV vc32, vc37(0x1)
    0xc3a: vc3a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc4f: vc4f = AND vc3a(0xffffffffffffffffffffffffffffffffffffffff), vc39
    0xc50: vc50(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc65: vc65 = AND vc50(0xffffffffffffffffffffffffffffffffffffffff), vc4f
    0xc66: vc66(0x8fc) = CONST 
    0xc69: vc69 = SELFBALANCE 
    0xc6c: vc6c = ISZERO vc69
    0xc6d: vc6d = MUL vc6c, vc66(0x8fc)
    0xc6f: vc6f(0x40) = CONST 
    0xc71: vc71 = MLOAD vc6f(0x40)
    0xc72: vc72(0x0) = CONST 
    0xc74: vc74(0x40) = CONST 
    0xc76: vc76 = MLOAD vc74(0x40)
    0xc79: vc79(0x0) = SUB vc71, vc76
    0xc7e: vc7e = CALL vc6d, vc65, vc69, vc76, vc79(0x0), vc76, vc72(0x0)
    0xc84: vc84 = ISZERO vc7e
    0xc86: vc86 = ISZERO vc84
    0xc87: vc87(0xc94) = CONST 
    0xc8a: JUMPI vc87(0xc94), vc86

    Begin block 0xc8b
    prev=[0xc2c], succ=[]
    =================================
    0xc8b: vc8b = RETURNDATASIZE 
    0xc8c: vc8c(0x0) = CONST 
    0xc8f: RETURNDATACOPY vc8c(0x0), vc8c(0x0), vc8b
    0xc90: vc90 = RETURNDATASIZE 
    0xc91: vc91(0x0) = CONST 
    0xc93: REVERT vc91(0x0), vc90

    Begin block 0xc94
    prev=[0xc2c], succ=[0xd7b, 0xd7f]
    =================================
    0xc96: vc96(0x1) = CONST 
    0xc98: vc98(0x0) = CONST 
    0xc9b: vc9b = SLOAD vc96(0x1)
    0xc9d: vc9d(0x100) = CONST 
    0xca0: vca0(0x1) = EXP vc9d(0x100), vc98(0x0)
    0xca2: vca2 = DIV vc9b, vca0(0x1)
    0xca3: vca3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcb8: vcb8 = AND vca3(0xffffffffffffffffffffffffffffffffffffffff), vca2
    0xcb9: vcb9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcce: vcce = AND vcb9(0xffffffffffffffffffffffffffffffffffffffff), vcb8
    0xccf: vccf(0xa9059cbb) = CONST 
    0xcd4: vcd4(0x5) = CONST 
    0xcd6: vcd6(0x0) = CONST 
    0xcd9: vcd9 = SLOAD vcd4(0x5)
    0xcdb: vcdb(0x100) = CONST 
    0xcde: vcde(0x1) = EXP vcdb(0x100), vcd6(0x0)
    0xce0: vce0 = DIV vcd9, vcde(0x1)
    0xce1: vce1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcf6: vcf6 = AND vce1(0xffffffffffffffffffffffffffffffffffffffff), vce0
    0xcf7: vcf7(0x1) = CONST 
    0xcf9: vcf9(0x0) = CONST 
    0xcfc: vcfc = SLOAD vcf7(0x1)
    0xcfe: vcfe(0x100) = CONST 
    0xd01: vd01(0x1) = EXP vcfe(0x100), vcf9(0x0)
    0xd03: vd03 = DIV vcfc, vd01(0x1)
    0xd04: vd04(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd19: vd19 = AND vd04(0xffffffffffffffffffffffffffffffffffffffff), vd03
    0xd1a: vd1a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd2f: vd2f = AND vd1a(0xffffffffffffffffffffffffffffffffffffffff), vd19
    0xd30: vd30(0x70a08231) = CONST 
    0xd35: vd35 = ADDRESS 
    0xd36: vd36(0x40) = CONST 
    0xd38: vd38 = MLOAD vd36(0x40)
    0xd3a: vd3a(0xffffffff) = CONST 
    0xd3f: vd3f(0x70a08231) = AND vd3a(0xffffffff), vd30(0x70a08231)
    0xd40: vd40(0xe0) = CONST 
    0xd42: vd42(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL vd40(0xe0), vd3f(0x70a08231)
    0xd44: MSTORE vd38, vd42(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0xd45: vd45(0x4) = CONST 
    0xd47: vd47 = ADD vd45(0x4), vd38
    0xd4a: vd4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd5f: vd5f = AND vd4a(0xffffffffffffffffffffffffffffffffffffffff), vd35
    0xd61: MSTORE vd47, vd5f
    0xd62: vd62(0x20) = CONST 
    0xd64: vd64 = ADD vd62(0x20), vd47
    0xd68: vd68(0x20) = CONST 
    0xd6a: vd6a(0x40) = CONST 
    0xd6c: vd6c = MLOAD vd6a(0x40)
    0xd6f: vd6f(0x24) = SUB vd64, vd6c
    0xd73: vd73 = EXTCODESIZE vd2f
    0xd74: vd74 = ISZERO vd73
    0xd76: vd76 = ISZERO vd74
    0xd77: vd77(0xd7f) = CONST 
    0xd7a: JUMPI vd77(0xd7f), vd76

    Begin block 0xd7b
    prev=[0xc94], succ=[]
    =================================
    0xd7b: vd7b(0x0) = CONST 
    0xd7e: REVERT vd7b(0x0), vd7b(0x0)

    Begin block 0xd7f
    prev=[0xc94], succ=[0xd8a, 0xd93]
    =================================
    0xd81: vd81 = GAS 
    0xd82: vd82 = STATICCALL vd81, vd2f, vd6c, vd6f(0x24), vd6c, vd68(0x20)
    0xd83: vd83 = ISZERO vd82
    0xd85: vd85 = ISZERO vd83
    0xd86: vd86(0xd93) = CONST 
    0xd89: JUMPI vd86(0xd93), vd85

    Begin block 0xd8a
    prev=[0xd7f], succ=[]
    =================================
    0xd8a: vd8a = RETURNDATASIZE 
    0xd8b: vd8b(0x0) = CONST 
    0xd8e: RETURNDATACOPY vd8b(0x0), vd8b(0x0), vd8a
    0xd8f: vd8f = RETURNDATASIZE 
    0xd90: vd90(0x0) = CONST 
    0xd92: REVERT vd90(0x0), vd8f

    Begin block 0xd93
    prev=[0xd7f], succ=[0xda5, 0xda9]
    =================================
    0xd98: vd98(0x40) = CONST 
    0xd9a: vd9a = MLOAD vd98(0x40)
    0xd9b: vd9b = RETURNDATASIZE 
    0xd9c: vd9c(0x20) = CONST 
    0xd9f: vd9f = LT vd9b, vd9c(0x20)
    0xda0: vda0 = ISZERO vd9f
    0xda1: vda1(0xda9) = CONST 
    0xda4: JUMPI vda1(0xda9), vda0

    Begin block 0xda5
    prev=[0xd93], succ=[]
    =================================
    0xda5: vda5(0x0) = CONST 
    0xda8: REVERT vda5(0x0), vda5(0x0)

    Begin block 0xda9
    prev=[0xd93], succ=[0xe09, 0xe0d]
    =================================
    0xdab: vdab = ADD vd9a, vd9b
    0xdaf: vdaf = MLOAD vd9a
    0xdb1: vdb1(0x20) = CONST 
    0xdb3: vdb3 = ADD vdb1(0x20), vd9a
    0xdbb: vdbb(0x40) = CONST 
    0xdbd: vdbd = MLOAD vdbb(0x40)
    0xdbf: vdbf(0xffffffff) = CONST 
    0xdc4: vdc4(0xa9059cbb) = AND vdbf(0xffffffff), vccf(0xa9059cbb)
    0xdc5: vdc5(0xe0) = CONST 
    0xdc7: vdc7(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL vdc5(0xe0), vdc4(0xa9059cbb)
    0xdc9: MSTORE vdbd, vdc7(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0xdca: vdca(0x4) = CONST 
    0xdcc: vdcc = ADD vdca(0x4), vdbd
    0xdcf: vdcf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xde4: vde4 = AND vdcf(0xffffffffffffffffffffffffffffffffffffffff), vcf6
    0xde6: MSTORE vdcc, vde4
    0xde7: vde7(0x20) = CONST 
    0xde9: vde9 = ADD vde7(0x20), vdcc
    0xdec: MSTORE vde9, vdaf
    0xded: vded(0x20) = CONST 
    0xdef: vdef = ADD vded(0x20), vde9
    0xdf4: vdf4(0x20) = CONST 
    0xdf6: vdf6(0x40) = CONST 
    0xdf8: vdf8 = MLOAD vdf6(0x40)
    0xdfb: vdfb(0x44) = SUB vdef, vdf8
    0xdfd: vdfd(0x0) = CONST 
    0xe01: ve01 = EXTCODESIZE vcce
    0xe02: ve02 = ISZERO ve01
    0xe04: ve04 = ISZERO ve02
    0xe05: ve05(0xe0d) = CONST 
    0xe08: JUMPI ve05(0xe0d), ve04

    Begin block 0xe09
    prev=[0xda9], succ=[]
    =================================
    0xe09: ve09(0x0) = CONST 
    0xe0c: REVERT ve09(0x0), ve09(0x0)

    Begin block 0xe0d
    prev=[0xda9], succ=[0xe18, 0xe21]
    =================================
    0xe0f: ve0f = GAS 
    0xe10: ve10 = CALL ve0f, vcce, vdfd(0x0), vdf8, vdfb(0x44), vdf8, vdf4(0x20)
    0xe11: ve11 = ISZERO ve10
    0xe13: ve13 = ISZERO ve11
    0xe14: ve14(0xe21) = CONST 
    0xe17: JUMPI ve14(0xe21), ve13

    Begin block 0xe18
    prev=[0xe0d], succ=[]
    =================================
    0xe18: ve18 = RETURNDATASIZE 
    0xe19: ve19(0x0) = CONST 
    0xe1c: RETURNDATACOPY ve19(0x0), ve19(0x0), ve18
    0xe1d: ve1d = RETURNDATASIZE 
    0xe1e: ve1e(0x0) = CONST 
    0xe20: REVERT ve1e(0x0), ve1d

    Begin block 0xe21
    prev=[0xe0d], succ=[0xe33, 0xe37]
    =================================
    0xe26: ve26(0x40) = CONST 
    0xe28: ve28 = MLOAD ve26(0x40)
    0xe29: ve29 = RETURNDATASIZE 
    0xe2a: ve2a(0x20) = CONST 
    0xe2d: ve2d = LT ve29, ve2a(0x20)
    0xe2e: ve2e = ISZERO ve2d
    0xe2f: ve2f(0xe37) = CONST 
    0xe32: JUMPI ve2f(0xe37), ve2e

    Begin block 0xe33
    prev=[0xe21], succ=[]
    =================================
    0xe33: ve33(0x0) = CONST 
    0xe36: REVERT ve33(0x0), ve33(0x0)

    Begin block 0xe37
    prev=[0xe21], succ=[0x194]
    =================================
    0xe39: ve39 = ADD ve28, ve29
    0xe3d: ve3d = MLOAD ve28
    0xe3f: ve3f(0x20) = CONST 
    0xe41: ve41 = ADD ve3f(0x20), ve28
    0xe4a: JUMP v18d(0x194)

    Begin block 0x194
    prev=[0xe37], succ=[]
    =================================
    0x195: STOP 

}

function owner()() public {
    Begin block 0x196
    prev=[], succ=[0x19e, 0x1a2]
    =================================
    0x197: v197 = CALLVALUE 
    0x199: v199 = ISZERO v197
    0x19a: v19a(0x1a2) = CONST 
    0x19d: JUMPI v19a(0x1a2), v199

    Begin block 0x19e
    prev=[0x196], succ=[]
    =================================
    0x19e: v19e(0x0) = CONST 
    0x1a1: REVERT v19e(0x0), v19e(0x0)

    Begin block 0x1a2
    prev=[0x196], succ=[0xe4b]
    =================================
    0x1a4: v1a4(0x1ab) = CONST 
    0x1a7: v1a7(0xe4b) = CONST 
    0x1aa: JUMP v1a7(0xe4b)

    Begin block 0xe4b
    prev=[0x1a2], succ=[0x1ab]
    =================================
    0xe4c: ve4c(0x0) = CONST 
    0xe4f: ve4f(0x0) = CONST 
    0xe52: ve52 = SLOAD ve4c(0x0)
    0xe54: ve54(0x100) = CONST 
    0xe57: ve57(0x1) = EXP ve54(0x100), ve4f(0x0)
    0xe59: ve59 = DIV ve52, ve57(0x1)
    0xe5a: ve5a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe6f: ve6f = AND ve5a(0xffffffffffffffffffffffffffffffffffffffff), ve59
    0xe73: JUMP v1a4(0x1ab)

    Begin block 0x1ab
    prev=[0xe4b], succ=[]
    =================================
    0x1ac: v1ac(0x40) = CONST 
    0x1ae: v1ae = MLOAD v1ac(0x40)
    0x1b1: v1b1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c6: v1c6 = AND v1b1(0xffffffffffffffffffffffffffffffffffffffff), ve6f
    0x1c8: MSTORE v1ae, v1c6
    0x1c9: v1c9(0x20) = CONST 
    0x1cb: v1cb = ADD v1c9(0x20), v1ae
    0x1cf: v1cf(0x40) = CONST 
    0x1d1: v1d1 = MLOAD v1cf(0x40)
    0x1d4: v1d4(0x20) = SUB v1cb, v1d1
    0x1d6: RETURN v1d1, v1d4(0x20)

}

function WETH()() public {
    Begin block 0x1d7
    prev=[], succ=[0x1df, 0x1e3]
    =================================
    0x1d8: v1d8 = CALLVALUE 
    0x1da: v1da = ISZERO v1d8
    0x1db: v1db(0x1e3) = CONST 
    0x1de: JUMPI v1db(0x1e3), v1da

    Begin block 0x1df
    prev=[0x1d7], succ=[]
    =================================
    0x1df: v1df(0x0) = CONST 
    0x1e2: REVERT v1df(0x0), v1df(0x0)

    Begin block 0x1e3
    prev=[0x1d7], succ=[0xe74]
    =================================
    0x1e5: v1e5(0x1ec) = CONST 
    0x1e8: v1e8(0xe74) = CONST 
    0x1eb: JUMP v1e8(0xe74)

    Begin block 0xe74
    prev=[0x1e3], succ=[0x1ec]
    =================================
    0xe75: ve75(0x4) = CONST 
    0xe77: ve77(0x0) = CONST 
    0xe7a: ve7a = SLOAD ve75(0x4)
    0xe7c: ve7c(0x100) = CONST 
    0xe7f: ve7f(0x1) = EXP ve7c(0x100), ve77(0x0)
    0xe81: ve81 = DIV ve7a, ve7f(0x1)
    0xe82: ve82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe97: ve97 = AND ve82(0xffffffffffffffffffffffffffffffffffffffff), ve81
    0xe99: JUMP v1e5(0x1ec)

    Begin block 0x1ec
    prev=[0xe74], succ=[]
    =================================
    0x1ed: v1ed(0x40) = CONST 
    0x1ef: v1ef = MLOAD v1ed(0x40)
    0x1f2: v1f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x207: v207 = AND v1f2(0xffffffffffffffffffffffffffffffffffffffff), ve97
    0x209: MSTORE v1ef, v207
    0x20a: v20a(0x20) = CONST 
    0x20c: v20c = ADD v20a(0x20), v1ef
    0x210: v210(0x40) = CONST 
    0x212: v212 = MLOAD v210(0x40)
    0x215: v215(0x20) = SUB v20c, v212
    0x217: RETURN v212, v215(0x20)

}

function 0xeeeeeeee() public {
    Begin block 0x1dda4
    prev=[], succ=[]
    =================================
    0x90: STOP 

}

function transferOwnership(address)() public {
    Begin block 0x218
    prev=[], succ=[0x220, 0x224]
    =================================
    0x219: v219 = CALLVALUE 
    0x21b: v21b = ISZERO v219
    0x21c: v21c(0x224) = CONST 
    0x21f: JUMPI v21c(0x224), v21b

    Begin block 0x220
    prev=[0x218], succ=[]
    =================================
    0x220: v220(0x0) = CONST 
    0x223: REVERT v220(0x0), v220(0x0)

    Begin block 0x224
    prev=[0x218], succ=[0x237, 0x23b]
    =================================
    0x226: v226(0x267) = CONST 
    0x229: v229(0x4) = CONST 
    0x22c: v22c = CALLDATASIZE 
    0x22d: v22d = SUB v22c, v229(0x4)
    0x22e: v22e(0x20) = CONST 
    0x231: v231 = LT v22d, v22e(0x20)
    0x232: v232 = ISZERO v231
    0x233: v233(0x23b) = CONST 
    0x236: JUMPI v233(0x23b), v232

    Begin block 0x237
    prev=[0x224], succ=[]
    =================================
    0x237: v237(0x0) = CONST 
    0x23a: REVERT v237(0x0), v237(0x0)

    Begin block 0x23b
    prev=[0x224], succ=[0xe9a]
    =================================
    0x23d: v23d = ADD v229(0x4), v22d
    0x241: v241 = CALLDATALOAD v229(0x4)
    0x242: v242(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x257: v257 = AND v242(0xffffffffffffffffffffffffffffffffffffffff), v241
    0x259: v259(0x20) = CONST 
    0x25b: v25b(0x24) = ADD v259(0x20), v229(0x4)
    0x263: v263(0xe9a) = CONST 
    0x266: JUMP v263(0xe9a)

    Begin block 0xe9a
    prev=[0x23b], succ=[0x119bB0xe9a]
    =================================
    0xe9b: ve9b(0xea2) = CONST 
    0xe9e: ve9e(0x119b) = CONST 
    0xea1: JUMP ve9e(0x119b)

    Begin block 0x119bB0xe9a
    prev=[0xe9a], succ=[0xea2]
    =================================
    0x119cS0xe9a: v119cVe9a(0x0) = CONST 
    0x119eS0xe9a: v119eVe9a = CALLER 
    0x11a2S0xe9a: JUMP ve9b(0xea2)

    Begin block 0xea2
    prev=[0x119bB0xe9a], succ=[0xef5, 0xf62]
    =================================
    0xea3: vea3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeb8: veb8 = AND vea3(0xffffffffffffffffffffffffffffffffffffffff), v119eVe9a
    0xeb9: veb9(0x0) = CONST 
    0xebc: vebc = SLOAD veb9(0x0)
    0xebe: vebe(0x100) = CONST 
    0xec1: vec1(0x1) = EXP vebe(0x100), veb9(0x0)
    0xec3: vec3 = DIV vebc, vec1(0x1)
    0xec4: vec4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xed9: ved9 = AND vec4(0xffffffffffffffffffffffffffffffffffffffff), vec3
    0xeda: veda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeef: veef = AND veda(0xffffffffffffffffffffffffffffffffffffffff), ved9
    0xef0: vef0 = EQ veef, veb8
    0xef1: vef1(0xf62) = CONST 
    0xef4: JUMPI vef1(0xf62), vef0

    Begin block 0xef5
    prev=[0xea2], succ=[]
    =================================
    0xef5: vef5(0x40) = CONST 
    0xef7: vef7 = MLOAD vef5(0x40)
    0xef8: vef8(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf1a: MSTORE vef7, vef8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf1b: vf1b(0x4) = CONST 
    0xf1d: vf1d = ADD vf1b(0x4), vef7
    0xf20: vf20(0x20) = CONST 
    0xf22: vf22 = ADD vf20(0x20), vf1d
    0xf25: vf25(0x20) = SUB vf22, vf1d
    0xf27: MSTORE vf1d, vf25(0x20)
    0xf28: vf28(0x20) = CONST 
    0xf2b: MSTORE vf22, vf28(0x20)
    0xf2c: vf2c(0x20) = CONST 
    0xf2e: vf2e = ADD vf2c(0x20), vf22
    0xf30: vf30(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xf52: MSTORE vf2e, vf30(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xf54: vf54(0x20) = CONST 
    0xf56: vf56 = ADD vf54(0x20), vf2e
    0xf5a: vf5a(0x40) = CONST 
    0xf5c: vf5c = MLOAD vf5a(0x40)
    0xf5f: vf5f(0x64) = SUB vf56, vf5c
    0xf61: REVERT vf5c, vf5f(0x64)

    Begin block 0xf62
    prev=[0xea2], succ=[0xf98, 0xfe8]
    =================================
    0xf63: vf63(0x0) = CONST 
    0xf65: vf65(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf7a: vf7a(0x0) = AND vf65(0xffffffffffffffffffffffffffffffffffffffff), vf63(0x0)
    0xf7c: vf7c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf91: vf91 = AND vf7c(0xffffffffffffffffffffffffffffffffffffffff), v257
    0xf92: vf92 = EQ vf91, vf7a(0x0)
    0xf93: vf93 = ISZERO vf92
    0xf94: vf94(0xfe8) = CONST 
    0xf97: JUMPI vf94(0xfe8), vf93

    Begin block 0xf98
    prev=[0xf62], succ=[]
    =================================
    0xf98: vf98(0x40) = CONST 
    0xf9a: vf9a = MLOAD vf98(0x40)
    0xf9b: vf9b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xfbd: MSTORE vf9a, vf9b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xfbe: vfbe(0x4) = CONST 
    0xfc0: vfc0 = ADD vfbe(0x4), vf9a
    0xfc3: vfc3(0x20) = CONST 
    0xfc5: vfc5 = ADD vfc3(0x20), vfc0
    0xfc8: vfc8(0x20) = SUB vfc5, vfc0
    0xfca: MSTORE vfc0, vfc8(0x20)
    0xfcb: vfcb(0x26) = CONST 
    0xfce: MSTORE vfc5, vfcb(0x26)
    0xfcf: vfcf(0x20) = CONST 
    0xfd1: vfd1 = ADD vfcf(0x20), vfc5
    0xfd3: vfd3(0x126a) = CONST 
    0xfd6: vfd6(0x26) = CONST 
    0xfd9: CODECOPY vfd1, vfd3(0x126a), vfd6(0x26)
    0xfda: vfda(0x40) = CONST 
    0xfdc: vfdc = ADD vfda(0x40), vfd1
    0xfe0: vfe0(0x40) = CONST 
    0xfe2: vfe2 = MLOAD vfe0(0x40)
    0xfe5: vfe5(0x84) = SUB vfdc, vfe2
    0xfe7: REVERT vfe2, vfe5(0x84)

    Begin block 0xfe8
    prev=[0xf62], succ=[0x267]
    =================================
    0xfea: vfea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfff: vfff = AND vfea(0xffffffffffffffffffffffffffffffffffffffff), v257
    0x1000: v1000(0x0) = CONST 
    0x1003: v1003 = SLOAD v1000(0x0)
    0x1005: v1005(0x100) = CONST 
    0x1008: v1008(0x1) = EXP v1005(0x100), v1000(0x0)
    0x100a: v100a = DIV v1003, v1008(0x1)
    0x100b: v100b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1020: v1020 = AND v100b(0xffffffffffffffffffffffffffffffffffffffff), v100a
    0x1021: v1021(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1036: v1036 = AND v1021(0xffffffffffffffffffffffffffffffffffffffff), v1020
    0x1037: v1037(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1058: v1058(0x40) = CONST 
    0x105a: v105a = MLOAD v1058(0x40)
    0x105b: v105b(0x40) = CONST 
    0x105d: v105d = MLOAD v105b(0x40)
    0x1060: v1060(0x0) = SUB v105a, v105d
    0x1062: LOG3 v105d, v1060(0x0), v1037(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1036, vfff
    0x1064: v1064(0x0) = CONST 
    0x1067: v1067(0x100) = CONST 
    0x106a: v106a(0x1) = EXP v1067(0x100), v1064(0x0)
    0x106c: v106c = SLOAD v1064(0x0)
    0x106e: v106e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1083: v1083(0xffffffffffffffffffffffffffffffffffffffff) = MUL v106e(0xffffffffffffffffffffffffffffffffffffffff), v106a(0x1)
    0x1084: v1084(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1083(0xffffffffffffffffffffffffffffffffffffffff)
    0x1085: v1085 = AND v1084(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v106c
    0x1088: v1088(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x109d: v109d = AND v1088(0xffffffffffffffffffffffffffffffffffffffff), v257
    0x109e: v109e = MUL v109d, v106a(0x1)
    0x109f: v109f = OR v109e, v1085
    0x10a1: SSTORE v1064(0x0), v109f
    0x10a4: JUMP v226(0x267)

    Begin block 0x267
    prev=[0xfe8], succ=[]
    =================================
    0x268: STOP 

}

function paper()() public {
    Begin block 0x269
    prev=[], succ=[0x271, 0x275]
    =================================
    0x26a: v26a = CALLVALUE 
    0x26c: v26c = ISZERO v26a
    0x26d: v26d(0x275) = CONST 
    0x270: JUMPI v26d(0x275), v26c

    Begin block 0x271
    prev=[0x269], succ=[]
    =================================
    0x271: v271(0x0) = CONST 
    0x274: REVERT v271(0x0), v271(0x0)

    Begin block 0x275
    prev=[0x269], succ=[0x10a5]
    =================================
    0x277: v277(0x27e) = CONST 
    0x27a: v27a(0x10a5) = CONST 
    0x27d: JUMP v27a(0x10a5)

    Begin block 0x10a5
    prev=[0x275], succ=[0x27e]
    =================================
    0x10a6: v10a6(0x1) = CONST 
    0x10a8: v10a8(0x0) = CONST 
    0x10ab: v10ab = SLOAD v10a6(0x1)
    0x10ad: v10ad(0x100) = CONST 
    0x10b0: v10b0(0x1) = EXP v10ad(0x100), v10a8(0x0)
    0x10b2: v10b2 = DIV v10ab, v10b0(0x1)
    0x10b3: v10b3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10c8: v10c8 = AND v10b3(0xffffffffffffffffffffffffffffffffffffffff), v10b2
    0x10ca: JUMP v277(0x27e)

    Begin block 0x27e
    prev=[0x10a5], succ=[]
    =================================
    0x27f: v27f(0x40) = CONST 
    0x281: v281 = MLOAD v27f(0x40)
    0x284: v284(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x299: v299 = AND v284(0xffffffffffffffffffffffffffffffffffffffff), v10c8
    0x29b: MSTORE v281, v299
    0x29c: v29c(0x20) = CONST 
    0x29e: v29e = ADD v29c(0x20), v281
    0x2a2: v2a2(0x40) = CONST 
    0x2a4: v2a4 = MLOAD v2a2(0x40)
    0x2a7: v2a7(0x20) = SUB v29e, v2a4
    0x2a9: RETURN v2a4, v2a7(0x20)

}

function 0x2aa(v2aaarg0, v2aaarg1) private {
    Begin block 0x2aa
    prev=[], succ=[0x35a, 0x35e]
    =================================
    0x2ab: v2ab(0x0) = CONST 
    0x2ad: v2ad(0x49b) = CONST 
    0x2b1: v2b1(0x48d) = CONST 
    0x2b4: v2b4(0x4) = CONST 
    0x2b6: v2b6(0x0) = CONST 
    0x2b9: v2b9 = SLOAD v2b4(0x4)
    0x2bb: v2bb(0x100) = CONST 
    0x2be: v2be(0x1) = EXP v2bb(0x100), v2b6(0x0)
    0x2c0: v2c0 = DIV v2b9, v2be(0x1)
    0x2c1: v2c1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d6: v2d6 = AND v2c1(0xffffffffffffffffffffffffffffffffffffffff), v2c0
    0x2d7: v2d7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ec: v2ec = AND v2d7(0xffffffffffffffffffffffffffffffffffffffff), v2d6
    0x2ed: v2ed(0x70a08231) = CONST 
    0x2f2: v2f2(0x2) = CONST 
    0x2f4: v2f4(0x0) = CONST 
    0x2f7: v2f7 = SLOAD v2f2(0x2)
    0x2f9: v2f9(0x100) = CONST 
    0x2fc: v2fc(0x1) = EXP v2f9(0x100), v2f4(0x0)
    0x2fe: v2fe = DIV v2f7, v2fc(0x1)
    0x2ff: v2ff(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x314: v314 = AND v2ff(0xffffffffffffffffffffffffffffffffffffffff), v2fe
    0x315: v315(0x40) = CONST 
    0x317: v317 = MLOAD v315(0x40)
    0x319: v319(0xffffffff) = CONST 
    0x31e: v31e(0x70a08231) = AND v319(0xffffffff), v2ed(0x70a08231)
    0x31f: v31f(0xe0) = CONST 
    0x321: v321(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v31f(0xe0), v31e(0x70a08231)
    0x323: MSTORE v317, v321(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x324: v324(0x4) = CONST 
    0x326: v326 = ADD v324(0x4), v317
    0x329: v329(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33e: v33e = AND v329(0xffffffffffffffffffffffffffffffffffffffff), v314
    0x340: MSTORE v326, v33e
    0x341: v341(0x20) = CONST 
    0x343: v343 = ADD v341(0x20), v326
    0x347: v347(0x20) = CONST 
    0x349: v349(0x40) = CONST 
    0x34b: v34b = MLOAD v349(0x40)
    0x34e: v34e(0x24) = SUB v343, v34b
    0x352: v352 = EXTCODESIZE v2ec
    0x353: v353 = ISZERO v352
    0x355: v355 = ISZERO v353
    0x356: v356(0x35e) = CONST 
    0x359: JUMPI v356(0x35e), v355

    Begin block 0x35a
    prev=[0x2aa], succ=[]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35d: REVERT v35a(0x0), v35a(0x0)

    Begin block 0x35e
    prev=[0x2aa], succ=[0x369, 0x372]
    =================================
    0x360: v360 = GAS 
    0x361: v361 = STATICCALL v360, v2ec, v34b, v34e(0x24), v34b, v347(0x20)
    0x362: v362 = ISZERO v361
    0x364: v364 = ISZERO v362
    0x365: v365(0x372) = CONST 
    0x368: JUMPI v365(0x372), v364

    Begin block 0x369
    prev=[0x35e], succ=[]
    =================================
    0x369: v369 = RETURNDATASIZE 
    0x36a: v36a(0x0) = CONST 
    0x36d: RETURNDATACOPY v36a(0x0), v36a(0x0), v369
    0x36e: v36e = RETURNDATASIZE 
    0x36f: v36f(0x0) = CONST 
    0x371: REVERT v36f(0x0), v36e

    Begin block 0x372
    prev=[0x35e], succ=[0x384, 0x388]
    =================================
    0x377: v377(0x40) = CONST 
    0x379: v379 = MLOAD v377(0x40)
    0x37a: v37a = RETURNDATASIZE 
    0x37b: v37b(0x20) = CONST 
    0x37e: v37e = LT v37a, v37b(0x20)
    0x37f: v37f = ISZERO v37e
    0x380: v380(0x388) = CONST 
    0x383: JUMPI v380(0x388), v37f

    Begin block 0x384
    prev=[0x372], succ=[]
    =================================
    0x384: v384(0x0) = CONST 
    0x387: REVERT v384(0x0), v384(0x0)

    Begin block 0x388
    prev=[0x372], succ=[0x440, 0x444]
    =================================
    0x38a: v38a = ADD v379, v37a
    0x38e: v38e = MLOAD v379
    0x390: v390(0x20) = CONST 
    0x392: v392 = ADD v390(0x20), v379
    0x39a: v39a(0x1) = CONST 
    0x39c: v39c(0x0) = CONST 
    0x39f: v39f = SLOAD v39a(0x1)
    0x3a1: v3a1(0x100) = CONST 
    0x3a4: v3a4(0x1) = EXP v3a1(0x100), v39c(0x0)
    0x3a6: v3a6 = DIV v39f, v3a4(0x1)
    0x3a7: v3a7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3bc: v3bc = AND v3a7(0xffffffffffffffffffffffffffffffffffffffff), v3a6
    0x3bd: v3bd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3d2: v3d2 = AND v3bd(0xffffffffffffffffffffffffffffffffffffffff), v3bc
    0x3d3: v3d3(0x70a08231) = CONST 
    0x3d8: v3d8(0x2) = CONST 
    0x3da: v3da(0x0) = CONST 
    0x3dd: v3dd = SLOAD v3d8(0x2)
    0x3df: v3df(0x100) = CONST 
    0x3e2: v3e2(0x1) = EXP v3df(0x100), v3da(0x0)
    0x3e4: v3e4 = DIV v3dd, v3e2(0x1)
    0x3e5: v3e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3fa: v3fa = AND v3e5(0xffffffffffffffffffffffffffffffffffffffff), v3e4
    0x3fb: v3fb(0x40) = CONST 
    0x3fd: v3fd = MLOAD v3fb(0x40)
    0x3ff: v3ff(0xffffffff) = CONST 
    0x404: v404(0x70a08231) = AND v3ff(0xffffffff), v3d3(0x70a08231)
    0x405: v405(0xe0) = CONST 
    0x407: v407(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v405(0xe0), v404(0x70a08231)
    0x409: MSTORE v3fd, v407(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x40a: v40a(0x4) = CONST 
    0x40c: v40c = ADD v40a(0x4), v3fd
    0x40f: v40f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x424: v424 = AND v40f(0xffffffffffffffffffffffffffffffffffffffff), v3fa
    0x426: MSTORE v40c, v424
    0x427: v427(0x20) = CONST 
    0x429: v429 = ADD v427(0x20), v40c
    0x42d: v42d(0x20) = CONST 
    0x42f: v42f(0x40) = CONST 
    0x431: v431 = MLOAD v42f(0x40)
    0x434: v434(0x24) = SUB v429, v431
    0x438: v438 = EXTCODESIZE v3d2
    0x439: v439 = ISZERO v438
    0x43b: v43b = ISZERO v439
    0x43c: v43c(0x444) = CONST 
    0x43f: JUMPI v43c(0x444), v43b

    Begin block 0x440
    prev=[0x388], succ=[]
    =================================
    0x440: v440(0x0) = CONST 
    0x443: REVERT v440(0x0), v440(0x0)

    Begin block 0x444
    prev=[0x388], succ=[0x44f, 0x458]
    =================================
    0x446: v446 = GAS 
    0x447: v447 = STATICCALL v446, v3d2, v431, v434(0x24), v431, v42d(0x20)
    0x448: v448 = ISZERO v447
    0x44a: v44a = ISZERO v448
    0x44b: v44b(0x458) = CONST 
    0x44e: JUMPI v44b(0x458), v44a

    Begin block 0x44f
    prev=[0x444], succ=[]
    =================================
    0x44f: v44f = RETURNDATASIZE 
    0x450: v450(0x0) = CONST 
    0x453: RETURNDATACOPY v450(0x0), v450(0x0), v44f
    0x454: v454 = RETURNDATASIZE 
    0x455: v455(0x0) = CONST 
    0x457: REVERT v455(0x0), v454

    Begin block 0x458
    prev=[0x444], succ=[0x46a, 0x46e]
    =================================
    0x45d: v45d(0x40) = CONST 
    0x45f: v45f = MLOAD v45d(0x40)
    0x460: v460 = RETURNDATASIZE 
    0x461: v461(0x20) = CONST 
    0x464: v464 = LT v460, v461(0x20)
    0x465: v465 = ISZERO v464
    0x466: v466(0x46e) = CONST 
    0x469: JUMPI v466(0x46e), v465

    Begin block 0x46a
    prev=[0x458], succ=[]
    =================================
    0x46a: v46a(0x0) = CONST 
    0x46d: REVERT v46a(0x0), v46a(0x0)

    Begin block 0x46e
    prev=[0x458], succ=[0x10cb0x2aa]
    =================================
    0x470: v470 = ADD v45f, v460
    0x474: v474 = MLOAD v45f
    0x476: v476(0x20) = CONST 
    0x478: v478 = ADD v476(0x20), v45f
    0x480: v480(0x10cb) = CONST 
    0x486: v486(0xffffffff) = CONST 
    0x48b: v48b(0x10cb) = AND v486(0xffffffff), v480(0x10cb)
    0x48c: JUMP v48b(0x10cb)

    Begin block 0x10cb0x2aa
    prev=[0x46e], succ=[0x11a30x2aa]
    =================================
    0x10cc0x2aa: v2aa10cc(0x0) = CONST 
    0x10ce0x2aa: v2aa10ce(0x110d) = CONST 
    0x10d30x2aa: v2aa10d3(0x40) = CONST 
    0x10d50x2aa: v2aa10d5 = MLOAD v2aa10d3(0x40)
    0x10d70x2aa: v2aa10d7(0x40) = CONST 
    0x10d90x2aa: v2aa10d9 = ADD v2aa10d7(0x40), v2aa10d5
    0x10da0x2aa: v2aa10da(0x40) = CONST 
    0x10dc0x2aa: MSTORE v2aa10da(0x40), v2aa10d9
    0x10de0x2aa: v2aa10de(0x1a) = CONST 
    0x10e10x2aa: MSTORE v2aa10d5, v2aa10de(0x1a)
    0x10e20x2aa: v2aa10e2(0x20) = CONST 
    0x10e40x2aa: v2aa10e4 = ADD v2aa10e2(0x20), v2aa10d5
    0x10e50x2aa: v2aa10e5(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x11070x2aa: MSTORE v2aa10e4, v2aa10e5(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x11090x2aa: v2aa1109(0x11a3) = CONST 
    0x110c0x2aa: JUMP v2aa1109(0x11a3)

    Begin block 0x11a30x2aa
    prev=[0x10cb0x2aa], succ=[0x11af0x2aa, 0x124f0x2aa]
    =================================
    0x11a40x2aa: v2aa11a4(0x0) = CONST 
    0x11a80x2aa: v2aa11a8 = GT v38e, v2aa11a4(0x0)
    0x11ab0x2aa: v2aa11ab(0x124f) = CONST 
    0x11ae0x2aa: JUMPI v2aa11ab(0x124f), v2aa11a8

    Begin block 0x11af0x2aa
    prev=[0x11a30x2aa], succ=[0x11f90x2aa]
    =================================
    0x11af0x2aa: v2aa11af(0x40) = CONST 
    0x11b10x2aa: v2aa11b1 = MLOAD v2aa11af(0x40)
    0x11b20x2aa: v2aa11b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11d40x2aa: MSTORE v2aa11b1, v2aa11b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11d50x2aa: v2aa11d5(0x4) = CONST 
    0x11d70x2aa: v2aa11d7 = ADD v2aa11d5(0x4), v2aa11b1
    0x11da0x2aa: v2aa11da(0x20) = CONST 
    0x11dc0x2aa: v2aa11dc = ADD v2aa11da(0x20), v2aa11d7
    0x11df0x2aa: v2aa11df(0x20) = SUB v2aa11dc, v2aa11d7
    0x11e10x2aa: MSTORE v2aa11d7, v2aa11df(0x20)
    0x11e50x2aa: v2aa11e5(0x1a) = MLOAD v2aa10d5
    0x11e70x2aa: MSTORE v2aa11dc, v2aa11e5(0x1a)
    0x11e80x2aa: v2aa11e8(0x20) = CONST 
    0x11ea0x2aa: v2aa11ea = ADD v2aa11e8(0x20), v2aa11dc
    0x11ee0x2aa: v2aa11ee(0x1a) = MLOAD v2aa10d5
    0x11f00x2aa: v2aa11f0(0x20) = CONST 
    0x11f20x2aa: v2aa11f2 = ADD v2aa11f0(0x20), v2aa10d5
    0x11f70x2aa: v2aa11f7(0x0) = CONST 
    0x568c0x2aa: v2aa568c(0x11f9) = CONST 
    0x56ac0x2aa: JUMP v2aa568c(0x11f9)

    Begin block 0x11f90x2aa
    prev=[0x11af0x2aa, 0x12020x2aa], succ=[0x12140x2aa, 0x12020x2aa]
    =================================
    0x11f90x2aa_0x0: v11f92aa_0 = PHI v2aa120d, v2aa11f7(0x0)
    0x11fc0x2aa: v2aa11fc = LT v11f92aa_0, v2aa11ee(0x1a)
    0x11fd0x2aa: v2aa11fd = ISZERO v2aa11fc
    0x11fe0x2aa: v2aa11fe(0x1214) = CONST 
    0x12010x2aa: JUMPI v2aa11fe(0x1214), v2aa11fd

    Begin block 0x12140x2aa
    prev=[0x11f90x2aa], succ=[0x12280x2aa, 0x12410x2aa]
    =================================
    0x121d0x2aa: v2aa121d = ADD v2aa11ee(0x1a), v2aa11ea
    0x121f0x2aa: v2aa121f(0x1f) = CONST 
    0x12210x2aa: v2aa1221(0x1a) = AND v2aa121f(0x1f), v2aa11ee(0x1a)
    0x12230x2aa: v2aa1223(0x0) = ISZERO v2aa1221(0x1a)
    0x12240x2aa: v2aa1224(0x1241) = CONST 
    0x12270x2aa: JUMPI v2aa1224(0x1241), v2aa1223(0x0)

    Begin block 0x12280x2aa
    prev=[0x12140x2aa], succ=[0x12410x2aa]
    =================================
    0x122a0x2aa: v2aa122a = SUB v2aa121d, v2aa1221(0x1a)
    0x122c0x2aa: v2aa122c = MLOAD v2aa122a
    0x122d0x2aa: v2aa122d(0x1) = CONST 
    0x12300x2aa: v2aa1230(0x20) = CONST 
    0x12320x2aa: v2aa1232(0x6) = SUB v2aa1230(0x20), v2aa1221(0x1a)
    0x12330x2aa: v2aa1233(0x100) = CONST 
    0x12360x2aa: v2aa1236(0x1000000000000) = EXP v2aa1233(0x100), v2aa1232(0x6)
    0x12370x2aa: v2aa1237(0xffffffffffff) = SUB v2aa1236(0x1000000000000), v2aa122d(0x1)
    0x12380x2aa: v2aa1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffff000000000000) = NOT v2aa1237(0xffffffffffff)
    0x12390x2aa: v2aa1239 = AND v2aa1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffff000000000000), v2aa122c
    0x123b0x2aa: MSTORE v2aa122a, v2aa1239
    0x123c0x2aa: v2aa123c(0x20) = CONST 
    0x123e0x2aa: v2aa123e = ADD v2aa123c(0x20), v2aa122a
    0x608c0x2aa: v2aa608c(0x1241) = CONST 
    0x60ac0x2aa: JUMP v2aa608c(0x1241)

    Begin block 0x12410x2aa
    prev=[0x12280x2aa, 0x12140x2aa], succ=[]
    =================================
    0x12410x2aa_0x1: v12412aa_1 = PHI v2aa123e, v2aa121d
    0x12470x2aa: v2aa1247(0x40) = CONST 
    0x12490x2aa: v2aa1249 = MLOAD v2aa1247(0x40)
    0x124c0x2aa: v2aa124c = SUB v12412aa_1, v2aa1249
    0x124e0x2aa: REVERT v2aa1249, v2aa124c

    Begin block 0x12020x2aa
    prev=[0x11f90x2aa], succ=[0x11f90x2aa]
    =================================
    0x12020x2aa_0x0: v12022aa_0 = PHI v2aa120d, v2aa11f7(0x0)
    0x12040x2aa: v2aa1204 = ADD v2aa11f2, v12022aa_0
    0x12050x2aa: v2aa1205 = MLOAD v2aa1204
    0x12080x2aa: v2aa1208 = ADD v2aa11ea, v12022aa_0
    0x12090x2aa: MSTORE v2aa1208, v2aa1205
    0x120a0x2aa: v2aa120a(0x20) = CONST 
    0x120d0x2aa: v2aa120d = ADD v12022aa_0, v2aa120a(0x20)
    0x12100x2aa: v2aa1210(0x11f9) = CONST 
    0x12130x2aa: JUMP v2aa1210(0x11f9)

    Begin block 0x124f0x2aa
    prev=[0x11a30x2aa], succ=[0x125a0x2aa, 0x125b0x2aa]
    =================================
    0x12510x2aa: v2aa1251(0x0) = CONST 
    0x12560x2aa: v2aa1256(0x125b) = CONST 
    0x12590x2aa: JUMPI v2aa1256(0x125b), v38e

    Begin block 0x125a0x2aa
    prev=[0x124f0x2aa], succ=[]
    =================================
    0x125a0x2aa: THROW 

    Begin block 0x125b0x2aa
    prev=[0x124f0x2aa], succ=[0x110d0x2aa]
    =================================
    0x125c0x2aa: v2aa125c = DIV v474, v38e
    0x12680x2aa: JUMP v2aa10ce(0x110d)

    Begin block 0x110d0x2aa
    prev=[0x125b0x2aa], succ=[0x48d]
    =================================
    0x11140x2aa: JUMP v2b1(0x48d)

    Begin block 0x48d
    prev=[0x110d0x2aa], succ=[0x11150x2aa]
    =================================
    0x48e: v48e(0x1115) = CONST 
    0x494: v494(0xffffffff) = CONST 
    0x499: v499(0x1115) = AND v494(0xffffffff), v48e(0x1115)
    0x49a: JUMP v499(0x1115)

    Begin block 0x11150x2aa
    prev=[0x48d], succ=[0x11200x2aa, 0x11280x2aa]
    =================================
    0x11160x2aa: v2aa1116(0x0) = CONST 
    0x111a0x2aa: v2aa111a = EQ v2aa125c, v2aa1116(0x0)
    0x111b0x2aa: v2aa111b = ISZERO v2aa111a
    0x111c0x2aa: v2aa111c(0x1128) = CONST 
    0x111f0x2aa: JUMPI v2aa111c(0x1128), v2aa111b

    Begin block 0x11200x2aa
    prev=[0x11150x2aa], succ=[0xc1780x2aa]
    =================================
    0x11200x2aa: v2aa1120(0x0) = CONST 
    0x11240x2aa: v2aa1124(0xc178) = CONST 
    0x11270x2aa: JUMP v2aa1124(0xc178)

    Begin block 0xc1780x2aa
    prev=[0x11200x2aa], succ=[0x49b]
    =================================
    0xc17d0x2aa: JUMP v2ad(0x49b)

    Begin block 0x49b
    prev=[0xc1780x2aa, 0xc19d0x2aa], succ=[]
    =================================
    0x49b_0x0: v49b_0 = PHI v2aa112d, v2aa1120(0x0)
    0x4a1: RETURNPRIVATE v2aaarg1, v49b_0

    Begin block 0x11280x2aa
    prev=[0x11150x2aa], succ=[0x11380x2aa, 0x11390x2aa]
    =================================
    0x11290x2aa: v2aa1129(0x0) = CONST 
    0x112d0x2aa: v2aa112d = MUL v2aa125c, v2aaarg0
    0x11340x2aa: v2aa1134(0x1139) = CONST 
    0x11370x2aa: JUMPI v2aa1134(0x1139), v2aa125c

    Begin block 0x11380x2aa
    prev=[0x11280x2aa], succ=[]
    =================================
    0x11380x2aa: THROW 

    Begin block 0x11390x2aa
    prev=[0x11280x2aa], succ=[0x11400x2aa, 0x11900x2aa]
    =================================
    0x113a0x2aa: v2aa113a = DIV v2aa112d, v2aa125c
    0x113b0x2aa: v2aa113b = EQ v2aa113a, v2aaarg0
    0x113c0x2aa: v2aa113c(0x1190) = CONST 
    0x113f0x2aa: JUMPI v2aa113c(0x1190), v2aa113b

    Begin block 0x11400x2aa
    prev=[0x11390x2aa], succ=[]
    =================================
    0x11400x2aa: v2aa1140(0x40) = CONST 
    0x11420x2aa: v2aa1142 = MLOAD v2aa1140(0x40)
    0x11430x2aa: v2aa1143(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11650x2aa: MSTORE v2aa1142, v2aa1143(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11660x2aa: v2aa1166(0x4) = CONST 
    0x11680x2aa: v2aa1168 = ADD v2aa1166(0x4), v2aa1142
    0x116b0x2aa: v2aa116b(0x20) = CONST 
    0x116d0x2aa: v2aa116d = ADD v2aa116b(0x20), v2aa1168
    0x11700x2aa: v2aa1170(0x20) = SUB v2aa116d, v2aa1168
    0x11720x2aa: MSTORE v2aa1168, v2aa1170(0x20)
    0x11730x2aa: v2aa1173(0x21) = CONST 
    0x11760x2aa: MSTORE v2aa116d, v2aa1173(0x21)
    0x11770x2aa: v2aa1177(0x20) = CONST 
    0x11790x2aa: v2aa1179 = ADD v2aa1177(0x20), v2aa116d
    0x117b0x2aa: v2aa117b(0x1290) = CONST 
    0x117e0x2aa: v2aa117e(0x21) = CONST 
    0x11810x2aa: CODECOPY v2aa1179, v2aa117b(0x1290), v2aa117e(0x21)
    0x11820x2aa: v2aa1182(0x40) = CONST 
    0x11840x2aa: v2aa1184 = ADD v2aa1182(0x40), v2aa1179
    0x11880x2aa: v2aa1188(0x40) = CONST 
    0x118a0x2aa: v2aa118a = MLOAD v2aa1188(0x40)
    0x118d0x2aa: v2aa118d(0x84) = SUB v2aa1184, v2aa118a
    0x118f0x2aa: REVERT v2aa118a, v2aa118d(0x84)

    Begin block 0x11900x2aa
    prev=[0x11390x2aa], succ=[0xc19d0x2aa]
    =================================
    0x4c8c0x2aa: v2aa4c8c(0xc19d) = CONST 
    0x4cac0x2aa: JUMP v2aa4c8c(0xc19d)

    Begin block 0xc19d0x2aa
    prev=[0x11900x2aa], succ=[0x49b]
    =================================
    0xc1a20x2aa: JUMP v2ad(0x49b)

}

function getPaperAmount(uint256)() public {
    Begin block 0x96
    prev=[], succ=[0x9e, 0xa2]
    =================================
    0x97: v97 = CALLVALUE 
    0x99: v99 = ISZERO v97
    0x9a: v9a(0xa2) = CONST 
    0x9d: JUMPI v9a(0xa2), v99

    Begin block 0x9e
    prev=[0x96], succ=[]
    =================================
    0x9e: v9e(0x0) = CONST 
    0xa1: REVERT v9e(0x0), v9e(0x0)

    Begin block 0xa2
    prev=[0x96], succ=[0xb5, 0xb9]
    =================================
    0xa4: va4(0xcf) = CONST 
    0xa7: va7(0x4) = CONST 
    0xaa: vaa = CALLDATASIZE 
    0xab: vab = SUB vaa, va7(0x4)
    0xac: vac(0x20) = CONST 
    0xaf: vaf = LT vab, vac(0x20)
    0xb0: vb0 = ISZERO vaf
    0xb1: vb1(0xb9) = CONST 
    0xb4: JUMPI vb1(0xb9), vb0

    Begin block 0xb5
    prev=[0xa2], succ=[]
    =================================
    0xb5: vb5(0x0) = CONST 
    0xb8: REVERT vb5(0x0), vb5(0x0)

    Begin block 0xb9
    prev=[0xa2], succ=[0xcf]
    =================================
    0xbb: vbb = ADD va7(0x4), vab
    0xbf: vbf = CALLDATALOAD va7(0x4)
    0xc1: vc1(0x20) = CONST 
    0xc3: vc3(0x24) = ADD vc1(0x20), va7(0x4)
    0xcb: vcb(0x2aa) = CONST 
    0xce: vce_0 = CALLPRIVATE vcb(0x2aa), vbf, va4(0xcf)

    Begin block 0xcf
    prev=[0xb9], succ=[]
    =================================
    0xd0: vd0(0x40) = CONST 
    0xd2: vd2 = MLOAD vd0(0x40)
    0xd6: MSTORE vd2, vce_0
    0xd7: vd7(0x20) = CONST 
    0xd9: vd9 = ADD vd7(0x20), vd2
    0xdd: vdd(0x40) = CONST 
    0xdf: vdf = MLOAD vdd(0x40)
    0xe2: ve2(0x20) = SUB vd9, vdf
    0xe4: RETURN vdf, ve2(0x20)

}

function developers()() public {
    Begin block 0xe5
    prev=[], succ=[0xed, 0xf1]
    =================================
    0xe6: ve6 = CALLVALUE 
    0xe8: ve8 = ISZERO ve6
    0xe9: ve9(0xf1) = CONST 
    0xec: JUMPI ve9(0xf1), ve8

    Begin block 0xed
    prev=[0xe5], succ=[]
    =================================
    0xed: ved(0x0) = CONST 
    0xf0: REVERT ved(0x0), ved(0x0)

    Begin block 0xf1
    prev=[0xe5], succ=[0x4a2]
    =================================
    0xf3: vf3(0xfa) = CONST 
    0xf6: vf6(0x4a2) = CONST 
    0xf9: JUMP vf6(0x4a2)

    Begin block 0x4a2
    prev=[0xf1], succ=[0xfa]
    =================================
    0x4a3: v4a3(0x5) = CONST 
    0x4a5: v4a5(0x0) = CONST 
    0x4a8: v4a8 = SLOAD v4a3(0x5)
    0x4aa: v4aa(0x100) = CONST 
    0x4ad: v4ad(0x1) = EXP v4aa(0x100), v4a5(0x0)
    0x4af: v4af = DIV v4a8, v4ad(0x1)
    0x4b0: v4b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4c5: v4c5 = AND v4b0(0xffffffffffffffffffffffffffffffffffffffff), v4af
    0x4c7: JUMP vf3(0xfa)

    Begin block 0xfa
    prev=[0x4a2], succ=[]
    =================================
    0xfb: vfb(0x40) = CONST 
    0xfd: vfd = MLOAD vfb(0x40)
    0x100: v100(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x115: v115 = AND v100(0xffffffffffffffffffffffffffffffffffffffff), v4c5
    0x117: MSTORE vfd, v115
    0x118: v118(0x20) = CONST 
    0x11a: v11a = ADD v118(0x20), vfd
    0x11e: v11e(0x40) = CONST 
    0x120: v120 = MLOAD v11e(0x40)
    0x123: v123(0x20) = SUB v11a, v120
    0x125: RETURN v120, v123(0x20)

}

