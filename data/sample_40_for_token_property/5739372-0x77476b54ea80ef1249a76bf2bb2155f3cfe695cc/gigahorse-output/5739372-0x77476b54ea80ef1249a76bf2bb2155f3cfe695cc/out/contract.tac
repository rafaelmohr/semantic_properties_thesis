function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x19310]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xc110: vc110(0x19310) = CONST 
    0xc130: JUMPI vc110(0x19310), v8

    Begin block 0xd
    prev=[0x0], succ=[0x19d10, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x5d2035b) = CONST 
    0x3c: v3c = EQ v37(0x5d2035b), v35
    0xcb10: vcb10(0x19d10) = CONST 
    0xcb30: JUMPI vcb10(0x19d10), v3c

    Begin block 0x19d10
    prev=[0xd], succ=[]
    =================================
    0x19d30: v19d30(0x117) = CONST 
    0x19d50: CALLPRIVATE v19d30(0x117)

    Begin block 0x41
    prev=[0xd], succ=[0x1a710, 0x4c]
    =================================
    0x42: v42(0x6fdde03) = CONST 
    0x47: v47 = EQ v42(0x6fdde03), v35
    0xd510: vd510(0x1a710) = CONST 
    0xd530: JUMPI vd510(0x1a710), v47

    Begin block 0x1a710
    prev=[0x41], succ=[]
    =================================
    0x1a730: v1a730(0x144) = CONST 
    0x1a750: CALLPRIVATE v1a730(0x144)

    Begin block 0x4c
    prev=[0x41], succ=[0x1b110, 0x57]
    =================================
    0x4d: v4d(0x95ea7b3) = CONST 
    0x52: v52 = EQ v4d(0x95ea7b3), v35
    0xdf10: vdf10(0x1b110) = CONST 
    0xdf30: JUMPI vdf10(0x1b110), v52

    Begin block 0x1b110
    prev=[0x4c], succ=[]
    =================================
    0x1b130: v1b130(0x1d2) = CONST 
    0x1b150: CALLPRIVATE v1b130(0x1d2)

    Begin block 0x57
    prev=[0x4c], succ=[0x1bb10, 0x62]
    =================================
    0x58: v58(0x18160ddd) = CONST 
    0x5d: v5d = EQ v58(0x18160ddd), v35
    0xe910: ve910(0x1bb10) = CONST 
    0xe930: JUMPI ve910(0x1bb10), v5d

    Begin block 0x1bb10
    prev=[0x57], succ=[]
    =================================
    0x1bb30: v1bb30(0x22c) = CONST 
    0x1bb50: CALLPRIVATE v1bb30(0x22c)

    Begin block 0x62
    prev=[0x57], succ=[0x1c510, 0x6d]
    =================================
    0x63: v63(0x23b872dd) = CONST 
    0x68: v68 = EQ v63(0x23b872dd), v35
    0xf310: vf310(0x1c510) = CONST 
    0xf330: JUMPI vf310(0x1c510), v68

    Begin block 0x1c510
    prev=[0x62], succ=[]
    =================================
    0x1c530: v1c530(0x255) = CONST 
    0x1c550: CALLPRIVATE v1c530(0x255)

    Begin block 0x6d
    prev=[0x62], succ=[0x1cf10, 0x78]
    =================================
    0x6e: v6e(0x313ce567) = CONST 
    0x73: v73 = EQ v6e(0x313ce567), v35
    0xfd10: vfd10(0x1cf10) = CONST 
    0xfd30: JUMPI vfd10(0x1cf10), v73

    Begin block 0x1cf10
    prev=[0x6d], succ=[]
    =================================
    0x1cf30: v1cf30(0x2ce) = CONST 
    0x1cf50: CALLPRIVATE v1cf30(0x2ce)

    Begin block 0x78
    prev=[0x6d], succ=[0x1d910, 0x83]
    =================================
    0x79: v79(0x3f4ba83a) = CONST 
    0x7e: v7e = EQ v79(0x3f4ba83a), v35
    0x10710: v10710(0x1d910) = CONST 
    0x10730: JUMPI v10710(0x1d910), v7e

    Begin block 0x1d910
    prev=[0x78], succ=[]
    =================================
    0x1d930: v1d930(0x2fd) = CONST 
    0x1d950: CALLPRIVATE v1d930(0x2fd)

    Begin block 0x83
    prev=[0x78], succ=[0x1e310, 0x8e]
    =================================
    0x84: v84(0x40c10f19) = CONST 
    0x89: v89 = EQ v84(0x40c10f19), v35
    0x11110: v11110(0x1e310) = CONST 
    0x11130: JUMPI v11110(0x1e310), v89

    Begin block 0x1e310
    prev=[0x83], succ=[]
    =================================
    0x1e330: v1e330(0x312) = CONST 
    0x1e350: CALLPRIVATE v1e330(0x312)

    Begin block 0x8e
    prev=[0x83], succ=[0x1ed10, 0x99]
    =================================
    0x8f: v8f(0x42966c68) = CONST 
    0x94: v94 = EQ v8f(0x42966c68), v35
    0x11b10: v11b10(0x1ed10) = CONST 
    0x11b30: JUMPI v11b10(0x1ed10), v94

    Begin block 0x1ed10
    prev=[0x8e], succ=[]
    =================================
    0x1ed30: v1ed30(0x36c) = CONST 
    0x1ed50: CALLPRIVATE v1ed30(0x36c)

    Begin block 0x99
    prev=[0x8e], succ=[0x1f710, 0xa4]
    =================================
    0x9a: v9a(0x5c975abb) = CONST 
    0x9f: v9f = EQ v9a(0x5c975abb), v35
    0x12510: v12510(0x1f710) = CONST 
    0x12530: JUMPI v12510(0x1f710), v9f

    Begin block 0x1f710
    prev=[0x99], succ=[]
    =================================
    0x1f730: v1f730(0x38f) = CONST 
    0x1f750: CALLPRIVATE v1f730(0x38f)

    Begin block 0xa4
    prev=[0x99], succ=[0x20110, 0xaf]
    =================================
    0xa5: va5(0x66188463) = CONST 
    0xaa: vaa = EQ va5(0x66188463), v35
    0x12f10: v12f10(0x20110) = CONST 
    0x12f30: JUMPI v12f10(0x20110), vaa

    Begin block 0x20110
    prev=[0xa4], succ=[]
    =================================
    0x20130: v20130(0x3bc) = CONST 
    0x20150: CALLPRIVATE v20130(0x3bc)

    Begin block 0xaf
    prev=[0xa4], succ=[0x20b10, 0xba]
    =================================
    0xb0: vb0(0x70a08231) = CONST 
    0xb5: vb5 = EQ vb0(0x70a08231), v35
    0x13910: v13910(0x20b10) = CONST 
    0x13930: JUMPI v13910(0x20b10), vb5

    Begin block 0x20b10
    prev=[0xaf], succ=[]
    =================================
    0x20b30: v20b30(0x416) = CONST 
    0x20b50: CALLPRIVATE v20b30(0x416)

    Begin block 0xba
    prev=[0xaf], succ=[0x21510, 0xc5]
    =================================
    0xbb: vbb(0x7d64bcb4) = CONST 
    0xc0: vc0 = EQ vbb(0x7d64bcb4), v35
    0x14310: v14310(0x21510) = CONST 
    0x14330: JUMPI v14310(0x21510), vc0

    Begin block 0x21510
    prev=[0xba], succ=[]
    =================================
    0x21530: v21530(0x463) = CONST 
    0x21550: CALLPRIVATE v21530(0x463)

    Begin block 0xc5
    prev=[0xba], succ=[0x21f10, 0xd0]
    =================================
    0xc6: vc6(0x8456cb59) = CONST 
    0xcb: vcb = EQ vc6(0x8456cb59), v35
    0x14d10: v14d10(0x21f10) = CONST 
    0x14d30: JUMPI v14d10(0x21f10), vcb

    Begin block 0x21f10
    prev=[0xc5], succ=[]
    =================================
    0x21f30: v21f30(0x490) = CONST 
    0x21f50: CALLPRIVATE v21f30(0x490)

    Begin block 0xd0
    prev=[0xc5], succ=[0x22910, 0xdb]
    =================================
    0xd1: vd1(0x8da5cb5b) = CONST 
    0xd6: vd6 = EQ vd1(0x8da5cb5b), v35
    0x15710: v15710(0x22910) = CONST 
    0x15730: JUMPI v15710(0x22910), vd6

    Begin block 0x22910
    prev=[0xd0], succ=[]
    =================================
    0x22930: v22930(0x4a5) = CONST 
    0x22950: CALLPRIVATE v22930(0x4a5)

    Begin block 0xdb
    prev=[0xd0], succ=[0x23310, 0xe6]
    =================================
    0xdc: vdc(0x95d89b41) = CONST 
    0xe1: ve1 = EQ vdc(0x95d89b41), v35
    0x16110: v16110(0x23310) = CONST 
    0x16130: JUMPI v16110(0x23310), ve1

    Begin block 0x23310
    prev=[0xdb], succ=[]
    =================================
    0x23330: v23330(0x4fa) = CONST 
    0x23350: CALLPRIVATE v23330(0x4fa)

    Begin block 0xe6
    prev=[0xdb], succ=[0x23d10, 0xf1]
    =================================
    0xe7: ve7(0xa9059cbb) = CONST 
    0xec: vec = EQ ve7(0xa9059cbb), v35
    0x16b10: v16b10(0x23d10) = CONST 
    0x16b30: JUMPI v16b10(0x23d10), vec

    Begin block 0x23d10
    prev=[0xe6], succ=[]
    =================================
    0x23d30: v23d30(0x588) = CONST 
    0x23d50: CALLPRIVATE v23d30(0x588)

    Begin block 0xf1
    prev=[0xe6], succ=[0x24710, 0xfc]
    =================================
    0xf2: vf2(0xd73dd623) = CONST 
    0xf7: vf7 = EQ vf2(0xd73dd623), v35
    0x17510: v17510(0x24710) = CONST 
    0x17530: JUMPI v17510(0x24710), vf7

    Begin block 0x24710
    prev=[0xf1], succ=[]
    =================================
    0x24730: v24730(0x5e2) = CONST 
    0x24750: CALLPRIVATE v24730(0x5e2)

    Begin block 0xfc
    prev=[0xf1], succ=[0x25110, 0x107]
    =================================
    0xfd: vfd(0xdd62ed3e) = CONST 
    0x102: v102 = EQ vfd(0xdd62ed3e), v35
    0x17f10: v17f10(0x25110) = CONST 
    0x17f30: JUMPI v17f10(0x25110), v102

    Begin block 0x25110
    prev=[0xfc], succ=[]
    =================================
    0x25130: v25130(0x63c) = CONST 
    0x25150: CALLPRIVATE v25130(0x63c)

    Begin block 0x107
    prev=[0xfc], succ=[0x19310, 0x25b10]
    =================================
    0x108: v108(0xf2fde38b) = CONST 
    0x10d: v10d = EQ v108(0xf2fde38b), v35
    0x18910: v18910(0x25b10) = CONST 
    0x18930: JUMPI v18910(0x25b10), v10d

    Begin block 0x19310
    prev=[0x0, 0x107], succ=[]
    =================================
    0x19330: v19330(0x112) = CONST 
    0x19350: CALLPRIVATE v19330(0x112)

    Begin block 0x25b10
    prev=[0x107], succ=[]
    =================================
    0x25b30: v25b30(0x6a8) = CONST 
    0x25b50: CALLPRIVATE v25b30(0x6a8)

}

function fallback()() public {
    Begin block 0x112
    prev=[], succ=[]
    =================================
    0x113: v113(0x0) = CONST 
    0x116: REVERT v113(0x0), v113(0x0)

}

function mintingFinished()() public {
    Begin block 0x117
    prev=[], succ=[0x11e, 0x122]
    =================================
    0x118: v118 = CALLVALUE 
    0x119: v119 = ISZERO v118
    0x11a: v11a(0x122) = CONST 
    0x11d: JUMPI v11a(0x122), v119

    Begin block 0x11e
    prev=[0x117], succ=[]
    =================================
    0x11e: v11e(0x0) = CONST 
    0x121: REVERT v11e(0x0), v11e(0x0)

    Begin block 0x122
    prev=[0x117], succ=[0x6e1]
    =================================
    0x123: v123(0x12a) = CONST 
    0x126: v126(0x6e1) = CONST 
    0x129: JUMP v126(0x6e1)

    Begin block 0x6e1
    prev=[0x122], succ=[0x12a]
    =================================
    0x6e2: v6e2(0x3) = CONST 
    0x6e4: v6e4(0x15) = CONST 
    0x6e7: v6e7 = SLOAD v6e2(0x3)
    0x6e9: v6e9(0x100) = CONST 
    0x6ec: v6ec(0x1000000000000000000000000000000000000000000) = EXP v6e9(0x100), v6e4(0x15)
    0x6ee: v6ee = DIV v6e7, v6ec(0x1000000000000000000000000000000000000000000)
    0x6ef: v6ef(0xff) = CONST 
    0x6f1: v6f1 = AND v6ef(0xff), v6ee
    0x6f3: JUMP v123(0x12a)

    Begin block 0x12a
    prev=[0x6e1], succ=[]
    =================================
    0x12b: v12b(0x40) = CONST 
    0x12d: v12d = MLOAD v12b(0x40)
    0x130: v130 = ISZERO v6f1
    0x131: v131 = ISZERO v130
    0x132: v132 = ISZERO v131
    0x133: v133 = ISZERO v132
    0x135: MSTORE v12d, v133
    0x136: v136(0x20) = CONST 
    0x138: v138 = ADD v136(0x20), v12d
    0x13c: v13c(0x40) = CONST 
    0x13e: v13e = MLOAD v13c(0x40)
    0x141: v141(0x20) = SUB v138, v13e
    0x143: RETURN v13e, v141(0x20)

}

function name()() public {
    Begin block 0x144
    prev=[], succ=[0x14b, 0x14f]
    =================================
    0x145: v145 = CALLVALUE 
    0x146: v146 = ISZERO v145
    0x147: v147(0x14f) = CONST 
    0x14a: JUMPI v147(0x14f), v146

    Begin block 0x14b
    prev=[0x144], succ=[]
    =================================
    0x14b: v14b(0x0) = CONST 
    0x14e: REVERT v14b(0x0), v14b(0x0)

    Begin block 0x14f
    prev=[0x144], succ=[0x6f4]
    =================================
    0x150: v150(0x157) = CONST 
    0x153: v153(0x6f4) = CONST 
    0x156: JUMP v153(0x6f4)

    Begin block 0x6f4
    prev=[0x14f], succ=[0x157]
    =================================
    0x6f5: v6f5(0x40) = CONST 
    0x6f8: v6f8 = MLOAD v6f5(0x40)
    0x6fb: v6fb = ADD v6f8, v6f5(0x40)
    0x6fc: v6fc(0x40) = CONST 
    0x6fe: MSTORE v6fc(0x40), v6fb
    0x700: v700(0x9) = CONST 
    0x703: MSTORE v6f8, v700(0x9)
    0x704: v704(0x20) = CONST 
    0x706: v706 = ADD v704(0x20), v6f8
    0x707: v707(0x50696c6172436f696e0000000000000000000000000000000000000000000000) = CONST 
    0x729: MSTORE v706, v707(0x50696c6172436f696e0000000000000000000000000000000000000000000000)
    0x72c: JUMP v150(0x157)

    Begin block 0x157
    prev=[0x6f4], succ=[0x17c]
    =================================
    0x158: v158(0x40) = CONST 
    0x15a: v15a = MLOAD v158(0x40)
    0x15d: v15d(0x20) = CONST 
    0x15f: v15f = ADD v15d(0x20), v15a
    0x162: v162(0x20) = SUB v15f, v15a
    0x164: MSTORE v15a, v162(0x20)
    0x168: v168(0x9) = MLOAD v6f8
    0x16a: MSTORE v15f, v168(0x9)
    0x16b: v16b(0x20) = CONST 
    0x16d: v16d = ADD v16b(0x20), v15f
    0x171: v171(0x9) = MLOAD v6f8
    0x173: v173(0x20) = CONST 
    0x175: v175 = ADD v173(0x20), v6f8
    0x17a: v17a(0x0) = CONST 
    0x3858: v3858(0x17c) = CONST 
    0x3878: JUMP v3858(0x17c)

    Begin block 0x17c
    prev=[0x157, 0x185], succ=[0x197, 0x185]
    =================================
    0x17c_0x0: v17c_0 = PHI v17a(0x0), v190
    0x17f: v17f = LT v17c_0, v171(0x9)
    0x180: v180 = ISZERO v17f
    0x181: v181(0x197) = CONST 
    0x184: JUMPI v181(0x197), v180

    Begin block 0x197
    prev=[0x17c], succ=[0x1c4, 0x1ab]
    =================================
    0x1a0: v1a0 = ADD v171(0x9), v16d
    0x1a2: v1a2(0x1f) = CONST 
    0x1a4: v1a4(0x9) = AND v1a2(0x1f), v171(0x9)
    0x1a6: v1a6(0x0) = ISZERO v1a4(0x9)
    0x1a7: v1a7(0x1c4) = CONST 
    0x1aa: JUMPI v1a7(0x1c4), v1a6(0x0)

    Begin block 0x1c4
    prev=[0x197, 0x1ab], succ=[]
    =================================
    0x1c4_0x1: v1c4_1 = PHI v1a0, v1c1
    0x1ca: v1ca(0x40) = CONST 
    0x1cc: v1cc = MLOAD v1ca(0x40)
    0x1cf: v1cf = SUB v1c4_1, v1cc
    0x1d1: RETURN v1cc, v1cf

    Begin block 0x1ab
    prev=[0x197], succ=[0x1c4]
    =================================
    0x1ad: v1ad = SUB v1a0, v1a4(0x9)
    0x1af: v1af = MLOAD v1ad
    0x1b0: v1b0(0x1) = CONST 
    0x1b3: v1b3(0x20) = CONST 
    0x1b5: v1b5(0x17) = SUB v1b3(0x20), v1a4(0x9)
    0x1b6: v1b6(0x100) = CONST 
    0x1b9: v1b9(0x10000000000000000000000000000000000000000000000) = EXP v1b6(0x100), v1b5(0x17)
    0x1ba: v1ba(0xffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1b9(0x10000000000000000000000000000000000000000000000), v1b0(0x1)
    0x1bb: v1bb(0xffffffffffffffffff0000000000000000000000000000000000000000000000) = NOT v1ba(0xffffffffffffffffffffffffffffffffffffffffffffff)
    0x1bc: v1bc = AND v1bb(0xffffffffffffffffff0000000000000000000000000000000000000000000000), v1af
    0x1be: MSTORE v1ad, v1bc
    0x1bf: v1bf(0x20) = CONST 
    0x1c1: v1c1 = ADD v1bf(0x20), v1ad
    0x4258: v4258(0x1c4) = CONST 
    0x4278: JUMP v4258(0x1c4)

    Begin block 0x185
    prev=[0x17c], succ=[0x17c]
    =================================
    0x185_0x0: v185_0 = PHI v17a(0x0), v190
    0x187: v187 = ADD v175, v185_0
    0x188: v188 = MLOAD v187
    0x18b: v18b = ADD v16d, v185_0
    0x18c: MSTORE v18b, v188
    0x18d: v18d(0x20) = CONST 
    0x190: v190 = ADD v185_0, v18d(0x20)
    0x193: v193(0x17c) = CONST 
    0x196: JUMP v193(0x17c)

}

function 0x1509(v1509arg0, v1509arg1, v1509arg2) private {
    Begin block 0x1509
    prev=[], succ=[0x151c, 0x151d]
    =================================
    0x150a: v150a(0x0) = CONST 
    0x150f: v150f = ADD v1509arg1, v1509arg0
    0x1514: v1514 = LT v150f, v1509arg1
    0x1515: v1515 = ISZERO v1514
    0x1516: v1516 = ISZERO v1515
    0x1517: v1517 = ISZERO v1516
    0x1518: v1518(0x151d) = CONST 
    0x151b: JUMPI v1518(0x151d), v1517

    Begin block 0x151c
    prev=[0x1509], succ=[]
    =================================
    0x151c: THROW 

    Begin block 0x151d
    prev=[0x1509], succ=[]
    =================================
    0x1526: RETURNPRIVATE v1509arg2, v150f

}

function 0x1527(v1527arg0, v1527arg1, v1527arg2) private {
    Begin block 0x1527
    prev=[], succ=[0x1534, 0x1535]
    =================================
    0x1528: v1528(0x0) = CONST 
    0x152c: v152c = GT v1527arg0, v1527arg1
    0x152d: v152d = ISZERO v152c
    0x152e: v152e = ISZERO v152d
    0x152f: v152f = ISZERO v152e
    0x1530: v1530(0x1535) = CONST 
    0x1533: JUMPI v1530(0x1535), v152f

    Begin block 0x1534
    prev=[0x1527], succ=[]
    =================================
    0x1534: THROW 

    Begin block 0x1535
    prev=[0x1527], succ=[]
    =================================
    0x1538: v1538 = SUB v1527arg1, v1527arg0
    0x153f: RETURNPRIVATE v1527arg2, v1538

}

function approve(address,uint256)() public {
    Begin block 0x1d2
    prev=[], succ=[0x1d9, 0x1dd]
    =================================
    0x1d3: v1d3 = CALLVALUE 
    0x1d4: v1d4 = ISZERO v1d3
    0x1d5: v1d5(0x1dd) = CONST 
    0x1d8: JUMPI v1d5(0x1dd), v1d4

    Begin block 0x1d9
    prev=[0x1d2], succ=[]
    =================================
    0x1d9: v1d9(0x0) = CONST 
    0x1dc: REVERT v1d9(0x0), v1d9(0x0)

    Begin block 0x1dd
    prev=[0x1d2], succ=[0x72dB0x1dd]
    =================================
    0x1de: v1de(0x212) = CONST 
    0x1e1: v1e1(0x4) = CONST 
    0x1e5: v1e5 = CALLDATALOAD v1e1(0x4)
    0x1e6: v1e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1fb: v1fb = AND v1e6(0xffffffffffffffffffffffffffffffffffffffff), v1e5
    0x1fd: v1fd(0x20) = CONST 
    0x1ff: v1ff(0x24) = ADD v1fd(0x20), v1e1(0x4)
    0x204: v204 = CALLDATALOAD v1ff(0x24)
    0x206: v206(0x20) = CONST 
    0x208: v208(0x44) = ADD v206(0x20), v1ff(0x24)
    0x20e: v20e(0x72d) = CONST 
    0x211: JUMP v20e(0x72d)

    Begin block 0x72dB0x1dd
    prev=[0x1dd], succ=[0x747B0x1dd, 0x74bB0x1dd]
    =================================
    0x72eS0x1dd: v72eV1dd(0x0) = CONST 
    0x730S0x1dd: v730V1dd(0x3) = CONST 
    0x732S0x1dd: v732V1dd(0x14) = CONST 
    0x735S0x1dd: v735V1dd = SLOAD v730V1dd(0x3)
    0x737S0x1dd: v737V1dd(0x100) = CONST 
    0x73aS0x1dd: v73aV1dd(0x10000000000000000000000000000000000000000) = EXP v737V1dd(0x100), v732V1dd(0x14)
    0x73cS0x1dd: v73cV1dd = DIV v735V1dd, v73aV1dd(0x10000000000000000000000000000000000000000)
    0x73dS0x1dd: v73dV1dd(0xff) = CONST 
    0x73fS0x1dd: v73fV1dd = AND v73dV1dd(0xff), v73cV1dd
    0x740S0x1dd: v740V1dd = ISZERO v73fV1dd
    0x741S0x1dd: v741V1dd = ISZERO v740V1dd
    0x742S0x1dd: v742V1dd = ISZERO v741V1dd
    0x743S0x1dd: v743V1dd(0x74b) = CONST 
    0x746S0x1dd: JUMPI v743V1dd(0x74b), v742V1dd

    Begin block 0x747B0x1dd
    prev=[0x72dB0x1dd], succ=[]
    =================================
    0x747S0x1dd: v747V1dd(0x0) = CONST 
    0x74aS0x1dd: REVERT v747V1dd(0x0), v747V1dd(0x0)

    Begin block 0x74bB0x1dd
    prev=[0x72dB0x1dd], succ=[0x1058B0x1dd]
    =================================
    0x74cS0x1dd: v74cV1dd(0x755) = CONST 
    0x751S0x1dd: v751V1dd(0x1058) = CONST 
    0x754S0x1dd: JUMP v751V1dd(0x1058)

    Begin block 0x1058B0x1dd
    prev=[0x74bB0x1dd], succ=[0x755B0x1dd]
    =================================
    0x1059S0x1dd: v1059V1dd(0x0) = CONST 
    0x105cS0x1dd: v105cV1dd(0x2) = CONST 
    0x105eS0x1dd: v105eV1dd(0x0) = CONST 
    0x1060S0x1dd: v1060V1dd = CALLER 
    0x1061S0x1dd: v1061V1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1076S0x1dd: v1076V1dd = AND v1061V1dd(0xffffffffffffffffffffffffffffffffffffffff), v1060V1dd
    0x1077S0x1dd: v1077V1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x108cS0x1dd: v108cV1dd = AND v1077V1dd(0xffffffffffffffffffffffffffffffffffffffff), v1076V1dd
    0x108eS0x1dd: MSTORE v105eV1dd(0x0), v108cV1dd
    0x108fS0x1dd: v108fV1dd(0x20) = CONST 
    0x1091S0x1dd: v1091V1dd(0x20) = ADD v108fV1dd(0x20), v105eV1dd(0x0)
    0x1094S0x1dd: MSTORE v1091V1dd(0x20), v105cV1dd(0x2)
    0x1095S0x1dd: v1095V1dd(0x20) = CONST 
    0x1097S0x1dd: v1097V1dd(0x40) = ADD v1095V1dd(0x20), v1091V1dd(0x20)
    0x1098S0x1dd: v1098V1dd(0x0) = CONST 
    0x109aS0x1dd: v109aV1dd = SHA3 v1098V1dd(0x0), v1097V1dd(0x40)
    0x109bS0x1dd: v109bV1dd(0x0) = CONST 
    0x109eS0x1dd: v109eV1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10b3S0x1dd: v10b3V1dd = AND v109eV1dd(0xffffffffffffffffffffffffffffffffffffffff), v1fb
    0x10b4S0x1dd: v10b4V1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10c9S0x1dd: v10c9V1dd = AND v10b4V1dd(0xffffffffffffffffffffffffffffffffffffffff), v10b3V1dd
    0x10cbS0x1dd: MSTORE v109bV1dd(0x0), v10c9V1dd
    0x10ccS0x1dd: v10ccV1dd(0x20) = CONST 
    0x10ceS0x1dd: v10ceV1dd(0x20) = ADD v10ccV1dd(0x20), v109bV1dd(0x0)
    0x10d1S0x1dd: MSTORE v10ceV1dd(0x20), v109aV1dd
    0x10d2S0x1dd: v10d2V1dd(0x20) = CONST 
    0x10d4S0x1dd: v10d4V1dd(0x40) = ADD v10d2V1dd(0x20), v10ceV1dd(0x20)
    0x10d5S0x1dd: v10d5V1dd(0x0) = CONST 
    0x10d7S0x1dd: v10d7V1dd = SHA3 v10d5V1dd(0x0), v10d4V1dd(0x40)
    0x10daS0x1dd: SSTORE v10d7V1dd, v204
    0x10ddS0x1dd: v10ddV1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10f2S0x1dd: v10f2V1dd = AND v10ddV1dd(0xffffffffffffffffffffffffffffffffffffffff), v1fb
    0x10f3S0x1dd: v10f3V1dd = CALLER 
    0x10f4S0x1dd: v10f4V1dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1109S0x1dd: v1109V1dd = AND v10f4V1dd(0xffffffffffffffffffffffffffffffffffffffff), v10f3V1dd
    0x110aS0x1dd: v110aV1dd(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x112cS0x1dd: v112cV1dd(0x40) = CONST 
    0x112eS0x1dd: v112eV1dd = MLOAD v112cV1dd(0x40)
    0x1132S0x1dd: MSTORE v112eV1dd, v204
    0x1133S0x1dd: v1133V1dd(0x20) = CONST 
    0x1135S0x1dd: v1135V1dd = ADD v1133V1dd(0x20), v112eV1dd
    0x1139S0x1dd: v1139V1dd(0x40) = CONST 
    0x113bS0x1dd: v113bV1dd = MLOAD v1139V1dd(0x40)
    0x113eS0x1dd: v113eV1dd(0x20) = SUB v1135V1dd, v113bV1dd
    0x1140S0x1dd: LOG3 v113bV1dd, v113eV1dd(0x20), v110aV1dd(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v1109V1dd, v10f2V1dd
    0x1141S0x1dd: v1141V1dd(0x1) = CONST 
    0x1149S0x1dd: JUMP v74cV1dd(0x755)

    Begin block 0x755B0x1dd
    prev=[0x1058B0x1dd], succ=[0x212]
    =================================
    0x75cS0x1dd: JUMP v1de(0x212)

    Begin block 0x212
    prev=[0x755B0x1dd], succ=[]
    =================================
    0x213: v213(0x40) = CONST 
    0x215: v215 = MLOAD v213(0x40)
    0x218: v218(0x0) = ISZERO v1141V1dd(0x1)
    0x219: v219(0x1) = ISZERO v218(0x0)
    0x21a: v21a(0x0) = ISZERO v219(0x1)
    0x21b: v21b(0x1) = ISZERO v21a(0x0)
    0x21d: MSTORE v215, v21b(0x1)
    0x21e: v21e(0x20) = CONST 
    0x220: v220 = ADD v21e(0x20), v215
    0x224: v224(0x40) = CONST 
    0x226: v226 = MLOAD v224(0x40)
    0x229: v229(0x20) = SUB v220, v226
    0x22b: RETURN v226, v229(0x20)

}

function totalSupply()() public {
    Begin block 0x22c
    prev=[], succ=[0x233, 0x237]
    =================================
    0x22d: v22d = CALLVALUE 
    0x22e: v22e = ISZERO v22d
    0x22f: v22f(0x237) = CONST 
    0x232: JUMPI v22f(0x237), v22e

    Begin block 0x233
    prev=[0x22c], succ=[]
    =================================
    0x233: v233(0x0) = CONST 
    0x236: REVERT v233(0x0), v233(0x0)

    Begin block 0x237
    prev=[0x22c], succ=[0x75d]
    =================================
    0x238: v238(0x23f) = CONST 
    0x23b: v23b(0x75d) = CONST 
    0x23e: JUMP v23b(0x75d)

    Begin block 0x75d
    prev=[0x237], succ=[0x23f]
    =================================
    0x75e: v75e(0x0) = CONST 
    0x760: v760 = SLOAD v75e(0x0)
    0x762: JUMP v238(0x23f)

    Begin block 0x23f
    prev=[0x75d], succ=[]
    =================================
    0x240: v240(0x40) = CONST 
    0x242: v242 = MLOAD v240(0x40)
    0x246: MSTORE v242, v760
    0x247: v247(0x20) = CONST 
    0x249: v249 = ADD v247(0x20), v242
    0x24d: v24d(0x40) = CONST 
    0x24f: v24f = MLOAD v24d(0x40)
    0x252: v252(0x20) = SUB v249, v24f
    0x254: RETURN v24f, v252(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x255
    prev=[], succ=[0x25c, 0x260]
    =================================
    0x256: v256 = CALLVALUE 
    0x257: v257 = ISZERO v256
    0x258: v258(0x260) = CONST 
    0x25b: JUMPI v258(0x260), v257

    Begin block 0x25c
    prev=[0x255], succ=[]
    =================================
    0x25c: v25c(0x0) = CONST 
    0x25f: REVERT v25c(0x0), v25c(0x0)

    Begin block 0x260
    prev=[0x255], succ=[0x763B0x260]
    =================================
    0x261: v261(0x2b4) = CONST 
    0x264: v264(0x4) = CONST 
    0x268: v268 = CALLDATALOAD v264(0x4)
    0x269: v269(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27e: v27e = AND v269(0xffffffffffffffffffffffffffffffffffffffff), v268
    0x280: v280(0x20) = CONST 
    0x282: v282(0x24) = ADD v280(0x20), v264(0x4)
    0x287: v287 = CALLDATALOAD v282(0x24)
    0x288: v288(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29d: v29d = AND v288(0xffffffffffffffffffffffffffffffffffffffff), v287
    0x29f: v29f(0x20) = CONST 
    0x2a1: v2a1(0x44) = ADD v29f(0x20), v282(0x24)
    0x2a6: v2a6 = CALLDATALOAD v2a1(0x44)
    0x2a8: v2a8(0x20) = CONST 
    0x2aa: v2aa(0x64) = ADD v2a8(0x20), v2a1(0x44)
    0x2b0: v2b0(0x763) = CONST 
    0x2b3: JUMP v2b0(0x763)

    Begin block 0x763B0x260
    prev=[0x260], succ=[0x77dB0x260, 0x781B0x260]
    =================================
    0x764S0x260: v764V260(0x0) = CONST 
    0x766S0x260: v766V260(0x3) = CONST 
    0x768S0x260: v768V260(0x14) = CONST 
    0x76bS0x260: v76bV260 = SLOAD v766V260(0x3)
    0x76dS0x260: v76dV260(0x100) = CONST 
    0x770S0x260: v770V260(0x10000000000000000000000000000000000000000) = EXP v76dV260(0x100), v768V260(0x14)
    0x772S0x260: v772V260 = DIV v76bV260, v770V260(0x10000000000000000000000000000000000000000)
    0x773S0x260: v773V260(0xff) = CONST 
    0x775S0x260: v775V260 = AND v773V260(0xff), v772V260
    0x776S0x260: v776V260 = ISZERO v775V260
    0x777S0x260: v777V260 = ISZERO v776V260
    0x778S0x260: v778V260 = ISZERO v777V260
    0x779S0x260: v779V260(0x781) = CONST 
    0x77cS0x260: JUMPI v779V260(0x781), v778V260

    Begin block 0x77dB0x260
    prev=[0x763B0x260], succ=[]
    =================================
    0x77dS0x260: v77dV260(0x0) = CONST 
    0x780S0x260: REVERT v77dV260(0x0), v77dV260(0x0)

    Begin block 0x781B0x260
    prev=[0x763B0x260], succ=[0x114aB0x260]
    =================================
    0x782S0x260: v782V260(0x78c) = CONST 
    0x788S0x260: v788V260(0x114a) = CONST 
    0x78bS0x260: JUMP v788V260(0x114a)

    Begin block 0x114aB0x260
    prev=[0x781B0x260], succ=[0x1183B0x260, 0x1187B0x260]
    =================================
    0x114bS0x260: v114bV260(0x0) = CONST 
    0x114eS0x260: v114eV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1163S0x260: v1163V260(0x0) = AND v114eV260(0xffffffffffffffffffffffffffffffffffffffff), v114bV260(0x0)
    0x1165S0x260: v1165V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x117aS0x260: v117aV260 = AND v1165V260(0xffffffffffffffffffffffffffffffffffffffff), v29d
    0x117bS0x260: v117bV260 = EQ v117aV260, v1163V260(0x0)
    0x117cS0x260: v117cV260 = ISZERO v117bV260
    0x117dS0x260: v117dV260 = ISZERO v117cV260
    0x117eS0x260: v117eV260 = ISZERO v117dV260
    0x117fS0x260: v117fV260(0x1187) = CONST 
    0x1182S0x260: JUMPI v117fV260(0x1187), v117eV260

    Begin block 0x1183B0x260
    prev=[0x114aB0x260], succ=[]
    =================================
    0x1183S0x260: v1183V260(0x0) = CONST 
    0x1186S0x260: REVERT v1183V260(0x0), v1183V260(0x0)

    Begin block 0x1187B0x260
    prev=[0x114aB0x260], succ=[0x11d1B0x260, 0x11d5B0x260]
    =================================
    0x1188S0x260: v1188V260(0x1) = CONST 
    0x118aS0x260: v118aV260(0x0) = CONST 
    0x118dS0x260: v118dV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11a2S0x260: v11a2V260 = AND v118dV260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x11a3S0x260: v11a3V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11b8S0x260: v11b8V260 = AND v11a3V260(0xffffffffffffffffffffffffffffffffffffffff), v11a2V260
    0x11baS0x260: MSTORE v118aV260(0x0), v11b8V260
    0x11bbS0x260: v11bbV260(0x20) = CONST 
    0x11bdS0x260: v11bdV260(0x20) = ADD v11bbV260(0x20), v118aV260(0x0)
    0x11c0S0x260: MSTORE v11bdV260(0x20), v1188V260(0x1)
    0x11c1S0x260: v11c1V260(0x20) = CONST 
    0x11c3S0x260: v11c3V260(0x40) = ADD v11c1V260(0x20), v11bdV260(0x20)
    0x11c4S0x260: v11c4V260(0x0) = CONST 
    0x11c6S0x260: v11c6V260 = SHA3 v11c4V260(0x0), v11c3V260(0x40)
    0x11c7S0x260: v11c7V260 = SLOAD v11c6V260
    0x11c9S0x260: v11c9V260 = GT v2a6, v11c7V260
    0x11caS0x260: v11caV260 = ISZERO v11c9V260
    0x11cbS0x260: v11cbV260 = ISZERO v11caV260
    0x11ccS0x260: v11ccV260 = ISZERO v11cbV260
    0x11cdS0x260: v11cdV260(0x11d5) = CONST 
    0x11d0S0x260: JUMPI v11cdV260(0x11d5), v11ccV260

    Begin block 0x11d1B0x260
    prev=[0x1187B0x260], succ=[]
    =================================
    0x11d1S0x260: v11d1V260(0x0) = CONST 
    0x11d4S0x260: REVERT v11d1V260(0x0), v11d1V260(0x0)

    Begin block 0x11d5B0x260
    prev=[0x1187B0x260], succ=[0x125cB0x260, 0x1260B0x260]
    =================================
    0x11d6S0x260: v11d6V260(0x2) = CONST 
    0x11d8S0x260: v11d8V260(0x0) = CONST 
    0x11dbS0x260: v11dbV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11f0S0x260: v11f0V260 = AND v11dbV260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x11f1S0x260: v11f1V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1206S0x260: v1206V260 = AND v11f1V260(0xffffffffffffffffffffffffffffffffffffffff), v11f0V260
    0x1208S0x260: MSTORE v11d8V260(0x0), v1206V260
    0x1209S0x260: v1209V260(0x20) = CONST 
    0x120bS0x260: v120bV260(0x20) = ADD v1209V260(0x20), v11d8V260(0x0)
    0x120eS0x260: MSTORE v120bV260(0x20), v11d6V260(0x2)
    0x120fS0x260: v120fV260(0x20) = CONST 
    0x1211S0x260: v1211V260(0x40) = ADD v120fV260(0x20), v120bV260(0x20)
    0x1212S0x260: v1212V260(0x0) = CONST 
    0x1214S0x260: v1214V260 = SHA3 v1212V260(0x0), v1211V260(0x40)
    0x1215S0x260: v1215V260(0x0) = CONST 
    0x1217S0x260: v1217V260 = CALLER 
    0x1218S0x260: v1218V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x122dS0x260: v122dV260 = AND v1218V260(0xffffffffffffffffffffffffffffffffffffffff), v1217V260
    0x122eS0x260: v122eV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1243S0x260: v1243V260 = AND v122eV260(0xffffffffffffffffffffffffffffffffffffffff), v122dV260
    0x1245S0x260: MSTORE v1215V260(0x0), v1243V260
    0x1246S0x260: v1246V260(0x20) = CONST 
    0x1248S0x260: v1248V260(0x20) = ADD v1246V260(0x20), v1215V260(0x0)
    0x124bS0x260: MSTORE v1248V260(0x20), v1214V260
    0x124cS0x260: v124cV260(0x20) = CONST 
    0x124eS0x260: v124eV260(0x40) = ADD v124cV260(0x20), v1248V260(0x20)
    0x124fS0x260: v124fV260(0x0) = CONST 
    0x1251S0x260: v1251V260 = SHA3 v124fV260(0x0), v124eV260(0x40)
    0x1252S0x260: v1252V260 = SLOAD v1251V260
    0x1254S0x260: v1254V260 = GT v2a6, v1252V260
    0x1255S0x260: v1255V260 = ISZERO v1254V260
    0x1256S0x260: v1256V260 = ISZERO v1255V260
    0x1257S0x260: v1257V260 = ISZERO v1256V260
    0x1258S0x260: v1258V260(0x1260) = CONST 
    0x125bS0x260: JUMPI v1258V260(0x1260), v1257V260

    Begin block 0x125cB0x260
    prev=[0x11d5B0x260], succ=[]
    =================================
    0x125cS0x260: v125cV260(0x0) = CONST 
    0x125fS0x260: REVERT v125cV260(0x0), v125cV260(0x0)

    Begin block 0x1260B0x260
    prev=[0x11d5B0x260], succ=[0x12b2B0x260]
    =================================
    0x1261S0x260: v1261V260(0x12b2) = CONST 
    0x1265S0x260: v1265V260(0x1) = CONST 
    0x1267S0x260: v1267V260(0x0) = CONST 
    0x126aS0x260: v126aV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x127fS0x260: v127fV260 = AND v126aV260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x1280S0x260: v1280V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1295S0x260: v1295V260 = AND v1280V260(0xffffffffffffffffffffffffffffffffffffffff), v127fV260
    0x1297S0x260: MSTORE v1267V260(0x0), v1295V260
    0x1298S0x260: v1298V260(0x20) = CONST 
    0x129aS0x260: v129aV260(0x20) = ADD v1298V260(0x20), v1267V260(0x0)
    0x129dS0x260: MSTORE v129aV260(0x20), v1265V260(0x1)
    0x129eS0x260: v129eV260(0x20) = CONST 
    0x12a0S0x260: v12a0V260(0x40) = ADD v129eV260(0x20), v129aV260(0x20)
    0x12a1S0x260: v12a1V260(0x0) = CONST 
    0x12a3S0x260: v12a3V260 = SHA3 v12a1V260(0x0), v12a0V260(0x40)
    0x12a4S0x260: v12a4V260 = SLOAD v12a3V260
    0x12a5S0x260: v12a5V260(0x1527) = CONST 
    0x12abS0x260: v12abV260(0xffffffff) = CONST 
    0x12b0S0x260: v12b0V260(0x1527) = AND v12abV260(0xffffffff), v12a5V260(0x1527)
    0x12b1S0x260: v12b1_0V260 = CALLPRIVATE v12b0V260(0x1527), v2a6, v12a4V260, v1261V260(0x12b2)

    Begin block 0x12b2B0x260
    prev=[0x1260B0x260], succ=[0x1347B0x260]
    =================================
    0x12b3S0x260: v12b3V260(0x1) = CONST 
    0x12b5S0x260: v12b5V260(0x0) = CONST 
    0x12b8S0x260: v12b8V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12cdS0x260: v12cdV260 = AND v12b8V260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x12ceS0x260: v12ceV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12e3S0x260: v12e3V260 = AND v12ceV260(0xffffffffffffffffffffffffffffffffffffffff), v12cdV260
    0x12e5S0x260: MSTORE v12b5V260(0x0), v12e3V260
    0x12e6S0x260: v12e6V260(0x20) = CONST 
    0x12e8S0x260: v12e8V260(0x20) = ADD v12e6V260(0x20), v12b5V260(0x0)
    0x12ebS0x260: MSTORE v12e8V260(0x20), v12b3V260(0x1)
    0x12ecS0x260: v12ecV260(0x20) = CONST 
    0x12eeS0x260: v12eeV260(0x40) = ADD v12ecV260(0x20), v12e8V260(0x20)
    0x12efS0x260: v12efV260(0x0) = CONST 
    0x12f1S0x260: v12f1V260 = SHA3 v12efV260(0x0), v12eeV260(0x40)
    0x12f4S0x260: SSTORE v12f1V260, v12b1_0V260
    0x12f6S0x260: v12f6V260(0x1347) = CONST 
    0x12faS0x260: v12faV260(0x1) = CONST 
    0x12fcS0x260: v12fcV260(0x0) = CONST 
    0x12ffS0x260: v12ffV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1314S0x260: v1314V260 = AND v12ffV260(0xffffffffffffffffffffffffffffffffffffffff), v29d
    0x1315S0x260: v1315V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x132aS0x260: v132aV260 = AND v1315V260(0xffffffffffffffffffffffffffffffffffffffff), v1314V260
    0x132cS0x260: MSTORE v12fcV260(0x0), v132aV260
    0x132dS0x260: v132dV260(0x20) = CONST 
    0x132fS0x260: v132fV260(0x20) = ADD v132dV260(0x20), v12fcV260(0x0)
    0x1332S0x260: MSTORE v132fV260(0x20), v12faV260(0x1)
    0x1333S0x260: v1333V260(0x20) = CONST 
    0x1335S0x260: v1335V260(0x40) = ADD v1333V260(0x20), v132fV260(0x20)
    0x1336S0x260: v1336V260(0x0) = CONST 
    0x1338S0x260: v1338V260 = SHA3 v1336V260(0x0), v1335V260(0x40)
    0x1339S0x260: v1339V260 = SLOAD v1338V260
    0x133aS0x260: v133aV260(0x1509) = CONST 
    0x1340S0x260: v1340V260(0xffffffff) = CONST 
    0x1345S0x260: v1345V260(0x1509) = AND v1340V260(0xffffffff), v133aV260(0x1509)
    0x1346S0x260: v1346_0V260 = CALLPRIVATE v1345V260(0x1509), v2a6, v1339V260, v12f6V260(0x1347)

    Begin block 0x1347B0x260
    prev=[0x12b2B0x260], succ=[0x1419B0x260]
    =================================
    0x1348S0x260: v1348V260(0x1) = CONST 
    0x134aS0x260: v134aV260(0x0) = CONST 
    0x134dS0x260: v134dV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1362S0x260: v1362V260 = AND v134dV260(0xffffffffffffffffffffffffffffffffffffffff), v29d
    0x1363S0x260: v1363V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1378S0x260: v1378V260 = AND v1363V260(0xffffffffffffffffffffffffffffffffffffffff), v1362V260
    0x137aS0x260: MSTORE v134aV260(0x0), v1378V260
    0x137bS0x260: v137bV260(0x20) = CONST 
    0x137dS0x260: v137dV260(0x20) = ADD v137bV260(0x20), v134aV260(0x0)
    0x1380S0x260: MSTORE v137dV260(0x20), v1348V260(0x1)
    0x1381S0x260: v1381V260(0x20) = CONST 
    0x1383S0x260: v1383V260(0x40) = ADD v1381V260(0x20), v137dV260(0x20)
    0x1384S0x260: v1384V260(0x0) = CONST 
    0x1386S0x260: v1386V260 = SHA3 v1384V260(0x0), v1383V260(0x40)
    0x1389S0x260: SSTORE v1386V260, v1346_0V260
    0x138bS0x260: v138bV260(0x1419) = CONST 
    0x138fS0x260: v138fV260(0x2) = CONST 
    0x1391S0x260: v1391V260(0x0) = CONST 
    0x1394S0x260: v1394V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13a9S0x260: v13a9V260 = AND v1394V260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x13aaS0x260: v13aaV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13bfS0x260: v13bfV260 = AND v13aaV260(0xffffffffffffffffffffffffffffffffffffffff), v13a9V260
    0x13c1S0x260: MSTORE v1391V260(0x0), v13bfV260
    0x13c2S0x260: v13c2V260(0x20) = CONST 
    0x13c4S0x260: v13c4V260(0x20) = ADD v13c2V260(0x20), v1391V260(0x0)
    0x13c7S0x260: MSTORE v13c4V260(0x20), v138fV260(0x2)
    0x13c8S0x260: v13c8V260(0x20) = CONST 
    0x13caS0x260: v13caV260(0x40) = ADD v13c8V260(0x20), v13c4V260(0x20)
    0x13cbS0x260: v13cbV260(0x0) = CONST 
    0x13cdS0x260: v13cdV260 = SHA3 v13cbV260(0x0), v13caV260(0x40)
    0x13ceS0x260: v13ceV260(0x0) = CONST 
    0x13d0S0x260: v13d0V260 = CALLER 
    0x13d1S0x260: v13d1V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13e6S0x260: v13e6V260 = AND v13d1V260(0xffffffffffffffffffffffffffffffffffffffff), v13d0V260
    0x13e7S0x260: v13e7V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13fcS0x260: v13fcV260 = AND v13e7V260(0xffffffffffffffffffffffffffffffffffffffff), v13e6V260
    0x13feS0x260: MSTORE v13ceV260(0x0), v13fcV260
    0x13ffS0x260: v13ffV260(0x20) = CONST 
    0x1401S0x260: v1401V260(0x20) = ADD v13ffV260(0x20), v13ceV260(0x0)
    0x1404S0x260: MSTORE v1401V260(0x20), v13cdV260
    0x1405S0x260: v1405V260(0x20) = CONST 
    0x1407S0x260: v1407V260(0x40) = ADD v1405V260(0x20), v1401V260(0x20)
    0x1408S0x260: v1408V260(0x0) = CONST 
    0x140aS0x260: v140aV260 = SHA3 v1408V260(0x0), v1407V260(0x40)
    0x140bS0x260: v140bV260 = SLOAD v140aV260
    0x140cS0x260: v140cV260(0x1527) = CONST 
    0x1412S0x260: v1412V260(0xffffffff) = CONST 
    0x1417S0x260: v1417V260(0x1527) = AND v1412V260(0xffffffff), v140cV260(0x1527)
    0x1418S0x260: v1418_0V260 = CALLPRIVATE v1417V260(0x1527), v2a6, v140bV260, v138bV260(0x1419)

    Begin block 0x1419B0x260
    prev=[0x1347B0x260], succ=[0x78cB0x260]
    =================================
    0x141aS0x260: v141aV260(0x2) = CONST 
    0x141cS0x260: v141cV260(0x0) = CONST 
    0x141fS0x260: v141fV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1434S0x260: v1434V260 = AND v141fV260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x1435S0x260: v1435V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x144aS0x260: v144aV260 = AND v1435V260(0xffffffffffffffffffffffffffffffffffffffff), v1434V260
    0x144cS0x260: MSTORE v141cV260(0x0), v144aV260
    0x144dS0x260: v144dV260(0x20) = CONST 
    0x144fS0x260: v144fV260(0x20) = ADD v144dV260(0x20), v141cV260(0x0)
    0x1452S0x260: MSTORE v144fV260(0x20), v141aV260(0x2)
    0x1453S0x260: v1453V260(0x20) = CONST 
    0x1455S0x260: v1455V260(0x40) = ADD v1453V260(0x20), v144fV260(0x20)
    0x1456S0x260: v1456V260(0x0) = CONST 
    0x1458S0x260: v1458V260 = SHA3 v1456V260(0x0), v1455V260(0x40)
    0x1459S0x260: v1459V260(0x0) = CONST 
    0x145bS0x260: v145bV260 = CALLER 
    0x145cS0x260: v145cV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1471S0x260: v1471V260 = AND v145cV260(0xffffffffffffffffffffffffffffffffffffffff), v145bV260
    0x1472S0x260: v1472V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1487S0x260: v1487V260 = AND v1472V260(0xffffffffffffffffffffffffffffffffffffffff), v1471V260
    0x1489S0x260: MSTORE v1459V260(0x0), v1487V260
    0x148aS0x260: v148aV260(0x20) = CONST 
    0x148cS0x260: v148cV260(0x20) = ADD v148aV260(0x20), v1459V260(0x0)
    0x148fS0x260: MSTORE v148cV260(0x20), v1458V260
    0x1490S0x260: v1490V260(0x20) = CONST 
    0x1492S0x260: v1492V260(0x40) = ADD v1490V260(0x20), v148cV260(0x20)
    0x1493S0x260: v1493V260(0x0) = CONST 
    0x1495S0x260: v1495V260 = SHA3 v1493V260(0x0), v1492V260(0x40)
    0x1498S0x260: SSTORE v1495V260, v1418_0V260
    0x149bS0x260: v149bV260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14b0S0x260: v14b0V260 = AND v149bV260(0xffffffffffffffffffffffffffffffffffffffff), v29d
    0x14b2S0x260: v14b2V260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14c7S0x260: v14c7V260 = AND v14b2V260(0xffffffffffffffffffffffffffffffffffffffff), v27e
    0x14c8S0x260: v14c8V260(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x14eaS0x260: v14eaV260(0x40) = CONST 
    0x14ecS0x260: v14ecV260 = MLOAD v14eaV260(0x40)
    0x14f0S0x260: MSTORE v14ecV260, v2a6
    0x14f1S0x260: v14f1V260(0x20) = CONST 
    0x14f3S0x260: v14f3V260 = ADD v14f1V260(0x20), v14ecV260
    0x14f7S0x260: v14f7V260(0x40) = CONST 
    0x14f9S0x260: v14f9V260 = MLOAD v14f7V260(0x40)
    0x14fcS0x260: v14fcV260(0x20) = SUB v14f3V260, v14f9V260
    0x14feS0x260: LOG3 v14f9V260, v14fcV260(0x20), v14c8V260(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v14c7V260, v14b0V260
    0x14ffS0x260: v14ffV260(0x1) = CONST 
    0x1508S0x260: JUMP v782V260(0x78c)

    Begin block 0x78cB0x260
    prev=[0x1419B0x260], succ=[0x2b4]
    =================================
    0x794S0x260: JUMP v261(0x2b4)

    Begin block 0x2b4
    prev=[0x78cB0x260], succ=[]
    =================================
    0x2b5: v2b5(0x40) = CONST 
    0x2b7: v2b7 = MLOAD v2b5(0x40)
    0x2ba: v2ba(0x0) = ISZERO v14ffV260(0x1)
    0x2bb: v2bb(0x1) = ISZERO v2ba(0x0)
    0x2bc: v2bc(0x0) = ISZERO v2bb(0x1)
    0x2bd: v2bd(0x1) = ISZERO v2bc(0x0)
    0x2bf: MSTORE v2b7, v2bd(0x1)
    0x2c0: v2c0(0x20) = CONST 
    0x2c2: v2c2 = ADD v2c0(0x20), v2b7
    0x2c6: v2c6(0x40) = CONST 
    0x2c8: v2c8 = MLOAD v2c6(0x40)
    0x2cb: v2cb(0x20) = SUB v2c2, v2c8
    0x2cd: RETURN v2c8, v2cb(0x20)

}

function decimals()() public {
    Begin block 0x2ce
    prev=[], succ=[0x2d5, 0x2d9]
    =================================
    0x2cf: v2cf = CALLVALUE 
    0x2d0: v2d0 = ISZERO v2cf
    0x2d1: v2d1(0x2d9) = CONST 
    0x2d4: JUMPI v2d1(0x2d9), v2d0

    Begin block 0x2d5
    prev=[0x2ce], succ=[]
    =================================
    0x2d5: v2d5(0x0) = CONST 
    0x2d8: REVERT v2d5(0x0), v2d5(0x0)

    Begin block 0x2d9
    prev=[0x2ce], succ=[0x795]
    =================================
    0x2da: v2da(0x2e1) = CONST 
    0x2dd: v2dd(0x795) = CONST 
    0x2e0: JUMP v2dd(0x795)

    Begin block 0x795
    prev=[0x2d9], succ=[0x2e1]
    =================================
    0x796: v796(0x2) = CONST 
    0x799: JUMP v2da(0x2e1)

    Begin block 0x2e1
    prev=[0x795], succ=[]
    =================================
    0x2e2: v2e2(0x40) = CONST 
    0x2e4: v2e4 = MLOAD v2e2(0x40)
    0x2e7: v2e7(0xff) = CONST 
    0x2e9: v2e9(0x2) = AND v2e7(0xff), v796(0x2)
    0x2ea: v2ea(0xff) = CONST 
    0x2ec: v2ec(0x2) = AND v2ea(0xff), v2e9(0x2)
    0x2ee: MSTORE v2e4, v2ec(0x2)
    0x2ef: v2ef(0x20) = CONST 
    0x2f1: v2f1 = ADD v2ef(0x20), v2e4
    0x2f5: v2f5(0x40) = CONST 
    0x2f7: v2f7 = MLOAD v2f5(0x40)
    0x2fa: v2fa(0x20) = SUB v2f1, v2f7
    0x2fc: RETURN v2f7, v2fa(0x20)

}

function unpause()() public {
    Begin block 0x2fd
    prev=[], succ=[0x304, 0x308]
    =================================
    0x2fe: v2fe = CALLVALUE 
    0x2ff: v2ff = ISZERO v2fe
    0x300: v300(0x308) = CONST 
    0x303: JUMPI v300(0x308), v2ff

    Begin block 0x304
    prev=[0x2fd], succ=[]
    =================================
    0x304: v304(0x0) = CONST 
    0x307: REVERT v304(0x0), v304(0x0)

    Begin block 0x308
    prev=[0x2fd], succ=[0x79a]
    =================================
    0x309: v309(0x310) = CONST 
    0x30c: v30c(0x79a) = CONST 
    0x30f: JUMP v30c(0x79a)

    Begin block 0x79a
    prev=[0x308], succ=[0x7f2, 0x7f6]
    =================================
    0x79b: v79b(0x3) = CONST 
    0x79d: v79d(0x0) = CONST 
    0x7a0: v7a0 = SLOAD v79b(0x3)
    0x7a2: v7a2(0x100) = CONST 
    0x7a5: v7a5(0x1) = EXP v7a2(0x100), v79d(0x0)
    0x7a7: v7a7 = DIV v7a0, v7a5(0x1)
    0x7a8: v7a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7bd: v7bd = AND v7a8(0xffffffffffffffffffffffffffffffffffffffff), v7a7
    0x7be: v7be(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7d3: v7d3 = AND v7be(0xffffffffffffffffffffffffffffffffffffffff), v7bd
    0x7d4: v7d4 = CALLER 
    0x7d5: v7d5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7ea: v7ea = AND v7d5(0xffffffffffffffffffffffffffffffffffffffff), v7d4
    0x7eb: v7eb = EQ v7ea, v7d3
    0x7ec: v7ec = ISZERO v7eb
    0x7ed: v7ed = ISZERO v7ec
    0x7ee: v7ee(0x7f6) = CONST 
    0x7f1: JUMPI v7ee(0x7f6), v7ed

    Begin block 0x7f2
    prev=[0x79a], succ=[]
    =================================
    0x7f2: v7f2(0x0) = CONST 
    0x7f5: REVERT v7f2(0x0), v7f2(0x0)

    Begin block 0x7f6
    prev=[0x79a], succ=[0x80d, 0x811]
    =================================
    0x7f7: v7f7(0x3) = CONST 
    0x7f9: v7f9(0x14) = CONST 
    0x7fc: v7fc = SLOAD v7f7(0x3)
    0x7fe: v7fe(0x100) = CONST 
    0x801: v801(0x10000000000000000000000000000000000000000) = EXP v7fe(0x100), v7f9(0x14)
    0x803: v803 = DIV v7fc, v801(0x10000000000000000000000000000000000000000)
    0x804: v804(0xff) = CONST 
    0x806: v806 = AND v804(0xff), v803
    0x807: v807 = ISZERO v806
    0x808: v808 = ISZERO v807
    0x809: v809(0x811) = CONST 
    0x80c: JUMPI v809(0x811), v808

    Begin block 0x80d
    prev=[0x7f6], succ=[]
    =================================
    0x80d: v80d(0x0) = CONST 
    0x810: REVERT v80d(0x0), v80d(0x0)

    Begin block 0x811
    prev=[0x7f6], succ=[0x310]
    =================================
    0x812: v812(0x0) = CONST 
    0x814: v814(0x3) = CONST 
    0x816: v816(0x14) = CONST 
    0x818: v818(0x100) = CONST 
    0x81b: v81b(0x10000000000000000000000000000000000000000) = EXP v818(0x100), v816(0x14)
    0x81d: v81d = SLOAD v814(0x3)
    0x81f: v81f(0xff) = CONST 
    0x821: v821(0xff0000000000000000000000000000000000000000) = MUL v81f(0xff), v81b(0x10000000000000000000000000000000000000000)
    0x822: v822(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v821(0xff0000000000000000000000000000000000000000)
    0x823: v823 = AND v822(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v81d
    0x826: v826(0x1) = ISZERO v812(0x0)
    0x827: v827(0x0) = ISZERO v826(0x1)
    0x828: v828(0x0) = MUL v827(0x0), v81b(0x10000000000000000000000000000000000000000)
    0x829: v829 = OR v828(0x0), v823
    0x82b: SSTORE v814(0x3), v829
    0x82d: v82d(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33) = CONST 
    0x84e: v84e(0x40) = CONST 
    0x850: v850 = MLOAD v84e(0x40)
    0x851: v851(0x40) = CONST 
    0x853: v853 = MLOAD v851(0x40)
    0x856: v856(0x0) = SUB v850, v853
    0x858: LOG1 v853, v856(0x0), v82d(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33)
    0x859: JUMP v309(0x310)

    Begin block 0x310
    prev=[0x811], succ=[]
    =================================
    0x311: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x312
    prev=[], succ=[0x319, 0x31d]
    =================================
    0x313: v313 = CALLVALUE 
    0x314: v314 = ISZERO v313
    0x315: v315(0x31d) = CONST 
    0x318: JUMPI v315(0x31d), v314

    Begin block 0x319
    prev=[0x312], succ=[]
    =================================
    0x319: v319(0x0) = CONST 
    0x31c: REVERT v319(0x0), v319(0x0)

    Begin block 0x31d
    prev=[0x312], succ=[0x85a]
    =================================
    0x31e: v31e(0x352) = CONST 
    0x321: v321(0x4) = CONST 
    0x325: v325 = CALLDATALOAD v321(0x4)
    0x326: v326(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33b: v33b = AND v326(0xffffffffffffffffffffffffffffffffffffffff), v325
    0x33d: v33d(0x20) = CONST 
    0x33f: v33f(0x24) = ADD v33d(0x20), v321(0x4)
    0x344: v344 = CALLDATALOAD v33f(0x24)
    0x346: v346(0x20) = CONST 
    0x348: v348(0x44) = ADD v346(0x20), v33f(0x24)
    0x34e: v34e(0x85a) = CONST 
    0x351: JUMP v34e(0x85a)

    Begin block 0x85a
    prev=[0x31d], succ=[0x8b4, 0x8b8]
    =================================
    0x85b: v85b(0x0) = CONST 
    0x85d: v85d(0x3) = CONST 
    0x85f: v85f(0x0) = CONST 
    0x862: v862 = SLOAD v85d(0x3)
    0x864: v864(0x100) = CONST 
    0x867: v867(0x1) = EXP v864(0x100), v85f(0x0)
    0x869: v869 = DIV v862, v867(0x1)
    0x86a: v86a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x87f: v87f = AND v86a(0xffffffffffffffffffffffffffffffffffffffff), v869
    0x880: v880(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x895: v895 = AND v880(0xffffffffffffffffffffffffffffffffffffffff), v87f
    0x896: v896 = CALLER 
    0x897: v897(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8ac: v8ac = AND v897(0xffffffffffffffffffffffffffffffffffffffff), v896
    0x8ad: v8ad = EQ v8ac, v895
    0x8ae: v8ae = ISZERO v8ad
    0x8af: v8af = ISZERO v8ae
    0x8b0: v8b0(0x8b8) = CONST 
    0x8b3: JUMPI v8b0(0x8b8), v8af

    Begin block 0x8b4
    prev=[0x85a], succ=[]
    =================================
    0x8b4: v8b4(0x0) = CONST 
    0x8b7: REVERT v8b4(0x0), v8b4(0x0)

    Begin block 0x8b8
    prev=[0x85a], succ=[0x8d0, 0x8d4]
    =================================
    0x8b9: v8b9(0x3) = CONST 
    0x8bb: v8bb(0x15) = CONST 
    0x8be: v8be = SLOAD v8b9(0x3)
    0x8c0: v8c0(0x100) = CONST 
    0x8c3: v8c3(0x1000000000000000000000000000000000000000000) = EXP v8c0(0x100), v8bb(0x15)
    0x8c5: v8c5 = DIV v8be, v8c3(0x1000000000000000000000000000000000000000000)
    0x8c6: v8c6(0xff) = CONST 
    0x8c8: v8c8 = AND v8c6(0xff), v8c5
    0x8c9: v8c9 = ISZERO v8c8
    0x8ca: v8ca = ISZERO v8c9
    0x8cb: v8cb = ISZERO v8ca
    0x8cc: v8cc(0x8d4) = CONST 
    0x8cf: JUMPI v8cc(0x8d4), v8cb

    Begin block 0x8d0
    prev=[0x8b8], succ=[]
    =================================
    0x8d0: v8d0(0x0) = CONST 
    0x8d3: REVERT v8d0(0x0), v8d0(0x0)

    Begin block 0x8d4
    prev=[0x8b8], succ=[0x8e9]
    =================================
    0x8d5: v8d5(0x8e9) = CONST 
    0x8d9: v8d9(0x0) = CONST 
    0x8db: v8db = SLOAD v8d9(0x0)
    0x8dc: v8dc(0x1509) = CONST 
    0x8e2: v8e2(0xffffffff) = CONST 
    0x8e7: v8e7(0x1509) = AND v8e2(0xffffffff), v8dc(0x1509)
    0x8e8: v8e8_0 = CALLPRIVATE v8e7(0x1509), v344, v8db, v8d5(0x8e9)

    Begin block 0x8e9
    prev=[0x8d4], succ=[0x941]
    =================================
    0x8ea: v8ea(0x0) = CONST 
    0x8ee: SSTORE v8ea(0x0), v8e8_0
    0x8f0: v8f0(0x941) = CONST 
    0x8f4: v8f4(0x1) = CONST 
    0x8f6: v8f6(0x0) = CONST 
    0x8f9: v8f9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x90e: v90e = AND v8f9(0xffffffffffffffffffffffffffffffffffffffff), v33b
    0x90f: v90f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x924: v924 = AND v90f(0xffffffffffffffffffffffffffffffffffffffff), v90e
    0x926: MSTORE v8f6(0x0), v924
    0x927: v927(0x20) = CONST 
    0x929: v929(0x20) = ADD v927(0x20), v8f6(0x0)
    0x92c: MSTORE v929(0x20), v8f4(0x1)
    0x92d: v92d(0x20) = CONST 
    0x92f: v92f(0x40) = ADD v92d(0x20), v929(0x20)
    0x930: v930(0x0) = CONST 
    0x932: v932 = SHA3 v930(0x0), v92f(0x40)
    0x933: v933 = SLOAD v932
    0x934: v934(0x1509) = CONST 
    0x93a: v93a(0xffffffff) = CONST 
    0x93f: v93f(0x1509) = AND v93a(0xffffffff), v934(0x1509)
    0x940: v940_0 = CALLPRIVATE v93f(0x1509), v344, v933, v8f0(0x941)

    Begin block 0x941
    prev=[0x8e9], succ=[0x352]
    =================================
    0x942: v942(0x1) = CONST 
    0x944: v944(0x0) = CONST 
    0x947: v947(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x95c: v95c = AND v947(0xffffffffffffffffffffffffffffffffffffffff), v33b
    0x95d: v95d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x972: v972 = AND v95d(0xffffffffffffffffffffffffffffffffffffffff), v95c
    0x974: MSTORE v944(0x0), v972
    0x975: v975(0x20) = CONST 
    0x977: v977(0x20) = ADD v975(0x20), v944(0x0)
    0x97a: MSTORE v977(0x20), v942(0x1)
    0x97b: v97b(0x20) = CONST 
    0x97d: v97d(0x40) = ADD v97b(0x20), v977(0x20)
    0x97e: v97e(0x0) = CONST 
    0x980: v980 = SHA3 v97e(0x0), v97d(0x40)
    0x983: SSTORE v980, v940_0
    0x986: v986(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x99b: v99b = AND v986(0xffffffffffffffffffffffffffffffffffffffff), v33b
    0x99c: v99c(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0x9be: v9be(0x40) = CONST 
    0x9c0: v9c0 = MLOAD v9be(0x40)
    0x9c4: MSTORE v9c0, v344
    0x9c5: v9c5(0x20) = CONST 
    0x9c7: v9c7 = ADD v9c5(0x20), v9c0
    0x9cb: v9cb(0x40) = CONST 
    0x9cd: v9cd = MLOAD v9cb(0x40)
    0x9d0: v9d0(0x20) = SUB v9c7, v9cd
    0x9d2: LOG2 v9cd, v9d0(0x20), v99c(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), v99b
    0x9d4: v9d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9e9: v9e9 = AND v9d4(0xffffffffffffffffffffffffffffffffffffffff), v33b
    0x9ea: v9ea(0x0) = CONST 
    0x9ec: v9ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa01: va01(0x0) = AND v9ec(0xffffffffffffffffffffffffffffffffffffffff), v9ea(0x0)
    0xa02: va02(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xa24: va24(0x40) = CONST 
    0xa26: va26 = MLOAD va24(0x40)
    0xa2a: MSTORE va26, v344
    0xa2b: va2b(0x20) = CONST 
    0xa2d: va2d = ADD va2b(0x20), va26
    0xa31: va31(0x40) = CONST 
    0xa33: va33 = MLOAD va31(0x40)
    0xa36: va36(0x20) = SUB va2d, va33
    0xa38: LOG3 va33, va36(0x20), va02(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), va01(0x0), v9e9
    0xa39: va39(0x1) = CONST 
    0xa41: JUMP v31e(0x352)

    Begin block 0x352
    prev=[0x941], succ=[]
    =================================
    0x353: v353(0x40) = CONST 
    0x355: v355 = MLOAD v353(0x40)
    0x358: v358(0x0) = ISZERO va39(0x1)
    0x359: v359(0x1) = ISZERO v358(0x0)
    0x35a: v35a(0x0) = ISZERO v359(0x1)
    0x35b: v35b(0x1) = ISZERO v35a(0x0)
    0x35d: MSTORE v355, v35b(0x1)
    0x35e: v35e(0x20) = CONST 
    0x360: v360 = ADD v35e(0x20), v355
    0x364: v364(0x40) = CONST 
    0x366: v366 = MLOAD v364(0x40)
    0x369: v369(0x20) = SUB v360, v366
    0x36b: RETURN v366, v369(0x20)

}

function burn(uint256)() public {
    Begin block 0x36c
    prev=[], succ=[0x373, 0x377]
    =================================
    0x36d: v36d = CALLVALUE 
    0x36e: v36e = ISZERO v36d
    0x36f: v36f(0x377) = CONST 
    0x372: JUMPI v36f(0x377), v36e

    Begin block 0x373
    prev=[0x36c], succ=[]
    =================================
    0x373: v373(0x0) = CONST 
    0x376: REVERT v373(0x0), v373(0x0)

    Begin block 0x377
    prev=[0x36c], succ=[0xa42]
    =================================
    0x378: v378(0x38d) = CONST 
    0x37b: v37b(0x4) = CONST 
    0x37f: v37f = CALLDATALOAD v37b(0x4)
    0x381: v381(0x20) = CONST 
    0x383: v383(0x24) = ADD v381(0x20), v37b(0x4)
    0x389: v389(0xa42) = CONST 
    0x38c: JUMP v389(0xa42)

    Begin block 0xa42
    prev=[0x377], succ=[0xa4e, 0xa52]
    =================================
    0xa43: va43(0x0) = CONST 
    0xa47: va47 = GT v37f, va43(0x0)
    0xa48: va48 = ISZERO va47
    0xa49: va49 = ISZERO va48
    0xa4a: va4a(0xa52) = CONST 
    0xa4d: JUMPI va4a(0xa52), va49

    Begin block 0xa4e
    prev=[0xa42], succ=[]
    =================================
    0xa4e: va4e(0x0) = CONST 
    0xa51: REVERT va4e(0x0), va4e(0x0)

    Begin block 0xa52
    prev=[0xa42], succ=[0xa9c, 0xaa0]
    =================================
    0xa53: va53(0x1) = CONST 
    0xa55: va55(0x0) = CONST 
    0xa57: va57 = CALLER 
    0xa58: va58(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa6d: va6d = AND va58(0xffffffffffffffffffffffffffffffffffffffff), va57
    0xa6e: va6e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa83: va83 = AND va6e(0xffffffffffffffffffffffffffffffffffffffff), va6d
    0xa85: MSTORE va55(0x0), va83
    0xa86: va86(0x20) = CONST 
    0xa88: va88(0x20) = ADD va86(0x20), va55(0x0)
    0xa8b: MSTORE va88(0x20), va53(0x1)
    0xa8c: va8c(0x20) = CONST 
    0xa8e: va8e(0x40) = ADD va8c(0x20), va88(0x20)
    0xa8f: va8f(0x0) = CONST 
    0xa91: va91 = SHA3 va8f(0x0), va8e(0x40)
    0xa92: va92 = SLOAD va91
    0xa94: va94 = GT v37f, va92
    0xa95: va95 = ISZERO va94
    0xa96: va96 = ISZERO va95
    0xa97: va97 = ISZERO va96
    0xa98: va98(0xaa0) = CONST 
    0xa9b: JUMPI va98(0xaa0), va97

    Begin block 0xa9c
    prev=[0xa52], succ=[]
    =================================
    0xa9c: va9c(0x0) = CONST 
    0xa9f: REVERT va9c(0x0), va9c(0x0)

    Begin block 0xaa0
    prev=[0xa52], succ=[0xaf5]
    =================================
    0xaa1: vaa1 = CALLER 
    0xaa4: vaa4(0xaf5) = CONST 
    0xaa8: vaa8(0x1) = CONST 
    0xaaa: vaaa(0x0) = CONST 
    0xaad: vaad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xac2: vac2 = AND vaad(0xffffffffffffffffffffffffffffffffffffffff), vaa1
    0xac3: vac3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xad8: vad8 = AND vac3(0xffffffffffffffffffffffffffffffffffffffff), vac2
    0xada: MSTORE vaaa(0x0), vad8
    0xadb: vadb(0x20) = CONST 
    0xadd: vadd(0x20) = ADD vadb(0x20), vaaa(0x0)
    0xae0: MSTORE vadd(0x20), vaa8(0x1)
    0xae1: vae1(0x20) = CONST 
    0xae3: vae3(0x40) = ADD vae1(0x20), vadd(0x20)
    0xae4: vae4(0x0) = CONST 
    0xae6: vae6 = SHA3 vae4(0x0), vae3(0x40)
    0xae7: vae7 = SLOAD vae6
    0xae8: vae8(0x1527) = CONST 
    0xaee: vaee(0xffffffff) = CONST 
    0xaf3: vaf3(0x1527) = AND vaee(0xffffffff), vae8(0x1527)
    0xaf4: vaf4_0 = CALLPRIVATE vaf3(0x1527), v37f, vae7, vaa4(0xaf5)

    Begin block 0xaf5
    prev=[0xaa0], succ=[0xb4d]
    =================================
    0xaf6: vaf6(0x1) = CONST 
    0xaf8: vaf8(0x0) = CONST 
    0xafb: vafb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb10: vb10 = AND vafb(0xffffffffffffffffffffffffffffffffffffffff), vaa1
    0xb11: vb11(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb26: vb26 = AND vb11(0xffffffffffffffffffffffffffffffffffffffff), vb10
    0xb28: MSTORE vaf8(0x0), vb26
    0xb29: vb29(0x20) = CONST 
    0xb2b: vb2b(0x20) = ADD vb29(0x20), vaf8(0x0)
    0xb2e: MSTORE vb2b(0x20), vaf6(0x1)
    0xb2f: vb2f(0x20) = CONST 
    0xb31: vb31(0x40) = ADD vb2f(0x20), vb2b(0x20)
    0xb32: vb32(0x0) = CONST 
    0xb34: vb34 = SHA3 vb32(0x0), vb31(0x40)
    0xb37: SSTORE vb34, vaf4_0
    0xb39: vb39(0xb4d) = CONST 
    0xb3d: vb3d(0x0) = CONST 
    0xb3f: vb3f = SLOAD vb3d(0x0)
    0xb40: vb40(0x1527) = CONST 
    0xb46: vb46(0xffffffff) = CONST 
    0xb4b: vb4b(0x1527) = AND vb46(0xffffffff), vb40(0x1527)
    0xb4c: vb4c_0 = CALLPRIVATE vb4b(0x1527), v37f, vb3f, vb39(0xb4d)

    Begin block 0xb4d
    prev=[0xaf5], succ=[0x38d]
    =================================
    0xb4e: vb4e(0x0) = CONST 
    0xb52: SSTORE vb4e(0x0), vb4c_0
    0xb55: vb55(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb6a: vb6a = AND vb55(0xffffffffffffffffffffffffffffffffffffffff), vaa1
    0xb6b: vb6b(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0xb8d: vb8d(0x40) = CONST 
    0xb8f: vb8f = MLOAD vb8d(0x40)
    0xb93: MSTORE vb8f, v37f
    0xb94: vb94(0x20) = CONST 
    0xb96: vb96 = ADD vb94(0x20), vb8f
    0xb9a: vb9a(0x40) = CONST 
    0xb9c: vb9c = MLOAD vb9a(0x40)
    0xb9f: vb9f(0x20) = SUB vb96, vb9c
    0xba1: LOG2 vb9c, vb9f(0x20), vb6b(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), vb6a
    0xba4: JUMP v378(0x38d)

    Begin block 0x38d
    prev=[0xb4d], succ=[]
    =================================
    0x38e: STOP 

}

function paused()() public {
    Begin block 0x38f
    prev=[], succ=[0x396, 0x39a]
    =================================
    0x390: v390 = CALLVALUE 
    0x391: v391 = ISZERO v390
    0x392: v392(0x39a) = CONST 
    0x395: JUMPI v392(0x39a), v391

    Begin block 0x396
    prev=[0x38f], succ=[]
    =================================
    0x396: v396(0x0) = CONST 
    0x399: REVERT v396(0x0), v396(0x0)

    Begin block 0x39a
    prev=[0x38f], succ=[0xba5]
    =================================
    0x39b: v39b(0x3a2) = CONST 
    0x39e: v39e(0xba5) = CONST 
    0x3a1: JUMP v39e(0xba5)

    Begin block 0xba5
    prev=[0x39a], succ=[0x3a2]
    =================================
    0xba6: vba6(0x3) = CONST 
    0xba8: vba8(0x14) = CONST 
    0xbab: vbab = SLOAD vba6(0x3)
    0xbad: vbad(0x100) = CONST 
    0xbb0: vbb0(0x10000000000000000000000000000000000000000) = EXP vbad(0x100), vba8(0x14)
    0xbb2: vbb2 = DIV vbab, vbb0(0x10000000000000000000000000000000000000000)
    0xbb3: vbb3(0xff) = CONST 
    0xbb5: vbb5 = AND vbb3(0xff), vbb2
    0xbb7: JUMP v39b(0x3a2)

    Begin block 0x3a2
    prev=[0xba5], succ=[]
    =================================
    0x3a3: v3a3(0x40) = CONST 
    0x3a5: v3a5 = MLOAD v3a3(0x40)
    0x3a8: v3a8 = ISZERO vbb5
    0x3a9: v3a9 = ISZERO v3a8
    0x3aa: v3aa = ISZERO v3a9
    0x3ab: v3ab = ISZERO v3aa
    0x3ad: MSTORE v3a5, v3ab
    0x3ae: v3ae(0x20) = CONST 
    0x3b0: v3b0 = ADD v3ae(0x20), v3a5
    0x3b4: v3b4(0x40) = CONST 
    0x3b6: v3b6 = MLOAD v3b4(0x40)
    0x3b9: v3b9(0x20) = SUB v3b0, v3b6
    0x3bb: RETURN v3b6, v3b9(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x3bc
    prev=[], succ=[0x3c3, 0x3c7]
    =================================
    0x3bd: v3bd = CALLVALUE 
    0x3be: v3be = ISZERO v3bd
    0x3bf: v3bf(0x3c7) = CONST 
    0x3c2: JUMPI v3bf(0x3c7), v3be

    Begin block 0x3c3
    prev=[0x3bc], succ=[]
    =================================
    0x3c3: v3c3(0x0) = CONST 
    0x3c6: REVERT v3c3(0x0), v3c3(0x0)

    Begin block 0x3c7
    prev=[0x3bc], succ=[0xbb8B0x3c7]
    =================================
    0x3c8: v3c8(0x3fc) = CONST 
    0x3cb: v3cb(0x4) = CONST 
    0x3cf: v3cf = CALLDATALOAD v3cb(0x4)
    0x3d0: v3d0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3e5: v3e5 = AND v3d0(0xffffffffffffffffffffffffffffffffffffffff), v3cf
    0x3e7: v3e7(0x20) = CONST 
    0x3e9: v3e9(0x24) = ADD v3e7(0x20), v3cb(0x4)
    0x3ee: v3ee = CALLDATALOAD v3e9(0x24)
    0x3f0: v3f0(0x20) = CONST 
    0x3f2: v3f2(0x44) = ADD v3f0(0x20), v3e9(0x24)
    0x3f8: v3f8(0xbb8) = CONST 
    0x3fb: JUMP v3f8(0xbb8)

    Begin block 0xbb8B0x3c7
    prev=[0x3c7], succ=[0xbd2B0x3c7, 0xbd6B0x3c7]
    =================================
    0xbb9S0x3c7: vbb9V3c7(0x0) = CONST 
    0xbbbS0x3c7: vbbbV3c7(0x3) = CONST 
    0xbbdS0x3c7: vbbdV3c7(0x14) = CONST 
    0xbc0S0x3c7: vbc0V3c7 = SLOAD vbbbV3c7(0x3)
    0xbc2S0x3c7: vbc2V3c7(0x100) = CONST 
    0xbc5S0x3c7: vbc5V3c7(0x10000000000000000000000000000000000000000) = EXP vbc2V3c7(0x100), vbbdV3c7(0x14)
    0xbc7S0x3c7: vbc7V3c7 = DIV vbc0V3c7, vbc5V3c7(0x10000000000000000000000000000000000000000)
    0xbc8S0x3c7: vbc8V3c7(0xff) = CONST 
    0xbcaS0x3c7: vbcaV3c7 = AND vbc8V3c7(0xff), vbc7V3c7
    0xbcbS0x3c7: vbcbV3c7 = ISZERO vbcaV3c7
    0xbccS0x3c7: vbccV3c7 = ISZERO vbcbV3c7
    0xbcdS0x3c7: vbcdV3c7 = ISZERO vbccV3c7
    0xbceS0x3c7: vbceV3c7(0xbd6) = CONST 
    0xbd1S0x3c7: JUMPI vbceV3c7(0xbd6), vbcdV3c7

    Begin block 0xbd2B0x3c7
    prev=[0xbb8B0x3c7], succ=[]
    =================================
    0xbd2S0x3c7: vbd2V3c7(0x0) = CONST 
    0xbd5S0x3c7: REVERT vbd2V3c7(0x0), vbd2V3c7(0x0)

    Begin block 0xbd6B0x3c7
    prev=[0xbb8B0x3c7], succ=[0x1540B0x3c7]
    =================================
    0xbd7S0x3c7: vbd7V3c7(0xbe0) = CONST 
    0xbdcS0x3c7: vbdcV3c7(0x1540) = CONST 
    0xbdfS0x3c7: JUMP vbdcV3c7(0x1540)

    Begin block 0x1540B0x3c7
    prev=[0xbd6B0x3c7], succ=[0x15cbB0x3c7, 0x1651B0x3c7]
    =================================
    0x1541S0x3c7: v1541V3c7(0x0) = CONST 
    0x1544S0x3c7: v1544V3c7(0x2) = CONST 
    0x1546S0x3c7: v1546V3c7(0x0) = CONST 
    0x1548S0x3c7: v1548V3c7 = CALLER 
    0x1549S0x3c7: v1549V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x155eS0x3c7: v155eV3c7 = AND v1549V3c7(0xffffffffffffffffffffffffffffffffffffffff), v1548V3c7
    0x155fS0x3c7: v155fV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1574S0x3c7: v1574V3c7 = AND v155fV3c7(0xffffffffffffffffffffffffffffffffffffffff), v155eV3c7
    0x1576S0x3c7: MSTORE v1546V3c7(0x0), v1574V3c7
    0x1577S0x3c7: v1577V3c7(0x20) = CONST 
    0x1579S0x3c7: v1579V3c7(0x20) = ADD v1577V3c7(0x20), v1546V3c7(0x0)
    0x157cS0x3c7: MSTORE v1579V3c7(0x20), v1544V3c7(0x2)
    0x157dS0x3c7: v157dV3c7(0x20) = CONST 
    0x157fS0x3c7: v157fV3c7(0x40) = ADD v157dV3c7(0x20), v1579V3c7(0x20)
    0x1580S0x3c7: v1580V3c7(0x0) = CONST 
    0x1582S0x3c7: v1582V3c7 = SHA3 v1580V3c7(0x0), v157fV3c7(0x40)
    0x1583S0x3c7: v1583V3c7(0x0) = CONST 
    0x1586S0x3c7: v1586V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x159bS0x3c7: v159bV3c7 = AND v1586V3c7(0xffffffffffffffffffffffffffffffffffffffff), v3e5
    0x159cS0x3c7: v159cV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15b1S0x3c7: v15b1V3c7 = AND v159cV3c7(0xffffffffffffffffffffffffffffffffffffffff), v159bV3c7
    0x15b3S0x3c7: MSTORE v1583V3c7(0x0), v15b1V3c7
    0x15b4S0x3c7: v15b4V3c7(0x20) = CONST 
    0x15b6S0x3c7: v15b6V3c7(0x20) = ADD v15b4V3c7(0x20), v1583V3c7(0x0)
    0x15b9S0x3c7: MSTORE v15b6V3c7(0x20), v1582V3c7
    0x15baS0x3c7: v15baV3c7(0x20) = CONST 
    0x15bcS0x3c7: v15bcV3c7(0x40) = ADD v15baV3c7(0x20), v15b6V3c7(0x20)
    0x15bdS0x3c7: v15bdV3c7(0x0) = CONST 
    0x15bfS0x3c7: v15bfV3c7 = SHA3 v15bdV3c7(0x0), v15bcV3c7(0x40)
    0x15c0S0x3c7: v15c0V3c7 = SLOAD v15bfV3c7
    0x15c5S0x3c7: v15c5V3c7 = GT v3ee, v15c0V3c7
    0x15c6S0x3c7: v15c6V3c7 = ISZERO v15c5V3c7
    0x15c7S0x3c7: v15c7V3c7(0x1651) = CONST 
    0x15caS0x3c7: JUMPI v15c7V3c7(0x1651), v15c6V3c7

    Begin block 0x15cbB0x3c7
    prev=[0x1540B0x3c7], succ=[0x16e5B0x3c7]
    =================================
    0x15cbS0x3c7: v15cbV3c7(0x0) = CONST 
    0x15cdS0x3c7: v15cdV3c7(0x2) = CONST 
    0x15cfS0x3c7: v15cfV3c7(0x0) = CONST 
    0x15d1S0x3c7: v15d1V3c7 = CALLER 
    0x15d2S0x3c7: v15d2V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15e7S0x3c7: v15e7V3c7 = AND v15d2V3c7(0xffffffffffffffffffffffffffffffffffffffff), v15d1V3c7
    0x15e8S0x3c7: v15e8V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15fdS0x3c7: v15fdV3c7 = AND v15e8V3c7(0xffffffffffffffffffffffffffffffffffffffff), v15e7V3c7
    0x15ffS0x3c7: MSTORE v15cfV3c7(0x0), v15fdV3c7
    0x1600S0x3c7: v1600V3c7(0x20) = CONST 
    0x1602S0x3c7: v1602V3c7(0x20) = ADD v1600V3c7(0x20), v15cfV3c7(0x0)
    0x1605S0x3c7: MSTORE v1602V3c7(0x20), v15cdV3c7(0x2)
    0x1606S0x3c7: v1606V3c7(0x20) = CONST 
    0x1608S0x3c7: v1608V3c7(0x40) = ADD v1606V3c7(0x20), v1602V3c7(0x20)
    0x1609S0x3c7: v1609V3c7(0x0) = CONST 
    0x160bS0x3c7: v160bV3c7 = SHA3 v1609V3c7(0x0), v1608V3c7(0x40)
    0x160cS0x3c7: v160cV3c7(0x0) = CONST 
    0x160fS0x3c7: v160fV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1624S0x3c7: v1624V3c7 = AND v160fV3c7(0xffffffffffffffffffffffffffffffffffffffff), v3e5
    0x1625S0x3c7: v1625V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x163aS0x3c7: v163aV3c7 = AND v1625V3c7(0xffffffffffffffffffffffffffffffffffffffff), v1624V3c7
    0x163cS0x3c7: MSTORE v160cV3c7(0x0), v163aV3c7
    0x163dS0x3c7: v163dV3c7(0x20) = CONST 
    0x163fS0x3c7: v163fV3c7(0x20) = ADD v163dV3c7(0x20), v160cV3c7(0x0)
    0x1642S0x3c7: MSTORE v163fV3c7(0x20), v160bV3c7
    0x1643S0x3c7: v1643V3c7(0x20) = CONST 
    0x1645S0x3c7: v1645V3c7(0x40) = ADD v1643V3c7(0x20), v163fV3c7(0x20)
    0x1646S0x3c7: v1646V3c7(0x0) = CONST 
    0x1648S0x3c7: v1648V3c7 = SHA3 v1646V3c7(0x0), v1645V3c7(0x40)
    0x164bS0x3c7: SSTORE v1648V3c7, v15cbV3c7(0x0)
    0x164dS0x3c7: v164dV3c7(0x16e5) = CONST 
    0x1650S0x3c7: JUMP v164dV3c7(0x16e5)

    Begin block 0x16e5B0x3c7
    prev=[0x15cbB0x3c7, 0x1664B0x3c7], succ=[0xbe0B0x3c7]
    =================================
    0x16e7S0x3c7: v16e7V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16fcS0x3c7: v16fcV3c7 = AND v16e7V3c7(0xffffffffffffffffffffffffffffffffffffffff), v3e5
    0x16fdS0x3c7: v16fdV3c7 = CALLER 
    0x16feS0x3c7: v16feV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1713S0x3c7: v1713V3c7 = AND v16feV3c7(0xffffffffffffffffffffffffffffffffffffffff), v16fdV3c7
    0x1714S0x3c7: v1714V3c7(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x1735S0x3c7: v1735V3c7(0x2) = CONST 
    0x1737S0x3c7: v1737V3c7(0x0) = CONST 
    0x1739S0x3c7: v1739V3c7 = CALLER 
    0x173aS0x3c7: v173aV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x174fS0x3c7: v174fV3c7 = AND v173aV3c7(0xffffffffffffffffffffffffffffffffffffffff), v1739V3c7
    0x1750S0x3c7: v1750V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1765S0x3c7: v1765V3c7 = AND v1750V3c7(0xffffffffffffffffffffffffffffffffffffffff), v174fV3c7
    0x1767S0x3c7: MSTORE v1737V3c7(0x0), v1765V3c7
    0x1768S0x3c7: v1768V3c7(0x20) = CONST 
    0x176aS0x3c7: v176aV3c7(0x20) = ADD v1768V3c7(0x20), v1737V3c7(0x0)
    0x176dS0x3c7: MSTORE v176aV3c7(0x20), v1735V3c7(0x2)
    0x176eS0x3c7: v176eV3c7(0x20) = CONST 
    0x1770S0x3c7: v1770V3c7(0x40) = ADD v176eV3c7(0x20), v176aV3c7(0x20)
    0x1771S0x3c7: v1771V3c7(0x0) = CONST 
    0x1773S0x3c7: v1773V3c7 = SHA3 v1771V3c7(0x0), v1770V3c7(0x40)
    0x1774S0x3c7: v1774V3c7(0x0) = CONST 
    0x1777S0x3c7: v1777V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x178cS0x3c7: v178cV3c7 = AND v1777V3c7(0xffffffffffffffffffffffffffffffffffffffff), v3e5
    0x178dS0x3c7: v178dV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17a2S0x3c7: v17a2V3c7 = AND v178dV3c7(0xffffffffffffffffffffffffffffffffffffffff), v178cV3c7
    0x17a4S0x3c7: MSTORE v1774V3c7(0x0), v17a2V3c7
    0x17a5S0x3c7: v17a5V3c7(0x20) = CONST 
    0x17a7S0x3c7: v17a7V3c7(0x20) = ADD v17a5V3c7(0x20), v1774V3c7(0x0)
    0x17aaS0x3c7: MSTORE v17a7V3c7(0x20), v1773V3c7
    0x17abS0x3c7: v17abV3c7(0x20) = CONST 
    0x17adS0x3c7: v17adV3c7(0x40) = ADD v17abV3c7(0x20), v17a7V3c7(0x20)
    0x17aeS0x3c7: v17aeV3c7(0x0) = CONST 
    0x17b0S0x3c7: v17b0V3c7 = SHA3 v17aeV3c7(0x0), v17adV3c7(0x40)
    0x17b1S0x3c7: v17b1V3c7 = SLOAD v17b0V3c7
    0x17b2S0x3c7: v17b2V3c7(0x40) = CONST 
    0x17b4S0x3c7: v17b4V3c7 = MLOAD v17b2V3c7(0x40)
    0x17b8S0x3c7: MSTORE v17b4V3c7, v17b1V3c7
    0x17b9S0x3c7: v17b9V3c7(0x20) = CONST 
    0x17bbS0x3c7: v17bbV3c7 = ADD v17b9V3c7(0x20), v17b4V3c7
    0x17bfS0x3c7: v17bfV3c7(0x40) = CONST 
    0x17c1S0x3c7: v17c1V3c7 = MLOAD v17bfV3c7(0x40)
    0x17c4S0x3c7: v17c4V3c7(0x20) = SUB v17bbV3c7, v17c1V3c7
    0x17c6S0x3c7: LOG3 v17c1V3c7, v17c4V3c7(0x20), v1714V3c7(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v1713V3c7, v16fcV3c7
    0x17c7S0x3c7: v17c7V3c7(0x1) = CONST 
    0x17d0S0x3c7: JUMP vbd7V3c7(0xbe0)

    Begin block 0xbe0B0x3c7
    prev=[0x16e5B0x3c7], succ=[0x3fc]
    =================================
    0xbe7S0x3c7: JUMP v3c8(0x3fc)

    Begin block 0x3fc
    prev=[0xbe0B0x3c7], succ=[]
    =================================
    0x3fd: v3fd(0x40) = CONST 
    0x3ff: v3ff = MLOAD v3fd(0x40)
    0x402: v402(0x0) = ISZERO v17c7V3c7(0x1)
    0x403: v403(0x1) = ISZERO v402(0x0)
    0x404: v404(0x0) = ISZERO v403(0x1)
    0x405: v405(0x1) = ISZERO v404(0x0)
    0x407: MSTORE v3ff, v405(0x1)
    0x408: v408(0x20) = CONST 
    0x40a: v40a = ADD v408(0x20), v3ff
    0x40e: v40e(0x40) = CONST 
    0x410: v410 = MLOAD v40e(0x40)
    0x413: v413(0x20) = SUB v40a, v410
    0x415: RETURN v410, v413(0x20)

    Begin block 0x1651B0x3c7
    prev=[0x1540B0x3c7], succ=[0x1664B0x3c7]
    =================================
    0x1652S0x3c7: v1652V3c7(0x1664) = CONST 
    0x1657S0x3c7: v1657V3c7(0x1527) = CONST 
    0x165dS0x3c7: v165dV3c7(0xffffffff) = CONST 
    0x1662S0x3c7: v1662V3c7(0x1527) = AND v165dV3c7(0xffffffff), v1657V3c7(0x1527)
    0x1663S0x3c7: v1663_0V3c7 = CALLPRIVATE v1662V3c7(0x1527), v3ee, v15c0V3c7, v1652V3c7(0x1664)

    Begin block 0x1664B0x3c7
    prev=[0x1651B0x3c7], succ=[0x16e5B0x3c7]
    =================================
    0x1665S0x3c7: v1665V3c7(0x2) = CONST 
    0x1667S0x3c7: v1667V3c7(0x0) = CONST 
    0x1669S0x3c7: v1669V3c7 = CALLER 
    0x166aS0x3c7: v166aV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x167fS0x3c7: v167fV3c7 = AND v166aV3c7(0xffffffffffffffffffffffffffffffffffffffff), v1669V3c7
    0x1680S0x3c7: v1680V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1695S0x3c7: v1695V3c7 = AND v1680V3c7(0xffffffffffffffffffffffffffffffffffffffff), v167fV3c7
    0x1697S0x3c7: MSTORE v1667V3c7(0x0), v1695V3c7
    0x1698S0x3c7: v1698V3c7(0x20) = CONST 
    0x169aS0x3c7: v169aV3c7(0x20) = ADD v1698V3c7(0x20), v1667V3c7(0x0)
    0x169dS0x3c7: MSTORE v169aV3c7(0x20), v1665V3c7(0x2)
    0x169eS0x3c7: v169eV3c7(0x20) = CONST 
    0x16a0S0x3c7: v16a0V3c7(0x40) = ADD v169eV3c7(0x20), v169aV3c7(0x20)
    0x16a1S0x3c7: v16a1V3c7(0x0) = CONST 
    0x16a3S0x3c7: v16a3V3c7 = SHA3 v16a1V3c7(0x0), v16a0V3c7(0x40)
    0x16a4S0x3c7: v16a4V3c7(0x0) = CONST 
    0x16a7S0x3c7: v16a7V3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16bcS0x3c7: v16bcV3c7 = AND v16a7V3c7(0xffffffffffffffffffffffffffffffffffffffff), v3e5
    0x16bdS0x3c7: v16bdV3c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16d2S0x3c7: v16d2V3c7 = AND v16bdV3c7(0xffffffffffffffffffffffffffffffffffffffff), v16bcV3c7
    0x16d4S0x3c7: MSTORE v16a4V3c7(0x0), v16d2V3c7
    0x16d5S0x3c7: v16d5V3c7(0x20) = CONST 
    0x16d7S0x3c7: v16d7V3c7(0x20) = ADD v16d5V3c7(0x20), v16a4V3c7(0x0)
    0x16daS0x3c7: MSTORE v16d7V3c7(0x20), v16a3V3c7
    0x16dbS0x3c7: v16dbV3c7(0x20) = CONST 
    0x16ddS0x3c7: v16ddV3c7(0x40) = ADD v16dbV3c7(0x20), v16d7V3c7(0x20)
    0x16deS0x3c7: v16deV3c7(0x0) = CONST 
    0x16e0S0x3c7: v16e0V3c7 = SHA3 v16deV3c7(0x0), v16ddV3c7(0x40)
    0x16e3S0x3c7: SSTORE v16e0V3c7, v1663_0V3c7
    0x6058S0x3c7: v6058V3c7(0x16e5) = CONST 
    0x6078S0x3c7: JUMP v6058V3c7(0x16e5)

}

function balanceOf(address)() public {
    Begin block 0x416
    prev=[], succ=[0x41d, 0x421]
    =================================
    0x417: v417 = CALLVALUE 
    0x418: v418 = ISZERO v417
    0x419: v419(0x421) = CONST 
    0x41c: JUMPI v419(0x421), v418

    Begin block 0x41d
    prev=[0x416], succ=[]
    =================================
    0x41d: v41d(0x0) = CONST 
    0x420: REVERT v41d(0x0), v41d(0x0)

    Begin block 0x421
    prev=[0x416], succ=[0xbe8]
    =================================
    0x422: v422(0x44d) = CONST 
    0x425: v425(0x4) = CONST 
    0x429: v429 = CALLDATALOAD v425(0x4)
    0x42a: v42a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x43f: v43f = AND v42a(0xffffffffffffffffffffffffffffffffffffffff), v429
    0x441: v441(0x20) = CONST 
    0x443: v443(0x24) = ADD v441(0x20), v425(0x4)
    0x449: v449(0xbe8) = CONST 
    0x44c: JUMP v449(0xbe8)

    Begin block 0xbe8
    prev=[0x421], succ=[0x44d]
    =================================
    0xbe9: vbe9(0x0) = CONST 
    0xbeb: vbeb(0x1) = CONST 
    0xbed: vbed(0x0) = CONST 
    0xbf0: vbf0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc05: vc05 = AND vbf0(0xffffffffffffffffffffffffffffffffffffffff), v43f
    0xc06: vc06(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc1b: vc1b = AND vc06(0xffffffffffffffffffffffffffffffffffffffff), vc05
    0xc1d: MSTORE vbed(0x0), vc1b
    0xc1e: vc1e(0x20) = CONST 
    0xc20: vc20(0x20) = ADD vc1e(0x20), vbed(0x0)
    0xc23: MSTORE vc20(0x20), vbeb(0x1)
    0xc24: vc24(0x20) = CONST 
    0xc26: vc26(0x40) = ADD vc24(0x20), vc20(0x20)
    0xc27: vc27(0x0) = CONST 
    0xc29: vc29 = SHA3 vc27(0x0), vc26(0x40)
    0xc2a: vc2a = SLOAD vc29
    0xc30: JUMP v422(0x44d)

    Begin block 0x44d
    prev=[0xbe8], succ=[]
    =================================
    0x44e: v44e(0x40) = CONST 
    0x450: v450 = MLOAD v44e(0x40)
    0x454: MSTORE v450, vc2a
    0x455: v455(0x20) = CONST 
    0x457: v457 = ADD v455(0x20), v450
    0x45b: v45b(0x40) = CONST 
    0x45d: v45d = MLOAD v45b(0x40)
    0x460: v460(0x20) = SUB v457, v45d
    0x462: RETURN v45d, v460(0x20)

}

function finishMinting()() public {
    Begin block 0x463
    prev=[], succ=[0x46a, 0x46e]
    =================================
    0x464: v464 = CALLVALUE 
    0x465: v465 = ISZERO v464
    0x466: v466(0x46e) = CONST 
    0x469: JUMPI v466(0x46e), v465

    Begin block 0x46a
    prev=[0x463], succ=[]
    =================================
    0x46a: v46a(0x0) = CONST 
    0x46d: REVERT v46a(0x0), v46a(0x0)

    Begin block 0x46e
    prev=[0x463], succ=[0xc31]
    =================================
    0x46f: v46f(0x476) = CONST 
    0x472: v472(0xc31) = CONST 
    0x475: JUMP v472(0xc31)

    Begin block 0xc31
    prev=[0x46e], succ=[0xc8b, 0xc8f]
    =================================
    0xc32: vc32(0x0) = CONST 
    0xc34: vc34(0x3) = CONST 
    0xc36: vc36(0x0) = CONST 
    0xc39: vc39 = SLOAD vc34(0x3)
    0xc3b: vc3b(0x100) = CONST 
    0xc3e: vc3e(0x1) = EXP vc3b(0x100), vc36(0x0)
    0xc40: vc40 = DIV vc39, vc3e(0x1)
    0xc41: vc41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc56: vc56 = AND vc41(0xffffffffffffffffffffffffffffffffffffffff), vc40
    0xc57: vc57(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc6c: vc6c = AND vc57(0xffffffffffffffffffffffffffffffffffffffff), vc56
    0xc6d: vc6d = CALLER 
    0xc6e: vc6e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc83: vc83 = AND vc6e(0xffffffffffffffffffffffffffffffffffffffff), vc6d
    0xc84: vc84 = EQ vc83, vc6c
    0xc85: vc85 = ISZERO vc84
    0xc86: vc86 = ISZERO vc85
    0xc87: vc87(0xc8f) = CONST 
    0xc8a: JUMPI vc87(0xc8f), vc86

    Begin block 0xc8b
    prev=[0xc31], succ=[]
    =================================
    0xc8b: vc8b(0x0) = CONST 
    0xc8e: REVERT vc8b(0x0), vc8b(0x0)

    Begin block 0xc8f
    prev=[0xc31], succ=[0xca7, 0xcab]
    =================================
    0xc90: vc90(0x3) = CONST 
    0xc92: vc92(0x15) = CONST 
    0xc95: vc95 = SLOAD vc90(0x3)
    0xc97: vc97(0x100) = CONST 
    0xc9a: vc9a(0x1000000000000000000000000000000000000000000) = EXP vc97(0x100), vc92(0x15)
    0xc9c: vc9c = DIV vc95, vc9a(0x1000000000000000000000000000000000000000000)
    0xc9d: vc9d(0xff) = CONST 
    0xc9f: vc9f = AND vc9d(0xff), vc9c
    0xca0: vca0 = ISZERO vc9f
    0xca1: vca1 = ISZERO vca0
    0xca2: vca2 = ISZERO vca1
    0xca3: vca3(0xcab) = CONST 
    0xca6: JUMPI vca3(0xcab), vca2

    Begin block 0xca7
    prev=[0xc8f], succ=[]
    =================================
    0xca7: vca7(0x0) = CONST 
    0xcaa: REVERT vca7(0x0), vca7(0x0)

    Begin block 0xcab
    prev=[0xc8f], succ=[0x476]
    =================================
    0xcac: vcac(0x1) = CONST 
    0xcae: vcae(0x3) = CONST 
    0xcb0: vcb0(0x15) = CONST 
    0xcb2: vcb2(0x100) = CONST 
    0xcb5: vcb5(0x1000000000000000000000000000000000000000000) = EXP vcb2(0x100), vcb0(0x15)
    0xcb7: vcb7 = SLOAD vcae(0x3)
    0xcb9: vcb9(0xff) = CONST 
    0xcbb: vcbb(0xff000000000000000000000000000000000000000000) = MUL vcb9(0xff), vcb5(0x1000000000000000000000000000000000000000000)
    0xcbc: vcbc(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT vcbb(0xff000000000000000000000000000000000000000000)
    0xcbd: vcbd = AND vcbc(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), vcb7
    0xcc0: vcc0(0x0) = ISZERO vcac(0x1)
    0xcc1: vcc1(0x1) = ISZERO vcc0(0x0)
    0xcc2: vcc2(0x1000000000000000000000000000000000000000000) = MUL vcc1(0x1), vcb5(0x1000000000000000000000000000000000000000000)
    0xcc3: vcc3 = OR vcc2(0x1000000000000000000000000000000000000000000), vcbd
    0xcc5: SSTORE vcae(0x3), vcc3
    0xcc7: vcc7(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08) = CONST 
    0xce8: vce8(0x40) = CONST 
    0xcea: vcea = MLOAD vce8(0x40)
    0xceb: vceb(0x40) = CONST 
    0xced: vced = MLOAD vceb(0x40)
    0xcf0: vcf0(0x0) = SUB vcea, vced
    0xcf2: LOG1 vced, vcf0(0x0), vcc7(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08)
    0xcf3: vcf3(0x1) = CONST 
    0xcf8: JUMP v46f(0x476)

    Begin block 0x476
    prev=[0xcab], succ=[]
    =================================
    0x477: v477(0x40) = CONST 
    0x479: v479 = MLOAD v477(0x40)
    0x47c: v47c(0x0) = ISZERO vcf3(0x1)
    0x47d: v47d(0x1) = ISZERO v47c(0x0)
    0x47e: v47e(0x0) = ISZERO v47d(0x1)
    0x47f: v47f(0x1) = ISZERO v47e(0x0)
    0x481: MSTORE v479, v47f(0x1)
    0x482: v482(0x20) = CONST 
    0x484: v484 = ADD v482(0x20), v479
    0x488: v488(0x40) = CONST 
    0x48a: v48a = MLOAD v488(0x40)
    0x48d: v48d(0x20) = SUB v484, v48a
    0x48f: RETURN v48a, v48d(0x20)

}

function pause()() public {
    Begin block 0x490
    prev=[], succ=[0x497, 0x49b]
    =================================
    0x491: v491 = CALLVALUE 
    0x492: v492 = ISZERO v491
    0x493: v493(0x49b) = CONST 
    0x496: JUMPI v493(0x49b), v492

    Begin block 0x497
    prev=[0x490], succ=[]
    =================================
    0x497: v497(0x0) = CONST 
    0x49a: REVERT v497(0x0), v497(0x0)

    Begin block 0x49b
    prev=[0x490], succ=[0xcf9]
    =================================
    0x49c: v49c(0x4a3) = CONST 
    0x49f: v49f(0xcf9) = CONST 
    0x4a2: JUMP v49f(0xcf9)

    Begin block 0xcf9
    prev=[0x49b], succ=[0xd51, 0xd55]
    =================================
    0xcfa: vcfa(0x3) = CONST 
    0xcfc: vcfc(0x0) = CONST 
    0xcff: vcff = SLOAD vcfa(0x3)
    0xd01: vd01(0x100) = CONST 
    0xd04: vd04(0x1) = EXP vd01(0x100), vcfc(0x0)
    0xd06: vd06 = DIV vcff, vd04(0x1)
    0xd07: vd07(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd1c: vd1c = AND vd07(0xffffffffffffffffffffffffffffffffffffffff), vd06
    0xd1d: vd1d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd32: vd32 = AND vd1d(0xffffffffffffffffffffffffffffffffffffffff), vd1c
    0xd33: vd33 = CALLER 
    0xd34: vd34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd49: vd49 = AND vd34(0xffffffffffffffffffffffffffffffffffffffff), vd33
    0xd4a: vd4a = EQ vd49, vd32
    0xd4b: vd4b = ISZERO vd4a
    0xd4c: vd4c = ISZERO vd4b
    0xd4d: vd4d(0xd55) = CONST 
    0xd50: JUMPI vd4d(0xd55), vd4c

    Begin block 0xd51
    prev=[0xcf9], succ=[]
    =================================
    0xd51: vd51(0x0) = CONST 
    0xd54: REVERT vd51(0x0), vd51(0x0)

    Begin block 0xd55
    prev=[0xcf9], succ=[0xd6d, 0xd71]
    =================================
    0xd56: vd56(0x3) = CONST 
    0xd58: vd58(0x14) = CONST 
    0xd5b: vd5b = SLOAD vd56(0x3)
    0xd5d: vd5d(0x100) = CONST 
    0xd60: vd60(0x10000000000000000000000000000000000000000) = EXP vd5d(0x100), vd58(0x14)
    0xd62: vd62 = DIV vd5b, vd60(0x10000000000000000000000000000000000000000)
    0xd63: vd63(0xff) = CONST 
    0xd65: vd65 = AND vd63(0xff), vd62
    0xd66: vd66 = ISZERO vd65
    0xd67: vd67 = ISZERO vd66
    0xd68: vd68 = ISZERO vd67
    0xd69: vd69(0xd71) = CONST 
    0xd6c: JUMPI vd69(0xd71), vd68

    Begin block 0xd6d
    prev=[0xd55], succ=[]
    =================================
    0xd6d: vd6d(0x0) = CONST 
    0xd70: REVERT vd6d(0x0), vd6d(0x0)

    Begin block 0xd71
    prev=[0xd55], succ=[0x4a3]
    =================================
    0xd72: vd72(0x1) = CONST 
    0xd74: vd74(0x3) = CONST 
    0xd76: vd76(0x14) = CONST 
    0xd78: vd78(0x100) = CONST 
    0xd7b: vd7b(0x10000000000000000000000000000000000000000) = EXP vd78(0x100), vd76(0x14)
    0xd7d: vd7d = SLOAD vd74(0x3)
    0xd7f: vd7f(0xff) = CONST 
    0xd81: vd81(0xff0000000000000000000000000000000000000000) = MUL vd7f(0xff), vd7b(0x10000000000000000000000000000000000000000)
    0xd82: vd82(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd81(0xff0000000000000000000000000000000000000000)
    0xd83: vd83 = AND vd82(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), vd7d
    0xd86: vd86(0x0) = ISZERO vd72(0x1)
    0xd87: vd87(0x1) = ISZERO vd86(0x0)
    0xd88: vd88(0x10000000000000000000000000000000000000000) = MUL vd87(0x1), vd7b(0x10000000000000000000000000000000000000000)
    0xd89: vd89 = OR vd88(0x10000000000000000000000000000000000000000), vd83
    0xd8b: SSTORE vd74(0x3), vd89
    0xd8d: vd8d(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625) = CONST 
    0xdae: vdae(0x40) = CONST 
    0xdb0: vdb0 = MLOAD vdae(0x40)
    0xdb1: vdb1(0x40) = CONST 
    0xdb3: vdb3 = MLOAD vdb1(0x40)
    0xdb6: vdb6(0x0) = SUB vdb0, vdb3
    0xdb8: LOG1 vdb3, vdb6(0x0), vd8d(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625)
    0xdb9: JUMP v49c(0x4a3)

    Begin block 0x4a3
    prev=[0xd71], succ=[]
    =================================
    0x4a4: STOP 

}

function owner()() public {
    Begin block 0x4a5
    prev=[], succ=[0x4ac, 0x4b0]
    =================================
    0x4a6: v4a6 = CALLVALUE 
    0x4a7: v4a7 = ISZERO v4a6
    0x4a8: v4a8(0x4b0) = CONST 
    0x4ab: JUMPI v4a8(0x4b0), v4a7

    Begin block 0x4ac
    prev=[0x4a5], succ=[]
    =================================
    0x4ac: v4ac(0x0) = CONST 
    0x4af: REVERT v4ac(0x0), v4ac(0x0)

    Begin block 0x4b0
    prev=[0x4a5], succ=[0xdba]
    =================================
    0x4b1: v4b1(0x4b8) = CONST 
    0x4b4: v4b4(0xdba) = CONST 
    0x4b7: JUMP v4b4(0xdba)

    Begin block 0xdba
    prev=[0x4b0], succ=[0x4b8]
    =================================
    0xdbb: vdbb(0x3) = CONST 
    0xdbd: vdbd(0x0) = CONST 
    0xdc0: vdc0 = SLOAD vdbb(0x3)
    0xdc2: vdc2(0x100) = CONST 
    0xdc5: vdc5(0x1) = EXP vdc2(0x100), vdbd(0x0)
    0xdc7: vdc7 = DIV vdc0, vdc5(0x1)
    0xdc8: vdc8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xddd: vddd = AND vdc8(0xffffffffffffffffffffffffffffffffffffffff), vdc7
    0xddf: JUMP v4b1(0x4b8)

    Begin block 0x4b8
    prev=[0xdba], succ=[]
    =================================
    0x4b9: v4b9(0x40) = CONST 
    0x4bb: v4bb = MLOAD v4b9(0x40)
    0x4be: v4be(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4d3: v4d3 = AND v4be(0xffffffffffffffffffffffffffffffffffffffff), vddd
    0x4d4: v4d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4e9: v4e9 = AND v4d4(0xffffffffffffffffffffffffffffffffffffffff), v4d3
    0x4eb: MSTORE v4bb, v4e9
    0x4ec: v4ec(0x20) = CONST 
    0x4ee: v4ee = ADD v4ec(0x20), v4bb
    0x4f2: v4f2(0x40) = CONST 
    0x4f4: v4f4 = MLOAD v4f2(0x40)
    0x4f7: v4f7(0x20) = SUB v4ee, v4f4
    0x4f9: RETURN v4f4, v4f7(0x20)

}

function symbol()() public {
    Begin block 0x4fa
    prev=[], succ=[0x501, 0x505]
    =================================
    0x4fb: v4fb = CALLVALUE 
    0x4fc: v4fc = ISZERO v4fb
    0x4fd: v4fd(0x505) = CONST 
    0x500: JUMPI v4fd(0x505), v4fc

    Begin block 0x501
    prev=[0x4fa], succ=[]
    =================================
    0x501: v501(0x0) = CONST 
    0x504: REVERT v501(0x0), v501(0x0)

    Begin block 0x505
    prev=[0x4fa], succ=[0xde0]
    =================================
    0x506: v506(0x50d) = CONST 
    0x509: v509(0xde0) = CONST 
    0x50c: JUMP v509(0xde0)

    Begin block 0xde0
    prev=[0x505], succ=[0x50d]
    =================================
    0xde1: vde1(0x40) = CONST 
    0xde4: vde4 = MLOAD vde1(0x40)
    0xde7: vde7 = ADD vde4, vde1(0x40)
    0xde8: vde8(0x40) = CONST 
    0xdea: MSTORE vde8(0x40), vde7
    0xdec: vdec(0x5) = CONST 
    0xdef: MSTORE vde4, vdec(0x5)
    0xdf0: vdf0(0x20) = CONST 
    0xdf2: vdf2 = ADD vdf0(0x20), vde4
    0xdf3: vdf3(0x50494c4152000000000000000000000000000000000000000000000000000000) = CONST 
    0xe15: MSTORE vdf2, vdf3(0x50494c4152000000000000000000000000000000000000000000000000000000)
    0xe18: JUMP v506(0x50d)

    Begin block 0x50d
    prev=[0xde0], succ=[0x532]
    =================================
    0x50e: v50e(0x40) = CONST 
    0x510: v510 = MLOAD v50e(0x40)
    0x513: v513(0x20) = CONST 
    0x515: v515 = ADD v513(0x20), v510
    0x518: v518(0x20) = SUB v515, v510
    0x51a: MSTORE v510, v518(0x20)
    0x51e: v51e(0x5) = MLOAD vde4
    0x520: MSTORE v515, v51e(0x5)
    0x521: v521(0x20) = CONST 
    0x523: v523 = ADD v521(0x20), v515
    0x527: v527(0x5) = MLOAD vde4
    0x529: v529(0x20) = CONST 
    0x52b: v52b = ADD v529(0x20), vde4
    0x530: v530(0x0) = CONST 
    0x4c58: v4c58(0x532) = CONST 
    0x4c78: JUMP v4c58(0x532)

    Begin block 0x532
    prev=[0x50d, 0x53b], succ=[0x54d, 0x53b]
    =================================
    0x532_0x0: v532_0 = PHI v530(0x0), v546
    0x535: v535 = LT v532_0, v527(0x5)
    0x536: v536 = ISZERO v535
    0x537: v537(0x54d) = CONST 
    0x53a: JUMPI v537(0x54d), v536

    Begin block 0x54d
    prev=[0x532], succ=[0x57a, 0x561]
    =================================
    0x556: v556 = ADD v527(0x5), v523
    0x558: v558(0x1f) = CONST 
    0x55a: v55a(0x5) = AND v558(0x1f), v527(0x5)
    0x55c: v55c(0x0) = ISZERO v55a(0x5)
    0x55d: v55d(0x57a) = CONST 
    0x560: JUMPI v55d(0x57a), v55c(0x0)

    Begin block 0x57a
    prev=[0x54d, 0x561], succ=[]
    =================================
    0x57a_0x1: v57a_1 = PHI v556, v577
    0x580: v580(0x40) = CONST 
    0x582: v582 = MLOAD v580(0x40)
    0x585: v585 = SUB v57a_1, v582
    0x587: RETURN v582, v585

    Begin block 0x561
    prev=[0x54d], succ=[0x57a]
    =================================
    0x563: v563 = SUB v556, v55a(0x5)
    0x565: v565 = MLOAD v563
    0x566: v566(0x1) = CONST 
    0x569: v569(0x20) = CONST 
    0x56b: v56b(0x1b) = SUB v569(0x20), v55a(0x5)
    0x56c: v56c(0x100) = CONST 
    0x56f: v56f(0x1000000000000000000000000000000000000000000000000000000) = EXP v56c(0x100), v56b(0x1b)
    0x570: v570(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v56f(0x1000000000000000000000000000000000000000000000000000000), v566(0x1)
    0x571: v571(0xffffffffff000000000000000000000000000000000000000000000000000000) = NOT v570(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x572: v572 = AND v571(0xffffffffff000000000000000000000000000000000000000000000000000000), v565
    0x574: MSTORE v563, v572
    0x575: v575(0x20) = CONST 
    0x577: v577 = ADD v575(0x20), v563
    0x5658: v5658(0x57a) = CONST 
    0x5678: JUMP v5658(0x57a)

    Begin block 0x53b
    prev=[0x532], succ=[0x532]
    =================================
    0x53b_0x0: v53b_0 = PHI v530(0x0), v546
    0x53d: v53d = ADD v52b, v53b_0
    0x53e: v53e = MLOAD v53d
    0x541: v541 = ADD v523, v53b_0
    0x542: MSTORE v541, v53e
    0x543: v543(0x20) = CONST 
    0x546: v546 = ADD v53b_0, v543(0x20)
    0x549: v549(0x532) = CONST 
    0x54c: JUMP v549(0x532)

}

function transfer(address,uint256)() public {
    Begin block 0x588
    prev=[], succ=[0x58f, 0x593]
    =================================
    0x589: v589 = CALLVALUE 
    0x58a: v58a = ISZERO v589
    0x58b: v58b(0x593) = CONST 
    0x58e: JUMPI v58b(0x593), v58a

    Begin block 0x58f
    prev=[0x588], succ=[]
    =================================
    0x58f: v58f(0x0) = CONST 
    0x592: REVERT v58f(0x0), v58f(0x0)

    Begin block 0x593
    prev=[0x588], succ=[0xe19B0x593]
    =================================
    0x594: v594(0x5c8) = CONST 
    0x597: v597(0x4) = CONST 
    0x59b: v59b = CALLDATALOAD v597(0x4)
    0x59c: v59c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b1: v5b1 = AND v59c(0xffffffffffffffffffffffffffffffffffffffff), v59b
    0x5b3: v5b3(0x20) = CONST 
    0x5b5: v5b5(0x24) = ADD v5b3(0x20), v597(0x4)
    0x5ba: v5ba = CALLDATALOAD v5b5(0x24)
    0x5bc: v5bc(0x20) = CONST 
    0x5be: v5be(0x44) = ADD v5bc(0x20), v5b5(0x24)
    0x5c4: v5c4(0xe19) = CONST 
    0x5c7: JUMP v5c4(0xe19)

    Begin block 0xe19B0x593
    prev=[0x593], succ=[0xe33B0x593, 0xe37B0x593]
    =================================
    0xe1aS0x593: ve1aV593(0x0) = CONST 
    0xe1cS0x593: ve1cV593(0x3) = CONST 
    0xe1eS0x593: ve1eV593(0x14) = CONST 
    0xe21S0x593: ve21V593 = SLOAD ve1cV593(0x3)
    0xe23S0x593: ve23V593(0x100) = CONST 
    0xe26S0x593: ve26V593(0x10000000000000000000000000000000000000000) = EXP ve23V593(0x100), ve1eV593(0x14)
    0xe28S0x593: ve28V593 = DIV ve21V593, ve26V593(0x10000000000000000000000000000000000000000)
    0xe29S0x593: ve29V593(0xff) = CONST 
    0xe2bS0x593: ve2bV593 = AND ve29V593(0xff), ve28V593
    0xe2cS0x593: ve2cV593 = ISZERO ve2bV593
    0xe2dS0x593: ve2dV593 = ISZERO ve2cV593
    0xe2eS0x593: ve2eV593 = ISZERO ve2dV593
    0xe2fS0x593: ve2fV593(0xe37) = CONST 
    0xe32S0x593: JUMPI ve2fV593(0xe37), ve2eV593

    Begin block 0xe33B0x593
    prev=[0xe19B0x593], succ=[]
    =================================
    0xe33S0x593: ve33V593(0x0) = CONST 
    0xe36S0x593: REVERT ve33V593(0x0), ve33V593(0x0)

    Begin block 0xe37B0x593
    prev=[0xe19B0x593], succ=[0x17d1B0x593]
    =================================
    0xe38S0x593: ve38V593(0xe41) = CONST 
    0xe3dS0x593: ve3dV593(0x17d1) = CONST 
    0xe40S0x593: JUMP ve3dV593(0x17d1)

    Begin block 0x17d1B0x593
    prev=[0xe37B0x593], succ=[0x180aB0x593, 0x180eB0x593]
    =================================
    0x17d2S0x593: v17d2V593(0x0) = CONST 
    0x17d5S0x593: v17d5V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17eaS0x593: v17eaV593(0x0) = AND v17d5V593(0xffffffffffffffffffffffffffffffffffffffff), v17d2V593(0x0)
    0x17ecS0x593: v17ecV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1801S0x593: v1801V593 = AND v17ecV593(0xffffffffffffffffffffffffffffffffffffffff), v5b1
    0x1802S0x593: v1802V593 = EQ v1801V593, v17eaV593(0x0)
    0x1803S0x593: v1803V593 = ISZERO v1802V593
    0x1804S0x593: v1804V593 = ISZERO v1803V593
    0x1805S0x593: v1805V593 = ISZERO v1804V593
    0x1806S0x593: v1806V593(0x180e) = CONST 
    0x1809S0x593: JUMPI v1806V593(0x180e), v1805V593

    Begin block 0x180aB0x593
    prev=[0x17d1B0x593], succ=[]
    =================================
    0x180aS0x593: v180aV593(0x0) = CONST 
    0x180dS0x593: REVERT v180aV593(0x0), v180aV593(0x0)

    Begin block 0x180eB0x593
    prev=[0x17d1B0x593], succ=[0x1858B0x593, 0x185cB0x593]
    =================================
    0x180fS0x593: v180fV593(0x1) = CONST 
    0x1811S0x593: v1811V593(0x0) = CONST 
    0x1813S0x593: v1813V593 = CALLER 
    0x1814S0x593: v1814V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1829S0x593: v1829V593 = AND v1814V593(0xffffffffffffffffffffffffffffffffffffffff), v1813V593
    0x182aS0x593: v182aV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x183fS0x593: v183fV593 = AND v182aV593(0xffffffffffffffffffffffffffffffffffffffff), v1829V593
    0x1841S0x593: MSTORE v1811V593(0x0), v183fV593
    0x1842S0x593: v1842V593(0x20) = CONST 
    0x1844S0x593: v1844V593(0x20) = ADD v1842V593(0x20), v1811V593(0x0)
    0x1847S0x593: MSTORE v1844V593(0x20), v180fV593(0x1)
    0x1848S0x593: v1848V593(0x20) = CONST 
    0x184aS0x593: v184aV593(0x40) = ADD v1848V593(0x20), v1844V593(0x20)
    0x184bS0x593: v184bV593(0x0) = CONST 
    0x184dS0x593: v184dV593 = SHA3 v184bV593(0x0), v184aV593(0x40)
    0x184eS0x593: v184eV593 = SLOAD v184dV593
    0x1850S0x593: v1850V593 = GT v5ba, v184eV593
    0x1851S0x593: v1851V593 = ISZERO v1850V593
    0x1852S0x593: v1852V593 = ISZERO v1851V593
    0x1853S0x593: v1853V593 = ISZERO v1852V593
    0x1854S0x593: v1854V593(0x185c) = CONST 
    0x1857S0x593: JUMPI v1854V593(0x185c), v1853V593

    Begin block 0x1858B0x593
    prev=[0x180eB0x593], succ=[]
    =================================
    0x1858S0x593: v1858V593(0x0) = CONST 
    0x185bS0x593: REVERT v1858V593(0x0), v1858V593(0x0)

    Begin block 0x185cB0x593
    prev=[0x180eB0x593], succ=[0x18aeB0x593]
    =================================
    0x185dS0x593: v185dV593(0x18ae) = CONST 
    0x1861S0x593: v1861V593(0x1) = CONST 
    0x1863S0x593: v1863V593(0x0) = CONST 
    0x1865S0x593: v1865V593 = CALLER 
    0x1866S0x593: v1866V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x187bS0x593: v187bV593 = AND v1866V593(0xffffffffffffffffffffffffffffffffffffffff), v1865V593
    0x187cS0x593: v187cV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1891S0x593: v1891V593 = AND v187cV593(0xffffffffffffffffffffffffffffffffffffffff), v187bV593
    0x1893S0x593: MSTORE v1863V593(0x0), v1891V593
    0x1894S0x593: v1894V593(0x20) = CONST 
    0x1896S0x593: v1896V593(0x20) = ADD v1894V593(0x20), v1863V593(0x0)
    0x1899S0x593: MSTORE v1896V593(0x20), v1861V593(0x1)
    0x189aS0x593: v189aV593(0x20) = CONST 
    0x189cS0x593: v189cV593(0x40) = ADD v189aV593(0x20), v1896V593(0x20)
    0x189dS0x593: v189dV593(0x0) = CONST 
    0x189fS0x593: v189fV593 = SHA3 v189dV593(0x0), v189cV593(0x40)
    0x18a0S0x593: v18a0V593 = SLOAD v189fV593
    0x18a1S0x593: v18a1V593(0x1527) = CONST 
    0x18a7S0x593: v18a7V593(0xffffffff) = CONST 
    0x18acS0x593: v18acV593(0x1527) = AND v18a7V593(0xffffffff), v18a1V593(0x1527)
    0x18adS0x593: v18ad_0V593 = CALLPRIVATE v18acV593(0x1527), v5ba, v18a0V593, v185dV593(0x18ae)

    Begin block 0x18aeB0x593
    prev=[0x185cB0x593], succ=[0x1943B0x593]
    =================================
    0x18afS0x593: v18afV593(0x1) = CONST 
    0x18b1S0x593: v18b1V593(0x0) = CONST 
    0x18b3S0x593: v18b3V593 = CALLER 
    0x18b4S0x593: v18b4V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18c9S0x593: v18c9V593 = AND v18b4V593(0xffffffffffffffffffffffffffffffffffffffff), v18b3V593
    0x18caS0x593: v18caV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18dfS0x593: v18dfV593 = AND v18caV593(0xffffffffffffffffffffffffffffffffffffffff), v18c9V593
    0x18e1S0x593: MSTORE v18b1V593(0x0), v18dfV593
    0x18e2S0x593: v18e2V593(0x20) = CONST 
    0x18e4S0x593: v18e4V593(0x20) = ADD v18e2V593(0x20), v18b1V593(0x0)
    0x18e7S0x593: MSTORE v18e4V593(0x20), v18afV593(0x1)
    0x18e8S0x593: v18e8V593(0x20) = CONST 
    0x18eaS0x593: v18eaV593(0x40) = ADD v18e8V593(0x20), v18e4V593(0x20)
    0x18ebS0x593: v18ebV593(0x0) = CONST 
    0x18edS0x593: v18edV593 = SHA3 v18ebV593(0x0), v18eaV593(0x40)
    0x18f0S0x593: SSTORE v18edV593, v18ad_0V593
    0x18f2S0x593: v18f2V593(0x1943) = CONST 
    0x18f6S0x593: v18f6V593(0x1) = CONST 
    0x18f8S0x593: v18f8V593(0x0) = CONST 
    0x18fbS0x593: v18fbV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1910S0x593: v1910V593 = AND v18fbV593(0xffffffffffffffffffffffffffffffffffffffff), v5b1
    0x1911S0x593: v1911V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1926S0x593: v1926V593 = AND v1911V593(0xffffffffffffffffffffffffffffffffffffffff), v1910V593
    0x1928S0x593: MSTORE v18f8V593(0x0), v1926V593
    0x1929S0x593: v1929V593(0x20) = CONST 
    0x192bS0x593: v192bV593(0x20) = ADD v1929V593(0x20), v18f8V593(0x0)
    0x192eS0x593: MSTORE v192bV593(0x20), v18f6V593(0x1)
    0x192fS0x593: v192fV593(0x20) = CONST 
    0x1931S0x593: v1931V593(0x40) = ADD v192fV593(0x20), v192bV593(0x20)
    0x1932S0x593: v1932V593(0x0) = CONST 
    0x1934S0x593: v1934V593 = SHA3 v1932V593(0x0), v1931V593(0x40)
    0x1935S0x593: v1935V593 = SLOAD v1934V593
    0x1936S0x593: v1936V593(0x1509) = CONST 
    0x193cS0x593: v193cV593(0xffffffff) = CONST 
    0x1941S0x593: v1941V593(0x1509) = AND v193cV593(0xffffffff), v1936V593(0x1509)
    0x1942S0x593: v1942_0V593 = CALLPRIVATE v1941V593(0x1509), v5ba, v1935V593, v18f2V593(0x1943)

    Begin block 0x1943B0x593
    prev=[0x18aeB0x593], succ=[0xe41B0x593]
    =================================
    0x1944S0x593: v1944V593(0x1) = CONST 
    0x1946S0x593: v1946V593(0x0) = CONST 
    0x1949S0x593: v1949V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x195eS0x593: v195eV593 = AND v1949V593(0xffffffffffffffffffffffffffffffffffffffff), v5b1
    0x195fS0x593: v195fV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1974S0x593: v1974V593 = AND v195fV593(0xffffffffffffffffffffffffffffffffffffffff), v195eV593
    0x1976S0x593: MSTORE v1946V593(0x0), v1974V593
    0x1977S0x593: v1977V593(0x20) = CONST 
    0x1979S0x593: v1979V593(0x20) = ADD v1977V593(0x20), v1946V593(0x0)
    0x197cS0x593: MSTORE v1979V593(0x20), v1944V593(0x1)
    0x197dS0x593: v197dV593(0x20) = CONST 
    0x197fS0x593: v197fV593(0x40) = ADD v197dV593(0x20), v1979V593(0x20)
    0x1980S0x593: v1980V593(0x0) = CONST 
    0x1982S0x593: v1982V593 = SHA3 v1980V593(0x0), v197fV593(0x40)
    0x1985S0x593: SSTORE v1982V593, v1942_0V593
    0x1988S0x593: v1988V593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x199dS0x593: v199dV593 = AND v1988V593(0xffffffffffffffffffffffffffffffffffffffff), v5b1
    0x199eS0x593: v199eV593 = CALLER 
    0x199fS0x593: v199fV593(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19b4S0x593: v19b4V593 = AND v199fV593(0xffffffffffffffffffffffffffffffffffffffff), v199eV593
    0x19b5S0x593: v19b5V593(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x19d7S0x593: v19d7V593(0x40) = CONST 
    0x19d9S0x593: v19d9V593 = MLOAD v19d7V593(0x40)
    0x19ddS0x593: MSTORE v19d9V593, v5ba
    0x19deS0x593: v19deV593(0x20) = CONST 
    0x19e0S0x593: v19e0V593 = ADD v19deV593(0x20), v19d9V593
    0x19e4S0x593: v19e4V593(0x40) = CONST 
    0x19e6S0x593: v19e6V593 = MLOAD v19e4V593(0x40)
    0x19e9S0x593: v19e9V593(0x20) = SUB v19e0V593, v19e6V593
    0x19ebS0x593: LOG3 v19e6V593, v19e9V593(0x20), v19b5V593(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v19b4V593, v199dV593
    0x19ecS0x593: v19ecV593(0x1) = CONST 
    0x19f4S0x593: JUMP ve38V593(0xe41)

    Begin block 0xe41B0x593
    prev=[0x1943B0x593], succ=[0x5c8]
    =================================
    0xe48S0x593: JUMP v594(0x5c8)

    Begin block 0x5c8
    prev=[0xe41B0x593], succ=[]
    =================================
    0x5c9: v5c9(0x40) = CONST 
    0x5cb: v5cb = MLOAD v5c9(0x40)
    0x5ce: v5ce(0x0) = ISZERO v19ecV593(0x1)
    0x5cf: v5cf(0x1) = ISZERO v5ce(0x0)
    0x5d0: v5d0(0x0) = ISZERO v5cf(0x1)
    0x5d1: v5d1(0x1) = ISZERO v5d0(0x0)
    0x5d3: MSTORE v5cb, v5d1(0x1)
    0x5d4: v5d4(0x20) = CONST 
    0x5d6: v5d6 = ADD v5d4(0x20), v5cb
    0x5da: v5da(0x40) = CONST 
    0x5dc: v5dc = MLOAD v5da(0x40)
    0x5df: v5df(0x20) = SUB v5d6, v5dc
    0x5e1: RETURN v5dc, v5df(0x20)

}

function increaseApproval(address,uint256)() public {
    Begin block 0x5e2
    prev=[], succ=[0x5e9, 0x5ed]
    =================================
    0x5e3: v5e3 = CALLVALUE 
    0x5e4: v5e4 = ISZERO v5e3
    0x5e5: v5e5(0x5ed) = CONST 
    0x5e8: JUMPI v5e5(0x5ed), v5e4

    Begin block 0x5e9
    prev=[0x5e2], succ=[]
    =================================
    0x5e9: v5e9(0x0) = CONST 
    0x5ec: REVERT v5e9(0x0), v5e9(0x0)

    Begin block 0x5ed
    prev=[0x5e2], succ=[0xe49B0x5ed]
    =================================
    0x5ee: v5ee(0x622) = CONST 
    0x5f1: v5f1(0x4) = CONST 
    0x5f5: v5f5 = CALLDATALOAD v5f1(0x4)
    0x5f6: v5f6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x60b: v60b = AND v5f6(0xffffffffffffffffffffffffffffffffffffffff), v5f5
    0x60d: v60d(0x20) = CONST 
    0x60f: v60f(0x24) = ADD v60d(0x20), v5f1(0x4)
    0x614: v614 = CALLDATALOAD v60f(0x24)
    0x616: v616(0x20) = CONST 
    0x618: v618(0x44) = ADD v616(0x20), v60f(0x24)
    0x61e: v61e(0xe49) = CONST 
    0x621: JUMP v61e(0xe49)

    Begin block 0xe49B0x5ed
    prev=[0x5ed], succ=[0xe63B0x5ed, 0xe67B0x5ed]
    =================================
    0xe4aS0x5ed: ve4aV5ed(0x0) = CONST 
    0xe4cS0x5ed: ve4cV5ed(0x3) = CONST 
    0xe4eS0x5ed: ve4eV5ed(0x14) = CONST 
    0xe51S0x5ed: ve51V5ed = SLOAD ve4cV5ed(0x3)
    0xe53S0x5ed: ve53V5ed(0x100) = CONST 
    0xe56S0x5ed: ve56V5ed(0x10000000000000000000000000000000000000000) = EXP ve53V5ed(0x100), ve4eV5ed(0x14)
    0xe58S0x5ed: ve58V5ed = DIV ve51V5ed, ve56V5ed(0x10000000000000000000000000000000000000000)
    0xe59S0x5ed: ve59V5ed(0xff) = CONST 
    0xe5bS0x5ed: ve5bV5ed = AND ve59V5ed(0xff), ve58V5ed
    0xe5cS0x5ed: ve5cV5ed = ISZERO ve5bV5ed
    0xe5dS0x5ed: ve5dV5ed = ISZERO ve5cV5ed
    0xe5eS0x5ed: ve5eV5ed = ISZERO ve5dV5ed
    0xe5fS0x5ed: ve5fV5ed(0xe67) = CONST 
    0xe62S0x5ed: JUMPI ve5fV5ed(0xe67), ve5eV5ed

    Begin block 0xe63B0x5ed
    prev=[0xe49B0x5ed], succ=[]
    =================================
    0xe63S0x5ed: ve63V5ed(0x0) = CONST 
    0xe66S0x5ed: REVERT ve63V5ed(0x0), ve63V5ed(0x0)

    Begin block 0xe67B0x5ed
    prev=[0xe49B0x5ed], succ=[0x19f5B0x5ed]
    =================================
    0xe68S0x5ed: ve68V5ed(0xe71) = CONST 
    0xe6dS0x5ed: ve6dV5ed(0x19f5) = CONST 
    0xe70S0x5ed: JUMP ve6dV5ed(0x19f5)

    Begin block 0x19f5B0x5ed
    prev=[0xe67B0x5ed], succ=[0x1a86B0x5ed]
    =================================
    0x19f6S0x5ed: v19f6V5ed(0x0) = CONST 
    0x19f8S0x5ed: v19f8V5ed(0x1a86) = CONST 
    0x19fcS0x5ed: v19fcV5ed(0x2) = CONST 
    0x19feS0x5ed: v19feV5ed(0x0) = CONST 
    0x1a00S0x5ed: v1a00V5ed = CALLER 
    0x1a01S0x5ed: v1a01V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a16S0x5ed: v1a16V5ed = AND v1a01V5ed(0xffffffffffffffffffffffffffffffffffffffff), v1a00V5ed
    0x1a17S0x5ed: v1a17V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a2cS0x5ed: v1a2cV5ed = AND v1a17V5ed(0xffffffffffffffffffffffffffffffffffffffff), v1a16V5ed
    0x1a2eS0x5ed: MSTORE v19feV5ed(0x0), v1a2cV5ed
    0x1a2fS0x5ed: v1a2fV5ed(0x20) = CONST 
    0x1a31S0x5ed: v1a31V5ed(0x20) = ADD v1a2fV5ed(0x20), v19feV5ed(0x0)
    0x1a34S0x5ed: MSTORE v1a31V5ed(0x20), v19fcV5ed(0x2)
    0x1a35S0x5ed: v1a35V5ed(0x20) = CONST 
    0x1a37S0x5ed: v1a37V5ed(0x40) = ADD v1a35V5ed(0x20), v1a31V5ed(0x20)
    0x1a38S0x5ed: v1a38V5ed(0x0) = CONST 
    0x1a3aS0x5ed: v1a3aV5ed = SHA3 v1a38V5ed(0x0), v1a37V5ed(0x40)
    0x1a3bS0x5ed: v1a3bV5ed(0x0) = CONST 
    0x1a3eS0x5ed: v1a3eV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a53S0x5ed: v1a53V5ed = AND v1a3eV5ed(0xffffffffffffffffffffffffffffffffffffffff), v60b
    0x1a54S0x5ed: v1a54V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a69S0x5ed: v1a69V5ed = AND v1a54V5ed(0xffffffffffffffffffffffffffffffffffffffff), v1a53V5ed
    0x1a6bS0x5ed: MSTORE v1a3bV5ed(0x0), v1a69V5ed
    0x1a6cS0x5ed: v1a6cV5ed(0x20) = CONST 
    0x1a6eS0x5ed: v1a6eV5ed(0x20) = ADD v1a6cV5ed(0x20), v1a3bV5ed(0x0)
    0x1a71S0x5ed: MSTORE v1a6eV5ed(0x20), v1a3aV5ed
    0x1a72S0x5ed: v1a72V5ed(0x20) = CONST 
    0x1a74S0x5ed: v1a74V5ed(0x40) = ADD v1a72V5ed(0x20), v1a6eV5ed(0x20)
    0x1a75S0x5ed: v1a75V5ed(0x0) = CONST 
    0x1a77S0x5ed: v1a77V5ed = SHA3 v1a75V5ed(0x0), v1a74V5ed(0x40)
    0x1a78S0x5ed: v1a78V5ed = SLOAD v1a77V5ed
    0x1a79S0x5ed: v1a79V5ed(0x1509) = CONST 
    0x1a7fS0x5ed: v1a7fV5ed(0xffffffff) = CONST 
    0x1a84S0x5ed: v1a84V5ed(0x1509) = AND v1a7fV5ed(0xffffffff), v1a79V5ed(0x1509)
    0x1a85S0x5ed: v1a85_0V5ed = CALLPRIVATE v1a84V5ed(0x1509), v614, v1a78V5ed, v19f8V5ed(0x1a86)

    Begin block 0x1a86B0x5ed
    prev=[0x19f5B0x5ed], succ=[0xe71B0x5ed]
    =================================
    0x1a87S0x5ed: v1a87V5ed(0x2) = CONST 
    0x1a89S0x5ed: v1a89V5ed(0x0) = CONST 
    0x1a8bS0x5ed: v1a8bV5ed = CALLER 
    0x1a8cS0x5ed: v1a8cV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1aa1S0x5ed: v1aa1V5ed = AND v1a8cV5ed(0xffffffffffffffffffffffffffffffffffffffff), v1a8bV5ed
    0x1aa2S0x5ed: v1aa2V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ab7S0x5ed: v1ab7V5ed = AND v1aa2V5ed(0xffffffffffffffffffffffffffffffffffffffff), v1aa1V5ed
    0x1ab9S0x5ed: MSTORE v1a89V5ed(0x0), v1ab7V5ed
    0x1abaS0x5ed: v1abaV5ed(0x20) = CONST 
    0x1abcS0x5ed: v1abcV5ed(0x20) = ADD v1abaV5ed(0x20), v1a89V5ed(0x0)
    0x1abfS0x5ed: MSTORE v1abcV5ed(0x20), v1a87V5ed(0x2)
    0x1ac0S0x5ed: v1ac0V5ed(0x20) = CONST 
    0x1ac2S0x5ed: v1ac2V5ed(0x40) = ADD v1ac0V5ed(0x20), v1abcV5ed(0x20)
    0x1ac3S0x5ed: v1ac3V5ed(0x0) = CONST 
    0x1ac5S0x5ed: v1ac5V5ed = SHA3 v1ac3V5ed(0x0), v1ac2V5ed(0x40)
    0x1ac6S0x5ed: v1ac6V5ed(0x0) = CONST 
    0x1ac9S0x5ed: v1ac9V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1adeS0x5ed: v1adeV5ed = AND v1ac9V5ed(0xffffffffffffffffffffffffffffffffffffffff), v60b
    0x1adfS0x5ed: v1adfV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1af4S0x5ed: v1af4V5ed = AND v1adfV5ed(0xffffffffffffffffffffffffffffffffffffffff), v1adeV5ed
    0x1af6S0x5ed: MSTORE v1ac6V5ed(0x0), v1af4V5ed
    0x1af7S0x5ed: v1af7V5ed(0x20) = CONST 
    0x1af9S0x5ed: v1af9V5ed(0x20) = ADD v1af7V5ed(0x20), v1ac6V5ed(0x0)
    0x1afcS0x5ed: MSTORE v1af9V5ed(0x20), v1ac5V5ed
    0x1afdS0x5ed: v1afdV5ed(0x20) = CONST 
    0x1affS0x5ed: v1affV5ed(0x40) = ADD v1afdV5ed(0x20), v1af9V5ed(0x20)
    0x1b00S0x5ed: v1b00V5ed(0x0) = CONST 
    0x1b02S0x5ed: v1b02V5ed = SHA3 v1b00V5ed(0x0), v1affV5ed(0x40)
    0x1b05S0x5ed: SSTORE v1b02V5ed, v1a85_0V5ed
    0x1b08S0x5ed: v1b08V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b1dS0x5ed: v1b1dV5ed = AND v1b08V5ed(0xffffffffffffffffffffffffffffffffffffffff), v60b
    0x1b1eS0x5ed: v1b1eV5ed = CALLER 
    0x1b1fS0x5ed: v1b1fV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b34S0x5ed: v1b34V5ed = AND v1b1fV5ed(0xffffffffffffffffffffffffffffffffffffffff), v1b1eV5ed
    0x1b35S0x5ed: v1b35V5ed(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x1b56S0x5ed: v1b56V5ed(0x2) = CONST 
    0x1b58S0x5ed: v1b58V5ed(0x0) = CONST 
    0x1b5aS0x5ed: v1b5aV5ed = CALLER 
    0x1b5bS0x5ed: v1b5bV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b70S0x5ed: v1b70V5ed = AND v1b5bV5ed(0xffffffffffffffffffffffffffffffffffffffff), v1b5aV5ed
    0x1b71S0x5ed: v1b71V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b86S0x5ed: v1b86V5ed = AND v1b71V5ed(0xffffffffffffffffffffffffffffffffffffffff), v1b70V5ed
    0x1b88S0x5ed: MSTORE v1b58V5ed(0x0), v1b86V5ed
    0x1b89S0x5ed: v1b89V5ed(0x20) = CONST 
    0x1b8bS0x5ed: v1b8bV5ed(0x20) = ADD v1b89V5ed(0x20), v1b58V5ed(0x0)
    0x1b8eS0x5ed: MSTORE v1b8bV5ed(0x20), v1b56V5ed(0x2)
    0x1b8fS0x5ed: v1b8fV5ed(0x20) = CONST 
    0x1b91S0x5ed: v1b91V5ed(0x40) = ADD v1b8fV5ed(0x20), v1b8bV5ed(0x20)
    0x1b92S0x5ed: v1b92V5ed(0x0) = CONST 
    0x1b94S0x5ed: v1b94V5ed = SHA3 v1b92V5ed(0x0), v1b91V5ed(0x40)
    0x1b95S0x5ed: v1b95V5ed(0x0) = CONST 
    0x1b98S0x5ed: v1b98V5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1badS0x5ed: v1badV5ed = AND v1b98V5ed(0xffffffffffffffffffffffffffffffffffffffff), v60b
    0x1baeS0x5ed: v1baeV5ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bc3S0x5ed: v1bc3V5ed = AND v1baeV5ed(0xffffffffffffffffffffffffffffffffffffffff), v1badV5ed
    0x1bc5S0x5ed: MSTORE v1b95V5ed(0x0), v1bc3V5ed
    0x1bc6S0x5ed: v1bc6V5ed(0x20) = CONST 
    0x1bc8S0x5ed: v1bc8V5ed(0x20) = ADD v1bc6V5ed(0x20), v1b95V5ed(0x0)
    0x1bcbS0x5ed: MSTORE v1bc8V5ed(0x20), v1b94V5ed
    0x1bccS0x5ed: v1bccV5ed(0x20) = CONST 
    0x1bceS0x5ed: v1bceV5ed(0x40) = ADD v1bccV5ed(0x20), v1bc8V5ed(0x20)
    0x1bcfS0x5ed: v1bcfV5ed(0x0) = CONST 
    0x1bd1S0x5ed: v1bd1V5ed = SHA3 v1bcfV5ed(0x0), v1bceV5ed(0x40)
    0x1bd2S0x5ed: v1bd2V5ed = SLOAD v1bd1V5ed
    0x1bd3S0x5ed: v1bd3V5ed(0x40) = CONST 
    0x1bd5S0x5ed: v1bd5V5ed = MLOAD v1bd3V5ed(0x40)
    0x1bd9S0x5ed: MSTORE v1bd5V5ed, v1bd2V5ed
    0x1bdaS0x5ed: v1bdaV5ed(0x20) = CONST 
    0x1bdcS0x5ed: v1bdcV5ed = ADD v1bdaV5ed(0x20), v1bd5V5ed
    0x1be0S0x5ed: v1be0V5ed(0x40) = CONST 
    0x1be2S0x5ed: v1be2V5ed = MLOAD v1be0V5ed(0x40)
    0x1be5S0x5ed: v1be5V5ed(0x20) = SUB v1bdcV5ed, v1be2V5ed
    0x1be7S0x5ed: LOG3 v1be2V5ed, v1be5V5ed(0x20), v1b35V5ed(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v1b34V5ed, v1b1dV5ed
    0x1be8S0x5ed: v1be8V5ed(0x1) = CONST 
    0x1bf0S0x5ed: JUMP ve68V5ed(0xe71)

    Begin block 0xe71B0x5ed
    prev=[0x1a86B0x5ed], succ=[0x622]
    =================================
    0xe78S0x5ed: JUMP v5ee(0x622)

    Begin block 0x622
    prev=[0xe71B0x5ed], succ=[]
    =================================
    0x623: v623(0x40) = CONST 
    0x625: v625 = MLOAD v623(0x40)
    0x628: v628(0x0) = ISZERO v1be8V5ed(0x1)
    0x629: v629(0x1) = ISZERO v628(0x0)
    0x62a: v62a(0x0) = ISZERO v629(0x1)
    0x62b: v62b(0x1) = ISZERO v62a(0x0)
    0x62d: MSTORE v625, v62b(0x1)
    0x62e: v62e(0x20) = CONST 
    0x630: v630 = ADD v62e(0x20), v625
    0x634: v634(0x40) = CONST 
    0x636: v636 = MLOAD v634(0x40)
    0x639: v639(0x20) = SUB v630, v636
    0x63b: RETURN v636, v639(0x20)

}

function allowance(address,address)() public {
    Begin block 0x63c
    prev=[], succ=[0x643, 0x647]
    =================================
    0x63d: v63d = CALLVALUE 
    0x63e: v63e = ISZERO v63d
    0x63f: v63f(0x647) = CONST 
    0x642: JUMPI v63f(0x647), v63e

    Begin block 0x643
    prev=[0x63c], succ=[]
    =================================
    0x643: v643(0x0) = CONST 
    0x646: REVERT v643(0x0), v643(0x0)

    Begin block 0x647
    prev=[0x63c], succ=[0xe79]
    =================================
    0x648: v648(0x692) = CONST 
    0x64b: v64b(0x4) = CONST 
    0x64f: v64f = CALLDATALOAD v64b(0x4)
    0x650: v650(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x665: v665 = AND v650(0xffffffffffffffffffffffffffffffffffffffff), v64f
    0x667: v667(0x20) = CONST 
    0x669: v669(0x24) = ADD v667(0x20), v64b(0x4)
    0x66e: v66e = CALLDATALOAD v669(0x24)
    0x66f: v66f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x684: v684 = AND v66f(0xffffffffffffffffffffffffffffffffffffffff), v66e
    0x686: v686(0x20) = CONST 
    0x688: v688(0x44) = ADD v686(0x20), v669(0x24)
    0x68e: v68e(0xe79) = CONST 
    0x691: JUMP v68e(0xe79)

    Begin block 0xe79
    prev=[0x647], succ=[0x692]
    =================================
    0xe7a: ve7a(0x0) = CONST 
    0xe7c: ve7c(0x2) = CONST 
    0xe7e: ve7e(0x0) = CONST 
    0xe81: ve81(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe96: ve96 = AND ve81(0xffffffffffffffffffffffffffffffffffffffff), v665
    0xe97: ve97(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeac: veac = AND ve97(0xffffffffffffffffffffffffffffffffffffffff), ve96
    0xeae: MSTORE ve7e(0x0), veac
    0xeaf: veaf(0x20) = CONST 
    0xeb1: veb1(0x20) = ADD veaf(0x20), ve7e(0x0)
    0xeb4: MSTORE veb1(0x20), ve7c(0x2)
    0xeb5: veb5(0x20) = CONST 
    0xeb7: veb7(0x40) = ADD veb5(0x20), veb1(0x20)
    0xeb8: veb8(0x0) = CONST 
    0xeba: veba = SHA3 veb8(0x0), veb7(0x40)
    0xebb: vebb(0x0) = CONST 
    0xebe: vebe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xed3: ved3 = AND vebe(0xffffffffffffffffffffffffffffffffffffffff), v684
    0xed4: ved4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xee9: vee9 = AND ved4(0xffffffffffffffffffffffffffffffffffffffff), ved3
    0xeeb: MSTORE vebb(0x0), vee9
    0xeec: veec(0x20) = CONST 
    0xeee: veee(0x20) = ADD veec(0x20), vebb(0x0)
    0xef1: MSTORE veee(0x20), veba
    0xef2: vef2(0x20) = CONST 
    0xef4: vef4(0x40) = ADD vef2(0x20), veee(0x20)
    0xef5: vef5(0x0) = CONST 
    0xef7: vef7 = SHA3 vef5(0x0), vef4(0x40)
    0xef8: vef8 = SLOAD vef7
    0xeff: JUMP v648(0x692)

    Begin block 0x692
    prev=[0xe79], succ=[]
    =================================
    0x693: v693(0x40) = CONST 
    0x695: v695 = MLOAD v693(0x40)
    0x699: MSTORE v695, vef8
    0x69a: v69a(0x20) = CONST 
    0x69c: v69c = ADD v69a(0x20), v695
    0x6a0: v6a0(0x40) = CONST 
    0x6a2: v6a2 = MLOAD v6a0(0x40)
    0x6a5: v6a5(0x20) = SUB v69c, v6a2
    0x6a7: RETURN v6a2, v6a5(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x6a8
    prev=[], succ=[0x6af, 0x6b3]
    =================================
    0x6a9: v6a9 = CALLVALUE 
    0x6aa: v6aa = ISZERO v6a9
    0x6ab: v6ab(0x6b3) = CONST 
    0x6ae: JUMPI v6ab(0x6b3), v6aa

    Begin block 0x6af
    prev=[0x6a8], succ=[]
    =================================
    0x6af: v6af(0x0) = CONST 
    0x6b2: REVERT v6af(0x0), v6af(0x0)

    Begin block 0x6b3
    prev=[0x6a8], succ=[0xf00]
    =================================
    0x6b4: v6b4(0x6df) = CONST 
    0x6b7: v6b7(0x4) = CONST 
    0x6bb: v6bb = CALLDATALOAD v6b7(0x4)
    0x6bc: v6bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6d1: v6d1 = AND v6bc(0xffffffffffffffffffffffffffffffffffffffff), v6bb
    0x6d3: v6d3(0x20) = CONST 
    0x6d5: v6d5(0x24) = ADD v6d3(0x20), v6b7(0x4)
    0x6db: v6db(0xf00) = CONST 
    0x6de: JUMP v6db(0xf00)

    Begin block 0xf00
    prev=[0x6b3], succ=[0xf58, 0xf5c]
    =================================
    0xf01: vf01(0x3) = CONST 
    0xf03: vf03(0x0) = CONST 
    0xf06: vf06 = SLOAD vf01(0x3)
    0xf08: vf08(0x100) = CONST 
    0xf0b: vf0b(0x1) = EXP vf08(0x100), vf03(0x0)
    0xf0d: vf0d = DIV vf06, vf0b(0x1)
    0xf0e: vf0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf23: vf23 = AND vf0e(0xffffffffffffffffffffffffffffffffffffffff), vf0d
    0xf24: vf24(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf39: vf39 = AND vf24(0xffffffffffffffffffffffffffffffffffffffff), vf23
    0xf3a: vf3a = CALLER 
    0xf3b: vf3b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf50: vf50 = AND vf3b(0xffffffffffffffffffffffffffffffffffffffff), vf3a
    0xf51: vf51 = EQ vf50, vf39
    0xf52: vf52 = ISZERO vf51
    0xf53: vf53 = ISZERO vf52
    0xf54: vf54(0xf5c) = CONST 
    0xf57: JUMPI vf54(0xf5c), vf53

    Begin block 0xf58
    prev=[0xf00], succ=[]
    =================================
    0xf58: vf58(0x0) = CONST 
    0xf5b: REVERT vf58(0x0), vf58(0x0)

    Begin block 0xf5c
    prev=[0xf00], succ=[0xf94, 0xf98]
    =================================
    0xf5d: vf5d(0x0) = CONST 
    0xf5f: vf5f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf74: vf74(0x0) = AND vf5f(0xffffffffffffffffffffffffffffffffffffffff), vf5d(0x0)
    0xf76: vf76(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf8b: vf8b = AND vf76(0xffffffffffffffffffffffffffffffffffffffff), v6d1
    0xf8c: vf8c = EQ vf8b, vf74(0x0)
    0xf8d: vf8d = ISZERO vf8c
    0xf8e: vf8e = ISZERO vf8d
    0xf8f: vf8f = ISZERO vf8e
    0xf90: vf90(0xf98) = CONST 
    0xf93: JUMPI vf90(0xf98), vf8f

    Begin block 0xf94
    prev=[0xf5c], succ=[]
    =================================
    0xf94: vf94(0x0) = CONST 
    0xf97: REVERT vf94(0x0), vf94(0x0)

    Begin block 0xf98
    prev=[0xf5c], succ=[0x6df]
    =================================
    0xf9a: vf9a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfaf: vfaf = AND vf9a(0xffffffffffffffffffffffffffffffffffffffff), v6d1
    0xfb0: vfb0(0x3) = CONST 
    0xfb2: vfb2(0x0) = CONST 
    0xfb5: vfb5 = SLOAD vfb0(0x3)
    0xfb7: vfb7(0x100) = CONST 
    0xfba: vfba(0x1) = EXP vfb7(0x100), vfb2(0x0)
    0xfbc: vfbc = DIV vfb5, vfba(0x1)
    0xfbd: vfbd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfd2: vfd2 = AND vfbd(0xffffffffffffffffffffffffffffffffffffffff), vfbc
    0xfd3: vfd3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfe8: vfe8 = AND vfd3(0xffffffffffffffffffffffffffffffffffffffff), vfd2
    0xfe9: vfe9(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x100a: v100a(0x40) = CONST 
    0x100c: v100c = MLOAD v100a(0x40)
    0x100d: v100d(0x40) = CONST 
    0x100f: v100f = MLOAD v100d(0x40)
    0x1012: v1012(0x0) = SUB v100c, v100f
    0x1014: LOG3 v100f, v1012(0x0), vfe9(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vfe8, vfaf
    0x1016: v1016(0x3) = CONST 
    0x1018: v1018(0x0) = CONST 
    0x101a: v101a(0x100) = CONST 
    0x101d: v101d(0x1) = EXP v101a(0x100), v1018(0x0)
    0x101f: v101f = SLOAD v1016(0x3)
    0x1021: v1021(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1036: v1036(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1021(0xffffffffffffffffffffffffffffffffffffffff), v101d(0x1)
    0x1037: v1037(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1036(0xffffffffffffffffffffffffffffffffffffffff)
    0x1038: v1038 = AND v1037(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v101f
    0x103b: v103b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1050: v1050 = AND v103b(0xffffffffffffffffffffffffffffffffffffffff), v6d1
    0x1051: v1051 = MUL v1050, v101d(0x1)
    0x1052: v1052 = OR v1051, v1038
    0x1054: SSTORE v1016(0x3), v1052
    0x1057: JUMP v6b4(0x6df)

    Begin block 0x6df
    prev=[0xf98], succ=[]
    =================================
    0x6e0: STOP 

}

