function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x44dae]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x317ae: v317ae(0x44dae) = CONST 
    0x317ce: JUMPI v317ae(0x44dae), v8

    Begin block 0xd
    prev=[0x0], succ=[0x457ae, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x321ae: v321ae(0x457ae) = CONST 
    0x321ce: JUMPI v321ae(0x457ae), v3c

    Begin block 0x457ae
    prev=[0xd], succ=[]
    =================================
    0x457ce: v457ce(0x29a) = CONST 
    0x457ee: CALLPRIVATE v457ce(0x29a)

    Begin block 0x41
    prev=[0xd], succ=[0x461ae, 0x4c]
    =================================
    0x42: v42(0x95ea7b3) = CONST 
    0x47: v47 = EQ v42(0x95ea7b3), v35
    0x32bae: v32bae(0x461ae) = CONST 
    0x32bce: JUMPI v32bae(0x461ae), v47

    Begin block 0x461ae
    prev=[0x41], succ=[]
    =================================
    0x461ce: v461ce(0x328) = CONST 
    0x461ee: CALLPRIVATE v461ce(0x328)

    Begin block 0x4c
    prev=[0x41], succ=[0x46bae, 0x57]
    =================================
    0x4d: v4d(0xa9ffdb7) = CONST 
    0x52: v52 = EQ v4d(0xa9ffdb7), v35
    0x335ae: v335ae(0x46bae) = CONST 
    0x335ce: JUMPI v335ae(0x46bae), v52

    Begin block 0x46bae
    prev=[0x4c], succ=[]
    =================================
    0x46bce: v46bce(0x382) = CONST 
    0x46bee: CALLPRIVATE v46bce(0x382)

    Begin block 0x57
    prev=[0x4c], succ=[0x475ae, 0x62]
    =================================
    0x58: v58(0x13b53153) = CONST 
    0x5d: v5d = EQ v58(0x13b53153), v35
    0x33fae: v33fae(0x475ae) = CONST 
    0x33fce: JUMPI v33fae(0x475ae), v5d

    Begin block 0x475ae
    prev=[0x57], succ=[]
    =================================
    0x475ce: v475ce(0x3c4) = CONST 
    0x475ee: CALLPRIVATE v475ce(0x3c4)

    Begin block 0x62
    prev=[0x57], succ=[0x47fae, 0x6d]
    =================================
    0x63: v63(0x18160ddd) = CONST 
    0x68: v68 = EQ v63(0x18160ddd), v35
    0x349ae: v349ae(0x47fae) = CONST 
    0x349ce: JUMPI v349ae(0x47fae), v68

    Begin block 0x47fae
    prev=[0x62], succ=[]
    =================================
    0x47fce: v47fce(0x3f1) = CONST 
    0x47fee: CALLPRIVATE v47fce(0x3f1)

    Begin block 0x6d
    prev=[0x62], succ=[0x489ae, 0x78]
    =================================
    0x6e: v6e(0x23b872dd) = CONST 
    0x73: v73 = EQ v6e(0x23b872dd), v35
    0x353ae: v353ae(0x489ae) = CONST 
    0x353ce: JUMPI v353ae(0x489ae), v73

    Begin block 0x489ae
    prev=[0x6d], succ=[]
    =================================
    0x489ce: v489ce(0x41a) = CONST 
    0x489ee: CALLPRIVATE v489ce(0x41a)

    Begin block 0x78
    prev=[0x6d], succ=[0x493ae, 0x83]
    =================================
    0x79: v79(0x26a21575) = CONST 
    0x7e: v7e = EQ v79(0x26a21575), v35
    0x35dae: v35dae(0x493ae) = CONST 
    0x35dce: JUMPI v35dae(0x493ae), v7e

    Begin block 0x493ae
    prev=[0x78], succ=[]
    =================================
    0x493ce: v493ce(0x493) = CONST 
    0x493ee: CALLPRIVATE v493ce(0x493)

    Begin block 0x83
    prev=[0x78], succ=[0x49dae, 0x8e]
    =================================
    0x84: v84(0x313ce567) = CONST 
    0x89: v89 = EQ v84(0x313ce567), v35
    0x367ae: v367ae(0x49dae) = CONST 
    0x367ce: JUMPI v367ae(0x49dae), v89

    Begin block 0x49dae
    prev=[0x83], succ=[]
    =================================
    0x49dce: v49dce(0x4bc) = CONST 
    0x49dee: CALLPRIVATE v49dce(0x4bc)

    Begin block 0x8e
    prev=[0x83], succ=[0x4a7ae, 0x99]
    =================================
    0x8f: v8f(0x32513ce5) = CONST 
    0x94: v94 = EQ v8f(0x32513ce5), v35
    0x371ae: v371ae(0x4a7ae) = CONST 
    0x371ce: JUMPI v371ae(0x4a7ae), v94

    Begin block 0x4a7ae
    prev=[0x8e], succ=[]
    =================================
    0x4a7ce: v4a7ce(0x4e5) = CONST 
    0x4a7ee: CALLPRIVATE v4a7ce(0x4e5)

    Begin block 0x99
    prev=[0x8e], succ=[0x4b1ae, 0xa4]
    =================================
    0x9a: v9a(0x4172d080) = CONST 
    0x9f: v9f = EQ v9a(0x4172d080), v35
    0x37bae: v37bae(0x4b1ae) = CONST 
    0x37bce: JUMPI v37bae(0x4b1ae), v9f

    Begin block 0x4b1ae
    prev=[0x99], succ=[]
    =================================
    0x4b1ce: v4b1ce(0x53a) = CONST 
    0x4b1ee: CALLPRIVATE v4b1ce(0x53a)

    Begin block 0xa4
    prev=[0x99], succ=[0x4bbae, 0xaf]
    =================================
    0xa5: va5(0x4477c5da) = CONST 
    0xaa: vaa = EQ va5(0x4477c5da), v35
    0x385ae: v385ae(0x4bbae) = CONST 
    0x385ce: JUMPI v385ae(0x4bbae), vaa

    Begin block 0x4bbae
    prev=[0xa4], succ=[]
    =================================
    0x4bbce: v4bbce(0x563) = CONST 
    0x4bbee: CALLPRIVATE v4bbce(0x563)

    Begin block 0xaf
    prev=[0xa4], succ=[0x4c5ae, 0xba]
    =================================
    0xb0: vb0(0x4a36df25) = CONST 
    0xb5: vb5 = EQ vb0(0x4a36df25), v35
    0x38fae: v38fae(0x4c5ae) = CONST 
    0x38fce: JUMPI v38fae(0x4c5ae), vb5

    Begin block 0x4c5ae
    prev=[0xaf], succ=[]
    =================================
    0x4c5ce: v4c5ce(0x578) = CONST 
    0x4c5ee: CALLPRIVATE v4c5ce(0x578)

    Begin block 0xba
    prev=[0xaf], succ=[0x4cfae, 0xc5]
    =================================
    0xbb: vbb(0x54fd4d50) = CONST 
    0xc0: vc0 = EQ vbb(0x54fd4d50), v35
    0x399ae: v399ae(0x4cfae) = CONST 
    0x399ce: JUMPI v399ae(0x4cfae), vc0

    Begin block 0x4cfae
    prev=[0xba], succ=[]
    =================================
    0x4cfce: v4cfce(0x5b1) = CONST 
    0x4cfee: CALLPRIVATE v4cfce(0x5b1)

    Begin block 0xc5
    prev=[0xba], succ=[0x4d9ae, 0xd0]
    =================================
    0xc6: vc6(0x6fe3a567) = CONST 
    0xcb: vcb = EQ vc6(0x6fe3a567), v35
    0x3a3ae: v3a3ae(0x4d9ae) = CONST 
    0x3a3ce: JUMPI v3a3ae(0x4d9ae), vcb

    Begin block 0x4d9ae
    prev=[0xc5], succ=[]
    =================================
    0x4d9ce: v4d9ce(0x63f) = CONST 
    0x4d9ee: CALLPRIVATE v4d9ce(0x63f)

    Begin block 0xd0
    prev=[0xc5], succ=[0x4e3ae, 0xdb]
    =================================
    0xd1: vd1(0x70a08231) = CONST 
    0xd6: vd6 = EQ vd1(0x70a08231), v35
    0x3adae: v3adae(0x4e3ae) = CONST 
    0x3adce: JUMPI v3adae(0x4e3ae), vd6

    Begin block 0x4e3ae
    prev=[0xd0], succ=[]
    =================================
    0x4e3ce: v4e3ce(0x668) = CONST 
    0x4e3ee: CALLPRIVATE v4e3ce(0x668)

    Begin block 0xdb
    prev=[0xd0], succ=[0x4edae, 0xe6]
    =================================
    0xdc: vdc(0x771282f6) = CONST 
    0xe1: ve1 = EQ vdc(0x771282f6), v35
    0x3b7ae: v3b7ae(0x4edae) = CONST 
    0x3b7ce: JUMPI v3b7ae(0x4edae), ve1

    Begin block 0x4edae
    prev=[0xdb], succ=[]
    =================================
    0x4edce: v4edce(0x6b5) = CONST 
    0x4edee: CALLPRIVATE v4edce(0x6b5)

    Begin block 0xe6
    prev=[0xdb], succ=[0x4f7ae, 0xf1]
    =================================
    0xe7: ve7(0x775c46cd) = CONST 
    0xec: vec = EQ ve7(0x775c46cd), v35
    0x3c1ae: v3c1ae(0x4f7ae) = CONST 
    0x3c1ce: JUMPI v3c1ae(0x4f7ae), vec

    Begin block 0x4f7ae
    prev=[0xe6], succ=[]
    =================================
    0x4f7ce: v4f7ce(0x6de) = CONST 
    0x4f7ee: CALLPRIVATE v4f7ce(0x6de)

    Begin block 0xf1
    prev=[0xe6], succ=[0x501ae, 0xfc]
    =================================
    0xf2: vf2(0x79c65068) = CONST 
    0xf7: vf7 = EQ vf2(0x79c65068), v35
    0x3cbae: v3cbae(0x501ae) = CONST 
    0x3cbce: JUMPI v3cbae(0x501ae), vf7

    Begin block 0x501ae
    prev=[0xf1], succ=[]
    =================================
    0x501ce: v501ce(0x70a) = CONST 
    0x501ee: CALLPRIVATE v501ce(0x70a)

    Begin block 0xfc
    prev=[0xf1], succ=[0x50bae, 0x107]
    =================================
    0xfd: vfd(0x8fd3ab80) = CONST 
    0x102: v102 = EQ vfd(0x8fd3ab80), v35
    0x3d5ae: v3d5ae(0x50bae) = CONST 
    0x3d5ce: JUMPI v3d5ae(0x50bae), v102

    Begin block 0x50bae
    prev=[0xfc], succ=[]
    =================================
    0x50bce: v50bce(0x74c) = CONST 
    0x50bee: CALLPRIVATE v50bce(0x74c)

    Begin block 0x107
    prev=[0xfc], succ=[0x515ae, 0x112]
    =================================
    0x108: v108(0x95d89b41) = CONST 
    0x10d: v10d = EQ v108(0x95d89b41), v35
    0x3dfae: v3dfae(0x515ae) = CONST 
    0x3dfce: JUMPI v3dfae(0x515ae), v10d

    Begin block 0x515ae
    prev=[0x107], succ=[]
    =================================
    0x515ce: v515ce(0x761) = CONST 
    0x515ee: CALLPRIVATE v515ce(0x761)

    Begin block 0x112
    prev=[0x107], succ=[0x51fae, 0x11d]
    =================================
    0x113: v113(0x98e52f9a) = CONST 
    0x118: v118 = EQ v113(0x98e52f9a), v35
    0x3e9ae: v3e9ae(0x51fae) = CONST 
    0x3e9ce: JUMPI v3e9ae(0x51fae), v118

    Begin block 0x51fae
    prev=[0x112], succ=[]
    =================================
    0x51fce: v51fce(0x7ef) = CONST 
    0x51fee: CALLPRIVATE v51fce(0x7ef)

    Begin block 0x11d
    prev=[0x112], succ=[0x529ae, 0x128]
    =================================
    0x11e: v11e(0xa6f9dae1) = CONST 
    0x123: v123 = EQ v11e(0xa6f9dae1), v35
    0x3f3ae: v3f3ae(0x529ae) = CONST 
    0x3f3ce: JUMPI v3f3ae(0x529ae), v123

    Begin block 0x529ae
    prev=[0x11d], succ=[]
    =================================
    0x529ce: v529ce(0x812) = CONST 
    0x529ee: CALLPRIVATE v529ce(0x812)

    Begin block 0x128
    prev=[0x11d], succ=[0x533ae, 0x133]
    =================================
    0x129: v129(0xa81c3bdf) = CONST 
    0x12e: v12e = EQ v129(0xa81c3bdf), v35
    0x3fdae: v3fdae(0x533ae) = CONST 
    0x3fdce: JUMPI v3fdae(0x533ae), v12e

    Begin block 0x533ae
    prev=[0x128], succ=[]
    =================================
    0x533ce: v533ce(0x84b) = CONST 
    0x533ee: CALLPRIVATE v533ce(0x84b)

    Begin block 0x133
    prev=[0x128], succ=[0x53dae, 0x13e]
    =================================
    0x134: v134(0xa9059cbb) = CONST 
    0x139: v139 = EQ v134(0xa9059cbb), v35
    0x407ae: v407ae(0x53dae) = CONST 
    0x407ce: JUMPI v407ae(0x53dae), v139

    Begin block 0x53dae
    prev=[0x133], succ=[]
    =================================
    0x53dce: v53dce(0x8a0) = CONST 
    0x53dee: CALLPRIVATE v53dce(0x8a0)

    Begin block 0x13e
    prev=[0x133], succ=[0x547ae, 0x149]
    =================================
    0x13f: v13f(0xb921e163) = CONST 
    0x144: v144 = EQ v13f(0xb921e163), v35
    0x411ae: v411ae(0x547ae) = CONST 
    0x411ce: JUMPI v411ae(0x547ae), v144

    Begin block 0x547ae
    prev=[0x13e], succ=[]
    =================================
    0x547ce: v547ce(0x8fa) = CONST 
    0x547ee: CALLPRIVATE v547ce(0x8fa)

    Begin block 0x149
    prev=[0x13e], succ=[0x551ae, 0x154]
    =================================
    0x14a: v14a(0xcb7b8673) = CONST 
    0x14f: v14f = EQ v14a(0xcb7b8673), v35
    0x41bae: v41bae(0x551ae) = CONST 
    0x41bce: JUMPI v41bae(0x551ae), v14f

    Begin block 0x551ae
    prev=[0x149], succ=[]
    =================================
    0x551ce: v551ce(0x91d) = CONST 
    0x551ee: CALLPRIVATE v551ce(0x91d)

    Begin block 0x154
    prev=[0x149], succ=[0x55bae, 0x15f]
    =================================
    0x155: v155(0xd648a647) = CONST 
    0x15a: v15a = EQ v155(0xd648a647), v35
    0x425ae: v425ae(0x55bae) = CONST 
    0x425ce: JUMPI v425ae(0x55bae), v15a

    Begin block 0x55bae
    prev=[0x154], succ=[]
    =================================
    0x55bce: v55bce(0x940) = CONST 
    0x55bee: CALLPRIVATE v55bce(0x940)

    Begin block 0x15f
    prev=[0x154], succ=[0x565ae, 0x16a]
    =================================
    0x160: v160(0xdd62ed3e) = CONST 
    0x165: v165 = EQ v160(0xdd62ed3e), v35
    0x42fae: v42fae(0x565ae) = CONST 
    0x42fce: JUMPI v42fae(0x565ae), v165

    Begin block 0x565ae
    prev=[0x15f], succ=[]
    =================================
    0x565ce: v565ce(0x969) = CONST 
    0x565ee: CALLPRIVATE v565ce(0x969)

    Begin block 0x16a
    prev=[0x15f], succ=[0x56fae, 0x175]
    =================================
    0x16b: v16b(0xe28d717b) = CONST 
    0x170: v170 = EQ v16b(0xe28d717b), v35
    0x439ae: v439ae(0x56fae) = CONST 
    0x439ce: JUMPI v439ae(0x56fae), v170

    Begin block 0x56fae
    prev=[0x16a], succ=[]
    =================================
    0x56fce: v56fce(0x9d5) = CONST 
    0x56fee: CALLPRIVATE v56fce(0x9d5)

    Begin block 0x175
    prev=[0x16a], succ=[0x44dae, 0x579ae]
    =================================
    0x176: v176(0xff29507d) = CONST 
    0x17b: v17b = EQ v176(0xff29507d), v35
    0x443ae: v443ae(0x579ae) = CONST 
    0x443ce: JUMPI v443ae(0x579ae), v17b

    Begin block 0x44dae
    prev=[0x0, 0x175], succ=[]
    =================================
    0x44dce: v44dce(0x180) = CONST 
    0x44dee: CALLPRIVATE v44dce(0x180)

    Begin block 0x579ae
    prev=[0x175], succ=[]
    =================================
    0x579ce: v579ce(0x9ea) = CONST 
    0x579ee: CALLPRIVATE v579ce(0x9ea)

}

function fallback()() public {
    Begin block 0x180
    prev=[], succ=[0x199, 0x19d]
    =================================
    0x181: v181(0x0) = CONST 
    0x183: v183(0x5) = CONST 
    0x185: v185(0x14) = CONST 
    0x188: v188 = SLOAD v183(0x5)
    0x18a: v18a(0x100) = CONST 
    0x18d: v18d(0x10000000000000000000000000000000000000000) = EXP v18a(0x100), v185(0x14)
    0x18f: v18f = DIV v188, v18d(0x10000000000000000000000000000000000000000)
    0x190: v190(0xff) = CONST 
    0x192: v192 = AND v190(0xff), v18f
    0x193: v193 = ISZERO v192
    0x194: v194 = ISZERO v193
    0x195: v195(0x19d) = CONST 
    0x198: JUMPI v195(0x19d), v194

    Begin block 0x199
    prev=[0x180], succ=[]
    =================================
    0x199: v199(0x0) = CONST 
    0x19c: REVERT v199(0x0), v199(0x0)

    Begin block 0x19d
    prev=[0x180], succ=[0x1a7, 0x1ab]
    =================================
    0x19e: v19e(0x0) = CONST 
    0x1a0: v1a0 = CALLVALUE 
    0x1a1: v1a1 = EQ v1a0, v19e(0x0)
    0x1a2: v1a2 = ISZERO v1a1
    0x1a3: v1a3(0x1ab) = CONST 
    0x1a6: JUMPI v1a3(0x1ab), v1a2

    Begin block 0x1a7
    prev=[0x19d], succ=[]
    =================================
    0x1a7: v1a7(0x0) = CONST 
    0x1aa: REVERT v1a7(0x0), v1a7(0x0)

    Begin block 0x1ab
    prev=[0x19d], succ=[0x1b6, 0x1ba]
    =================================
    0x1ac: v1ac(0x6) = CONST 
    0x1ae: v1ae = SLOAD v1ac(0x6)
    0x1af: v1af = NUMBER 
    0x1b0: v1b0 = LT v1af, v1ae
    0x1b1: v1b1 = ISZERO v1b0
    0x1b2: v1b2(0x1ba) = CONST 
    0x1b5: JUMPI v1b2(0x1ba), v1b1

    Begin block 0x1b6
    prev=[0x1ab], succ=[]
    =================================
    0x1b6: v1b6(0x0) = CONST 
    0x1b9: REVERT v1b6(0x0), v1b6(0x0)

    Begin block 0x1ba
    prev=[0x1ab], succ=[0x1c5, 0x1c9]
    =================================
    0x1bb: v1bb(0x7) = CONST 
    0x1bd: v1bd = SLOAD v1bb(0x7)
    0x1be: v1be = NUMBER 
    0x1bf: v1bf = GT v1be, v1bd
    0x1c0: v1c0 = ISZERO v1bf
    0x1c1: v1c1(0x1c9) = CONST 
    0x1c4: JUMPI v1c1(0x1c9), v1c0

    Begin block 0x1c5
    prev=[0x1ba], succ=[]
    =================================
    0x1c5: v1c5(0x0) = CONST 
    0x1c8: REVERT v1c5(0x0), v1c5(0x0)

    Begin block 0x1c9
    prev=[0x1ba], succ=[0x1d5]
    =================================
    0x1ca: v1ca(0x1d5) = CONST 
    0x1cd: v1cd = CALLVALUE 
    0x1ce: v1ce(0xb) = CONST 
    0x1d0: v1d0 = SLOAD v1ce(0xb)
    0x1d1: v1d1(0xa13) = CONST 
    0x1d4: v1d4_0 = CALLPRIVATE v1d1(0xa13), v1d0, v1cd, v1ca(0x1d5)

    Begin block 0x1d5
    prev=[0x1c9], succ=[0x1e6, 0x1ea]
    =================================
    0x1d8: v1d8(0x8) = CONST 
    0x1da: v1da = SLOAD v1d8(0x8)
    0x1db: v1db(0x9) = CONST 
    0x1dd: v1dd = SLOAD v1db(0x9)
    0x1df: v1df = ADD v1d4_0, v1dd
    0x1e0: v1e0 = GT v1df, v1da
    0x1e1: v1e1 = ISZERO v1e0
    0x1e2: v1e2(0x1ea) = CONST 
    0x1e5: JUMPI v1e2(0x1ea), v1e1

    Begin block 0x1e6
    prev=[0x1d5], succ=[]
    =================================
    0x1e6: v1e6(0x0) = CONST 
    0x1e9: REVERT v1e6(0x0), v1e6(0x0)

    Begin block 0x1ea
    prev=[0x1d5], succ=[0x1f6]
    =================================
    0x1eb: v1eb(0x1f6) = CONST 
    0x1ee: v1ee(0x9) = CONST 
    0x1f0: v1f0 = SLOAD v1ee(0x9)
    0x1f2: v1f2(0xa46) = CONST 
    0x1f5: v1f5_0 = CALLPRIVATE v1f2(0xa46), v1d4_0, v1f0, v1eb(0x1f6)

    Begin block 0x1f6
    prev=[0x1ea], succ=[]
    =================================
    0x1f7: v1f7(0x9) = CONST 
    0x1fb: SSTORE v1f7(0x9), v1f5_0
    0x1fe: v1fe(0x1) = CONST 
    0x200: v200(0x0) = CONST 
    0x202: v202 = CALLER 
    0x203: v203(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x218: v218 = AND v203(0xffffffffffffffffffffffffffffffffffffffff), v202
    0x219: v219(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22e: v22e = AND v219(0xffffffffffffffffffffffffffffffffffffffff), v218
    0x230: MSTORE v200(0x0), v22e
    0x231: v231(0x20) = CONST 
    0x233: v233(0x20) = ADD v231(0x20), v200(0x0)
    0x236: MSTORE v233(0x20), v1fe(0x1)
    0x237: v237(0x20) = CONST 
    0x239: v239(0x40) = ADD v237(0x20), v233(0x20)
    0x23a: v23a(0x0) = CONST 
    0x23c: v23c = SHA3 v23a(0x0), v239(0x40)
    0x23d: v23d(0x0) = CONST 
    0x241: v241 = SLOAD v23c
    0x242: v242 = ADD v241, v1d4_0
    0x248: SSTORE v23c, v242
    0x24a: v24a = CALLER 
    0x24b: v24b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x260: v260 = AND v24b(0xffffffffffffffffffffffffffffffffffffffff), v24a
    0x261: v261(0x7ba26a0f068612fb882b3272004674d21fed286c2c8c795cf653044690b32db4) = CONST 
    0x283: v283(0x40) = CONST 
    0x285: v285 = MLOAD v283(0x40)
    0x289: MSTORE v285, v1d4_0
    0x28a: v28a(0x20) = CONST 
    0x28c: v28c = ADD v28a(0x20), v285
    0x290: v290(0x40) = CONST 
    0x292: v292 = MLOAD v290(0x40)
    0x295: v295(0x20) = SUB v28c, v292
    0x297: LOG2 v292, v295(0x20), v261(0x7ba26a0f068612fb882b3272004674d21fed286c2c8c795cf653044690b32db4), v260
    0x299: STOP 

}

function name()() public {
    Begin block 0x29a
    prev=[], succ=[0x2a1, 0x2a5]
    =================================
    0x29b: v29b = CALLVALUE 
    0x29c: v29c = ISZERO v29b
    0x29d: v29d(0x2a5) = CONST 
    0x2a0: JUMPI v29d(0x2a5), v29c

    Begin block 0x2a1
    prev=[0x29a], succ=[]
    =================================
    0x2a1: v2a1(0x0) = CONST 
    0x2a4: REVERT v2a1(0x0), v2a1(0x0)

    Begin block 0x2a5
    prev=[0x29a], succ=[0xa70]
    =================================
    0x2a6: v2a6(0x2ad) = CONST 
    0x2a9: v2a9(0xa70) = CONST 
    0x2ac: JUMP v2a9(0xa70)

    Begin block 0xa70
    prev=[0x2a5], succ=[0x2ad]
    =================================
    0xa71: va71(0x40) = CONST 
    0xa74: va74 = MLOAD va71(0x40)
    0xa77: va77 = ADD va74, va71(0x40)
    0xa78: va78(0x40) = CONST 
    0xa7a: MSTORE va78(0x40), va77
    0xa7c: va7c(0x4) = CONST 
    0xa7f: MSTORE va74, va7c(0x4)
    0xa80: va80(0x20) = CONST 
    0xa82: va82 = ADD va80(0x20), va74
    0xa83: va83(0x6162636400000000000000000000000000000000000000000000000000000000) = CONST 
    0xaa5: MSTORE va82, va83(0x6162636400000000000000000000000000000000000000000000000000000000)
    0xaa8: JUMP v2a6(0x2ad)

    Begin block 0x2ad
    prev=[0xa70], succ=[0x2d2]
    =================================
    0x2ae: v2ae(0x40) = CONST 
    0x2b0: v2b0 = MLOAD v2ae(0x40)
    0x2b3: v2b3(0x20) = CONST 
    0x2b5: v2b5 = ADD v2b3(0x20), v2b0
    0x2b8: v2b8(0x20) = SUB v2b5, v2b0
    0x2ba: MSTORE v2b0, v2b8(0x20)
    0x2be: v2be(0x4) = MLOAD va74
    0x2c0: MSTORE v2b5, v2be(0x4)
    0x2c1: v2c1(0x20) = CONST 
    0x2c3: v2c3 = ADD v2c1(0x20), v2b5
    0x2c7: v2c7(0x4) = MLOAD va74
    0x2c9: v2c9(0x20) = CONST 
    0x2cb: v2cb = ADD v2c9(0x20), va74
    0x2d0: v2d0(0x0) = CONST 
    0x393e: v393e(0x2d2) = CONST 
    0x395e: JUMP v393e(0x2d2)

    Begin block 0x2d2
    prev=[0x2ad, 0x2db], succ=[0x2ed, 0x2db]
    =================================
    0x2d2_0x0: v2d2_0 = PHI v2d0(0x0), v2e6
    0x2d5: v2d5 = LT v2d2_0, v2c7(0x4)
    0x2d6: v2d6 = ISZERO v2d5
    0x2d7: v2d7(0x2ed) = CONST 
    0x2da: JUMPI v2d7(0x2ed), v2d6

    Begin block 0x2ed
    prev=[0x2d2], succ=[0x31a, 0x301]
    =================================
    0x2f6: v2f6 = ADD v2c7(0x4), v2c3
    0x2f8: v2f8(0x1f) = CONST 
    0x2fa: v2fa(0x4) = AND v2f8(0x1f), v2c7(0x4)
    0x2fc: v2fc(0x0) = ISZERO v2fa(0x4)
    0x2fd: v2fd(0x31a) = CONST 
    0x300: JUMPI v2fd(0x31a), v2fc(0x0)

    Begin block 0x31a
    prev=[0x2ed, 0x301], succ=[]
    =================================
    0x31a_0x1: v31a_1 = PHI v2f6, v317
    0x320: v320(0x40) = CONST 
    0x322: v322 = MLOAD v320(0x40)
    0x325: v325 = SUB v31a_1, v322
    0x327: RETURN v322, v325

    Begin block 0x301
    prev=[0x2ed], succ=[0x31a]
    =================================
    0x303: v303 = SUB v2f6, v2fa(0x4)
    0x305: v305 = MLOAD v303
    0x306: v306(0x1) = CONST 
    0x309: v309(0x20) = CONST 
    0x30b: v30b(0x1c) = SUB v309(0x20), v2fa(0x4)
    0x30c: v30c(0x100) = CONST 
    0x30f: v30f(0x100000000000000000000000000000000000000000000000000000000) = EXP v30c(0x100), v30b(0x1c)
    0x310: v310(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v30f(0x100000000000000000000000000000000000000000000000000000000), v306(0x1)
    0x311: v311(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v310(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x312: v312 = AND v311(0xffffffff00000000000000000000000000000000000000000000000000000000), v305
    0x314: MSTORE v303, v312
    0x315: v315(0x20) = CONST 
    0x317: v317 = ADD v315(0x20), v303
    0x433e: v433e(0x31a) = CONST 
    0x435e: JUMP v433e(0x31a)

    Begin block 0x2db
    prev=[0x2d2], succ=[0x2d2]
    =================================
    0x2db_0x0: v2db_0 = PHI v2d0(0x0), v2e6
    0x2dd: v2dd = ADD v2cb, v2db_0
    0x2de: v2de = MLOAD v2dd
    0x2e1: v2e1 = ADD v2c3, v2db_0
    0x2e2: MSTORE v2e1, v2de
    0x2e3: v2e3(0x20) = CONST 
    0x2e6: v2e6 = ADD v2db_0, v2e3(0x20)
    0x2e9: v2e9(0x2d2) = CONST 
    0x2ec: JUMP v2e9(0x2d2)

}

function approve(address,uint256)() public {
    Begin block 0x328
    prev=[], succ=[0x32f, 0x333]
    =================================
    0x329: v329 = CALLVALUE 
    0x32a: v32a = ISZERO v329
    0x32b: v32b(0x333) = CONST 
    0x32e: JUMPI v32b(0x333), v32a

    Begin block 0x32f
    prev=[0x328], succ=[]
    =================================
    0x32f: v32f(0x0) = CONST 
    0x332: REVERT v32f(0x0), v32f(0x0)

    Begin block 0x333
    prev=[0x328], succ=[0xaa9]
    =================================
    0x334: v334(0x368) = CONST 
    0x337: v337(0x4) = CONST 
    0x33b: v33b = CALLDATALOAD v337(0x4)
    0x33c: v33c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x351: v351 = AND v33c(0xffffffffffffffffffffffffffffffffffffffff), v33b
    0x353: v353(0x20) = CONST 
    0x355: v355(0x24) = ADD v353(0x20), v337(0x4)
    0x35a: v35a = CALLDATALOAD v355(0x24)
    0x35c: v35c(0x20) = CONST 
    0x35e: v35e(0x44) = ADD v35c(0x20), v355(0x24)
    0x364: v364(0xaa9) = CONST 
    0x367: JUMP v364(0xaa9)

    Begin block 0xaa9
    prev=[0x333], succ=[0x368]
    =================================
    0xaaa: vaaa(0x0) = CONST 
    0xaad: vaad(0x2) = CONST 
    0xaaf: vaaf(0x0) = CONST 
    0xab1: vab1 = CALLER 
    0xab2: vab2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xac7: vac7 = AND vab2(0xffffffffffffffffffffffffffffffffffffffff), vab1
    0xac8: vac8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xadd: vadd = AND vac8(0xffffffffffffffffffffffffffffffffffffffff), vac7
    0xadf: MSTORE vaaf(0x0), vadd
    0xae0: vae0(0x20) = CONST 
    0xae2: vae2(0x20) = ADD vae0(0x20), vaaf(0x0)
    0xae5: MSTORE vae2(0x20), vaad(0x2)
    0xae6: vae6(0x20) = CONST 
    0xae8: vae8(0x40) = ADD vae6(0x20), vae2(0x20)
    0xae9: vae9(0x0) = CONST 
    0xaeb: vaeb = SHA3 vae9(0x0), vae8(0x40)
    0xaec: vaec(0x0) = CONST 
    0xaef: vaef(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb04: vb04 = AND vaef(0xffffffffffffffffffffffffffffffffffffffff), v351
    0xb05: vb05(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb1a: vb1a = AND vb05(0xffffffffffffffffffffffffffffffffffffffff), vb04
    0xb1c: MSTORE vaec(0x0), vb1a
    0xb1d: vb1d(0x20) = CONST 
    0xb1f: vb1f(0x20) = ADD vb1d(0x20), vaec(0x0)
    0xb22: MSTORE vb1f(0x20), vaeb
    0xb23: vb23(0x20) = CONST 
    0xb25: vb25(0x40) = ADD vb23(0x20), vb1f(0x20)
    0xb26: vb26(0x0) = CONST 
    0xb28: vb28 = SHA3 vb26(0x0), vb25(0x40)
    0xb2b: SSTORE vb28, v35a
    0xb2e: vb2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb43: vb43 = AND vb2e(0xffffffffffffffffffffffffffffffffffffffff), v351
    0xb44: vb44 = CALLER 
    0xb45: vb45(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb5a: vb5a = AND vb45(0xffffffffffffffffffffffffffffffffffffffff), vb44
    0xb5b: vb5b(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xb7d: vb7d(0x40) = CONST 
    0xb7f: vb7f = MLOAD vb7d(0x40)
    0xb83: MSTORE vb7f, v35a
    0xb84: vb84(0x20) = CONST 
    0xb86: vb86 = ADD vb84(0x20), vb7f
    0xb8a: vb8a(0x40) = CONST 
    0xb8c: vb8c = MLOAD vb8a(0x40)
    0xb8f: vb8f(0x20) = SUB vb86, vb8c
    0xb91: LOG3 vb8c, vb8f(0x20), vb5b(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vb5a, vb43
    0xb92: vb92(0x1) = CONST 
    0xb9a: JUMP v334(0x368)

    Begin block 0x368
    prev=[0xaa9], succ=[]
    =================================
    0x369: v369(0x40) = CONST 
    0x36b: v36b = MLOAD v369(0x40)
    0x36e: v36e(0x0) = ISZERO vb92(0x1)
    0x36f: v36f(0x1) = ISZERO v36e(0x0)
    0x370: v370(0x0) = ISZERO v36f(0x1)
    0x371: v371(0x1) = ISZERO v370(0x0)
    0x373: MSTORE v36b, v371(0x1)
    0x374: v374(0x20) = CONST 
    0x376: v376 = ADD v374(0x20), v36b
    0x37a: v37a(0x40) = CONST 
    0x37c: v37c = MLOAD v37a(0x40)
    0x37f: v37f(0x20) = SUB v376, v37c
    0x381: RETURN v37c, v37f(0x20)

}

function allocateToken(address,uint256)() public {
    Begin block 0x382
    prev=[], succ=[0x389, 0x38d]
    =================================
    0x383: v383 = CALLVALUE 
    0x384: v384 = ISZERO v383
    0x385: v385(0x38d) = CONST 
    0x388: JUMPI v385(0x38d), v384

    Begin block 0x389
    prev=[0x382], succ=[]
    =================================
    0x389: v389(0x0) = CONST 
    0x38c: REVERT v389(0x0), v389(0x0)

    Begin block 0x38d
    prev=[0x382], succ=[0xb9b]
    =================================
    0x38e: v38e(0x3c2) = CONST 
    0x391: v391(0x4) = CONST 
    0x395: v395 = CALLDATALOAD v391(0x4)
    0x396: v396(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ab: v3ab = AND v396(0xffffffffffffffffffffffffffffffffffffffff), v395
    0x3ad: v3ad(0x20) = CONST 
    0x3af: v3af(0x24) = ADD v3ad(0x20), v391(0x4)
    0x3b4: v3b4 = CALLDATALOAD v3af(0x24)
    0x3b6: v3b6(0x20) = CONST 
    0x3b8: v3b8(0x44) = ADD v3b6(0x20), v3af(0x24)
    0x3be: v3be(0xb9b) = CONST 
    0x3c1: JUMP v3be(0xb9b)

    Begin block 0xb9b
    prev=[0x38d], succ=[0xbf5, 0xbf9]
    =================================
    0xb9c: vb9c(0x0) = CONST 
    0xb9e: vb9e(0x4) = CONST 
    0xba0: vba0(0x0) = CONST 
    0xba3: vba3 = SLOAD vb9e(0x4)
    0xba5: vba5(0x100) = CONST 
    0xba8: vba8(0x1) = EXP vba5(0x100), vba0(0x0)
    0xbaa: vbaa = DIV vba3, vba8(0x1)
    0xbab: vbab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbc0: vbc0 = AND vbab(0xffffffffffffffffffffffffffffffffffffffff), vbaa
    0xbc1: vbc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbd6: vbd6 = AND vbc1(0xffffffffffffffffffffffffffffffffffffffff), vbc0
    0xbd7: vbd7 = CALLER 
    0xbd8: vbd8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbed: vbed = AND vbd8(0xffffffffffffffffffffffffffffffffffffffff), vbd7
    0xbee: vbee = EQ vbed, vbd6
    0xbef: vbef = ISZERO vbee
    0xbf0: vbf0 = ISZERO vbef
    0xbf1: vbf1(0xbf9) = CONST 
    0xbf4: JUMPI vbf1(0xbf9), vbf0

    Begin block 0xbf5
    prev=[0xb9b], succ=[]
    =================================
    0xbf5: vbf5(0x0) = CONST 
    0xbf8: REVERT vbf5(0x0), vbf5(0x0)

    Begin block 0xbf9
    prev=[0xb9b], succ=[0xc03, 0xc07]
    =================================
    0xbfa: vbfa(0x0) = CONST 
    0xbfd: vbfd = EQ v3b4, vbfa(0x0)
    0xbfe: vbfe = ISZERO vbfd
    0xbff: vbff(0xc07) = CONST 
    0xc02: JUMPI vbff(0xc07), vbfe

    Begin block 0xc03
    prev=[0xbf9], succ=[]
    =================================
    0xc03: vc03(0x0) = CONST 
    0xc06: REVERT vc03(0x0), vc03(0x0)

    Begin block 0xc07
    prev=[0xbf9], succ=[0xc3d, 0xc41]
    =================================
    0xc08: vc08(0x0) = CONST 
    0xc0a: vc0a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc1f: vc1f(0x0) = AND vc0a(0xffffffffffffffffffffffffffffffffffffffff), vc08(0x0)
    0xc21: vc21(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc36: vc36 = AND vc21(0xffffffffffffffffffffffffffffffffffffffff), v3ab
    0xc37: vc37 = EQ vc36, vc1f(0x0)
    0xc38: vc38 = ISZERO vc37
    0xc39: vc39(0xc41) = CONST 
    0xc3c: JUMPI vc39(0xc41), vc38

    Begin block 0xc3d
    prev=[0xc07], succ=[]
    =================================
    0xc3d: vc3d(0x0) = CONST 
    0xc40: REVERT vc3d(0x0), vc3d(0x0)

    Begin block 0xc41
    prev=[0xc07], succ=[0x1c3aB0xc41]
    =================================
    0xc42: vc42(0xc55) = CONST 
    0xc45: vc45(0xc4d) = CONST 
    0xc49: vc49(0x1c3a) = CONST 
    0xc4c: JUMP vc49(0x1c3a)

    Begin block 0x1c3aB0xc41
    prev=[0xc41], succ=[0xc4d]
    =================================
    0x1c3bS0xc41: v1c3bVc41(0x0) = CONST 
    0x1c3dS0xc41: v1c3dVc41(0x12) = CONST 
    0x1c3fS0xc41: v1c3fVc41(0xa) = CONST 
    0x1c41S0xc41: v1c41Vc41(0xde0b6b3a7640000) = EXP v1c3fVc41(0xa), v1c3dVc41(0x12)
    0x1c43S0xc41: v1c43Vc41 = MUL v3b4, v1c41Vc41(0xde0b6b3a7640000)
    0x1c49S0xc41: JUMP vc45(0xc4d)

    Begin block 0xc4d
    prev=[0x1c3aB0xc41], succ=[0xc55]
    =================================
    0xc4e: vc4e(0xb) = CONST 
    0xc50: vc50 = SLOAD vc4e(0xb)
    0xc51: vc51(0xa13) = CONST 
    0xc54: vc54_0 = CALLPRIVATE vc51(0xa13), vc50, v1c43Vc41, vc42(0xc55)

    Begin block 0xc55
    prev=[0xc4d], succ=[0xc66, 0xc6a]
    =================================
    0xc58: vc58(0x8) = CONST 
    0xc5a: vc5a = SLOAD vc58(0x8)
    0xc5b: vc5b(0x9) = CONST 
    0xc5d: vc5d = SLOAD vc5b(0x9)
    0xc5f: vc5f = ADD vc54_0, vc5d
    0xc60: vc60 = GT vc5f, vc5a
    0xc61: vc61 = ISZERO vc60
    0xc62: vc62(0xc6a) = CONST 
    0xc65: JUMPI vc62(0xc6a), vc61

    Begin block 0xc66
    prev=[0xc55], succ=[]
    =================================
    0xc66: vc66(0x0) = CONST 
    0xc69: REVERT vc66(0x0), vc66(0x0)

    Begin block 0xc6a
    prev=[0xc55], succ=[0xc76]
    =================================
    0xc6b: vc6b(0xc76) = CONST 
    0xc6e: vc6e(0x9) = CONST 
    0xc70: vc70 = SLOAD vc6e(0x9)
    0xc72: vc72(0xa46) = CONST 
    0xc75: vc75_0 = CALLPRIVATE vc72(0xa46), vc54_0, vc70, vc6b(0xc76)

    Begin block 0xc76
    prev=[0xc6a], succ=[0x3c2]
    =================================
    0xc77: vc77(0x9) = CONST 
    0xc7b: SSTORE vc77(0x9), vc75_0
    0xc7e: vc7e(0x1) = CONST 
    0xc80: vc80(0x0) = CONST 
    0xc83: vc83(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc98: vc98 = AND vc83(0xffffffffffffffffffffffffffffffffffffffff), v3ab
    0xc99: vc99(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcae: vcae = AND vc99(0xffffffffffffffffffffffffffffffffffffffff), vc98
    0xcb0: MSTORE vc80(0x0), vcae
    0xcb1: vcb1(0x20) = CONST 
    0xcb3: vcb3(0x20) = ADD vcb1(0x20), vc80(0x0)
    0xcb6: MSTORE vcb3(0x20), vc7e(0x1)
    0xcb7: vcb7(0x20) = CONST 
    0xcb9: vcb9(0x40) = ADD vcb7(0x20), vcb3(0x20)
    0xcba: vcba(0x0) = CONST 
    0xcbc: vcbc = SHA3 vcba(0x0), vcb9(0x40)
    0xcbd: vcbd(0x0) = CONST 
    0xcc1: vcc1 = SLOAD vcbc
    0xcc2: vcc2 = ADD vcc1, vc54_0
    0xcc8: SSTORE vcbc, vcc2
    0xccb: vccb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xce0: vce0 = AND vccb(0xffffffffffffffffffffffffffffffffffffffff), v3ab
    0xce1: vce1(0x1aee3ddc9eba03c98b273cd914e999b78162e1ddd1c022045394f635a469e105) = CONST 
    0xd03: vd03(0x40) = CONST 
    0xd05: vd05 = MLOAD vd03(0x40)
    0xd09: MSTORE vd05, vc54_0
    0xd0a: vd0a(0x20) = CONST 
    0xd0c: vd0c = ADD vd0a(0x20), vd05
    0xd10: vd10(0x40) = CONST 
    0xd12: vd12 = MLOAD vd10(0x40)
    0xd15: vd15(0x20) = SUB vd0c, vd12
    0xd17: LOG2 vd12, vd15(0x20), vce1(0x1aee3ddc9eba03c98b273cd914e999b78162e1ddd1c022045394f635a469e105), vce0
    0xd1b: JUMP v38e(0x3c2)

    Begin block 0x3c2
    prev=[0xc76], succ=[]
    =================================
    0x3c3: STOP 

}

function isFunding()() public {
    Begin block 0x3c4
    prev=[], succ=[0x3cb, 0x3cf]
    =================================
    0x3c5: v3c5 = CALLVALUE 
    0x3c6: v3c6 = ISZERO v3c5
    0x3c7: v3c7(0x3cf) = CONST 
    0x3ca: JUMPI v3c7(0x3cf), v3c6

    Begin block 0x3cb
    prev=[0x3c4], succ=[]
    =================================
    0x3cb: v3cb(0x0) = CONST 
    0x3ce: REVERT v3cb(0x0), v3cb(0x0)

    Begin block 0x3cf
    prev=[0x3c4], succ=[0xd1c]
    =================================
    0x3d0: v3d0(0x3d7) = CONST 
    0x3d3: v3d3(0xd1c) = CONST 
    0x3d6: JUMP v3d3(0xd1c)

    Begin block 0xd1c
    prev=[0x3cf], succ=[0x3d7]
    =================================
    0xd1d: vd1d(0x5) = CONST 
    0xd1f: vd1f(0x14) = CONST 
    0xd22: vd22 = SLOAD vd1d(0x5)
    0xd24: vd24(0x100) = CONST 
    0xd27: vd27(0x10000000000000000000000000000000000000000) = EXP vd24(0x100), vd1f(0x14)
    0xd29: vd29 = DIV vd22, vd27(0x10000000000000000000000000000000000000000)
    0xd2a: vd2a(0xff) = CONST 
    0xd2c: vd2c = AND vd2a(0xff), vd29
    0xd2e: JUMP v3d0(0x3d7)

    Begin block 0x3d7
    prev=[0xd1c], succ=[]
    =================================
    0x3d8: v3d8(0x40) = CONST 
    0x3da: v3da = MLOAD v3d8(0x40)
    0x3dd: v3dd = ISZERO vd2c
    0x3de: v3de = ISZERO v3dd
    0x3df: v3df = ISZERO v3de
    0x3e0: v3e0 = ISZERO v3df
    0x3e2: MSTORE v3da, v3e0
    0x3e3: v3e3(0x20) = CONST 
    0x3e5: v3e5 = ADD v3e3(0x20), v3da
    0x3e9: v3e9(0x40) = CONST 
    0x3eb: v3eb = MLOAD v3e9(0x40)
    0x3ee: v3ee(0x20) = SUB v3e5, v3eb
    0x3f0: RETURN v3eb, v3ee(0x20)

}

function totalSupply()() public {
    Begin block 0x3f1
    prev=[], succ=[0x3f8, 0x3fc]
    =================================
    0x3f2: v3f2 = CALLVALUE 
    0x3f3: v3f3 = ISZERO v3f2
    0x3f4: v3f4(0x3fc) = CONST 
    0x3f7: JUMPI v3f4(0x3fc), v3f3

    Begin block 0x3f8
    prev=[0x3f1], succ=[]
    =================================
    0x3f8: v3f8(0x0) = CONST 
    0x3fb: REVERT v3f8(0x0), v3f8(0x0)

    Begin block 0x3fc
    prev=[0x3f1], succ=[0xd2f]
    =================================
    0x3fd: v3fd(0x404) = CONST 
    0x400: v400(0xd2f) = CONST 
    0x403: JUMP v400(0xd2f)

    Begin block 0xd2f
    prev=[0x3fc], succ=[0x404]
    =================================
    0xd30: vd30(0x0) = CONST 
    0xd32: vd32 = SLOAD vd30(0x0)
    0xd34: JUMP v3fd(0x404)

    Begin block 0x404
    prev=[0xd2f], succ=[]
    =================================
    0x405: v405(0x40) = CONST 
    0x407: v407 = MLOAD v405(0x40)
    0x40b: MSTORE v407, vd32
    0x40c: v40c(0x20) = CONST 
    0x40e: v40e = ADD v40c(0x20), v407
    0x412: v412(0x40) = CONST 
    0x414: v414 = MLOAD v412(0x40)
    0x417: v417(0x20) = SUB v40e, v414
    0x419: RETURN v414, v417(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x41a
    prev=[], succ=[0x421, 0x425]
    =================================
    0x41b: v41b = CALLVALUE 
    0x41c: v41c = ISZERO v41b
    0x41d: v41d(0x425) = CONST 
    0x420: JUMPI v41d(0x425), v41c

    Begin block 0x421
    prev=[0x41a], succ=[]
    =================================
    0x421: v421(0x0) = CONST 
    0x424: REVERT v421(0x0), v421(0x0)

    Begin block 0x425
    prev=[0x41a], succ=[0x479]
    =================================
    0x426: v426(0x479) = CONST 
    0x429: v429(0x4) = CONST 
    0x42d: v42d = CALLDATALOAD v429(0x4)
    0x42e: v42e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x443: v443 = AND v42e(0xffffffffffffffffffffffffffffffffffffffff), v42d
    0x445: v445(0x20) = CONST 
    0x447: v447(0x24) = ADD v445(0x20), v429(0x4)
    0x44c: v44c = CALLDATALOAD v447(0x24)
    0x44d: v44d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x462: v462 = AND v44d(0xffffffffffffffffffffffffffffffffffffffff), v44c
    0x464: v464(0x20) = CONST 
    0x466: v466(0x44) = ADD v464(0x20), v447(0x24)
    0x46b: v46b = CALLDATALOAD v466(0x44)
    0x46d: v46d(0x20) = CONST 
    0x46f: v46f(0x64) = ADD v46d(0x20), v466(0x44)
    0x475: v475(0xd35) = CONST 
    0x478: v478_0 = CALLPRIVATE v475(0xd35), v46b, v462, v443, v426(0x479)

    Begin block 0x479
    prev=[0x425], succ=[]
    =================================
    0x47a: v47a(0x40) = CONST 
    0x47c: v47c = MLOAD v47a(0x40)
    0x47f: v47f = ISZERO v478_0
    0x480: v480 = ISZERO v47f
    0x481: v481 = ISZERO v480
    0x482: v482 = ISZERO v481
    0x484: MSTORE v47c, v482
    0x485: v485(0x20) = CONST 
    0x487: v487 = ADD v485(0x20), v47c
    0x48b: v48b(0x40) = CONST 
    0x48d: v48d = MLOAD v48b(0x40)
    0x490: v490(0x20) = SUB v487, v48d
    0x492: RETURN v48d, v490(0x20)

}

function tokenRaised()() public {
    Begin block 0x493
    prev=[], succ=[0x49a, 0x49e]
    =================================
    0x494: v494 = CALLVALUE 
    0x495: v495 = ISZERO v494
    0x496: v496(0x49e) = CONST 
    0x499: JUMPI v496(0x49e), v495

    Begin block 0x49a
    prev=[0x493], succ=[]
    =================================
    0x49a: v49a(0x0) = CONST 
    0x49d: REVERT v49a(0x0), v49a(0x0)

    Begin block 0x49e
    prev=[0x493], succ=[0xfb1]
    =================================
    0x49f: v49f(0x4a6) = CONST 
    0x4a2: v4a2(0xfb1) = CONST 
    0x4a5: JUMP v4a2(0xfb1)

    Begin block 0xfb1
    prev=[0x49e], succ=[0x4a6]
    =================================
    0xfb2: vfb2(0x9) = CONST 
    0xfb4: vfb4 = SLOAD vfb2(0x9)
    0xfb6: JUMP v49f(0x4a6)

    Begin block 0x4a6
    prev=[0xfb1], succ=[]
    =================================
    0x4a7: v4a7(0x40) = CONST 
    0x4a9: v4a9 = MLOAD v4a7(0x40)
    0x4ad: MSTORE v4a9, vfb4
    0x4ae: v4ae(0x20) = CONST 
    0x4b0: v4b0 = ADD v4ae(0x20), v4a9
    0x4b4: v4b4(0x40) = CONST 
    0x4b6: v4b6 = MLOAD v4b4(0x40)
    0x4b9: v4b9(0x20) = SUB v4b0, v4b6
    0x4bb: RETURN v4b6, v4b9(0x20)

}

function decimals()() public {
    Begin block 0x4bc
    prev=[], succ=[0x4c3, 0x4c7]
    =================================
    0x4bd: v4bd = CALLVALUE 
    0x4be: v4be = ISZERO v4bd
    0x4bf: v4bf(0x4c7) = CONST 
    0x4c2: JUMPI v4bf(0x4c7), v4be

    Begin block 0x4c3
    prev=[0x4bc], succ=[]
    =================================
    0x4c3: v4c3(0x0) = CONST 
    0x4c6: REVERT v4c3(0x0), v4c3(0x0)

    Begin block 0x4c7
    prev=[0x4bc], succ=[0xfb7]
    =================================
    0x4c8: v4c8(0x4cf) = CONST 
    0x4cb: v4cb(0xfb7) = CONST 
    0x4ce: JUMP v4cb(0xfb7)

    Begin block 0xfb7
    prev=[0x4c7], succ=[0x4cf]
    =================================
    0xfb8: vfb8(0x12) = CONST 
    0xfbb: JUMP v4c8(0x4cf)

    Begin block 0x4cf
    prev=[0xfb7], succ=[]
    =================================
    0x4d0: v4d0(0x40) = CONST 
    0x4d2: v4d2 = MLOAD v4d0(0x40)
    0x4d6: MSTORE v4d2, vfb8(0x12)
    0x4d7: v4d7(0x20) = CONST 
    0x4d9: v4d9 = ADD v4d7(0x20), v4d2
    0x4dd: v4dd(0x40) = CONST 
    0x4df: v4df = MLOAD v4dd(0x40)
    0x4e2: v4e2(0x20) = SUB v4d9, v4df
    0x4e4: RETURN v4df, v4e2(0x20)

}

function newContractAddr()() public {
    Begin block 0x4e5
    prev=[], succ=[0x4ec, 0x4f0]
    =================================
    0x4e6: v4e6 = CALLVALUE 
    0x4e7: v4e7 = ISZERO v4e6
    0x4e8: v4e8(0x4f0) = CONST 
    0x4eb: JUMPI v4e8(0x4f0), v4e7

    Begin block 0x4ec
    prev=[0x4e5], succ=[]
    =================================
    0x4ec: v4ec(0x0) = CONST 
    0x4ef: REVERT v4ec(0x0), v4ec(0x0)

    Begin block 0x4f0
    prev=[0x4e5], succ=[0xfbc]
    =================================
    0x4f1: v4f1(0x4f8) = CONST 
    0x4f4: v4f4(0xfbc) = CONST 
    0x4f7: JUMP v4f4(0xfbc)

    Begin block 0xfbc
    prev=[0x4f0], succ=[0x4f8]
    =================================
    0xfbd: vfbd(0x5) = CONST 
    0xfbf: vfbf(0x0) = CONST 
    0xfc2: vfc2 = SLOAD vfbd(0x5)
    0xfc4: vfc4(0x100) = CONST 
    0xfc7: vfc7(0x1) = EXP vfc4(0x100), vfbf(0x0)
    0xfc9: vfc9 = DIV vfc2, vfc7(0x1)
    0xfca: vfca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfdf: vfdf = AND vfca(0xffffffffffffffffffffffffffffffffffffffff), vfc9
    0xfe1: JUMP v4f1(0x4f8)

    Begin block 0x4f8
    prev=[0xfbc], succ=[]
    =================================
    0x4f9: v4f9(0x40) = CONST 
    0x4fb: v4fb = MLOAD v4f9(0x40)
    0x4fe: v4fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x513: v513 = AND v4fe(0xffffffffffffffffffffffffffffffffffffffff), vfdf
    0x514: v514(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x529: v529 = AND v514(0xffffffffffffffffffffffffffffffffffffffff), v513
    0x52b: MSTORE v4fb, v529
    0x52c: v52c(0x20) = CONST 
    0x52e: v52e = ADD v52c(0x20), v4fb
    0x532: v532(0x40) = CONST 
    0x534: v534 = MLOAD v532(0x40)
    0x537: v537(0x20) = SUB v52e, v534
    0x539: RETURN v534, v537(0x20)

}

function tokenExchangeRate()() public {
    Begin block 0x53a
    prev=[], succ=[0x541, 0x545]
    =================================
    0x53b: v53b = CALLVALUE 
    0x53c: v53c = ISZERO v53b
    0x53d: v53d(0x545) = CONST 
    0x540: JUMPI v53d(0x545), v53c

    Begin block 0x541
    prev=[0x53a], succ=[]
    =================================
    0x541: v541(0x0) = CONST 
    0x544: REVERT v541(0x0), v541(0x0)

    Begin block 0x545
    prev=[0x53a], succ=[0xfe2]
    =================================
    0x546: v546(0x54d) = CONST 
    0x549: v549(0xfe2) = CONST 
    0x54c: JUMP v549(0xfe2)

    Begin block 0xfe2
    prev=[0x545], succ=[0x54d]
    =================================
    0xfe3: vfe3(0xb) = CONST 
    0xfe5: vfe5 = SLOAD vfe3(0xb)
    0xfe7: JUMP v546(0x54d)

    Begin block 0x54d
    prev=[0xfe2], succ=[]
    =================================
    0x54e: v54e(0x40) = CONST 
    0x550: v550 = MLOAD v54e(0x40)
    0x554: MSTORE v550, vfe5
    0x555: v555(0x20) = CONST 
    0x557: v557 = ADD v555(0x20), v550
    0x55b: v55b(0x40) = CONST 
    0x55d: v55d = MLOAD v55b(0x40)
    0x560: v560(0x20) = SUB v557, v55d
    0x562: RETURN v55d, v560(0x20)

}

function stopFunding()() public {
    Begin block 0x563
    prev=[], succ=[0x56a, 0x56e]
    =================================
    0x564: v564 = CALLVALUE 
    0x565: v565 = ISZERO v564
    0x566: v566(0x56e) = CONST 
    0x569: JUMPI v566(0x56e), v565

    Begin block 0x56a
    prev=[0x563], succ=[]
    =================================
    0x56a: v56a(0x0) = CONST 
    0x56d: REVERT v56a(0x0), v56a(0x0)

    Begin block 0x56e
    prev=[0x563], succ=[0xfe8]
    =================================
    0x56f: v56f(0x576) = CONST 
    0x572: v572(0xfe8) = CONST 
    0x575: JUMP v572(0xfe8)

    Begin block 0xfe8
    prev=[0x56e], succ=[0x1040, 0x1044]
    =================================
    0xfe9: vfe9(0x4) = CONST 
    0xfeb: vfeb(0x0) = CONST 
    0xfee: vfee = SLOAD vfe9(0x4)
    0xff0: vff0(0x100) = CONST 
    0xff3: vff3(0x1) = EXP vff0(0x100), vfeb(0x0)
    0xff5: vff5 = DIV vfee, vff3(0x1)
    0xff6: vff6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x100b: v100b = AND vff6(0xffffffffffffffffffffffffffffffffffffffff), vff5
    0x100c: v100c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1021: v1021 = AND v100c(0xffffffffffffffffffffffffffffffffffffffff), v100b
    0x1022: v1022 = CALLER 
    0x1023: v1023(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1038: v1038 = AND v1023(0xffffffffffffffffffffffffffffffffffffffff), v1022
    0x1039: v1039 = EQ v1038, v1021
    0x103a: v103a = ISZERO v1039
    0x103b: v103b = ISZERO v103a
    0x103c: v103c(0x1044) = CONST 
    0x103f: JUMPI v103c(0x1044), v103b

    Begin block 0x1040
    prev=[0xfe8], succ=[]
    =================================
    0x1040: v1040(0x0) = CONST 
    0x1043: REVERT v1040(0x0), v1040(0x0)

    Begin block 0x1044
    prev=[0xfe8], succ=[0x105b, 0x105f]
    =================================
    0x1045: v1045(0x5) = CONST 
    0x1047: v1047(0x14) = CONST 
    0x104a: v104a = SLOAD v1045(0x5)
    0x104c: v104c(0x100) = CONST 
    0x104f: v104f(0x10000000000000000000000000000000000000000) = EXP v104c(0x100), v1047(0x14)
    0x1051: v1051 = DIV v104a, v104f(0x10000000000000000000000000000000000000000)
    0x1052: v1052(0xff) = CONST 
    0x1054: v1054 = AND v1052(0xff), v1051
    0x1055: v1055 = ISZERO v1054
    0x1056: v1056 = ISZERO v1055
    0x1057: v1057(0x105f) = CONST 
    0x105a: JUMPI v1057(0x105f), v1056

    Begin block 0x105b
    prev=[0x1044], succ=[]
    =================================
    0x105b: v105b(0x0) = CONST 
    0x105e: REVERT v105b(0x0), v105b(0x0)

    Begin block 0x105f
    prev=[0x1044], succ=[0x576]
    =================================
    0x1060: v1060(0x0) = CONST 
    0x1062: v1062(0x5) = CONST 
    0x1064: v1064(0x14) = CONST 
    0x1066: v1066(0x100) = CONST 
    0x1069: v1069(0x10000000000000000000000000000000000000000) = EXP v1066(0x100), v1064(0x14)
    0x106b: v106b = SLOAD v1062(0x5)
    0x106d: v106d(0xff) = CONST 
    0x106f: v106f(0xff0000000000000000000000000000000000000000) = MUL v106d(0xff), v1069(0x10000000000000000000000000000000000000000)
    0x1070: v1070(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v106f(0xff0000000000000000000000000000000000000000)
    0x1071: v1071 = AND v1070(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v106b
    0x1074: v1074(0x1) = ISZERO v1060(0x0)
    0x1075: v1075(0x0) = ISZERO v1074(0x1)
    0x1076: v1076(0x0) = MUL v1075(0x0), v1069(0x10000000000000000000000000000000000000000)
    0x1077: v1077 = OR v1076(0x0), v1071
    0x1079: SSTORE v1062(0x5), v1077
    0x107b: JUMP v56f(0x576)

    Begin block 0x576
    prev=[0x105f], succ=[]
    =================================
    0x577: STOP 

}

function setMigrateContract(address)() public {
    Begin block 0x578
    prev=[], succ=[0x57f, 0x583]
    =================================
    0x579: v579 = CALLVALUE 
    0x57a: v57a = ISZERO v579
    0x57b: v57b(0x583) = CONST 
    0x57e: JUMPI v57b(0x583), v57a

    Begin block 0x57f
    prev=[0x578], succ=[]
    =================================
    0x57f: v57f(0x0) = CONST 
    0x582: REVERT v57f(0x0), v57f(0x0)

    Begin block 0x583
    prev=[0x578], succ=[0x107c]
    =================================
    0x584: v584(0x5af) = CONST 
    0x587: v587(0x4) = CONST 
    0x58b: v58b = CALLDATALOAD v587(0x4)
    0x58c: v58c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5a1: v5a1 = AND v58c(0xffffffffffffffffffffffffffffffffffffffff), v58b
    0x5a3: v5a3(0x20) = CONST 
    0x5a5: v5a5(0x24) = ADD v5a3(0x20), v587(0x4)
    0x5ab: v5ab(0x107c) = CONST 
    0x5ae: JUMP v5ab(0x107c)

    Begin block 0x107c
    prev=[0x583], succ=[0x10d4, 0x10d8]
    =================================
    0x107d: v107d(0x4) = CONST 
    0x107f: v107f(0x0) = CONST 
    0x1082: v1082 = SLOAD v107d(0x4)
    0x1084: v1084(0x100) = CONST 
    0x1087: v1087(0x1) = EXP v1084(0x100), v107f(0x0)
    0x1089: v1089 = DIV v1082, v1087(0x1)
    0x108a: v108a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x109f: v109f = AND v108a(0xffffffffffffffffffffffffffffffffffffffff), v1089
    0x10a0: v10a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10b5: v10b5 = AND v10a0(0xffffffffffffffffffffffffffffffffffffffff), v109f
    0x10b6: v10b6 = CALLER 
    0x10b7: v10b7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10cc: v10cc = AND v10b7(0xffffffffffffffffffffffffffffffffffffffff), v10b6
    0x10cd: v10cd = EQ v10cc, v10b5
    0x10ce: v10ce = ISZERO v10cd
    0x10cf: v10cf = ISZERO v10ce
    0x10d0: v10d0(0x10d8) = CONST 
    0x10d3: JUMPI v10d0(0x10d8), v10cf

    Begin block 0x10d4
    prev=[0x107c], succ=[]
    =================================
    0x10d4: v10d4(0x0) = CONST 
    0x10d7: REVERT v10d4(0x0), v10d4(0x0)

    Begin block 0x10d8
    prev=[0x107c], succ=[0x112f, 0x1133]
    =================================
    0x10d9: v10d9(0x5) = CONST 
    0x10db: v10db(0x0) = CONST 
    0x10de: v10de = SLOAD v10d9(0x5)
    0x10e0: v10e0(0x100) = CONST 
    0x10e3: v10e3(0x1) = EXP v10e0(0x100), v10db(0x0)
    0x10e5: v10e5 = DIV v10de, v10e3(0x1)
    0x10e6: v10e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10fb: v10fb = AND v10e6(0xffffffffffffffffffffffffffffffffffffffff), v10e5
    0x10fc: v10fc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1111: v1111 = AND v10fc(0xffffffffffffffffffffffffffffffffffffffff), v10fb
    0x1113: v1113(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1128: v1128 = AND v1113(0xffffffffffffffffffffffffffffffffffffffff), v5a1
    0x1129: v1129 = EQ v1128, v1111
    0x112a: v112a = ISZERO v1129
    0x112b: v112b(0x1133) = CONST 
    0x112e: JUMPI v112b(0x1133), v112a

    Begin block 0x112f
    prev=[0x10d8], succ=[]
    =================================
    0x112f: v112f(0x0) = CONST 
    0x1132: REVERT v112f(0x0), v112f(0x0)

    Begin block 0x1133
    prev=[0x10d8], succ=[0x5af]
    =================================
    0x1135: v1135(0x5) = CONST 
    0x1137: v1137(0x0) = CONST 
    0x1139: v1139(0x100) = CONST 
    0x113c: v113c(0x1) = EXP v1139(0x100), v1137(0x0)
    0x113e: v113e = SLOAD v1135(0x5)
    0x1140: v1140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1155: v1155(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1140(0xffffffffffffffffffffffffffffffffffffffff), v113c(0x1)
    0x1156: v1156(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1155(0xffffffffffffffffffffffffffffffffffffffff)
    0x1157: v1157 = AND v1156(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v113e
    0x115a: v115a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x116f: v116f = AND v115a(0xffffffffffffffffffffffffffffffffffffffff), v5a1
    0x1170: v1170 = MUL v116f, v113c(0x1)
    0x1171: v1171 = OR v1170, v1157
    0x1173: SSTORE v1135(0x5), v1171
    0x1176: JUMP v584(0x5af)

    Begin block 0x5af
    prev=[0x1133], succ=[]
    =================================
    0x5b0: STOP 

}

function version()() public {
    Begin block 0x5b1
    prev=[], succ=[0x5b8, 0x5bc]
    =================================
    0x5b2: v5b2 = CALLVALUE 
    0x5b3: v5b3 = ISZERO v5b2
    0x5b4: v5b4(0x5bc) = CONST 
    0x5b7: JUMPI v5b4(0x5bc), v5b3

    Begin block 0x5b8
    prev=[0x5b1], succ=[]
    =================================
    0x5b8: v5b8(0x0) = CONST 
    0x5bb: REVERT v5b8(0x0), v5b8(0x0)

    Begin block 0x5bc
    prev=[0x5b1], succ=[0x1177B0x5bc]
    =================================
    0x5bd: v5bd(0x5c4) = CONST 
    0x5c0: v5c0(0x1177) = CONST 
    0x5c3: JUMP v5c0(0x1177)

    Begin block 0x1177B0x5bc
    prev=[0x5bc], succ=[0x11c7B0x5bc, 0x18b02B0x5bc]
    =================================
    0x1178S0x5bc: v1178V5bc(0x3) = CONST 
    0x117bS0x5bc: v117bV5bc = SLOAD v1178V5bc(0x3)
    0x117cS0x5bc: v117cV5bc(0x1) = CONST 
    0x117fS0x5bc: v117fV5bc(0x1) = CONST 
    0x1181S0x5bc: v1181V5bc = AND v117fV5bc(0x1), v117bV5bc
    0x1182S0x5bc: v1182V5bc = ISZERO v1181V5bc
    0x1183S0x5bc: v1183V5bc(0x100) = CONST 
    0x1186S0x5bc: v1186V5bc = MUL v1183V5bc(0x100), v1182V5bc
    0x1187S0x5bc: v1187V5bc = SUB v1186V5bc, v117cV5bc(0x1)
    0x1188S0x5bc: v1188V5bc = AND v1187V5bc, v117bV5bc
    0x1189S0x5bc: v1189V5bc(0x2) = CONST 
    0x118cS0x5bc: v118cV5bc = DIV v1188V5bc, v1189V5bc(0x2)
    0x118eS0x5bc: v118eV5bc(0x1f) = CONST 
    0x1190S0x5bc: v1190V5bc = ADD v118eV5bc(0x1f), v118cV5bc
    0x1191S0x5bc: v1191V5bc(0x20) = CONST 
    0x1195S0x5bc: v1195V5bc = DIV v1190V5bc, v1191V5bc(0x20)
    0x1196S0x5bc: v1196V5bc = MUL v1195V5bc, v1191V5bc(0x20)
    0x1197S0x5bc: v1197V5bc(0x20) = CONST 
    0x1199S0x5bc: v1199V5bc = ADD v1197V5bc(0x20), v1196V5bc
    0x119aS0x5bc: v119aV5bc(0x40) = CONST 
    0x119cS0x5bc: v119cV5bc = MLOAD v119aV5bc(0x40)
    0x119fS0x5bc: v119fV5bc = ADD v119cV5bc, v1199V5bc
    0x11a0S0x5bc: v11a0V5bc(0x40) = CONST 
    0x11a2S0x5bc: MSTORE v11a0V5bc(0x40), v119fV5bc
    0x11a9S0x5bc: MSTORE v119cV5bc, v118cV5bc
    0x11aaS0x5bc: v11aaV5bc(0x20) = CONST 
    0x11acS0x5bc: v11acV5bc = ADD v11aaV5bc(0x20), v119cV5bc
    0x11afS0x5bc: v11afV5bc = SLOAD v1178V5bc(0x3)
    0x11b0S0x5bc: v11b0V5bc(0x1) = CONST 
    0x11b3S0x5bc: v11b3V5bc(0x1) = CONST 
    0x11b5S0x5bc: v11b5V5bc = AND v11b3V5bc(0x1), v11afV5bc
    0x11b6S0x5bc: v11b6V5bc = ISZERO v11b5V5bc
    0x11b7S0x5bc: v11b7V5bc(0x100) = CONST 
    0x11baS0x5bc: v11baV5bc = MUL v11b7V5bc(0x100), v11b6V5bc
    0x11bbS0x5bc: v11bbV5bc = SUB v11baV5bc, v11b0V5bc(0x1)
    0x11bcS0x5bc: v11bcV5bc = AND v11bbV5bc, v11afV5bc
    0x11bdS0x5bc: v11bdV5bc(0x2) = CONST 
    0x11c0S0x5bc: v11c0V5bc = DIV v11bcV5bc, v11bdV5bc(0x2)
    0x11c2S0x5bc: v11c2V5bc = ISZERO v11c0V5bc
    0x11c3S0x5bc: v11c3V5bc(0x18b02) = CONST 
    0x11c6S0x5bc: JUMPI v11c3V5bc(0x18b02), v11c2V5bc

    Begin block 0x11c7B0x5bc
    prev=[0x1177B0x5bc], succ=[0x11cfB0x5bc, 0x11e2B0x5bc]
    =================================
    0x11c8S0x5bc: v11c8V5bc(0x1f) = CONST 
    0x11caS0x5bc: v11caV5bc = LT v11c8V5bc(0x1f), v11c0V5bc
    0x11cbS0x5bc: v11cbV5bc(0x11e2) = CONST 
    0x11ceS0x5bc: JUMPI v11cbV5bc(0x11e2), v11caV5bc

    Begin block 0x11cfB0x5bc
    prev=[0x11c7B0x5bc], succ=[0x18b29B0x5bc]
    =================================
    0x11cfS0x5bc: v11cfV5bc(0x100) = CONST 
    0x11d4S0x5bc: v11d4V5bc = SLOAD v1178V5bc(0x3)
    0x11d5S0x5bc: v11d5V5bc = DIV v11d4V5bc, v11cfV5bc(0x100)
    0x11d6S0x5bc: v11d6V5bc = MUL v11d5V5bc, v11cfV5bc(0x100)
    0x11d8S0x5bc: MSTORE v11acV5bc, v11d6V5bc
    0x11daS0x5bc: v11daV5bc(0x20) = CONST 
    0x11dcS0x5bc: v11dcV5bc = ADD v11daV5bc(0x20), v11acV5bc
    0x11deS0x5bc: v11deV5bc(0x18b29) = CONST 
    0x11e1S0x5bc: JUMP v11deV5bc(0x18b29)

    Begin block 0x18b29B0x5bc
    prev=[0x11cfB0x5bc], succ=[0x5c4]
    =================================
    0x18b30S0x5bc: JUMP v5bd(0x5c4)

    Begin block 0x5c4
    prev=[0x18b02B0x5bc, 0x18b29B0x5bc, 0x18b9bB0x5bc], succ=[0x5e9]
    =================================
    0x5c5: v5c5(0x40) = CONST 
    0x5c7: v5c7 = MLOAD v5c5(0x40)
    0x5ca: v5ca(0x20) = CONST 
    0x5cc: v5cc = ADD v5ca(0x20), v5c7
    0x5cf: v5cf(0x20) = SUB v5cc, v5c7
    0x5d1: MSTORE v5c7, v5cf(0x20)
    0x5d5: v5d5 = MLOAD v119cV5bc
    0x5d7: MSTORE v5cc, v5d5
    0x5d8: v5d8(0x20) = CONST 
    0x5da: v5da = ADD v5d8(0x20), v5cc
    0x5de: v5de = MLOAD v119cV5bc
    0x5e0: v5e0(0x20) = CONST 
    0x5e2: v5e2 = ADD v5e0(0x20), v119cV5bc
    0x5e7: v5e7(0x0) = CONST 
    0x4d3e: v4d3e(0x5e9) = CONST 
    0x4d5e: JUMP v4d3e(0x5e9)

    Begin block 0x5e9
    prev=[0x5c4, 0x5f2], succ=[0x604, 0x5f2]
    =================================
    0x5e9_0x0: v5e9_0 = PHI v5e7(0x0), v5fd
    0x5ec: v5ec = LT v5e9_0, v5de
    0x5ed: v5ed = ISZERO v5ec
    0x5ee: v5ee(0x604) = CONST 
    0x5f1: JUMPI v5ee(0x604), v5ed

    Begin block 0x604
    prev=[0x5e9], succ=[0x631, 0x618]
    =================================
    0x60d: v60d = ADD v5de, v5da
    0x60f: v60f(0x1f) = CONST 
    0x611: v611 = AND v60f(0x1f), v5de
    0x613: v613 = ISZERO v611
    0x614: v614(0x631) = CONST 
    0x617: JUMPI v614(0x631), v613

    Begin block 0x631
    prev=[0x604, 0x618], succ=[]
    =================================
    0x631_0x1: v631_1 = PHI v60d, v62e
    0x637: v637(0x40) = CONST 
    0x639: v639 = MLOAD v637(0x40)
    0x63c: v63c = SUB v631_1, v639
    0x63e: RETURN v639, v63c

    Begin block 0x618
    prev=[0x604], succ=[0x631]
    =================================
    0x61a: v61a = SUB v60d, v611
    0x61c: v61c = MLOAD v61a
    0x61d: v61d(0x1) = CONST 
    0x620: v620(0x20) = CONST 
    0x622: v622 = SUB v620(0x20), v611
    0x623: v623(0x100) = CONST 
    0x626: v626 = EXP v623(0x100), v622
    0x627: v627 = SUB v626, v61d(0x1)
    0x628: v628 = NOT v627
    0x629: v629 = AND v628, v61c
    0x62b: MSTORE v61a, v629
    0x62c: v62c(0x20) = CONST 
    0x62e: v62e = ADD v62c(0x20), v61a
    0x573e: v573e(0x631) = CONST 
    0x575e: JUMP v573e(0x631)

    Begin block 0x5f2
    prev=[0x5e9], succ=[0x5e9]
    =================================
    0x5f2_0x0: v5f2_0 = PHI v5e7(0x0), v5fd
    0x5f4: v5f4 = ADD v5e2, v5f2_0
    0x5f5: v5f5 = MLOAD v5f4
    0x5f8: v5f8 = ADD v5da, v5f2_0
    0x5f9: MSTORE v5f8, v5f5
    0x5fa: v5fa(0x20) = CONST 
    0x5fd: v5fd = ADD v5f2_0, v5fa(0x20)
    0x600: v600(0x5e9) = CONST 
    0x603: JUMP v600(0x5e9)

    Begin block 0x11e2B0x5bc
    prev=[0x11c7B0x5bc], succ=[0x11f0B0x5bc]
    =================================
    0x11e4S0x5bc: v11e4V5bc = ADD v11acV5bc, v11c0V5bc
    0x11e7S0x5bc: v11e7V5bc(0x0) = CONST 
    0x11e9S0x5bc: MSTORE v11e7V5bc(0x0), v1178V5bc(0x3)
    0x11eaS0x5bc: v11eaV5bc(0x20) = CONST 
    0x11ecS0x5bc: v11ecV5bc(0x0) = CONST 
    0x11eeS0x5bc: v11eeV5bc = SHA3 v11ecV5bc(0x0), v11eaV5bc(0x20)
    0xa73eS0x5bc: va73eV5bc(0x11f0) = CONST 
    0xa75eS0x5bc: JUMP va73eV5bc(0x11f0)

    Begin block 0x11f0B0x5bc
    prev=[0x11e2B0x5bc, 0x11f0B0x5bc], succ=[0x11f0B0x5bc, 0x1204B0x5bc]
    =================================
    0x11f0_0x0S0x5bc: v11f0_0V5bc = PHI v11acV5bc, v11fcV5bc
    0x11f0_0x1S0x5bc: v11f0_1V5bc = PHI v11eeV5bc, v11f8V5bc
    0x11f2S0x5bc: v11f2V5bc = SLOAD v11f0_1V5bc
    0x11f4S0x5bc: MSTORE v11f0_0V5bc, v11f2V5bc
    0x11f6S0x5bc: v11f6V5bc(0x1) = CONST 
    0x11f8S0x5bc: v11f8V5bc = ADD v11f6V5bc(0x1), v11f0_1V5bc
    0x11faS0x5bc: v11faV5bc(0x20) = CONST 
    0x11fcS0x5bc: v11fcV5bc = ADD v11faV5bc(0x20), v11f0_0V5bc
    0x11ffS0x5bc: v11ffV5bc = GT v11e4V5bc, v11fcV5bc
    0x1200S0x5bc: v1200V5bc(0x11f0) = CONST 
    0x1203S0x5bc: JUMPI v1200V5bc(0x11f0), v11ffV5bc

    Begin block 0x1204B0x5bc
    prev=[0x11f0B0x5bc], succ=[0x18b9bB0x5bc]
    =================================
    0x1206S0x5bc: v1206V5bc = SUB v11fcV5bc, v11e4V5bc
    0x1207S0x5bc: v1207V5bc(0x1f) = CONST 
    0x1209S0x5bc: v1209V5bc = AND v1207V5bc(0x1f), v1206V5bc
    0x120bS0x5bc: v120bV5bc = ADD v11e4V5bc, v1209V5bc
    0xb13eS0x5bc: vb13eV5bc(0x18b9b) = CONST 
    0xb15eS0x5bc: JUMP vb13eV5bc(0x18b9b)

    Begin block 0x18b9bB0x5bc
    prev=[0x1204B0x5bc], succ=[0x5c4]
    =================================
    0x18ba2S0x5bc: JUMP v5bd(0x5c4)

    Begin block 0x18b02B0x5bc
    prev=[0x1177B0x5bc], succ=[0x5c4]
    =================================
    0x18b09S0x5bc: JUMP v5bd(0x5c4)

}

function tokenMigrated()() public {
    Begin block 0x63f
    prev=[], succ=[0x646, 0x64a]
    =================================
    0x640: v640 = CALLVALUE 
    0x641: v641 = ISZERO v640
    0x642: v642(0x64a) = CONST 
    0x645: JUMPI v642(0x64a), v641

    Begin block 0x646
    prev=[0x63f], succ=[]
    =================================
    0x646: v646(0x0) = CONST 
    0x649: REVERT v646(0x0), v646(0x0)

    Begin block 0x64a
    prev=[0x63f], succ=[0x1215]
    =================================
    0x64b: v64b(0x652) = CONST 
    0x64e: v64e(0x1215) = CONST 
    0x651: JUMP v64e(0x1215)

    Begin block 0x1215
    prev=[0x64a], succ=[0x652]
    =================================
    0x1216: v1216(0xa) = CONST 
    0x1218: v1218 = SLOAD v1216(0xa)
    0x121a: JUMP v64b(0x652)

    Begin block 0x652
    prev=[0x1215], succ=[]
    =================================
    0x653: v653(0x40) = CONST 
    0x655: v655 = MLOAD v653(0x40)
    0x659: MSTORE v655, v1218
    0x65a: v65a(0x20) = CONST 
    0x65c: v65c = ADD v65a(0x20), v655
    0x660: v660(0x40) = CONST 
    0x662: v662 = MLOAD v660(0x40)
    0x665: v665(0x20) = SUB v65c, v662
    0x667: RETURN v662, v665(0x20)

}

function balanceOf(address)() public {
    Begin block 0x668
    prev=[], succ=[0x66f, 0x673]
    =================================
    0x669: v669 = CALLVALUE 
    0x66a: v66a = ISZERO v669
    0x66b: v66b(0x673) = CONST 
    0x66e: JUMPI v66b(0x673), v66a

    Begin block 0x66f
    prev=[0x668], succ=[]
    =================================
    0x66f: v66f(0x0) = CONST 
    0x672: REVERT v66f(0x0), v66f(0x0)

    Begin block 0x673
    prev=[0x668], succ=[0x121b]
    =================================
    0x674: v674(0x69f) = CONST 
    0x677: v677(0x4) = CONST 
    0x67b: v67b = CALLDATALOAD v677(0x4)
    0x67c: v67c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x691: v691 = AND v67c(0xffffffffffffffffffffffffffffffffffffffff), v67b
    0x693: v693(0x20) = CONST 
    0x695: v695(0x24) = ADD v693(0x20), v677(0x4)
    0x69b: v69b(0x121b) = CONST 
    0x69e: JUMP v69b(0x121b)

    Begin block 0x121b
    prev=[0x673], succ=[0x69f]
    =================================
    0x121c: v121c(0x0) = CONST 
    0x121e: v121e(0x1) = CONST 
    0x1220: v1220(0x0) = CONST 
    0x1223: v1223(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1238: v1238 = AND v1223(0xffffffffffffffffffffffffffffffffffffffff), v691
    0x1239: v1239(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x124e: v124e = AND v1239(0xffffffffffffffffffffffffffffffffffffffff), v1238
    0x1250: MSTORE v1220(0x0), v124e
    0x1251: v1251(0x20) = CONST 
    0x1253: v1253(0x20) = ADD v1251(0x20), v1220(0x0)
    0x1256: MSTORE v1253(0x20), v121e(0x1)
    0x1257: v1257(0x20) = CONST 
    0x1259: v1259(0x40) = ADD v1257(0x20), v1253(0x20)
    0x125a: v125a(0x0) = CONST 
    0x125c: v125c = SHA3 v125a(0x0), v1259(0x40)
    0x125d: v125d = SLOAD v125c
    0x1263: JUMP v674(0x69f)

    Begin block 0x69f
    prev=[0x121b], succ=[]
    =================================
    0x6a0: v6a0(0x40) = CONST 
    0x6a2: v6a2 = MLOAD v6a0(0x40)
    0x6a6: MSTORE v6a2, v125d
    0x6a7: v6a7(0x20) = CONST 
    0x6a9: v6a9 = ADD v6a7(0x20), v6a2
    0x6ad: v6ad(0x40) = CONST 
    0x6af: v6af = MLOAD v6ad(0x40)
    0x6b2: v6b2(0x20) = SUB v6a9, v6af
    0x6b4: RETURN v6af, v6b2(0x20)

}

function currentSupply()() public {
    Begin block 0x6b5
    prev=[], succ=[0x6bc, 0x6c0]
    =================================
    0x6b6: v6b6 = CALLVALUE 
    0x6b7: v6b7 = ISZERO v6b6
    0x6b8: v6b8(0x6c0) = CONST 
    0x6bb: JUMPI v6b8(0x6c0), v6b7

    Begin block 0x6bc
    prev=[0x6b5], succ=[]
    =================================
    0x6bc: v6bc(0x0) = CONST 
    0x6bf: REVERT v6bc(0x0), v6bc(0x0)

    Begin block 0x6c0
    prev=[0x6b5], succ=[0x1264]
    =================================
    0x6c1: v6c1(0x6c8) = CONST 
    0x6c4: v6c4(0x1264) = CONST 
    0x6c7: JUMP v6c4(0x1264)

    Begin block 0x1264
    prev=[0x6c0], succ=[0x6c8]
    =================================
    0x1265: v1265(0x8) = CONST 
    0x1267: v1267 = SLOAD v1265(0x8)
    0x1269: JUMP v6c1(0x6c8)

    Begin block 0x6c8
    prev=[0x1264], succ=[]
    =================================
    0x6c9: v6c9(0x40) = CONST 
    0x6cb: v6cb = MLOAD v6c9(0x40)
    0x6cf: MSTORE v6cb, v1267
    0x6d0: v6d0(0x20) = CONST 
    0x6d2: v6d2 = ADD v6d0(0x20), v6cb
    0x6d6: v6d6(0x40) = CONST 
    0x6d8: v6d8 = MLOAD v6d6(0x40)
    0x6db: v6db(0x20) = SUB v6d2, v6d8
    0x6dd: RETURN v6d8, v6db(0x20)

}

function startFunding(uint256,uint256)() public {
    Begin block 0x6de
    prev=[], succ=[0x6e5, 0x6e9]
    =================================
    0x6df: v6df = CALLVALUE 
    0x6e0: v6e0 = ISZERO v6df
    0x6e1: v6e1(0x6e9) = CONST 
    0x6e4: JUMPI v6e1(0x6e9), v6e0

    Begin block 0x6e5
    prev=[0x6de], succ=[]
    =================================
    0x6e5: v6e5(0x0) = CONST 
    0x6e8: REVERT v6e5(0x0), v6e5(0x0)

    Begin block 0x6e9
    prev=[0x6de], succ=[0x126a]
    =================================
    0x6ea: v6ea(0x708) = CONST 
    0x6ed: v6ed(0x4) = CONST 
    0x6f1: v6f1 = CALLDATALOAD v6ed(0x4)
    0x6f3: v6f3(0x20) = CONST 
    0x6f5: v6f5(0x24) = ADD v6f3(0x20), v6ed(0x4)
    0x6fa: v6fa = CALLDATALOAD v6f5(0x24)
    0x6fc: v6fc(0x20) = CONST 
    0x6fe: v6fe(0x44) = ADD v6fc(0x20), v6f5(0x24)
    0x704: v704(0x126a) = CONST 
    0x707: JUMP v704(0x126a)

    Begin block 0x126a
    prev=[0x6e9], succ=[0x12c2, 0x12c6]
    =================================
    0x126b: v126b(0x4) = CONST 
    0x126d: v126d(0x0) = CONST 
    0x1270: v1270 = SLOAD v126b(0x4)
    0x1272: v1272(0x100) = CONST 
    0x1275: v1275(0x1) = EXP v1272(0x100), v126d(0x0)
    0x1277: v1277 = DIV v1270, v1275(0x1)
    0x1278: v1278(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x128d: v128d = AND v1278(0xffffffffffffffffffffffffffffffffffffffff), v1277
    0x128e: v128e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12a3: v12a3 = AND v128e(0xffffffffffffffffffffffffffffffffffffffff), v128d
    0x12a4: v12a4 = CALLER 
    0x12a5: v12a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12ba: v12ba = AND v12a5(0xffffffffffffffffffffffffffffffffffffffff), v12a4
    0x12bb: v12bb = EQ v12ba, v12a3
    0x12bc: v12bc = ISZERO v12bb
    0x12bd: v12bd = ISZERO v12bc
    0x12be: v12be(0x12c6) = CONST 
    0x12c1: JUMPI v12be(0x12c6), v12bd

    Begin block 0x12c2
    prev=[0x126a], succ=[]
    =================================
    0x12c2: v12c2(0x0) = CONST 
    0x12c5: REVERT v12c2(0x0), v12c2(0x0)

    Begin block 0x12c6
    prev=[0x126a], succ=[0x12dc, 0x12e0]
    =================================
    0x12c7: v12c7(0x5) = CONST 
    0x12c9: v12c9(0x14) = CONST 
    0x12cc: v12cc = SLOAD v12c7(0x5)
    0x12ce: v12ce(0x100) = CONST 
    0x12d1: v12d1(0x10000000000000000000000000000000000000000) = EXP v12ce(0x100), v12c9(0x14)
    0x12d3: v12d3 = DIV v12cc, v12d1(0x10000000000000000000000000000000000000000)
    0x12d4: v12d4(0xff) = CONST 
    0x12d6: v12d6 = AND v12d4(0xff), v12d3
    0x12d7: v12d7 = ISZERO v12d6
    0x12d8: v12d8(0x12e0) = CONST 
    0x12db: JUMPI v12d8(0x12e0), v12d7

    Begin block 0x12dc
    prev=[0x12c6], succ=[]
    =================================
    0x12dc: v12dc(0x0) = CONST 
    0x12df: REVERT v12dc(0x0), v12dc(0x0)

    Begin block 0x12e0
    prev=[0x12c6], succ=[0x12ea, 0x12ee]
    =================================
    0x12e3: v12e3 = LT v6f1, v6fa
    0x12e4: v12e4 = ISZERO v12e3
    0x12e5: v12e5 = ISZERO v12e4
    0x12e6: v12e6(0x12ee) = CONST 
    0x12e9: JUMPI v12e6(0x12ee), v12e5

    Begin block 0x12ea
    prev=[0x12e0], succ=[]
    =================================
    0x12ea: v12ea(0x0) = CONST 
    0x12ed: REVERT v12ea(0x0), v12ea(0x0)

    Begin block 0x12ee
    prev=[0x12e0], succ=[0x12f8, 0x12fc]
    =================================
    0x12f0: v12f0 = NUMBER 
    0x12f1: v12f1 = LT v12f0, v6f1
    0x12f2: v12f2 = ISZERO v12f1
    0x12f3: v12f3 = ISZERO v12f2
    0x12f4: v12f4(0x12fc) = CONST 
    0x12f7: JUMPI v12f4(0x12fc), v12f3

    Begin block 0x12f8
    prev=[0x12ee], succ=[]
    =================================
    0x12f8: v12f8(0x0) = CONST 
    0x12fb: REVERT v12f8(0x0), v12f8(0x0)

    Begin block 0x12fc
    prev=[0x12ee], succ=[0x708]
    =================================
    0x12fe: v12fe(0x6) = CONST 
    0x1302: SSTORE v12fe(0x6), v6f1
    0x1305: v1305(0x7) = CONST 
    0x1309: SSTORE v1305(0x7), v6fa
    0x130b: v130b(0x1) = CONST 
    0x130d: v130d(0x5) = CONST 
    0x130f: v130f(0x14) = CONST 
    0x1311: v1311(0x100) = CONST 
    0x1314: v1314(0x10000000000000000000000000000000000000000) = EXP v1311(0x100), v130f(0x14)
    0x1316: v1316 = SLOAD v130d(0x5)
    0x1318: v1318(0xff) = CONST 
    0x131a: v131a(0xff0000000000000000000000000000000000000000) = MUL v1318(0xff), v1314(0x10000000000000000000000000000000000000000)
    0x131b: v131b(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v131a(0xff0000000000000000000000000000000000000000)
    0x131c: v131c = AND v131b(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1316
    0x131f: v131f(0x0) = ISZERO v130b(0x1)
    0x1320: v1320(0x1) = ISZERO v131f(0x0)
    0x1321: v1321(0x10000000000000000000000000000000000000000) = MUL v1320(0x1), v1314(0x10000000000000000000000000000000000000000)
    0x1322: v1322 = OR v1321(0x10000000000000000000000000000000000000000), v131c
    0x1324: SSTORE v130d(0x5), v1322
    0x1328: JUMP v6ea(0x708)

    Begin block 0x708
    prev=[0x12fc], succ=[]
    =================================
    0x709: STOP 

}

function mintToken(address,uint256)() public {
    Begin block 0x70a
    prev=[], succ=[0x711, 0x715]
    =================================
    0x70b: v70b = CALLVALUE 
    0x70c: v70c = ISZERO v70b
    0x70d: v70d(0x715) = CONST 
    0x710: JUMPI v70d(0x715), v70c

    Begin block 0x711
    prev=[0x70a], succ=[]
    =================================
    0x711: v711(0x0) = CONST 
    0x714: REVERT v711(0x0), v711(0x0)

    Begin block 0x715
    prev=[0x70a], succ=[0x1329B0x715]
    =================================
    0x716: v716(0x74a) = CONST 
    0x719: v719(0x4) = CONST 
    0x71d: v71d = CALLDATALOAD v719(0x4)
    0x71e: v71e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x733: v733 = AND v71e(0xffffffffffffffffffffffffffffffffffffffff), v71d
    0x735: v735(0x20) = CONST 
    0x737: v737(0x24) = ADD v735(0x20), v719(0x4)
    0x73c: v73c = CALLDATALOAD v737(0x24)
    0x73e: v73e(0x20) = CONST 
    0x740: v740(0x44) = ADD v73e(0x20), v737(0x24)
    0x746: v746(0x1329) = CONST 
    0x749: JUMP v746(0x1329)

    Begin block 0x1329B0x715
    prev=[0x715], succ=[0x1366B0x715]
    =================================
    0x132bS0x715: v132bV715(0x0) = CONST 
    0x1330S0x715: v1330V715 = SLOAD v132bV715(0x0)
    0x1331S0x715: v1331V715 = ADD v1330V715, v73c
    0x1337S0x715: SSTORE v132bV715(0x0), v1331V715
    0x1339S0x715: v1339V715(0x1366) = CONST 
    0x133cS0x715: v133cV715(0x0) = CONST 
    0x133eS0x715: v133eV715(0x4) = CONST 
    0x1340S0x715: v1340V715(0x0) = CONST 
    0x1343S0x715: v1343V715 = SLOAD v133eV715(0x4)
    0x1345S0x715: v1345V715(0x100) = CONST 
    0x1348S0x715: v1348V715(0x1) = EXP v1345V715(0x100), v1340V715(0x0)
    0x134aS0x715: v134aV715 = DIV v1343V715, v1348V715(0x1)
    0x134bS0x715: v134bV715(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1360S0x715: v1360V715 = AND v134bV715(0xffffffffffffffffffffffffffffffffffffffff), v134aV715
    0x1362S0x715: v1362V715(0xd35) = CONST 
    0x1365S0x715: v1365_0V715 = CALLPRIVATE v1362V715(0xd35), v73c, v1360V715, v133cV715(0x0), v1339V715(0x1366)

    Begin block 0x1366B0x715
    prev=[0x1329B0x715], succ=[0x1394B0x715]
    =================================
    0x1368S0x715: v1368V715(0x1394) = CONST 
    0x136bS0x715: v136bV715(0x4) = CONST 
    0x136dS0x715: v136dV715(0x0) = CONST 
    0x1370S0x715: v1370V715 = SLOAD v136bV715(0x4)
    0x1372S0x715: v1372V715(0x100) = CONST 
    0x1375S0x715: v1375V715(0x1) = EXP v1372V715(0x100), v136dV715(0x0)
    0x1377S0x715: v1377V715 = DIV v1370V715, v1375V715(0x1)
    0x1378S0x715: v1378V715(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x138dS0x715: v138dV715 = AND v1378V715(0xffffffffffffffffffffffffffffffffffffffff), v1377V715
    0x1390S0x715: v1390V715(0xd35) = CONST 
    0x1393S0x715: v1393_0V715 = CALLPRIVATE v1390V715(0xd35), v73c, v733, v138dV715, v1368V715(0x1394)

    Begin block 0x1394B0x715
    prev=[0x1366B0x715], succ=[0x74a]
    =================================
    0x1398S0x715: JUMP v716(0x74a)

    Begin block 0x74a
    prev=[0x1394B0x715], succ=[]
    =================================
    0x74b: STOP 

}

function migrate()() public {
    Begin block 0x74c
    prev=[], succ=[0x753, 0x757]
    =================================
    0x74d: v74d = CALLVALUE 
    0x74e: v74e = ISZERO v74d
    0x74f: v74f(0x757) = CONST 
    0x752: JUMPI v74f(0x757), v74e

    Begin block 0x753
    prev=[0x74c], succ=[]
    =================================
    0x753: v753(0x0) = CONST 
    0x756: REVERT v753(0x0), v753(0x0)

    Begin block 0x757
    prev=[0x74c], succ=[0x1399]
    =================================
    0x758: v758(0x75f) = CONST 
    0x75b: v75b(0x1399) = CONST 
    0x75e: JUMP v75b(0x1399)

    Begin block 0x1399
    prev=[0x757], succ=[0x13b2, 0x13b6]
    =================================
    0x139a: v139a(0x0) = CONST 
    0x139d: v139d(0x5) = CONST 
    0x139f: v139f(0x14) = CONST 
    0x13a2: v13a2 = SLOAD v139d(0x5)
    0x13a4: v13a4(0x100) = CONST 
    0x13a7: v13a7(0x10000000000000000000000000000000000000000) = EXP v13a4(0x100), v139f(0x14)
    0x13a9: v13a9 = DIV v13a2, v13a7(0x10000000000000000000000000000000000000000)
    0x13aa: v13aa(0xff) = CONST 
    0x13ac: v13ac = AND v13aa(0xff), v13a9
    0x13ad: v13ad = ISZERO v13ac
    0x13ae: v13ae(0x13b6) = CONST 
    0x13b1: JUMPI v13ae(0x13b6), v13ad

    Begin block 0x13b2
    prev=[0x1399], succ=[]
    =================================
    0x13b2: v13b2(0x0) = CONST 
    0x13b5: REVERT v13b2(0x0), v13b2(0x0)

    Begin block 0x13b6
    prev=[0x1399], succ=[0x140e, 0x1412]
    =================================
    0x13b7: v13b7(0x0) = CONST 
    0x13b9: v13b9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13ce: v13ce(0x0) = AND v13b9(0xffffffffffffffffffffffffffffffffffffffff), v13b7(0x0)
    0x13cf: v13cf(0x5) = CONST 
    0x13d1: v13d1(0x0) = CONST 
    0x13d4: v13d4 = SLOAD v13cf(0x5)
    0x13d6: v13d6(0x100) = CONST 
    0x13d9: v13d9(0x1) = EXP v13d6(0x100), v13d1(0x0)
    0x13db: v13db = DIV v13d4, v13d9(0x1)
    0x13dc: v13dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13f1: v13f1 = AND v13dc(0xffffffffffffffffffffffffffffffffffffffff), v13db
    0x13f2: v13f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1407: v1407 = AND v13f2(0xffffffffffffffffffffffffffffffffffffffff), v13f1
    0x1408: v1408 = EQ v1407, v13ce(0x0)
    0x1409: v1409 = ISZERO v1408
    0x140a: v140a(0x1412) = CONST 
    0x140d: JUMPI v140a(0x1412), v1409

    Begin block 0x140e
    prev=[0x13b6], succ=[]
    =================================
    0x140e: v140e(0x0) = CONST 
    0x1411: REVERT v140e(0x0), v140e(0x0)

    Begin block 0x1412
    prev=[0x13b6], succ=[0x145e, 0x1462]
    =================================
    0x1413: v1413(0x1) = CONST 
    0x1415: v1415(0x0) = CONST 
    0x1417: v1417 = CALLER 
    0x1418: v1418(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x142d: v142d = AND v1418(0xffffffffffffffffffffffffffffffffffffffff), v1417
    0x142e: v142e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1443: v1443 = AND v142e(0xffffffffffffffffffffffffffffffffffffffff), v142d
    0x1445: MSTORE v1415(0x0), v1443
    0x1446: v1446(0x20) = CONST 
    0x1448: v1448(0x20) = ADD v1446(0x20), v1415(0x0)
    0x144b: MSTORE v1448(0x20), v1413(0x1)
    0x144c: v144c(0x20) = CONST 
    0x144e: v144e(0x40) = ADD v144c(0x20), v1448(0x20)
    0x144f: v144f(0x0) = CONST 
    0x1451: v1451 = SHA3 v144f(0x0), v144e(0x40)
    0x1452: v1452 = SLOAD v1451
    0x1455: v1455(0x0) = CONST 
    0x1458: v1458 = EQ v1452, v1455(0x0)
    0x1459: v1459 = ISZERO v1458
    0x145a: v145a(0x1462) = CONST 
    0x145d: JUMPI v145a(0x1462), v1459

    Begin block 0x145e
    prev=[0x1412], succ=[]
    =================================
    0x145e: v145e(0x0) = CONST 
    0x1461: REVERT v145e(0x0), v145e(0x0)

    Begin block 0x1462
    prev=[0x1412], succ=[0x14b3]
    =================================
    0x1463: v1463(0x0) = CONST 
    0x1465: v1465(0x1) = CONST 
    0x1467: v1467(0x0) = CONST 
    0x1469: v1469 = CALLER 
    0x146a: v146a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x147f: v147f = AND v146a(0xffffffffffffffffffffffffffffffffffffffff), v1469
    0x1480: v1480(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1495: v1495 = AND v1480(0xffffffffffffffffffffffffffffffffffffffff), v147f
    0x1497: MSTORE v1467(0x0), v1495
    0x1498: v1498(0x20) = CONST 
    0x149a: v149a(0x20) = ADD v1498(0x20), v1467(0x0)
    0x149d: MSTORE v149a(0x20), v1465(0x1)
    0x149e: v149e(0x20) = CONST 
    0x14a0: v14a0(0x40) = ADD v149e(0x20), v149a(0x20)
    0x14a1: v14a1(0x0) = CONST 
    0x14a3: v14a3 = SHA3 v14a1(0x0), v14a0(0x40)
    0x14a6: SSTORE v14a3, v1463(0x0)
    0x14a8: v14a8(0x14b3) = CONST 
    0x14ab: v14ab(0xa) = CONST 
    0x14ad: v14ad = SLOAD v14ab(0xa)
    0x14af: v14af(0xa46) = CONST 
    0x14b2: v14b2_0 = CALLPRIVATE v14af(0xa46), v1452, v14ad, v14a8(0x14b3)

    Begin block 0x14b3
    prev=[0x1462], succ=[0x157c, 0x1580]
    =================================
    0x14b4: v14b4(0xa) = CONST 
    0x14b8: SSTORE v14b4(0xa), v14b2_0
    0x14ba: v14ba(0x5) = CONST 
    0x14bc: v14bc(0x0) = CONST 
    0x14bf: v14bf = SLOAD v14ba(0x5)
    0x14c1: v14c1(0x100) = CONST 
    0x14c4: v14c4(0x1) = EXP v14c1(0x100), v14bc(0x0)
    0x14c6: v14c6 = DIV v14bf, v14c4(0x1)
    0x14c7: v14c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14dc: v14dc = AND v14c7(0xffffffffffffffffffffffffffffffffffffffff), v14c6
    0x14e0: v14e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14f5: v14f5 = AND v14e0(0xffffffffffffffffffffffffffffffffffffffff), v14dc
    0x14f6: v14f6(0xad68ebf7) = CONST 
    0x14fb: v14fb = CALLER 
    0x14fd: v14fd(0x40) = CONST 
    0x14ff: v14ff = MLOAD v14fd(0x40)
    0x1501: v1501(0xffffffff) = CONST 
    0x1506: v1506(0xad68ebf7) = AND v1501(0xffffffff), v14f6(0xad68ebf7)
    0x1507: v1507(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x1525: v1525(0xad68ebf700000000000000000000000000000000000000000000000000000000) = MUL v1507(0x100000000000000000000000000000000000000000000000000000000), v1506(0xad68ebf7)
    0x1527: MSTORE v14ff, v1525(0xad68ebf700000000000000000000000000000000000000000000000000000000)
    0x1528: v1528(0x4) = CONST 
    0x152a: v152a = ADD v1528(0x4), v14ff
    0x152d: v152d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1542: v1542 = AND v152d(0xffffffffffffffffffffffffffffffffffffffff), v14fb
    0x1543: v1543(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1558: v1558 = AND v1543(0xffffffffffffffffffffffffffffffffffffffff), v1542
    0x155a: MSTORE v152a, v1558
    0x155b: v155b(0x20) = CONST 
    0x155d: v155d = ADD v155b(0x20), v152a
    0x1560: MSTORE v155d, v1452
    0x1561: v1561(0x20) = CONST 
    0x1563: v1563 = ADD v1561(0x20), v155d
    0x1568: v1568(0x20) = CONST 
    0x156a: v156a(0x40) = CONST 
    0x156c: v156c = MLOAD v156a(0x40)
    0x156f: v156f(0x44) = SUB v1563, v156c
    0x1571: v1571(0x0) = CONST 
    0x1575: v1575 = EXTCODESIZE v14f5
    0x1576: v1576 = ISZERO v1575
    0x1577: v1577 = ISZERO v1576
    0x1578: v1578(0x1580) = CONST 
    0x157b: JUMPI v1578(0x1580), v1577

    Begin block 0x157c
    prev=[0x14b3], succ=[]
    =================================
    0x157c: v157c(0x0) = CONST 
    0x157f: REVERT v157c(0x0), v157c(0x0)

    Begin block 0x1580
    prev=[0x14b3], succ=[0x1589, 0x158d]
    =================================
    0x1581: v1581 = GAS 
    0x1582: v1582 = CALL v1581, v14f5, v1571(0x0), v156c, v156f(0x44), v156c, v1568(0x20)
    0x1583: v1583 = ISZERO v1582
    0x1584: v1584 = ISZERO v1583
    0x1585: v1585(0x158d) = CONST 
    0x1588: JUMPI v1585(0x158d), v1584

    Begin block 0x1589
    prev=[0x1580], succ=[]
    =================================
    0x1589: v1589(0x0) = CONST 
    0x158c: REVERT v1589(0x0), v1589(0x0)

    Begin block 0x158d
    prev=[0x1580], succ=[0x159e, 0x15a2]
    =================================
    0x1591: v1591(0x40) = CONST 
    0x1593: v1593 = MLOAD v1591(0x40)
    0x1595: v1595 = MLOAD v1593
    0x1598: v1598 = ISZERO v1595
    0x1599: v1599 = ISZERO v1598
    0x159a: v159a(0x15a2) = CONST 
    0x159d: JUMPI v159a(0x15a2), v1599

    Begin block 0x159e
    prev=[0x158d], succ=[]
    =================================
    0x159e: v159e(0x0) = CONST 
    0x15a1: REVERT v159e(0x0), v159e(0x0)

    Begin block 0x15a2
    prev=[0x158d], succ=[0x75f]
    =================================
    0x15a3: v15a3 = CALLER 
    0x15a4: v15a4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15b9: v15b9 = AND v15a4(0xffffffffffffffffffffffffffffffffffffffff), v15a3
    0x15ba: v15ba(0xa59785389b00cbd19745afbe8d59b28e3161395c6b1e3525861a2b0dede0b90d) = CONST 
    0x15dc: v15dc(0x40) = CONST 
    0x15de: v15de = MLOAD v15dc(0x40)
    0x15e2: MSTORE v15de, v1452
    0x15e3: v15e3(0x20) = CONST 
    0x15e5: v15e5 = ADD v15e3(0x20), v15de
    0x15e9: v15e9(0x40) = CONST 
    0x15eb: v15eb = MLOAD v15e9(0x40)
    0x15ee: v15ee(0x20) = SUB v15e5, v15eb
    0x15f0: LOG2 v15eb, v15ee(0x20), v15ba(0xa59785389b00cbd19745afbe8d59b28e3161395c6b1e3525861a2b0dede0b90d), v15b9
    0x15f3: JUMP v758(0x75f)

    Begin block 0x75f
    prev=[0x15a2], succ=[]
    =================================
    0x760: STOP 

}

function symbol()() public {
    Begin block 0x761
    prev=[], succ=[0x768, 0x76c]
    =================================
    0x762: v762 = CALLVALUE 
    0x763: v763 = ISZERO v762
    0x764: v764(0x76c) = CONST 
    0x767: JUMPI v764(0x76c), v763

    Begin block 0x768
    prev=[0x761], succ=[]
    =================================
    0x768: v768(0x0) = CONST 
    0x76b: REVERT v768(0x0), v768(0x0)

    Begin block 0x76c
    prev=[0x761], succ=[0x15f4]
    =================================
    0x76d: v76d(0x774) = CONST 
    0x770: v770(0x15f4) = CONST 
    0x773: JUMP v770(0x15f4)

    Begin block 0x15f4
    prev=[0x76c], succ=[0x774]
    =================================
    0x15f5: v15f5(0x40) = CONST 
    0x15f8: v15f8 = MLOAD v15f5(0x40)
    0x15fb: v15fb = ADD v15f8, v15f5(0x40)
    0x15fc: v15fc(0x40) = CONST 
    0x15fe: MSTORE v15fc(0x40), v15fb
    0x1600: v1600(0x5) = CONST 
    0x1603: MSTORE v15f8, v1600(0x5)
    0x1604: v1604(0x20) = CONST 
    0x1606: v1606 = ADD v1604(0x20), v15f8
    0x1607: v1607(0x61636f696e000000000000000000000000000000000000000000000000000000) = CONST 
    0x1629: MSTORE v1606, v1607(0x61636f696e000000000000000000000000000000000000000000000000000000)
    0x162c: JUMP v76d(0x774)

    Begin block 0x774
    prev=[0x15f4], succ=[0x799]
    =================================
    0x775: v775(0x40) = CONST 
    0x777: v777 = MLOAD v775(0x40)
    0x77a: v77a(0x20) = CONST 
    0x77c: v77c = ADD v77a(0x20), v777
    0x77f: v77f(0x20) = SUB v77c, v777
    0x781: MSTORE v777, v77f(0x20)
    0x785: v785(0x5) = MLOAD v15f8
    0x787: MSTORE v77c, v785(0x5)
    0x788: v788(0x20) = CONST 
    0x78a: v78a = ADD v788(0x20), v77c
    0x78e: v78e(0x5) = MLOAD v15f8
    0x790: v790(0x20) = CONST 
    0x792: v792 = ADD v790(0x20), v15f8
    0x797: v797(0x0) = CONST 
    0x613e: v613e(0x799) = CONST 
    0x615e: JUMP v613e(0x799)

    Begin block 0x799
    prev=[0x774, 0x7a2], succ=[0x7b4, 0x7a2]
    =================================
    0x799_0x0: v799_0 = PHI v797(0x0), v7ad
    0x79c: v79c = LT v799_0, v78e(0x5)
    0x79d: v79d = ISZERO v79c
    0x79e: v79e(0x7b4) = CONST 
    0x7a1: JUMPI v79e(0x7b4), v79d

    Begin block 0x7b4
    prev=[0x799], succ=[0x7e1, 0x7c8]
    =================================
    0x7bd: v7bd = ADD v78e(0x5), v78a
    0x7bf: v7bf(0x1f) = CONST 
    0x7c1: v7c1(0x5) = AND v7bf(0x1f), v78e(0x5)
    0x7c3: v7c3(0x0) = ISZERO v7c1(0x5)
    0x7c4: v7c4(0x7e1) = CONST 
    0x7c7: JUMPI v7c4(0x7e1), v7c3(0x0)

    Begin block 0x7e1
    prev=[0x7b4, 0x7c8], succ=[]
    =================================
    0x7e1_0x1: v7e1_1 = PHI v7bd, v7de
    0x7e7: v7e7(0x40) = CONST 
    0x7e9: v7e9 = MLOAD v7e7(0x40)
    0x7ec: v7ec = SUB v7e1_1, v7e9
    0x7ee: RETURN v7e9, v7ec

    Begin block 0x7c8
    prev=[0x7b4], succ=[0x7e1]
    =================================
    0x7ca: v7ca = SUB v7bd, v7c1(0x5)
    0x7cc: v7cc = MLOAD v7ca
    0x7cd: v7cd(0x1) = CONST 
    0x7d0: v7d0(0x20) = CONST 
    0x7d2: v7d2(0x1b) = SUB v7d0(0x20), v7c1(0x5)
    0x7d3: v7d3(0x100) = CONST 
    0x7d6: v7d6(0x1000000000000000000000000000000000000000000000000000000) = EXP v7d3(0x100), v7d2(0x1b)
    0x7d7: v7d7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v7d6(0x1000000000000000000000000000000000000000000000000000000), v7cd(0x1)
    0x7d8: v7d8(0xffffffffff000000000000000000000000000000000000000000000000000000) = NOT v7d7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x7d9: v7d9 = AND v7d8(0xffffffffff000000000000000000000000000000000000000000000000000000), v7cc
    0x7db: MSTORE v7ca, v7d9
    0x7dc: v7dc(0x20) = CONST 
    0x7de: v7de = ADD v7dc(0x20), v7ca
    0x6b3e: v6b3e(0x7e1) = CONST 
    0x6b5e: JUMP v6b3e(0x7e1)

    Begin block 0x7a2
    prev=[0x799], succ=[0x799]
    =================================
    0x7a2_0x0: v7a2_0 = PHI v797(0x0), v7ad
    0x7a4: v7a4 = ADD v792, v7a2_0
    0x7a5: v7a5 = MLOAD v7a4
    0x7a8: v7a8 = ADD v78a, v7a2_0
    0x7a9: MSTORE v7a8, v7a5
    0x7aa: v7aa(0x20) = CONST 
    0x7ad: v7ad = ADD v7a2_0, v7aa(0x20)
    0x7b0: v7b0(0x799) = CONST 
    0x7b3: JUMP v7b0(0x799)

}

function decreaseSupply(uint256)() public {
    Begin block 0x7ef
    prev=[], succ=[0x7f6, 0x7fa]
    =================================
    0x7f0: v7f0 = CALLVALUE 
    0x7f1: v7f1 = ISZERO v7f0
    0x7f2: v7f2(0x7fa) = CONST 
    0x7f5: JUMPI v7f2(0x7fa), v7f1

    Begin block 0x7f6
    prev=[0x7ef], succ=[]
    =================================
    0x7f6: v7f6(0x0) = CONST 
    0x7f9: REVERT v7f6(0x0), v7f6(0x0)

    Begin block 0x7fa
    prev=[0x7ef], succ=[0x162d]
    =================================
    0x7fb: v7fb(0x810) = CONST 
    0x7fe: v7fe(0x4) = CONST 
    0x802: v802 = CALLDATALOAD v7fe(0x4)
    0x804: v804(0x20) = CONST 
    0x806: v806(0x24) = ADD v804(0x20), v7fe(0x4)
    0x80c: v80c(0x162d) = CONST 
    0x80f: JUMP v80c(0x162d)

    Begin block 0x162d
    prev=[0x7fa], succ=[0x1687, 0x168b]
    =================================
    0x162e: v162e(0x0) = CONST 
    0x1630: v1630(0x4) = CONST 
    0x1632: v1632(0x0) = CONST 
    0x1635: v1635 = SLOAD v1630(0x4)
    0x1637: v1637(0x100) = CONST 
    0x163a: v163a(0x1) = EXP v1637(0x100), v1632(0x0)
    0x163c: v163c = DIV v1635, v163a(0x1)
    0x163d: v163d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1652: v1652 = AND v163d(0xffffffffffffffffffffffffffffffffffffffff), v163c
    0x1653: v1653(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1668: v1668 = AND v1653(0xffffffffffffffffffffffffffffffffffffffff), v1652
    0x1669: v1669 = CALLER 
    0x166a: v166a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x167f: v167f = AND v166a(0xffffffffffffffffffffffffffffffffffffffff), v1669
    0x1680: v1680 = EQ v167f, v1668
    0x1681: v1681 = ISZERO v1680
    0x1682: v1682 = ISZERO v1681
    0x1683: v1683(0x168b) = CONST 
    0x1686: JUMPI v1683(0x168b), v1682

    Begin block 0x1687
    prev=[0x162d], succ=[]
    =================================
    0x1687: v1687(0x0) = CONST 
    0x168a: REVERT v1687(0x0), v1687(0x0)

    Begin block 0x168b
    prev=[0x162d], succ=[0x1c3aB0x168b]
    =================================
    0x168c: v168c(0x1694) = CONST 
    0x1690: v1690(0x1c3a) = CONST 
    0x1693: JUMP v1690(0x1c3a)

    Begin block 0x1c3aB0x168b
    prev=[0x168b], succ=[0x1694]
    =================================
    0x1c3bS0x168b: v1c3bV168b(0x0) = CONST 
    0x1c3dS0x168b: v1c3dV168b(0x12) = CONST 
    0x1c3fS0x168b: v1c3fV168b(0xa) = CONST 
    0x1c41S0x168b: v1c41V168b(0xde0b6b3a7640000) = EXP v1c3fV168b(0xa), v1c3dV168b(0x12)
    0x1c43S0x168b: v1c43V168b = MUL v802, v1c41V168b(0xde0b6b3a7640000)
    0x1c49S0x168b: JUMP v168c(0x1694)

    Begin block 0x1694
    prev=[0x1c3aB0x168b], succ=[0x16a5, 0x16a9]
    =================================
    0x1697: v1697(0x8) = CONST 
    0x1699: v1699 = SLOAD v1697(0x8)
    0x169a: v169a(0x9) = CONST 
    0x169c: v169c = SLOAD v169a(0x9)
    0x169e: v169e = ADD v1c43V168b, v169c
    0x169f: v169f = GT v169e, v1699
    0x16a0: v16a0 = ISZERO v169f
    0x16a1: v16a1(0x16a9) = CONST 
    0x16a4: JUMPI v16a1(0x16a9), v16a0

    Begin block 0x16a5
    prev=[0x1694], succ=[]
    =================================
    0x16a5: v16a5(0x0) = CONST 
    0x16a8: REVERT v16a5(0x0), v16a5(0x0)

    Begin block 0x16a9
    prev=[0x1694], succ=[0x1c4a]
    =================================
    0x16aa: v16aa(0x16b5) = CONST 
    0x16ad: v16ad(0x8) = CONST 
    0x16af: v16af = SLOAD v16ad(0x8)
    0x16b1: v16b1(0x1c4a) = CONST 
    0x16b4: JUMP v16b1(0x1c4a)

    Begin block 0x1c4a
    prev=[0x16a9], succ=[0x1c58, 0x1c59]
    =================================
    0x1c4b: v1c4b(0x0) = CONST 
    0x1c50: v1c50 = LT v16af, v1c43V168b
    0x1c51: v1c51 = ISZERO v1c50
    0x1c52: v1c52 = ISZERO v1c51
    0x1c53: v1c53 = ISZERO v1c52
    0x1c54: v1c54(0x1c59) = CONST 
    0x1c57: JUMPI v1c54(0x1c59), v1c53

    Begin block 0x1c58
    prev=[0x1c4a], succ=[]
    =================================
    0x1c58: THROW 

    Begin block 0x1c59
    prev=[0x1c4a], succ=[0x16b5]
    =================================
    0x1c5c: v1c5c = SUB v16af, v1c43V168b
    0x1c67: JUMP v16aa(0x16b5)

    Begin block 0x16b5
    prev=[0x1c59], succ=[0x810]
    =================================
    0x16b6: v16b6(0x8) = CONST 
    0x16ba: SSTORE v16b6(0x8), v1c5c
    0x16bc: v16bc(0x9ecdebfa921d6ab8cecf7259ef30327664ad0d45d32fa3641089b00b533f2eee) = CONST 
    0x16de: v16de(0x40) = CONST 
    0x16e0: v16e0 = MLOAD v16de(0x40)
    0x16e4: MSTORE v16e0, v1c43V168b
    0x16e5: v16e5(0x20) = CONST 
    0x16e7: v16e7 = ADD v16e5(0x20), v16e0
    0x16eb: v16eb(0x40) = CONST 
    0x16ed: v16ed = MLOAD v16eb(0x40)
    0x16f0: v16f0(0x20) = SUB v16e7, v16ed
    0x16f2: LOG1 v16ed, v16f0(0x20), v16bc(0x9ecdebfa921d6ab8cecf7259ef30327664ad0d45d32fa3641089b00b533f2eee)
    0x16f5: JUMP v7fb(0x810)

    Begin block 0x810
    prev=[0x16b5], succ=[]
    =================================
    0x811: STOP 

}

function changeOwner(address)() public {
    Begin block 0x812
    prev=[], succ=[0x819, 0x81d]
    =================================
    0x813: v813 = CALLVALUE 
    0x814: v814 = ISZERO v813
    0x815: v815(0x81d) = CONST 
    0x818: JUMPI v815(0x81d), v814

    Begin block 0x819
    prev=[0x812], succ=[]
    =================================
    0x819: v819(0x0) = CONST 
    0x81c: REVERT v819(0x0), v819(0x0)

    Begin block 0x81d
    prev=[0x812], succ=[0x16f6]
    =================================
    0x81e: v81e(0x849) = CONST 
    0x821: v821(0x4) = CONST 
    0x825: v825 = CALLDATALOAD v821(0x4)
    0x826: v826(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x83b: v83b = AND v826(0xffffffffffffffffffffffffffffffffffffffff), v825
    0x83d: v83d(0x20) = CONST 
    0x83f: v83f(0x24) = ADD v83d(0x20), v821(0x4)
    0x845: v845(0x16f6) = CONST 
    0x848: JUMP v845(0x16f6)

    Begin block 0x16f6
    prev=[0x81d], succ=[0x174e, 0x1752]
    =================================
    0x16f7: v16f7(0x4) = CONST 
    0x16f9: v16f9(0x0) = CONST 
    0x16fc: v16fc = SLOAD v16f7(0x4)
    0x16fe: v16fe(0x100) = CONST 
    0x1701: v1701(0x1) = EXP v16fe(0x100), v16f9(0x0)
    0x1703: v1703 = DIV v16fc, v1701(0x1)
    0x1704: v1704(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1719: v1719 = AND v1704(0xffffffffffffffffffffffffffffffffffffffff), v1703
    0x171a: v171a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x172f: v172f = AND v171a(0xffffffffffffffffffffffffffffffffffffffff), v1719
    0x1730: v1730 = CALLER 
    0x1731: v1731(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1746: v1746 = AND v1731(0xffffffffffffffffffffffffffffffffffffffff), v1730
    0x1747: v1747 = EQ v1746, v172f
    0x1748: v1748 = ISZERO v1747
    0x1749: v1749 = ISZERO v1748
    0x174a: v174a(0x1752) = CONST 
    0x174d: JUMPI v174a(0x1752), v1749

    Begin block 0x174e
    prev=[0x16f6], succ=[]
    =================================
    0x174e: v174e(0x0) = CONST 
    0x1751: REVERT v174e(0x0), v174e(0x0)

    Begin block 0x1752
    prev=[0x16f6], succ=[0x1788, 0x178c]
    =================================
    0x1753: v1753(0x0) = CONST 
    0x1755: v1755(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x176a: v176a(0x0) = AND v1755(0xffffffffffffffffffffffffffffffffffffffff), v1753(0x0)
    0x176c: v176c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1781: v1781 = AND v176c(0xffffffffffffffffffffffffffffffffffffffff), v83b
    0x1782: v1782 = EQ v1781, v176a(0x0)
    0x1783: v1783 = ISZERO v1782
    0x1784: v1784(0x178c) = CONST 
    0x1787: JUMPI v1784(0x178c), v1783

    Begin block 0x1788
    prev=[0x1752], succ=[]
    =================================
    0x1788: v1788(0x0) = CONST 
    0x178b: REVERT v1788(0x0), v1788(0x0)

    Begin block 0x178c
    prev=[0x1752], succ=[0x849]
    =================================
    0x178e: v178e(0x4) = CONST 
    0x1790: v1790(0x0) = CONST 
    0x1792: v1792(0x100) = CONST 
    0x1795: v1795(0x1) = EXP v1792(0x100), v1790(0x0)
    0x1797: v1797 = SLOAD v178e(0x4)
    0x1799: v1799(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17ae: v17ae(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1799(0xffffffffffffffffffffffffffffffffffffffff), v1795(0x1)
    0x17af: v17af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v17ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x17b0: v17b0 = AND v17af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1797
    0x17b3: v17b3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17c8: v17c8 = AND v17b3(0xffffffffffffffffffffffffffffffffffffffff), v83b
    0x17c9: v17c9 = MUL v17c8, v1795(0x1)
    0x17ca: v17ca = OR v17c9, v17b0
    0x17cc: SSTORE v178e(0x4), v17ca
    0x17cf: JUMP v81e(0x849)

    Begin block 0x849
    prev=[0x178c], succ=[]
    =================================
    0x84a: STOP 

}

function ethFundDeposit()() public {
    Begin block 0x84b
    prev=[], succ=[0x852, 0x856]
    =================================
    0x84c: v84c = CALLVALUE 
    0x84d: v84d = ISZERO v84c
    0x84e: v84e(0x856) = CONST 
    0x851: JUMPI v84e(0x856), v84d

    Begin block 0x852
    prev=[0x84b], succ=[]
    =================================
    0x852: v852(0x0) = CONST 
    0x855: REVERT v852(0x0), v852(0x0)

    Begin block 0x856
    prev=[0x84b], succ=[0x17d0]
    =================================
    0x857: v857(0x85e) = CONST 
    0x85a: v85a(0x17d0) = CONST 
    0x85d: JUMP v85a(0x17d0)

    Begin block 0x17d0
    prev=[0x856], succ=[0x85e]
    =================================
    0x17d1: v17d1(0x4) = CONST 
    0x17d3: v17d3(0x0) = CONST 
    0x17d6: v17d6 = SLOAD v17d1(0x4)
    0x17d8: v17d8(0x100) = CONST 
    0x17db: v17db(0x1) = EXP v17d8(0x100), v17d3(0x0)
    0x17dd: v17dd = DIV v17d6, v17db(0x1)
    0x17de: v17de(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17f3: v17f3 = AND v17de(0xffffffffffffffffffffffffffffffffffffffff), v17dd
    0x17f5: JUMP v857(0x85e)

    Begin block 0x85e
    prev=[0x17d0], succ=[]
    =================================
    0x85f: v85f(0x40) = CONST 
    0x861: v861 = MLOAD v85f(0x40)
    0x864: v864(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x879: v879 = AND v864(0xffffffffffffffffffffffffffffffffffffffff), v17f3
    0x87a: v87a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x88f: v88f = AND v87a(0xffffffffffffffffffffffffffffffffffffffff), v879
    0x891: MSTORE v861, v88f
    0x892: v892(0x20) = CONST 
    0x894: v894 = ADD v892(0x20), v861
    0x898: v898(0x40) = CONST 
    0x89a: v89a = MLOAD v898(0x40)
    0x89d: v89d(0x20) = SUB v894, v89a
    0x89f: RETURN v89a, v89d(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x8a0
    prev=[], succ=[0x8a7, 0x8ab]
    =================================
    0x8a1: v8a1 = CALLVALUE 
    0x8a2: v8a2 = ISZERO v8a1
    0x8a3: v8a3(0x8ab) = CONST 
    0x8a6: JUMPI v8a3(0x8ab), v8a2

    Begin block 0x8a7
    prev=[0x8a0], succ=[]
    =================================
    0x8a7: v8a7(0x0) = CONST 
    0x8aa: REVERT v8a7(0x0), v8a7(0x0)

    Begin block 0x8ab
    prev=[0x8a0], succ=[0x17f6B0x8ab]
    =================================
    0x8ac: v8ac(0x8e0) = CONST 
    0x8af: v8af(0x4) = CONST 
    0x8b3: v8b3 = CALLDATALOAD v8af(0x4)
    0x8b4: v8b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8c9: v8c9 = AND v8b4(0xffffffffffffffffffffffffffffffffffffffff), v8b3
    0x8cb: v8cb(0x20) = CONST 
    0x8cd: v8cd(0x24) = ADD v8cb(0x20), v8af(0x4)
    0x8d2: v8d2 = CALLDATALOAD v8cd(0x24)
    0x8d4: v8d4(0x20) = CONST 
    0x8d6: v8d6(0x44) = ADD v8d4(0x20), v8cd(0x24)
    0x8dc: v8dc(0x17f6) = CONST 
    0x8df: JUMP v8dc(0x17f6)

    Begin block 0x17f6B0x8ab
    prev=[0x8ab], succ=[0x1847B0x8ab, 0x1842B0x8ab]
    =================================
    0x17f7S0x8ab: v17f7V8ab(0x0) = CONST 
    0x17faS0x8ab: v17faV8ab(0x1) = CONST 
    0x17fcS0x8ab: v17fcV8ab(0x0) = CONST 
    0x17feS0x8ab: v17feV8ab = CALLER 
    0x17ffS0x8ab: v17ffV8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1814S0x8ab: v1814V8ab = AND v17ffV8ab(0xffffffffffffffffffffffffffffffffffffffff), v17feV8ab
    0x1815S0x8ab: v1815V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x182aS0x8ab: v182aV8ab = AND v1815V8ab(0xffffffffffffffffffffffffffffffffffffffff), v1814V8ab
    0x182cS0x8ab: MSTORE v17fcV8ab(0x0), v182aV8ab
    0x182dS0x8ab: v182dV8ab(0x20) = CONST 
    0x182fS0x8ab: v182fV8ab(0x20) = ADD v182dV8ab(0x20), v17fcV8ab(0x0)
    0x1832S0x8ab: MSTORE v182fV8ab(0x20), v17faV8ab(0x1)
    0x1833S0x8ab: v1833V8ab(0x20) = CONST 
    0x1835S0x8ab: v1835V8ab(0x40) = ADD v1833V8ab(0x20), v182fV8ab(0x20)
    0x1836S0x8ab: v1836V8ab(0x0) = CONST 
    0x1838S0x8ab: v1838V8ab = SHA3 v1836V8ab(0x0), v1835V8ab(0x40)
    0x1839S0x8ab: v1839V8ab = SLOAD v1838V8ab
    0x183aS0x8ab: v183aV8ab = LT v1839V8ab, v8d2
    0x183bS0x8ab: v183bV8ab = ISZERO v183aV8ab
    0x183dS0x8ab: v183dV8ab = ISZERO v183bV8ab
    0x183eS0x8ab: v183eV8ab(0x1847) = CONST 
    0x1841S0x8ab: JUMPI v183eV8ab(0x1847), v183dV8ab

    Begin block 0x1847B0x8ab
    prev=[0x17f6B0x8ab, 0x1842B0x8ab], succ=[0x1954B0x8ab, 0x184dB0x8ab]
    =================================
    0x1847_0x0S0x8ab: v1847_0V8ab = PHI v183bV8ab, v1846V8ab
    0x1848S0x8ab: v1848V8ab = ISZERO v1847_0V8ab
    0x1849S0x8ab: v1849V8ab(0x1954) = CONST 
    0x184cS0x8ab: JUMPI v1849V8ab(0x1954), v1848V8ab

    Begin block 0x1954B0x8ab
    prev=[0x1847B0x8ab], succ=[0x18bc2B0x8ab]
    =================================
    0x1955S0x8ab: v1955V8ab(0x0) = CONST 
    0xc53eS0x8ab: vc53eV8ab(0x18bc2) = CONST 
    0xc55eS0x8ab: JUMP vc53eV8ab(0x18bc2)

    Begin block 0x18bc2B0x8ab
    prev=[0x1954B0x8ab], succ=[0x8e0]
    =================================
    0x18bc7S0x8ab: JUMP v8ac(0x8e0)

    Begin block 0x8e0
    prev=[0x18b50B0x8ab, 0x18bc2B0x8ab], succ=[]
    =================================
    0x8abS0x8e0_0: v8df_0V8e0_0 = PHI v1955V8ab(0x0), v194cV8ab(0x1)
    0x8e1: v8e1(0x40) = CONST 
    0x8e3: v8e3 = MLOAD v8e1(0x40)
    0x8e6: v8e6 = ISZERO v8df_0V8e0_0
    0x8e7: v8e7 = ISZERO v8e6
    0x8e8: v8e8 = ISZERO v8e7
    0x8e9: v8e9 = ISZERO v8e8
    0x8eb: MSTORE v8e3, v8e9
    0x8ec: v8ec(0x20) = CONST 
    0x8ee: v8ee = ADD v8ec(0x20), v8e3
    0x8f2: v8f2(0x40) = CONST 
    0x8f4: v8f4 = MLOAD v8f2(0x40)
    0x8f7: v8f7(0x20) = SUB v8ee, v8f4
    0x8f9: RETURN v8f4, v8f7(0x20)

    Begin block 0x184dB0x8ab
    prev=[0x1847B0x8ab], succ=[0x18b50B0x8ab]
    =================================
    0x184eS0x8ab: v184eV8ab(0x1) = CONST 
    0x1850S0x8ab: v1850V8ab(0x0) = CONST 
    0x1852S0x8ab: v1852V8ab = CALLER 
    0x1853S0x8ab: v1853V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1868S0x8ab: v1868V8ab = AND v1853V8ab(0xffffffffffffffffffffffffffffffffffffffff), v1852V8ab
    0x1869S0x8ab: v1869V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x187eS0x8ab: v187eV8ab = AND v1869V8ab(0xffffffffffffffffffffffffffffffffffffffff), v1868V8ab
    0x1880S0x8ab: MSTORE v1850V8ab(0x0), v187eV8ab
    0x1881S0x8ab: v1881V8ab(0x20) = CONST 
    0x1883S0x8ab: v1883V8ab(0x20) = ADD v1881V8ab(0x20), v1850V8ab(0x0)
    0x1886S0x8ab: MSTORE v1883V8ab(0x20), v184eV8ab(0x1)
    0x1887S0x8ab: v1887V8ab(0x20) = CONST 
    0x1889S0x8ab: v1889V8ab(0x40) = ADD v1887V8ab(0x20), v1883V8ab(0x20)
    0x188aS0x8ab: v188aV8ab(0x0) = CONST 
    0x188cS0x8ab: v188cV8ab = SHA3 v188aV8ab(0x0), v1889V8ab(0x40)
    0x188dS0x8ab: v188dV8ab(0x0) = CONST 
    0x1891S0x8ab: v1891V8ab = SLOAD v188cV8ab
    0x1892S0x8ab: v1892V8ab = SUB v1891V8ab, v8d2
    0x1898S0x8ab: SSTORE v188cV8ab, v1892V8ab
    0x189bS0x8ab: v189bV8ab(0x1) = CONST 
    0x189dS0x8ab: v189dV8ab(0x0) = CONST 
    0x18a0S0x8ab: v18a0V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18b5S0x8ab: v18b5V8ab = AND v18a0V8ab(0xffffffffffffffffffffffffffffffffffffffff), v8c9
    0x18b6S0x8ab: v18b6V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18cbS0x8ab: v18cbV8ab = AND v18b6V8ab(0xffffffffffffffffffffffffffffffffffffffff), v18b5V8ab
    0x18cdS0x8ab: MSTORE v189dV8ab(0x0), v18cbV8ab
    0x18ceS0x8ab: v18ceV8ab(0x20) = CONST 
    0x18d0S0x8ab: v18d0V8ab(0x20) = ADD v18ceV8ab(0x20), v189dV8ab(0x0)
    0x18d3S0x8ab: MSTORE v18d0V8ab(0x20), v189bV8ab(0x1)
    0x18d4S0x8ab: v18d4V8ab(0x20) = CONST 
    0x18d6S0x8ab: v18d6V8ab(0x40) = ADD v18d4V8ab(0x20), v18d0V8ab(0x20)
    0x18d7S0x8ab: v18d7V8ab(0x0) = CONST 
    0x18d9S0x8ab: v18d9V8ab = SHA3 v18d7V8ab(0x0), v18d6V8ab(0x40)
    0x18daS0x8ab: v18daV8ab(0x0) = CONST 
    0x18deS0x8ab: v18deV8ab = SLOAD v18d9V8ab
    0x18dfS0x8ab: v18dfV8ab = ADD v18deV8ab, v8d2
    0x18e5S0x8ab: SSTORE v18d9V8ab, v18dfV8ab
    0x18e8S0x8ab: v18e8V8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18fdS0x8ab: v18fdV8ab = AND v18e8V8ab(0xffffffffffffffffffffffffffffffffffffffff), v8c9
    0x18feS0x8ab: v18feV8ab = CALLER 
    0x18ffS0x8ab: v18ffV8ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1914S0x8ab: v1914V8ab = AND v18ffV8ab(0xffffffffffffffffffffffffffffffffffffffff), v18feV8ab
    0x1915S0x8ab: v1915V8ab(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1937S0x8ab: v1937V8ab(0x40) = CONST 
    0x1939S0x8ab: v1939V8ab = MLOAD v1937V8ab(0x40)
    0x193dS0x8ab: MSTORE v1939V8ab, v8d2
    0x193eS0x8ab: v193eV8ab(0x20) = CONST 
    0x1940S0x8ab: v1940V8ab = ADD v193eV8ab(0x20), v1939V8ab
    0x1944S0x8ab: v1944V8ab(0x40) = CONST 
    0x1946S0x8ab: v1946V8ab = MLOAD v1944V8ab(0x40)
    0x1949S0x8ab: v1949V8ab(0x20) = SUB v1940V8ab, v1946V8ab
    0x194bS0x8ab: LOG3 v1946V8ab, v1949V8ab(0x20), v1915V8ab(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1914V8ab, v18fdV8ab
    0x194cS0x8ab: v194cV8ab(0x1) = CONST 
    0x1950S0x8ab: v1950V8ab(0x18b50) = CONST 
    0x1953S0x8ab: JUMP v1950V8ab(0x18b50)

    Begin block 0x18b50B0x8ab
    prev=[0x184dB0x8ab], succ=[0x8e0]
    =================================
    0x18b55S0x8ab: JUMP v8ac(0x8e0)

    Begin block 0x1842B0x8ab
    prev=[0x17f6B0x8ab], succ=[0x1847B0x8ab]
    =================================
    0x1843S0x8ab: v1843V8ab(0x0) = CONST 
    0x1846S0x8ab: v1846V8ab = GT v8d2, v1843V8ab(0x0)
    0xbb3eS0x8ab: vbb3eV8ab(0x1847) = CONST 
    0xbb5eS0x8ab: JUMP vbb3eV8ab(0x1847)

}

function increaseSupply(uint256)() public {
    Begin block 0x8fa
    prev=[], succ=[0x901, 0x905]
    =================================
    0x8fb: v8fb = CALLVALUE 
    0x8fc: v8fc = ISZERO v8fb
    0x8fd: v8fd(0x905) = CONST 
    0x900: JUMPI v8fd(0x905), v8fc

    Begin block 0x901
    prev=[0x8fa], succ=[]
    =================================
    0x901: v901(0x0) = CONST 
    0x904: REVERT v901(0x0), v901(0x0)

    Begin block 0x905
    prev=[0x8fa], succ=[0x195f]
    =================================
    0x906: v906(0x91b) = CONST 
    0x909: v909(0x4) = CONST 
    0x90d: v90d = CALLDATALOAD v909(0x4)
    0x90f: v90f(0x20) = CONST 
    0x911: v911(0x24) = ADD v90f(0x20), v909(0x4)
    0x917: v917(0x195f) = CONST 
    0x91a: JUMP v917(0x195f)

    Begin block 0x195f
    prev=[0x905], succ=[0x19b9, 0x19bd]
    =================================
    0x1960: v1960(0x0) = CONST 
    0x1962: v1962(0x4) = CONST 
    0x1964: v1964(0x0) = CONST 
    0x1967: v1967 = SLOAD v1962(0x4)
    0x1969: v1969(0x100) = CONST 
    0x196c: v196c(0x1) = EXP v1969(0x100), v1964(0x0)
    0x196e: v196e = DIV v1967, v196c(0x1)
    0x196f: v196f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1984: v1984 = AND v196f(0xffffffffffffffffffffffffffffffffffffffff), v196e
    0x1985: v1985(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x199a: v199a = AND v1985(0xffffffffffffffffffffffffffffffffffffffff), v1984
    0x199b: v199b = CALLER 
    0x199c: v199c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19b1: v19b1 = AND v199c(0xffffffffffffffffffffffffffffffffffffffff), v199b
    0x19b2: v19b2 = EQ v19b1, v199a
    0x19b3: v19b3 = ISZERO v19b2
    0x19b4: v19b4 = ISZERO v19b3
    0x19b5: v19b5(0x19bd) = CONST 
    0x19b8: JUMPI v19b5(0x19bd), v19b4

    Begin block 0x19b9
    prev=[0x195f], succ=[]
    =================================
    0x19b9: v19b9(0x0) = CONST 
    0x19bc: REVERT v19b9(0x0), v19b9(0x0)

    Begin block 0x19bd
    prev=[0x195f], succ=[0x1c3aB0x19bd]
    =================================
    0x19be: v19be(0x19c6) = CONST 
    0x19c2: v19c2(0x1c3a) = CONST 
    0x19c5: JUMP v19c2(0x1c3a)

    Begin block 0x1c3aB0x19bd
    prev=[0x19bd], succ=[0x19c6]
    =================================
    0x1c3bS0x19bd: v1c3bV19bd(0x0) = CONST 
    0x1c3dS0x19bd: v1c3dV19bd(0x12) = CONST 
    0x1c3fS0x19bd: v1c3fV19bd(0xa) = CONST 
    0x1c41S0x19bd: v1c41V19bd(0xde0b6b3a7640000) = EXP v1c3fV19bd(0xa), v1c3dV19bd(0x12)
    0x1c43S0x19bd: v1c43V19bd = MUL v90d, v1c41V19bd(0xde0b6b3a7640000)
    0x1c49S0x19bd: JUMP v19be(0x19c6)

    Begin block 0x19c6
    prev=[0x1c3aB0x19bd], succ=[0x19d7, 0x19db]
    =================================
    0x19c9: v19c9(0x0) = CONST 
    0x19cb: v19cb = SLOAD v19c9(0x0)
    0x19cc: v19cc(0x8) = CONST 
    0x19ce: v19ce = SLOAD v19cc(0x8)
    0x19d0: v19d0 = ADD v1c43V19bd, v19ce
    0x19d1: v19d1 = GT v19d0, v19cb
    0x19d2: v19d2 = ISZERO v19d1
    0x19d3: v19d3(0x19db) = CONST 
    0x19d6: JUMPI v19d3(0x19db), v19d2

    Begin block 0x19d7
    prev=[0x19c6], succ=[]
    =================================
    0x19d7: v19d7(0x0) = CONST 
    0x19da: REVERT v19d7(0x0), v19d7(0x0)

    Begin block 0x19db
    prev=[0x19c6], succ=[0x19e7]
    =================================
    0x19dc: v19dc(0x19e7) = CONST 
    0x19df: v19df(0x8) = CONST 
    0x19e1: v19e1 = SLOAD v19df(0x8)
    0x19e3: v19e3(0xa46) = CONST 
    0x19e6: v19e6_0 = CALLPRIVATE v19e3(0xa46), v1c43V19bd, v19e1, v19dc(0x19e7)

    Begin block 0x19e7
    prev=[0x19db], succ=[0x91b]
    =================================
    0x19e8: v19e8(0x8) = CONST 
    0x19ec: SSTORE v19e8(0x8), v19e6_0
    0x19ee: v19ee(0xfaabf704b783af9e21c676de8e3e6e0c9c2260dce2ee299437ec9b70151ddaeb) = CONST 
    0x1a10: v1a10(0x40) = CONST 
    0x1a12: v1a12 = MLOAD v1a10(0x40)
    0x1a16: MSTORE v1a12, v1c43V19bd
    0x1a17: v1a17(0x20) = CONST 
    0x1a19: v1a19 = ADD v1a17(0x20), v1a12
    0x1a1d: v1a1d(0x40) = CONST 
    0x1a1f: v1a1f = MLOAD v1a1d(0x40)
    0x1a22: v1a22(0x20) = SUB v1a19, v1a1f
    0x1a24: LOG1 v1a1f, v1a22(0x20), v19ee(0xfaabf704b783af9e21c676de8e3e6e0c9c2260dce2ee299437ec9b70151ddaeb)
    0x1a27: JUMP v906(0x91b)

    Begin block 0x91b
    prev=[0x19e7], succ=[]
    =================================
    0x91c: STOP 

}

function setTokenExchangeRate(uint256)() public {
    Begin block 0x91d
    prev=[], succ=[0x924, 0x928]
    =================================
    0x91e: v91e = CALLVALUE 
    0x91f: v91f = ISZERO v91e
    0x920: v920(0x928) = CONST 
    0x923: JUMPI v920(0x928), v91f

    Begin block 0x924
    prev=[0x91d], succ=[]
    =================================
    0x924: v924(0x0) = CONST 
    0x927: REVERT v924(0x0), v924(0x0)

    Begin block 0x928
    prev=[0x91d], succ=[0x1a28]
    =================================
    0x929: v929(0x93e) = CONST 
    0x92c: v92c(0x4) = CONST 
    0x930: v930 = CALLDATALOAD v92c(0x4)
    0x932: v932(0x20) = CONST 
    0x934: v934(0x24) = ADD v932(0x20), v92c(0x4)
    0x93a: v93a(0x1a28) = CONST 
    0x93d: JUMP v93a(0x1a28)

    Begin block 0x1a28
    prev=[0x928], succ=[0x1a80, 0x1a84]
    =================================
    0x1a29: v1a29(0x4) = CONST 
    0x1a2b: v1a2b(0x0) = CONST 
    0x1a2e: v1a2e = SLOAD v1a29(0x4)
    0x1a30: v1a30(0x100) = CONST 
    0x1a33: v1a33(0x1) = EXP v1a30(0x100), v1a2b(0x0)
    0x1a35: v1a35 = DIV v1a2e, v1a33(0x1)
    0x1a36: v1a36(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a4b: v1a4b = AND v1a36(0xffffffffffffffffffffffffffffffffffffffff), v1a35
    0x1a4c: v1a4c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a61: v1a61 = AND v1a4c(0xffffffffffffffffffffffffffffffffffffffff), v1a4b
    0x1a62: v1a62 = CALLER 
    0x1a63: v1a63(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a78: v1a78 = AND v1a63(0xffffffffffffffffffffffffffffffffffffffff), v1a62
    0x1a79: v1a79 = EQ v1a78, v1a61
    0x1a7a: v1a7a = ISZERO v1a79
    0x1a7b: v1a7b = ISZERO v1a7a
    0x1a7c: v1a7c(0x1a84) = CONST 
    0x1a7f: JUMPI v1a7c(0x1a84), v1a7b

    Begin block 0x1a80
    prev=[0x1a28], succ=[]
    =================================
    0x1a80: v1a80(0x0) = CONST 
    0x1a83: REVERT v1a80(0x0), v1a80(0x0)

    Begin block 0x1a84
    prev=[0x1a28], succ=[0x1a8e, 0x1a92]
    =================================
    0x1a85: v1a85(0x0) = CONST 
    0x1a88: v1a88 = EQ v930, v1a85(0x0)
    0x1a89: v1a89 = ISZERO v1a88
    0x1a8a: v1a8a(0x1a92) = CONST 
    0x1a8d: JUMPI v1a8a(0x1a92), v1a89

    Begin block 0x1a8e
    prev=[0x1a84], succ=[]
    =================================
    0x1a8e: v1a8e(0x0) = CONST 
    0x1a91: REVERT v1a8e(0x0), v1a8e(0x0)

    Begin block 0x1a92
    prev=[0x1a84], succ=[0x1a9d, 0x1aa1]
    =================================
    0x1a93: v1a93(0xb) = CONST 
    0x1a95: v1a95 = SLOAD v1a93(0xb)
    0x1a97: v1a97 = EQ v930, v1a95
    0x1a98: v1a98 = ISZERO v1a97
    0x1a99: v1a99(0x1aa1) = CONST 
    0x1a9c: JUMPI v1a99(0x1aa1), v1a98

    Begin block 0x1a9d
    prev=[0x1a92], succ=[]
    =================================
    0x1a9d: v1a9d(0x0) = CONST 
    0x1aa0: REVERT v1a9d(0x0), v1a9d(0x0)

    Begin block 0x1aa1
    prev=[0x1a92], succ=[0x93e]
    =================================
    0x1aa3: v1aa3(0xb) = CONST 
    0x1aa7: SSTORE v1aa3(0xb), v930
    0x1aaa: JUMP v929(0x93e)

    Begin block 0x93e
    prev=[0x1aa1], succ=[]
    =================================
    0x93f: STOP 

}

function fundingStartBlock()() public {
    Begin block 0x940
    prev=[], succ=[0x947, 0x94b]
    =================================
    0x941: v941 = CALLVALUE 
    0x942: v942 = ISZERO v941
    0x943: v943(0x94b) = CONST 
    0x946: JUMPI v943(0x94b), v942

    Begin block 0x947
    prev=[0x940], succ=[]
    =================================
    0x947: v947(0x0) = CONST 
    0x94a: REVERT v947(0x0), v947(0x0)

    Begin block 0x94b
    prev=[0x940], succ=[0x1aab]
    =================================
    0x94c: v94c(0x953) = CONST 
    0x94f: v94f(0x1aab) = CONST 
    0x952: JUMP v94f(0x1aab)

    Begin block 0x1aab
    prev=[0x94b], succ=[0x953]
    =================================
    0x1aac: v1aac(0x6) = CONST 
    0x1aae: v1aae = SLOAD v1aac(0x6)
    0x1ab0: JUMP v94c(0x953)

    Begin block 0x953
    prev=[0x1aab], succ=[]
    =================================
    0x954: v954(0x40) = CONST 
    0x956: v956 = MLOAD v954(0x40)
    0x95a: MSTORE v956, v1aae
    0x95b: v95b(0x20) = CONST 
    0x95d: v95d = ADD v95b(0x20), v956
    0x961: v961(0x40) = CONST 
    0x963: v963 = MLOAD v961(0x40)
    0x966: v966(0x20) = SUB v95d, v963
    0x968: RETURN v963, v966(0x20)

}

function allowance(address,address)() public {
    Begin block 0x969
    prev=[], succ=[0x970, 0x974]
    =================================
    0x96a: v96a = CALLVALUE 
    0x96b: v96b = ISZERO v96a
    0x96c: v96c(0x974) = CONST 
    0x96f: JUMPI v96c(0x974), v96b

    Begin block 0x970
    prev=[0x969], succ=[]
    =================================
    0x970: v970(0x0) = CONST 
    0x973: REVERT v970(0x0), v970(0x0)

    Begin block 0x974
    prev=[0x969], succ=[0x1ab1]
    =================================
    0x975: v975(0x9bf) = CONST 
    0x978: v978(0x4) = CONST 
    0x97c: v97c = CALLDATALOAD v978(0x4)
    0x97d: v97d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x992: v992 = AND v97d(0xffffffffffffffffffffffffffffffffffffffff), v97c
    0x994: v994(0x20) = CONST 
    0x996: v996(0x24) = ADD v994(0x20), v978(0x4)
    0x99b: v99b = CALLDATALOAD v996(0x24)
    0x99c: v99c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9b1: v9b1 = AND v99c(0xffffffffffffffffffffffffffffffffffffffff), v99b
    0x9b3: v9b3(0x20) = CONST 
    0x9b5: v9b5(0x44) = ADD v9b3(0x20), v996(0x24)
    0x9bb: v9bb(0x1ab1) = CONST 
    0x9be: JUMP v9bb(0x1ab1)

    Begin block 0x1ab1
    prev=[0x974], succ=[0x9bf]
    =================================
    0x1ab2: v1ab2(0x0) = CONST 
    0x1ab4: v1ab4(0x2) = CONST 
    0x1ab6: v1ab6(0x0) = CONST 
    0x1ab9: v1ab9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ace: v1ace = AND v1ab9(0xffffffffffffffffffffffffffffffffffffffff), v992
    0x1acf: v1acf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ae4: v1ae4 = AND v1acf(0xffffffffffffffffffffffffffffffffffffffff), v1ace
    0x1ae6: MSTORE v1ab6(0x0), v1ae4
    0x1ae7: v1ae7(0x20) = CONST 
    0x1ae9: v1ae9(0x20) = ADD v1ae7(0x20), v1ab6(0x0)
    0x1aec: MSTORE v1ae9(0x20), v1ab4(0x2)
    0x1aed: v1aed(0x20) = CONST 
    0x1aef: v1aef(0x40) = ADD v1aed(0x20), v1ae9(0x20)
    0x1af0: v1af0(0x0) = CONST 
    0x1af2: v1af2 = SHA3 v1af0(0x0), v1aef(0x40)
    0x1af3: v1af3(0x0) = CONST 
    0x1af6: v1af6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b0b: v1b0b = AND v1af6(0xffffffffffffffffffffffffffffffffffffffff), v9b1
    0x1b0c: v1b0c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b21: v1b21 = AND v1b0c(0xffffffffffffffffffffffffffffffffffffffff), v1b0b
    0x1b23: MSTORE v1af3(0x0), v1b21
    0x1b24: v1b24(0x20) = CONST 
    0x1b26: v1b26(0x20) = ADD v1b24(0x20), v1af3(0x0)
    0x1b29: MSTORE v1b26(0x20), v1af2
    0x1b2a: v1b2a(0x20) = CONST 
    0x1b2c: v1b2c(0x40) = ADD v1b2a(0x20), v1b26(0x20)
    0x1b2d: v1b2d(0x0) = CONST 
    0x1b2f: v1b2f = SHA3 v1b2d(0x0), v1b2c(0x40)
    0x1b30: v1b30 = SLOAD v1b2f
    0x1b37: JUMP v975(0x9bf)

    Begin block 0x9bf
    prev=[0x1ab1], succ=[]
    =================================
    0x9c0: v9c0(0x40) = CONST 
    0x9c2: v9c2 = MLOAD v9c0(0x40)
    0x9c6: MSTORE v9c2, v1b30
    0x9c7: v9c7(0x20) = CONST 
    0x9c9: v9c9 = ADD v9c7(0x20), v9c2
    0x9cd: v9cd(0x40) = CONST 
    0x9cf: v9cf = MLOAD v9cd(0x40)
    0x9d2: v9d2(0x20) = SUB v9c9, v9cf
    0x9d4: RETURN v9cf, v9d2(0x20)

}

function transferETH()() public {
    Begin block 0x9d5
    prev=[], succ=[0x9dc, 0x9e0]
    =================================
    0x9d6: v9d6 = CALLVALUE 
    0x9d7: v9d7 = ISZERO v9d6
    0x9d8: v9d8(0x9e0) = CONST 
    0x9db: JUMPI v9d8(0x9e0), v9d7

    Begin block 0x9dc
    prev=[0x9d5], succ=[]
    =================================
    0x9dc: v9dc(0x0) = CONST 
    0x9df: REVERT v9dc(0x0), v9dc(0x0)

    Begin block 0x9e0
    prev=[0x9d5], succ=[0x1b38B0x9e0]
    =================================
    0x9e1: v9e1(0x9e8) = CONST 
    0x9e4: v9e4(0x1b38) = CONST 
    0x9e7: JUMP v9e4(0x1b38)

    Begin block 0x1b38B0x9e0
    prev=[0x9e0], succ=[0x1b90B0x9e0, 0x1b94B0x9e0]
    =================================
    0x1b39S0x9e0: v1b39V9e0(0x4) = CONST 
    0x1b3bS0x9e0: v1b3bV9e0(0x0) = CONST 
    0x1b3eS0x9e0: v1b3eV9e0 = SLOAD v1b39V9e0(0x4)
    0x1b40S0x9e0: v1b40V9e0(0x100) = CONST 
    0x1b43S0x9e0: v1b43V9e0(0x1) = EXP v1b40V9e0(0x100), v1b3bV9e0(0x0)
    0x1b45S0x9e0: v1b45V9e0 = DIV v1b3eV9e0, v1b43V9e0(0x1)
    0x1b46S0x9e0: v1b46V9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b5bS0x9e0: v1b5bV9e0 = AND v1b46V9e0(0xffffffffffffffffffffffffffffffffffffffff), v1b45V9e0
    0x1b5cS0x9e0: v1b5cV9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b71S0x9e0: v1b71V9e0 = AND v1b5cV9e0(0xffffffffffffffffffffffffffffffffffffffff), v1b5bV9e0
    0x1b72S0x9e0: v1b72V9e0 = CALLER 
    0x1b73S0x9e0: v1b73V9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b88S0x9e0: v1b88V9e0 = AND v1b73V9e0(0xffffffffffffffffffffffffffffffffffffffff), v1b72V9e0
    0x1b89S0x9e0: v1b89V9e0 = EQ v1b88V9e0, v1b71V9e0
    0x1b8aS0x9e0: v1b8aV9e0 = ISZERO v1b89V9e0
    0x1b8bS0x9e0: v1b8bV9e0 = ISZERO v1b8aV9e0
    0x1b8cS0x9e0: v1b8cV9e0(0x1b94) = CONST 
    0x1b8fS0x9e0: JUMPI v1b8cV9e0(0x1b94), v1b8bV9e0

    Begin block 0x1b90B0x9e0
    prev=[0x1b38B0x9e0], succ=[]
    =================================
    0x1b90S0x9e0: v1b90V9e0(0x0) = CONST 
    0x1b93S0x9e0: REVERT v1b90V9e0(0x0), v1b90V9e0(0x0)

    Begin block 0x1b94B0x9e0
    prev=[0x1b38B0x9e0], succ=[0x1bb5B0x9e0, 0x1bb9B0x9e0]
    =================================
    0x1b95S0x9e0: v1b95V9e0(0x0) = CONST 
    0x1b97S0x9e0: v1b97V9e0 = ADDRESS 
    0x1b98S0x9e0: v1b98V9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1badS0x9e0: v1badV9e0 = AND v1b98V9e0(0xffffffffffffffffffffffffffffffffffffffff), v1b97V9e0
    0x1baeS0x9e0: v1baeV9e0 = BALANCE v1badV9e0
    0x1bafS0x9e0: v1bafV9e0 = EQ v1baeV9e0, v1b95V9e0(0x0)
    0x1bb0S0x9e0: v1bb0V9e0 = ISZERO v1bafV9e0
    0x1bb1S0x9e0: v1bb1V9e0(0x1bb9) = CONST 
    0x1bb4S0x9e0: JUMPI v1bb1V9e0(0x1bb9), v1bb0V9e0

    Begin block 0x1bb5B0x9e0
    prev=[0x1b94B0x9e0], succ=[]
    =================================
    0x1bb5S0x9e0: v1bb5V9e0(0x0) = CONST 
    0x1bb8S0x9e0: REVERT v1bb5V9e0(0x0), v1bb5V9e0(0x0)

    Begin block 0x1bb9B0x9e0
    prev=[0x1b94B0x9e0], succ=[0x1c2eB0x9e0, 0x1c32B0x9e0]
    =================================
    0x1bbaS0x9e0: v1bbaV9e0(0x4) = CONST 
    0x1bbcS0x9e0: v1bbcV9e0(0x0) = CONST 
    0x1bbfS0x9e0: v1bbfV9e0 = SLOAD v1bbaV9e0(0x4)
    0x1bc1S0x9e0: v1bc1V9e0(0x100) = CONST 
    0x1bc4S0x9e0: v1bc4V9e0(0x1) = EXP v1bc1V9e0(0x100), v1bbcV9e0(0x0)
    0x1bc6S0x9e0: v1bc6V9e0 = DIV v1bbfV9e0, v1bc4V9e0(0x1)
    0x1bc7S0x9e0: v1bc7V9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bdcS0x9e0: v1bdcV9e0 = AND v1bc7V9e0(0xffffffffffffffffffffffffffffffffffffffff), v1bc6V9e0
    0x1bddS0x9e0: v1bddV9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bf2S0x9e0: v1bf2V9e0 = AND v1bddV9e0(0xffffffffffffffffffffffffffffffffffffffff), v1bdcV9e0
    0x1bf3S0x9e0: v1bf3V9e0(0x8fc) = CONST 
    0x1bf6S0x9e0: v1bf6V9e0 = ADDRESS 
    0x1bf7S0x9e0: v1bf7V9e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c0cS0x9e0: v1c0cV9e0 = AND v1bf7V9e0(0xffffffffffffffffffffffffffffffffffffffff), v1bf6V9e0
    0x1c0dS0x9e0: v1c0dV9e0 = BALANCE v1c0cV9e0
    0x1c10S0x9e0: v1c10V9e0 = ISZERO v1c0dV9e0
    0x1c11S0x9e0: v1c11V9e0 = MUL v1c10V9e0, v1bf3V9e0(0x8fc)
    0x1c13S0x9e0: v1c13V9e0(0x40) = CONST 
    0x1c15S0x9e0: v1c15V9e0 = MLOAD v1c13V9e0(0x40)
    0x1c16S0x9e0: v1c16V9e0(0x0) = CONST 
    0x1c18S0x9e0: v1c18V9e0(0x40) = CONST 
    0x1c1aS0x9e0: v1c1aV9e0 = MLOAD v1c18V9e0(0x40)
    0x1c1dS0x9e0: v1c1dV9e0(0x0) = SUB v1c15V9e0, v1c1aV9e0
    0x1c22S0x9e0: v1c22V9e0 = CALL v1c11V9e0, v1bf2V9e0, v1c0dV9e0, v1c1aV9e0, v1c1dV9e0(0x0), v1c1aV9e0, v1c16V9e0(0x0)
    0x1c28S0x9e0: v1c28V9e0 = ISZERO v1c22V9e0
    0x1c29S0x9e0: v1c29V9e0 = ISZERO v1c28V9e0
    0x1c2aS0x9e0: v1c2aV9e0(0x1c32) = CONST 
    0x1c2dS0x9e0: JUMPI v1c2aV9e0(0x1c32), v1c29V9e0

    Begin block 0x1c2eB0x9e0
    prev=[0x1bb9B0x9e0], succ=[]
    =================================
    0x1c2eS0x9e0: v1c2eV9e0(0x0) = CONST 
    0x1c31S0x9e0: REVERT v1c2eV9e0(0x0), v1c2eV9e0(0x0)

    Begin block 0x1c32B0x9e0
    prev=[0x1bb9B0x9e0], succ=[0x9e8]
    =================================
    0x1c33S0x9e0: JUMP v9e1(0x9e8)

    Begin block 0x9e8
    prev=[0x1c32B0x9e0], succ=[]
    =================================
    0x9e9: STOP 

}

function fundingStopBlock()() public {
    Begin block 0x9ea
    prev=[], succ=[0x9f1, 0x9f5]
    =================================
    0x9eb: v9eb = CALLVALUE 
    0x9ec: v9ec = ISZERO v9eb
    0x9ed: v9ed(0x9f5) = CONST 
    0x9f0: JUMPI v9ed(0x9f5), v9ec

    Begin block 0x9f1
    prev=[0x9ea], succ=[]
    =================================
    0x9f1: v9f1(0x0) = CONST 
    0x9f4: REVERT v9f1(0x0), v9f1(0x0)

    Begin block 0x9f5
    prev=[0x9ea], succ=[0x1c34]
    =================================
    0x9f6: v9f6(0x9fd) = CONST 
    0x9f9: v9f9(0x1c34) = CONST 
    0x9fc: JUMP v9f9(0x1c34)

    Begin block 0x1c34
    prev=[0x9f5], succ=[0x9fd]
    =================================
    0x1c35: v1c35(0x7) = CONST 
    0x1c37: v1c37 = SLOAD v1c35(0x7)
    0x1c39: JUMP v9f6(0x9fd)

    Begin block 0x9fd
    prev=[0x1c34], succ=[]
    =================================
    0x9fe: v9fe(0x40) = CONST 
    0xa00: va00 = MLOAD v9fe(0x40)
    0xa04: MSTORE va00, v1c37
    0xa05: va05(0x20) = CONST 
    0xa07: va07 = ADD va05(0x20), va00
    0xa0b: va0b(0x40) = CONST 
    0xa0d: va0d = MLOAD va0b(0x40)
    0xa10: va10(0x20) = SUB va07, va0d
    0xa12: RETURN va0d, va10(0x20)

}

function 0xa13(va13arg0, va13arg1, va13arg2) private {
    Begin block 0xa13
    prev=[], succ=[0xa34, 0xa25]
    =================================
    0xa14: va14(0x0) = CONST 
    0xa19: va19 = MUL va13arg1, va13arg0
    0xa1c: va1c(0x0) = CONST 
    0xa1f: va1f = EQ va13arg1, va1c(0x0)
    0xa21: va21(0xa34) = CONST 
    0xa24: JUMPI va21(0xa34), va1f

    Begin block 0xa34
    prev=[0xa13, 0xa31], succ=[0xa3b, 0xa3c]
    =================================
    0xa34_0x0: va34_0 = PHI va1f, va33
    0xa35: va35 = ISZERO va34_0
    0xa36: va36 = ISZERO va35
    0xa37: va37(0xa3c) = CONST 
    0xa3a: JUMPI va37(0xa3c), va36

    Begin block 0xa3b
    prev=[0xa34], succ=[]
    =================================
    0xa3b: THROW 

    Begin block 0xa3c
    prev=[0xa34], succ=[]
    =================================
    0xa45: RETURNPRIVATE va13arg2, va19

    Begin block 0xa25
    prev=[0xa13], succ=[0xa30, 0xa31]
    =================================
    0xa2a: va2a = ISZERO va13arg1
    0xa2b: va2b = ISZERO va2a
    0xa2c: va2c(0xa31) = CONST 
    0xa2f: JUMPI va2c(0xa31), va2b

    Begin block 0xa30
    prev=[0xa25], succ=[]
    =================================
    0xa30: THROW 

    Begin block 0xa31
    prev=[0xa25], succ=[0xa34]
    =================================
    0xa32: va32 = DIV va19, va13arg1
    0xa33: va33 = EQ va32, va13arg0
    0x753e: v753e(0xa34) = CONST 
    0x755e: JUMP v753e(0xa34)

}

function 0xa46(va46arg0, va46arg1, va46arg2) private {
    Begin block 0xa46
    prev=[], succ=[0xa5e, 0xa59]
    =================================
    0xa47: va47(0x0) = CONST 
    0xa4c: va4c = ADD va46arg1, va46arg0
    0xa51: va51 = LT va4c, va46arg1
    0xa52: va52 = ISZERO va51
    0xa54: va54 = ISZERO va52
    0xa55: va55(0xa5e) = CONST 
    0xa58: JUMPI va55(0xa5e), va54

    Begin block 0xa5e
    prev=[0xa46, 0xa59], succ=[0xa65, 0xa66]
    =================================
    0xa5e_0x0: va5e_0 = PHI va52, va5d
    0xa5f: va5f = ISZERO va5e_0
    0xa60: va60 = ISZERO va5f
    0xa61: va61(0xa66) = CONST 
    0xa64: JUMPI va61(0xa66), va60

    Begin block 0xa65
    prev=[0xa5e], succ=[]
    =================================
    0xa65: THROW 

    Begin block 0xa66
    prev=[0xa5e], succ=[]
    =================================
    0xa6f: RETURNPRIVATE va46arg2, va4c

    Begin block 0xa59
    prev=[0xa46], succ=[0xa5e]
    =================================
    0xa5c: va5c = LT va4c, va46arg0
    0xa5d: va5d = ISZERO va5c
    0x7f3e: v7f3e(0xa5e) = CONST 
    0x7f5e: JUMP v7f3e(0xa5e)

}

function 0xd35(vd35arg0, vd35arg1, vd35arg2, vd35arg3) private {
    Begin block 0xd35
    prev=[], succ=[0xe02, 0xd81]
    =================================
    0xd36: vd36(0x0) = CONST 
    0xd39: vd39(0x1) = CONST 
    0xd3b: vd3b(0x0) = CONST 
    0xd3e: vd3e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd53: vd53 = AND vd3e(0xffffffffffffffffffffffffffffffffffffffff), vd35arg2
    0xd54: vd54(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd69: vd69 = AND vd54(0xffffffffffffffffffffffffffffffffffffffff), vd53
    0xd6b: MSTORE vd3b(0x0), vd69
    0xd6c: vd6c(0x20) = CONST 
    0xd6e: vd6e(0x20) = ADD vd6c(0x20), vd3b(0x0)
    0xd71: MSTORE vd6e(0x20), vd39(0x1)
    0xd72: vd72(0x20) = CONST 
    0xd74: vd74(0x40) = ADD vd72(0x20), vd6e(0x20)
    0xd75: vd75(0x0) = CONST 
    0xd77: vd77 = SHA3 vd75(0x0), vd74(0x40)
    0xd78: vd78 = SLOAD vd77
    0xd79: vd79 = LT vd78, vd35arg0
    0xd7a: vd7a = ISZERO vd79
    0xd7c: vd7c = ISZERO vd7a
    0xd7d: vd7d(0xe02) = CONST 
    0xd80: JUMPI vd7d(0xe02), vd7c

    Begin block 0xe02
    prev=[0xd35, 0xd81], succ=[0xe0e, 0xe09]
    =================================
    0xe02_0x0: ve02_0 = PHI vd7a, ve01
    0xe04: ve04 = ISZERO ve02_0
    0xe05: ve05(0xe0e) = CONST 
    0xe08: JUMPI ve05(0xe0e), ve04

    Begin block 0xe0e
    prev=[0xe02, 0xe09], succ=[0xfa5, 0xe14]
    =================================
    0xe0e_0x0: ve0e_0 = PHI vd7a, ve01, ve0d
    0xe0f: ve0f = ISZERO ve0e_0
    0xe10: ve10(0xfa5) = CONST 
    0xe13: JUMPI ve10(0xfa5), ve0f

    Begin block 0xfa5
    prev=[0xe0e], succ=[0x18b75]
    =================================
    0xfa6: vfa6(0x0) = CONST 
    0x9d3e: v9d3e(0x18b75) = CONST 
    0x9d5e: JUMP v9d3e(0x18b75)

    Begin block 0x18b75
    prev=[0xfa5], succ=[]
    =================================
    0x18b7b: RETURNPRIVATE vd35arg3, vfa6(0x0)

    Begin block 0xe14
    prev=[0xe0e], succ=[0x18adc]
    =================================
    0xe15: ve15(0x1) = CONST 
    0xe17: ve17(0x0) = CONST 
    0xe1a: ve1a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe2f: ve2f = AND ve1a(0xffffffffffffffffffffffffffffffffffffffff), vd35arg1
    0xe30: ve30(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe45: ve45 = AND ve30(0xffffffffffffffffffffffffffffffffffffffff), ve2f
    0xe47: MSTORE ve17(0x0), ve45
    0xe48: ve48(0x20) = CONST 
    0xe4a: ve4a(0x20) = ADD ve48(0x20), ve17(0x0)
    0xe4d: MSTORE ve4a(0x20), ve15(0x1)
    0xe4e: ve4e(0x20) = CONST 
    0xe50: ve50(0x40) = ADD ve4e(0x20), ve4a(0x20)
    0xe51: ve51(0x0) = CONST 
    0xe53: ve53 = SHA3 ve51(0x0), ve50(0x40)
    0xe54: ve54(0x0) = CONST 
    0xe58: ve58 = SLOAD ve53
    0xe59: ve59 = ADD ve58, vd35arg0
    0xe5f: SSTORE ve53, ve59
    0xe62: ve62(0x1) = CONST 
    0xe64: ve64(0x0) = CONST 
    0xe67: ve67(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe7c: ve7c = AND ve67(0xffffffffffffffffffffffffffffffffffffffff), vd35arg2
    0xe7d: ve7d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe92: ve92 = AND ve7d(0xffffffffffffffffffffffffffffffffffffffff), ve7c
    0xe94: MSTORE ve64(0x0), ve92
    0xe95: ve95(0x20) = CONST 
    0xe97: ve97(0x20) = ADD ve95(0x20), ve64(0x0)
    0xe9a: MSTORE ve97(0x20), ve62(0x1)
    0xe9b: ve9b(0x20) = CONST 
    0xe9d: ve9d(0x40) = ADD ve9b(0x20), ve97(0x20)
    0xe9e: ve9e(0x0) = CONST 
    0xea0: vea0 = SHA3 ve9e(0x0), ve9d(0x40)
    0xea1: vea1(0x0) = CONST 
    0xea5: vea5 = SLOAD vea0
    0xea6: vea6 = SUB vea5, vd35arg0
    0xeac: SSTORE vea0, vea6
    0xeaf: veaf(0x2) = CONST 
    0xeb1: veb1(0x0) = CONST 
    0xeb4: veb4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec9: vec9 = AND veb4(0xffffffffffffffffffffffffffffffffffffffff), vd35arg2
    0xeca: veca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xedf: vedf = AND veca(0xffffffffffffffffffffffffffffffffffffffff), vec9
    0xee1: MSTORE veb1(0x0), vedf
    0xee2: vee2(0x20) = CONST 
    0xee4: vee4(0x20) = ADD vee2(0x20), veb1(0x0)
    0xee7: MSTORE vee4(0x20), veaf(0x2)
    0xee8: vee8(0x20) = CONST 
    0xeea: veea(0x40) = ADD vee8(0x20), vee4(0x20)
    0xeeb: veeb(0x0) = CONST 
    0xeed: veed = SHA3 veeb(0x0), veea(0x40)
    0xeee: veee(0x0) = CONST 
    0xef0: vef0 = CALLER 
    0xef1: vef1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf06: vf06 = AND vef1(0xffffffffffffffffffffffffffffffffffffffff), vef0
    0xf07: vf07(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf1c: vf1c = AND vf07(0xffffffffffffffffffffffffffffffffffffffff), vf06
    0xf1e: MSTORE veee(0x0), vf1c
    0xf1f: vf1f(0x20) = CONST 
    0xf21: vf21(0x20) = ADD vf1f(0x20), veee(0x0)
    0xf24: MSTORE vf21(0x20), veed
    0xf25: vf25(0x20) = CONST 
    0xf27: vf27(0x40) = ADD vf25(0x20), vf21(0x20)
    0xf28: vf28(0x0) = CONST 
    0xf2a: vf2a = SHA3 vf28(0x0), vf27(0x40)
    0xf2b: vf2b(0x0) = CONST 
    0xf2f: vf2f = SLOAD vf2a
    0xf30: vf30 = SUB vf2f, vd35arg0
    0xf36: SSTORE vf2a, vf30
    0xf39: vf39(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf4e: vf4e = AND vf39(0xffffffffffffffffffffffffffffffffffffffff), vd35arg1
    0xf50: vf50(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf65: vf65 = AND vf50(0xffffffffffffffffffffffffffffffffffffffff), vd35arg2
    0xf66: vf66(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xf88: vf88(0x40) = CONST 
    0xf8a: vf8a = MLOAD vf88(0x40)
    0xf8e: MSTORE vf8a, vd35arg0
    0xf8f: vf8f(0x20) = CONST 
    0xf91: vf91 = ADD vf8f(0x20), vf8a
    0xf95: vf95(0x40) = CONST 
    0xf97: vf97 = MLOAD vf95(0x40)
    0xf9a: vf9a(0x20) = SUB vf91, vf97
    0xf9c: LOG3 vf97, vf9a(0x20), vf66(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vf65, vf4e
    0xf9d: vf9d(0x1) = CONST 
    0xfa1: vfa1(0x18adc) = CONST 
    0xfa4: JUMP vfa1(0x18adc)

    Begin block 0x18adc
    prev=[0xe14], succ=[]
    =================================
    0x18ae2: RETURNPRIVATE vd35arg3, vf9d(0x1)

    Begin block 0xe09
    prev=[0xe02], succ=[0xe0e]
    =================================
    0xe0a: ve0a(0x0) = CONST 
    0xe0d: ve0d = GT vd35arg0, ve0a(0x0)
    0x933e: v933e(0xe0e) = CONST 
    0x935e: JUMP v933e(0xe0e)

    Begin block 0xd81
    prev=[0xd35], succ=[0xe02]
    =================================
    0xd83: vd83(0x2) = CONST 
    0xd85: vd85(0x0) = CONST 
    0xd88: vd88(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd9d: vd9d = AND vd88(0xffffffffffffffffffffffffffffffffffffffff), vd35arg2
    0xd9e: vd9e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdb3: vdb3 = AND vd9e(0xffffffffffffffffffffffffffffffffffffffff), vd9d
    0xdb5: MSTORE vd85(0x0), vdb3
    0xdb6: vdb6(0x20) = CONST 
    0xdb8: vdb8(0x20) = ADD vdb6(0x20), vd85(0x0)
    0xdbb: MSTORE vdb8(0x20), vd83(0x2)
    0xdbc: vdbc(0x20) = CONST 
    0xdbe: vdbe(0x40) = ADD vdbc(0x20), vdb8(0x20)
    0xdbf: vdbf(0x0) = CONST 
    0xdc1: vdc1 = SHA3 vdbf(0x0), vdbe(0x40)
    0xdc2: vdc2(0x0) = CONST 
    0xdc4: vdc4 = CALLER 
    0xdc5: vdc5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdda: vdda = AND vdc5(0xffffffffffffffffffffffffffffffffffffffff), vdc4
    0xddb: vddb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf0: vdf0 = AND vddb(0xffffffffffffffffffffffffffffffffffffffff), vdda
    0xdf2: MSTORE vdc2(0x0), vdf0
    0xdf3: vdf3(0x20) = CONST 
    0xdf5: vdf5(0x20) = ADD vdf3(0x20), vdc2(0x0)
    0xdf8: MSTORE vdf5(0x20), vdc1
    0xdf9: vdf9(0x20) = CONST 
    0xdfb: vdfb(0x40) = ADD vdf9(0x20), vdf5(0x20)
    0xdfc: vdfc(0x0) = CONST 
    0xdfe: vdfe = SHA3 vdfc(0x0), vdfb(0x40)
    0xdff: vdff = SLOAD vdfe
    0xe00: ve00 = LT vdff, vd35arg0
    0xe01: ve01 = ISZERO ve00
    0x893e: v893e(0xe02) = CONST 
    0x895e: JUMP v893e(0xe02)

}

