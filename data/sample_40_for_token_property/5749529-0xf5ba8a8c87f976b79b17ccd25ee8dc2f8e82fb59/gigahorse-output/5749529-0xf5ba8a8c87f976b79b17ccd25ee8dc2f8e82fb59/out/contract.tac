function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2bb28]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x21b28: v21b28(0x2bb28) = CONST 
    0x21b48: JUMPI v21b28(0x2bb28), v8

    Begin block 0xd
    prev=[0x0], succ=[0x21128, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x22528: v22528(0x21128) = CONST 
    0x22548: JUMPI v22528(0x21128), v3c

    Begin block 0x21128
    prev=[0xd], succ=[]
    =================================
    0x21148: v21148(0xe0) = CONST 
    0x21168: CALLPRIVATE v21148(0xe0)

    Begin block 0x41
    prev=[0xd], succ=[0x2c528, 0x4c]
    =================================
    0x42: v42(0x95ea7b3) = CONST 
    0x47: v47 = EQ v42(0x95ea7b3), v35
    0x22f28: v22f28(0x2c528) = CONST 
    0x22f48: JUMPI v22f28(0x2c528), v47

    Begin block 0x2c528
    prev=[0x41], succ=[]
    =================================
    0x2c548: v2c548(0x170) = CONST 
    0x2c568: CALLPRIVATE v2c548(0x170)

    Begin block 0x4c
    prev=[0x41], succ=[0x2cf28, 0x57]
    =================================
    0x4d: v4d(0x18160ddd) = CONST 
    0x52: v52 = EQ v4d(0x18160ddd), v35
    0x23928: v23928(0x2cf28) = CONST 
    0x23948: JUMPI v23928(0x2cf28), v52

    Begin block 0x2cf28
    prev=[0x4c], succ=[]
    =================================
    0x2cf48: v2cf48(0x1d5) = CONST 
    0x2cf68: CALLPRIVATE v2cf48(0x1d5)

    Begin block 0x57
    prev=[0x4c], succ=[0x2d928, 0x62]
    =================================
    0x58: v58(0x19cae462) = CONST 
    0x5d: v5d = EQ v58(0x19cae462), v35
    0x24328: v24328(0x2d928) = CONST 
    0x24348: JUMPI v24328(0x2d928), v5d

    Begin block 0x2d928
    prev=[0x57], succ=[]
    =================================
    0x2d948: v2d948(0x200) = CONST 
    0x2d968: CALLPRIVATE v2d948(0x200)

    Begin block 0x62
    prev=[0x57], succ=[0x2e328, 0x6d]
    =================================
    0x63: v63(0x23b872dd) = CONST 
    0x68: v68 = EQ v63(0x23b872dd), v35
    0x24d28: v24d28(0x2e328) = CONST 
    0x24d48: JUMPI v24d28(0x2e328), v68

    Begin block 0x2e328
    prev=[0x62], succ=[]
    =================================
    0x2e348: v2e348(0x22b) = CONST 
    0x2e368: CALLPRIVATE v2e348(0x22b)

    Begin block 0x6d
    prev=[0x62], succ=[0x2ed28, 0x78]
    =================================
    0x6e: v6e(0x313ce567) = CONST 
    0x73: v73 = EQ v6e(0x313ce567), v35
    0x25728: v25728(0x2ed28) = CONST 
    0x25748: JUMPI v25728(0x2ed28), v73

    Begin block 0x2ed28
    prev=[0x6d], succ=[]
    =================================
    0x2ed48: v2ed48(0x2b0) = CONST 
    0x2ed68: CALLPRIVATE v2ed48(0x2b0)

    Begin block 0x78
    prev=[0x6d], succ=[0x2f728, 0x83]
    =================================
    0x79: v79(0x51bdd585) = CONST 
    0x7e: v7e = EQ v79(0x51bdd585), v35
    0x26128: v26128(0x2f728) = CONST 
    0x26148: JUMPI v26128(0x2f728), v7e

    Begin block 0x2f728
    prev=[0x78], succ=[]
    =================================
    0x2f748: v2f748(0x2db) = CONST 
    0x2f768: CALLPRIVATE v2f748(0x2db)

    Begin block 0x83
    prev=[0x78], succ=[0x30128, 0x8e]
    =================================
    0x84: v84(0x5c10fe08) = CONST 
    0x89: v89 = EQ v84(0x5c10fe08), v35
    0x26b28: v26b28(0x30128) = CONST 
    0x26b48: JUMPI v26b28(0x30128), v89

    Begin block 0x30128
    prev=[0x83], succ=[]
    =================================
    0x30148: v30148(0x30e) = CONST 
    0x30168: CALLPRIVATE v30148(0x30e)

    Begin block 0x8e
    prev=[0x83], succ=[0x30b28, 0x99]
    =================================
    0x8f: v8f(0x70a08231) = CONST 
    0x94: v94 = EQ v8f(0x70a08231), v35
    0x27528: v27528(0x30b28) = CONST 
    0x27548: JUMPI v27528(0x30b28), v94

    Begin block 0x30b28
    prev=[0x8e], succ=[]
    =================================
    0x30b48: v30b48(0x33b) = CONST 
    0x30b68: CALLPRIVATE v30b48(0x33b)

    Begin block 0x99
    prev=[0x8e], succ=[0x31528, 0xa4]
    =================================
    0x9a: v9a(0x81c8149d) = CONST 
    0x9f: v9f = EQ v9a(0x81c8149d), v35
    0x27f28: v27f28(0x31528) = CONST 
    0x27f48: JUMPI v27f28(0x31528), v9f

    Begin block 0x31528
    prev=[0x99], succ=[]
    =================================
    0x31548: v31548(0x392) = CONST 
    0x31568: CALLPRIVATE v31548(0x392)

    Begin block 0xa4
    prev=[0x99], succ=[0x31f28, 0xaf]
    =================================
    0xa5: va5(0x95d89b41) = CONST 
    0xaa: vaa = EQ va5(0x95d89b41), v35
    0x28928: v28928(0x31f28) = CONST 
    0x28948: JUMPI v28928(0x31f28), vaa

    Begin block 0x31f28
    prev=[0xa4], succ=[]
    =================================
    0x31f48: v31f48(0x3bd) = CONST 
    0x31f68: CALLPRIVATE v31f48(0x3bd)

    Begin block 0xaf
    prev=[0xa4], succ=[0x32928, 0xba]
    =================================
    0xb0: vb0(0xa9059cbb) = CONST 
    0xb5: vb5 = EQ vb0(0xa9059cbb), v35
    0x29328: v29328(0x32928) = CONST 
    0x29348: JUMPI v29328(0x32928), vb5

    Begin block 0x32928
    prev=[0xaf], succ=[]
    =================================
    0x32948: v32948(0x44d) = CONST 
    0x32968: CALLPRIVATE v32948(0x44d)

    Begin block 0xba
    prev=[0xaf], succ=[0x33328, 0xc5]
    =================================
    0xbb: vbb(0xcae9ca51) = CONST 
    0xc0: vc0 = EQ vbb(0xcae9ca51), v35
    0x29d28: v29d28(0x33328) = CONST 
    0x29d48: JUMPI v29d28(0x33328), vc0

    Begin block 0x33328
    prev=[0xba], succ=[]
    =================================
    0x33348: v33348(0x49a) = CONST 
    0x33368: CALLPRIVATE v33348(0x49a)

    Begin block 0xc5
    prev=[0xba], succ=[0x33d28, 0xd0]
    =================================
    0xc6: vc6(0xdd62ed3e) = CONST 
    0xcb: vcb = EQ vc6(0xdd62ed3e), v35
    0x2a728: v2a728(0x33d28) = CONST 
    0x2a748: JUMPI v2a728(0x33d28), vcb

    Begin block 0x33d28
    prev=[0xc5], succ=[]
    =================================
    0x33d48: v33d48(0x545) = CONST 
    0x33d68: CALLPRIVATE v33d48(0x545)

    Begin block 0xd0
    prev=[0xc5], succ=[0x2bb28, 0x34728]
    =================================
    0xd1: vd1(0xfcd6e339) = CONST 
    0xd6: vd6 = EQ vd1(0xfcd6e339), v35
    0x2b128: v2b128(0x34728) = CONST 
    0x2b148: JUMPI v2b128(0x34728), vd6

    Begin block 0x2bb28
    prev=[0x0, 0xd0], succ=[]
    =================================
    0x2bb48: v2bb48(0xdb) = CONST 
    0x2bb68: CALLPRIVATE v2bb48(0xdb)

    Begin block 0x34728
    prev=[0xd0], succ=[]
    =================================
    0x34748: v34748(0x5bc) = CONST 
    0x34768: CALLPRIVATE v34748(0x5bc)

}

function approve(address,uint256)() public {
    Begin block 0x170
    prev=[], succ=[0x178, 0x17c]
    =================================
    0x171: v171 = CALLVALUE 
    0x173: v173 = ISZERO v171
    0x174: v174(0x17c) = CONST 
    0x177: JUMPI v174(0x17c), v173

    Begin block 0x178
    prev=[0x170], succ=[]
    =================================
    0x178: v178(0x0) = CONST 
    0x17b: REVERT v178(0x0), v178(0x0)

    Begin block 0x17c
    prev=[0x170], succ=[0x671B0x17c]
    =================================
    0x17e: v17e(0x1bb) = CONST 
    0x181: v181(0x4) = CONST 
    0x184: v184 = CALLDATASIZE 
    0x185: v185 = SUB v184, v181(0x4)
    0x187: v187 = ADD v181(0x4), v185
    0x18b: v18b = CALLDATALOAD v181(0x4)
    0x18c: v18c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a1: v1a1 = AND v18c(0xffffffffffffffffffffffffffffffffffffffff), v18b
    0x1a3: v1a3(0x20) = CONST 
    0x1a5: v1a5(0x24) = ADD v1a3(0x20), v181(0x4)
    0x1ab: v1ab = CALLDATALOAD v1a5(0x24)
    0x1ad: v1ad(0x20) = CONST 
    0x1af: v1af(0x44) = ADD v1ad(0x20), v1a5(0x24)
    0x1b7: v1b7(0x671) = CONST 
    0x1ba: JUMP v1b7(0x671)

    Begin block 0x671B0x17c
    prev=[0x17c], succ=[0x1bb]
    =================================
    0x672S0x17c: v672V17c(0x0) = CONST 
    0x675S0x17c: v675V17c(0x5) = CONST 
    0x677S0x17c: v677V17c(0x0) = CONST 
    0x679S0x17c: v679V17c = CALLER 
    0x67aS0x17c: v67aV17c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68fS0x17c: v68fV17c = AND v67aV17c(0xffffffffffffffffffffffffffffffffffffffff), v679V17c
    0x690S0x17c: v690V17c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a5S0x17c: v6a5V17c = AND v690V17c(0xffffffffffffffffffffffffffffffffffffffff), v68fV17c
    0x6a7S0x17c: MSTORE v677V17c(0x0), v6a5V17c
    0x6a8S0x17c: v6a8V17c(0x20) = CONST 
    0x6aaS0x17c: v6aaV17c(0x20) = ADD v6a8V17c(0x20), v677V17c(0x0)
    0x6adS0x17c: MSTORE v6aaV17c(0x20), v675V17c(0x5)
    0x6aeS0x17c: v6aeV17c(0x20) = CONST 
    0x6b0S0x17c: v6b0V17c(0x40) = ADD v6aeV17c(0x20), v6aaV17c(0x20)
    0x6b1S0x17c: v6b1V17c(0x0) = CONST 
    0x6b3S0x17c: v6b3V17c = SHA3 v6b1V17c(0x0), v6b0V17c(0x40)
    0x6b4S0x17c: v6b4V17c(0x0) = CONST 
    0x6b7S0x17c: v6b7V17c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6ccS0x17c: v6ccV17c = AND v6b7V17c(0xffffffffffffffffffffffffffffffffffffffff), v1a1
    0x6cdS0x17c: v6cdV17c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6e2S0x17c: v6e2V17c = AND v6cdV17c(0xffffffffffffffffffffffffffffffffffffffff), v6ccV17c
    0x6e4S0x17c: MSTORE v6b4V17c(0x0), v6e2V17c
    0x6e5S0x17c: v6e5V17c(0x20) = CONST 
    0x6e7S0x17c: v6e7V17c(0x20) = ADD v6e5V17c(0x20), v6b4V17c(0x0)
    0x6eaS0x17c: MSTORE v6e7V17c(0x20), v6b3V17c
    0x6ebS0x17c: v6ebV17c(0x20) = CONST 
    0x6edS0x17c: v6edV17c(0x40) = ADD v6ebV17c(0x20), v6e7V17c(0x20)
    0x6eeS0x17c: v6eeV17c(0x0) = CONST 
    0x6f0S0x17c: v6f0V17c = SHA3 v6eeV17c(0x0), v6edV17c(0x40)
    0x6f3S0x17c: SSTORE v6f0V17c, v1ab
    0x6f5S0x17c: v6f5V17c(0x1) = CONST 
    0x6fdS0x17c: JUMP v17e(0x1bb)

    Begin block 0x1bb
    prev=[0x671B0x17c], succ=[]
    =================================
    0x1bc: v1bc(0x40) = CONST 
    0x1be: v1be = MLOAD v1bc(0x40)
    0x1c1: v1c1(0x0) = ISZERO v6f5V17c(0x1)
    0x1c2: v1c2(0x1) = ISZERO v1c1(0x0)
    0x1c3: v1c3(0x0) = ISZERO v1c2(0x1)
    0x1c4: v1c4(0x1) = ISZERO v1c3(0x0)
    0x1c6: MSTORE v1be, v1c4(0x1)
    0x1c7: v1c7(0x20) = CONST 
    0x1c9: v1c9 = ADD v1c7(0x20), v1be
    0x1cd: v1cd(0x40) = CONST 
    0x1cf: v1cf = MLOAD v1cd(0x40)
    0x1d2: v1d2(0x20) = SUB v1c9, v1cf
    0x1d4: RETURN v1cf, v1d2(0x20)

}

function totalSupply()() public {
    Begin block 0x1d5
    prev=[], succ=[0x1dd, 0x1e1]
    =================================
    0x1d6: v1d6 = CALLVALUE 
    0x1d8: v1d8 = ISZERO v1d6
    0x1d9: v1d9(0x1e1) = CONST 
    0x1dc: JUMPI v1d9(0x1e1), v1d8

    Begin block 0x1dd
    prev=[0x1d5], succ=[]
    =================================
    0x1dd: v1dd(0x0) = CONST 
    0x1e0: REVERT v1dd(0x0), v1dd(0x0)

    Begin block 0x1e1
    prev=[0x1d5], succ=[0x6fe]
    =================================
    0x1e3: v1e3(0x1ea) = CONST 
    0x1e6: v1e6(0x6fe) = CONST 
    0x1e9: JUMP v1e6(0x6fe)

    Begin block 0x6fe
    prev=[0x1e1], succ=[0x1ea]
    =================================
    0x6ff: v6ff(0x3) = CONST 
    0x701: v701 = SLOAD v6ff(0x3)
    0x703: JUMP v1e3(0x1ea)

    Begin block 0x1ea
    prev=[0x6fe], succ=[]
    =================================
    0x1eb: v1eb(0x40) = CONST 
    0x1ed: v1ed = MLOAD v1eb(0x40)
    0x1f1: MSTORE v1ed, v701
    0x1f2: v1f2(0x20) = CONST 
    0x1f4: v1f4 = ADD v1f2(0x20), v1ed
    0x1f8: v1f8(0x40) = CONST 
    0x1fa: v1fa = MLOAD v1f8(0x40)
    0x1fd: v1fd(0x20) = SUB v1f4, v1fa
    0x1ff: RETURN v1fa, v1fd(0x20)

}

function difficulty()() public {
    Begin block 0x200
    prev=[], succ=[0x208, 0x20c]
    =================================
    0x201: v201 = CALLVALUE 
    0x203: v203 = ISZERO v201
    0x204: v204(0x20c) = CONST 
    0x207: JUMPI v204(0x20c), v203

    Begin block 0x208
    prev=[0x200], succ=[]
    =================================
    0x208: v208(0x0) = CONST 
    0x20b: REVERT v208(0x0), v208(0x0)

    Begin block 0x20c
    prev=[0x200], succ=[0x704]
    =================================
    0x20e: v20e(0x215) = CONST 
    0x211: v211(0x704) = CONST 
    0x214: JUMP v211(0x704)

    Begin block 0x704
    prev=[0x20c], succ=[0x215]
    =================================
    0x705: v705(0x8) = CONST 
    0x707: v707 = SLOAD v705(0x8)
    0x709: JUMP v20e(0x215)

    Begin block 0x215
    prev=[0x704], succ=[]
    =================================
    0x216: v216(0x40) = CONST 
    0x218: v218 = MLOAD v216(0x40)
    0x21c: MSTORE v218, v707
    0x21d: v21d(0x20) = CONST 
    0x21f: v21f = ADD v21d(0x20), v218
    0x223: v223(0x40) = CONST 
    0x225: v225 = MLOAD v223(0x40)
    0x228: v228(0x20) = SUB v21f, v225
    0x22a: RETURN v225, v228(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x22b
    prev=[], succ=[0x233, 0x237]
    =================================
    0x22c: v22c = CALLVALUE 
    0x22e: v22e = ISZERO v22c
    0x22f: v22f(0x237) = CONST 
    0x232: JUMPI v22f(0x237), v22e

    Begin block 0x233
    prev=[0x22b], succ=[]
    =================================
    0x233: v233(0x0) = CONST 
    0x236: REVERT v233(0x0), v233(0x0)

    Begin block 0x237
    prev=[0x22b], succ=[0x70a]
    =================================
    0x239: v239(0x296) = CONST 
    0x23c: v23c(0x4) = CONST 
    0x23f: v23f = CALLDATASIZE 
    0x240: v240 = SUB v23f, v23c(0x4)
    0x242: v242 = ADD v23c(0x4), v240
    0x246: v246 = CALLDATALOAD v23c(0x4)
    0x247: v247(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25c: v25c = AND v247(0xffffffffffffffffffffffffffffffffffffffff), v246
    0x25e: v25e(0x20) = CONST 
    0x260: v260(0x24) = ADD v25e(0x20), v23c(0x4)
    0x266: v266 = CALLDATALOAD v260(0x24)
    0x267: v267(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27c: v27c = AND v267(0xffffffffffffffffffffffffffffffffffffffff), v266
    0x27e: v27e(0x20) = CONST 
    0x280: v280(0x44) = ADD v27e(0x20), v260(0x24)
    0x286: v286 = CALLDATALOAD v280(0x44)
    0x288: v288(0x20) = CONST 
    0x28a: v28a(0x64) = ADD v288(0x20), v280(0x44)
    0x292: v292(0x70a) = CONST 
    0x295: JUMP v292(0x70a)

    Begin block 0x70a
    prev=[0x237], succ=[0x793, 0x797]
    =================================
    0x70b: v70b(0x0) = CONST 
    0x70d: v70d(0x5) = CONST 
    0x70f: v70f(0x0) = CONST 
    0x712: v712(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x727: v727 = AND v712(0xffffffffffffffffffffffffffffffffffffffff), v25c
    0x728: v728(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x73d: v73d = AND v728(0xffffffffffffffffffffffffffffffffffffffff), v727
    0x73f: MSTORE v70f(0x0), v73d
    0x740: v740(0x20) = CONST 
    0x742: v742(0x20) = ADD v740(0x20), v70f(0x0)
    0x745: MSTORE v742(0x20), v70d(0x5)
    0x746: v746(0x20) = CONST 
    0x748: v748(0x40) = ADD v746(0x20), v742(0x20)
    0x749: v749(0x0) = CONST 
    0x74b: v74b = SHA3 v749(0x0), v748(0x40)
    0x74c: v74c(0x0) = CONST 
    0x74e: v74e = CALLER 
    0x74f: v74f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x764: v764 = AND v74f(0xffffffffffffffffffffffffffffffffffffffff), v74e
    0x765: v765(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x77a: v77a = AND v765(0xffffffffffffffffffffffffffffffffffffffff), v764
    0x77c: MSTORE v74c(0x0), v77a
    0x77d: v77d(0x20) = CONST 
    0x77f: v77f(0x20) = ADD v77d(0x20), v74c(0x0)
    0x782: MSTORE v77f(0x20), v74b
    0x783: v783(0x20) = CONST 
    0x785: v785(0x40) = ADD v783(0x20), v77f(0x20)
    0x786: v786(0x0) = CONST 
    0x788: v788 = SHA3 v786(0x0), v785(0x40)
    0x789: v789 = SLOAD v788
    0x78b: v78b = GT v286, v789
    0x78c: v78c = ISZERO v78b
    0x78d: v78d = ISZERO v78c
    0x78e: v78e = ISZERO v78d
    0x78f: v78f(0x797) = CONST 
    0x792: JUMPI v78f(0x797), v78e

    Begin block 0x793
    prev=[0x70a], succ=[]
    =================================
    0x793: v793(0x0) = CONST 
    0x796: REVERT v793(0x0), v793(0x0)

    Begin block 0x797
    prev=[0x70a], succ=[0x82c]
    =================================
    0x799: v799(0x5) = CONST 
    0x79b: v79b(0x0) = CONST 
    0x79e: v79e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7b3: v7b3 = AND v79e(0xffffffffffffffffffffffffffffffffffffffff), v25c
    0x7b4: v7b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7c9: v7c9 = AND v7b4(0xffffffffffffffffffffffffffffffffffffffff), v7b3
    0x7cb: MSTORE v79b(0x0), v7c9
    0x7cc: v7cc(0x20) = CONST 
    0x7ce: v7ce(0x20) = ADD v7cc(0x20), v79b(0x0)
    0x7d1: MSTORE v7ce(0x20), v799(0x5)
    0x7d2: v7d2(0x20) = CONST 
    0x7d4: v7d4(0x40) = ADD v7d2(0x20), v7ce(0x20)
    0x7d5: v7d5(0x0) = CONST 
    0x7d7: v7d7 = SHA3 v7d5(0x0), v7d4(0x40)
    0x7d8: v7d8(0x0) = CONST 
    0x7da: v7da = CALLER 
    0x7db: v7db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7f0: v7f0 = AND v7db(0xffffffffffffffffffffffffffffffffffffffff), v7da
    0x7f1: v7f1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x806: v806 = AND v7f1(0xffffffffffffffffffffffffffffffffffffffff), v7f0
    0x808: MSTORE v7d8(0x0), v806
    0x809: v809(0x20) = CONST 
    0x80b: v80b(0x20) = ADD v809(0x20), v7d8(0x0)
    0x80e: MSTORE v80b(0x20), v7d7
    0x80f: v80f(0x20) = CONST 
    0x811: v811(0x40) = ADD v80f(0x20), v80b(0x20)
    0x812: v812(0x0) = CONST 
    0x814: v814 = SHA3 v812(0x0), v811(0x40)
    0x815: v815(0x0) = CONST 
    0x819: v819 = SLOAD v814
    0x81a: v81a = SUB v819, v286
    0x820: SSTORE v814, v81a
    0x822: v822(0x82c) = CONST 
    0x828: v828(0xc72) = CONST 
    0x82b: CALLPRIVATE v828(0xc72), v286, v27c, v25c, v822(0x82c)

    Begin block 0x82c
    prev=[0x797], succ=[0x296]
    =================================
    0x82d: v82d(0x1) = CONST 
    0x836: JUMP v239(0x296)

    Begin block 0x296
    prev=[0x82c], succ=[]
    =================================
    0x297: v297(0x40) = CONST 
    0x299: v299 = MLOAD v297(0x40)
    0x29c: v29c(0x0) = ISZERO v82d(0x1)
    0x29d: v29d(0x1) = ISZERO v29c(0x0)
    0x29e: v29e(0x0) = ISZERO v29d(0x1)
    0x29f: v29f(0x1) = ISZERO v29e(0x0)
    0x2a1: MSTORE v299, v29f(0x1)
    0x2a2: v2a2(0x20) = CONST 
    0x2a4: v2a4 = ADD v2a2(0x20), v299
    0x2a8: v2a8(0x40) = CONST 
    0x2aa: v2aa = MLOAD v2a8(0x40)
    0x2ad: v2ad(0x20) = SUB v2a4, v2aa
    0x2af: RETURN v2aa, v2ad(0x20)

}

function decimals()() public {
    Begin block 0x2b0
    prev=[], succ=[0x2b8, 0x2bc]
    =================================
    0x2b1: v2b1 = CALLVALUE 
    0x2b3: v2b3 = ISZERO v2b1
    0x2b4: v2b4(0x2bc) = CONST 
    0x2b7: JUMPI v2b4(0x2bc), v2b3

    Begin block 0x2b8
    prev=[0x2b0], succ=[]
    =================================
    0x2b8: v2b8(0x0) = CONST 
    0x2bb: REVERT v2b8(0x0), v2b8(0x0)

    Begin block 0x2bc
    prev=[0x2b0], succ=[0x837]
    =================================
    0x2be: v2be(0x2c5) = CONST 
    0x2c1: v2c1(0x837) = CONST 
    0x2c4: JUMP v2c1(0x837)

    Begin block 0x837
    prev=[0x2bc], succ=[0x2c5]
    =================================
    0x838: v838(0x2) = CONST 
    0x83a: v83a = SLOAD v838(0x2)
    0x83c: JUMP v2be(0x2c5)

    Begin block 0x2c5
    prev=[0x837], succ=[]
    =================================
    0x2c6: v2c6(0x40) = CONST 
    0x2c8: v2c8 = MLOAD v2c6(0x40)
    0x2cc: MSTORE v2c8, v83a
    0x2cd: v2cd(0x20) = CONST 
    0x2cf: v2cf = ADD v2cd(0x20), v2c8
    0x2d3: v2d3(0x40) = CONST 
    0x2d5: v2d5 = MLOAD v2d3(0x40)
    0x2d8: v2d8(0x20) = SUB v2cf, v2d5
    0x2da: RETURN v2d5, v2d8(0x20)

}

function currentChallenge()() public {
    Begin block 0x2db
    prev=[], succ=[0x2e3, 0x2e7]
    =================================
    0x2dc: v2dc = CALLVALUE 
    0x2de: v2de = ISZERO v2dc
    0x2df: v2df(0x2e7) = CONST 
    0x2e2: JUMPI v2df(0x2e7), v2de

    Begin block 0x2e3
    prev=[0x2db], succ=[]
    =================================
    0x2e3: v2e3(0x0) = CONST 
    0x2e6: REVERT v2e3(0x0), v2e3(0x0)

    Begin block 0x2e7
    prev=[0x2db], succ=[0x83d]
    =================================
    0x2e9: v2e9(0x2f0) = CONST 
    0x2ec: v2ec(0x83d) = CONST 
    0x2ef: JUMP v2ec(0x83d)

    Begin block 0x83d
    prev=[0x2e7], succ=[0x2f0]
    =================================
    0x83e: v83e(0x6) = CONST 
    0x840: v840 = SLOAD v83e(0x6)
    0x842: JUMP v2e9(0x2f0)

    Begin block 0x2f0
    prev=[0x83d], succ=[]
    =================================
    0x2f1: v2f1(0x40) = CONST 
    0x2f3: v2f3 = MLOAD v2f1(0x40)
    0x2f6: v2f6(0x0) = CONST 
    0x2f8: v2f8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v2f6(0x0)
    0x2f9: v2f9 = AND v2f8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v840
    0x2fa: v2fa(0x0) = CONST 
    0x2fc: v2fc(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v2fa(0x0)
    0x2fd: v2fd = AND v2fc(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2f9
    0x2ff: MSTORE v2f3, v2fd
    0x300: v300(0x20) = CONST 
    0x302: v302 = ADD v300(0x20), v2f3
    0x306: v306(0x40) = CONST 
    0x308: v308 = MLOAD v306(0x40)
    0x30b: v30b(0x20) = SUB v302, v308
    0x30d: RETURN v308, v30b(0x20)

}

function proofOfWork(uint256)() public {
    Begin block 0x30e
    prev=[], succ=[0x316, 0x31a]
    =================================
    0x30f: v30f = CALLVALUE 
    0x311: v311 = ISZERO v30f
    0x312: v312(0x31a) = CONST 
    0x315: JUMPI v312(0x31a), v311

    Begin block 0x316
    prev=[0x30e], succ=[]
    =================================
    0x316: v316(0x0) = CONST 
    0x319: REVERT v316(0x0), v316(0x0)

    Begin block 0x31a
    prev=[0x30e], succ=[0x843]
    =================================
    0x31c: v31c(0x339) = CONST 
    0x31f: v31f(0x4) = CONST 
    0x322: v322 = CALLDATASIZE 
    0x323: v323 = SUB v322, v31f(0x4)
    0x325: v325 = ADD v31f(0x4), v323
    0x329: v329 = CALLDATALOAD v31f(0x4)
    0x32b: v32b(0x20) = CONST 
    0x32d: v32d(0x24) = ADD v32b(0x20), v31f(0x4)
    0x335: v335(0x843) = CONST 
    0x338: JUMP v335(0x843)

    Begin block 0x843
    prev=[0x31a], succ=[0x8ce, 0x8d2]
    =================================
    0x844: v844(0x0) = CONST 
    0x848: v848(0x6) = CONST 
    0x84a: v84a = SLOAD v848(0x6)
    0x84b: v84b(0x40) = CONST 
    0x84d: v84d = MLOAD v84b(0x40)
    0x851: MSTORE v84d, v329
    0x852: v852(0x20) = CONST 
    0x854: v854 = ADD v852(0x20), v84d
    0x856: v856(0x0) = CONST 
    0x858: v858(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v856(0x0)
    0x859: v859 = AND v858(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v84a
    0x85a: v85a(0x0) = CONST 
    0x85c: v85c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v85a(0x0)
    0x85d: v85d = AND v85c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v859
    0x85f: MSTORE v854, v85d
    0x860: v860(0x20) = CONST 
    0x862: v862 = ADD v860(0x20), v854
    0x867: v867(0x40) = CONST 
    0x869: v869 = MLOAD v867(0x40)
    0x86c: v86c(0x40) = SUB v862, v869
    0x86e: v86e = SHA3 v869, v86c(0x40)
    0x871: v871(0x8) = CONST 
    0x873: v873 = SLOAD v871(0x8)
    0x874: v874(0x1000000000000000000000000000000000000000000000000) = CONST 
    0x88e: v88e = MUL v874(0x1000000000000000000000000000000000000000000000000), v873
    0x88f: v88f(0xffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8a8: v8a8(0xffffffffffffffff000000000000000000000000000000000000000000000000) = NOT v88f(0xffffffffffffffffffffffffffffffffffffffffffffffff)
    0x8a9: v8a9 = AND v8a8(0xffffffffffffffff000000000000000000000000000000000000000000000000), v88e
    0x8ab: v8ab(0xffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8c4: v8c4(0xffffffffffffffff000000000000000000000000000000000000000000000000) = NOT v8ab(0xffffffffffffffffffffffffffffffffffffffffffffffff)
    0x8c5: v8c5 = AND v8c4(0xffffffffffffffff000000000000000000000000000000000000000000000000), v86e
    0x8c6: v8c6 = LT v8c5, v8a9
    0x8c7: v8c7 = ISZERO v8c6
    0x8c8: v8c8 = ISZERO v8c7
    0x8c9: v8c9 = ISZERO v8c8
    0x8ca: v8ca(0x8d2) = CONST 
    0x8cd: JUMPI v8ca(0x8d2), v8c9

    Begin block 0x8ce
    prev=[0x843], succ=[]
    =================================
    0x8ce: v8ce(0x0) = CONST 
    0x8d1: REVERT v8ce(0x0), v8ce(0x0)

    Begin block 0x8d2
    prev=[0x843], succ=[0x8e5, 0x8e9]
    =================================
    0x8d3: v8d3(0x7) = CONST 
    0x8d5: v8d5 = SLOAD v8d3(0x7)
    0x8d6: v8d6 = TIMESTAMP 
    0x8d7: v8d7 = SUB v8d6, v8d5
    0x8da: v8da(0x5) = CONST 
    0x8dd: v8dd = LT v8d7, v8da(0x5)
    0x8de: v8de = ISZERO v8dd
    0x8df: v8df = ISZERO v8de
    0x8e0: v8e0 = ISZERO v8df
    0x8e1: v8e1(0x8e9) = CONST 
    0x8e4: JUMPI v8e1(0x8e9), v8e0

    Begin block 0x8e5
    prev=[0x8d2], succ=[]
    =================================
    0x8e5: v8e5(0x0) = CONST 
    0x8e8: REVERT v8e5(0x0), v8e5(0x0)

    Begin block 0x8e9
    prev=[0x8d2], succ=[0x8f4, 0x8f5]
    =================================
    0x8ea: v8ea(0x3c) = CONST 
    0x8ee: v8ee(0x0) = ISZERO v8ea(0x3c)
    0x8ef: v8ef(0x1) = ISZERO v8ee(0x0)
    0x8f0: v8f0(0x8f5) = CONST 
    0x8f3: JUMPI v8f0(0x8f5), v8ef(0x1)

    Begin block 0x8f4
    prev=[0x8e9], succ=[]
    =================================
    0x8f4: THROW 

    Begin block 0x8f5
    prev=[0x8e9], succ=[0x954, 0x955]
    =================================
    0x8f6: v8f6 = DIV v8d7, v8ea(0x3c)
    0x8f7: v8f7(0x4) = CONST 
    0x8f9: v8f9(0x0) = CONST 
    0x8fb: v8fb = CALLER 
    0x8fc: v8fc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x911: v911 = AND v8fc(0xffffffffffffffffffffffffffffffffffffffff), v8fb
    0x912: v912(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x927: v927 = AND v912(0xffffffffffffffffffffffffffffffffffffffff), v911
    0x929: MSTORE v8f9(0x0), v927
    0x92a: v92a(0x20) = CONST 
    0x92c: v92c(0x20) = ADD v92a(0x20), v8f9(0x0)
    0x92f: MSTORE v92c(0x20), v8f7(0x4)
    0x930: v930(0x20) = CONST 
    0x932: v932(0x40) = ADD v930(0x20), v92c(0x20)
    0x933: v933(0x0) = CONST 
    0x935: v935 = SHA3 v933(0x0), v932(0x40)
    0x936: v936(0x0) = CONST 
    0x93a: v93a = SLOAD v935
    0x93b: v93b = ADD v93a, v8f6
    0x941: SSTORE v935, v93b
    0x943: v943(0x1) = CONST 
    0x946: v946(0x258) = CONST 
    0x949: v949(0x8) = CONST 
    0x94b: v94b = SLOAD v949(0x8)
    0x94c: v94c = MUL v94b, v946(0x258)
    0x94e: v94e = ISZERO v8d7
    0x94f: v94f = ISZERO v94e
    0x950: v950(0x955) = CONST 
    0x953: JUMPI v950(0x955), v94f

    Begin block 0x954
    prev=[0x8f5], succ=[]
    =================================
    0x954: THROW 

    Begin block 0x955
    prev=[0x8f5], succ=[0x339]
    =================================
    0x956: v956 = DIV v94c, v8d7
    0x957: v957 = ADD v956, v943(0x1)
    0x958: v958(0x8) = CONST 
    0x95c: SSTORE v958(0x8), v957
    0x95e: v95e = TIMESTAMP 
    0x95f: v95f(0x7) = CONST 
    0x963: SSTORE v95f(0x7), v95e
    0x966: v966(0x6) = CONST 
    0x968: v968 = SLOAD v966(0x6)
    0x969: v969(0x1) = CONST 
    0x96b: v96b = NUMBER 
    0x96c: v96c = SUB v96b, v969(0x1)
    0x96d: v96d = BLOCKHASH v96c
    0x96e: v96e(0x40) = CONST 
    0x970: v970 = MLOAD v96e(0x40)
    0x974: MSTORE v970, v329
    0x975: v975(0x20) = CONST 
    0x977: v977 = ADD v975(0x20), v970
    0x979: v979(0x0) = CONST 
    0x97b: v97b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v979(0x0)
    0x97c: v97c = AND v97b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v968
    0x97d: v97d(0x0) = CONST 
    0x97f: v97f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v97d(0x0)
    0x980: v980 = AND v97f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v97c
    0x982: MSTORE v977, v980
    0x983: v983(0x20) = CONST 
    0x985: v985 = ADD v983(0x20), v977
    0x987: v987(0x0) = CONST 
    0x989: v989(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v987(0x0)
    0x98a: v98a = AND v989(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v96d
    0x98b: v98b(0x0) = CONST 
    0x98d: v98d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v98b(0x0)
    0x98e: v98e = AND v98d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v98a
    0x990: MSTORE v985, v98e
    0x991: v991(0x20) = CONST 
    0x993: v993 = ADD v991(0x20), v985
    0x999: v999(0x40) = CONST 
    0x99b: v99b = MLOAD v999(0x40)
    0x99e: v99e(0x60) = SUB v993, v99b
    0x9a0: v9a0 = SHA3 v99b, v99e(0x60)
    0x9a1: v9a1(0x6) = CONST 
    0x9a4: v9a4(0x0) = CONST 
    0x9a6: v9a6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v9a4(0x0)
    0x9a7: v9a7 = AND v9a6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v9a0
    0x9a9: SSTORE v9a1(0x6), v9a7
    0x9ae: JUMP v31c(0x339)

    Begin block 0x339
    prev=[0x955], succ=[]
    =================================
    0x33a: STOP 

}

function balanceOf(address)() public {
    Begin block 0x33b
    prev=[], succ=[0x343, 0x347]
    =================================
    0x33c: v33c = CALLVALUE 
    0x33e: v33e = ISZERO v33c
    0x33f: v33f(0x347) = CONST 
    0x342: JUMPI v33f(0x347), v33e

    Begin block 0x343
    prev=[0x33b], succ=[]
    =================================
    0x343: v343(0x0) = CONST 
    0x346: REVERT v343(0x0), v343(0x0)

    Begin block 0x347
    prev=[0x33b], succ=[0x9af]
    =================================
    0x349: v349(0x37c) = CONST 
    0x34c: v34c(0x4) = CONST 
    0x34f: v34f = CALLDATASIZE 
    0x350: v350 = SUB v34f, v34c(0x4)
    0x352: v352 = ADD v34c(0x4), v350
    0x356: v356 = CALLDATALOAD v34c(0x4)
    0x357: v357(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36c: v36c = AND v357(0xffffffffffffffffffffffffffffffffffffffff), v356
    0x36e: v36e(0x20) = CONST 
    0x370: v370(0x24) = ADD v36e(0x20), v34c(0x4)
    0x378: v378(0x9af) = CONST 
    0x37b: JUMP v378(0x9af)

    Begin block 0x9af
    prev=[0x347], succ=[0x37c]
    =================================
    0x9b0: v9b0(0x4) = CONST 
    0x9b2: v9b2(0x20) = CONST 
    0x9b4: MSTORE v9b2(0x20), v9b0(0x4)
    0x9b6: v9b6(0x0) = CONST 
    0x9b8: MSTORE v9b6(0x0), v36c
    0x9b9: v9b9(0x40) = CONST 
    0x9bb: v9bb(0x0) = CONST 
    0x9bd: v9bd = SHA3 v9bb(0x0), v9b9(0x40)
    0x9be: v9be(0x0) = CONST 
    0x9c4: v9c4 = SLOAD v9bd
    0x9c6: JUMP v349(0x37c)

    Begin block 0x37c
    prev=[0x9af], succ=[]
    =================================
    0x37d: v37d(0x40) = CONST 
    0x37f: v37f = MLOAD v37d(0x40)
    0x383: MSTORE v37f, v9c4
    0x384: v384(0x20) = CONST 
    0x386: v386 = ADD v384(0x20), v37f
    0x38a: v38a(0x40) = CONST 
    0x38c: v38c = MLOAD v38a(0x40)
    0x38f: v38f(0x20) = SUB v386, v38c
    0x391: RETURN v38c, v38f(0x20)

}

function timeOfLastProof()() public {
    Begin block 0x392
    prev=[], succ=[0x39a, 0x39e]
    =================================
    0x393: v393 = CALLVALUE 
    0x395: v395 = ISZERO v393
    0x396: v396(0x39e) = CONST 
    0x399: JUMPI v396(0x39e), v395

    Begin block 0x39a
    prev=[0x392], succ=[]
    =================================
    0x39a: v39a(0x0) = CONST 
    0x39d: REVERT v39a(0x0), v39a(0x0)

    Begin block 0x39e
    prev=[0x392], succ=[0x9c7]
    =================================
    0x3a0: v3a0(0x3a7) = CONST 
    0x3a3: v3a3(0x9c7) = CONST 
    0x3a6: JUMP v3a3(0x9c7)

    Begin block 0x9c7
    prev=[0x39e], succ=[0x3a7]
    =================================
    0x9c8: v9c8(0x7) = CONST 
    0x9ca: v9ca = SLOAD v9c8(0x7)
    0x9cc: JUMP v3a0(0x3a7)

    Begin block 0x3a7
    prev=[0x9c7], succ=[]
    =================================
    0x3a8: v3a8(0x40) = CONST 
    0x3aa: v3aa = MLOAD v3a8(0x40)
    0x3ae: MSTORE v3aa, v9ca
    0x3af: v3af(0x20) = CONST 
    0x3b1: v3b1 = ADD v3af(0x20), v3aa
    0x3b5: v3b5(0x40) = CONST 
    0x3b7: v3b7 = MLOAD v3b5(0x40)
    0x3ba: v3ba(0x20) = SUB v3b1, v3b7
    0x3bc: RETURN v3b7, v3ba(0x20)

}

function symbol()() public {
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
    prev=[0x3bd], succ=[0x9cdB0x3c9]
    =================================
    0x3cb: v3cb(0x3d2) = CONST 
    0x3ce: v3ce(0x9cd) = CONST 
    0x3d1: JUMP v3ce(0x9cd)

    Begin block 0x9cdB0x3c9
    prev=[0x3c9], succ=[0xa1dB0x3c9, 0x107baB0x3c9]
    =================================
    0x9ceS0x3c9: v9ceV3c9(0x1) = CONST 
    0x9d1S0x3c9: v9d1V3c9 = SLOAD v9ceV3c9(0x1)
    0x9d2S0x3c9: v9d2V3c9(0x1) = CONST 
    0x9d5S0x3c9: v9d5V3c9(0x1) = CONST 
    0x9d7S0x3c9: v9d7V3c9 = AND v9d5V3c9(0x1), v9d1V3c9
    0x9d8S0x3c9: v9d8V3c9 = ISZERO v9d7V3c9
    0x9d9S0x3c9: v9d9V3c9(0x100) = CONST 
    0x9dcS0x3c9: v9dcV3c9 = MUL v9d9V3c9(0x100), v9d8V3c9
    0x9ddS0x3c9: v9ddV3c9 = SUB v9dcV3c9, v9d2V3c9(0x1)
    0x9deS0x3c9: v9deV3c9 = AND v9ddV3c9, v9d1V3c9
    0x9dfS0x3c9: v9dfV3c9(0x2) = CONST 
    0x9e2S0x3c9: v9e2V3c9 = DIV v9deV3c9, v9dfV3c9(0x2)
    0x9e4S0x3c9: v9e4V3c9(0x1f) = CONST 
    0x9e6S0x3c9: v9e6V3c9 = ADD v9e4V3c9(0x1f), v9e2V3c9
    0x9e7S0x3c9: v9e7V3c9(0x20) = CONST 
    0x9ebS0x3c9: v9ebV3c9 = DIV v9e6V3c9, v9e7V3c9(0x20)
    0x9ecS0x3c9: v9ecV3c9 = MUL v9ebV3c9, v9e7V3c9(0x20)
    0x9edS0x3c9: v9edV3c9(0x20) = CONST 
    0x9efS0x3c9: v9efV3c9 = ADD v9edV3c9(0x20), v9ecV3c9
    0x9f0S0x3c9: v9f0V3c9(0x40) = CONST 
    0x9f2S0x3c9: v9f2V3c9 = MLOAD v9f0V3c9(0x40)
    0x9f5S0x3c9: v9f5V3c9 = ADD v9f2V3c9, v9efV3c9
    0x9f6S0x3c9: v9f6V3c9(0x40) = CONST 
    0x9f8S0x3c9: MSTORE v9f6V3c9(0x40), v9f5V3c9
    0x9ffS0x3c9: MSTORE v9f2V3c9, v9e2V3c9
    0xa00S0x3c9: va00V3c9(0x20) = CONST 
    0xa02S0x3c9: va02V3c9 = ADD va00V3c9(0x20), v9f2V3c9
    0xa05S0x3c9: va05V3c9 = SLOAD v9ceV3c9(0x1)
    0xa06S0x3c9: va06V3c9(0x1) = CONST 
    0xa09S0x3c9: va09V3c9(0x1) = CONST 
    0xa0bS0x3c9: va0bV3c9 = AND va09V3c9(0x1), va05V3c9
    0xa0cS0x3c9: va0cV3c9 = ISZERO va0bV3c9
    0xa0dS0x3c9: va0dV3c9(0x100) = CONST 
    0xa10S0x3c9: va10V3c9 = MUL va0dV3c9(0x100), va0cV3c9
    0xa11S0x3c9: va11V3c9 = SUB va10V3c9, va06V3c9(0x1)
    0xa12S0x3c9: va12V3c9 = AND va11V3c9, va05V3c9
    0xa13S0x3c9: va13V3c9(0x2) = CONST 
    0xa16S0x3c9: va16V3c9 = DIV va12V3c9, va13V3c9(0x2)
    0xa18S0x3c9: va18V3c9 = ISZERO va16V3c9
    0xa19S0x3c9: va19V3c9(0x107ba) = CONST 
    0xa1cS0x3c9: JUMPI va19V3c9(0x107ba), va18V3c9

    Begin block 0xa1dB0x3c9
    prev=[0x9cdB0x3c9], succ=[0xa25B0x3c9, 0xa38B0x3c9]
    =================================
    0xa1eS0x3c9: va1eV3c9(0x1f) = CONST 
    0xa20S0x3c9: va20V3c9 = LT va1eV3c9(0x1f), va16V3c9
    0xa21S0x3c9: va21V3c9(0xa38) = CONST 
    0xa24S0x3c9: JUMPI va21V3c9(0xa38), va20V3c9

    Begin block 0xa25B0x3c9
    prev=[0xa1dB0x3c9], succ=[0x107e1B0x3c9]
    =================================
    0xa25S0x3c9: va25V3c9(0x100) = CONST 
    0xa2aS0x3c9: va2aV3c9 = SLOAD v9ceV3c9(0x1)
    0xa2bS0x3c9: va2bV3c9 = DIV va2aV3c9, va25V3c9(0x100)
    0xa2cS0x3c9: va2cV3c9 = MUL va2bV3c9, va25V3c9(0x100)
    0xa2eS0x3c9: MSTORE va02V3c9, va2cV3c9
    0xa30S0x3c9: va30V3c9(0x20) = CONST 
    0xa32S0x3c9: va32V3c9 = ADD va30V3c9(0x20), va02V3c9
    0xa34S0x3c9: va34V3c9(0x107e1) = CONST 
    0xa37S0x3c9: JUMP va34V3c9(0x107e1)

    Begin block 0x107e1B0x3c9
    prev=[0xa25B0x3c9], succ=[0x3d2]
    =================================
    0x107e8S0x3c9: JUMP v3cb(0x3d2)

    Begin block 0x3d2
    prev=[0x107baB0x3c9, 0x107e1B0x3c9, 0x10856B0x3c9], succ=[0x3f7]
    =================================
    0x3d3: v3d3(0x40) = CONST 
    0x3d5: v3d5 = MLOAD v3d3(0x40)
    0x3d8: v3d8(0x20) = CONST 
    0x3da: v3da = ADD v3d8(0x20), v3d5
    0x3dd: v3dd(0x20) = SUB v3da, v3d5
    0x3df: MSTORE v3d5, v3dd(0x20)
    0x3e3: v3e3 = MLOAD v9f2V3c9
    0x3e5: MSTORE v3da, v3e3
    0x3e6: v3e6(0x20) = CONST 
    0x3e8: v3e8 = ADD v3e6(0x20), v3da
    0x3ec: v3ec = MLOAD v9f2V3c9
    0x3ee: v3ee(0x20) = CONST 
    0x3f0: v3f0 = ADD v3ee(0x20), v9f2V3c9
    0x3f5: v3f5(0x0) = CONST 
    0x3386: v3386(0x3f7) = CONST 
    0x33a6: JUMP v3386(0x3f7)

    Begin block 0x3f7
    prev=[0x3d2, 0x400], succ=[0x412, 0x400]
    =================================
    0x3f7_0x0: v3f7_0 = PHI v3f5(0x0), v40b
    0x3fa: v3fa = LT v3f7_0, v3ec
    0x3fb: v3fb = ISZERO v3fa
    0x3fc: v3fc(0x412) = CONST 
    0x3ff: JUMPI v3fc(0x412), v3fb

    Begin block 0x412
    prev=[0x3f7], succ=[0x43f, 0x426]
    =================================
    0x41b: v41b = ADD v3ec, v3e8
    0x41d: v41d(0x1f) = CONST 
    0x41f: v41f = AND v41d(0x1f), v3ec
    0x421: v421 = ISZERO v41f
    0x422: v422(0x43f) = CONST 
    0x425: JUMPI v422(0x43f), v421

    Begin block 0x43f
    prev=[0x412, 0x426], succ=[]
    =================================
    0x43f_0x1: v43f_1 = PHI v41b, v43c
    0x445: v445(0x40) = CONST 
    0x447: v447 = MLOAD v445(0x40)
    0x44a: v44a = SUB v43f_1, v447
    0x44c: RETURN v447, v44a

    Begin block 0x426
    prev=[0x412], succ=[0x43f]
    =================================
    0x428: v428 = SUB v41b, v41f
    0x42a: v42a = MLOAD v428
    0x42b: v42b(0x1) = CONST 
    0x42e: v42e(0x20) = CONST 
    0x430: v430 = SUB v42e(0x20), v41f
    0x431: v431(0x100) = CONST 
    0x434: v434 = EXP v431(0x100), v430
    0x435: v435 = SUB v434, v42b(0x1)
    0x436: v436 = NOT v435
    0x437: v437 = AND v436, v42a
    0x439: MSTORE v428, v437
    0x43a: v43a(0x20) = CONST 
    0x43c: v43c = ADD v43a(0x20), v428
    0x3d86: v3d86(0x43f) = CONST 
    0x3da6: JUMP v3d86(0x43f)

    Begin block 0x400
    prev=[0x3f7], succ=[0x3f7]
    =================================
    0x400_0x0: v400_0 = PHI v3f5(0x0), v40b
    0x402: v402 = ADD v3f0, v400_0
    0x403: v403 = MLOAD v402
    0x406: v406 = ADD v3e8, v400_0
    0x407: MSTORE v406, v403
    0x408: v408(0x20) = CONST 
    0x40b: v40b = ADD v400_0, v408(0x20)
    0x40e: v40e(0x3f7) = CONST 
    0x411: JUMP v40e(0x3f7)

    Begin block 0xa38B0x3c9
    prev=[0xa1dB0x3c9], succ=[0xa46B0x3c9]
    =================================
    0xa3aS0x3c9: va3aV3c9 = ADD va02V3c9, va16V3c9
    0xa3dS0x3c9: va3dV3c9(0x0) = CONST 
    0xa3fS0x3c9: MSTORE va3dV3c9(0x0), v9ceV3c9(0x1)
    0xa40S0x3c9: va40V3c9(0x20) = CONST 
    0xa42S0x3c9: va42V3c9(0x0) = CONST 
    0xa44S0x3c9: va44V3c9 = SHA3 va42V3c9(0x0), va40V3c9(0x20)
    0x5b86S0x3c9: v5b86V3c9(0xa46) = CONST 
    0x5ba6S0x3c9: JUMP v5b86V3c9(0xa46)

    Begin block 0xa46B0x3c9
    prev=[0xa38B0x3c9, 0xa46B0x3c9], succ=[0xa46B0x3c9, 0xa5aB0x3c9]
    =================================
    0xa46_0x0S0x3c9: va46_0V3c9 = PHI va02V3c9, va52V3c9
    0xa46_0x1S0x3c9: va46_1V3c9 = PHI va44V3c9, va4eV3c9
    0xa48S0x3c9: va48V3c9 = SLOAD va46_1V3c9
    0xa4aS0x3c9: MSTORE va46_0V3c9, va48V3c9
    0xa4cS0x3c9: va4cV3c9(0x1) = CONST 
    0xa4eS0x3c9: va4eV3c9 = ADD va4cV3c9(0x1), va46_1V3c9
    0xa50S0x3c9: va50V3c9(0x20) = CONST 
    0xa52S0x3c9: va52V3c9 = ADD va50V3c9(0x20), va46_0V3c9
    0xa55S0x3c9: va55V3c9 = GT va3aV3c9, va52V3c9
    0xa56S0x3c9: va56V3c9(0xa46) = CONST 
    0xa59S0x3c9: JUMPI va56V3c9(0xa46), va55V3c9

    Begin block 0xa5aB0x3c9
    prev=[0xa46B0x3c9], succ=[0x10856B0x3c9]
    =================================
    0xa5cS0x3c9: va5cV3c9 = SUB va52V3c9, va3aV3c9
    0xa5dS0x3c9: va5dV3c9(0x1f) = CONST 
    0xa5fS0x3c9: va5fV3c9 = AND va5dV3c9(0x1f), va5cV3c9
    0xa61S0x3c9: va61V3c9 = ADD va3aV3c9, va5fV3c9
    0x6586S0x3c9: v6586V3c9(0x10856) = CONST 
    0x65a6S0x3c9: JUMP v6586V3c9(0x10856)

    Begin block 0x10856B0x3c9
    prev=[0xa5aB0x3c9], succ=[0x3d2]
    =================================
    0x1085dS0x3c9: JUMP v3cb(0x3d2)

    Begin block 0x107baB0x3c9
    prev=[0x9cdB0x3c9], succ=[0x3d2]
    =================================
    0x107c1S0x3c9: JUMP v3cb(0x3d2)

}

function transfer(address,uint256)() public {
    Begin block 0x44d
    prev=[], succ=[0x455, 0x459]
    =================================
    0x44e: v44e = CALLVALUE 
    0x450: v450 = ISZERO v44e
    0x451: v451(0x459) = CONST 
    0x454: JUMPI v451(0x459), v450

    Begin block 0x455
    prev=[0x44d], succ=[]
    =================================
    0x455: v455(0x0) = CONST 
    0x458: REVERT v455(0x0), v455(0x0)

    Begin block 0x459
    prev=[0x44d], succ=[0xa6bB0x459]
    =================================
    0x45b: v45b(0x498) = CONST 
    0x45e: v45e(0x4) = CONST 
    0x461: v461 = CALLDATASIZE 
    0x462: v462 = SUB v461, v45e(0x4)
    0x464: v464 = ADD v45e(0x4), v462
    0x468: v468 = CALLDATALOAD v45e(0x4)
    0x469: v469(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x47e: v47e = AND v469(0xffffffffffffffffffffffffffffffffffffffff), v468
    0x480: v480(0x20) = CONST 
    0x482: v482(0x24) = ADD v480(0x20), v45e(0x4)
    0x488: v488 = CALLDATALOAD v482(0x24)
    0x48a: v48a(0x20) = CONST 
    0x48c: v48c(0x44) = ADD v48a(0x20), v482(0x24)
    0x494: v494(0xa6b) = CONST 
    0x497: JUMP v494(0xa6b)

    Begin block 0xa6bB0x459
    prev=[0x459], succ=[0xa76B0x459]
    =================================
    0xa6cS0x459: va6cV459(0xa76) = CONST 
    0xa6fS0x459: va6fV459 = CALLER 
    0xa72S0x459: va72V459(0xc72) = CONST 
    0xa75S0x459: CALLPRIVATE va72V459(0xc72), v488, v47e, va6fV459, va6cV459(0xa76)

    Begin block 0xa76B0x459
    prev=[0xa6bB0x459], succ=[0x498]
    =================================
    0xa79S0x459: JUMP v45b(0x498)

    Begin block 0x498
    prev=[0xa76B0x459], succ=[]
    =================================
    0x499: STOP 

}

function approveAndCall(address,uint256,bytes)() public {
    Begin block 0x49a
    prev=[], succ=[0x4a2, 0x4a6]
    =================================
    0x49b: v49b = CALLVALUE 
    0x49d: v49d = ISZERO v49b
    0x49e: v49e(0x4a6) = CONST 
    0x4a1: JUMPI v49e(0x4a6), v49d

    Begin block 0x4a2
    prev=[0x49a], succ=[]
    =================================
    0x4a2: v4a2(0x0) = CONST 
    0x4a5: REVERT v4a2(0x0), v4a2(0x0)

    Begin block 0x4a6
    prev=[0x49a], succ=[0xa7aB0x4a6]
    =================================
    0x4a8: v4a8(0x52b) = CONST 
    0x4ab: v4ab(0x4) = CONST 
    0x4ae: v4ae = CALLDATASIZE 
    0x4af: v4af = SUB v4ae, v4ab(0x4)
    0x4b1: v4b1 = ADD v4ab(0x4), v4af
    0x4b5: v4b5 = CALLDATALOAD v4ab(0x4)
    0x4b6: v4b6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4cb: v4cb = AND v4b6(0xffffffffffffffffffffffffffffffffffffffff), v4b5
    0x4cd: v4cd(0x20) = CONST 
    0x4cf: v4cf(0x24) = ADD v4cd(0x20), v4ab(0x4)
    0x4d5: v4d5 = CALLDATALOAD v4cf(0x24)
    0x4d7: v4d7(0x20) = CONST 
    0x4d9: v4d9(0x44) = ADD v4d7(0x20), v4cf(0x24)
    0x4df: v4df = CALLDATALOAD v4d9(0x44)
    0x4e1: v4e1(0x20) = CONST 
    0x4e3: v4e3(0x64) = ADD v4e1(0x20), v4d9(0x44)
    0x4e6: v4e6 = ADD v4ab(0x4), v4df
    0x4e8: v4e8 = CALLDATALOAD v4e6
    0x4ea: v4ea(0x20) = CONST 
    0x4ec: v4ec = ADD v4ea(0x20), v4e6
    0x4f0: v4f0(0x1f) = CONST 
    0x4f2: v4f2 = ADD v4f0(0x1f), v4e8
    0x4f3: v4f3(0x20) = CONST 
    0x4f7: v4f7 = DIV v4f2, v4f3(0x20)
    0x4f8: v4f8 = MUL v4f7, v4f3(0x20)
    0x4f9: v4f9(0x20) = CONST 
    0x4fb: v4fb = ADD v4f9(0x20), v4f8
    0x4fc: v4fc(0x40) = CONST 
    0x4fe: v4fe = MLOAD v4fc(0x40)
    0x501: v501 = ADD v4fe, v4fb
    0x502: v502(0x40) = CONST 
    0x504: MSTORE v502(0x40), v501
    0x50c: MSTORE v4fe, v4e8
    0x50d: v50d(0x20) = CONST 
    0x50f: v50f = ADD v50d(0x20), v4fe
    0x515: CALLDATACOPY v50f, v4ec, v4e8
    0x517: v517 = ADD v50f, v4e8
    0x527: v527(0xa7a) = CONST 
    0x52a: JUMP v527(0xa7a)

    Begin block 0xa7aB0x4a6
    prev=[0x4a6], succ=[0x671B0xa7aB0x4a6]
    =================================
    0xa7bS0x4a6: va7bV4a6(0x0) = CONST 
    0xa81S0x4a6: va81V4a6(0xa8a) = CONST 
    0xa86S0x4a6: va86V4a6(0x671) = CONST 
    0xa89S0x4a6: JUMP va86V4a6(0x671)

    Begin block 0x671B0xa7aB0x4a6
    prev=[0xa7aB0x4a6], succ=[0xa8aB0x4a6]
    =================================
    0x672S0xa7aS0x4a6: v672Va7aV4a6(0x0) = CONST 
    0x675S0xa7aS0x4a6: v675Va7aV4a6(0x5) = CONST 
    0x677S0xa7aS0x4a6: v677Va7aV4a6(0x0) = CONST 
    0x679S0xa7aS0x4a6: v679Va7aV4a6 = CALLER 
    0x67aS0xa7aS0x4a6: v67aVa7aV4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68fS0xa7aS0x4a6: v68fVa7aV4a6 = AND v67aVa7aV4a6(0xffffffffffffffffffffffffffffffffffffffff), v679Va7aV4a6
    0x690S0xa7aS0x4a6: v690Va7aV4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a5S0xa7aS0x4a6: v6a5Va7aV4a6 = AND v690Va7aV4a6(0xffffffffffffffffffffffffffffffffffffffff), v68fVa7aV4a6
    0x6a7S0xa7aS0x4a6: MSTORE v677Va7aV4a6(0x0), v6a5Va7aV4a6
    0x6a8S0xa7aS0x4a6: v6a8Va7aV4a6(0x20) = CONST 
    0x6aaS0xa7aS0x4a6: v6aaVa7aV4a6(0x20) = ADD v6a8Va7aV4a6(0x20), v677Va7aV4a6(0x0)
    0x6adS0xa7aS0x4a6: MSTORE v6aaVa7aV4a6(0x20), v675Va7aV4a6(0x5)
    0x6aeS0xa7aS0x4a6: v6aeVa7aV4a6(0x20) = CONST 
    0x6b0S0xa7aS0x4a6: v6b0Va7aV4a6(0x40) = ADD v6aeVa7aV4a6(0x20), v6aaVa7aV4a6(0x20)
    0x6b1S0xa7aS0x4a6: v6b1Va7aV4a6(0x0) = CONST 
    0x6b3S0xa7aS0x4a6: v6b3Va7aV4a6 = SHA3 v6b1Va7aV4a6(0x0), v6b0Va7aV4a6(0x40)
    0x6b4S0xa7aS0x4a6: v6b4Va7aV4a6(0x0) = CONST 
    0x6b7S0xa7aS0x4a6: v6b7Va7aV4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6ccS0xa7aS0x4a6: v6ccVa7aV4a6 = AND v6b7Va7aV4a6(0xffffffffffffffffffffffffffffffffffffffff), v4cb
    0x6cdS0xa7aS0x4a6: v6cdVa7aV4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6e2S0xa7aS0x4a6: v6e2Va7aV4a6 = AND v6cdVa7aV4a6(0xffffffffffffffffffffffffffffffffffffffff), v6ccVa7aV4a6
    0x6e4S0xa7aS0x4a6: MSTORE v6b4Va7aV4a6(0x0), v6e2Va7aV4a6
    0x6e5S0xa7aS0x4a6: v6e5Va7aV4a6(0x20) = CONST 
    0x6e7S0xa7aS0x4a6: v6e7Va7aV4a6(0x20) = ADD v6e5Va7aV4a6(0x20), v6b4Va7aV4a6(0x0)
    0x6eaS0xa7aS0x4a6: MSTORE v6e7Va7aV4a6(0x20), v6b3Va7aV4a6
    0x6ebS0xa7aS0x4a6: v6ebVa7aV4a6(0x20) = CONST 
    0x6edS0xa7aS0x4a6: v6edVa7aV4a6(0x40) = ADD v6ebVa7aV4a6(0x20), v6e7Va7aV4a6(0x20)
    0x6eeS0xa7aS0x4a6: v6eeVa7aV4a6(0x0) = CONST 
    0x6f0S0xa7aS0x4a6: v6f0Va7aV4a6 = SHA3 v6eeVa7aV4a6(0x0), v6edVa7aV4a6(0x40)
    0x6f3S0xa7aS0x4a6: SSTORE v6f0Va7aV4a6, v4d5
    0x6f5S0xa7aS0x4a6: v6f5Va7aV4a6(0x1) = CONST 
    0x6fdS0xa7aS0x4a6: JUMP va81V4a6(0xa8a)

    Begin block 0xa8aB0x4a6
    prev=[0x671B0xa7aB0x4a6], succ=[0xbf4B0x4a6, 0xa90B0x4a6]
    =================================
    0xa8bS0x4a6: va8bV4a6(0x0) = ISZERO v6f5Va7aV4a6(0x1)
    0xa8cS0x4a6: va8cV4a6(0xbf4) = CONST 
    0xa8fS0x4a6: JUMPI va8cV4a6(0xbf4), va8bV4a6(0x0)

    Begin block 0xbf4B0x4a6
    prev=[0xa8aB0x4a6], succ=[0x1087dB0x4a6]
    =================================
    0x8386S0x4a6: v8386V4a6(0x1087d) = CONST 
    0x83a6S0x4a6: JUMP v8386V4a6(0x1087d)

    Begin block 0x1087dB0x4a6
    prev=[0xbf4B0x4a6], succ=[0x52b]
    =================================
    0x10884S0x4a6: JUMP v4a8(0x52b)

    Begin block 0x52b
    prev=[0x10808B0x4a6, 0x1087dB0x4a6], succ=[]
    =================================
    0x4a6S0x52b_0: v52a_0V52b_0 = PHI va7bV4a6(0x0), vbecV4a6(0x1)
    0x52c: v52c(0x40) = CONST 
    0x52e: v52e = MLOAD v52c(0x40)
    0x531: v531 = ISZERO v52a_0V52b_0
    0x532: v532 = ISZERO v531
    0x533: v533 = ISZERO v532
    0x534: v534 = ISZERO v533
    0x536: MSTORE v52e, v534
    0x537: v537(0x20) = CONST 
    0x539: v539 = ADD v537(0x20), v52e
    0x53d: v53d(0x40) = CONST 
    0x53f: v53f = MLOAD v53d(0x40)
    0x542: v542(0x20) = SUB v539, v53f
    0x544: RETURN v53f, v542(0x20)

    Begin block 0xa90B0x4a6
    prev=[0xa8aB0x4a6], succ=[0xb69B0x4a6]
    =================================
    0xa91S0x4a6: va91V4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaa6S0x4a6: vaa6V4a6 = AND va91V4a6(0xffffffffffffffffffffffffffffffffffffffff), v4cb
    0xaa7S0x4a6: vaa7V4a6(0x8f4ffcb1) = CONST 
    0xaacS0x4a6: vaacV4a6 = CALLER 
    0xaaeS0x4a6: vaaeV4a6 = ADDRESS 
    0xab0S0x4a6: vab0V4a6(0x40) = CONST 
    0xab2S0x4a6: vab2V4a6 = MLOAD vab0V4a6(0x40)
    0xab4S0x4a6: vab4V4a6(0xffffffff) = CONST 
    0xab9S0x4a6: vab9V4a6(0x8f4ffcb1) = AND vab4V4a6(0xffffffff), vaa7V4a6(0x8f4ffcb1)
    0xabaS0x4a6: vabaV4a6(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xad8S0x4a6: vad8V4a6(0x8f4ffcb100000000000000000000000000000000000000000000000000000000) = MUL vabaV4a6(0x100000000000000000000000000000000000000000000000000000000), vab9V4a6(0x8f4ffcb1)
    0xadaS0x4a6: MSTORE vab2V4a6, vad8V4a6(0x8f4ffcb100000000000000000000000000000000000000000000000000000000)
    0xadbS0x4a6: vadbV4a6(0x4) = CONST 
    0xaddS0x4a6: vaddV4a6 = ADD vadbV4a6(0x4), vab2V4a6
    0xae0S0x4a6: vae0V4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf5S0x4a6: vaf5V4a6 = AND vae0V4a6(0xffffffffffffffffffffffffffffffffffffffff), vaacV4a6
    0xaf6S0x4a6: vaf6V4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb0bS0x4a6: vb0bV4a6 = AND vaf6V4a6(0xffffffffffffffffffffffffffffffffffffffff), vaf5V4a6
    0xb0dS0x4a6: MSTORE vaddV4a6, vb0bV4a6
    0xb0eS0x4a6: vb0eV4a6(0x20) = CONST 
    0xb10S0x4a6: vb10V4a6 = ADD vb0eV4a6(0x20), vaddV4a6
    0xb13S0x4a6: MSTORE vb10V4a6, v4d5
    0xb14S0x4a6: vb14V4a6(0x20) = CONST 
    0xb16S0x4a6: vb16V4a6 = ADD vb14V4a6(0x20), vb10V4a6
    0xb18S0x4a6: vb18V4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb2dS0x4a6: vb2dV4a6 = AND vb18V4a6(0xffffffffffffffffffffffffffffffffffffffff), vaaeV4a6
    0xb2eS0x4a6: vb2eV4a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb43S0x4a6: vb43V4a6 = AND vb2eV4a6(0xffffffffffffffffffffffffffffffffffffffff), vb2dV4a6
    0xb45S0x4a6: MSTORE vb16V4a6, vb43V4a6
    0xb46S0x4a6: vb46V4a6(0x20) = CONST 
    0xb48S0x4a6: vb48V4a6 = ADD vb46V4a6(0x20), vb16V4a6
    0xb4aS0x4a6: vb4aV4a6(0x20) = CONST 
    0xb4cS0x4a6: vb4cV4a6 = ADD vb4aV4a6(0x20), vb48V4a6
    0xb4fS0x4a6: vb4fV4a6(0x80) = SUB vb4cV4a6, vaddV4a6
    0xb51S0x4a6: MSTORE vb48V4a6, vb4fV4a6(0x80)
    0xb55S0x4a6: vb55V4a6 = MLOAD v4fe
    0xb57S0x4a6: MSTORE vb4cV4a6, vb55V4a6
    0xb58S0x4a6: vb58V4a6(0x20) = CONST 
    0xb5aS0x4a6: vb5aV4a6 = ADD vb58V4a6(0x20), vb4cV4a6
    0xb5eS0x4a6: vb5eV4a6 = MLOAD v4fe
    0xb60S0x4a6: vb60V4a6(0x20) = CONST 
    0xb62S0x4a6: vb62V4a6 = ADD vb60V4a6(0x20), v4fe
    0xb67S0x4a6: vb67V4a6(0x0) = CONST 
    0x6f86S0x4a6: v6f86V4a6(0xb69) = CONST 
    0x6fa6S0x4a6: JUMP v6f86V4a6(0xb69)

    Begin block 0xb69B0x4a6
    prev=[0xa90B0x4a6, 0xb72B0x4a6], succ=[0xb84B0x4a6, 0xb72B0x4a6]
    =================================
    0xb69_0x0S0x4a6: vb69_0V4a6 = PHI vb67V4a6(0x0), vb7dV4a6
    0xb6cS0x4a6: vb6cV4a6 = LT vb69_0V4a6, vb5eV4a6
    0xb6dS0x4a6: vb6dV4a6 = ISZERO vb6cV4a6
    0xb6eS0x4a6: vb6eV4a6(0xb84) = CONST 
    0xb71S0x4a6: JUMPI vb6eV4a6(0xb84), vb6dV4a6

    Begin block 0xb84B0x4a6
    prev=[0xb69B0x4a6], succ=[0xbb1B0x4a6, 0xb98B0x4a6]
    =================================
    0xb8dS0x4a6: vb8dV4a6 = ADD vb5eV4a6, vb5aV4a6
    0xb8fS0x4a6: vb8fV4a6(0x1f) = CONST 
    0xb91S0x4a6: vb91V4a6 = AND vb8fV4a6(0x1f), vb5eV4a6
    0xb93S0x4a6: vb93V4a6 = ISZERO vb91V4a6
    0xb94S0x4a6: vb94V4a6(0xbb1) = CONST 
    0xb97S0x4a6: JUMPI vb94V4a6(0xbb1), vb93V4a6

    Begin block 0xbb1B0x4a6
    prev=[0xb84B0x4a6, 0xb98B0x4a6], succ=[0xbcfB0x4a6, 0xbd3B0x4a6]
    =================================
    0xbb1_0x1S0x4a6: vbb1_1V4a6 = PHI vb8dV4a6, vbaeV4a6
    0xbbaS0x4a6: vbbaV4a6(0x0) = CONST 
    0xbbcS0x4a6: vbbcV4a6(0x40) = CONST 
    0xbbeS0x4a6: vbbeV4a6 = MLOAD vbbcV4a6(0x40)
    0xbc1S0x4a6: vbc1V4a6 = SUB vbb1_1V4a6, vbbeV4a6
    0xbc3S0x4a6: vbc3V4a6(0x0) = CONST 
    0xbc7S0x4a6: vbc7V4a6 = EXTCODESIZE vaa6V4a6
    0xbc8S0x4a6: vbc8V4a6 = ISZERO vbc7V4a6
    0xbcaS0x4a6: vbcaV4a6 = ISZERO vbc8V4a6
    0xbcbS0x4a6: vbcbV4a6(0xbd3) = CONST 
    0xbceS0x4a6: JUMPI vbcbV4a6(0xbd3), vbcaV4a6

    Begin block 0xbcfB0x4a6
    prev=[0xbb1B0x4a6], succ=[]
    =================================
    0xbcfS0x4a6: vbcfV4a6(0x0) = CONST 
    0xbd2S0x4a6: REVERT vbcfV4a6(0x0), vbcfV4a6(0x0)

    Begin block 0xbd3B0x4a6
    prev=[0xbb1B0x4a6], succ=[0xbdeB0x4a6, 0xbe7B0x4a6]
    =================================
    0xbd5S0x4a6: vbd5V4a6 = GAS 
    0xbd6S0x4a6: vbd6V4a6 = CALL vbd5V4a6, vaa6V4a6, vbc3V4a6(0x0), vbbeV4a6, vbc1V4a6, vbbeV4a6, vbbaV4a6(0x0)
    0xbd7S0x4a6: vbd7V4a6 = ISZERO vbd6V4a6
    0xbd9S0x4a6: vbd9V4a6 = ISZERO vbd7V4a6
    0xbdaS0x4a6: vbdaV4a6(0xbe7) = CONST 
    0xbddS0x4a6: JUMPI vbdaV4a6(0xbe7), vbd9V4a6

    Begin block 0xbdeB0x4a6
    prev=[0xbd3B0x4a6], succ=[]
    =================================
    0xbdeS0x4a6: vbdeV4a6 = RETURNDATASIZE 
    0xbdfS0x4a6: vbdfV4a6(0x0) = CONST 
    0xbe2S0x4a6: RETURNDATACOPY vbdfV4a6(0x0), vbdfV4a6(0x0), vbdeV4a6
    0xbe3S0x4a6: vbe3V4a6 = RETURNDATASIZE 
    0xbe4S0x4a6: vbe4V4a6(0x0) = CONST 
    0xbe6S0x4a6: REVERT vbe4V4a6(0x0), vbe3V4a6

    Begin block 0xbe7B0x4a6
    prev=[0xbd3B0x4a6], succ=[0x10808B0x4a6]
    =================================
    0xbecS0x4a6: vbecV4a6(0x1) = CONST 
    0xbf0S0x4a6: vbf0V4a6(0x10808) = CONST 
    0xbf3S0x4a6: JUMP vbf0V4a6(0x10808)

    Begin block 0x10808B0x4a6
    prev=[0xbe7B0x4a6], succ=[0x52b]
    =================================
    0x1080fS0x4a6: JUMP v4a8(0x52b)

    Begin block 0xb98B0x4a6
    prev=[0xb84B0x4a6], succ=[0xbb1B0x4a6]
    =================================
    0xb9aS0x4a6: vb9aV4a6 = SUB vb8dV4a6, vb91V4a6
    0xb9cS0x4a6: vb9cV4a6 = MLOAD vb9aV4a6
    0xb9dS0x4a6: vb9dV4a6(0x1) = CONST 
    0xba0S0x4a6: vba0V4a6(0x20) = CONST 
    0xba2S0x4a6: vba2V4a6 = SUB vba0V4a6(0x20), vb91V4a6
    0xba3S0x4a6: vba3V4a6(0x100) = CONST 
    0xba6S0x4a6: vba6V4a6 = EXP vba3V4a6(0x100), vba2V4a6
    0xba7S0x4a6: vba7V4a6 = SUB vba6V4a6, vb9dV4a6(0x1)
    0xba8S0x4a6: vba8V4a6 = NOT vba7V4a6
    0xba9S0x4a6: vba9V4a6 = AND vba8V4a6, vb9cV4a6
    0xbabS0x4a6: MSTORE vb9aV4a6, vba9V4a6
    0xbacS0x4a6: vbacV4a6(0x20) = CONST 
    0xbaeS0x4a6: vbaeV4a6 = ADD vbacV4a6(0x20), vb9aV4a6
    0x7986S0x4a6: v7986V4a6(0xbb1) = CONST 
    0x79a6S0x4a6: JUMP v7986V4a6(0xbb1)

    Begin block 0xb72B0x4a6
    prev=[0xb69B0x4a6], succ=[0xb69B0x4a6]
    =================================
    0xb72_0x0S0x4a6: vb72_0V4a6 = PHI vb67V4a6(0x0), vb7dV4a6
    0xb74S0x4a6: vb74V4a6 = ADD vb62V4a6, vb72_0V4a6
    0xb75S0x4a6: vb75V4a6 = MLOAD vb74V4a6
    0xb78S0x4a6: vb78V4a6 = ADD vb5aV4a6, vb72_0V4a6
    0xb79S0x4a6: MSTORE vb78V4a6, vb75V4a6
    0xb7aS0x4a6: vb7aV4a6(0x20) = CONST 
    0xb7dS0x4a6: vb7dV4a6 = ADD vb72_0V4a6, vb7aV4a6(0x20)
    0xb80S0x4a6: vb80V4a6(0xb69) = CONST 
    0xb83S0x4a6: JUMP vb80V4a6(0xb69)

}

function allowance(address,address)() public {
    Begin block 0x545
    prev=[], succ=[0x54d, 0x551]
    =================================
    0x546: v546 = CALLVALUE 
    0x548: v548 = ISZERO v546
    0x549: v549(0x551) = CONST 
    0x54c: JUMPI v549(0x551), v548

    Begin block 0x54d
    prev=[0x545], succ=[]
    =================================
    0x54d: v54d(0x0) = CONST 
    0x550: REVERT v54d(0x0), v54d(0x0)

    Begin block 0x551
    prev=[0x545], succ=[0xbfd]
    =================================
    0x553: v553(0x5a6) = CONST 
    0x556: v556(0x4) = CONST 
    0x559: v559 = CALLDATASIZE 
    0x55a: v55a = SUB v559, v556(0x4)
    0x55c: v55c = ADD v556(0x4), v55a
    0x560: v560 = CALLDATALOAD v556(0x4)
    0x561: v561(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x576: v576 = AND v561(0xffffffffffffffffffffffffffffffffffffffff), v560
    0x578: v578(0x20) = CONST 
    0x57a: v57a(0x24) = ADD v578(0x20), v556(0x4)
    0x580: v580 = CALLDATALOAD v57a(0x24)
    0x581: v581(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x596: v596 = AND v581(0xffffffffffffffffffffffffffffffffffffffff), v580
    0x598: v598(0x20) = CONST 
    0x59a: v59a(0x44) = ADD v598(0x20), v57a(0x24)
    0x5a2: v5a2(0xbfd) = CONST 
    0x5a5: JUMP v5a2(0xbfd)

    Begin block 0xbfd
    prev=[0x551], succ=[0x5a6]
    =================================
    0xbfe: vbfe(0x5) = CONST 
    0xc00: vc00(0x20) = CONST 
    0xc02: MSTORE vc00(0x20), vbfe(0x5)
    0xc04: vc04(0x0) = CONST 
    0xc06: MSTORE vc04(0x0), v576
    0xc07: vc07(0x40) = CONST 
    0xc09: vc09(0x0) = CONST 
    0xc0b: vc0b = SHA3 vc09(0x0), vc07(0x40)
    0xc0c: vc0c(0x20) = CONST 
    0xc0e: MSTORE vc0c(0x20), vc0b
    0xc10: vc10(0x0) = CONST 
    0xc12: MSTORE vc10(0x0), v596
    0xc13: vc13(0x40) = CONST 
    0xc15: vc15(0x0) = CONST 
    0xc17: vc17 = SHA3 vc15(0x0), vc13(0x40)
    0xc18: vc18(0x0) = CONST 
    0xc1f: vc1f = SLOAD vc17
    0xc21: JUMP v553(0x5a6)

    Begin block 0x5a6
    prev=[0xbfd], succ=[]
    =================================
    0x5a7: v5a7(0x40) = CONST 
    0x5a9: v5a9 = MLOAD v5a7(0x40)
    0x5ad: MSTORE v5a9, vc1f
    0x5ae: v5ae(0x20) = CONST 
    0x5b0: v5b0 = ADD v5ae(0x20), v5a9
    0x5b4: v5b4(0x40) = CONST 
    0x5b6: v5b6 = MLOAD v5b4(0x40)
    0x5b9: v5b9(0x20) = SUB v5b0, v5b6
    0x5bb: RETURN v5b6, v5b9(0x20)

}

function giveBlockReward()() public {
    Begin block 0x5bc
    prev=[], succ=[0x5c4, 0x5c8]
    =================================
    0x5bd: v5bd = CALLVALUE 
    0x5bf: v5bf = ISZERO v5bd
    0x5c0: v5c0(0x5c8) = CONST 
    0x5c3: JUMPI v5c0(0x5c8), v5bf

    Begin block 0x5c4
    prev=[0x5bc], succ=[]
    =================================
    0x5c4: v5c4(0x0) = CONST 
    0x5c7: REVERT v5c4(0x0), v5c4(0x0)

    Begin block 0x5c8
    prev=[0x5bc], succ=[0xc22]
    =================================
    0x5ca: v5ca(0x5d1) = CONST 
    0x5cd: v5cd(0xc22) = CONST 
    0x5d0: JUMP v5cd(0xc22)

    Begin block 0xc22
    prev=[0x5c8], succ=[0x5d1]
    =================================
    0xc23: vc23(0x1) = CONST 
    0xc25: vc25(0x4) = CONST 
    0xc27: vc27(0x0) = CONST 
    0xc29: vc29 = COINBASE 
    0xc2a: vc2a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc3f: vc3f = AND vc2a(0xffffffffffffffffffffffffffffffffffffffff), vc29
    0xc40: vc40(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc55: vc55 = AND vc40(0xffffffffffffffffffffffffffffffffffffffff), vc3f
    0xc57: MSTORE vc27(0x0), vc55
    0xc58: vc58(0x20) = CONST 
    0xc5a: vc5a(0x20) = ADD vc58(0x20), vc27(0x0)
    0xc5d: MSTORE vc5a(0x20), vc25(0x4)
    0xc5e: vc5e(0x20) = CONST 
    0xc60: vc60(0x40) = ADD vc5e(0x20), vc5a(0x20)
    0xc61: vc61(0x0) = CONST 
    0xc63: vc63 = SHA3 vc61(0x0), vc60(0x40)
    0xc64: vc64(0x0) = CONST 
    0xc68: vc68 = SLOAD vc63
    0xc69: vc69 = ADD vc68, vc23(0x1)
    0xc6f: SSTORE vc63, vc69
    0xc71: JUMP v5ca(0x5d1)

    Begin block 0x5d1
    prev=[0xc22], succ=[]
    =================================
    0x5d2: STOP 

}

function 0xc72(vc72arg0, vc72arg1, vc72arg2, vc72arg3) private {
    Begin block 0xc72
    prev=[], succ=[0xc95, 0xc99]
    =================================
    0xc73: vc73(0x0) = CONST 
    0xc77: vc77(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc8c: vc8c = AND vc77(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xc8d: vc8d = EQ vc8c, vc73(0x0)
    0xc8e: vc8e = ISZERO vc8d
    0xc8f: vc8f = ISZERO vc8e
    0xc90: vc90 = ISZERO vc8f
    0xc91: vc91(0xc99) = CONST 
    0xc94: JUMPI vc91(0xc99), vc90

    Begin block 0xc95
    prev=[0xc72], succ=[]
    =================================
    0xc95: vc95(0x0) = CONST 
    0xc98: REVERT vc95(0x0), vc95(0x0)

    Begin block 0xc99
    prev=[0xc72], succ=[0xce3, 0xce7]
    =================================
    0xc9b: vc9b(0x4) = CONST 
    0xc9d: vc9d(0x0) = CONST 
    0xca0: vca0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcb5: vcb5 = AND vca0(0xffffffffffffffffffffffffffffffffffffffff), vc72arg2
    0xcb6: vcb6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xccb: vccb = AND vcb6(0xffffffffffffffffffffffffffffffffffffffff), vcb5
    0xccd: MSTORE vc9d(0x0), vccb
    0xcce: vcce(0x20) = CONST 
    0xcd0: vcd0(0x20) = ADD vcce(0x20), vc9d(0x0)
    0xcd3: MSTORE vcd0(0x20), vc9b(0x4)
    0xcd4: vcd4(0x20) = CONST 
    0xcd6: vcd6(0x40) = ADD vcd4(0x20), vcd0(0x20)
    0xcd7: vcd7(0x0) = CONST 
    0xcd9: vcd9 = SHA3 vcd7(0x0), vcd6(0x40)
    0xcda: vcda = SLOAD vcd9
    0xcdb: vcdb = LT vcda, vc72arg0
    0xcdc: vcdc = ISZERO vcdb
    0xcdd: vcdd = ISZERO vcdc
    0xcde: vcde = ISZERO vcdd
    0xcdf: vcdf(0xce7) = CONST 
    0xce2: JUMPI vcdf(0xce7), vcde

    Begin block 0xce3
    prev=[0xc99], succ=[]
    =================================
    0xce3: vce3(0x0) = CONST 
    0xce6: REVERT vce3(0x0), vce3(0x0)

    Begin block 0xce7
    prev=[0xc99], succ=[0xd71, 0xd75]
    =================================
    0xce8: vce8(0x4) = CONST 
    0xcea: vcea(0x0) = CONST 
    0xced: vced(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd02: vd02 = AND vced(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xd03: vd03(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd18: vd18 = AND vd03(0xffffffffffffffffffffffffffffffffffffffff), vd02
    0xd1a: MSTORE vcea(0x0), vd18
    0xd1b: vd1b(0x20) = CONST 
    0xd1d: vd1d(0x20) = ADD vd1b(0x20), vcea(0x0)
    0xd20: MSTORE vd1d(0x20), vce8(0x4)
    0xd21: vd21(0x20) = CONST 
    0xd23: vd23(0x40) = ADD vd21(0x20), vd1d(0x20)
    0xd24: vd24(0x0) = CONST 
    0xd26: vd26 = SHA3 vd24(0x0), vd23(0x40)
    0xd27: vd27 = SLOAD vd26
    0xd29: vd29(0x4) = CONST 
    0xd2b: vd2b(0x0) = CONST 
    0xd2e: vd2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd43: vd43 = AND vd2e(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xd44: vd44(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd59: vd59 = AND vd44(0xffffffffffffffffffffffffffffffffffffffff), vd43
    0xd5b: MSTORE vd2b(0x0), vd59
    0xd5c: vd5c(0x20) = CONST 
    0xd5e: vd5e(0x20) = ADD vd5c(0x20), vd2b(0x0)
    0xd61: MSTORE vd5e(0x20), vd29(0x4)
    0xd62: vd62(0x20) = CONST 
    0xd64: vd64(0x40) = ADD vd62(0x20), vd5e(0x20)
    0xd65: vd65(0x0) = CONST 
    0xd67: vd67 = SHA3 vd65(0x0), vd64(0x40)
    0xd68: vd68 = SLOAD vd67
    0xd69: vd69 = ADD vd68, vc72arg0
    0xd6a: vd6a = GT vd69, vd27
    0xd6b: vd6b = ISZERO vd6a
    0xd6c: vd6c = ISZERO vd6b
    0xd6d: vd6d(0xd75) = CONST 
    0xd70: JUMPI vd6d(0xd75), vd6c

    Begin block 0xd71
    prev=[0xce7], succ=[]
    =================================
    0xd71: vd71(0x0) = CONST 
    0xd74: REVERT vd71(0x0), vd71(0x0)

    Begin block 0xd75
    prev=[0xce7], succ=[0xf81, 0xf82]
    =================================
    0xd76: vd76(0x4) = CONST 
    0xd78: vd78(0x0) = CONST 
    0xd7b: vd7b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd90: vd90 = AND vd7b(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xd91: vd91(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xda6: vda6 = AND vd91(0xffffffffffffffffffffffffffffffffffffffff), vd90
    0xda8: MSTORE vd78(0x0), vda6
    0xda9: vda9(0x20) = CONST 
    0xdab: vdab(0x20) = ADD vda9(0x20), vd78(0x0)
    0xdae: MSTORE vdab(0x20), vd76(0x4)
    0xdaf: vdaf(0x20) = CONST 
    0xdb1: vdb1(0x40) = ADD vdaf(0x20), vdab(0x20)
    0xdb2: vdb2(0x0) = CONST 
    0xdb4: vdb4 = SHA3 vdb2(0x0), vdb1(0x40)
    0xdb5: vdb5 = SLOAD vdb4
    0xdb6: vdb6(0x4) = CONST 
    0xdb8: vdb8(0x0) = CONST 
    0xdbb: vdbb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdd0: vdd0 = AND vdbb(0xffffffffffffffffffffffffffffffffffffffff), vc72arg2
    0xdd1: vdd1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xde6: vde6 = AND vdd1(0xffffffffffffffffffffffffffffffffffffffff), vdd0
    0xde8: MSTORE vdb8(0x0), vde6
    0xde9: vde9(0x20) = CONST 
    0xdeb: vdeb(0x20) = ADD vde9(0x20), vdb8(0x0)
    0xdee: MSTORE vdeb(0x20), vdb6(0x4)
    0xdef: vdef(0x20) = CONST 
    0xdf1: vdf1(0x40) = ADD vdef(0x20), vdeb(0x20)
    0xdf2: vdf2(0x0) = CONST 
    0xdf4: vdf4 = SHA3 vdf2(0x0), vdf1(0x40)
    0xdf5: vdf5 = SLOAD vdf4
    0xdf6: vdf6 = ADD vdf5, vdb5
    0xdfa: vdfa(0x4) = CONST 
    0xdfc: vdfc(0x0) = CONST 
    0xdff: vdff(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe14: ve14 = AND vdff(0xffffffffffffffffffffffffffffffffffffffff), vc72arg2
    0xe15: ve15(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe2a: ve2a = AND ve15(0xffffffffffffffffffffffffffffffffffffffff), ve14
    0xe2c: MSTORE vdfc(0x0), ve2a
    0xe2d: ve2d(0x20) = CONST 
    0xe2f: ve2f(0x20) = ADD ve2d(0x20), vdfc(0x0)
    0xe32: MSTORE ve2f(0x20), vdfa(0x4)
    0xe33: ve33(0x20) = CONST 
    0xe35: ve35(0x40) = ADD ve33(0x20), ve2f(0x20)
    0xe36: ve36(0x0) = CONST 
    0xe38: ve38 = SHA3 ve36(0x0), ve35(0x40)
    0xe39: ve39(0x0) = CONST 
    0xe3d: ve3d = SLOAD ve38
    0xe3e: ve3e = SUB ve3d, vc72arg0
    0xe44: SSTORE ve38, ve3e
    0xe47: ve47(0x4) = CONST 
    0xe49: ve49(0x0) = CONST 
    0xe4c: ve4c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe61: ve61 = AND ve4c(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xe62: ve62(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe77: ve77 = AND ve62(0xffffffffffffffffffffffffffffffffffffffff), ve61
    0xe79: MSTORE ve49(0x0), ve77
    0xe7a: ve7a(0x20) = CONST 
    0xe7c: ve7c(0x20) = ADD ve7a(0x20), ve49(0x0)
    0xe7f: MSTORE ve7c(0x20), ve47(0x4)
    0xe80: ve80(0x20) = CONST 
    0xe82: ve82(0x40) = ADD ve80(0x20), ve7c(0x20)
    0xe83: ve83(0x0) = CONST 
    0xe85: ve85 = SHA3 ve83(0x0), ve82(0x40)
    0xe86: ve86(0x0) = CONST 
    0xe8a: ve8a = SLOAD ve85
    0xe8b: ve8b = ADD ve8a, vc72arg0
    0xe91: SSTORE ve85, ve8b
    0xe94: ve94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xea9: vea9 = AND ve94(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xeab: veab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec0: vec0 = AND veab(0xffffffffffffffffffffffffffffffffffffffff), vc72arg2
    0xec1: vec1(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xee3: vee3(0x40) = CONST 
    0xee5: vee5 = MLOAD vee3(0x40)
    0xee9: MSTORE vee5, vc72arg0
    0xeea: veea(0x20) = CONST 
    0xeec: veec = ADD veea(0x20), vee5
    0xef0: vef0(0x40) = CONST 
    0xef2: vef2 = MLOAD vef0(0x40)
    0xef5: vef5(0x20) = SUB veec, vef2
    0xef7: LOG3 vef2, vef5(0x20), vec1(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vec0, vea9
    0xef9: vef9(0x4) = CONST 
    0xefb: vefb(0x0) = CONST 
    0xefe: vefe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf13: vf13 = AND vefe(0xffffffffffffffffffffffffffffffffffffffff), vc72arg1
    0xf14: vf14(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf29: vf29 = AND vf14(0xffffffffffffffffffffffffffffffffffffffff), vf13
    0xf2b: MSTORE vefb(0x0), vf29
    0xf2c: vf2c(0x20) = CONST 
    0xf2e: vf2e(0x20) = ADD vf2c(0x20), vefb(0x0)
    0xf31: MSTORE vf2e(0x20), vef9(0x4)
    0xf32: vf32(0x20) = CONST 
    0xf34: vf34(0x40) = ADD vf32(0x20), vf2e(0x20)
    0xf35: vf35(0x0) = CONST 
    0xf37: vf37 = SHA3 vf35(0x0), vf34(0x40)
    0xf38: vf38 = SLOAD vf37
    0xf39: vf39(0x4) = CONST 
    0xf3b: vf3b(0x0) = CONST 
    0xf3e: vf3e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf53: vf53 = AND vf3e(0xffffffffffffffffffffffffffffffffffffffff), vc72arg2
    0xf54: vf54(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf69: vf69 = AND vf54(0xffffffffffffffffffffffffffffffffffffffff), vf53
    0xf6b: MSTORE vf3b(0x0), vf69
    0xf6c: vf6c(0x20) = CONST 
    0xf6e: vf6e(0x20) = ADD vf6c(0x20), vf3b(0x0)
    0xf71: MSTORE vf6e(0x20), vf39(0x4)
    0xf72: vf72(0x20) = CONST 
    0xf74: vf74(0x40) = ADD vf72(0x20), vf6e(0x20)
    0xf75: vf75(0x0) = CONST 
    0xf77: vf77 = SHA3 vf75(0x0), vf74(0x40)
    0xf78: vf78 = SLOAD vf77
    0xf79: vf79 = ADD vf78, vf38
    0xf7a: vf7a = EQ vf79, vdf6
    0xf7b: vf7b = ISZERO vf7a
    0xf7c: vf7c = ISZERO vf7b
    0xf7d: vf7d(0xf82) = CONST 
    0xf80: JUMPI vf7d(0xf82), vf7c

    Begin block 0xf81
    prev=[0xd75], succ=[]
    =================================
    0xf81: THROW 

    Begin block 0xf82
    prev=[0xd75], succ=[]
    =================================
    0xf87: RETURNPRIVATE vc72arg3

}

function fallback()() public {
    Begin block 0xdb
    prev=[], succ=[]
    =================================
    0xdc: vdc(0x0) = CONST 
    0xdf: REVERT vdc(0x0), vdc(0x0)

}

function name()() public {
    Begin block 0xe0
    prev=[], succ=[0xe8, 0xec]
    =================================
    0xe1: ve1 = CALLVALUE 
    0xe3: ve3 = ISZERO ve1
    0xe4: ve4(0xec) = CONST 
    0xe7: JUMPI ve4(0xec), ve3

    Begin block 0xe8
    prev=[0xe0], succ=[]
    =================================
    0xe8: ve8(0x0) = CONST 
    0xeb: REVERT ve8(0x0), ve8(0x0)

    Begin block 0xec
    prev=[0xe0], succ=[0x5d3B0xec]
    =================================
    0xee: vee(0xf5) = CONST 
    0xf1: vf1(0x5d3) = CONST 
    0xf4: JUMP vf1(0x5d3)

    Begin block 0x5d3B0xec
    prev=[0xec], succ=[0x623B0xec, 0x1076cB0xec]
    =================================
    0x5d4S0xec: v5d4Vec(0x0) = CONST 
    0x5d7S0xec: v5d7Vec = SLOAD v5d4Vec(0x0)
    0x5d8S0xec: v5d8Vec(0x1) = CONST 
    0x5dbS0xec: v5dbVec(0x1) = CONST 
    0x5ddS0xec: v5ddVec = AND v5dbVec(0x1), v5d7Vec
    0x5deS0xec: v5deVec = ISZERO v5ddVec
    0x5dfS0xec: v5dfVec(0x100) = CONST 
    0x5e2S0xec: v5e2Vec = MUL v5dfVec(0x100), v5deVec
    0x5e3S0xec: v5e3Vec = SUB v5e2Vec, v5d8Vec(0x1)
    0x5e4S0xec: v5e4Vec = AND v5e3Vec, v5d7Vec
    0x5e5S0xec: v5e5Vec(0x2) = CONST 
    0x5e8S0xec: v5e8Vec = DIV v5e4Vec, v5e5Vec(0x2)
    0x5eaS0xec: v5eaVec(0x1f) = CONST 
    0x5ecS0xec: v5ecVec = ADD v5eaVec(0x1f), v5e8Vec
    0x5edS0xec: v5edVec(0x20) = CONST 
    0x5f1S0xec: v5f1Vec = DIV v5ecVec, v5edVec(0x20)
    0x5f2S0xec: v5f2Vec = MUL v5f1Vec, v5edVec(0x20)
    0x5f3S0xec: v5f3Vec(0x20) = CONST 
    0x5f5S0xec: v5f5Vec = ADD v5f3Vec(0x20), v5f2Vec
    0x5f6S0xec: v5f6Vec(0x40) = CONST 
    0x5f8S0xec: v5f8Vec = MLOAD v5f6Vec(0x40)
    0x5fbS0xec: v5fbVec = ADD v5f8Vec, v5f5Vec
    0x5fcS0xec: v5fcVec(0x40) = CONST 
    0x5feS0xec: MSTORE v5fcVec(0x40), v5fbVec
    0x605S0xec: MSTORE v5f8Vec, v5e8Vec
    0x606S0xec: v606Vec(0x20) = CONST 
    0x608S0xec: v608Vec = ADD v606Vec(0x20), v5f8Vec
    0x60bS0xec: v60bVec = SLOAD v5d4Vec(0x0)
    0x60cS0xec: v60cVec(0x1) = CONST 
    0x60fS0xec: v60fVec(0x1) = CONST 
    0x611S0xec: v611Vec = AND v60fVec(0x1), v60bVec
    0x612S0xec: v612Vec = ISZERO v611Vec
    0x613S0xec: v613Vec(0x100) = CONST 
    0x616S0xec: v616Vec = MUL v613Vec(0x100), v612Vec
    0x617S0xec: v617Vec = SUB v616Vec, v60cVec(0x1)
    0x618S0xec: v618Vec = AND v617Vec, v60bVec
    0x619S0xec: v619Vec(0x2) = CONST 
    0x61cS0xec: v61cVec = DIV v618Vec, v619Vec(0x2)
    0x61eS0xec: v61eVec = ISZERO v61cVec
    0x61fS0xec: v61fVec(0x1076c) = CONST 
    0x622S0xec: JUMPI v61fVec(0x1076c), v61eVec

    Begin block 0x623B0xec
    prev=[0x5d3B0xec], succ=[0x62bB0xec, 0x63eB0xec]
    =================================
    0x624S0xec: v624Vec(0x1f) = CONST 
    0x626S0xec: v626Vec = LT v624Vec(0x1f), v61cVec
    0x627S0xec: v627Vec(0x63e) = CONST 
    0x62aS0xec: JUMPI v627Vec(0x63e), v626Vec

    Begin block 0x62bB0xec
    prev=[0x623B0xec], succ=[0x10793B0xec]
    =================================
    0x62bS0xec: v62bVec(0x100) = CONST 
    0x630S0xec: v630Vec = SLOAD v5d4Vec(0x0)
    0x631S0xec: v631Vec = DIV v630Vec, v62bVec(0x100)
    0x632S0xec: v632Vec = MUL v631Vec, v62bVec(0x100)
    0x634S0xec: MSTORE v608Vec, v632Vec
    0x636S0xec: v636Vec(0x20) = CONST 
    0x638S0xec: v638Vec = ADD v636Vec(0x20), v608Vec
    0x63aS0xec: v63aVec(0x10793) = CONST 
    0x63dS0xec: JUMP v63aVec(0x10793)

    Begin block 0x10793B0xec
    prev=[0x62bB0xec], succ=[0xf5]
    =================================
    0x1079aS0xec: JUMP vee(0xf5)

    Begin block 0xf5
    prev=[0x1076cB0xec, 0x10793B0xec, 0x1082fB0xec], succ=[0x11a]
    =================================
    0xf6: vf6(0x40) = CONST 
    0xf8: vf8 = MLOAD vf6(0x40)
    0xfb: vfb(0x20) = CONST 
    0xfd: vfd = ADD vfb(0x20), vf8
    0x100: v100(0x20) = SUB vfd, vf8
    0x102: MSTORE vf8, v100(0x20)
    0x106: v106 = MLOAD v5f8Vec
    0x108: MSTORE vfd, v106
    0x109: v109(0x20) = CONST 
    0x10b: v10b = ADD v109(0x20), vfd
    0x10f: v10f = MLOAD v5f8Vec
    0x111: v111(0x20) = CONST 
    0x113: v113 = ADD v111(0x20), v5f8Vec
    0x118: v118(0x0) = CONST 
    0x1f86: v1f86(0x11a) = CONST 
    0x1fa6: JUMP v1f86(0x11a)

    Begin block 0x11a
    prev=[0xf5, 0x123], succ=[0x135, 0x123]
    =================================
    0x11a_0x0: v11a_0 = PHI v118(0x0), v12e
    0x11d: v11d = LT v11a_0, v10f
    0x11e: v11e = ISZERO v11d
    0x11f: v11f(0x135) = CONST 
    0x122: JUMPI v11f(0x135), v11e

    Begin block 0x135
    prev=[0x11a], succ=[0x162, 0x149]
    =================================
    0x13e: v13e = ADD v10f, v10b
    0x140: v140(0x1f) = CONST 
    0x142: v142 = AND v140(0x1f), v10f
    0x144: v144 = ISZERO v142
    0x145: v145(0x162) = CONST 
    0x148: JUMPI v145(0x162), v144

    Begin block 0x162
    prev=[0x135, 0x149], succ=[]
    =================================
    0x162_0x1: v162_1 = PHI v13e, v15f
    0x168: v168(0x40) = CONST 
    0x16a: v16a = MLOAD v168(0x40)
    0x16d: v16d = SUB v162_1, v16a
    0x16f: RETURN v16a, v16d

    Begin block 0x149
    prev=[0x135], succ=[0x162]
    =================================
    0x14b: v14b = SUB v13e, v142
    0x14d: v14d = MLOAD v14b
    0x14e: v14e(0x1) = CONST 
    0x151: v151(0x20) = CONST 
    0x153: v153 = SUB v151(0x20), v142
    0x154: v154(0x100) = CONST 
    0x157: v157 = EXP v154(0x100), v153
    0x158: v158 = SUB v157, v14e(0x1)
    0x159: v159 = NOT v158
    0x15a: v15a = AND v159, v14d
    0x15c: MSTORE v14b, v15a
    0x15d: v15d(0x20) = CONST 
    0x15f: v15f = ADD v15d(0x20), v14b
    0x2986: v2986(0x162) = CONST 
    0x29a6: JUMP v2986(0x162)

    Begin block 0x123
    prev=[0x11a], succ=[0x11a]
    =================================
    0x123_0x0: v123_0 = PHI v118(0x0), v12e
    0x125: v125 = ADD v113, v123_0
    0x126: v126 = MLOAD v125
    0x129: v129 = ADD v10b, v123_0
    0x12a: MSTORE v129, v126
    0x12b: v12b(0x20) = CONST 
    0x12e: v12e = ADD v123_0, v12b(0x20)
    0x131: v131(0x11a) = CONST 
    0x134: JUMP v131(0x11a)

    Begin block 0x63eB0xec
    prev=[0x623B0xec], succ=[0x64cB0xec]
    =================================
    0x640S0xec: v640Vec = ADD v608Vec, v61cVec
    0x643S0xec: v643Vec(0x0) = CONST 
    0x645S0xec: MSTORE v643Vec(0x0), v5d4Vec(0x0)
    0x646S0xec: v646Vec(0x20) = CONST 
    0x648S0xec: v648Vec(0x0) = CONST 
    0x64aS0xec: v64aVec = SHA3 v648Vec(0x0), v646Vec(0x20)
    0x4786S0xec: v4786Vec(0x64c) = CONST 
    0x47a6S0xec: JUMP v4786Vec(0x64c)

    Begin block 0x64cB0xec
    prev=[0x63eB0xec, 0x64cB0xec], succ=[0x64cB0xec, 0x660B0xec]
    =================================
    0x64c_0x0S0xec: v64c_0Vec = PHI v608Vec, v658Vec
    0x64c_0x1S0xec: v64c_1Vec = PHI v64aVec, v654Vec
    0x64eS0xec: v64eVec = SLOAD v64c_1Vec
    0x650S0xec: MSTORE v64c_0Vec, v64eVec
    0x652S0xec: v652Vec(0x1) = CONST 
    0x654S0xec: v654Vec = ADD v652Vec(0x1), v64c_1Vec
    0x656S0xec: v656Vec(0x20) = CONST 
    0x658S0xec: v658Vec = ADD v656Vec(0x20), v64c_0Vec
    0x65bS0xec: v65bVec = GT v640Vec, v658Vec
    0x65cS0xec: v65cVec(0x64c) = CONST 
    0x65fS0xec: JUMPI v65cVec(0x64c), v65bVec

    Begin block 0x660B0xec
    prev=[0x64cB0xec], succ=[0x1082fB0xec]
    =================================
    0x662S0xec: v662Vec = SUB v658Vec, v640Vec
    0x663S0xec: v663Vec(0x1f) = CONST 
    0x665S0xec: v665Vec = AND v663Vec(0x1f), v662Vec
    0x667S0xec: v667Vec = ADD v640Vec, v665Vec
    0x5186S0xec: v5186Vec(0x1082f) = CONST 
    0x51a6S0xec: JUMP v5186Vec(0x1082f)

    Begin block 0x1082fB0xec
    prev=[0x660B0xec], succ=[0xf5]
    =================================
    0x10836S0xec: JUMP vee(0xf5)

    Begin block 0x1076cB0xec
    prev=[0x5d3B0xec], succ=[0xf5]
    =================================
    0x10773S0xec: JUMP vee(0xf5)

}

