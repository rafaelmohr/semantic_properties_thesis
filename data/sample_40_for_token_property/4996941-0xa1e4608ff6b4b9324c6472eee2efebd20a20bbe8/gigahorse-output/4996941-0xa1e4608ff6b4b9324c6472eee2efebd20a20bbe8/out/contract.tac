function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x181ac]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xc3ac: vc3ac(0x181ac) = CONST 
    0xc3cc: JUMPI vc3ac(0x181ac), v8

    Begin block 0xd
    prev=[0x0], succ=[0x18bac, 0x27]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0xe0) = CONST 
    0x14: v14(0x2) = CONST 
    0x16: v16(0x100000000000000000000000000000000000000000000000000000000) = EXP v14(0x2), v12(0xe0)
    0x17: v17(0x0) = CONST 
    0x19: v19 = CALLDATALOAD v17(0x0)
    0x1a: v1a = DIV v19, v16(0x100000000000000000000000000000000000000000000000000000000)
    0x1b: v1b = AND v1a, vd(0xffffffff)
    0x1c: v1c(0x1f98394d) = CONST 
    0x22: v22 = EQ v1b, v1c(0x1f98394d)
    0xcdac: vcdac(0x18bac) = CONST 
    0xcdcc: JUMPI vcdac(0x18bac), v22

    Begin block 0x18bac
    prev=[0xd], succ=[]
    =================================
    0x18bcc: v18bcc(0x2a4) = CONST 
    0x18bec: CALLPRIVATE v18bcc(0x2a4)

    Begin block 0x27
    prev=[0xd], succ=[0x195ac, 0x32]
    =================================
    0x28: v28(0x2605b3c7) = CONST 
    0x2d: v2d = EQ v28(0x2605b3c7), v1b
    0xd7ac: vd7ac(0x195ac) = CONST 
    0xd7cc: JUMPI vd7ac(0x195ac), v2d

    Begin block 0x195ac
    prev=[0x27], succ=[]
    =================================
    0x195cc: v195cc(0x2c9) = CONST 
    0x195ec: CALLPRIVATE v195cc(0x2c9)

    Begin block 0x32
    prev=[0x27], succ=[0x19fac, 0x3d]
    =================================
    0x33: v33(0x316cb1b4) = CONST 
    0x38: v38 = EQ v33(0x316cb1b4), v1b
    0xe1ac: ve1ac(0x19fac) = CONST 
    0xe1cc: JUMPI ve1ac(0x19fac), v38

    Begin block 0x19fac
    prev=[0x32], succ=[]
    =================================
    0x19fcc: v19fcc(0x2fe) = CONST 
    0x19fec: CALLPRIVATE v19fcc(0x2fe)

    Begin block 0x3d
    prev=[0x32], succ=[0x1a9ac, 0x48]
    =================================
    0x3e: v3e(0x334191f7) = CONST 
    0x43: v43 = EQ v3e(0x334191f7), v1b
    0xebac: vebac(0x1a9ac) = CONST 
    0xebcc: JUMPI vebac(0x1a9ac), v43

    Begin block 0x1a9ac
    prev=[0x3d], succ=[]
    =================================
    0x1a9cc: v1a9cc(0x313) = CONST 
    0x1a9ec: CALLPRIVATE v1a9cc(0x313)

    Begin block 0x48
    prev=[0x3d], succ=[0x1b3ac, 0x53]
    =================================
    0x49: v49(0x4a35035a) = CONST 
    0x4e: v4e = EQ v49(0x4a35035a), v1b
    0xf5ac: vf5ac(0x1b3ac) = CONST 
    0xf5cc: JUMPI vf5ac(0x1b3ac), v4e

    Begin block 0x1b3ac
    prev=[0x48], succ=[]
    =================================
    0x1b3cc: v1b3cc(0x326) = CONST 
    0x1b3ec: CALLPRIVATE v1b3cc(0x326)

    Begin block 0x53
    prev=[0x48], succ=[0x1bdac, 0x5e]
    =================================
    0x54: v54(0x5adf292f) = CONST 
    0x59: v59 = EQ v54(0x5adf292f), v1b
    0xffac: vffac(0x1bdac) = CONST 
    0xffcc: JUMPI vffac(0x1bdac), v59

    Begin block 0x1bdac
    prev=[0x53], succ=[]
    =================================
    0x1bdcc: v1bdcc(0x339) = CONST 
    0x1bdec: CALLPRIVATE v1bdcc(0x339)

    Begin block 0x5e
    prev=[0x53], succ=[0x1c7ac, 0x69]
    =================================
    0x5f: v5f(0x604e7af6) = CONST 
    0x64: v64 = EQ v5f(0x604e7af6), v1b
    0x109ac: v109ac(0x1c7ac) = CONST 
    0x109cc: JUMPI v109ac(0x1c7ac), v64

    Begin block 0x1c7ac
    prev=[0x5e], succ=[]
    =================================
    0x1c7cc: v1c7cc(0x34c) = CONST 
    0x1c7ec: CALLPRIVATE v1c7cc(0x34c)

    Begin block 0x69
    prev=[0x5e], succ=[0x1d1ac, 0x74]
    =================================
    0x6a: v6a(0x65db63d0) = CONST 
    0x6f: v6f = EQ v6a(0x65db63d0), v1b
    0x113ac: v113ac(0x1d1ac) = CONST 
    0x113cc: JUMPI v113ac(0x1d1ac), v6f

    Begin block 0x1d1ac
    prev=[0x69], succ=[]
    =================================
    0x1d1cc: v1d1cc(0x35f) = CONST 
    0x1d1ec: CALLPRIVATE v1d1cc(0x35f)

    Begin block 0x74
    prev=[0x69], succ=[0x1dbac, 0x7f]
    =================================
    0x75: v75(0x6bcc28a9) = CONST 
    0x7a: v7a = EQ v75(0x6bcc28a9), v1b
    0x11dac: v11dac(0x1dbac) = CONST 
    0x11dcc: JUMPI v11dac(0x1dbac), v7a

    Begin block 0x1dbac
    prev=[0x74], succ=[]
    =================================
    0x1dbcc: v1dbcc(0x372) = CONST 
    0x1dbec: CALLPRIVATE v1dbcc(0x372)

    Begin block 0x7f
    prev=[0x74], succ=[0x1e5ac, 0x8a]
    =================================
    0x80: v80(0x7be2d5a2) = CONST 
    0x85: v85 = EQ v80(0x7be2d5a2), v1b
    0x127ac: v127ac(0x1e5ac) = CONST 
    0x127cc: JUMPI v127ac(0x1e5ac), v85

    Begin block 0x1e5ac
    prev=[0x7f], succ=[]
    =================================
    0x1e5cc: v1e5cc(0x385) = CONST 
    0x1e5ec: CALLPRIVATE v1e5cc(0x385)

    Begin block 0x8a
    prev=[0x7f], succ=[0x1efac, 0x95]
    =================================
    0x8b: v8b(0x853828b6) = CONST 
    0x90: v90 = EQ v8b(0x853828b6), v1b
    0x131ac: v131ac(0x1efac) = CONST 
    0x131cc: JUMPI v131ac(0x1efac), v90

    Begin block 0x1efac
    prev=[0x8a], succ=[]
    =================================
    0x1efcc: v1efcc(0x39e) = CONST 
    0x1efec: CALLPRIVATE v1efcc(0x39e)

    Begin block 0x95
    prev=[0x8a], succ=[0xa0, 0x1f9ac]
    =================================
    0x96: v96(0x8da5cb5b) = CONST 
    0x9b: v9b = EQ v96(0x8da5cb5b), v1b
    0x13bac: v13bac(0x1f9ac) = CONST 
    0x13bcc: JUMPI v13bac(0x1f9ac), v9b

    Begin block 0xa0
    prev=[0x95], succ=[0x203ac, 0xab]
    =================================
    0xa1: va1(0x98f9724f) = CONST 
    0xa6: va6 = EQ va1(0x98f9724f), v1b
    0x145ac: v145ac(0x203ac) = CONST 
    0x145cc: JUMPI v145ac(0x203ac), va6

    Begin block 0x203ac
    prev=[0xa0], succ=[]
    =================================
    0x203cc: v203cc(0x3e0) = CONST 
    0x203ec: CALLPRIVATE v203cc(0x3e0)

    Begin block 0xab
    prev=[0xa0], succ=[0x20dac, 0xb6]
    =================================
    0xac: vac(0xa2558ee2) = CONST 
    0xb1: vb1 = EQ vac(0xa2558ee2), v1b
    0x14fac: v14fac(0x20dac) = CONST 
    0x14fcc: JUMPI v14fac(0x20dac), vb1

    Begin block 0x20dac
    prev=[0xab], succ=[]
    =================================
    0x20dcc: v20dcc(0x3f3) = CONST 
    0x20dec: CALLPRIVATE v20dcc(0x3f3)

    Begin block 0xb6
    prev=[0xab], succ=[0x217ac, 0xc1]
    =================================
    0xb7: vb7(0xb2b158e8) = CONST 
    0xbc: vbc = EQ vb7(0xb2b158e8), v1b
    0x159ac: v159ac(0x217ac) = CONST 
    0x159cc: JUMPI v159ac(0x217ac), vbc

    Begin block 0x217ac
    prev=[0xb6], succ=[]
    =================================
    0x217cc: v217cc(0x406) = CONST 
    0x217ec: CALLPRIVATE v217cc(0x406)

    Begin block 0xc1
    prev=[0xb6], succ=[0x221ac, 0xcc]
    =================================
    0xc2: vc2(0xf2fde38b) = CONST 
    0xc7: vc7 = EQ vc2(0xf2fde38b), v1b
    0x163ac: v163ac(0x221ac) = CONST 
    0x163cc: JUMPI v163ac(0x221ac), vc7

    Begin block 0x221ac
    prev=[0xc1], succ=[]
    =================================
    0x221cc: v221cc(0x41c) = CONST 
    0x221ec: CALLPRIVATE v221cc(0x41c)

    Begin block 0xcc
    prev=[0xc1], succ=[0x22bac, 0xd7]
    =================================
    0xcd: vcd(0xf36d1e4e) = CONST 
    0xd2: vd2 = EQ vcd(0xf36d1e4e), v1b
    0x16dac: v16dac(0x22bac) = CONST 
    0x16dcc: JUMPI v16dac(0x22bac), vd2

    Begin block 0x22bac
    prev=[0xcc], succ=[]
    =================================
    0x22bcc: v22bcc(0x43b) = CONST 
    0x22bec: CALLPRIVATE v22bcc(0x43b)

    Begin block 0xd7
    prev=[0xcc], succ=[0x181ac, 0x235ac]
    =================================
    0xd8: vd8(0xff757d59) = CONST 
    0xdd: vdd = EQ vd8(0xff757d59), v1b
    0x177ac: v177ac(0x235ac) = CONST 
    0x177cc: JUMPI v177ac(0x235ac), vdd

    Begin block 0x181ac
    prev=[0x0, 0xd7], succ=[]
    =================================
    0x181cc: v181cc(0xe2) = CONST 
    0x181ec: CALLPRIVATE v181cc(0xe2)

    Begin block 0x235ac
    prev=[0xd7], succ=[]
    =================================
    0x235cc: v235cc(0x457) = CONST 
    0x235ec: CALLPRIVATE v235cc(0x457)

    Begin block 0x1f9ac
    prev=[0x95], succ=[]
    =================================
    0x1f9cc: v1f9cc(0x3b1) = CONST 
    0x1f9ec: CALLPRIVATE v1f9cc(0x3b1)

}

function basicReward()() public {
    Begin block 0x2a4
    prev=[], succ=[0x2ab, 0x2af]
    =================================
    0x2a5: v2a5 = CALLVALUE 
    0x2a6: v2a6 = ISZERO v2a5
    0x2a7: v2a7(0x2af) = CONST 
    0x2aa: JUMPI v2a7(0x2af), v2a6

    Begin block 0x2ab
    prev=[0x2a4], succ=[]
    =================================
    0x2ab: v2ab(0x0) = CONST 
    0x2ae: REVERT v2ab(0x0), v2ab(0x0)

    Begin block 0x2af
    prev=[0x2a4], succ=[0x46a]
    =================================
    0x2b0: v2b0(0x5ec4) = CONST 
    0x2b3: v2b3(0x46a) = CONST 
    0x2b6: JUMP v2b3(0x46a)

    Begin block 0x46a
    prev=[0x2af], succ=[0x5ec4]
    =================================
    0x46b: v46b(0x5) = CONST 
    0x46d: v46d = SLOAD v46b(0x5)
    0x46f: JUMP v2b0(0x5ec4)

    Begin block 0x5ec4
    prev=[0x46a], succ=[]
    =================================
    0x5ec5: v5ec5(0x40) = CONST 
    0x5ec7: v5ec7 = MLOAD v5ec5(0x40)
    0x5eca: MSTORE v5ec7, v46d
    0x5ecb: v5ecb(0x20) = CONST 
    0x5ecd: v5ecd = ADD v5ecb(0x20), v5ec7
    0x5ece: v5ece(0x40) = CONST 
    0x5ed0: v5ed0 = MLOAD v5ece(0x40)
    0x5ed3: v5ed3(0x20) = SUB v5ecd, v5ed0
    0x5ed5: RETURN v5ed0, v5ed3(0x20)

}

function participant(address)() public {
    Begin block 0x2c9
    prev=[], succ=[0x2d0, 0x2d4]
    =================================
    0x2ca: v2ca = CALLVALUE 
    0x2cb: v2cb = ISZERO v2ca
    0x2cc: v2cc(0x2d4) = CONST 
    0x2cf: JUMPI v2cc(0x2d4), v2cb

    Begin block 0x2d0
    prev=[0x2c9], succ=[]
    =================================
    0x2d0: v2d0(0x0) = CONST 
    0x2d3: REVERT v2d0(0x0), v2d0(0x0)

    Begin block 0x2d4
    prev=[0x2c9], succ=[0x470]
    =================================
    0x2d5: v2d5(0x5ef5) = CONST 
    0x2d8: v2d8(0x1) = CONST 
    0x2da: v2da(0xa0) = CONST 
    0x2dc: v2dc(0x2) = CONST 
    0x2de: v2de(0x10000000000000000000000000000000000000000) = EXP v2dc(0x2), v2da(0xa0)
    0x2df: v2df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2de(0x10000000000000000000000000000000000000000), v2d8(0x1)
    0x2e0: v2e0(0x4) = CONST 
    0x2e2: v2e2 = CALLDATALOAD v2e0(0x4)
    0x2e3: v2e3 = AND v2e2, v2df(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e4: v2e4(0x470) = CONST 
    0x2e7: JUMP v2e4(0x470)

    Begin block 0x470
    prev=[0x2d4], succ=[0x5ef5]
    =================================
    0x471: v471(0x1) = CONST 
    0x473: v473(0xa0) = CONST 
    0x475: v475(0x2) = CONST 
    0x477: v477(0x10000000000000000000000000000000000000000) = EXP v475(0x2), v473(0xa0)
    0x478: v478(0xffffffffffffffffffffffffffffffffffffffff) = SUB v477(0x10000000000000000000000000000000000000000), v471(0x1)
    0x479: v479 = AND v478(0xffffffffffffffffffffffffffffffffffffffff), v2e3
    0x47a: v47a(0x0) = CONST 
    0x47e: MSTORE v47a(0x0), v479
    0x47f: v47f(0x9) = CONST 
    0x481: v481(0x20) = CONST 
    0x483: MSTORE v481(0x20), v47f(0x9)
    0x484: v484(0x40) = CONST 
    0x487: v487 = SHA3 v47a(0x0), v484(0x40)
    0x488: v488 = SLOAD v487
    0x489: v489(0xff) = CONST 
    0x48b: v48b = AND v489(0xff), v488
    0x48d: JUMP v2d5(0x5ef5)

    Begin block 0x5ef5
    prev=[0x470], succ=[]
    =================================
    0x5ef6: v5ef6(0x40) = CONST 
    0x5ef8: v5ef8 = MLOAD v5ef6(0x40)
    0x5ef9: v5ef9(0xff) = CONST 
    0x5efd: v5efd = AND v48b, v5ef9(0xff)
    0x5eff: MSTORE v5ef8, v5efd
    0x5f00: v5f00(0x20) = CONST 
    0x5f02: v5f02 = ADD v5f00(0x20), v5ef8
    0x5f03: v5f03(0x40) = CONST 
    0x5f05: v5f05 = MLOAD v5f03(0x40)
    0x5f08: v5f08(0x20) = SUB v5f02, v5f05
    0x5f0a: RETURN v5f05, v5f08(0x20)

}

function withdrawKittenCoins()() public {
    Begin block 0x2fe
    prev=[], succ=[0x305, 0x309]
    =================================
    0x2ff: v2ff = CALLVALUE 
    0x300: v300 = ISZERO v2ff
    0x301: v301(0x309) = CONST 
    0x304: JUMPI v301(0x309), v300

    Begin block 0x305
    prev=[0x2fe], succ=[]
    =================================
    0x305: v305(0x0) = CONST 
    0x308: REVERT v305(0x0), v305(0x0)

    Begin block 0x309
    prev=[0x2fe], succ=[0x48e]
    =================================
    0x30a: v30a(0x5f2a) = CONST 
    0x30d: v30d(0x48e) = CONST 
    0x310: JUMP v30d(0x48e)

    Begin block 0x48e
    prev=[0x309], succ=[0x4a5, 0x4a9]
    =================================
    0x48f: v48f(0x0) = CONST 
    0x491: v491 = SLOAD v48f(0x0)
    0x492: v492 = CALLER 
    0x493: v493(0x1) = CONST 
    0x495: v495(0xa0) = CONST 
    0x497: v497(0x2) = CONST 
    0x499: v499(0x10000000000000000000000000000000000000000) = EXP v497(0x2), v495(0xa0)
    0x49a: v49a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v499(0x10000000000000000000000000000000000000000), v493(0x1)
    0x49d: v49d = AND v49a(0xffffffffffffffffffffffffffffffffffffffff), v492
    0x49f: v49f = AND v491, v49a(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a0: v4a0 = EQ v49f, v49d
    0x4a1: v4a1(0x4a9) = CONST 
    0x4a4: JUMPI v4a1(0x4a9), v4a0

    Begin block 0x4a5
    prev=[0x48e], succ=[]
    =================================
    0x4a5: v4a5(0x0) = CONST 
    0x4a8: REVERT v4a5(0x0), v4a5(0x0)

    Begin block 0x4a9
    prev=[0x48e], succ=[0x510, 0x514]
    =================================
    0x4aa: v4aa(0x1) = CONST 
    0x4ac: v4ac = SLOAD v4aa(0x1)
    0x4ad: v4ad(0x0) = CONST 
    0x4b0: v4b0 = SLOAD v4ad(0x0)
    0x4b1: v4b1(0x1) = CONST 
    0x4b3: v4b3(0xa0) = CONST 
    0x4b5: v4b5(0x2) = CONST 
    0x4b7: v4b7(0x10000000000000000000000000000000000000000) = EXP v4b5(0x2), v4b3(0xa0)
    0x4b8: v4b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b7(0x10000000000000000000000000000000000000000), v4b1(0x1)
    0x4bb: v4bb = AND v4b8(0xffffffffffffffffffffffffffffffffffffffff), v4ac
    0x4bd: v4bd(0xa9059cbb) = CONST 
    0x4c4: v4c4 = AND v4b0, v4b8(0xffffffffffffffffffffffffffffffffffffffff)
    0x4c8: v4c8(0x70a08231) = CONST 
    0x4ce: v4ce = ADDRESS 
    0x4d0: v4d0(0x40) = CONST 
    0x4d2: v4d2 = MLOAD v4d0(0x40)
    0x4d3: v4d3(0x20) = CONST 
    0x4d5: v4d5 = ADD v4d3(0x20), v4d2
    0x4d6: MSTORE v4d5, v4ad(0x0)
    0x4d7: v4d7(0x40) = CONST 
    0x4d9: v4d9 = MLOAD v4d7(0x40)
    0x4da: v4da(0xe0) = CONST 
    0x4dc: v4dc(0x2) = CONST 
    0x4de: v4de(0x100000000000000000000000000000000000000000000000000000000) = EXP v4dc(0x2), v4da(0xe0)
    0x4df: v4df(0xffffffff) = CONST 
    0x4e5: v4e5(0x70a08231) = AND v4c8(0x70a08231), v4df(0xffffffff)
    0x4e6: v4e6(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL v4e5(0x70a08231), v4de(0x100000000000000000000000000000000000000000000000000000000)
    0x4e8: MSTORE v4d9, v4e6(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x4e9: v4e9(0x1) = CONST 
    0x4eb: v4eb(0xa0) = CONST 
    0x4ed: v4ed(0x2) = CONST 
    0x4ef: v4ef(0x10000000000000000000000000000000000000000) = EXP v4ed(0x2), v4eb(0xa0)
    0x4f0: v4f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ef(0x10000000000000000000000000000000000000000), v4e9(0x1)
    0x4f3: v4f3 = AND v4ce, v4f0(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f4: v4f4(0x4) = CONST 
    0x4f7: v4f7 = ADD v4d9, v4f4(0x4)
    0x4f8: MSTORE v4f7, v4f3
    0x4f9: v4f9(0x24) = CONST 
    0x4fb: v4fb = ADD v4f9(0x24), v4d9
    0x4fc: v4fc(0x20) = CONST 
    0x4fe: v4fe(0x40) = CONST 
    0x500: v500 = MLOAD v4fe(0x40)
    0x503: v503(0x24) = SUB v4fb, v500
    0x505: v505(0x0) = CONST 
    0x509: v509 = EXTCODESIZE v4bb
    0x50a: v50a = ISZERO v509
    0x50b: v50b = ISZERO v50a
    0x50c: v50c(0x514) = CONST 
    0x50f: JUMPI v50c(0x514), v50b

    Begin block 0x510
    prev=[0x4a9], succ=[]
    =================================
    0x510: v510(0x0) = CONST 
    0x513: REVERT v510(0x0), v510(0x0)

    Begin block 0x514
    prev=[0x4a9], succ=[0x521, 0x525]
    =================================
    0x515: v515(0x2c6) = CONST 
    0x518: v518 = GAS 
    0x519: v519 = SUB v518, v515(0x2c6)
    0x51a: v51a = CALL v519, v4bb, v505(0x0), v500, v503(0x24), v500, v4fc(0x20)
    0x51b: v51b = ISZERO v51a
    0x51c: v51c = ISZERO v51b
    0x51d: v51d(0x525) = CONST 
    0x520: JUMPI v51d(0x525), v51c

    Begin block 0x521
    prev=[0x514], succ=[]
    =================================
    0x521: v521(0x0) = CONST 
    0x524: REVERT v521(0x0), v521(0x0)

    Begin block 0x525
    prev=[0x514], succ=[0x577, 0x57b]
    =================================
    0x529: v529(0x40) = CONST 
    0x52b: v52b = MLOAD v529(0x40)
    0x52d: v52d = MLOAD v52b
    0x530: v530(0x0) = CONST 
    0x532: v532(0x40) = CONST 
    0x534: v534 = MLOAD v532(0x40)
    0x535: v535(0x20) = CONST 
    0x537: v537 = ADD v535(0x20), v534
    0x538: MSTORE v537, v530(0x0)
    0x539: v539(0x40) = CONST 
    0x53b: v53b = MLOAD v539(0x40)
    0x53c: v53c(0xe0) = CONST 
    0x53e: v53e(0x2) = CONST 
    0x540: v540(0x100000000000000000000000000000000000000000000000000000000) = EXP v53e(0x2), v53c(0xe0)
    0x541: v541(0xffffffff) = CONST 
    0x547: v547(0xa9059cbb) = AND v4bd(0xa9059cbb), v541(0xffffffff)
    0x548: v548(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = MUL v547(0xa9059cbb), v540(0x100000000000000000000000000000000000000000000000000000000)
    0x54a: MSTORE v53b, v548(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x54b: v54b(0x1) = CONST 
    0x54d: v54d(0xa0) = CONST 
    0x54f: v54f(0x2) = CONST 
    0x551: v551(0x10000000000000000000000000000000000000000) = EXP v54f(0x2), v54d(0xa0)
    0x552: v552(0xffffffffffffffffffffffffffffffffffffffff) = SUB v551(0x10000000000000000000000000000000000000000), v54b(0x1)
    0x555: v555 = AND v4c4, v552(0xffffffffffffffffffffffffffffffffffffffff)
    0x556: v556(0x4) = CONST 
    0x559: v559 = ADD v53b, v556(0x4)
    0x55a: MSTORE v559, v555
    0x55b: v55b(0x24) = CONST 
    0x55e: v55e = ADD v53b, v55b(0x24)
    0x55f: MSTORE v55e, v52d
    0x560: v560(0x44) = CONST 
    0x562: v562 = ADD v560(0x44), v53b
    0x563: v563(0x20) = CONST 
    0x565: v565(0x40) = CONST 
    0x567: v567 = MLOAD v565(0x40)
    0x56a: v56a(0x44) = SUB v562, v567
    0x56c: v56c(0x0) = CONST 
    0x570: v570 = EXTCODESIZE v4bb
    0x571: v571 = ISZERO v570
    0x572: v572 = ISZERO v571
    0x573: v573(0x57b) = CONST 
    0x576: JUMPI v573(0x57b), v572

    Begin block 0x577
    prev=[0x525], succ=[]
    =================================
    0x577: v577(0x0) = CONST 
    0x57a: REVERT v577(0x0), v577(0x0)

    Begin block 0x57b
    prev=[0x525], succ=[0x588, 0x58c]
    =================================
    0x57c: v57c(0x2c6) = CONST 
    0x57f: v57f = GAS 
    0x580: v580 = SUB v57f, v57c(0x2c6)
    0x581: v581 = CALL v580, v4bb, v56c(0x0), v567, v56a(0x44), v567, v563(0x20)
    0x582: v582 = ISZERO v581
    0x583: v583 = ISZERO v582
    0x584: v584(0x58c) = CONST 
    0x587: JUMPI v584(0x58c), v583

    Begin block 0x588
    prev=[0x57b], succ=[]
    =================================
    0x588: v588(0x0) = CONST 
    0x58b: REVERT v588(0x0), v588(0x0)

    Begin block 0x58c
    prev=[0x57b], succ=[0x5f2a]
    =================================
    0x590: v590(0x40) = CONST 
    0x592: v592 = MLOAD v590(0x40)
    0x594: v594 = MLOAD v592
    0x597: v597(0x0) = CONST 
    0x599: v599(0x3) = CONST 
    0x59b: SSTORE v599(0x3), v597(0x0)
    0x59c: JUMP v30a(0x5f2a)

    Begin block 0x5f2a
    prev=[0x58c], succ=[]
    =================================
    0x5f2b: STOP 

}

function donatorReward()() public {
    Begin block 0x313
    prev=[], succ=[0x31a, 0x31e]
    =================================
    0x314: v314 = CALLVALUE 
    0x315: v315 = ISZERO v314
    0x316: v316(0x31e) = CONST 
    0x319: JUMPI v316(0x31e), v315

    Begin block 0x31a
    prev=[0x313], succ=[]
    =================================
    0x31a: v31a(0x0) = CONST 
    0x31d: REVERT v31a(0x0), v31a(0x0)

    Begin block 0x31e
    prev=[0x313], succ=[0x59d]
    =================================
    0x31f: v31f(0x5f4b) = CONST 
    0x322: v322(0x59d) = CONST 
    0x325: JUMP v322(0x59d)

    Begin block 0x59d
    prev=[0x31e], succ=[0x5f4b]
    =================================
    0x59e: v59e(0x6) = CONST 
    0x5a0: v5a0 = SLOAD v59e(0x6)
    0x5a2: JUMP v31f(0x5f4b)

    Begin block 0x5f4b
    prev=[0x59d], succ=[]
    =================================
    0x5f4c: v5f4c(0x40) = CONST 
    0x5f4e: v5f4e = MLOAD v5f4c(0x40)
    0x5f51: MSTORE v5f4e, v5a0
    0x5f52: v5f52(0x20) = CONST 
    0x5f54: v5f54 = ADD v5f52(0x20), v5f4e
    0x5f55: v5f55(0x40) = CONST 
    0x5f57: v5f57 = MLOAD v5f55(0x40)
    0x5f5a: v5f5a(0x20) = SUB v5f54, v5f57
    0x5f5c: RETURN v5f57, v5f5a(0x20)

}

function dropNumber()() public {
    Begin block 0x326
    prev=[], succ=[0x32d, 0x331]
    =================================
    0x327: v327 = CALLVALUE 
    0x328: v328 = ISZERO v327
    0x329: v329(0x331) = CONST 
    0x32c: JUMPI v329(0x331), v328

    Begin block 0x32d
    prev=[0x326], succ=[]
    =================================
    0x32d: v32d(0x0) = CONST 
    0x330: REVERT v32d(0x0), v32d(0x0)

    Begin block 0x331
    prev=[0x326], succ=[0x5a3]
    =================================
    0x332: v332(0x5f7c) = CONST 
    0x335: v335(0x5a3) = CONST 
    0x338: JUMP v335(0x5a3)

    Begin block 0x5a3
    prev=[0x331], succ=[0x5f7c]
    =================================
    0x5a4: v5a4(0x1) = CONST 
    0x5a6: v5a6 = SLOAD v5a4(0x1)
    0x5a7: v5a7(0xa0) = CONST 
    0x5a9: v5a9(0x2) = CONST 
    0x5ab: v5ab(0x10000000000000000000000000000000000000000) = EXP v5a9(0x2), v5a7(0xa0)
    0x5ad: v5ad = DIV v5a6, v5ab(0x10000000000000000000000000000000000000000)
    0x5ae: v5ae(0xff) = CONST 
    0x5b0: v5b0 = AND v5ae(0xff), v5ad
    0x5b2: JUMP v332(0x5f7c)

    Begin block 0x5f7c
    prev=[0x5a3], succ=[]
    =================================
    0x5f7d: v5f7d(0x40) = CONST 
    0x5f7f: v5f7f = MLOAD v5f7d(0x40)
    0x5f80: v5f80(0xff) = CONST 
    0x5f84: v5f84 = AND v5b0, v5f80(0xff)
    0x5f86: MSTORE v5f7f, v5f84
    0x5f87: v5f87(0x20) = CONST 
    0x5f89: v5f89 = ADD v5f87(0x20), v5f7f
    0x5f8a: v5f8a(0x40) = CONST 
    0x5f8c: v5f8c = MLOAD v5f8a(0x40)
    0x5f8f: v5f8f(0x20) = SUB v5f89, v5f8c
    0x5f91: RETURN v5f8c, v5f8f(0x20)

}

function updateKittenCoinsRemainingToDrop()() public {
    Begin block 0x339
    prev=[], succ=[0x340, 0x344]
    =================================
    0x33a: v33a = CALLVALUE 
    0x33b: v33b = ISZERO v33a
    0x33c: v33c(0x344) = CONST 
    0x33f: JUMPI v33c(0x344), v33b

    Begin block 0x340
    prev=[0x339], succ=[]
    =================================
    0x340: v340(0x0) = CONST 
    0x343: REVERT v340(0x0), v340(0x0)

    Begin block 0x344
    prev=[0x339], succ=[0x5b3]
    =================================
    0x345: v345(0x5fb1) = CONST 
    0x348: v348(0x5b3) = CONST 
    0x34b: JUMP v348(0x5b3)

    Begin block 0x5b3
    prev=[0x344], succ=[0x608, 0x60c]
    =================================
    0x5b4: v5b4(0x1) = CONST 
    0x5b6: v5b6 = SLOAD v5b4(0x1)
    0x5b7: v5b7(0x1) = CONST 
    0x5b9: v5b9(0xa0) = CONST 
    0x5bb: v5bb(0x2) = CONST 
    0x5bd: v5bd(0x10000000000000000000000000000000000000000) = EXP v5bb(0x2), v5b9(0xa0)
    0x5be: v5be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5bd(0x10000000000000000000000000000000000000000), v5b7(0x1)
    0x5bf: v5bf = AND v5be(0xffffffffffffffffffffffffffffffffffffffff), v5b6
    0x5c0: v5c0(0x70a08231) = CONST 
    0x5c5: v5c5 = ADDRESS 
    0x5c6: v5c6(0x0) = CONST 
    0x5c8: v5c8(0x40) = CONST 
    0x5ca: v5ca = MLOAD v5c8(0x40)
    0x5cb: v5cb(0x20) = CONST 
    0x5cd: v5cd = ADD v5cb(0x20), v5ca
    0x5ce: MSTORE v5cd, v5c6(0x0)
    0x5cf: v5cf(0x40) = CONST 
    0x5d1: v5d1 = MLOAD v5cf(0x40)
    0x5d2: v5d2(0xe0) = CONST 
    0x5d4: v5d4(0x2) = CONST 
    0x5d6: v5d6(0x100000000000000000000000000000000000000000000000000000000) = EXP v5d4(0x2), v5d2(0xe0)
    0x5d7: v5d7(0xffffffff) = CONST 
    0x5dd: v5dd(0x70a08231) = AND v5c0(0x70a08231), v5d7(0xffffffff)
    0x5de: v5de(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL v5dd(0x70a08231), v5d6(0x100000000000000000000000000000000000000000000000000000000)
    0x5e0: MSTORE v5d1, v5de(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x5e1: v5e1(0x1) = CONST 
    0x5e3: v5e3(0xa0) = CONST 
    0x5e5: v5e5(0x2) = CONST 
    0x5e7: v5e7(0x10000000000000000000000000000000000000000) = EXP v5e5(0x2), v5e3(0xa0)
    0x5e8: v5e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5e7(0x10000000000000000000000000000000000000000), v5e1(0x1)
    0x5eb: v5eb = AND v5c5, v5e8(0xffffffffffffffffffffffffffffffffffffffff)
    0x5ec: v5ec(0x4) = CONST 
    0x5ef: v5ef = ADD v5d1, v5ec(0x4)
    0x5f0: MSTORE v5ef, v5eb
    0x5f1: v5f1(0x24) = CONST 
    0x5f3: v5f3 = ADD v5f1(0x24), v5d1
    0x5f4: v5f4(0x20) = CONST 
    0x5f6: v5f6(0x40) = CONST 
    0x5f8: v5f8 = MLOAD v5f6(0x40)
    0x5fb: v5fb(0x24) = SUB v5f3, v5f8
    0x5fd: v5fd(0x0) = CONST 
    0x601: v601 = EXTCODESIZE v5bf
    0x602: v602 = ISZERO v601
    0x603: v603 = ISZERO v602
    0x604: v604(0x60c) = CONST 
    0x607: JUMPI v604(0x60c), v603

    Begin block 0x608
    prev=[0x5b3], succ=[]
    =================================
    0x608: v608(0x0) = CONST 
    0x60b: REVERT v608(0x0), v608(0x0)

    Begin block 0x60c
    prev=[0x5b3], succ=[0x619, 0x61d]
    =================================
    0x60d: v60d(0x2c6) = CONST 
    0x610: v610 = GAS 
    0x611: v611 = SUB v610, v60d(0x2c6)
    0x612: v612 = CALL v611, v5bf, v5fd(0x0), v5f8, v5fb(0x24), v5f8, v5f4(0x20)
    0x613: v613 = ISZERO v612
    0x614: v614 = ISZERO v613
    0x615: v615(0x61d) = CONST 
    0x618: JUMPI v615(0x61d), v614

    Begin block 0x619
    prev=[0x60c], succ=[]
    =================================
    0x619: v619(0x0) = CONST 
    0x61c: REVERT v619(0x0), v619(0x0)

    Begin block 0x61d
    prev=[0x60c], succ=[0x5fb1]
    =================================
    0x621: v621(0x40) = CONST 
    0x623: v623 = MLOAD v621(0x40)
    0x625: v625 = MLOAD v623
    0x626: v626(0x3) = CONST 
    0x628: SSTORE v626(0x3), v625
    0x62a: JUMP v345(0x5fb1)

    Begin block 0x5fb1
    prev=[0x61d], succ=[]
    =================================
    0x5fb2: STOP 

}

function totalDropTransactions()() public {
    Begin block 0x34c
    prev=[], succ=[0x353, 0x357]
    =================================
    0x34d: v34d = CALLVALUE 
    0x34e: v34e = ISZERO v34d
    0x34f: v34f(0x357) = CONST 
    0x352: JUMPI v34f(0x357), v34e

    Begin block 0x353
    prev=[0x34c], succ=[]
    =================================
    0x353: v353(0x0) = CONST 
    0x356: REVERT v353(0x0), v353(0x0)

    Begin block 0x357
    prev=[0x34c], succ=[0x62b]
    =================================
    0x358: v358(0x5fd2) = CONST 
    0x35b: v35b(0x62b) = CONST 
    0x35e: JUMP v35b(0x62b)

    Begin block 0x62b
    prev=[0x357], succ=[0x5fd2]
    =================================
    0x62c: v62c(0x8) = CONST 
    0x62e: v62e = SLOAD v62c(0x8)
    0x62f: v62f(0xff) = CONST 
    0x631: v631 = AND v62f(0xff), v62e
    0x633: JUMP v358(0x5fd2)

    Begin block 0x5fd2
    prev=[0x62b], succ=[]
    =================================
    0x5fd3: v5fd3(0x40) = CONST 
    0x5fd5: v5fd5 = MLOAD v5fd3(0x40)
    0x5fd6: v5fd6(0xff) = CONST 
    0x5fda: v5fda = AND v631, v5fd6(0xff)
    0x5fdc: MSTORE v5fd5, v5fda
    0x5fdd: v5fdd(0x20) = CONST 
    0x5fdf: v5fdf = ADD v5fdd(0x20), v5fd5
    0x5fe0: v5fe0(0x40) = CONST 
    0x5fe2: v5fe2 = MLOAD v5fe0(0x40)
    0x5fe5: v5fe5(0x20) = SUB v5fdf, v5fe2
    0x5fe7: RETURN v5fe2, v5fe5(0x20)

}

function kittensDroppedToTheWorld()() public {
    Begin block 0x35f
    prev=[], succ=[0x366, 0x36a]
    =================================
    0x360: v360 = CALLVALUE 
    0x361: v361 = ISZERO v360
    0x362: v362(0x36a) = CONST 
    0x365: JUMPI v362(0x36a), v361

    Begin block 0x366
    prev=[0x35f], succ=[]
    =================================
    0x366: v366(0x0) = CONST 
    0x369: REVERT v366(0x0), v366(0x0)

    Begin block 0x36a
    prev=[0x35f], succ=[0x634]
    =================================
    0x36b: v36b(0x6007) = CONST 
    0x36e: v36e(0x634) = CONST 
    0x371: JUMP v36e(0x634)

    Begin block 0x634
    prev=[0x36a], succ=[0x6007]
    =================================
    0x635: v635(0x2) = CONST 
    0x637: v637 = SLOAD v635(0x2)
    0x639: JUMP v36b(0x6007)

    Begin block 0x6007
    prev=[0x634], succ=[]
    =================================
    0x6008: v6008(0x40) = CONST 
    0x600a: v600a = MLOAD v6008(0x40)
    0x600d: MSTORE v600a, v637
    0x600e: v600e(0x20) = CONST 
    0x6010: v6010 = ADD v600e(0x20), v600a
    0x6011: v6011(0x40) = CONST 
    0x6013: v6013 = MLOAD v6011(0x40)
    0x6016: v6016(0x20) = SUB v6010, v6013
    0x6018: RETURN v6013, v6016(0x20)

}

function kittensRemainingToDrop()() public {
    Begin block 0x372
    prev=[], succ=[0x379, 0x37d]
    =================================
    0x373: v373 = CALLVALUE 
    0x374: v374 = ISZERO v373
    0x375: v375(0x37d) = CONST 
    0x378: JUMPI v375(0x37d), v374

    Begin block 0x379
    prev=[0x372], succ=[]
    =================================
    0x379: v379(0x0) = CONST 
    0x37c: REVERT v379(0x0), v379(0x0)

    Begin block 0x37d
    prev=[0x372], succ=[0x63a]
    =================================
    0x37e: v37e(0x6038) = CONST 
    0x381: v381(0x63a) = CONST 
    0x384: JUMP v381(0x63a)

    Begin block 0x63a
    prev=[0x37d], succ=[0x6038]
    =================================
    0x63b: v63b(0x3) = CONST 
    0x63d: v63d = SLOAD v63b(0x3)
    0x63f: JUMP v37e(0x6038)

    Begin block 0x6038
    prev=[0x63a], succ=[]
    =================================
    0x6039: v6039(0x40) = CONST 
    0x603b: v603b = MLOAD v6039(0x40)
    0x603e: MSTORE v603b, v63d
    0x603f: v603f(0x20) = CONST 
    0x6041: v6041 = ADD v603f(0x20), v603b
    0x6042: v6042(0x40) = CONST 
    0x6044: v6044 = MLOAD v6042(0x40)
    0x6047: v6047(0x20) = SUB v6041, v6044
    0x6049: RETURN v6044, v6047(0x20)

}

function setDropNumber(uint8)() public {
    Begin block 0x385
    prev=[], succ=[0x38c, 0x390]
    =================================
    0x386: v386 = CALLVALUE 
    0x387: v387 = ISZERO v386
    0x388: v388(0x390) = CONST 
    0x38b: JUMPI v388(0x390), v387

    Begin block 0x38c
    prev=[0x385], succ=[]
    =================================
    0x38c: v38c(0x0) = CONST 
    0x38f: REVERT v38c(0x0), v38c(0x0)

    Begin block 0x390
    prev=[0x385], succ=[0x640]
    =================================
    0x391: v391(0x6069) = CONST 
    0x394: v394(0xff) = CONST 
    0x396: v396(0x4) = CONST 
    0x398: v398 = CALLDATALOAD v396(0x4)
    0x399: v399 = AND v398, v394(0xff)
    0x39a: v39a(0x640) = CONST 
    0x39d: JUMP v39a(0x640)

    Begin block 0x640
    prev=[0x390], succ=[0x657, 0x65b]
    =================================
    0x641: v641(0x0) = CONST 
    0x643: v643 = SLOAD v641(0x0)
    0x644: v644 = CALLER 
    0x645: v645(0x1) = CONST 
    0x647: v647(0xa0) = CONST 
    0x649: v649(0x2) = CONST 
    0x64b: v64b(0x10000000000000000000000000000000000000000) = EXP v649(0x2), v647(0xa0)
    0x64c: v64c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64b(0x10000000000000000000000000000000000000000), v645(0x1)
    0x64f: v64f = AND v64c(0xffffffffffffffffffffffffffffffffffffffff), v644
    0x651: v651 = AND v643, v64c(0xffffffffffffffffffffffffffffffffffffffff)
    0x652: v652 = EQ v651, v64f
    0x653: v653(0x65b) = CONST 
    0x656: JUMPI v653(0x65b), v652

    Begin block 0x657
    prev=[0x640], succ=[]
    =================================
    0x657: v657(0x0) = CONST 
    0x65a: REVERT v657(0x0), v657(0x0)

    Begin block 0x65b
    prev=[0x640], succ=[0x6d8, 0x6dc]
    =================================
    0x65c: v65c(0x1) = CONST 
    0x65f: v65f = SLOAD v65c(0x1)
    0x660: v660(0xff0000000000000000000000000000000000000000) = CONST 
    0x676: v676(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v660(0xff0000000000000000000000000000000000000000)
    0x677: v677 = AND v676(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v65f
    0x678: v678(0xa0) = CONST 
    0x67a: v67a(0x2) = CONST 
    0x67c: v67c(0x10000000000000000000000000000000000000000) = EXP v67a(0x2), v678(0xa0)
    0x67d: v67d(0xff) = CONST 
    0x680: v680 = AND v399, v67d(0xff)
    0x681: v681 = MUL v680, v67c(0x10000000000000000000000000000000000000000)
    0x682: v682 = OR v681, v677
    0x686: SSTORE v65c(0x1), v682
    0x687: v687(0x1) = CONST 
    0x689: v689(0xa0) = CONST 
    0x68b: v68b(0x2) = CONST 
    0x68d: v68d(0x10000000000000000000000000000000000000000) = EXP v68b(0x2), v689(0xa0)
    0x68e: v68e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v68d(0x10000000000000000000000000000000000000000), v687(0x1)
    0x68f: v68f = AND v68e(0xffffffffffffffffffffffffffffffffffffffff), v682
    0x690: v690(0x70a08231) = CONST 
    0x695: v695 = ADDRESS 
    0x696: v696(0x0) = CONST 
    0x698: v698(0x40) = CONST 
    0x69a: v69a = MLOAD v698(0x40)
    0x69b: v69b(0x20) = CONST 
    0x69d: v69d = ADD v69b(0x20), v69a
    0x69e: MSTORE v69d, v696(0x0)
    0x69f: v69f(0x40) = CONST 
    0x6a1: v6a1 = MLOAD v69f(0x40)
    0x6a2: v6a2(0xe0) = CONST 
    0x6a4: v6a4(0x2) = CONST 
    0x6a6: v6a6(0x100000000000000000000000000000000000000000000000000000000) = EXP v6a4(0x2), v6a2(0xe0)
    0x6a7: v6a7(0xffffffff) = CONST 
    0x6ad: v6ad(0x70a08231) = AND v690(0x70a08231), v6a7(0xffffffff)
    0x6ae: v6ae(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL v6ad(0x70a08231), v6a6(0x100000000000000000000000000000000000000000000000000000000)
    0x6b0: MSTORE v6a1, v6ae(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x6b1: v6b1(0x1) = CONST 
    0x6b3: v6b3(0xa0) = CONST 
    0x6b5: v6b5(0x2) = CONST 
    0x6b7: v6b7(0x10000000000000000000000000000000000000000) = EXP v6b5(0x2), v6b3(0xa0)
    0x6b8: v6b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b7(0x10000000000000000000000000000000000000000), v6b1(0x1)
    0x6bb: v6bb = AND v695, v6b8(0xffffffffffffffffffffffffffffffffffffffff)
    0x6bc: v6bc(0x4) = CONST 
    0x6bf: v6bf = ADD v6a1, v6bc(0x4)
    0x6c0: MSTORE v6bf, v6bb
    0x6c1: v6c1(0x24) = CONST 
    0x6c3: v6c3 = ADD v6c1(0x24), v6a1
    0x6c4: v6c4(0x20) = CONST 
    0x6c6: v6c6(0x40) = CONST 
    0x6c8: v6c8 = MLOAD v6c6(0x40)
    0x6cb: v6cb(0x24) = SUB v6c3, v6c8
    0x6cd: v6cd(0x0) = CONST 
    0x6d1: v6d1 = EXTCODESIZE v68f
    0x6d2: v6d2 = ISZERO v6d1
    0x6d3: v6d3 = ISZERO v6d2
    0x6d4: v6d4(0x6dc) = CONST 
    0x6d7: JUMPI v6d4(0x6dc), v6d3

    Begin block 0x6d8
    prev=[0x65b], succ=[]
    =================================
    0x6d8: v6d8(0x0) = CONST 
    0x6db: REVERT v6d8(0x0), v6d8(0x0)

    Begin block 0x6dc
    prev=[0x65b], succ=[0x6e9, 0x6ed]
    =================================
    0x6dd: v6dd(0x2c6) = CONST 
    0x6e0: v6e0 = GAS 
    0x6e1: v6e1 = SUB v6e0, v6dd(0x2c6)
    0x6e2: v6e2 = CALL v6e1, v68f, v6cd(0x0), v6c8, v6cb(0x24), v6c8, v6c4(0x20)
    0x6e3: v6e3 = ISZERO v6e2
    0x6e4: v6e4 = ISZERO v6e3
    0x6e5: v6e5(0x6ed) = CONST 
    0x6e8: JUMPI v6e5(0x6ed), v6e4

    Begin block 0x6e9
    prev=[0x6dc], succ=[]
    =================================
    0x6e9: v6e9(0x0) = CONST 
    0x6ec: REVERT v6e9(0x0), v6e9(0x0)

    Begin block 0x6ed
    prev=[0x6dc], succ=[0x6069]
    =================================
    0x6f1: v6f1(0x40) = CONST 
    0x6f3: v6f3 = MLOAD v6f1(0x40)
    0x6f5: v6f5 = MLOAD v6f3
    0x6f6: v6f6(0x3) = CONST 
    0x6f8: SSTORE v6f6(0x3), v6f5
    0x6fb: JUMP v391(0x6069)

    Begin block 0x6069
    prev=[0x6ed], succ=[]
    =================================
    0x606a: STOP 

}

function withdrawAll()() public {
    Begin block 0x39e
    prev=[], succ=[0x3a5, 0x3a9]
    =================================
    0x39f: v39f = CALLVALUE 
    0x3a0: v3a0 = ISZERO v39f
    0x3a1: v3a1(0x3a9) = CONST 
    0x3a4: JUMPI v3a1(0x3a9), v3a0

    Begin block 0x3a5
    prev=[0x39e], succ=[]
    =================================
    0x3a5: v3a5(0x0) = CONST 
    0x3a8: REVERT v3a5(0x0), v3a5(0x0)

    Begin block 0x3a9
    prev=[0x39e], succ=[0x6fcB0x3a9]
    =================================
    0x3aa: v3aa(0x608a) = CONST 
    0x3ad: v3ad(0x6fc) = CONST 
    0x3b0: JUMP v3ad(0x6fc)

    Begin block 0x6fcB0x3a9
    prev=[0x3a9], succ=[0x713B0x3a9, 0x717B0x3a9]
    =================================
    0x6fdS0x3a9: v6fdV3a9(0x0) = CONST 
    0x6ffS0x3a9: v6ffV3a9 = SLOAD v6fdV3a9(0x0)
    0x700S0x3a9: v700V3a9 = CALLER 
    0x701S0x3a9: v701V3a9(0x1) = CONST 
    0x703S0x3a9: v703V3a9(0xa0) = CONST 
    0x705S0x3a9: v705V3a9(0x2) = CONST 
    0x707S0x3a9: v707V3a9(0x10000000000000000000000000000000000000000) = EXP v705V3a9(0x2), v703V3a9(0xa0)
    0x708S0x3a9: v708V3a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v707V3a9(0x10000000000000000000000000000000000000000), v701V3a9(0x1)
    0x70bS0x3a9: v70bV3a9 = AND v708V3a9(0xffffffffffffffffffffffffffffffffffffffff), v700V3a9
    0x70dS0x3a9: v70dV3a9 = AND v6ffV3a9, v708V3a9(0xffffffffffffffffffffffffffffffffffffffff)
    0x70eS0x3a9: v70eV3a9 = EQ v70dV3a9, v70bV3a9
    0x70fS0x3a9: v70fV3a9(0x717) = CONST 
    0x712S0x3a9: JUMPI v70fV3a9(0x717), v70eV3a9

    Begin block 0x713B0x3a9
    prev=[0x6fcB0x3a9], succ=[]
    =================================
    0x713S0x3a9: v713V3a9(0x0) = CONST 
    0x716S0x3a9: REVERT v713V3a9(0x0), v713V3a9(0x0)

    Begin block 0x717B0x3a9
    prev=[0x6fcB0x3a9], succ=[0x74cB0x3a9, 0x750B0x3a9]
    =================================
    0x718S0x3a9: v718V3a9(0x0) = CONST 
    0x71aS0x3a9: v71aV3a9 = SLOAD v718V3a9(0x0)
    0x71bS0x3a9: v71bV3a9(0x1) = CONST 
    0x71dS0x3a9: v71dV3a9(0xa0) = CONST 
    0x71fS0x3a9: v71fV3a9(0x2) = CONST 
    0x721S0x3a9: v721V3a9(0x10000000000000000000000000000000000000000) = EXP v71fV3a9(0x2), v71dV3a9(0xa0)
    0x722S0x3a9: v722V3a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v721V3a9(0x10000000000000000000000000000000000000000), v71bV3a9(0x1)
    0x725S0x3a9: v725V3a9 = AND v722V3a9(0xffffffffffffffffffffffffffffffffffffffff), v71aV3a9
    0x727S0x3a9: v727V3a9 = ADDRESS 
    0x728S0x3a9: v728V3a9 = AND v727V3a9, v722V3a9(0xffffffffffffffffffffffffffffffffffffffff)
    0x729S0x3a9: v729V3a9 = BALANCE v728V3a9
    0x72bS0x3a9: v72bV3a9 = ISZERO v729V3a9
    0x72cS0x3a9: v72cV3a9(0x8fc) = CONST 
    0x72fS0x3a9: v72fV3a9 = MUL v72cV3a9(0x8fc), v72bV3a9
    0x731S0x3a9: v731V3a9(0x40) = CONST 
    0x733S0x3a9: v733V3a9 = MLOAD v731V3a9(0x40)
    0x734S0x3a9: v734V3a9(0x0) = CONST 
    0x736S0x3a9: v736V3a9(0x40) = CONST 
    0x738S0x3a9: v738V3a9 = MLOAD v736V3a9(0x40)
    0x73bS0x3a9: v73bV3a9(0x0) = SUB v733V3a9, v738V3a9
    0x740S0x3a9: v740V3a9 = CALL v72fV3a9, v725V3a9, v729V3a9, v738V3a9, v73bV3a9(0x0), v738V3a9, v734V3a9(0x0)
    0x746S0x3a9: v746V3a9 = ISZERO v740V3a9
    0x747S0x3a9: v747V3a9 = ISZERO v746V3a9
    0x748S0x3a9: v748V3a9(0x750) = CONST 
    0x74bS0x3a9: JUMPI v748V3a9(0x750), v747V3a9

    Begin block 0x74cB0x3a9
    prev=[0x717B0x3a9], succ=[]
    =================================
    0x74cS0x3a9: v74cV3a9(0x0) = CONST 
    0x74fS0x3a9: REVERT v74cV3a9(0x0), v74cV3a9(0x0)

    Begin block 0x750B0x3a9
    prev=[0x717B0x3a9], succ=[0x608a]
    =================================
    0x751S0x3a9: JUMP v3aa(0x608a)

    Begin block 0x608a
    prev=[0x750B0x3a9], succ=[]
    =================================
    0x608b: STOP 

}

function owner()() public {
    Begin block 0x3b1
    prev=[], succ=[0x3b8, 0x3bc]
    =================================
    0x3b2: v3b2 = CALLVALUE 
    0x3b3: v3b3 = ISZERO v3b2
    0x3b4: v3b4(0x3bc) = CONST 
    0x3b7: JUMPI v3b4(0x3bc), v3b3

    Begin block 0x3b8
    prev=[0x3b1], succ=[]
    =================================
    0x3b8: v3b8(0x0) = CONST 
    0x3bb: REVERT v3b8(0x0), v3b8(0x0)

    Begin block 0x3bc
    prev=[0x3b1], succ=[0x752]
    =================================
    0x3bd: v3bd(0x60ab) = CONST 
    0x3c0: v3c0(0x752) = CONST 
    0x3c3: JUMP v3c0(0x752)

    Begin block 0x752
    prev=[0x3bc], succ=[0x60ab]
    =================================
    0x753: v753(0x0) = CONST 
    0x755: v755 = SLOAD v753(0x0)
    0x756: v756(0x1) = CONST 
    0x758: v758(0xa0) = CONST 
    0x75a: v75a(0x2) = CONST 
    0x75c: v75c(0x10000000000000000000000000000000000000000) = EXP v75a(0x2), v758(0xa0)
    0x75d: v75d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75c(0x10000000000000000000000000000000000000000), v756(0x1)
    0x75e: v75e = AND v75d(0xffffffffffffffffffffffffffffffffffffffff), v755
    0x760: JUMP v3bd(0x60ab)

    Begin block 0x60ab
    prev=[0x752], succ=[]
    =================================
    0x60ac: v60ac(0x40) = CONST 
    0x60ae: v60ae = MLOAD v60ac(0x40)
    0x60af: v60af(0x1) = CONST 
    0x60b1: v60b1(0xa0) = CONST 
    0x60b3: v60b3(0x2) = CONST 
    0x60b5: v60b5(0x10000000000000000000000000000000000000000) = EXP v60b3(0x2), v60b1(0xa0)
    0x60b6: v60b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v60b5(0x10000000000000000000000000000000000000000), v60af(0x1)
    0x60b9: v60b9 = AND v75e, v60b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x60bb: MSTORE v60ae, v60b9
    0x60bc: v60bc(0x20) = CONST 
    0x60be: v60be = ADD v60bc(0x20), v60ae
    0x60bf: v60bf(0x40) = CONST 
    0x60c1: v60c1 = MLOAD v60bf(0x40)
    0x60c4: v60c4(0x20) = SUB v60be, v60c1
    0x60c6: RETURN v60c1, v60c4(0x20)

}

function holderAmount()() public {
    Begin block 0x3e0
    prev=[], succ=[0x3e7, 0x3eb]
    =================================
    0x3e1: v3e1 = CALLVALUE 
    0x3e2: v3e2 = ISZERO v3e1
    0x3e3: v3e3(0x3eb) = CONST 
    0x3e6: JUMPI v3e3(0x3eb), v3e2

    Begin block 0x3e7
    prev=[0x3e0], succ=[]
    =================================
    0x3e7: v3e7(0x0) = CONST 
    0x3ea: REVERT v3e7(0x0), v3e7(0x0)

    Begin block 0x3eb
    prev=[0x3e0], succ=[0x761]
    =================================
    0x3ec: v3ec(0x60e6) = CONST 
    0x3ef: v3ef(0x761) = CONST 
    0x3f2: JUMP v3ef(0x761)

    Begin block 0x761
    prev=[0x3eb], succ=[0x60e6]
    =================================
    0x762: v762(0x4) = CONST 
    0x764: v764 = SLOAD v762(0x4)
    0x766: JUMP v3ec(0x60e6)

    Begin block 0x60e6
    prev=[0x761], succ=[]
    =================================
    0x60e7: v60e7(0x40) = CONST 
    0x60e9: v60e9 = MLOAD v60e7(0x40)
    0x60ec: MSTORE v60e9, v764
    0x60ed: v60ed(0x20) = CONST 
    0x60ef: v60ef = ADD v60ed(0x20), v60e9
    0x60f0: v60f0(0x40) = CONST 
    0x60f2: v60f2 = MLOAD v60f0(0x40)
    0x60f5: v60f5(0x20) = SUB v60ef, v60f2
    0x60f7: RETURN v60f2, v60f5(0x20)

}

function holderReward()() public {
    Begin block 0x3f3
    prev=[], succ=[0x3fa, 0x3fe]
    =================================
    0x3f4: v3f4 = CALLVALUE 
    0x3f5: v3f5 = ISZERO v3f4
    0x3f6: v3f6(0x3fe) = CONST 
    0x3f9: JUMPI v3f6(0x3fe), v3f5

    Begin block 0x3fa
    prev=[0x3f3], succ=[]
    =================================
    0x3fa: v3fa(0x0) = CONST 
    0x3fd: REVERT v3fa(0x0), v3fa(0x0)

    Begin block 0x3fe
    prev=[0x3f3], succ=[0x767]
    =================================
    0x3ff: v3ff(0x6117) = CONST 
    0x402: v402(0x767) = CONST 
    0x405: JUMP v402(0x767)

    Begin block 0x767
    prev=[0x3fe], succ=[0x6117]
    =================================
    0x768: v768(0x7) = CONST 
    0x76a: v76a = SLOAD v768(0x7)
    0x76c: JUMP v3ff(0x6117)

    Begin block 0x6117
    prev=[0x767], succ=[]
    =================================
    0x6118: v6118(0x40) = CONST 
    0x611a: v611a = MLOAD v6118(0x40)
    0x611d: MSTORE v611a, v76a
    0x611e: v611e(0x20) = CONST 
    0x6120: v6120 = ADD v611e(0x20), v611a
    0x6121: v6121(0x40) = CONST 
    0x6123: v6123 = MLOAD v6121(0x40)
    0x6126: v6126(0x20) = SUB v6120, v6123
    0x6128: RETURN v6123, v6126(0x20)

}

function setHolderAmount(uint256)() public {
    Begin block 0x406
    prev=[], succ=[0x40d, 0x411]
    =================================
    0x407: v407 = CALLVALUE 
    0x408: v408 = ISZERO v407
    0x409: v409(0x411) = CONST 
    0x40c: JUMPI v409(0x411), v408

    Begin block 0x40d
    prev=[0x406], succ=[]
    =================================
    0x40d: v40d(0x0) = CONST 
    0x410: REVERT v40d(0x0), v40d(0x0)

    Begin block 0x411
    prev=[0x406], succ=[0x76d]
    =================================
    0x412: v412(0x6148) = CONST 
    0x415: v415(0x4) = CONST 
    0x417: v417 = CALLDATALOAD v415(0x4)
    0x418: v418(0x76d) = CONST 
    0x41b: JUMP v418(0x76d)

    Begin block 0x76d
    prev=[0x411], succ=[0x784, 0x788]
    =================================
    0x76e: v76e(0x0) = CONST 
    0x770: v770 = SLOAD v76e(0x0)
    0x771: v771 = CALLER 
    0x772: v772(0x1) = CONST 
    0x774: v774(0xa0) = CONST 
    0x776: v776(0x2) = CONST 
    0x778: v778(0x10000000000000000000000000000000000000000) = EXP v776(0x2), v774(0xa0)
    0x779: v779(0xffffffffffffffffffffffffffffffffffffffff) = SUB v778(0x10000000000000000000000000000000000000000), v772(0x1)
    0x77c: v77c = AND v779(0xffffffffffffffffffffffffffffffffffffffff), v771
    0x77e: v77e = AND v770, v779(0xffffffffffffffffffffffffffffffffffffffff)
    0x77f: v77f = EQ v77e, v77c
    0x780: v780(0x788) = CONST 
    0x783: JUMPI v780(0x788), v77f

    Begin block 0x784
    prev=[0x76d], succ=[]
    =================================
    0x784: v784(0x0) = CONST 
    0x787: REVERT v784(0x0), v784(0x0)

    Begin block 0x788
    prev=[0x76d], succ=[0x6148]
    =================================
    0x789: v789(0x4) = CONST 
    0x78b: SSTORE v789(0x4), v417
    0x78c: JUMP v412(0x6148)

    Begin block 0x6148
    prev=[0x788], succ=[]
    =================================
    0x6149: STOP 

}

function transferOwnership(address)() public {
    Begin block 0x41c
    prev=[], succ=[0x423, 0x427]
    =================================
    0x41d: v41d = CALLVALUE 
    0x41e: v41e = ISZERO v41d
    0x41f: v41f(0x427) = CONST 
    0x422: JUMPI v41f(0x427), v41e

    Begin block 0x423
    prev=[0x41c], succ=[]
    =================================
    0x423: v423(0x0) = CONST 
    0x426: REVERT v423(0x0), v423(0x0)

    Begin block 0x427
    prev=[0x41c], succ=[0x78d]
    =================================
    0x428: v428(0x6169) = CONST 
    0x42b: v42b(0x1) = CONST 
    0x42d: v42d(0xa0) = CONST 
    0x42f: v42f(0x2) = CONST 
    0x431: v431(0x10000000000000000000000000000000000000000) = EXP v42f(0x2), v42d(0xa0)
    0x432: v432(0xffffffffffffffffffffffffffffffffffffffff) = SUB v431(0x10000000000000000000000000000000000000000), v42b(0x1)
    0x433: v433(0x4) = CONST 
    0x435: v435 = CALLDATALOAD v433(0x4)
    0x436: v436 = AND v435, v432(0xffffffffffffffffffffffffffffffffffffffff)
    0x437: v437(0x78d) = CONST 
    0x43a: JUMP v437(0x78d)

    Begin block 0x78d
    prev=[0x427], succ=[0x7a4, 0x7a8]
    =================================
    0x78e: v78e(0x0) = CONST 
    0x790: v790 = SLOAD v78e(0x0)
    0x791: v791 = CALLER 
    0x792: v792(0x1) = CONST 
    0x794: v794(0xa0) = CONST 
    0x796: v796(0x2) = CONST 
    0x798: v798(0x10000000000000000000000000000000000000000) = EXP v796(0x2), v794(0xa0)
    0x799: v799(0xffffffffffffffffffffffffffffffffffffffff) = SUB v798(0x10000000000000000000000000000000000000000), v792(0x1)
    0x79c: v79c = AND v799(0xffffffffffffffffffffffffffffffffffffffff), v791
    0x79e: v79e = AND v790, v799(0xffffffffffffffffffffffffffffffffffffffff)
    0x79f: v79f = EQ v79e, v79c
    0x7a0: v7a0(0x7a8) = CONST 
    0x7a3: JUMPI v7a0(0x7a8), v79f

    Begin block 0x7a4
    prev=[0x78d], succ=[]
    =================================
    0x7a4: v7a4(0x0) = CONST 
    0x7a7: REVERT v7a4(0x0), v7a4(0x0)

    Begin block 0x7a8
    prev=[0x78d], succ=[0x7b9, 0x7bd]
    =================================
    0x7a9: v7a9(0x1) = CONST 
    0x7ab: v7ab(0xa0) = CONST 
    0x7ad: v7ad(0x2) = CONST 
    0x7af: v7af(0x10000000000000000000000000000000000000000) = EXP v7ad(0x2), v7ab(0xa0)
    0x7b0: v7b0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7af(0x10000000000000000000000000000000000000000), v7a9(0x1)
    0x7b2: v7b2 = AND v436, v7b0(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b3: v7b3 = ISZERO v7b2
    0x7b4: v7b4 = ISZERO v7b3
    0x7b5: v7b5(0x7bd) = CONST 
    0x7b8: JUMPI v7b5(0x7bd), v7b4

    Begin block 0x7b9
    prev=[0x7a8], succ=[]
    =================================
    0x7b9: v7b9(0x0) = CONST 
    0x7bc: REVERT v7b9(0x0), v7b9(0x0)

    Begin block 0x7bd
    prev=[0x7a8], succ=[0x6169]
    =================================
    0x7be: v7be(0x0) = CONST 
    0x7c0: v7c0 = SLOAD v7be(0x0)
    0x7c1: v7c1(0x1) = CONST 
    0x7c3: v7c3(0xa0) = CONST 
    0x7c5: v7c5(0x2) = CONST 
    0x7c7: v7c7(0x10000000000000000000000000000000000000000) = EXP v7c5(0x2), v7c3(0xa0)
    0x7c8: v7c8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c7(0x10000000000000000000000000000000000000000), v7c1(0x1)
    0x7cb: v7cb = AND v436, v7c8(0xffffffffffffffffffffffffffffffffffffffff)
    0x7cd: v7cd = AND v7c0, v7c8(0xffffffffffffffffffffffffffffffffffffffff)
    0x7ce: v7ce(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x7ef: v7ef(0x40) = CONST 
    0x7f1: v7f1 = MLOAD v7ef(0x40)
    0x7f2: v7f2(0x40) = CONST 
    0x7f4: v7f4 = MLOAD v7f2(0x40)
    0x7f7: v7f7(0x0) = SUB v7f1, v7f4
    0x7f9: LOG3 v7f4, v7f7(0x0), v7ce(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v7cd, v7cb
    0x7fa: v7fa(0x0) = CONST 
    0x7fd: v7fd = SLOAD v7fa(0x0)
    0x7fe: v7fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x813: v813(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v7fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x814: v814 = AND v813(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v7fd
    0x815: v815(0x1) = CONST 
    0x817: v817(0xa0) = CONST 
    0x819: v819(0x2) = CONST 
    0x81b: v81b(0x10000000000000000000000000000000000000000) = EXP v819(0x2), v817(0xa0)
    0x81c: v81c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v81b(0x10000000000000000000000000000000000000000), v815(0x1)
    0x820: v820 = AND v81c(0xffffffffffffffffffffffffffffffffffffffff), v436
    0x824: v824 = OR v820, v814
    0x826: SSTORE v7fa(0x0), v824
    0x827: JUMP v428(0x6169)

    Begin block 0x6169
    prev=[0x7bd], succ=[]
    =================================
    0x616a: STOP 

}

function setRewards(uint256,uint256,uint256)() public {
    Begin block 0x43b
    prev=[], succ=[0x442, 0x446]
    =================================
    0x43c: v43c = CALLVALUE 
    0x43d: v43d = ISZERO v43c
    0x43e: v43e(0x446) = CONST 
    0x441: JUMPI v43e(0x446), v43d

    Begin block 0x442
    prev=[0x43b], succ=[]
    =================================
    0x442: v442(0x0) = CONST 
    0x445: REVERT v442(0x0), v442(0x0)

    Begin block 0x446
    prev=[0x43b], succ=[0x828]
    =================================
    0x447: v447(0x618a) = CONST 
    0x44a: v44a(0x4) = CONST 
    0x44c: v44c = CALLDATALOAD v44a(0x4)
    0x44d: v44d(0x24) = CONST 
    0x44f: v44f = CALLDATALOAD v44d(0x24)
    0x450: v450(0x44) = CONST 
    0x452: v452 = CALLDATALOAD v450(0x44)
    0x453: v453(0x828) = CONST 
    0x456: JUMP v453(0x828)

    Begin block 0x828
    prev=[0x446], succ=[0x83f, 0x843]
    =================================
    0x829: v829(0x0) = CONST 
    0x82b: v82b = SLOAD v829(0x0)
    0x82c: v82c = CALLER 
    0x82d: v82d(0x1) = CONST 
    0x82f: v82f(0xa0) = CONST 
    0x831: v831(0x2) = CONST 
    0x833: v833(0x10000000000000000000000000000000000000000) = EXP v831(0x2), v82f(0xa0)
    0x834: v834(0xffffffffffffffffffffffffffffffffffffffff) = SUB v833(0x10000000000000000000000000000000000000000), v82d(0x1)
    0x837: v837 = AND v834(0xffffffffffffffffffffffffffffffffffffffff), v82c
    0x839: v839 = AND v82b, v834(0xffffffffffffffffffffffffffffffffffffffff)
    0x83a: v83a = EQ v839, v837
    0x83b: v83b(0x843) = CONST 
    0x83e: JUMPI v83b(0x843), v83a

    Begin block 0x83f
    prev=[0x828], succ=[]
    =================================
    0x83f: v83f(0x0) = CONST 
    0x842: REVERT v83f(0x0), v83f(0x0)

    Begin block 0x843
    prev=[0x828], succ=[0x618a]
    =================================
    0x844: v844(0x5) = CONST 
    0x849: SSTORE v844(0x5), v44c
    0x84a: v84a(0x6) = CONST 
    0x84c: SSTORE v84a(0x6), v44f
    0x84d: v84d(0x7) = CONST 
    0x84f: SSTORE v84d(0x7), v452
    0x850: JUMP v447(0x618a)

    Begin block 0x618a
    prev=[0x843], succ=[]
    =================================
    0x618b: STOP 

}

function kittenContract()() public {
    Begin block 0x457
    prev=[], succ=[0x45e, 0x462]
    =================================
    0x458: v458 = CALLVALUE 
    0x459: v459 = ISZERO v458
    0x45a: v45a(0x462) = CONST 
    0x45d: JUMPI v45a(0x462), v459

    Begin block 0x45e
    prev=[0x457], succ=[]
    =================================
    0x45e: v45e(0x0) = CONST 
    0x461: REVERT v45e(0x0), v45e(0x0)

    Begin block 0x462
    prev=[0x457], succ=[0x851]
    =================================
    0x463: v463(0x61ab) = CONST 
    0x466: v466(0x851) = CONST 
    0x469: JUMP v466(0x851)

    Begin block 0x851
    prev=[0x462], succ=[0x61ab]
    =================================
    0x852: v852(0x1) = CONST 
    0x854: v854 = SLOAD v852(0x1)
    0x855: v855(0x1) = CONST 
    0x857: v857(0xa0) = CONST 
    0x859: v859(0x2) = CONST 
    0x85b: v85b(0x10000000000000000000000000000000000000000) = EXP v859(0x2), v857(0xa0)
    0x85c: v85c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v85b(0x10000000000000000000000000000000000000000), v855(0x1)
    0x85d: v85d = AND v85c(0xffffffffffffffffffffffffffffffffffffffff), v854
    0x85f: JUMP v463(0x61ab)

    Begin block 0x61ab
    prev=[0x851], succ=[]
    =================================
    0x61ac: v61ac(0x40) = CONST 
    0x61ae: v61ae = MLOAD v61ac(0x40)
    0x61af: v61af(0x1) = CONST 
    0x61b1: v61b1(0xa0) = CONST 
    0x61b3: v61b3(0x2) = CONST 
    0x61b5: v61b5(0x10000000000000000000000000000000000000000) = EXP v61b3(0x2), v61b1(0xa0)
    0x61b6: v61b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v61b5(0x10000000000000000000000000000000000000000), v61af(0x1)
    0x61b9: v61b9 = AND v85d, v61b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x61bb: MSTORE v61ae, v61b9
    0x61bc: v61bc(0x20) = CONST 
    0x61be: v61be = ADD v61bc(0x20), v61ae
    0x61bf: v61bf(0x40) = CONST 
    0x61c1: v61c1 = MLOAD v61bf(0x40)
    0x61c4: v61c4(0x20) = SUB v61be, v61c1
    0x61c6: RETURN v61c1, v61c4(0x20)

}

function fallback()() public {
    Begin block 0xe2
    prev=[], succ=[0x11e, 0x116]
    =================================
    0xe3: ve3(0x1) = CONST 
    0xe5: ve5 = SLOAD ve3(0x1)
    0xe6: ve6(0x1) = CONST 
    0xe8: ve8(0xa0) = CONST 
    0xea: vea(0x2) = CONST 
    0xec: vec(0x10000000000000000000000000000000000000000) = EXP vea(0x2), ve8(0xa0)
    0xed: ved(0xffffffffffffffffffffffffffffffffffffffff) = SUB vec(0x10000000000000000000000000000000000000000), ve6(0x1)
    0xee: vee = CALLER 
    0xef: vef = AND vee, ved(0xffffffffffffffffffffffffffffffffffffffff)
    0xf0: vf0(0x0) = CONST 
    0xf4: MSTORE vf0(0x0), vef
    0xf5: vf5(0x9) = CONST 
    0xf7: vf7(0x20) = CONST 
    0xf9: MSTORE vf7(0x20), vf5(0x9)
    0xfa: vfa(0x40) = CONST 
    0xfd: vfd = SHA3 vf0(0x0), vfa(0x40)
    0xfe: vfe = SLOAD vfd
    0x101: v101(0xff) = CONST 
    0x103: v103(0xa0) = CONST 
    0x105: v105(0x2) = CONST 
    0x107: v107(0x10000000000000000000000000000000000000000) = EXP v105(0x2), v103(0xa0)
    0x10a: v10a = DIV ve5, v107(0x10000000000000000000000000000000000000000)
    0x10c: v10c = AND v101(0xff), v10a
    0x10e: v10e = AND vfe, v101(0xff)
    0x10f: v10f = LT v10e, v10c
    0x111: v111 = ISZERO v10f
    0x112: v112(0x11e) = CONST 
    0x115: JUMPI v112(0x11e), v111

    Begin block 0x11e
    prev=[0xe2, 0x116], succ=[0x125, 0x129]
    =================================
    0x11e_0x0: v11e_0 = PHI v10f, v11d
    0x11f: v11f = ISZERO v11e_0
    0x120: v120 = ISZERO v11f
    0x121: v121(0x129) = CONST 
    0x124: JUMPI v121(0x129), v120

    Begin block 0x125
    prev=[0x11e], succ=[]
    =================================
    0x125: v125(0x0) = CONST 
    0x128: REVERT v125(0x0), v125(0x0)

    Begin block 0x129
    prev=[0x11e], succ=[0x137, 0x13b]
    =================================
    0x12b: v12b(0x5) = CONST 
    0x12d: v12d = SLOAD v12b(0x5)
    0x12e: v12e(0x0) = CONST 
    0x130: v130 = CALLVALUE 
    0x131: v131 = GT v130, v12e(0x0)
    0x132: v132 = ISZERO v131
    0x133: v133(0x13b) = CONST 
    0x136: JUMPI v133(0x13b), v132

    Begin block 0x137
    prev=[0x129], succ=[0x13b]
    =================================
    0x137: v137(0x6) = CONST 
    0x139: v139 = SLOAD v137(0x6)
    0x13a: v13a = ADD v139, v12d
    0x1b32: v1b32(0x13b) = CONST 
    0x1b52: JUMP v1b32(0x13b)

    Begin block 0x13b
    prev=[0x137, 0x129], succ=[0x193, 0x197]
    =================================
    0x13c: v13c(0x4) = CONST 
    0x13e: v13e = SLOAD v13c(0x4)
    0x13f: v13f(0x1) = CONST 
    0x141: v141 = SLOAD v13f(0x1)
    0x142: v142(0x1) = CONST 
    0x144: v144(0xa0) = CONST 
    0x146: v146(0x2) = CONST 
    0x148: v148(0x10000000000000000000000000000000000000000) = EXP v146(0x2), v144(0xa0)
    0x149: v149(0xffffffffffffffffffffffffffffffffffffffff) = SUB v148(0x10000000000000000000000000000000000000000), v142(0x1)
    0x14a: v14a = AND v149(0xffffffffffffffffffffffffffffffffffffffff), v141
    0x14b: v14b(0x70a08231) = CONST 
    0x150: v150 = CALLER 
    0x151: v151(0x0) = CONST 
    0x153: v153(0x40) = CONST 
    0x155: v155 = MLOAD v153(0x40)
    0x156: v156(0x20) = CONST 
    0x158: v158 = ADD v156(0x20), v155
    0x159: MSTORE v158, v151(0x0)
    0x15a: v15a(0x40) = CONST 
    0x15c: v15c = MLOAD v15a(0x40)
    0x15d: v15d(0xe0) = CONST 
    0x15f: v15f(0x2) = CONST 
    0x161: v161(0x100000000000000000000000000000000000000000000000000000000) = EXP v15f(0x2), v15d(0xe0)
    0x162: v162(0xffffffff) = CONST 
    0x168: v168(0x70a08231) = AND v14b(0x70a08231), v162(0xffffffff)
    0x169: v169(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL v168(0x70a08231), v161(0x100000000000000000000000000000000000000000000000000000000)
    0x16b: MSTORE v15c, v169(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x16c: v16c(0x1) = CONST 
    0x16e: v16e(0xa0) = CONST 
    0x170: v170(0x2) = CONST 
    0x172: v172(0x10000000000000000000000000000000000000000) = EXP v170(0x2), v16e(0xa0)
    0x173: v173(0xffffffffffffffffffffffffffffffffffffffff) = SUB v172(0x10000000000000000000000000000000000000000), v16c(0x1)
    0x176: v176 = AND v150, v173(0xffffffffffffffffffffffffffffffffffffffff)
    0x177: v177(0x4) = CONST 
    0x17a: v17a = ADD v15c, v177(0x4)
    0x17b: MSTORE v17a, v176
    0x17c: v17c(0x24) = CONST 
    0x17e: v17e = ADD v17c(0x24), v15c
    0x17f: v17f(0x20) = CONST 
    0x181: v181(0x40) = CONST 
    0x183: v183 = MLOAD v181(0x40)
    0x186: v186(0x24) = SUB v17e, v183
    0x188: v188(0x0) = CONST 
    0x18c: v18c = EXTCODESIZE v14a
    0x18d: v18d = ISZERO v18c
    0x18e: v18e = ISZERO v18d
    0x18f: v18f(0x197) = CONST 
    0x192: JUMPI v18f(0x197), v18e

    Begin block 0x193
    prev=[0x13b], succ=[]
    =================================
    0x193: v193(0x0) = CONST 
    0x196: REVERT v193(0x0), v193(0x0)

    Begin block 0x197
    prev=[0x13b], succ=[0x1a4, 0x1a8]
    =================================
    0x198: v198(0x2c6) = CONST 
    0x19b: v19b = GAS 
    0x19c: v19c = SUB v19b, v198(0x2c6)
    0x19d: v19d = CALL v19c, v14a, v188(0x0), v183, v186(0x24), v183, v17f(0x20)
    0x19e: v19e = ISZERO v19d
    0x19f: v19f = ISZERO v19e
    0x1a0: v1a0(0x1a8) = CONST 
    0x1a3: JUMPI v1a0(0x1a8), v19f

    Begin block 0x1a4
    prev=[0x197], succ=[]
    =================================
    0x1a4: v1a4(0x0) = CONST 
    0x1a7: REVERT v1a4(0x0), v1a4(0x0)

    Begin block 0x1a8
    prev=[0x197], succ=[0x1ba, 0x1be]
    =================================
    0x1ac: v1ac(0x40) = CONST 
    0x1ae: v1ae = MLOAD v1ac(0x40)
    0x1b0: v1b0 = MLOAD v1ae
    0x1b3: v1b3 = LT v1b0, v13e
    0x1b4: v1b4 = ISZERO v1b3
    0x1b5: v1b5 = ISZERO v1b4
    0x1b6: v1b6(0x1be) = CONST 
    0x1b9: JUMPI v1b6(0x1be), v1b5

    Begin block 0x1ba
    prev=[0x1a8], succ=[0x1be]
    =================================
    0x1ba: v1ba(0x7) = CONST 
    0x1ba_0x0: v1ba_0 = PHI v12d, v13a
    0x1bc: v1bc = SLOAD v1ba(0x7)
    0x1bd: v1bd = ADD v1bc, v1ba_0
    0x2532: v2532(0x1be) = CONST 
    0x2552: JUMP v2532(0x1be)

    Begin block 0x1be
    prev=[0x1ba, 0x1a8], succ=[0x1cd, 0x1c9]
    =================================
    0x1be_0x0: v1be_0 = PHI v12d, v13a, v1bd
    0x1bf: v1bf(0x3) = CONST 
    0x1c1: v1c1 = SLOAD v1bf(0x3)
    0x1c3: v1c3 = GT v1be_0, v1c1
    0x1c4: v1c4 = ISZERO v1c3
    0x1c5: v1c5(0x1cd) = CONST 
    0x1c8: JUMPI v1c5(0x1cd), v1c4

    Begin block 0x1cd
    prev=[0x1be, 0x1c9], succ=[0x228, 0x22c]
    =================================
    0x1cd_0x0: v1cd_0 = PHI v12d, v13a, v1bd, v1cc
    0x1ce: v1ce(0x1) = CONST 
    0x1d0: v1d0 = SLOAD v1ce(0x1)
    0x1d1: v1d1(0x1) = CONST 
    0x1d3: v1d3(0xa0) = CONST 
    0x1d5: v1d5(0x2) = CONST 
    0x1d7: v1d7(0x10000000000000000000000000000000000000000) = EXP v1d5(0x2), v1d3(0xa0)
    0x1d8: v1d8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d7(0x10000000000000000000000000000000000000000), v1d1(0x1)
    0x1d9: v1d9 = AND v1d8(0xffffffffffffffffffffffffffffffffffffffff), v1d0
    0x1da: v1da(0xa9059cbb) = CONST 
    0x1df: v1df = CALLER 
    0x1e1: v1e1(0x0) = CONST 
    0x1e3: v1e3(0x40) = CONST 
    0x1e5: v1e5 = MLOAD v1e3(0x40)
    0x1e6: v1e6(0x20) = CONST 
    0x1e8: v1e8 = ADD v1e6(0x20), v1e5
    0x1e9: MSTORE v1e8, v1e1(0x0)
    0x1ea: v1ea(0x40) = CONST 
    0x1ec: v1ec = MLOAD v1ea(0x40)
    0x1ed: v1ed(0xe0) = CONST 
    0x1ef: v1ef(0x2) = CONST 
    0x1f1: v1f1(0x100000000000000000000000000000000000000000000000000000000) = EXP v1ef(0x2), v1ed(0xe0)
    0x1f2: v1f2(0xffffffff) = CONST 
    0x1f8: v1f8(0xa9059cbb) = AND v1da(0xa9059cbb), v1f2(0xffffffff)
    0x1f9: v1f9(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = MUL v1f8(0xa9059cbb), v1f1(0x100000000000000000000000000000000000000000000000000000000)
    0x1fb: MSTORE v1ec, v1f9(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x1fc: v1fc(0x1) = CONST 
    0x1fe: v1fe(0xa0) = CONST 
    0x200: v200(0x2) = CONST 
    0x202: v202(0x10000000000000000000000000000000000000000) = EXP v200(0x2), v1fe(0xa0)
    0x203: v203(0xffffffffffffffffffffffffffffffffffffffff) = SUB v202(0x10000000000000000000000000000000000000000), v1fc(0x1)
    0x206: v206 = AND v1df, v203(0xffffffffffffffffffffffffffffffffffffffff)
    0x207: v207(0x4) = CONST 
    0x20a: v20a = ADD v1ec, v207(0x4)
    0x20b: MSTORE v20a, v206
    0x20c: v20c(0x24) = CONST 
    0x20f: v20f = ADD v1ec, v20c(0x24)
    0x210: MSTORE v20f, v1cd_0
    0x211: v211(0x44) = CONST 
    0x213: v213 = ADD v211(0x44), v1ec
    0x214: v214(0x20) = CONST 
    0x216: v216(0x40) = CONST 
    0x218: v218 = MLOAD v216(0x40)
    0x21b: v21b(0x44) = SUB v213, v218
    0x21d: v21d(0x0) = CONST 
    0x221: v221 = EXTCODESIZE v1d9
    0x222: v222 = ISZERO v221
    0x223: v223 = ISZERO v222
    0x224: v224(0x22c) = CONST 
    0x227: JUMPI v224(0x22c), v223

    Begin block 0x228
    prev=[0x1cd], succ=[]
    =================================
    0x228: v228(0x0) = CONST 
    0x22b: REVERT v228(0x0), v228(0x0)

    Begin block 0x22c
    prev=[0x1cd], succ=[0x239, 0x23d]
    =================================
    0x22d: v22d(0x2c6) = CONST 
    0x230: v230 = GAS 
    0x231: v231 = SUB v230, v22d(0x2c6)
    0x232: v232 = CALL v231, v1d9, v21d(0x0), v218, v21b(0x44), v218, v214(0x20)
    0x233: v233 = ISZERO v232
    0x234: v234 = ISZERO v233
    0x235: v235(0x23d) = CONST 
    0x238: JUMPI v235(0x23d), v234

    Begin block 0x239
    prev=[0x22c], succ=[]
    =================================
    0x239: v239(0x0) = CONST 
    0x23c: REVERT v239(0x0), v239(0x0)

    Begin block 0x23d
    prev=[0x22c], succ=[]
    =================================
    0x23d_0x3: v23d_3 = PHI v12d, v13a, v1bd, v1cc
    0x241: v241(0x40) = CONST 
    0x243: v243 = MLOAD v241(0x40)
    0x245: v245 = MLOAD v243
    0x248: v248(0x1) = CONST 
    0x24b: v24b = SLOAD v248(0x1)
    0x24c: v24c(0x1) = CONST 
    0x24e: v24e(0xa0) = CONST 
    0x250: v250(0x2) = CONST 
    0x252: v252(0x10000000000000000000000000000000000000000) = EXP v250(0x2), v24e(0xa0)
    0x253: v253(0xffffffffffffffffffffffffffffffffffffffff) = SUB v252(0x10000000000000000000000000000000000000000), v24c(0x1)
    0x254: v254 = CALLER 
    0x255: v255 = AND v254, v253(0xffffffffffffffffffffffffffffffffffffffff)
    0x256: v256(0x0) = CONST 
    0x25a: MSTORE v256(0x0), v255
    0x25b: v25b(0x9) = CONST 
    0x25d: v25d(0x20) = CONST 
    0x25f: MSTORE v25d(0x20), v25b(0x9)
    0x260: v260(0x40) = CONST 
    0x263: v263 = SHA3 v256(0x0), v260(0x40)
    0x265: v265 = SLOAD v263
    0x266: v266(0xff) = CONST 
    0x268: v268(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v266(0xff)
    0x26b: v26b = AND v268(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v265
    0x26c: v26c(0xff) = CONST 
    0x26e: v26e(0xa0) = CONST 
    0x270: v270(0x2) = CONST 
    0x272: v272(0x10000000000000000000000000000000000000000) = EXP v270(0x2), v26e(0xa0)
    0x275: v275 = DIV v24b, v272(0x10000000000000000000000000000000000000000)
    0x277: v277 = AND v26c(0xff), v275
    0x278: v278 = OR v277, v26b
    0x27b: SSTORE v263, v278
    0x27c: v27c(0x3) = CONST 
    0x27f: v27f = SLOAD v27c(0x3)
    0x282: v282 = SUB v27f, v23d_3
    0x284: SSTORE v27c(0x3), v282
    0x285: v285(0x2) = CONST 
    0x288: v288 = SLOAD v285(0x2)
    0x28b: v28b = ADD v23d_3, v288
    0x28e: SSTORE v285(0x2), v28b
    0x28f: v28f(0x8) = CONST 
    0x292: v292 = SLOAD v28f(0x8)
    0x295: v295 = AND v26c(0xff), v292
    0x298: v298 = ADD v248(0x1), v295
    0x29b: v29b = AND v26c(0xff), v298
    0x29f: v29f = AND v268(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v292
    0x2a0: v2a0 = OR v29f, v29b
    0x2a2: SSTORE v28f(0x8), v2a0
    0x2a3: STOP 

    Begin block 0x1c9
    prev=[0x1be], succ=[0x1cd]
    =================================
    0x1ca: v1ca(0x3) = CONST 
    0x1cc: v1cc = SLOAD v1ca(0x3)
    0x2f32: v2f32(0x1cd) = CONST 
    0x2f52: JUMP v2f32(0x1cd)

    Begin block 0x116
    prev=[0xe2], succ=[0x11e]
    =================================
    0x117: v117(0x5) = CONST 
    0x119: v119 = SLOAD v117(0x5)
    0x11a: v11a(0x3) = CONST 
    0x11c: v11c = SLOAD v11a(0x3)
    0x11d: v11d = GT v11c, v119
    0x1132: v1132(0x11e) = CONST 
    0x1152: JUMP v1132(0x11e)

}

