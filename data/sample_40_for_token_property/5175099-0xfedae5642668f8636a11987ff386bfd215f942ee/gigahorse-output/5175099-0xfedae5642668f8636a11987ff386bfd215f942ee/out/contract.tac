function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x28632]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x1c832: v1c832(0x28632) = CONST 
    0x1c852: JUMPI v1c832(0x28632), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x29032]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x6fdde03) = CONST 
    0x3b: v3b = EQ v34, v35(0x6fdde03)
    0x1d232: v1d232(0x29032) = CONST 
    0x1d252: JUMPI v1d232(0x29032), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x29a32, 0x4b]
    =================================
    0x41: v41(0x95ea7b3) = CONST 
    0x46: v46 = EQ v41(0x95ea7b3), v34
    0x1dc32: v1dc32(0x29a32) = CONST 
    0x1dc52: JUMPI v1dc32(0x29a32), v46

    Begin block 0x29a32
    prev=[0x40], succ=[]
    =================================
    0x29a52: v29a52(0x18a) = CONST 
    0x29a72: CALLPRIVATE v29a52(0x18a)

    Begin block 0x4b
    prev=[0x40], succ=[0x2a432, 0x56]
    =================================
    0x4c: v4c(0x18160ddd) = CONST 
    0x51: v51 = EQ v4c(0x18160ddd), v34
    0x1e632: v1e632(0x2a432) = CONST 
    0x1e652: JUMPI v1e632(0x2a432), v51

    Begin block 0x2a432
    prev=[0x4b], succ=[]
    =================================
    0x2a452: v2a452(0x1c0) = CONST 
    0x2a472: CALLPRIVATE v2a452(0x1c0)

    Begin block 0x56
    prev=[0x4b], succ=[0x2ae32, 0x61]
    =================================
    0x57: v57(0x23b872dd) = CONST 
    0x5c: v5c = EQ v57(0x23b872dd), v34
    0x1f032: v1f032(0x2ae32) = CONST 
    0x1f052: JUMPI v1f032(0x2ae32), v5c

    Begin block 0x2ae32
    prev=[0x56], succ=[]
    =================================
    0x2ae52: v2ae52(0x1e5) = CONST 
    0x2ae72: CALLPRIVATE v2ae52(0x1e5)

    Begin block 0x61
    prev=[0x56], succ=[0x2b832, 0x6c]
    =================================
    0x62: v62(0x313ce567) = CONST 
    0x67: v67 = EQ v62(0x313ce567), v34
    0x1fa32: v1fa32(0x2b832) = CONST 
    0x1fa52: JUMPI v1fa32(0x2b832), v67

    Begin block 0x2b832
    prev=[0x61], succ=[]
    =================================
    0x2b852: v2b852(0x20d) = CONST 
    0x2b872: CALLPRIVATE v2b852(0x20d)

    Begin block 0x6c
    prev=[0x61], succ=[0x2c232, 0x77]
    =================================
    0x6d: v6d(0x42966c68) = CONST 
    0x72: v72 = EQ v6d(0x42966c68), v34
    0x20432: v20432(0x2c232) = CONST 
    0x20452: JUMPI v20432(0x2c232), v72

    Begin block 0x2c232
    prev=[0x6c], succ=[]
    =================================
    0x2c252: v2c252(0x236) = CONST 
    0x2c272: CALLPRIVATE v2c252(0x236)

    Begin block 0x77
    prev=[0x6c], succ=[0x2cc32, 0x82]
    =================================
    0x78: v78(0x5d5aa277) = CONST 
    0x7d: v7d = EQ v78(0x5d5aa277), v34
    0x20e32: v20e32(0x2cc32) = CONST 
    0x20e52: JUMPI v20e32(0x2cc32), v7d

    Begin block 0x2cc32
    prev=[0x77], succ=[]
    =================================
    0x2cc52: v2cc52(0x24e) = CONST 
    0x2cc72: CALLPRIVATE v2cc52(0x24e)

    Begin block 0x82
    prev=[0x77], succ=[0x2d632, 0x8d]
    =================================
    0x83: v83(0x66188463) = CONST 
    0x88: v88 = EQ v83(0x66188463), v34
    0x21832: v21832(0x2d632) = CONST 
    0x21852: JUMPI v21832(0x2d632), v88

    Begin block 0x2d632
    prev=[0x82], succ=[]
    =================================
    0x2d652: v2d652(0x27d) = CONST 
    0x2d672: CALLPRIVATE v2d652(0x27d)

    Begin block 0x8d
    prev=[0x82], succ=[0x2e032, 0x98]
    =================================
    0x8e: v8e(0x70a08231) = CONST 
    0x93: v93 = EQ v8e(0x70a08231), v34
    0x22232: v22232(0x2e032) = CONST 
    0x22252: JUMPI v22232(0x2e032), v93

    Begin block 0x2e032
    prev=[0x8d], succ=[]
    =================================
    0x2e052: v2e052(0x29f) = CONST 
    0x2e072: CALLPRIVATE v2e052(0x29f)

    Begin block 0x98
    prev=[0x8d], succ=[0x2ea32, 0xa3]
    =================================
    0x99: v99(0x8da5cb5b) = CONST 
    0x9e: v9e = EQ v99(0x8da5cb5b), v34
    0x22c32: v22c32(0x2ea32) = CONST 
    0x22c52: JUMPI v22c32(0x2ea32), v9e

    Begin block 0x2ea32
    prev=[0x98], succ=[]
    =================================
    0x2ea52: v2ea52(0x2be) = CONST 
    0x2ea72: CALLPRIVATE v2ea52(0x2be)

    Begin block 0xa3
    prev=[0x98], succ=[0x2f432, 0xae]
    =================================
    0xa4: va4(0x958222aa) = CONST 
    0xa9: va9 = EQ va4(0x958222aa), v34
    0x23632: v23632(0x2f432) = CONST 
    0x23652: JUMPI v23632(0x2f432), va9

    Begin block 0x2f432
    prev=[0xa3], succ=[]
    =================================
    0x2f452: v2f452(0x2d1) = CONST 
    0x2f472: CALLPRIVATE v2f452(0x2d1)

    Begin block 0xae
    prev=[0xa3], succ=[0x2fe32, 0xb9]
    =================================
    0xaf: vaf(0x95d89b41) = CONST 
    0xb4: vb4 = EQ vaf(0x95d89b41), v34
    0x24032: v24032(0x2fe32) = CONST 
    0x24052: JUMPI v24032(0x2fe32), vb4

    Begin block 0x2fe32
    prev=[0xae], succ=[]
    =================================
    0x2fe52: v2fe52(0x2e4) = CONST 
    0x2fe72: CALLPRIVATE v2fe52(0x2e4)

    Begin block 0xb9
    prev=[0xae], succ=[0x30832, 0xc4]
    =================================
    0xba: vba(0xa9059cbb) = CONST 
    0xbf: vbf = EQ vba(0xa9059cbb), v34
    0x24a32: v24a32(0x30832) = CONST 
    0x24a52: JUMPI v24a32(0x30832), vbf

    Begin block 0x30832
    prev=[0xb9], succ=[]
    =================================
    0x30852: v30852(0x2f7) = CONST 
    0x30872: CALLPRIVATE v30852(0x2f7)

    Begin block 0xc4
    prev=[0xb9], succ=[0x31232, 0xcf]
    =================================
    0xc5: vc5(0xd73dd623) = CONST 
    0xca: vca = EQ vc5(0xd73dd623), v34
    0x25432: v25432(0x31232) = CONST 
    0x25452: JUMPI v25432(0x31232), vca

    Begin block 0x31232
    prev=[0xc4], succ=[]
    =================================
    0x31252: v31252(0x319) = CONST 
    0x31272: CALLPRIVATE v31252(0x319)

    Begin block 0xcf
    prev=[0xc4], succ=[0x31c32, 0xda]
    =================================
    0xd0: vd0(0xd9194d2c) = CONST 
    0xd5: vd5 = EQ vd0(0xd9194d2c), v34
    0x25e32: v25e32(0x31c32) = CONST 
    0x25e52: JUMPI v25e32(0x31c32), vd5

    Begin block 0x31c32
    prev=[0xcf], succ=[]
    =================================
    0x31c52: v31c52(0x33b) = CONST 
    0x31c72: CALLPRIVATE v31c52(0x33b)

    Begin block 0xda
    prev=[0xcf], succ=[0x32632, 0xe5]
    =================================
    0xdb: vdb(0xdb0e16f1) = CONST 
    0xe0: ve0 = EQ vdb(0xdb0e16f1), v34
    0x26832: v26832(0x32632) = CONST 
    0x26852: JUMPI v26832(0x32632), ve0

    Begin block 0x32632
    prev=[0xda], succ=[]
    =================================
    0x32652: v32652(0x353) = CONST 
    0x32672: CALLPRIVATE v32652(0x353)

    Begin block 0xe5
    prev=[0xda], succ=[0x33032, 0xf0]
    =================================
    0xe6: ve6(0xdd62ed3e) = CONST 
    0xeb: veb = EQ ve6(0xdd62ed3e), v34
    0x27232: v27232(0x33032) = CONST 
    0x27252: JUMPI v27232(0x33032), veb

    Begin block 0x33032
    prev=[0xe5], succ=[]
    =================================
    0x33052: v33052(0x375) = CONST 
    0x33072: CALLPRIVATE v33052(0x375)

    Begin block 0xf0
    prev=[0xe5], succ=[0x28632, 0x33a32]
    =================================
    0xf1: vf1(0xf2fde38b) = CONST 
    0xf6: vf6 = EQ vf1(0xf2fde38b), v34
    0x27c32: v27c32(0x33a32) = CONST 
    0x27c52: JUMPI v27c32(0x33a32), vf6

    Begin block 0x28632
    prev=[0x0, 0xf0], succ=[]
    =================================
    0x28652: v28652(0xfb) = CONST 
    0x28672: CALLPRIVATE v28652(0xfb)

    Begin block 0x33a32
    prev=[0xf0], succ=[]
    =================================
    0x33a52: v33a52(0x39a) = CONST 
    0x33a72: CALLPRIVATE v33a52(0x39a)

    Begin block 0x29032
    prev=[0xd], succ=[]
    =================================
    0x29052: v29052(0x100) = CONST 
    0x29072: CALLPRIVATE v29052(0x100)

}

function name()() public {
    Begin block 0x100
    prev=[], succ=[0x107, 0x10b]
    =================================
    0x101: v101 = CALLVALUE 
    0x102: v102 = ISZERO v101
    0x103: v103(0x10b) = CONST 
    0x106: JUMPI v103(0x10b), v102

    Begin block 0x107
    prev=[0x100], succ=[]
    =================================
    0x107: v107(0x0) = CONST 
    0x10a: REVERT v107(0x0), v107(0x0)

    Begin block 0x10b
    prev=[0x100], succ=[0x3b9]
    =================================
    0x10c: v10c(0xadb8) = CONST 
    0x10f: v10f(0x3b9) = CONST 
    0x112: JUMP v10f(0x3b9)

    Begin block 0x3b9
    prev=[0x10b], succ=[0xadb8]
    =================================
    0x3ba: v3ba(0x40) = CONST 
    0x3bd: v3bd = MLOAD v3ba(0x40)
    0x3c0: v3c0 = ADD v3bd, v3ba(0x40)
    0x3c1: v3c1(0x40) = CONST 
    0x3c3: MSTORE v3c1(0x40), v3c0
    0x3c4: v3c4(0x17) = CONST 
    0x3c7: MSTORE v3bd, v3c4(0x17)
    0x3c8: v3c8(0x506f6c69637950616c204e6574776f726b20546f6b656e000000000000000000) = CONST 
    0x3e9: v3e9(0x20) = CONST 
    0x3ec: v3ec = ADD v3bd, v3e9(0x20)
    0x3ed: MSTORE v3ec, v3c8(0x506f6c69637950616c204e6574776f726b20546f6b656e000000000000000000)
    0x3ef: JUMP v10c(0xadb8)

    Begin block 0xadb8
    prev=[0x3b9], succ=[0x1370x100]
    =================================
    0xadb9: vadb9(0x40) = CONST 
    0xadbb: vadbb = MLOAD vadb9(0x40)
    0xadbc: vadbc(0x20) = CONST 
    0xadc0: MSTORE vadbb, vadbc(0x20)
    0xadc4: vadc4 = ADD vadbb, vadbc(0x20)
    0xadc8: vadc8(0x17) = MLOAD v3bd
    0xadca: MSTORE vadc4, vadc8(0x17)
    0xadcb: vadcb(0x20) = CONST 
    0xadcd: vadcd = ADD vadcb(0x20), vadc4
    0xadd1: vadd1(0x17) = MLOAD v3bd
    0xadd3: vadd3(0x20) = CONST 
    0xadd5: vadd5 = ADD vadd3(0x20), v3bd
    0xadda: vadda(0x0) = CONST 
    0xc751: vc751(0x137) = CONST 
    0xc771: JUMP vc751(0x137)

    Begin block 0x1370x100
    prev=[0xadb8, 0x1400x100], succ=[0x14f0x100, 0x1400x100]
    =================================
    0x1370x100_0x0: v137100_0 = PHI vadda(0x0), v10014a
    0x13a0x100: v10013a = LT v137100_0, vadd1(0x17)
    0x13b0x100: v10013b = ISZERO v10013a
    0x13c0x100: v10013c(0x14f) = CONST 
    0x13f0x100: JUMPI v10013c(0x14f), v10013b

    Begin block 0x14f0x100
    prev=[0x1370x100], succ=[0x1630x100, 0x17c0x100]
    =================================
    0x1580x100: v100158 = ADD vadd1(0x17), vadcd
    0x15a0x100: v10015a(0x1f) = CONST 
    0x15c0x100: v10015c(0x17) = AND v10015a(0x1f), vadd1(0x17)
    0x15e0x100: v10015e(0x0) = ISZERO v10015c(0x17)
    0x15f0x100: v10015f(0x17c) = CONST 
    0x1620x100: JUMPI v10015f(0x17c), v10015e(0x0)

    Begin block 0x1630x100
    prev=[0x14f0x100], succ=[0x17c0x100]
    =================================
    0x1650x100: v100165 = SUB v100158, v10015c(0x17)
    0x1670x100: v100167 = MLOAD v100165
    0x1680x100: v100168(0x1) = CONST 
    0x16b0x100: v10016b(0x20) = CONST 
    0x16d0x100: v10016d(0x9) = SUB v10016b(0x20), v10015c(0x17)
    0x16e0x100: v10016e(0x100) = CONST 
    0x1710x100: v100171(0x1000000000000000000) = EXP v10016e(0x100), v10016d(0x9)
    0x1720x100: v100172(0xffffffffffffffffff) = SUB v100171(0x1000000000000000000), v100168(0x1)
    0x1730x100: v100173(0xffffffffffffffffffffffffffffffffffffffffffffff000000000000000000) = NOT v100172(0xffffffffffffffffff)
    0x1740x100: v100174 = AND v100173(0xffffffffffffffffffffffffffffffffffffffffffffff000000000000000000), v100167
    0x1760x100: MSTORE v100165, v100174
    0x1770x100: v100177(0x20) = CONST 
    0x1790x100: v100179 = ADD v100177(0x20), v100165
    0x24ac0x100: v10024ac(0x17c) = CONST 
    0x24cc0x100: JUMP v10024ac(0x17c)

    Begin block 0x17c0x100
    prev=[0x1630x100, 0x14f0x100], succ=[]
    =================================
    0x17c0x100_0x1: v17c100_1 = PHI v100179, v100158
    0x1820x100: v100182(0x40) = CONST 
    0x1840x100: v100184 = MLOAD v100182(0x40)
    0x1870x100: v100187 = SUB v17c100_1, v100184
    0x1890x100: RETURN v100184, v100187

    Begin block 0x1400x100
    prev=[0x1370x100], succ=[0x1370x100]
    =================================
    0x1400x100_0x0: v140100_0 = PHI vadda(0x0), v10014a
    0x1420x100: v100142 = ADD vadd5, v140100_0
    0x1430x100: v100143 = MLOAD v100142
    0x1460x100: v100146 = ADD v140100_0, vadcd
    0x1470x100: MSTORE v100146, v100143
    0x1480x100: v100148(0x20) = CONST 
    0x14a0x100: v10014a = ADD v100148(0x20), v140100_0
    0x14b0x100: v10014b(0x137) = CONST 
    0x14e0x100: JUMP v10014b(0x137)

}

function approve(address,uint256)() public {
    Begin block 0x18a
    prev=[], succ=[0x191, 0x195]
    =================================
    0x18b: v18b = CALLVALUE 
    0x18c: v18c = ISZERO v18b
    0x18d: v18d(0x195) = CONST 
    0x190: JUMPI v18d(0x195), v18c

    Begin block 0x191
    prev=[0x18a], succ=[]
    =================================
    0x191: v191(0x0) = CONST 
    0x194: REVERT v191(0x0), v191(0x0)

    Begin block 0x195
    prev=[0x18a], succ=[0x3f0]
    =================================
    0x196: v196(0xc791) = CONST 
    0x199: v199(0x1) = CONST 
    0x19b: v19b(0xa0) = CONST 
    0x19d: v19d(0x2) = CONST 
    0x19f: v19f(0x10000000000000000000000000000000000000000) = EXP v19d(0x2), v19b(0xa0)
    0x1a0: v1a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19f(0x10000000000000000000000000000000000000000), v199(0x1)
    0x1a1: v1a1(0x4) = CONST 
    0x1a3: v1a3 = CALLDATALOAD v1a1(0x4)
    0x1a4: v1a4 = AND v1a3, v1a0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a5: v1a5(0x24) = CONST 
    0x1a7: v1a7 = CALLDATALOAD v1a5(0x24)
    0x1a8: v1a8(0x3f0) = CONST 
    0x1ab: JUMP v1a8(0x3f0)

    Begin block 0x3f0
    prev=[0x195], succ=[0xc791]
    =================================
    0x3f1: v3f1(0x1) = CONST 
    0x3f3: v3f3(0xa0) = CONST 
    0x3f5: v3f5(0x2) = CONST 
    0x3f7: v3f7(0x10000000000000000000000000000000000000000) = EXP v3f5(0x2), v3f3(0xa0)
    0x3f8: v3f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f7(0x10000000000000000000000000000000000000000), v3f1(0x1)
    0x3f9: v3f9 = CALLER 
    0x3fb: v3fb = AND v3f8(0xffffffffffffffffffffffffffffffffffffffff), v3f9
    0x3fc: v3fc(0x0) = CONST 
    0x400: MSTORE v3fc(0x0), v3fb
    0x401: v401(0x2) = CONST 
    0x403: v403(0x20) = CONST 
    0x407: MSTORE v403(0x20), v401(0x2)
    0x408: v408(0x40) = CONST 
    0x40c: v40c = SHA3 v3fc(0x0), v408(0x40)
    0x40f: v40f = AND v1a4, v3f8(0xffffffffffffffffffffffffffffffffffffffff)
    0x412: MSTORE v3fc(0x0), v40f
    0x416: MSTORE v403(0x20), v40c
    0x419: v419 = SHA3 v3fc(0x0), v408(0x40)
    0x41c: SSTORE v419, v1a7
    0x421: v421(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x445: v445 = MLOAD v408(0x40)
    0x448: MSTORE v445, v1a7
    0x449: v449(0x20) = CONST 
    0x44b: v44b = ADD v449(0x20), v445
    0x44c: v44c(0x40) = CONST 
    0x44e: v44e = MLOAD v44c(0x40)
    0x451: v451(0x20) = SUB v44b, v44e
    0x453: LOG3 v44e, v451(0x20), v421(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v3fb, v40f
    0x455: v455(0x1) = CONST 
    0x45b: JUMP v196(0xc791)

    Begin block 0xc791
    prev=[0x3f0], succ=[]
    =================================
    0xc792: vc792(0x40) = CONST 
    0xc794: vc794 = MLOAD vc792(0x40)
    0xc796: vc796(0x0) = ISZERO v455(0x1)
    0xc797: vc797(0x1) = ISZERO vc796(0x0)
    0xc799: MSTORE vc794, vc797(0x1)
    0xc79a: vc79a(0x20) = CONST 
    0xc79c: vc79c = ADD vc79a(0x20), vc794
    0xc79d: vc79d(0x40) = CONST 
    0xc79f: vc79f = MLOAD vc79d(0x40)
    0xc7a2: vc7a2(0x20) = SUB vc79c, vc79f
    0xc7a4: RETURN vc79f, vc7a2(0x20)

}

function totalSupply()() public {
    Begin block 0x1c0
    prev=[], succ=[0x1c7, 0x1cb]
    =================================
    0x1c1: v1c1 = CALLVALUE 
    0x1c2: v1c2 = ISZERO v1c1
    0x1c3: v1c3(0x1cb) = CONST 
    0x1c6: JUMPI v1c3(0x1cb), v1c2

    Begin block 0x1c7
    prev=[0x1c0], succ=[]
    =================================
    0x1c7: v1c7(0x0) = CONST 
    0x1ca: REVERT v1c7(0x0), v1c7(0x0)

    Begin block 0x1cb
    prev=[0x1c0], succ=[0x45c]
    =================================
    0x1cc: v1cc(0xc7c4) = CONST 
    0x1cf: v1cf(0x45c) = CONST 
    0x1d2: JUMP v1cf(0x45c)

    Begin block 0x45c
    prev=[0x1cb], succ=[0xc7c4]
    =================================
    0x45d: v45d(0x1) = CONST 
    0x45f: v45f = SLOAD v45d(0x1)
    0x461: JUMP v1cc(0xc7c4)

    Begin block 0xc7c4
    prev=[0x45c], succ=[]
    =================================
    0xc7c5: vc7c5(0x40) = CONST 
    0xc7c7: vc7c7 = MLOAD vc7c5(0x40)
    0xc7ca: MSTORE vc7c7, v45f
    0xc7cb: vc7cb(0x20) = CONST 
    0xc7cd: vc7cd = ADD vc7cb(0x20), vc7c7
    0xc7ce: vc7ce(0x40) = CONST 
    0xc7d0: vc7d0 = MLOAD vc7ce(0x40)
    0xc7d3: vc7d3(0x20) = SUB vc7cd, vc7d0
    0xc7d5: RETURN vc7d0, vc7d3(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x1e5
    prev=[], succ=[0x1ec, 0x1f0]
    =================================
    0x1e6: v1e6 = CALLVALUE 
    0x1e7: v1e7 = ISZERO v1e6
    0x1e8: v1e8(0x1f0) = CONST 
    0x1eb: JUMPI v1e8(0x1f0), v1e7

    Begin block 0x1ec
    prev=[0x1e5], succ=[]
    =================================
    0x1ec: v1ec(0x0) = CONST 
    0x1ef: REVERT v1ec(0x0), v1ec(0x0)

    Begin block 0x1f0
    prev=[0x1e5], succ=[0x462B0x1f0]
    =================================
    0x1f1: v1f1(0xc7f5) = CONST 
    0x1f4: v1f4(0x1) = CONST 
    0x1f6: v1f6(0xa0) = CONST 
    0x1f8: v1f8(0x2) = CONST 
    0x1fa: v1fa(0x10000000000000000000000000000000000000000) = EXP v1f8(0x2), v1f6(0xa0)
    0x1fb: v1fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fa(0x10000000000000000000000000000000000000000), v1f4(0x1)
    0x1fc: v1fc(0x4) = CONST 
    0x1fe: v1fe = CALLDATALOAD v1fc(0x4)
    0x200: v200 = AND v1fb(0xffffffffffffffffffffffffffffffffffffffff), v1fe
    0x202: v202(0x24) = CONST 
    0x204: v204 = CALLDATALOAD v202(0x24)
    0x205: v205 = AND v204, v1fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x206: v206(0x44) = CONST 
    0x208: v208 = CALLDATALOAD v206(0x44)
    0x209: v209(0x462) = CONST 
    0x20c: JUMP v209(0x462)

    Begin block 0x462B0x1f0
    prev=[0x1f0], succ=[0x48bB0x1f0, 0x478B0x1f0]
    =================================
    0x463S0x1f0: v463V1f0(0x4) = CONST 
    0x465S0x1f0: v465V1f0 = SLOAD v463V1f0(0x4)
    0x466S0x1f0: v466V1f0(0x0) = CONST 
    0x469S0x1f0: v469V1f0(0xa0) = CONST 
    0x46bS0x1f0: v46bV1f0(0x2) = CONST 
    0x46dS0x1f0: v46dV1f0(0x10000000000000000000000000000000000000000) = EXP v46bV1f0(0x2), v469V1f0(0xa0)
    0x46fS0x1f0: v46fV1f0 = DIV v465V1f0, v46dV1f0(0x10000000000000000000000000000000000000000)
    0x470S0x1f0: v470V1f0(0xff) = CONST 
    0x472S0x1f0: v472V1f0 = AND v470V1f0(0xff), v46fV1f0
    0x474S0x1f0: v474V1f0(0x48b) = CONST 
    0x477S0x1f0: JUMPI v474V1f0(0x48b), v472V1f0

    Begin block 0x48bB0x1f0
    prev=[0x462B0x1f0, 0x478B0x1f0], succ=[0x4a4B0x1f0, 0x491B0x1f0]
    =================================
    0x48b_0x0S0x1f0: v48b_0V1f0 = PHI v472V1f0, v48aV1f0
    0x48dS0x1f0: v48dV1f0(0x4a4) = CONST 
    0x490S0x1f0: JUMPI v48dV1f0(0x4a4), v48b_0V1f0

    Begin block 0x4a4B0x1f0
    prev=[0x48bB0x1f0, 0x491B0x1f0], succ=[0x4abB0x1f0, 0x4afB0x1f0]
    =================================
    0x4a4_0x0S0x1f0: v4a4_0V1f0 = PHI v472V1f0, v48aV1f0, v4a3V1f0
    0x4a5S0x1f0: v4a5V1f0 = ISZERO v4a4_0V1f0
    0x4a6S0x1f0: v4a6V1f0 = ISZERO v4a5V1f0
    0x4a7S0x1f0: v4a7V1f0(0x4af) = CONST 
    0x4aaS0x1f0: JUMPI v4a7V1f0(0x4af), v4a6V1f0

    Begin block 0x4abB0x1f0
    prev=[0x4a4B0x1f0], succ=[]
    =================================
    0x4abS0x1f0: v4abV1f0(0x0) = CONST 
    0x4aeS0x1f0: REVERT v4abV1f0(0x0), v4abV1f0(0x0)

    Begin block 0x4afB0x1f0
    prev=[0x4a4B0x1f0], succ=[0x4c1B0x1f0, 0x4c5B0x1f0]
    =================================
    0x4b1S0x1f0: v4b1V1f0(0x1) = CONST 
    0x4b3S0x1f0: v4b3V1f0(0xa0) = CONST 
    0x4b5S0x1f0: v4b5V1f0(0x2) = CONST 
    0x4b7S0x1f0: v4b7V1f0(0x10000000000000000000000000000000000000000) = EXP v4b5V1f0(0x2), v4b3V1f0(0xa0)
    0x4b8S0x1f0: v4b8V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b7V1f0(0x10000000000000000000000000000000000000000), v4b1V1f0(0x1)
    0x4baS0x1f0: v4baV1f0 = AND v205, v4b8V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x4bbS0x1f0: v4bbV1f0 = ISZERO v4baV1f0
    0x4bcS0x1f0: v4bcV1f0 = ISZERO v4bbV1f0
    0x4bdS0x1f0: v4bdV1f0(0x4c5) = CONST 
    0x4c0S0x1f0: JUMPI v4bdV1f0(0x4c5), v4bcV1f0

    Begin block 0x4c1B0x1f0
    prev=[0x4afB0x1f0], succ=[]
    =================================
    0x4c1S0x1f0: v4c1V1f0(0x0) = CONST 
    0x4c4S0x1f0: REVERT v4c1V1f0(0x0), v4c1V1f0(0x0)

    Begin block 0x4c5B0x1f0
    prev=[0x4afB0x1f0], succ=[0x4e2B0x1f0, 0x4e6B0x1f0]
    =================================
    0x4c6S0x1f0: v4c6V1f0 = ADDRESS 
    0x4c7S0x1f0: v4c7V1f0(0x1) = CONST 
    0x4c9S0x1f0: v4c9V1f0(0xa0) = CONST 
    0x4cbS0x1f0: v4cbV1f0(0x2) = CONST 
    0x4cdS0x1f0: v4cdV1f0(0x10000000000000000000000000000000000000000) = EXP v4cbV1f0(0x2), v4c9V1f0(0xa0)
    0x4ceS0x1f0: v4ceV1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4cdV1f0(0x10000000000000000000000000000000000000000), v4c7V1f0(0x1)
    0x4cfS0x1f0: v4cfV1f0 = AND v4ceV1f0(0xffffffffffffffffffffffffffffffffffffffff), v4c6V1f0
    0x4d1S0x1f0: v4d1V1f0(0x1) = CONST 
    0x4d3S0x1f0: v4d3V1f0(0xa0) = CONST 
    0x4d5S0x1f0: v4d5V1f0(0x2) = CONST 
    0x4d7S0x1f0: v4d7V1f0(0x10000000000000000000000000000000000000000) = EXP v4d5V1f0(0x2), v4d3V1f0(0xa0)
    0x4d8S0x1f0: v4d8V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d7V1f0(0x10000000000000000000000000000000000000000), v4d1V1f0(0x1)
    0x4d9S0x1f0: v4d9V1f0 = AND v4d8V1f0(0xffffffffffffffffffffffffffffffffffffffff), v205
    0x4daS0x1f0: v4daV1f0 = EQ v4d9V1f0, v4cfV1f0
    0x4dbS0x1f0: v4dbV1f0 = ISZERO v4daV1f0
    0x4dcS0x1f0: v4dcV1f0 = ISZERO v4dbV1f0
    0x4ddS0x1f0: v4ddV1f0 = ISZERO v4dcV1f0
    0x4deS0x1f0: v4deV1f0(0x4e6) = CONST 
    0x4e1S0x1f0: JUMPI v4deV1f0(0x4e6), v4ddV1f0

    Begin block 0x4e2B0x1f0
    prev=[0x4c5B0x1f0], succ=[]
    =================================
    0x4e2S0x1f0: v4e2V1f0(0x0) = CONST 
    0x4e5S0x1f0: REVERT v4e2V1f0(0x0), v4e2V1f0(0x0)

    Begin block 0x4e6B0x1f0
    prev=[0x4c5B0x1f0], succ=[0x9c4B0x1f0]
    =================================
    0x4e7S0x1f0: v4e7V1f0(0x4f1) = CONST 
    0x4edS0x1f0: v4edV1f0(0x9c4) = CONST 
    0x4f0S0x1f0: JUMP v4edV1f0(0x9c4)

    Begin block 0x9c4B0x1f0
    prev=[0x4e6B0x1f0], succ=[0x9d7B0x1f0, 0x9dbB0x1f0]
    =================================
    0x9c5S0x1f0: v9c5V1f0(0x0) = CONST 
    0x9c7S0x1f0: v9c7V1f0(0x1) = CONST 
    0x9c9S0x1f0: v9c9V1f0(0xa0) = CONST 
    0x9cbS0x1f0: v9cbV1f0(0x2) = CONST 
    0x9cdS0x1f0: v9cdV1f0(0x10000000000000000000000000000000000000000) = EXP v9cbV1f0(0x2), v9c9V1f0(0xa0)
    0x9ceS0x1f0: v9ceV1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9cdV1f0(0x10000000000000000000000000000000000000000), v9c7V1f0(0x1)
    0x9d0S0x1f0: v9d0V1f0 = AND v205, v9ceV1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x9d1S0x1f0: v9d1V1f0 = ISZERO v9d0V1f0
    0x9d2S0x1f0: v9d2V1f0 = ISZERO v9d1V1f0
    0x9d3S0x1f0: v9d3V1f0(0x9db) = CONST 
    0x9d6S0x1f0: JUMPI v9d3V1f0(0x9db), v9d2V1f0

    Begin block 0x9d7B0x1f0
    prev=[0x9c4B0x1f0], succ=[]
    =================================
    0x9d7S0x1f0: v9d7V1f0(0x0) = CONST 
    0x9daS0x1f0: REVERT v9d7V1f0(0x0), v9d7V1f0(0x0)

    Begin block 0x9dbB0x1f0
    prev=[0x9c4B0x1f0], succ=[0x9fcB0x1f0, 0xa00B0x1f0]
    =================================
    0x9dcS0x1f0: v9dcV1f0(0x1) = CONST 
    0x9deS0x1f0: v9deV1f0(0xa0) = CONST 
    0x9e0S0x1f0: v9e0V1f0(0x2) = CONST 
    0x9e2S0x1f0: v9e2V1f0(0x10000000000000000000000000000000000000000) = EXP v9e0V1f0(0x2), v9deV1f0(0xa0)
    0x9e3S0x1f0: v9e3V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9e2V1f0(0x10000000000000000000000000000000000000000), v9dcV1f0(0x1)
    0x9e5S0x1f0: v9e5V1f0 = AND v200, v9e3V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x9e6S0x1f0: v9e6V1f0(0x0) = CONST 
    0x9eaS0x1f0: MSTORE v9e6V1f0(0x0), v9e5V1f0
    0x9ebS0x1f0: v9ebV1f0(0x20) = CONST 
    0x9efS0x1f0: MSTORE v9ebV1f0(0x20), v9e6V1f0(0x0)
    0x9f0S0x1f0: v9f0V1f0(0x40) = CONST 
    0x9f3S0x1f0: v9f3V1f0 = SHA3 v9e6V1f0(0x0), v9f0V1f0(0x40)
    0x9f4S0x1f0: v9f4V1f0 = SLOAD v9f3V1f0
    0x9f6S0x1f0: v9f6V1f0 = GT v208, v9f4V1f0
    0x9f7S0x1f0: v9f7V1f0 = ISZERO v9f6V1f0
    0x9f8S0x1f0: v9f8V1f0(0xa00) = CONST 
    0x9fbS0x1f0: JUMPI v9f8V1f0(0xa00), v9f7V1f0

    Begin block 0x9fcB0x1f0
    prev=[0x9dbB0x1f0], succ=[]
    =================================
    0x9fcS0x1f0: v9fcV1f0(0x0) = CONST 
    0x9ffS0x1f0: REVERT v9fcV1f0(0x0), v9fcV1f0(0x0)

    Begin block 0xa00B0x1f0
    prev=[0x9dbB0x1f0], succ=[0xa2fB0x1f0, 0xa33B0x1f0]
    =================================
    0xa01S0x1f0: va01V1f0(0x1) = CONST 
    0xa03S0x1f0: va03V1f0(0xa0) = CONST 
    0xa05S0x1f0: va05V1f0(0x2) = CONST 
    0xa07S0x1f0: va07V1f0(0x10000000000000000000000000000000000000000) = EXP va05V1f0(0x2), va03V1f0(0xa0)
    0xa08S0x1f0: va08V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB va07V1f0(0x10000000000000000000000000000000000000000), va01V1f0(0x1)
    0xa0bS0x1f0: va0bV1f0 = AND v200, va08V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xa0cS0x1f0: va0cV1f0(0x0) = CONST 
    0xa10S0x1f0: MSTORE va0cV1f0(0x0), va0bV1f0
    0xa11S0x1f0: va11V1f0(0x2) = CONST 
    0xa13S0x1f0: va13V1f0(0x20) = CONST 
    0xa17S0x1f0: MSTORE va13V1f0(0x20), va11V1f0(0x2)
    0xa18S0x1f0: va18V1f0(0x40) = CONST 
    0xa1cS0x1f0: va1cV1f0 = SHA3 va0cV1f0(0x0), va18V1f0(0x40)
    0xa1dS0x1f0: va1dV1f0 = CALLER 
    0xa20S0x1f0: va20V1f0 = AND va08V1f0(0xffffffffffffffffffffffffffffffffffffffff), va1dV1f0
    0xa22S0x1f0: MSTORE va0cV1f0(0x0), va20V1f0
    0xa25S0x1f0: MSTORE va13V1f0(0x20), va1cV1f0
    0xa26S0x1f0: va26V1f0 = SHA3 va0cV1f0(0x0), va18V1f0(0x40)
    0xa27S0x1f0: va27V1f0 = SLOAD va26V1f0
    0xa29S0x1f0: va29V1f0 = GT v208, va27V1f0
    0xa2aS0x1f0: va2aV1f0 = ISZERO va29V1f0
    0xa2bS0x1f0: va2bV1f0(0xa33) = CONST 
    0xa2eS0x1f0: JUMPI va2bV1f0(0xa33), va2aV1f0

    Begin block 0xa2fB0x1f0
    prev=[0xa00B0x1f0], succ=[]
    =================================
    0xa2fS0x1f0: va2fV1f0(0x0) = CONST 
    0xa32S0x1f0: REVERT va2fV1f0(0x0), va2fV1f0(0x0)

    Begin block 0xa33B0x1f0
    prev=[0xa00B0x1f0], succ=[0xa5cB0x1f0]
    =================================
    0xa34S0x1f0: va34V1f0(0x1) = CONST 
    0xa36S0x1f0: va36V1f0(0xa0) = CONST 
    0xa38S0x1f0: va38V1f0(0x2) = CONST 
    0xa3aS0x1f0: va3aV1f0(0x10000000000000000000000000000000000000000) = EXP va38V1f0(0x2), va36V1f0(0xa0)
    0xa3bS0x1f0: va3bV1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB va3aV1f0(0x10000000000000000000000000000000000000000), va34V1f0(0x1)
    0xa3dS0x1f0: va3dV1f0 = AND v200, va3bV1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xa3eS0x1f0: va3eV1f0(0x0) = CONST 
    0xa42S0x1f0: MSTORE va3eV1f0(0x0), va3dV1f0
    0xa43S0x1f0: va43V1f0(0x20) = CONST 
    0xa47S0x1f0: MSTORE va43V1f0(0x20), va3eV1f0(0x0)
    0xa48S0x1f0: va48V1f0(0x40) = CONST 
    0xa4bS0x1f0: va4bV1f0 = SHA3 va3eV1f0(0x0), va48V1f0(0x40)
    0xa4cS0x1f0: va4cV1f0 = SLOAD va4bV1f0
    0xa4dS0x1f0: va4dV1f0(0xa5c) = CONST 
    0xa52S0x1f0: va52V1f0(0xffffffff) = CONST 
    0xa57S0x1f0: va57V1f0(0xbfe) = CONST 
    0xa5aS0x1f0: va5aV1f0(0xbfe) = AND va57V1f0(0xbfe), va52V1f0(0xffffffff)
    0xa5bS0x1f0: va5b_0V1f0 = CALLPRIVATE va5aV1f0(0xbfe), v208, va4cV1f0, va4dV1f0(0xa5c)

    Begin block 0xa5cB0x1f0
    prev=[0xa33B0x1f0], succ=[0xa91B0x1f0]
    =================================
    0xa5dS0x1f0: va5dV1f0(0x1) = CONST 
    0xa5fS0x1f0: va5fV1f0(0xa0) = CONST 
    0xa61S0x1f0: va61V1f0(0x2) = CONST 
    0xa63S0x1f0: va63V1f0(0x10000000000000000000000000000000000000000) = EXP va61V1f0(0x2), va5fV1f0(0xa0)
    0xa64S0x1f0: va64V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB va63V1f0(0x10000000000000000000000000000000000000000), va5dV1f0(0x1)
    0xa67S0x1f0: va67V1f0 = AND v200, va64V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xa68S0x1f0: va68V1f0(0x0) = CONST 
    0xa6cS0x1f0: MSTORE va68V1f0(0x0), va67V1f0
    0xa6dS0x1f0: va6dV1f0(0x20) = CONST 
    0xa71S0x1f0: MSTORE va6dV1f0(0x20), va68V1f0(0x0)
    0xa72S0x1f0: va72V1f0(0x40) = CONST 
    0xa76S0x1f0: va76V1f0 = SHA3 va68V1f0(0x0), va72V1f0(0x40)
    0xa7aS0x1f0: SSTORE va76V1f0, va5b_0V1f0
    0xa7dS0x1f0: va7dV1f0 = AND v205, va64V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xa7fS0x1f0: MSTORE va68V1f0(0x0), va7dV1f0
    0xa80S0x1f0: va80V1f0 = SHA3 va68V1f0(0x0), va72V1f0(0x40)
    0xa81S0x1f0: va81V1f0 = SLOAD va80V1f0
    0xa82S0x1f0: va82V1f0(0xa91) = CONST 
    0xa87S0x1f0: va87V1f0(0xffffffff) = CONST 
    0xa8cS0x1f0: va8cV1f0(0xd22) = CONST 
    0xa8fS0x1f0: va8fV1f0(0xd22) = AND va8cV1f0(0xd22), va87V1f0(0xffffffff)
    0xa90S0x1f0: va90_0V1f0 = CALLPRIVATE va8fV1f0(0xd22), v208, va81V1f0, va82V1f0(0xa91)

    Begin block 0xa91B0x1f0
    prev=[0xa5cB0x1f0], succ=[0xad7B0x1f0]
    =================================
    0xa92S0x1f0: va92V1f0(0x1) = CONST 
    0xa94S0x1f0: va94V1f0(0xa0) = CONST 
    0xa96S0x1f0: va96V1f0(0x2) = CONST 
    0xa98S0x1f0: va98V1f0(0x10000000000000000000000000000000000000000) = EXP va96V1f0(0x2), va94V1f0(0xa0)
    0xa99S0x1f0: va99V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB va98V1f0(0x10000000000000000000000000000000000000000), va92V1f0(0x1)
    0xa9cS0x1f0: va9cV1f0 = AND v205, va99V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xa9dS0x1f0: va9dV1f0(0x0) = CONST 
    0xaa1S0x1f0: MSTORE va9dV1f0(0x0), va9cV1f0
    0xaa2S0x1f0: vaa2V1f0(0x20) = CONST 
    0xaa6S0x1f0: MSTORE vaa2V1f0(0x20), va9dV1f0(0x0)
    0xaa7S0x1f0: vaa7V1f0(0x40) = CONST 
    0xaabS0x1f0: vaabV1f0 = SHA3 va9dV1f0(0x0), vaa7V1f0(0x40)
    0xaafS0x1f0: SSTORE vaabV1f0, va90_0V1f0
    0xab2S0x1f0: vab2V1f0 = AND va99V1f0(0xffffffffffffffffffffffffffffffffffffffff), v200
    0xab4S0x1f0: MSTORE va9dV1f0(0x0), vab2V1f0
    0xab5S0x1f0: vab5V1f0(0x2) = CONST 
    0xab8S0x1f0: MSTORE vaa2V1f0(0x20), vab5V1f0(0x2)
    0xabbS0x1f0: vabbV1f0 = SHA3 va9dV1f0(0x0), vaa7V1f0(0x40)
    0xabcS0x1f0: vabcV1f0 = CALLER 
    0xabfS0x1f0: vabfV1f0 = AND va99V1f0(0xffffffffffffffffffffffffffffffffffffffff), vabcV1f0
    0xac1S0x1f0: MSTORE va9dV1f0(0x0), vabfV1f0
    0xac5S0x1f0: MSTORE vaa2V1f0(0x20), vabbV1f0
    0xac6S0x1f0: vac6V1f0 = SHA3 va9dV1f0(0x0), vaa7V1f0(0x40)
    0xac7S0x1f0: vac7V1f0 = SLOAD vac6V1f0
    0xac8S0x1f0: vac8V1f0(0xad7) = CONST 
    0xacdS0x1f0: vacdV1f0(0xffffffff) = CONST 
    0xad2S0x1f0: vad2V1f0(0xbfe) = CONST 
    0xad5S0x1f0: vad5V1f0(0xbfe) = AND vad2V1f0(0xbfe), vacdV1f0(0xffffffff)
    0xad6S0x1f0: vad6_0V1f0 = CALLPRIVATE vad5V1f0(0xbfe), v208, vac7V1f0, vac8V1f0(0xad7)

    Begin block 0xad7B0x1f0
    prev=[0xa91B0x1f0], succ=[0x4f1B0x1f0]
    =================================
    0xad8S0x1f0: vad8V1f0(0x1) = CONST 
    0xadaS0x1f0: vadaV1f0(0xa0) = CONST 
    0xadcS0x1f0: vadcV1f0(0x2) = CONST 
    0xadeS0x1f0: vadeV1f0(0x10000000000000000000000000000000000000000) = EXP vadcV1f0(0x2), vadaV1f0(0xa0)
    0xadfS0x1f0: vadfV1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB vadeV1f0(0x10000000000000000000000000000000000000000), vad8V1f0(0x1)
    0xae2S0x1f0: vae2V1f0 = AND v200, vadfV1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xae3S0x1f0: vae3V1f0(0x0) = CONST 
    0xae7S0x1f0: MSTORE vae3V1f0(0x0), vae2V1f0
    0xae8S0x1f0: vae8V1f0(0x2) = CONST 
    0xaeaS0x1f0: vaeaV1f0(0x20) = CONST 
    0xaeeS0x1f0: MSTORE vaeaV1f0(0x20), vae8V1f0(0x2)
    0xaefS0x1f0: vaefV1f0(0x40) = CONST 
    0xaf3S0x1f0: vaf3V1f0 = SHA3 vae3V1f0(0x0), vaefV1f0(0x40)
    0xaf4S0x1f0: vaf4V1f0 = CALLER 
    0xaf6S0x1f0: vaf6V1f0 = AND vadfV1f0(0xffffffffffffffffffffffffffffffffffffffff), vaf4V1f0
    0xaf8S0x1f0: MSTORE vae3V1f0(0x0), vaf6V1f0
    0xafbS0x1f0: MSTORE vaeaV1f0(0x20), vaf3V1f0
    0xaffS0x1f0: vaffV1f0 = SHA3 vae3V1f0(0x0), vaefV1f0(0x40)
    0xb03S0x1f0: SSTORE vaffV1f0, vad6_0V1f0
    0xb06S0x1f0: vb06V1f0 = AND v205, vadfV1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0xb08S0x1f0: vb08V1f0(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xb2cS0x1f0: vb2cV1f0 = MLOAD vaefV1f0(0x40)
    0xb2fS0x1f0: MSTORE vb2cV1f0, v208
    0xb30S0x1f0: vb30V1f0(0x20) = CONST 
    0xb32S0x1f0: vb32V1f0 = ADD vb30V1f0(0x20), vb2cV1f0
    0xb33S0x1f0: vb33V1f0(0x40) = CONST 
    0xb35S0x1f0: vb35V1f0 = MLOAD vb33V1f0(0x40)
    0xb38S0x1f0: vb38V1f0(0x20) = SUB vb32V1f0, vb35V1f0
    0xb3aS0x1f0: LOG3 vb35V1f0, vb38V1f0(0x20), vb08V1f0(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vae2V1f0, vb06V1f0
    0xb3cS0x1f0: vb3cV1f0(0x1) = CONST 
    0xb43S0x1f0: JUMP v4e7V1f0(0x4f1)

    Begin block 0x4f1B0x1f0
    prev=[0xad7B0x1f0], succ=[0xc7f5]
    =================================
    0x4f9S0x1f0: JUMP v1f1(0xc7f5)

    Begin block 0xc7f5
    prev=[0x4f1B0x1f0], succ=[]
    =================================
    0xc7f6: vc7f6(0x40) = CONST 
    0xc7f8: vc7f8 = MLOAD vc7f6(0x40)
    0xc7fa: vc7fa(0x0) = ISZERO vb3cV1f0(0x1)
    0xc7fb: vc7fb(0x1) = ISZERO vc7fa(0x0)
    0xc7fd: MSTORE vc7f8, vc7fb(0x1)
    0xc7fe: vc7fe(0x20) = CONST 
    0xc800: vc800 = ADD vc7fe(0x20), vc7f8
    0xc801: vc801(0x40) = CONST 
    0xc803: vc803 = MLOAD vc801(0x40)
    0xc806: vc806(0x20) = SUB vc800, vc803
    0xc808: RETURN vc803, vc806(0x20)

    Begin block 0x491B0x1f0
    prev=[0x48bB0x1f0], succ=[0x4a4B0x1f0]
    =================================
    0x492S0x1f0: v492V1f0(0x4) = CONST 
    0x494S0x1f0: v494V1f0 = SLOAD v492V1f0(0x4)
    0x495S0x1f0: v495V1f0 = CALLER 
    0x496S0x1f0: v496V1f0(0x1) = CONST 
    0x498S0x1f0: v498V1f0(0xa0) = CONST 
    0x49aS0x1f0: v49aV1f0(0x2) = CONST 
    0x49cS0x1f0: v49cV1f0(0x10000000000000000000000000000000000000000) = EXP v49aV1f0(0x2), v498V1f0(0xa0)
    0x49dS0x1f0: v49dV1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49cV1f0(0x10000000000000000000000000000000000000000), v496V1f0(0x1)
    0x4a0S0x1f0: v4a0V1f0 = AND v49dV1f0(0xffffffffffffffffffffffffffffffffffffffff), v495V1f0
    0x4a2S0x1f0: v4a2V1f0 = AND v494V1f0, v49dV1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a3S0x1f0: v4a3V1f0 = EQ v4a2V1f0, v4a0V1f0
    0x38acS0x1f0: v38acV1f0(0x4a4) = CONST 
    0x38ccS0x1f0: JUMP v38acV1f0(0x4a4)

    Begin block 0x478B0x1f0
    prev=[0x462B0x1f0], succ=[0x48bB0x1f0]
    =================================
    0x479S0x1f0: v479V1f0(0x3) = CONST 
    0x47bS0x1f0: v47bV1f0 = SLOAD v479V1f0(0x3)
    0x47cS0x1f0: v47cV1f0 = CALLER 
    0x47dS0x1f0: v47dV1f0(0x1) = CONST 
    0x47fS0x1f0: v47fV1f0(0xa0) = CONST 
    0x481S0x1f0: v481V1f0(0x2) = CONST 
    0x483S0x1f0: v483V1f0(0x10000000000000000000000000000000000000000) = EXP v481V1f0(0x2), v47fV1f0(0xa0)
    0x484S0x1f0: v484V1f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v483V1f0(0x10000000000000000000000000000000000000000), v47dV1f0(0x1)
    0x487S0x1f0: v487V1f0 = AND v484V1f0(0xffffffffffffffffffffffffffffffffffffffff), v47cV1f0
    0x489S0x1f0: v489V1f0 = AND v47bV1f0, v484V1f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x48aS0x1f0: v48aV1f0 = EQ v489V1f0, v487V1f0
    0x2eacS0x1f0: v2eacV1f0(0x48b) = CONST 
    0x2eccS0x1f0: JUMP v2eacV1f0(0x48b)

}

function decimals()() public {
    Begin block 0x20d
    prev=[], succ=[0x214, 0x218]
    =================================
    0x20e: v20e = CALLVALUE 
    0x20f: v20f = ISZERO v20e
    0x210: v210(0x218) = CONST 
    0x213: JUMPI v210(0x218), v20f

    Begin block 0x214
    prev=[0x20d], succ=[]
    =================================
    0x214: v214(0x0) = CONST 
    0x217: REVERT v214(0x0), v214(0x0)

    Begin block 0x218
    prev=[0x20d], succ=[0x4fa]
    =================================
    0x219: v219(0x220) = CONST 
    0x21c: v21c(0x4fa) = CONST 
    0x21f: JUMP v21c(0x4fa)

    Begin block 0x4fa
    prev=[0x218], succ=[0x220]
    =================================
    0x4fb: v4fb(0x12) = CONST 
    0x4fe: JUMP v219(0x220)

    Begin block 0x220
    prev=[0x4fa], succ=[]
    =================================
    0x221: v221(0x40) = CONST 
    0x223: v223 = MLOAD v221(0x40)
    0x224: v224(0xff) = CONST 
    0x228: v228(0x12) = AND v4fb(0x12), v224(0xff)
    0x22a: MSTORE v223, v228(0x12)
    0x22b: v22b(0x20) = CONST 
    0x22d: v22d = ADD v22b(0x20), v223
    0x22e: v22e(0x40) = CONST 
    0x230: v230 = MLOAD v22e(0x40)
    0x233: v233(0x20) = SUB v22d, v230
    0x235: RETURN v230, v233(0x20)

}

function burn(uint256)() public {
    Begin block 0x236
    prev=[], succ=[0x23d, 0x241]
    =================================
    0x237: v237 = CALLVALUE 
    0x238: v238 = ISZERO v237
    0x239: v239(0x241) = CONST 
    0x23c: JUMPI v239(0x241), v238

    Begin block 0x23d
    prev=[0x236], succ=[]
    =================================
    0x23d: v23d(0x0) = CONST 
    0x240: REVERT v23d(0x0), v23d(0x0)

    Begin block 0x241
    prev=[0x236], succ=[0x4ff]
    =================================
    0x242: v242(0xc828) = CONST 
    0x245: v245(0x4) = CONST 
    0x247: v247 = CALLDATALOAD v245(0x4)
    0x248: v248(0x4ff) = CONST 
    0x24b: JUMP v248(0x4ff)

    Begin block 0x4ff
    prev=[0x241], succ=[0xb44]
    =================================
    0x500: v500(0x508) = CONST 
    0x504: v504(0xb44) = CONST 
    0x507: JUMP v504(0xb44)

    Begin block 0xb44
    prev=[0x4ff], succ=[0xb65, 0xb69]
    =================================
    0xb45: vb45(0x1) = CONST 
    0xb47: vb47(0xa0) = CONST 
    0xb49: vb49(0x2) = CONST 
    0xb4b: vb4b(0x10000000000000000000000000000000000000000) = EXP vb49(0x2), vb47(0xa0)
    0xb4c: vb4c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb4b(0x10000000000000000000000000000000000000000), vb45(0x1)
    0xb4d: vb4d = CALLER 
    0xb4e: vb4e = AND vb4d, vb4c(0xffffffffffffffffffffffffffffffffffffffff)
    0xb4f: vb4f(0x0) = CONST 
    0xb53: MSTORE vb4f(0x0), vb4e
    0xb54: vb54(0x20) = CONST 
    0xb58: MSTORE vb54(0x20), vb4f(0x0)
    0xb59: vb59(0x40) = CONST 
    0xb5c: vb5c = SHA3 vb4f(0x0), vb59(0x40)
    0xb5d: vb5d = SLOAD vb5c
    0xb5f: vb5f = GT v247, vb5d
    0xb60: vb60 = ISZERO vb5f
    0xb61: vb61(0xb69) = CONST 
    0xb64: JUMPI vb61(0xb69), vb60

    Begin block 0xb65
    prev=[0xb44], succ=[]
    =================================
    0xb65: vb65(0x0) = CONST 
    0xb68: REVERT vb65(0x0), vb65(0x0)

    Begin block 0xb69
    prev=[0xb44], succ=[0xb8e]
    =================================
    0xb6b: vb6b = CALLER 
    0xb6c: vb6c(0x1) = CONST 
    0xb6e: vb6e(0xa0) = CONST 
    0xb70: vb70(0x2) = CONST 
    0xb72: vb72(0x10000000000000000000000000000000000000000) = EXP vb70(0x2), vb6e(0xa0)
    0xb73: vb73(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb72(0x10000000000000000000000000000000000000000), vb6c(0x1)
    0xb75: vb75 = AND vb6b, vb73(0xffffffffffffffffffffffffffffffffffffffff)
    0xb76: vb76(0x0) = CONST 
    0xb7a: MSTORE vb76(0x0), vb75
    0xb7b: vb7b(0x20) = CONST 
    0xb7f: MSTORE vb7b(0x20), vb76(0x0)
    0xb80: vb80(0x40) = CONST 
    0xb83: vb83 = SHA3 vb76(0x0), vb80(0x40)
    0xb84: vb84 = SLOAD vb83
    0xb85: vb85(0xb8e) = CONST 
    0xb8a: vb8a(0xbfe) = CONST 
    0xb8d: vb8d_0 = CALLPRIVATE vb8a(0xbfe), v247, vb84, vb85(0xb8e)

    Begin block 0xb8e
    prev=[0xb69], succ=[0xbba]
    =================================
    0xb8f: vb8f(0x1) = CONST 
    0xb91: vb91(0xa0) = CONST 
    0xb93: vb93(0x2) = CONST 
    0xb95: vb95(0x10000000000000000000000000000000000000000) = EXP vb93(0x2), vb91(0xa0)
    0xb96: vb96(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb95(0x10000000000000000000000000000000000000000), vb8f(0x1)
    0xb98: vb98 = AND vb6b, vb96(0xffffffffffffffffffffffffffffffffffffffff)
    0xb99: vb99(0x0) = CONST 
    0xb9d: MSTORE vb99(0x0), vb98
    0xb9e: vb9e(0x20) = CONST 
    0xba2: MSTORE vb9e(0x20), vb99(0x0)
    0xba3: vba3(0x40) = CONST 
    0xba6: vba6 = SHA3 vb99(0x0), vba3(0x40)
    0xba7: SSTORE vba6, vb8d_0
    0xba8: vba8(0x1) = CONST 
    0xbaa: vbaa = SLOAD vba8(0x1)
    0xbab: vbab(0xbba) = CONST 
    0xbb0: vbb0(0xffffffff) = CONST 
    0xbb5: vbb5(0xbfe) = CONST 
    0xbb8: vbb8(0xbfe) = AND vbb5(0xbfe), vbb0(0xffffffff)
    0xbb9: vbb9_0 = CALLPRIVATE vbb8(0xbfe), v247, vbaa, vbab(0xbba)

    Begin block 0xbba
    prev=[0xb8e], succ=[0x508]
    =================================
    0xbbb: vbbb(0x1) = CONST 
    0xbbd: SSTORE vbbb(0x1), vbb9_0
    0xbbe: vbbe(0x1) = CONST 
    0xbc0: vbc0(0xa0) = CONST 
    0xbc2: vbc2(0x2) = CONST 
    0xbc4: vbc4(0x10000000000000000000000000000000000000000) = EXP vbc2(0x2), vbc0(0xa0)
    0xbc5: vbc5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbc4(0x10000000000000000000000000000000000000000), vbbe(0x1)
    0xbc7: vbc7 = AND vb6b, vbc5(0xffffffffffffffffffffffffffffffffffffffff)
    0xbc8: vbc8(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0xbea: vbea(0x40) = CONST 
    0xbec: vbec = MLOAD vbea(0x40)
    0xbef: MSTORE vbec, v247
    0xbf0: vbf0(0x20) = CONST 
    0xbf2: vbf2 = ADD vbf0(0x20), vbec
    0xbf3: vbf3(0x40) = CONST 
    0xbf5: vbf5 = MLOAD vbf3(0x40)
    0xbf8: vbf8(0x20) = SUB vbf2, vbf5
    0xbfa: LOG2 vbf5, vbf8(0x20), vbc8(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), vbc7
    0xbfd: JUMP v500(0x508)

    Begin block 0x508
    prev=[0xbba], succ=[0xc828]
    =================================
    0x509: v509(0x0) = CONST 
    0x50b: v50b = CALLER 
    0x50c: v50c(0x1) = CONST 
    0x50e: v50e(0xa0) = CONST 
    0x510: v510(0x2) = CONST 
    0x512: v512(0x10000000000000000000000000000000000000000) = EXP v510(0x2), v50e(0xa0)
    0x513: v513(0xffffffffffffffffffffffffffffffffffffffff) = SUB v512(0x10000000000000000000000000000000000000000), v50c(0x1)
    0x514: v514 = AND v513(0xffffffffffffffffffffffffffffffffffffffff), v50b
    0x515: v515(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x537: v537(0x40) = CONST 
    0x539: v539 = MLOAD v537(0x40)
    0x53c: MSTORE v539, v247
    0x53d: v53d(0x20) = CONST 
    0x53f: v53f = ADD v53d(0x20), v539
    0x540: v540(0x40) = CONST 
    0x542: v542 = MLOAD v540(0x40)
    0x545: v545(0x20) = SUB v53f, v542
    0x547: LOG3 v542, v545(0x20), v515(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v514, v509(0x0)
    0x549: JUMP v242(0xc828)

    Begin block 0xc828
    prev=[0x508], succ=[]
    =================================
    0xc829: STOP 

}

function tokenSaleContract()() public {
    Begin block 0x24e
    prev=[], succ=[0x255, 0x259]
    =================================
    0x24f: v24f = CALLVALUE 
    0x250: v250 = ISZERO v24f
    0x251: v251(0x259) = CONST 
    0x254: JUMPI v251(0x259), v250

    Begin block 0x255
    prev=[0x24e], succ=[]
    =================================
    0x255: v255(0x0) = CONST 
    0x258: REVERT v255(0x0), v255(0x0)

    Begin block 0x259
    prev=[0x24e], succ=[0x54a]
    =================================
    0x25a: v25a(0xc849) = CONST 
    0x25d: v25d(0x54a) = CONST 
    0x260: JUMP v25d(0x54a)

    Begin block 0x54a
    prev=[0x259], succ=[0xc849]
    =================================
    0x54b: v54b(0x4) = CONST 
    0x54d: v54d = SLOAD v54b(0x4)
    0x54e: v54e(0x1) = CONST 
    0x550: v550(0xa0) = CONST 
    0x552: v552(0x2) = CONST 
    0x554: v554(0x10000000000000000000000000000000000000000) = EXP v552(0x2), v550(0xa0)
    0x555: v555(0xffffffffffffffffffffffffffffffffffffffff) = SUB v554(0x10000000000000000000000000000000000000000), v54e(0x1)
    0x556: v556 = AND v555(0xffffffffffffffffffffffffffffffffffffffff), v54d
    0x558: JUMP v25a(0xc849)

    Begin block 0xc849
    prev=[0x54a], succ=[]
    =================================
    0xc84a: vc84a(0x40) = CONST 
    0xc84c: vc84c = MLOAD vc84a(0x40)
    0xc84d: vc84d(0x1) = CONST 
    0xc84f: vc84f(0xa0) = CONST 
    0xc851: vc851(0x2) = CONST 
    0xc853: vc853(0x10000000000000000000000000000000000000000) = EXP vc851(0x2), vc84f(0xa0)
    0xc854: vc854(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc853(0x10000000000000000000000000000000000000000), vc84d(0x1)
    0xc857: vc857 = AND v556, vc854(0xffffffffffffffffffffffffffffffffffffffff)
    0xc859: MSTORE vc84c, vc857
    0xc85a: vc85a(0x20) = CONST 
    0xc85c: vc85c = ADD vc85a(0x20), vc84c
    0xc85d: vc85d(0x40) = CONST 
    0xc85f: vc85f = MLOAD vc85d(0x40)
    0xc862: vc862(0x20) = SUB vc85c, vc85f
    0xc864: RETURN vc85f, vc862(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x27d
    prev=[], succ=[0x284, 0x288]
    =================================
    0x27e: v27e = CALLVALUE 
    0x27f: v27f = ISZERO v27e
    0x280: v280(0x288) = CONST 
    0x283: JUMPI v280(0x288), v27f

    Begin block 0x284
    prev=[0x27d], succ=[]
    =================================
    0x284: v284(0x0) = CONST 
    0x287: REVERT v284(0x0), v284(0x0)

    Begin block 0x288
    prev=[0x27d], succ=[0x559]
    =================================
    0x289: v289(0xc884) = CONST 
    0x28c: v28c(0x1) = CONST 
    0x28e: v28e(0xa0) = CONST 
    0x290: v290(0x2) = CONST 
    0x292: v292(0x10000000000000000000000000000000000000000) = EXP v290(0x2), v28e(0xa0)
    0x293: v293(0xffffffffffffffffffffffffffffffffffffffff) = SUB v292(0x10000000000000000000000000000000000000000), v28c(0x1)
    0x294: v294(0x4) = CONST 
    0x296: v296 = CALLDATALOAD v294(0x4)
    0x297: v297 = AND v296, v293(0xffffffffffffffffffffffffffffffffffffffff)
    0x298: v298(0x24) = CONST 
    0x29a: v29a = CALLDATALOAD v298(0x24)
    0x29b: v29b(0x559) = CONST 
    0x29e: JUMP v29b(0x559)

    Begin block 0x559
    prev=[0x288], succ=[0x58a, 0x5b6]
    =================================
    0x55a: v55a(0x1) = CONST 
    0x55c: v55c(0xa0) = CONST 
    0x55e: v55e(0x2) = CONST 
    0x560: v560(0x10000000000000000000000000000000000000000) = EXP v55e(0x2), v55c(0xa0)
    0x561: v561(0xffffffffffffffffffffffffffffffffffffffff) = SUB v560(0x10000000000000000000000000000000000000000), v55a(0x1)
    0x562: v562 = CALLER 
    0x564: v564 = AND v561(0xffffffffffffffffffffffffffffffffffffffff), v562
    0x565: v565(0x0) = CONST 
    0x569: MSTORE v565(0x0), v564
    0x56a: v56a(0x2) = CONST 
    0x56c: v56c(0x20) = CONST 
    0x570: MSTORE v56c(0x20), v56a(0x2)
    0x571: v571(0x40) = CONST 
    0x575: v575 = SHA3 v565(0x0), v571(0x40)
    0x578: v578 = AND v297, v561(0xffffffffffffffffffffffffffffffffffffffff)
    0x57a: MSTORE v565(0x0), v578
    0x57d: MSTORE v56c(0x20), v575
    0x580: v580 = SHA3 v565(0x0), v571(0x40)
    0x581: v581 = SLOAD v580
    0x584: v584 = GT v29a, v581
    0x585: v585 = ISZERO v584
    0x586: v586(0x5b6) = CONST 
    0x589: JUMPI v586(0x5b6), v585

    Begin block 0x58a
    prev=[0x559], succ=[0x5ed]
    =================================
    0x58a: v58a(0x1) = CONST 
    0x58c: v58c(0xa0) = CONST 
    0x58e: v58e(0x2) = CONST 
    0x590: v590(0x10000000000000000000000000000000000000000) = EXP v58e(0x2), v58c(0xa0)
    0x591: v591(0xffffffffffffffffffffffffffffffffffffffff) = SUB v590(0x10000000000000000000000000000000000000000), v58a(0x1)
    0x592: v592 = CALLER 
    0x594: v594 = AND v591(0xffffffffffffffffffffffffffffffffffffffff), v592
    0x595: v595(0x0) = CONST 
    0x599: MSTORE v595(0x0), v594
    0x59a: v59a(0x2) = CONST 
    0x59c: v59c(0x20) = CONST 
    0x5a0: MSTORE v59c(0x20), v59a(0x2)
    0x5a1: v5a1(0x40) = CONST 
    0x5a5: v5a5 = SHA3 v595(0x0), v5a1(0x40)
    0x5a8: v5a8 = AND v297, v591(0xffffffffffffffffffffffffffffffffffffffff)
    0x5aa: MSTORE v595(0x0), v5a8
    0x5ad: MSTORE v59c(0x20), v5a5
    0x5b0: v5b0 = SHA3 v595(0x0), v5a1(0x40)
    0x5b1: SSTORE v5b0, v595(0x0)
    0x5b2: v5b2(0x5ed) = CONST 
    0x5b5: JUMP v5b2(0x5ed)

    Begin block 0x5ed
    prev=[0x58a, 0x5c6], succ=[0xc884]
    =================================
    0x5ee: v5ee(0x1) = CONST 
    0x5f0: v5f0(0xa0) = CONST 
    0x5f2: v5f2(0x2) = CONST 
    0x5f4: v5f4(0x10000000000000000000000000000000000000000) = EXP v5f2(0x2), v5f0(0xa0)
    0x5f5: v5f5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5f4(0x10000000000000000000000000000000000000000), v5ee(0x1)
    0x5f6: v5f6 = CALLER 
    0x5f8: v5f8 = AND v5f5(0xffffffffffffffffffffffffffffffffffffffff), v5f6
    0x5f9: v5f9(0x0) = CONST 
    0x5fd: MSTORE v5f9(0x0), v5f8
    0x5fe: v5fe(0x2) = CONST 
    0x600: v600(0x20) = CONST 
    0x604: MSTORE v600(0x20), v5fe(0x2)
    0x605: v605(0x40) = CONST 
    0x609: v609 = SHA3 v5f9(0x0), v605(0x40)
    0x60c: v60c = AND v297, v5f5(0xffffffffffffffffffffffffffffffffffffffff)
    0x60f: MSTORE v5f9(0x0), v60c
    0x613: MSTORE v600(0x20), v609
    0x617: v617 = SHA3 v5f9(0x0), v605(0x40)
    0x618: v618 = SLOAD v617
    0x619: v619(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x63b: v63b = MLOAD v605(0x40)
    0x63e: MSTORE v63b, v618
    0x63f: v63f(0x20) = CONST 
    0x641: v641 = ADD v63f(0x20), v63b
    0x642: v642(0x40) = CONST 
    0x644: v644 = MLOAD v642(0x40)
    0x647: v647(0x20) = SUB v641, v644
    0x649: LOG3 v644, v647(0x20), v619(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v5f8, v60c
    0x64b: v64b(0x1) = CONST 
    0x652: JUMP v289(0xc884)

    Begin block 0xc884
    prev=[0x5ed], succ=[]
    =================================
    0xc885: vc885(0x40) = CONST 
    0xc887: vc887 = MLOAD vc885(0x40)
    0xc889: vc889(0x0) = ISZERO v64b(0x1)
    0xc88a: vc88a(0x1) = ISZERO vc889(0x0)
    0xc88c: MSTORE vc887, vc88a(0x1)
    0xc88d: vc88d(0x20) = CONST 
    0xc88f: vc88f = ADD vc88d(0x20), vc887
    0xc890: vc890(0x40) = CONST 
    0xc892: vc892 = MLOAD vc890(0x40)
    0xc895: vc895(0x20) = SUB vc88f, vc892
    0xc897: RETURN vc892, vc895(0x20)

    Begin block 0x5b6
    prev=[0x559], succ=[0x5c6]
    =================================
    0x5b7: v5b7(0x5c6) = CONST 
    0x5bc: v5bc(0xffffffff) = CONST 
    0x5c1: v5c1(0xbfe) = CONST 
    0x5c4: v5c4(0xbfe) = AND v5c1(0xbfe), v5bc(0xffffffff)
    0x5c5: v5c5_0 = CALLPRIVATE v5c4(0xbfe), v29a, v581, v5b7(0x5c6)

    Begin block 0x5c6
    prev=[0x5b6], succ=[0x5ed]
    =================================
    0x5c7: v5c7(0x1) = CONST 
    0x5c9: v5c9(0xa0) = CONST 
    0x5cb: v5cb(0x2) = CONST 
    0x5cd: v5cd(0x10000000000000000000000000000000000000000) = EXP v5cb(0x2), v5c9(0xa0)
    0x5ce: v5ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5cd(0x10000000000000000000000000000000000000000), v5c7(0x1)
    0x5cf: v5cf = CALLER 
    0x5d1: v5d1 = AND v5ce(0xffffffffffffffffffffffffffffffffffffffff), v5cf
    0x5d2: v5d2(0x0) = CONST 
    0x5d6: MSTORE v5d2(0x0), v5d1
    0x5d7: v5d7(0x2) = CONST 
    0x5d9: v5d9(0x20) = CONST 
    0x5dd: MSTORE v5d9(0x20), v5d7(0x2)
    0x5de: v5de(0x40) = CONST 
    0x5e2: v5e2 = SHA3 v5d2(0x0), v5de(0x40)
    0x5e5: v5e5 = AND v297, v5ce(0xffffffffffffffffffffffffffffffffffffffff)
    0x5e7: MSTORE v5d2(0x0), v5e5
    0x5ea: MSTORE v5d9(0x20), v5e2
    0x5eb: v5eb = SHA3 v5d2(0x0), v5de(0x40)
    0x5ec: SSTORE v5eb, v5c5_0
    0x42ac: v42ac(0x5ed) = CONST 
    0x42cc: JUMP v42ac(0x5ed)

}

function balanceOf(address)() public {
    Begin block 0x29f
    prev=[], succ=[0x2a6, 0x2aa]
    =================================
    0x2a0: v2a0 = CALLVALUE 
    0x2a1: v2a1 = ISZERO v2a0
    0x2a2: v2a2(0x2aa) = CONST 
    0x2a5: JUMPI v2a2(0x2aa), v2a1

    Begin block 0x2a6
    prev=[0x29f], succ=[]
    =================================
    0x2a6: v2a6(0x0) = CONST 
    0x2a9: REVERT v2a6(0x0), v2a6(0x0)

    Begin block 0x2aa
    prev=[0x29f], succ=[0x653]
    =================================
    0x2ab: v2ab(0xc8b7) = CONST 
    0x2ae: v2ae(0x1) = CONST 
    0x2b0: v2b0(0xa0) = CONST 
    0x2b2: v2b2(0x2) = CONST 
    0x2b4: v2b4(0x10000000000000000000000000000000000000000) = EXP v2b2(0x2), v2b0(0xa0)
    0x2b5: v2b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b4(0x10000000000000000000000000000000000000000), v2ae(0x1)
    0x2b6: v2b6(0x4) = CONST 
    0x2b8: v2b8 = CALLDATALOAD v2b6(0x4)
    0x2b9: v2b9 = AND v2b8, v2b5(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ba: v2ba(0x653) = CONST 
    0x2bd: JUMP v2ba(0x653)

    Begin block 0x653
    prev=[0x2aa], succ=[0xc8b7]
    =================================
    0x654: v654(0x1) = CONST 
    0x656: v656(0xa0) = CONST 
    0x658: v658(0x2) = CONST 
    0x65a: v65a(0x10000000000000000000000000000000000000000) = EXP v658(0x2), v656(0xa0)
    0x65b: v65b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v65a(0x10000000000000000000000000000000000000000), v654(0x1)
    0x65c: v65c = AND v65b(0xffffffffffffffffffffffffffffffffffffffff), v2b9
    0x65d: v65d(0x0) = CONST 
    0x661: MSTORE v65d(0x0), v65c
    0x662: v662(0x20) = CONST 
    0x666: MSTORE v662(0x20), v65d(0x0)
    0x667: v667(0x40) = CONST 
    0x66a: v66a = SHA3 v65d(0x0), v667(0x40)
    0x66b: v66b = SLOAD v66a
    0x66d: JUMP v2ab(0xc8b7)

    Begin block 0xc8b7
    prev=[0x653], succ=[]
    =================================
    0xc8b8: vc8b8(0x40) = CONST 
    0xc8ba: vc8ba = MLOAD vc8b8(0x40)
    0xc8bd: MSTORE vc8ba, v66b
    0xc8be: vc8be(0x20) = CONST 
    0xc8c0: vc8c0 = ADD vc8be(0x20), vc8ba
    0xc8c1: vc8c1(0x40) = CONST 
    0xc8c3: vc8c3 = MLOAD vc8c1(0x40)
    0xc8c6: vc8c6(0x20) = SUB vc8c0, vc8c3
    0xc8c8: RETURN vc8c3, vc8c6(0x20)

}

function owner()() public {
    Begin block 0x2be
    prev=[], succ=[0x2c5, 0x2c9]
    =================================
    0x2bf: v2bf = CALLVALUE 
    0x2c0: v2c0 = ISZERO v2bf
    0x2c1: v2c1(0x2c9) = CONST 
    0x2c4: JUMPI v2c1(0x2c9), v2c0

    Begin block 0x2c5
    prev=[0x2be], succ=[]
    =================================
    0x2c5: v2c5(0x0) = CONST 
    0x2c8: REVERT v2c5(0x0), v2c5(0x0)

    Begin block 0x2c9
    prev=[0x2be], succ=[0x66e]
    =================================
    0x2ca: v2ca(0xc8e8) = CONST 
    0x2cd: v2cd(0x66e) = CONST 
    0x2d0: JUMP v2cd(0x66e)

    Begin block 0x66e
    prev=[0x2c9], succ=[0xc8e8]
    =================================
    0x66f: v66f(0x3) = CONST 
    0x671: v671 = SLOAD v66f(0x3)
    0x672: v672(0x1) = CONST 
    0x674: v674(0xa0) = CONST 
    0x676: v676(0x2) = CONST 
    0x678: v678(0x10000000000000000000000000000000000000000) = EXP v676(0x2), v674(0xa0)
    0x679: v679(0xffffffffffffffffffffffffffffffffffffffff) = SUB v678(0x10000000000000000000000000000000000000000), v672(0x1)
    0x67a: v67a = AND v679(0xffffffffffffffffffffffffffffffffffffffff), v671
    0x67c: JUMP v2ca(0xc8e8)

    Begin block 0xc8e8
    prev=[0x66e], succ=[]
    =================================
    0xc8e9: vc8e9(0x40) = CONST 
    0xc8eb: vc8eb = MLOAD vc8e9(0x40)
    0xc8ec: vc8ec(0x1) = CONST 
    0xc8ee: vc8ee(0xa0) = CONST 
    0xc8f0: vc8f0(0x2) = CONST 
    0xc8f2: vc8f2(0x10000000000000000000000000000000000000000) = EXP vc8f0(0x2), vc8ee(0xa0)
    0xc8f3: vc8f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc8f2(0x10000000000000000000000000000000000000000), vc8ec(0x1)
    0xc8f6: vc8f6 = AND v67a, vc8f3(0xffffffffffffffffffffffffffffffffffffffff)
    0xc8f8: MSTORE vc8eb, vc8f6
    0xc8f9: vc8f9(0x20) = CONST 
    0xc8fb: vc8fb = ADD vc8f9(0x20), vc8eb
    0xc8fc: vc8fc(0x40) = CONST 
    0xc8fe: vc8fe = MLOAD vc8fc(0x40)
    0xc901: vc901(0x20) = SUB vc8fb, vc8fe
    0xc903: RETURN vc8fe, vc901(0x20)

}

function isTokenTransferable()() public {
    Begin block 0x2d1
    prev=[], succ=[0x2d8, 0x2dc]
    =================================
    0x2d2: v2d2 = CALLVALUE 
    0x2d3: v2d3 = ISZERO v2d2
    0x2d4: v2d4(0x2dc) = CONST 
    0x2d7: JUMPI v2d4(0x2dc), v2d3

    Begin block 0x2d8
    prev=[0x2d1], succ=[]
    =================================
    0x2d8: v2d8(0x0) = CONST 
    0x2db: REVERT v2d8(0x0), v2d8(0x0)

    Begin block 0x2dc
    prev=[0x2d1], succ=[0x67d]
    =================================
    0x2dd: v2dd(0xc923) = CONST 
    0x2e0: v2e0(0x67d) = CONST 
    0x2e3: JUMP v2e0(0x67d)

    Begin block 0x67d
    prev=[0x2dc], succ=[0xc923]
    =================================
    0x67e: v67e(0x4) = CONST 
    0x680: v680 = SLOAD v67e(0x4)
    0x681: v681(0xa0) = CONST 
    0x683: v683(0x2) = CONST 
    0x685: v685(0x10000000000000000000000000000000000000000) = EXP v683(0x2), v681(0xa0)
    0x687: v687 = DIV v680, v685(0x10000000000000000000000000000000000000000)
    0x688: v688(0xff) = CONST 
    0x68a: v68a = AND v688(0xff), v687
    0x68c: JUMP v2dd(0xc923)

    Begin block 0xc923
    prev=[0x67d], succ=[]
    =================================
    0xc924: vc924(0x40) = CONST 
    0xc926: vc926 = MLOAD vc924(0x40)
    0xc928: vc928 = ISZERO v68a
    0xc929: vc929 = ISZERO vc928
    0xc92b: MSTORE vc926, vc929
    0xc92c: vc92c(0x20) = CONST 
    0xc92e: vc92e = ADD vc92c(0x20), vc926
    0xc92f: vc92f(0x40) = CONST 
    0xc931: vc931 = MLOAD vc92f(0x40)
    0xc934: vc934(0x20) = SUB vc92e, vc931
    0xc936: RETURN vc931, vc934(0x20)

}

function symbol()() public {
    Begin block 0x2e4
    prev=[], succ=[0x2eb, 0x2ef]
    =================================
    0x2e5: v2e5 = CALLVALUE 
    0x2e6: v2e6 = ISZERO v2e5
    0x2e7: v2e7(0x2ef) = CONST 
    0x2ea: JUMPI v2e7(0x2ef), v2e6

    Begin block 0x2eb
    prev=[0x2e4], succ=[]
    =================================
    0x2eb: v2eb(0x0) = CONST 
    0x2ee: REVERT v2eb(0x0), v2eb(0x0)

    Begin block 0x2ef
    prev=[0x2e4], succ=[0x68d]
    =================================
    0x2f0: v2f0(0xc956) = CONST 
    0x2f3: v2f3(0x68d) = CONST 
    0x2f6: JUMP v2f3(0x68d)

    Begin block 0x68d
    prev=[0x2ef], succ=[0xc956]
    =================================
    0x68e: v68e(0x40) = CONST 
    0x691: v691 = MLOAD v68e(0x40)
    0x694: v694 = ADD v691, v68e(0x40)
    0x695: v695(0x40) = CONST 
    0x697: MSTORE v695(0x40), v694
    0x698: v698(0x3) = CONST 
    0x69b: MSTORE v691, v698(0x3)
    0x69c: v69c(0x50414c0000000000000000000000000000000000000000000000000000000000) = CONST 
    0x6bd: v6bd(0x20) = CONST 
    0x6c0: v6c0 = ADD v691, v6bd(0x20)
    0x6c1: MSTORE v6c0, v69c(0x50414c0000000000000000000000000000000000000000000000000000000000)
    0x6c3: JUMP v2f0(0xc956)

    Begin block 0xc956
    prev=[0x68d], succ=[0x1370x2e4]
    =================================
    0xc957: vc957(0x40) = CONST 
    0xc959: vc959 = MLOAD vc957(0x40)
    0xc95a: vc95a(0x20) = CONST 
    0xc95e: MSTORE vc959, vc95a(0x20)
    0xc962: vc962 = ADD vc959, vc95a(0x20)
    0xc966: vc966(0x3) = MLOAD v691
    0xc968: MSTORE vc962, vc966(0x3)
    0xc969: vc969(0x20) = CONST 
    0xc96b: vc96b = ADD vc969(0x20), vc962
    0xc96f: vc96f(0x3) = MLOAD v691
    0xc971: vc971(0x20) = CONST 
    0xc973: vc973 = ADD vc971(0x20), v691
    0xc978: vc978(0x0) = CONST 
    0xe2ef: ve2ef(0x137) = CONST 
    0xe30f: JUMP ve2ef(0x137)

    Begin block 0x1370x2e4
    prev=[0xc956, 0x1400x2e4], succ=[0x14f0x2e4, 0x1400x2e4]
    =================================
    0x1370x2e4_0x0: v1372e4_0 = PHI vc978(0x0), v2e414a
    0x13a0x2e4: v2e413a = LT v1372e4_0, vc96f(0x3)
    0x13b0x2e4: v2e413b = ISZERO v2e413a
    0x13c0x2e4: v2e413c(0x14f) = CONST 
    0x13f0x2e4: JUMPI v2e413c(0x14f), v2e413b

    Begin block 0x14f0x2e4
    prev=[0x1370x2e4], succ=[0x1630x2e4, 0x17c0x2e4]
    =================================
    0x1580x2e4: v2e4158 = ADD vc96f(0x3), vc96b
    0x15a0x2e4: v2e415a(0x1f) = CONST 
    0x15c0x2e4: v2e415c(0x3) = AND v2e415a(0x1f), vc96f(0x3)
    0x15e0x2e4: v2e415e(0x0) = ISZERO v2e415c(0x3)
    0x15f0x2e4: v2e415f(0x17c) = CONST 
    0x1620x2e4: JUMPI v2e415f(0x17c), v2e415e(0x0)

    Begin block 0x1630x2e4
    prev=[0x14f0x2e4], succ=[0x17c0x2e4]
    =================================
    0x1650x2e4: v2e4165 = SUB v2e4158, v2e415c(0x3)
    0x1670x2e4: v2e4167 = MLOAD v2e4165
    0x1680x2e4: v2e4168(0x1) = CONST 
    0x16b0x2e4: v2e416b(0x20) = CONST 
    0x16d0x2e4: v2e416d(0x1d) = SUB v2e416b(0x20), v2e415c(0x3)
    0x16e0x2e4: v2e416e(0x100) = CONST 
    0x1710x2e4: v2e4171(0x10000000000000000000000000000000000000000000000000000000000) = EXP v2e416e(0x100), v2e416d(0x1d)
    0x1720x2e4: v2e4172(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2e4171(0x10000000000000000000000000000000000000000000000000000000000), v2e4168(0x1)
    0x1730x2e4: v2e4173(0xffffff0000000000000000000000000000000000000000000000000000000000) = NOT v2e4172(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1740x2e4: v2e4174 = AND v2e4173(0xffffff0000000000000000000000000000000000000000000000000000000000), v2e4167
    0x1760x2e4: MSTORE v2e4165, v2e4174
    0x1770x2e4: v2e4177(0x20) = CONST 
    0x1790x2e4: v2e4179 = ADD v2e4177(0x20), v2e4165
    0x24ac0x2e4: v2e424ac(0x17c) = CONST 
    0x24cc0x2e4: JUMP v2e424ac(0x17c)

    Begin block 0x17c0x2e4
    prev=[0x1630x2e4, 0x14f0x2e4], succ=[]
    =================================
    0x17c0x2e4_0x1: v17c2e4_1 = PHI v2e4179, v2e4158
    0x1820x2e4: v2e4182(0x40) = CONST 
    0x1840x2e4: v2e4184 = MLOAD v2e4182(0x40)
    0x1870x2e4: v2e4187 = SUB v17c2e4_1, v2e4184
    0x1890x2e4: RETURN v2e4184, v2e4187

    Begin block 0x1400x2e4
    prev=[0x1370x2e4], succ=[0x1370x2e4]
    =================================
    0x1400x2e4_0x0: v1402e4_0 = PHI vc978(0x0), v2e414a
    0x1420x2e4: v2e4142 = ADD vc973, v1402e4_0
    0x1430x2e4: v2e4143 = MLOAD v2e4142
    0x1460x2e4: v2e4146 = ADD v1402e4_0, vc96b
    0x1470x2e4: MSTORE v2e4146, v2e4143
    0x1480x2e4: v2e4148(0x20) = CONST 
    0x14a0x2e4: v2e414a = ADD v2e4148(0x20), v1402e4_0
    0x14b0x2e4: v2e414b(0x137) = CONST 
    0x14e0x2e4: JUMP v2e414b(0x137)

}

function transfer(address,uint256)() public {
    Begin block 0x2f7
    prev=[], succ=[0x2fe, 0x302]
    =================================
    0x2f8: v2f8 = CALLVALUE 
    0x2f9: v2f9 = ISZERO v2f8
    0x2fa: v2fa(0x302) = CONST 
    0x2fd: JUMPI v2fa(0x302), v2f9

    Begin block 0x2fe
    prev=[0x2f7], succ=[]
    =================================
    0x2fe: v2fe(0x0) = CONST 
    0x301: REVERT v2fe(0x0), v2fe(0x0)

    Begin block 0x302
    prev=[0x2f7], succ=[0x6c4B0x302]
    =================================
    0x303: v303(0xe32f) = CONST 
    0x306: v306(0x1) = CONST 
    0x308: v308(0xa0) = CONST 
    0x30a: v30a(0x2) = CONST 
    0x30c: v30c(0x10000000000000000000000000000000000000000) = EXP v30a(0x2), v308(0xa0)
    0x30d: v30d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30c(0x10000000000000000000000000000000000000000), v306(0x1)
    0x30e: v30e(0x4) = CONST 
    0x310: v310 = CALLDATALOAD v30e(0x4)
    0x311: v311 = AND v310, v30d(0xffffffffffffffffffffffffffffffffffffffff)
    0x312: v312(0x24) = CONST 
    0x314: v314 = CALLDATALOAD v312(0x24)
    0x315: v315(0x6c4) = CONST 
    0x318: JUMP v315(0x6c4)

    Begin block 0x6c4B0x302
    prev=[0x302], succ=[0x6edB0x302, 0x6daB0x302]
    =================================
    0x6c5S0x302: v6c5V302(0x4) = CONST 
    0x6c7S0x302: v6c7V302 = SLOAD v6c5V302(0x4)
    0x6c8S0x302: v6c8V302(0x0) = CONST 
    0x6cbS0x302: v6cbV302(0xa0) = CONST 
    0x6cdS0x302: v6cdV302(0x2) = CONST 
    0x6cfS0x302: v6cfV302(0x10000000000000000000000000000000000000000) = EXP v6cdV302(0x2), v6cbV302(0xa0)
    0x6d1S0x302: v6d1V302 = DIV v6c7V302, v6cfV302(0x10000000000000000000000000000000000000000)
    0x6d2S0x302: v6d2V302(0xff) = CONST 
    0x6d4S0x302: v6d4V302 = AND v6d2V302(0xff), v6d1V302
    0x6d6S0x302: v6d6V302(0x6ed) = CONST 
    0x6d9S0x302: JUMPI v6d6V302(0x6ed), v6d4V302

    Begin block 0x6edB0x302
    prev=[0x6c4B0x302, 0x6daB0x302], succ=[0x706B0x302, 0x6f3B0x302]
    =================================
    0x6ed_0x0S0x302: v6ed_0V302 = PHI v6d4V302, v6ecV302
    0x6efS0x302: v6efV302(0x706) = CONST 
    0x6f2S0x302: JUMPI v6efV302(0x706), v6ed_0V302

    Begin block 0x706B0x302
    prev=[0x6edB0x302, 0x6f3B0x302], succ=[0x70dB0x302, 0x711B0x302]
    =================================
    0x706_0x0S0x302: v706_0V302 = PHI v6d4V302, v6ecV302, v705V302
    0x707S0x302: v707V302 = ISZERO v706_0V302
    0x708S0x302: v708V302 = ISZERO v707V302
    0x709S0x302: v709V302(0x711) = CONST 
    0x70cS0x302: JUMPI v709V302(0x711), v708V302

    Begin block 0x70dB0x302
    prev=[0x706B0x302], succ=[]
    =================================
    0x70dS0x302: v70dV302(0x0) = CONST 
    0x710S0x302: REVERT v70dV302(0x0), v70dV302(0x0)

    Begin block 0x711B0x302
    prev=[0x706B0x302], succ=[0x723B0x302, 0x727B0x302]
    =================================
    0x713S0x302: v713V302(0x1) = CONST 
    0x715S0x302: v715V302(0xa0) = CONST 
    0x717S0x302: v717V302(0x2) = CONST 
    0x719S0x302: v719V302(0x10000000000000000000000000000000000000000) = EXP v717V302(0x2), v715V302(0xa0)
    0x71aS0x302: v71aV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB v719V302(0x10000000000000000000000000000000000000000), v713V302(0x1)
    0x71cS0x302: v71cV302 = AND v311, v71aV302(0xffffffffffffffffffffffffffffffffffffffff)
    0x71dS0x302: v71dV302 = ISZERO v71cV302
    0x71eS0x302: v71eV302 = ISZERO v71dV302
    0x71fS0x302: v71fV302(0x727) = CONST 
    0x722S0x302: JUMPI v71fV302(0x727), v71eV302

    Begin block 0x723B0x302
    prev=[0x711B0x302], succ=[]
    =================================
    0x723S0x302: v723V302(0x0) = CONST 
    0x726S0x302: REVERT v723V302(0x0), v723V302(0x0)

    Begin block 0x727B0x302
    prev=[0x711B0x302], succ=[0x744B0x302, 0x748B0x302]
    =================================
    0x728S0x302: v728V302 = ADDRESS 
    0x729S0x302: v729V302(0x1) = CONST 
    0x72bS0x302: v72bV302(0xa0) = CONST 
    0x72dS0x302: v72dV302(0x2) = CONST 
    0x72fS0x302: v72fV302(0x10000000000000000000000000000000000000000) = EXP v72dV302(0x2), v72bV302(0xa0)
    0x730S0x302: v730V302(0xffffffffffffffffffffffffffffffffffffffff) = SUB v72fV302(0x10000000000000000000000000000000000000000), v729V302(0x1)
    0x731S0x302: v731V302 = AND v730V302(0xffffffffffffffffffffffffffffffffffffffff), v728V302
    0x733S0x302: v733V302(0x1) = CONST 
    0x735S0x302: v735V302(0xa0) = CONST 
    0x737S0x302: v737V302(0x2) = CONST 
    0x739S0x302: v739V302(0x10000000000000000000000000000000000000000) = EXP v737V302(0x2), v735V302(0xa0)
    0x73aS0x302: v73aV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB v739V302(0x10000000000000000000000000000000000000000), v733V302(0x1)
    0x73bS0x302: v73bV302 = AND v73aV302(0xffffffffffffffffffffffffffffffffffffffff), v311
    0x73cS0x302: v73cV302 = EQ v73bV302, v731V302
    0x73dS0x302: v73dV302 = ISZERO v73cV302
    0x73eS0x302: v73eV302 = ISZERO v73dV302
    0x73fS0x302: v73fV302 = ISZERO v73eV302
    0x740S0x302: v740V302(0x748) = CONST 
    0x743S0x302: JUMPI v740V302(0x748), v73fV302

    Begin block 0x744B0x302
    prev=[0x727B0x302], succ=[]
    =================================
    0x744S0x302: v744V302(0x0) = CONST 
    0x747S0x302: REVERT v744V302(0x0), v744V302(0x0)

    Begin block 0x748B0x302
    prev=[0x727B0x302], succ=[0xc10B0x302]
    =================================
    0x749S0x302: v749V302(0x752) = CONST 
    0x74eS0x302: v74eV302(0xc10) = CONST 
    0x751S0x302: JUMP v74eV302(0xc10)

    Begin block 0xc10B0x302
    prev=[0x748B0x302], succ=[0xc23B0x302, 0xc27B0x302]
    =================================
    0xc11S0x302: vc11V302(0x0) = CONST 
    0xc13S0x302: vc13V302(0x1) = CONST 
    0xc15S0x302: vc15V302(0xa0) = CONST 
    0xc17S0x302: vc17V302(0x2) = CONST 
    0xc19S0x302: vc19V302(0x10000000000000000000000000000000000000000) = EXP vc17V302(0x2), vc15V302(0xa0)
    0xc1aS0x302: vc1aV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc19V302(0x10000000000000000000000000000000000000000), vc13V302(0x1)
    0xc1cS0x302: vc1cV302 = AND v311, vc1aV302(0xffffffffffffffffffffffffffffffffffffffff)
    0xc1dS0x302: vc1dV302 = ISZERO vc1cV302
    0xc1eS0x302: vc1eV302 = ISZERO vc1dV302
    0xc1fS0x302: vc1fV302(0xc27) = CONST 
    0xc22S0x302: JUMPI vc1fV302(0xc27), vc1eV302

    Begin block 0xc23B0x302
    prev=[0xc10B0x302], succ=[]
    =================================
    0xc23S0x302: vc23V302(0x0) = CONST 
    0xc26S0x302: REVERT vc23V302(0x0), vc23V302(0x0)

    Begin block 0xc27B0x302
    prev=[0xc10B0x302], succ=[0xc48B0x302, 0xc4cB0x302]
    =================================
    0xc28S0x302: vc28V302(0x1) = CONST 
    0xc2aS0x302: vc2aV302(0xa0) = CONST 
    0xc2cS0x302: vc2cV302(0x2) = CONST 
    0xc2eS0x302: vc2eV302(0x10000000000000000000000000000000000000000) = EXP vc2cV302(0x2), vc2aV302(0xa0)
    0xc2fS0x302: vc2fV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc2eV302(0x10000000000000000000000000000000000000000), vc28V302(0x1)
    0xc30S0x302: vc30V302 = CALLER 
    0xc31S0x302: vc31V302 = AND vc30V302, vc2fV302(0xffffffffffffffffffffffffffffffffffffffff)
    0xc32S0x302: vc32V302(0x0) = CONST 
    0xc36S0x302: MSTORE vc32V302(0x0), vc31V302
    0xc37S0x302: vc37V302(0x20) = CONST 
    0xc3bS0x302: MSTORE vc37V302(0x20), vc32V302(0x0)
    0xc3cS0x302: vc3cV302(0x40) = CONST 
    0xc3fS0x302: vc3fV302 = SHA3 vc32V302(0x0), vc3cV302(0x40)
    0xc40S0x302: vc40V302 = SLOAD vc3fV302
    0xc42S0x302: vc42V302 = GT v314, vc40V302
    0xc43S0x302: vc43V302 = ISZERO vc42V302
    0xc44S0x302: vc44V302(0xc4c) = CONST 
    0xc47S0x302: JUMPI vc44V302(0xc4c), vc43V302

    Begin block 0xc48B0x302
    prev=[0xc27B0x302], succ=[]
    =================================
    0xc48S0x302: vc48V302(0x0) = CONST 
    0xc4bS0x302: REVERT vc48V302(0x0), vc48V302(0x0)

    Begin block 0xc4cB0x302
    prev=[0xc27B0x302], succ=[0xc75B0x302]
    =================================
    0xc4dS0x302: vc4dV302(0x1) = CONST 
    0xc4fS0x302: vc4fV302(0xa0) = CONST 
    0xc51S0x302: vc51V302(0x2) = CONST 
    0xc53S0x302: vc53V302(0x10000000000000000000000000000000000000000) = EXP vc51V302(0x2), vc4fV302(0xa0)
    0xc54S0x302: vc54V302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc53V302(0x10000000000000000000000000000000000000000), vc4dV302(0x1)
    0xc55S0x302: vc55V302 = CALLER 
    0xc56S0x302: vc56V302 = AND vc55V302, vc54V302(0xffffffffffffffffffffffffffffffffffffffff)
    0xc57S0x302: vc57V302(0x0) = CONST 
    0xc5bS0x302: MSTORE vc57V302(0x0), vc56V302
    0xc5cS0x302: vc5cV302(0x20) = CONST 
    0xc60S0x302: MSTORE vc5cV302(0x20), vc57V302(0x0)
    0xc61S0x302: vc61V302(0x40) = CONST 
    0xc64S0x302: vc64V302 = SHA3 vc57V302(0x0), vc61V302(0x40)
    0xc65S0x302: vc65V302 = SLOAD vc64V302
    0xc66S0x302: vc66V302(0xc75) = CONST 
    0xc6bS0x302: vc6bV302(0xffffffff) = CONST 
    0xc70S0x302: vc70V302(0xbfe) = CONST 
    0xc73S0x302: vc73V302(0xbfe) = AND vc70V302(0xbfe), vc6bV302(0xffffffff)
    0xc74S0x302: vc74_0V302 = CALLPRIVATE vc73V302(0xbfe), v314, vc65V302, vc66V302(0xc75)

    Begin block 0xc75B0x302
    prev=[0xc4cB0x302], succ=[0xcaaB0x302]
    =================================
    0xc76S0x302: vc76V302(0x1) = CONST 
    0xc78S0x302: vc78V302(0xa0) = CONST 
    0xc7aS0x302: vc7aV302(0x2) = CONST 
    0xc7cS0x302: vc7cV302(0x10000000000000000000000000000000000000000) = EXP vc7aV302(0x2), vc78V302(0xa0)
    0xc7dS0x302: vc7dV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc7cV302(0x10000000000000000000000000000000000000000), vc76V302(0x1)
    0xc7eS0x302: vc7eV302 = CALLER 
    0xc80S0x302: vc80V302 = AND vc7dV302(0xffffffffffffffffffffffffffffffffffffffff), vc7eV302
    0xc81S0x302: vc81V302(0x0) = CONST 
    0xc85S0x302: MSTORE vc81V302(0x0), vc80V302
    0xc86S0x302: vc86V302(0x20) = CONST 
    0xc8aS0x302: MSTORE vc86V302(0x20), vc81V302(0x0)
    0xc8bS0x302: vc8bV302(0x40) = CONST 
    0xc8fS0x302: vc8fV302 = SHA3 vc81V302(0x0), vc8bV302(0x40)
    0xc93S0x302: SSTORE vc8fV302, vc74_0V302
    0xc96S0x302: vc96V302 = AND v311, vc7dV302(0xffffffffffffffffffffffffffffffffffffffff)
    0xc98S0x302: MSTORE vc81V302(0x0), vc96V302
    0xc99S0x302: vc99V302 = SHA3 vc81V302(0x0), vc8bV302(0x40)
    0xc9aS0x302: vc9aV302 = SLOAD vc99V302
    0xc9bS0x302: vc9bV302(0xcaa) = CONST 
    0xca0S0x302: vca0V302(0xffffffff) = CONST 
    0xca5S0x302: vca5V302(0xd22) = CONST 
    0xca8S0x302: vca8V302(0xd22) = AND vca5V302(0xd22), vca0V302(0xffffffff)
    0xca9S0x302: vca9_0V302 = CALLPRIVATE vca8V302(0xd22), v314, vc9aV302, vc9bV302(0xcaa)

    Begin block 0xcaaB0x302
    prev=[0xc75B0x302], succ=[0x752B0x302]
    =================================
    0xcabS0x302: vcabV302(0x0) = CONST 
    0xcafS0x302: vcafV302(0x1) = CONST 
    0xcb1S0x302: vcb1V302(0xa0) = CONST 
    0xcb3S0x302: vcb3V302(0x2) = CONST 
    0xcb5S0x302: vcb5V302(0x10000000000000000000000000000000000000000) = EXP vcb3V302(0x2), vcb1V302(0xa0)
    0xcb6S0x302: vcb6V302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcb5V302(0x10000000000000000000000000000000000000000), vcafV302(0x1)
    0xcb7S0x302: vcb7V302 = AND vcb6V302(0xffffffffffffffffffffffffffffffffffffffff), v311
    0xcb8S0x302: vcb8V302(0x1) = CONST 
    0xcbaS0x302: vcbaV302(0xa0) = CONST 
    0xcbcS0x302: vcbcV302(0x2) = CONST 
    0xcbeS0x302: vcbeV302(0x10000000000000000000000000000000000000000) = EXP vcbcV302(0x2), vcbaV302(0xa0)
    0xcbfS0x302: vcbfV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcbeV302(0x10000000000000000000000000000000000000000), vcb8V302(0x1)
    0xcc0S0x302: vcc0V302 = AND vcbfV302(0xffffffffffffffffffffffffffffffffffffffff), vcb7V302
    0xcc2S0x302: MSTORE vcabV302(0x0), vcc0V302
    0xcc3S0x302: vcc3V302(0x20) = CONST 
    0xcc5S0x302: vcc5V302(0x20) = ADD vcc3V302(0x20), vcabV302(0x0)
    0xcc8S0x302: MSTORE vcc5V302(0x20), vcabV302(0x0)
    0xcc9S0x302: vcc9V302(0x20) = CONST 
    0xccbS0x302: vccbV302(0x40) = ADD vcc9V302(0x20), vcc5V302(0x20)
    0xcccS0x302: vcccV302(0x0) = CONST 
    0xcceS0x302: vcceV302 = SHA3 vcccV302(0x0), vccbV302(0x40)
    0xcd1S0x302: SSTORE vcceV302, vca9_0V302
    0xcd4S0x302: vcd4V302(0x1) = CONST 
    0xcd6S0x302: vcd6V302(0xa0) = CONST 
    0xcd8S0x302: vcd8V302(0x2) = CONST 
    0xcdaS0x302: vcdaV302(0x10000000000000000000000000000000000000000) = EXP vcd8V302(0x2), vcd6V302(0xa0)
    0xcdbS0x302: vcdbV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcdaV302(0x10000000000000000000000000000000000000000), vcd4V302(0x1)
    0xcdcS0x302: vcdcV302 = AND vcdbV302(0xffffffffffffffffffffffffffffffffffffffff), v311
    0xcddS0x302: vcddV302 = CALLER 
    0xcdeS0x302: vcdeV302(0x1) = CONST 
    0xce0S0x302: vce0V302(0xa0) = CONST 
    0xce2S0x302: vce2V302(0x2) = CONST 
    0xce4S0x302: vce4V302(0x10000000000000000000000000000000000000000) = EXP vce2V302(0x2), vce0V302(0xa0)
    0xce5S0x302: vce5V302(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce4V302(0x10000000000000000000000000000000000000000), vcdeV302(0x1)
    0xce6S0x302: vce6V302 = AND vce5V302(0xffffffffffffffffffffffffffffffffffffffff), vcddV302
    0xce7S0x302: vce7V302(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xd09S0x302: vd09V302(0x40) = CONST 
    0xd0bS0x302: vd0bV302 = MLOAD vd09V302(0x40)
    0xd0eS0x302: MSTORE vd0bV302, v314
    0xd0fS0x302: vd0fV302(0x20) = CONST 
    0xd11S0x302: vd11V302 = ADD vd0fV302(0x20), vd0bV302
    0xd12S0x302: vd12V302(0x40) = CONST 
    0xd14S0x302: vd14V302 = MLOAD vd12V302(0x40)
    0xd17S0x302: vd17V302(0x20) = SUB vd11V302, vd14V302
    0xd19S0x302: LOG3 vd14V302, vd17V302(0x20), vce7V302(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vce6V302, vcdcV302
    0xd1bS0x302: vd1bV302(0x1) = CONST 
    0xd21S0x302: JUMP v749V302(0x752)

    Begin block 0x752B0x302
    prev=[0xcaaB0x302], succ=[0xe32f]
    =================================
    0x759S0x302: JUMP v303(0xe32f)

    Begin block 0xe32f
    prev=[0x752B0x302], succ=[]
    =================================
    0xe330: ve330(0x40) = CONST 
    0xe332: ve332 = MLOAD ve330(0x40)
    0xe334: ve334(0x0) = ISZERO vd1bV302(0x1)
    0xe335: ve335(0x1) = ISZERO ve334(0x0)
    0xe337: MSTORE ve332, ve335(0x1)
    0xe338: ve338(0x20) = CONST 
    0xe33a: ve33a = ADD ve338(0x20), ve332
    0xe33b: ve33b(0x40) = CONST 
    0xe33d: ve33d = MLOAD ve33b(0x40)
    0xe340: ve340(0x20) = SUB ve33a, ve33d
    0xe342: RETURN ve33d, ve340(0x20)

    Begin block 0x6f3B0x302
    prev=[0x6edB0x302], succ=[0x706B0x302]
    =================================
    0x6f4S0x302: v6f4V302(0x4) = CONST 
    0x6f6S0x302: v6f6V302 = SLOAD v6f4V302(0x4)
    0x6f7S0x302: v6f7V302 = CALLER 
    0x6f8S0x302: v6f8V302(0x1) = CONST 
    0x6faS0x302: v6faV302(0xa0) = CONST 
    0x6fcS0x302: v6fcV302(0x2) = CONST 
    0x6feS0x302: v6feV302(0x10000000000000000000000000000000000000000) = EXP v6fcV302(0x2), v6faV302(0xa0)
    0x6ffS0x302: v6ffV302(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6feV302(0x10000000000000000000000000000000000000000), v6f8V302(0x1)
    0x702S0x302: v702V302 = AND v6ffV302(0xffffffffffffffffffffffffffffffffffffffff), v6f7V302
    0x704S0x302: v704V302 = AND v6f6V302, v6ffV302(0xffffffffffffffffffffffffffffffffffffffff)
    0x705S0x302: v705V302 = EQ v704V302, v702V302
    0x56acS0x302: v56acV302(0x706) = CONST 
    0x56ccS0x302: JUMP v56acV302(0x706)

    Begin block 0x6daB0x302
    prev=[0x6c4B0x302], succ=[0x6edB0x302]
    =================================
    0x6dbS0x302: v6dbV302(0x3) = CONST 
    0x6ddS0x302: v6ddV302 = SLOAD v6dbV302(0x3)
    0x6deS0x302: v6deV302 = CALLER 
    0x6dfS0x302: v6dfV302(0x1) = CONST 
    0x6e1S0x302: v6e1V302(0xa0) = CONST 
    0x6e3S0x302: v6e3V302(0x2) = CONST 
    0x6e5S0x302: v6e5V302(0x10000000000000000000000000000000000000000) = EXP v6e3V302(0x2), v6e1V302(0xa0)
    0x6e6S0x302: v6e6V302(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e5V302(0x10000000000000000000000000000000000000000), v6dfV302(0x1)
    0x6e9S0x302: v6e9V302 = AND v6e6V302(0xffffffffffffffffffffffffffffffffffffffff), v6deV302
    0x6ebS0x302: v6ebV302 = AND v6ddV302, v6e6V302(0xffffffffffffffffffffffffffffffffffffffff)
    0x6ecS0x302: v6ecV302 = EQ v6ebV302, v6e9V302
    0x4cacS0x302: v4cacV302(0x6ed) = CONST 
    0x4cccS0x302: JUMP v4cacV302(0x6ed)

}

function increaseApproval(address,uint256)() public {
    Begin block 0x319
    prev=[], succ=[0x320, 0x324]
    =================================
    0x31a: v31a = CALLVALUE 
    0x31b: v31b = ISZERO v31a
    0x31c: v31c(0x324) = CONST 
    0x31f: JUMPI v31c(0x324), v31b

    Begin block 0x320
    prev=[0x319], succ=[]
    =================================
    0x320: v320(0x0) = CONST 
    0x323: REVERT v320(0x0), v320(0x0)

    Begin block 0x324
    prev=[0x319], succ=[0x75a]
    =================================
    0x325: v325(0xe362) = CONST 
    0x328: v328(0x1) = CONST 
    0x32a: v32a(0xa0) = CONST 
    0x32c: v32c(0x2) = CONST 
    0x32e: v32e(0x10000000000000000000000000000000000000000) = EXP v32c(0x2), v32a(0xa0)
    0x32f: v32f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32e(0x10000000000000000000000000000000000000000), v328(0x1)
    0x330: v330(0x4) = CONST 
    0x332: v332 = CALLDATALOAD v330(0x4)
    0x333: v333 = AND v332, v32f(0xffffffffffffffffffffffffffffffffffffffff)
    0x334: v334(0x24) = CONST 
    0x336: v336 = CALLDATALOAD v334(0x24)
    0x337: v337(0x75a) = CONST 
    0x33a: JUMP v337(0x75a)

    Begin block 0x75a
    prev=[0x324], succ=[0x792]
    =================================
    0x75b: v75b(0x1) = CONST 
    0x75d: v75d(0xa0) = CONST 
    0x75f: v75f(0x2) = CONST 
    0x761: v761(0x10000000000000000000000000000000000000000) = EXP v75f(0x2), v75d(0xa0)
    0x762: v762(0xffffffffffffffffffffffffffffffffffffffff) = SUB v761(0x10000000000000000000000000000000000000000), v75b(0x1)
    0x763: v763 = CALLER 
    0x765: v765 = AND v762(0xffffffffffffffffffffffffffffffffffffffff), v763
    0x766: v766(0x0) = CONST 
    0x76a: MSTORE v766(0x0), v765
    0x76b: v76b(0x2) = CONST 
    0x76d: v76d(0x20) = CONST 
    0x771: MSTORE v76d(0x20), v76b(0x2)
    0x772: v772(0x40) = CONST 
    0x776: v776 = SHA3 v766(0x0), v772(0x40)
    0x779: v779 = AND v333, v762(0xffffffffffffffffffffffffffffffffffffffff)
    0x77b: MSTORE v766(0x0), v779
    0x77e: MSTORE v76d(0x20), v776
    0x781: v781 = SHA3 v766(0x0), v772(0x40)
    0x782: v782 = SLOAD v781
    0x783: v783(0x792) = CONST 
    0x788: v788(0xffffffff) = CONST 
    0x78d: v78d(0xd22) = CONST 
    0x790: v790(0xd22) = AND v78d(0xd22), v788(0xffffffff)
    0x791: v791_0 = CALLPRIVATE v790(0xd22), v336, v782, v783(0x792)

    Begin block 0x792
    prev=[0x75a], succ=[0xe362]
    =================================
    0x793: v793(0x1) = CONST 
    0x795: v795(0xa0) = CONST 
    0x797: v797(0x2) = CONST 
    0x799: v799(0x10000000000000000000000000000000000000000) = EXP v797(0x2), v795(0xa0)
    0x79a: v79a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v799(0x10000000000000000000000000000000000000000), v793(0x1)
    0x79b: v79b = CALLER 
    0x79d: v79d = AND v79a(0xffffffffffffffffffffffffffffffffffffffff), v79b
    0x79e: v79e(0x0) = CONST 
    0x7a2: MSTORE v79e(0x0), v79d
    0x7a3: v7a3(0x2) = CONST 
    0x7a5: v7a5(0x20) = CONST 
    0x7a9: MSTORE v7a5(0x20), v7a3(0x2)
    0x7aa: v7aa(0x40) = CONST 
    0x7ae: v7ae = SHA3 v79e(0x0), v7aa(0x40)
    0x7b1: v7b1 = AND v333, v79a(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b4: MSTORE v79e(0x0), v7b1
    0x7b8: MSTORE v7a5(0x20), v7ae
    0x7bc: v7bc = SHA3 v79e(0x0), v7aa(0x40)
    0x7bf: SSTORE v7bc, v791_0
    0x7c4: v7c4(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x7e7: v7e7 = MLOAD v7aa(0x40)
    0x7ea: MSTORE v7e7, v791_0
    0x7eb: v7eb(0x20) = CONST 
    0x7ed: v7ed = ADD v7eb(0x20), v7e7
    0x7ee: v7ee(0x40) = CONST 
    0x7f0: v7f0 = MLOAD v7ee(0x40)
    0x7f3: v7f3(0x20) = SUB v7ed, v7f0
    0x7f5: LOG3 v7f0, v7f3(0x20), v7c4(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v79d, v7b1
    0x7f7: v7f7(0x1) = CONST 
    0x7fd: JUMP v325(0xe362)

    Begin block 0xe362
    prev=[0x792], succ=[]
    =================================
    0xe363: ve363(0x40) = CONST 
    0xe365: ve365 = MLOAD ve363(0x40)
    0xe367: ve367(0x0) = ISZERO v7f7(0x1)
    0xe368: ve368(0x1) = ISZERO ve367(0x0)
    0xe36a: MSTORE ve365, ve368(0x1)
    0xe36b: ve36b(0x20) = CONST 
    0xe36d: ve36d = ADD ve36b(0x20), ve365
    0xe36e: ve36e(0x40) = CONST 
    0xe370: ve370 = MLOAD ve36e(0x40)
    0xe373: ve373(0x20) = SUB ve36d, ve370
    0xe375: RETURN ve370, ve373(0x20)

}

function toggleTransferable(bool)() public {
    Begin block 0x33b
    prev=[], succ=[0x342, 0x346]
    =================================
    0x33c: v33c = CALLVALUE 
    0x33d: v33d = ISZERO v33c
    0x33e: v33e(0x346) = CONST 
    0x341: JUMPI v33e(0x346), v33d

    Begin block 0x342
    prev=[0x33b], succ=[]
    =================================
    0x342: v342(0x0) = CONST 
    0x345: REVERT v342(0x0), v342(0x0)

    Begin block 0x346
    prev=[0x33b], succ=[0x7fe]
    =================================
    0x347: v347(0xe395) = CONST 
    0x34a: v34a(0x4) = CONST 
    0x34c: v34c = CALLDATALOAD v34a(0x4)
    0x34d: v34d = ISZERO v34c
    0x34e: v34e = ISZERO v34d
    0x34f: v34f(0x7fe) = CONST 
    0x352: JUMP v34f(0x7fe)

    Begin block 0x7fe
    prev=[0x346], succ=[0x815, 0x819]
    =================================
    0x7ff: v7ff(0x3) = CONST 
    0x801: v801 = SLOAD v7ff(0x3)
    0x802: v802 = CALLER 
    0x803: v803(0x1) = CONST 
    0x805: v805(0xa0) = CONST 
    0x807: v807(0x2) = CONST 
    0x809: v809(0x10000000000000000000000000000000000000000) = EXP v807(0x2), v805(0xa0)
    0x80a: v80a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v809(0x10000000000000000000000000000000000000000), v803(0x1)
    0x80d: v80d = AND v80a(0xffffffffffffffffffffffffffffffffffffffff), v802
    0x80f: v80f = AND v801, v80a(0xffffffffffffffffffffffffffffffffffffffff)
    0x810: v810 = EQ v80f, v80d
    0x811: v811(0x819) = CONST 
    0x814: JUMPI v811(0x819), v810

    Begin block 0x815
    prev=[0x7fe], succ=[]
    =================================
    0x815: v815(0x0) = CONST 
    0x818: REVERT v815(0x0), v815(0x0)

    Begin block 0x819
    prev=[0x7fe], succ=[0xe395]
    =================================
    0x81a: v81a(0x4) = CONST 
    0x81d: v81d = SLOAD v81a(0x4)
    0x81f: v81f = ISZERO v34e
    0x820: v820 = ISZERO v81f
    0x821: v821(0xa0) = CONST 
    0x823: v823(0x2) = CONST 
    0x825: v825(0x10000000000000000000000000000000000000000) = EXP v823(0x2), v821(0xa0)
    0x826: v826 = MUL v825(0x10000000000000000000000000000000000000000), v820
    0x827: v827(0xff0000000000000000000000000000000000000000) = CONST 
    0x83d: v83d(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v827(0xff0000000000000000000000000000000000000000)
    0x840: v840 = AND v81d, v83d(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff)
    0x844: v844 = OR v840, v826
    0x846: SSTORE v81a(0x4), v844
    0x847: JUMP v347(0xe395)

    Begin block 0xe395
    prev=[0x819], succ=[]
    =================================
    0xe396: STOP 

}

function emergencyERC20Drain(address,uint256)() public {
    Begin block 0x353
    prev=[], succ=[0x35a, 0x35e]
    =================================
    0x354: v354 = CALLVALUE 
    0x355: v355 = ISZERO v354
    0x356: v356(0x35e) = CONST 
    0x359: JUMPI v356(0x35e), v355

    Begin block 0x35a
    prev=[0x353], succ=[]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35d: REVERT v35a(0x0), v35a(0x0)

    Begin block 0x35e
    prev=[0x353], succ=[0x848]
    =================================
    0x35f: v35f(0xe3b6) = CONST 
    0x362: v362(0x1) = CONST 
    0x364: v364(0xa0) = CONST 
    0x366: v366(0x2) = CONST 
    0x368: v368(0x10000000000000000000000000000000000000000) = EXP v366(0x2), v364(0xa0)
    0x369: v369(0xffffffffffffffffffffffffffffffffffffffff) = SUB v368(0x10000000000000000000000000000000000000000), v362(0x1)
    0x36a: v36a(0x4) = CONST 
    0x36c: v36c = CALLDATALOAD v36a(0x4)
    0x36d: v36d = AND v36c, v369(0xffffffffffffffffffffffffffffffffffffffff)
    0x36e: v36e(0x24) = CONST 
    0x370: v370 = CALLDATALOAD v36e(0x24)
    0x371: v371(0x848) = CONST 
    0x374: JUMP v371(0x848)

    Begin block 0x848
    prev=[0x35e], succ=[0x85f, 0x863]
    =================================
    0x849: v849(0x3) = CONST 
    0x84b: v84b = SLOAD v849(0x3)
    0x84c: v84c = CALLER 
    0x84d: v84d(0x1) = CONST 
    0x84f: v84f(0xa0) = CONST 
    0x851: v851(0x2) = CONST 
    0x853: v853(0x10000000000000000000000000000000000000000) = EXP v851(0x2), v84f(0xa0)
    0x854: v854(0xffffffffffffffffffffffffffffffffffffffff) = SUB v853(0x10000000000000000000000000000000000000000), v84d(0x1)
    0x857: v857 = AND v854(0xffffffffffffffffffffffffffffffffffffffff), v84c
    0x859: v859 = AND v84b, v854(0xffffffffffffffffffffffffffffffffffffffff)
    0x85a: v85a = EQ v859, v857
    0x85b: v85b(0x863) = CONST 
    0x85e: JUMPI v85b(0x863), v85a

    Begin block 0x85f
    prev=[0x848], succ=[]
    =================================
    0x85f: v85f(0x0) = CONST 
    0x862: REVERT v85f(0x0), v85f(0x0)

    Begin block 0x863
    prev=[0x848], succ=[0x8db, 0x8df]
    =================================
    0x864: v864(0x3) = CONST 
    0x866: v866 = SLOAD v864(0x3)
    0x867: v867(0x1) = CONST 
    0x869: v869(0xa0) = CONST 
    0x86b: v86b(0x2) = CONST 
    0x86d: v86d(0x10000000000000000000000000000000000000000) = EXP v86b(0x2), v869(0xa0)
    0x86e: v86e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86d(0x10000000000000000000000000000000000000000), v867(0x1)
    0x871: v871 = AND v36d, v86e(0xffffffffffffffffffffffffffffffffffffffff)
    0x873: v873(0xa9059cbb) = CONST 
    0x879: v879 = AND v86e(0xffffffffffffffffffffffffffffffffffffffff), v866
    0x87b: v87b(0x0) = CONST 
    0x87d: v87d(0x40) = CONST 
    0x87f: v87f = MLOAD v87d(0x40)
    0x880: v880(0x20) = CONST 
    0x882: v882 = ADD v880(0x20), v87f
    0x883: MSTORE v882, v87b(0x0)
    0x884: v884(0x40) = CONST 
    0x886: v886 = MLOAD v884(0x40)
    0x887: v887(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x8a5: v8a5(0xffffffff) = CONST 
    0x8ab: v8ab(0xa9059cbb) = AND v873(0xa9059cbb), v8a5(0xffffffff)
    0x8ac: v8ac(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = MUL v8ab(0xa9059cbb), v887(0x100000000000000000000000000000000000000000000000000000000)
    0x8ae: MSTORE v886, v8ac(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x8af: v8af(0x1) = CONST 
    0x8b1: v8b1(0xa0) = CONST 
    0x8b3: v8b3(0x2) = CONST 
    0x8b5: v8b5(0x10000000000000000000000000000000000000000) = EXP v8b3(0x2), v8b1(0xa0)
    0x8b6: v8b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8b5(0x10000000000000000000000000000000000000000), v8af(0x1)
    0x8b9: v8b9 = AND v879, v8b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ba: v8ba(0x4) = CONST 
    0x8bd: v8bd = ADD v886, v8ba(0x4)
    0x8be: MSTORE v8bd, v8b9
    0x8bf: v8bf(0x24) = CONST 
    0x8c2: v8c2 = ADD v886, v8bf(0x24)
    0x8c3: MSTORE v8c2, v370
    0x8c4: v8c4(0x44) = CONST 
    0x8c6: v8c6 = ADD v8c4(0x44), v886
    0x8c7: v8c7(0x20) = CONST 
    0x8c9: v8c9(0x40) = CONST 
    0x8cb: v8cb = MLOAD v8c9(0x40)
    0x8ce: v8ce(0x44) = SUB v8c6, v8cb
    0x8d0: v8d0(0x0) = CONST 
    0x8d4: v8d4 = EXTCODESIZE v871
    0x8d5: v8d5 = ISZERO v8d4
    0x8d6: v8d6 = ISZERO v8d5
    0x8d7: v8d7(0x8df) = CONST 
    0x8da: JUMPI v8d7(0x8df), v8d6

    Begin block 0x8db
    prev=[0x863], succ=[]
    =================================
    0x8db: v8db(0x0) = CONST 
    0x8de: REVERT v8db(0x0), v8db(0x0)

    Begin block 0x8df
    prev=[0x863], succ=[0x8ec, 0x8f0]
    =================================
    0x8e0: v8e0(0x2c6) = CONST 
    0x8e3: v8e3 = GAS 
    0x8e4: v8e4 = SUB v8e3, v8e0(0x2c6)
    0x8e5: v8e5 = CALL v8e4, v871, v8d0(0x0), v8cb, v8ce(0x44), v8cb, v8c7(0x20)
    0x8e6: v8e6 = ISZERO v8e5
    0x8e7: v8e7 = ISZERO v8e6
    0x8e8: v8e8(0x8f0) = CONST 
    0x8eb: JUMPI v8e8(0x8f0), v8e7

    Begin block 0x8ec
    prev=[0x8df], succ=[]
    =================================
    0x8ec: v8ec(0x0) = CONST 
    0x8ef: REVERT v8ec(0x0), v8ec(0x0)

    Begin block 0x8f0
    prev=[0x8df], succ=[0xe3b6]
    =================================
    0x8f4: v8f4(0x40) = CONST 
    0x8f6: v8f6 = MLOAD v8f4(0x40)
    0x8f8: v8f8 = MLOAD v8f6
    0x8fd: JUMP v35f(0xe3b6)

    Begin block 0xe3b6
    prev=[0x8f0], succ=[]
    =================================
    0xe3b7: STOP 

}

function allowance(address,address)() public {
    Begin block 0x375
    prev=[], succ=[0x37c, 0x380]
    =================================
    0x376: v376 = CALLVALUE 
    0x377: v377 = ISZERO v376
    0x378: v378(0x380) = CONST 
    0x37b: JUMPI v378(0x380), v377

    Begin block 0x37c
    prev=[0x375], succ=[]
    =================================
    0x37c: v37c(0x0) = CONST 
    0x37f: REVERT v37c(0x0), v37c(0x0)

    Begin block 0x380
    prev=[0x375], succ=[0x8fe]
    =================================
    0x381: v381(0xe3d7) = CONST 
    0x384: v384(0x1) = CONST 
    0x386: v386(0xa0) = CONST 
    0x388: v388(0x2) = CONST 
    0x38a: v38a(0x10000000000000000000000000000000000000000) = EXP v388(0x2), v386(0xa0)
    0x38b: v38b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38a(0x10000000000000000000000000000000000000000), v384(0x1)
    0x38c: v38c(0x4) = CONST 
    0x38e: v38e = CALLDATALOAD v38c(0x4)
    0x390: v390 = AND v38b(0xffffffffffffffffffffffffffffffffffffffff), v38e
    0x392: v392(0x24) = CONST 
    0x394: v394 = CALLDATALOAD v392(0x24)
    0x395: v395 = AND v394, v38b(0xffffffffffffffffffffffffffffffffffffffff)
    0x396: v396(0x8fe) = CONST 
    0x399: JUMP v396(0x8fe)

    Begin block 0x8fe
    prev=[0x380], succ=[0xe3d7]
    =================================
    0x8ff: v8ff(0x1) = CONST 
    0x901: v901(0xa0) = CONST 
    0x903: v903(0x2) = CONST 
    0x905: v905(0x10000000000000000000000000000000000000000) = EXP v903(0x2), v901(0xa0)
    0x906: v906(0xffffffffffffffffffffffffffffffffffffffff) = SUB v905(0x10000000000000000000000000000000000000000), v8ff(0x1)
    0x909: v909 = AND v906(0xffffffffffffffffffffffffffffffffffffffff), v390
    0x90a: v90a(0x0) = CONST 
    0x90e: MSTORE v90a(0x0), v909
    0x90f: v90f(0x2) = CONST 
    0x911: v911(0x20) = CONST 
    0x915: MSTORE v911(0x20), v90f(0x2)
    0x916: v916(0x40) = CONST 
    0x91a: v91a = SHA3 v90a(0x0), v916(0x40)
    0x91e: v91e = AND v906(0xffffffffffffffffffffffffffffffffffffffff), v395
    0x920: MSTORE v90a(0x0), v91e
    0x924: MSTORE v911(0x20), v91a
    0x925: v925 = SHA3 v90a(0x0), v916(0x40)
    0x926: v926 = SLOAD v925
    0x928: JUMP v381(0xe3d7)

    Begin block 0xe3d7
    prev=[0x8fe], succ=[]
    =================================
    0xe3d8: ve3d8(0x40) = CONST 
    0xe3da: ve3da = MLOAD ve3d8(0x40)
    0xe3dd: MSTORE ve3da, v926
    0xe3de: ve3de(0x20) = CONST 
    0xe3e0: ve3e0 = ADD ve3de(0x20), ve3da
    0xe3e1: ve3e1(0x40) = CONST 
    0xe3e3: ve3e3 = MLOAD ve3e1(0x40)
    0xe3e6: ve3e6(0x20) = SUB ve3e0, ve3e3
    0xe3e8: RETURN ve3e3, ve3e6(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x39a
    prev=[], succ=[0x3a1, 0x3a5]
    =================================
    0x39b: v39b = CALLVALUE 
    0x39c: v39c = ISZERO v39b
    0x39d: v39d(0x3a5) = CONST 
    0x3a0: JUMPI v39d(0x3a5), v39c

    Begin block 0x3a1
    prev=[0x39a], succ=[]
    =================================
    0x3a1: v3a1(0x0) = CONST 
    0x3a4: REVERT v3a1(0x0), v3a1(0x0)

    Begin block 0x3a5
    prev=[0x39a], succ=[0x929]
    =================================
    0x3a6: v3a6(0xe408) = CONST 
    0x3a9: v3a9(0x1) = CONST 
    0x3ab: v3ab(0xa0) = CONST 
    0x3ad: v3ad(0x2) = CONST 
    0x3af: v3af(0x10000000000000000000000000000000000000000) = EXP v3ad(0x2), v3ab(0xa0)
    0x3b0: v3b0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3af(0x10000000000000000000000000000000000000000), v3a9(0x1)
    0x3b1: v3b1(0x4) = CONST 
    0x3b3: v3b3 = CALLDATALOAD v3b1(0x4)
    0x3b4: v3b4 = AND v3b3, v3b0(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b5: v3b5(0x929) = CONST 
    0x3b8: JUMP v3b5(0x929)

    Begin block 0x929
    prev=[0x3a5], succ=[0x940, 0x944]
    =================================
    0x92a: v92a(0x3) = CONST 
    0x92c: v92c = SLOAD v92a(0x3)
    0x92d: v92d = CALLER 
    0x92e: v92e(0x1) = CONST 
    0x930: v930(0xa0) = CONST 
    0x932: v932(0x2) = CONST 
    0x934: v934(0x10000000000000000000000000000000000000000) = EXP v932(0x2), v930(0xa0)
    0x935: v935(0xffffffffffffffffffffffffffffffffffffffff) = SUB v934(0x10000000000000000000000000000000000000000), v92e(0x1)
    0x938: v938 = AND v935(0xffffffffffffffffffffffffffffffffffffffff), v92d
    0x93a: v93a = AND v92c, v935(0xffffffffffffffffffffffffffffffffffffffff)
    0x93b: v93b = EQ v93a, v938
    0x93c: v93c(0x944) = CONST 
    0x93f: JUMPI v93c(0x944), v93b

    Begin block 0x940
    prev=[0x929], succ=[]
    =================================
    0x940: v940(0x0) = CONST 
    0x943: REVERT v940(0x0), v940(0x0)

    Begin block 0x944
    prev=[0x929], succ=[0x955, 0x959]
    =================================
    0x945: v945(0x1) = CONST 
    0x947: v947(0xa0) = CONST 
    0x949: v949(0x2) = CONST 
    0x94b: v94b(0x10000000000000000000000000000000000000000) = EXP v949(0x2), v947(0xa0)
    0x94c: v94c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v94b(0x10000000000000000000000000000000000000000), v945(0x1)
    0x94e: v94e = AND v3b4, v94c(0xffffffffffffffffffffffffffffffffffffffff)
    0x94f: v94f = ISZERO v94e
    0x950: v950 = ISZERO v94f
    0x951: v951(0x959) = CONST 
    0x954: JUMPI v951(0x959), v950

    Begin block 0x955
    prev=[0x944], succ=[]
    =================================
    0x955: v955(0x0) = CONST 
    0x958: REVERT v955(0x0), v955(0x0)

    Begin block 0x959
    prev=[0x944], succ=[0xe408]
    =================================
    0x95a: v95a(0x3) = CONST 
    0x95c: v95c = SLOAD v95a(0x3)
    0x95d: v95d(0x1) = CONST 
    0x95f: v95f(0xa0) = CONST 
    0x961: v961(0x2) = CONST 
    0x963: v963(0x10000000000000000000000000000000000000000) = EXP v961(0x2), v95f(0xa0)
    0x964: v964(0xffffffffffffffffffffffffffffffffffffffff) = SUB v963(0x10000000000000000000000000000000000000000), v95d(0x1)
    0x967: v967 = AND v3b4, v964(0xffffffffffffffffffffffffffffffffffffffff)
    0x969: v969 = AND v95c, v964(0xffffffffffffffffffffffffffffffffffffffff)
    0x96a: v96a(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x98b: v98b(0x40) = CONST 
    0x98d: v98d = MLOAD v98b(0x40)
    0x98e: v98e(0x40) = CONST 
    0x990: v990 = MLOAD v98e(0x40)
    0x993: v993(0x0) = SUB v98d, v990
    0x995: LOG3 v990, v993(0x0), v96a(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v969, v967
    0x996: v996(0x3) = CONST 
    0x999: v999 = SLOAD v996(0x3)
    0x99a: v99a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9af: v9af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v99a(0xffffffffffffffffffffffffffffffffffffffff)
    0x9b0: v9b0 = AND v9af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v999
    0x9b1: v9b1(0x1) = CONST 
    0x9b3: v9b3(0xa0) = CONST 
    0x9b5: v9b5(0x2) = CONST 
    0x9b7: v9b7(0x10000000000000000000000000000000000000000) = EXP v9b5(0x2), v9b3(0xa0)
    0x9b8: v9b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9b7(0x10000000000000000000000000000000000000000), v9b1(0x1)
    0x9bc: v9bc = AND v9b8(0xffffffffffffffffffffffffffffffffffffffff), v3b4
    0x9c0: v9c0 = OR v9bc, v9b0
    0x9c2: SSTORE v996(0x3), v9c0
    0x9c3: JUMP v3a6(0xe408)

    Begin block 0xe408
    prev=[0x959], succ=[]
    =================================
    0xe409: STOP 

}

function 0xbfe(vbfearg0, vbfearg1, vbfearg2) private {
    Begin block 0xbfe
    prev=[], succ=[0xc09, 0xc0a]
    =================================
    0xbff: vbff(0x0) = CONST 
    0xc03: vc03 = GT vbfearg0, vbfearg1
    0xc04: vc04 = ISZERO vc03
    0xc05: vc05(0xc0a) = CONST 
    0xc08: JUMPI vc05(0xc0a), vc04

    Begin block 0xc09
    prev=[0xbfe], succ=[]
    =================================
    0xc09: THROW 

    Begin block 0xc0a
    prev=[0xbfe], succ=[]
    =================================
    0xc0d: vc0d = SUB vbfearg1, vbfearg0
    0xc0f: RETURNPRIVATE vbfearg2, vc0d

}

function 0xd22(vd22arg0, vd22arg1, vd22arg2) private {
    Begin block 0xd22
    prev=[], succ=[0xd30, 0xd31]
    =================================
    0xd23: vd23(0x0) = CONST 
    0xd27: vd27 = ADD vd22arg0, vd22arg1
    0xd2a: vd2a = LT vd27, vd22arg1
    0xd2b: vd2b = ISZERO vd2a
    0xd2c: vd2c(0xd31) = CONST 
    0xd2f: JUMPI vd2c(0xd31), vd2b

    Begin block 0xd30
    prev=[0xd22], succ=[]
    =================================
    0xd30: THROW 

    Begin block 0xd31
    prev=[0xd22], succ=[]
    =================================
    0xd37: RETURNPRIVATE vd22arg2, vd27

}

function fallback()() public {
    Begin block 0xfb
    prev=[], succ=[]
    =================================
    0xfc: vfc(0x0) = CONST 
    0xff: REVERT vfc(0x0), vfc(0x0)

}

