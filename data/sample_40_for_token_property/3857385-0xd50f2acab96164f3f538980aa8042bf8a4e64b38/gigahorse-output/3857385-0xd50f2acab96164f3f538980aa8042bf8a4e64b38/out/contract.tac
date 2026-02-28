function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xb, 0x10f]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5 = CALLDATASIZE 
    0x6: v6 = ISZERO v5
    0x7: v7(0x10f) = CONST 
    0xa: JUMPI v7(0x10f), v6

    Begin block 0xb
    prev=[0x0], succ=[0xb3112, 0x3e]
    =================================
    0xb: vb(0xffffffff) = CONST 
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2e: v2e(0x0) = CONST 
    0x30: v30 = CALLDATALOAD v2e(0x0)
    0x31: v31 = DIV v30, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x32: v32 = AND v31, vb(0xffffffff)
    0x33: v33(0x6fdde03) = CONST 
    0x39: v39 = EQ v32, v33(0x6fdde03)
    0xa6912: va6912(0xb3112) = CONST 
    0xa6932: JUMPI va6912(0xb3112), v39

    Begin block 0xb3112
    prev=[0xb], succ=[]
    =================================
    0xb3132: vb3132(0x120) = CONST 
    0xb3152: CALLPRIVATE vb3132(0x120)

    Begin block 0x3e
    prev=[0xb], succ=[0xb3b12, 0x49]
    =================================
    0x3f: v3f(0x95ea7b3) = CONST 
    0x44: v44 = EQ v3f(0x95ea7b3), v32
    0xa7312: va7312(0xb3b12) = CONST 
    0xa7332: JUMPI va7312(0xb3b12), v44

    Begin block 0xb3b12
    prev=[0x3e], succ=[]
    =================================
    0xb3b32: vb3b32(0x1b0) = CONST 
    0xb3b52: CALLPRIVATE vb3b32(0x1b0)

    Begin block 0x49
    prev=[0x3e], succ=[0xb4512, 0x54]
    =================================
    0x4a: v4a(0x18160ddd) = CONST 
    0x4f: v4f = EQ v4a(0x18160ddd), v32
    0xa7d12: va7d12(0xb4512) = CONST 
    0xa7d32: JUMPI va7d12(0xb4512), v4f

    Begin block 0xb4512
    prev=[0x49], succ=[]
    =================================
    0xb4532: vb4532(0x1e3) = CONST 
    0xb4552: CALLPRIVATE vb4532(0x1e3)

    Begin block 0x54
    prev=[0x49], succ=[0xb4f12, 0x5f]
    =================================
    0x55: v55(0x23b872dd) = CONST 
    0x5a: v5a = EQ v55(0x23b872dd), v32
    0xa8712: va8712(0xb4f12) = CONST 
    0xa8732: JUMPI va8712(0xb4f12), v5a

    Begin block 0xb4f12
    prev=[0x54], succ=[]
    =================================
    0xb4f32: vb4f32(0x205) = CONST 
    0xb4f52: CALLPRIVATE vb4f32(0x205)

    Begin block 0x5f
    prev=[0x54], succ=[0xb5912, 0x6a]
    =================================
    0x60: v60(0x313ce567) = CONST 
    0x65: v65 = EQ v60(0x313ce567), v32
    0xa9112: va9112(0xb5912) = CONST 
    0xa9132: JUMPI va9112(0xb5912), v65

    Begin block 0xb5912
    prev=[0x5f], succ=[]
    =================================
    0xb5932: vb5932(0x23e) = CONST 
    0xb5952: CALLPRIVATE vb5932(0x23e)

    Begin block 0x6a
    prev=[0x5f], succ=[0xb6312, 0x75]
    =================================
    0x6b: v6b(0x31711884) = CONST 
    0x70: v70 = EQ v6b(0x31711884), v32
    0xa9b12: va9b12(0xb6312) = CONST 
    0xa9b32: JUMPI va9b12(0xb6312), v70

    Begin block 0xb6312
    prev=[0x6a], succ=[]
    =================================
    0xb6332: vb6332(0x260) = CONST 
    0xb6352: CALLPRIVATE vb6332(0x260)

    Begin block 0x75
    prev=[0x6a], succ=[0xb6d12, 0x80]
    =================================
    0x76: v76(0x31de7e72) = CONST 
    0x7b: v7b = EQ v76(0x31de7e72), v32
    0xaa512: vaa512(0xb6d12) = CONST 
    0xaa532: JUMPI vaa512(0xb6d12), v7b

    Begin block 0xb6d12
    prev=[0x75], succ=[]
    =================================
    0xb6d32: vb6d32(0x282) = CONST 
    0xb6d52: CALLPRIVATE vb6d32(0x282)

    Begin block 0x80
    prev=[0x75], succ=[0xb7712, 0x8b]
    =================================
    0x81: v81(0x4bb278f3) = CONST 
    0x86: v86 = EQ v81(0x4bb278f3), v32
    0xaaf12: vaaf12(0xb7712) = CONST 
    0xaaf32: JUMPI vaaf12(0xb7712), v86

    Begin block 0xb7712
    prev=[0x80], succ=[]
    =================================
    0xb7732: vb7732(0x2a4) = CONST 
    0xb7752: CALLPRIVATE vb7732(0x2a4)

    Begin block 0x8b
    prev=[0x80], succ=[0xb8112, 0x96]
    =================================
    0x8c: v8c(0x54fd4d50) = CONST 
    0x91: v91 = EQ v8c(0x54fd4d50), v32
    0xab912: vab912(0xb8112) = CONST 
    0xab932: JUMPI vab912(0xb8112), v91

    Begin block 0xb8112
    prev=[0x8b], succ=[]
    =================================
    0xb8132: vb8132(0x2b6) = CONST 
    0xb8152: CALLPRIVATE vb8132(0x2b6)

    Begin block 0x96
    prev=[0x8b], succ=[0xb8b12, 0xa1]
    =================================
    0x97: v97(0x6f7920fd) = CONST 
    0x9c: v9c = EQ v97(0x6f7920fd), v32
    0xac312: vac312(0xb8b12) = CONST 
    0xac332: JUMPI vac312(0xb8b12), v9c

    Begin block 0xb8b12
    prev=[0x96], succ=[]
    =================================
    0xb8b32: vb8b32(0x346) = CONST 
    0xb8b52: CALLPRIVATE vb8b32(0x346)

    Begin block 0xa1
    prev=[0x96], succ=[0xb9512, 0xac]
    =================================
    0xa2: va2(0x70a08231) = CONST 
    0xa7: va7 = EQ va2(0x70a08231), v32
    0xacd12: vacd12(0xb9512) = CONST 
    0xacd32: JUMPI vacd12(0xb9512), va7

    Begin block 0xb9512
    prev=[0xa1], succ=[]
    =================================
    0xb9532: vb9532(0x368) = CONST 
    0xb9552: CALLPRIVATE vb9532(0x368)

    Begin block 0xac
    prev=[0xa1], succ=[0xb9f12, 0xb7]
    =================================
    0xad: vad(0x73cc3ec7) = CONST 
    0xb2: vb2 = EQ vad(0x73cc3ec7), v32
    0xad712: vad712(0xb9f12) = CONST 
    0xad732: JUMPI vad712(0xb9f12), vb2

    Begin block 0xb9f12
    prev=[0xac], succ=[]
    =================================
    0xb9f32: vb9f32(0x396) = CONST 
    0xb9f52: CALLPRIVATE vb9f32(0x396)

    Begin block 0xb7
    prev=[0xac], succ=[0xba912, 0xc2]
    =================================
    0xb8: vb8(0x8d4e4083) = CONST 
    0xbd: vbd = EQ vb8(0x8d4e4083), v32
    0xae112: vae112(0xba912) = CONST 
    0xae132: JUMPI vae112(0xba912), vbd

    Begin block 0xba912
    prev=[0xb7], succ=[]
    =================================
    0xba932: vba932(0x3c2) = CONST 
    0xba952: CALLPRIVATE vba932(0x3c2)

    Begin block 0xc2
    prev=[0xb7], succ=[0xbb312, 0xcd]
    =================================
    0xc3: vc3(0x91b43d13) = CONST 
    0xc8: vc8 = EQ vc3(0x91b43d13), v32
    0xaeb12: vaeb12(0xbb312) = CONST 
    0xaeb32: JUMPI vaeb12(0xbb312), vc8

    Begin block 0xbb312
    prev=[0xc2], succ=[]
    =================================
    0xbb332: vbb332(0x3e6) = CONST 
    0xbb352: CALLPRIVATE vbb332(0x3e6)

    Begin block 0xcd
    prev=[0xc2], succ=[0xbbd12, 0xd8]
    =================================
    0xce: vce(0x95d89b41) = CONST 
    0xd3: vd3 = EQ vce(0x95d89b41), v32
    0xaf512: vaf512(0xbbd12) = CONST 
    0xaf532: JUMPI vaf512(0xbbd12), vd3

    Begin block 0xbbd12
    prev=[0xcd], succ=[]
    =================================
    0xbbd32: vbbd32(0x408) = CONST 
    0xbbd52: CALLPRIVATE vbbd32(0x408)

    Begin block 0xd8
    prev=[0xcd], succ=[0xbc712, 0xe3]
    =================================
    0xd9: vd9(0xa81c3bdf) = CONST 
    0xde: vde = EQ vd9(0xa81c3bdf), v32
    0xaff12: vaff12(0xbc712) = CONST 
    0xaff32: JUMPI vaff12(0xbc712), vde

    Begin block 0xbc712
    prev=[0xd8], succ=[]
    =================================
    0xbc732: vbc732(0x498) = CONST 
    0xbc752: CALLPRIVATE vbc732(0x498)

    Begin block 0xe3
    prev=[0xd8], succ=[0xbd112, 0xee]
    =================================
    0xe4: ve4(0xa9059cbb) = CONST 
    0xe9: ve9 = EQ ve4(0xa9059cbb), v32
    0xb0912: vb0912(0xbd112) = CONST 
    0xb0932: JUMPI vb0912(0xbd112), ve9

    Begin block 0xbd112
    prev=[0xe3], succ=[]
    =================================
    0xbd132: vbd132(0x4c4) = CONST 
    0xbd152: CALLPRIVATE vbd132(0x4c4)

    Begin block 0xee
    prev=[0xe3], succ=[0xbdb12, 0xf9]
    =================================
    0xef: vef(0xbe28f5db) = CONST 
    0xf4: vf4 = EQ vef(0xbe28f5db), v32
    0xb1312: vb1312(0xbdb12) = CONST 
    0xb1332: JUMPI vb1312(0xbdb12), vf4

    Begin block 0xbdb12
    prev=[0xee], succ=[]
    =================================
    0xbdb32: vbdb32(0x4f7) = CONST 
    0xbdb52: CALLPRIVATE vbdb32(0x4f7)

    Begin block 0xf9
    prev=[0xee], succ=[0xbe512, 0x104]
    =================================
    0xfa: vfa(0xd648a647) = CONST 
    0xff: vff = EQ vfa(0xd648a647), v32
    0xb1d12: vb1d12(0xbe512) = CONST 
    0xb1d32: JUMPI vb1d12(0xbe512), vff

    Begin block 0xbe512
    prev=[0xf9], succ=[]
    =================================
    0xbe532: vbe532(0x501) = CONST 
    0xbe552: CALLPRIVATE vbe532(0x501)

    Begin block 0x104
    prev=[0xf9], succ=[0x10f, 0xbef12]
    =================================
    0x105: v105(0xdd62ed3e) = CONST 
    0x10a: v10a = EQ v105(0xdd62ed3e), v32
    0xb2712: vb2712(0xbef12) = CONST 
    0xb2732: JUMPI vb2712(0xbef12), v10a

    Begin block 0x10f
    prev=[0x0, 0x104], succ=[0x113B0x10f]
    =================================
    0x110: v110(0x22298) = CONST 
    0x171c: v171c(0x113) = CONST 
    0x173c: JUMP v171c(0x113)

    Begin block 0x113B0x10f
    prev=[0x10f], succ=[0x222b9B0x10f]
    =================================
    0x114S0x10f: v114V10f(0x222b9) = CONST 
    0x117S0x10f: v117V10f(0x557) = CONST 
    0x11aS0x10f: CALLPRIVATE v117V10f(0x557), v114V10f(0x222b9)

    Begin block 0x222b9B0x10f
    prev=[0x113B0x10f], succ=[0x533bfB0x10f]
    =================================
    0x242baS0x10f: v242baV10f(0x533bf) = CONST 
    0x242daS0x10f: JUMP v242baV10f(0x533bf)

    Begin block 0x533bfB0x10f
    prev=[0x222b9B0x10f], succ=[0x22298]
    =================================
    0x533c0S0x10f: JUMP v110(0x22298)

    Begin block 0x22298
    prev=[0x533bfB0x10f], succ=[]
    =================================
    0x22299: STOP 

    Begin block 0xbef12
    prev=[0x104], succ=[]
    =================================
    0xbef32: vbef32(0x523) = CONST 
    0xbef52: CALLPRIVATE vbef32(0x523)

}

function name()() public {
    Begin block 0x120
    prev=[], succ=[0x127, 0x128]
    =================================
    0x121: v121 = CALLVALUE 
    0x122: v122 = ISZERO v121
    0x123: v123(0x128) = CONST 
    0x126: JUMPI v123(0x128), v122

    Begin block 0x127
    prev=[0x120], succ=[]
    =================================
    0x127: THROW 

    Begin block 0x128
    prev=[0x120], succ=[0x63a]
    =================================
    0x129: v129(0x130) = CONST 
    0x12c: v12c(0x63a) = CONST 
    0x12f: JUMP v12c(0x63a)

    Begin block 0x63a
    prev=[0x128], succ=[0x1300x120]
    =================================
    0x63b: v63b(0x40) = CONST 
    0x63e: v63e = MLOAD v63b(0x40)
    0x641: v641 = ADD v63b(0x40), v63e
    0x644: MSTORE v63b(0x40), v641
    0x645: v645(0x5) = CONST 
    0x648: MSTORE v63e, v645(0x5)
    0x649: v649(0x4944494345000000000000000000000000000000000000000000000000000000) = CONST 
    0x66a: v66a(0x20) = CONST 
    0x66d: v66d = ADD v63e, v66a(0x20)
    0x66e: MSTORE v66d, v649(0x4944494345000000000000000000000000000000000000000000000000000000)
    0x670: JUMP v129(0x130)

    Begin block 0x1300x120
    prev=[0x63a], succ=[0x1760x120, 0x1560x120]
    =================================
    0x1310x120: v120131(0x40) = CONST 
    0x1340x120: v120134 = MLOAD v120131(0x40)
    0x1350x120: v120135(0x20) = CONST 
    0x1390x120: MSTORE v120134, v120135(0x20)
    0x13b0x120: v12013b(0x5) = MLOAD v63e
    0x13e0x120: v12013e = ADD v120134, v120135(0x20)
    0x13f0x120: MSTORE v12013e, v12013b(0x5)
    0x1410x120: v120141(0x5) = MLOAD v63e
    0x1480x120: v120148 = ADD v120134, v120131(0x40)
    0x14b0x120: v12014b = ADD v63e, v120135(0x20)
    0x1510x120: v120151(0x0) = ISZERO v120141(0x5)
    0x1520x120: v120152(0x176) = CONST 
    0x1550x120: JUMPI v120152(0x176), v120151(0x0)

    Begin block 0x1760x120
    prev=[0x1560x120, 0x1300x120], succ=[0x1890x120, 0x1a20x120]
    =================================
    0x17e0x120: v12017e = ADD v120141(0x5), v120148
    0x1800x120: v120180(0x1f) = CONST 
    0x1820x120: v120182(0x5) = AND v120180(0x1f), v120141(0x5)
    0x1840x120: v120184(0x0) = ISZERO v120182(0x5)
    0x1850x120: v120185(0x1a2) = CONST 
    0x1880x120: JUMPI v120185(0x1a2), v120184(0x0)

    Begin block 0x1890x120
    prev=[0x1760x120], succ=[0x1a20x120]
    =================================
    0x18b0x120: v12018b = SUB v12017e, v120182(0x5)
    0x18d0x120: v12018d = MLOAD v12018b
    0x18e0x120: v12018e(0x1) = CONST 
    0x1910x120: v120191(0x20) = CONST 
    0x1930x120: v120193(0x1b) = SUB v120191(0x20), v120182(0x5)
    0x1940x120: v120194(0x100) = CONST 
    0x1970x120: v120197(0x1000000000000000000000000000000000000000000000000000000) = EXP v120194(0x100), v120193(0x1b)
    0x1980x120: v120198(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v120197(0x1000000000000000000000000000000000000000000000000000000), v12018e(0x1)
    0x1990x120: v120199(0xffffffffff000000000000000000000000000000000000000000000000000000) = NOT v120198(0xffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x19a0x120: v12019a = AND v120199(0xffffffffff000000000000000000000000000000000000000000000000000000), v12018d
    0x19c0x120: MSTORE v12018b, v12019a
    0x19d0x120: v12019d(0x20) = CONST 
    0x19f0x120: v12019f = ADD v12019d(0x20), v12018b
    0x2b1c0x120: v1202b1c(0x1a2) = CONST 
    0x2b3c0x120: JUMP v1202b1c(0x1a2)

    Begin block 0x1a20x120
    prev=[0x1890x120, 0x1760x120], succ=[]
    =================================
    0x1a20x120_0x1: v1a2120_1 = PHI v12019f, v12017e
    0x1a80x120: v1201a8(0x40) = CONST 
    0x1aa0x120: v1201aa = MLOAD v1201a8(0x40)
    0x1ad0x120: v1201ad = SUB v1a2120_1, v1201aa
    0x1af0x120: RETURN v1201aa, v1201ad

    Begin block 0x1560x120
    prev=[0x1640x120, 0x1300x120], succ=[0x1640x120, 0x1760x120]
    =================================
    0x1560x120_0x0: v156120_0 = PHI v120171, v12014b
    0x1560x120_0x1: v156120_1 = PHI v12016f, v120148
    0x1560x120_0x2: v156120_2 = PHI v120169, v120141(0x5)
    0x1580x120: v120158 = MLOAD v156120_0
    0x15a0x120: MSTORE v156120_1, v120158
    0x15b0x120: v12015b(0x20) = CONST 
    0x15e0x120: v12015e = GT v156120_2, v12015b(0x20)
    0x15f0x120: v12015f = ISZERO v12015e
    0x1600x120: v120160(0x176) = CONST 
    0x1630x120: JUMPI v120160(0x176), v12015f

    Begin block 0x1640x120
    prev=[0x1560x120], succ=[0x1560x120]
    =================================
    0x1640x120_0x0: v164120_0 = PHI v120171, v12014b
    0x1640x120_0x1: v164120_1 = PHI v12016f, v120148
    0x1640x120_0x2: v164120_2 = PHI v120169, v120141(0x5)
    0x1640x120: v120164(0x1f) = CONST 
    0x1660x120: v120166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v120164(0x1f)
    0x1690x120: v120169 = ADD v164120_2, v120166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x16b0x120: v12016b(0x20) = CONST 
    0x16f0x120: v12016f = ADD v12016b(0x20), v164120_1
    0x1710x120: v120171 = ADD v12016b(0x20), v164120_0
    0x1720x120: v120172(0x156) = CONST 
    0x1750x120: JUMP v120172(0x156)

}

function approve(address,uint256)() public {
    Begin block 0x1b0
    prev=[], succ=[0x1b7, 0x1b8]
    =================================
    0x1b1: v1b1 = CALLVALUE 
    0x1b2: v1b2 = ISZERO v1b1
    0x1b3: v1b3(0x1b8) = CONST 
    0x1b6: JUMPI v1b3(0x1b8), v1b2

    Begin block 0x1b7
    prev=[0x1b0], succ=[]
    =================================
    0x1b7: THROW 

    Begin block 0x1b8
    prev=[0x1b0], succ=[0x671B0x1b8]
    =================================
    0x1b9: v1b9(0x242fa) = CONST 
    0x1bc: v1bc(0x1) = CONST 
    0x1be: v1be(0xa0) = CONST 
    0x1c0: v1c0(0x2) = CONST 
    0x1c2: v1c2(0x10000000000000000000000000000000000000000) = EXP v1c0(0x2), v1be(0xa0)
    0x1c3: v1c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c2(0x10000000000000000000000000000000000000000), v1bc(0x1)
    0x1c4: v1c4(0x4) = CONST 
    0x1c6: v1c6 = CALLDATALOAD v1c4(0x4)
    0x1c7: v1c7 = AND v1c6, v1c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c8: v1c8(0x24) = CONST 
    0x1ca: v1ca = CALLDATALOAD v1c8(0x24)
    0x1cb: v1cb(0x671) = CONST 
    0x1ce: JUMP v1cb(0x671)

    Begin block 0x671B0x1b8
    prev=[0x1b8], succ=[0x4bf79B0x1b8]
    =================================
    0x672S0x1b8: v672V1b8(0x1) = CONST 
    0x674S0x1b8: v674V1b8(0xa0) = CONST 
    0x676S0x1b8: v676V1b8(0x2) = CONST 
    0x678S0x1b8: v678V1b8(0x10000000000000000000000000000000000000000) = EXP v676V1b8(0x2), v674V1b8(0xa0)
    0x679S0x1b8: v679V1b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v678V1b8(0x10000000000000000000000000000000000000000), v672V1b8(0x1)
    0x67aS0x1b8: v67aV1b8 = CALLER 
    0x67cS0x1b8: v67cV1b8 = AND v679V1b8(0xffffffffffffffffffffffffffffffffffffffff), v67aV1b8
    0x67dS0x1b8: v67dV1b8(0x0) = CONST 
    0x681S0x1b8: MSTORE v67dV1b8(0x0), v67cV1b8
    0x682S0x1b8: v682V1b8(0x2) = CONST 
    0x684S0x1b8: v684V1b8(0x20) = CONST 
    0x688S0x1b8: MSTORE v684V1b8(0x20), v682V1b8(0x2)
    0x689S0x1b8: v689V1b8(0x40) = CONST 
    0x68dS0x1b8: v68dV1b8 = SHA3 v67dV1b8(0x0), v689V1b8(0x40)
    0x690S0x1b8: v690V1b8 = AND v1c7, v679V1b8(0xffffffffffffffffffffffffffffffffffffffff)
    0x693S0x1b8: MSTORE v67dV1b8(0x0), v690V1b8
    0x696S0x1b8: MSTORE v684V1b8(0x20), v68dV1b8
    0x699S0x1b8: v699V1b8 = SHA3 v67dV1b8(0x0), v689V1b8(0x40)
    0x69cS0x1b8: SSTORE v699V1b8, v1ca
    0x69eS0x1b8: v69eV1b8 = MLOAD v689V1b8(0x40)
    0x6a1S0x1b8: MSTORE v69eV1b8, v1ca
    0x6a3S0x1b8: v6a3V1b8 = MLOAD v689V1b8(0x40)
    0x6a8S0x1b8: v6a8V1b8(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x6cdS0x1b8: v6cdV1b8(0x0) = SUB v69eV1b8, v6a3V1b8
    0x6d0S0x1b8: v6d0V1b8(0x20) = ADD v684V1b8(0x20), v6cdV1b8(0x0)
    0x6d2S0x1b8: LOG3 v6a3V1b8, v6d0V1b8(0x20), v6a8V1b8(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v67cV1b8, v690V1b8
    0x6d4S0x1b8: v6d4V1b8(0x1) = CONST 
    0x531cS0x1b8: v531cV1b8(0x4bf79) = CONST 
    0x533cS0x1b8: JUMP v531cV1b8(0x4bf79)

    Begin block 0x4bf79B0x1b8
    prev=[0x671B0x1b8], succ=[0x242fa]
    =================================
    0x4bf7eS0x1b8: JUMP v1b9(0x242fa)

    Begin block 0x242fa
    prev=[0x4bf79B0x1b8], succ=[]
    =================================
    0x242fb: v242fb(0x40) = CONST 
    0x242fe: v242fe = MLOAD v242fb(0x40)
    0x24300: v24300(0x0) = ISZERO v6d4V1b8(0x1)
    0x24301: v24301(0x1) = ISZERO v24300(0x0)
    0x24303: MSTORE v242fe, v24301(0x1)
    0x24304: v24304 = MLOAD v242fb(0x40)
    0x24308: v24308(0x0) = SUB v242fe, v24304
    0x24309: v24309(0x20) = CONST 
    0x2430b: v2430b(0x20) = ADD v24309(0x20), v24308(0x0)
    0x2430d: RETURN v24304, v2430b(0x20)

}

function totalSupply()() public {
    Begin block 0x1e3
    prev=[], succ=[0x1ea, 0x1eb]
    =================================
    0x1e4: v1e4 = CALLVALUE 
    0x1e5: v1e5 = ISZERO v1e4
    0x1e6: v1e6(0x1eb) = CONST 
    0x1e9: JUMPI v1e6(0x1eb), v1e5

    Begin block 0x1ea
    prev=[0x1e3], succ=[]
    =================================
    0x1ea: THROW 

    Begin block 0x1eb
    prev=[0x1e3], succ=[0x6dc]
    =================================
    0x1ec: v1ec(0x2432d) = CONST 
    0x1ef: v1ef(0x6dc) = CONST 
    0x1f2: JUMP v1ef(0x6dc)

    Begin block 0x6dc
    prev=[0x1eb], succ=[0x2432d]
    =================================
    0x6dd: v6dd(0x0) = CONST 
    0x6df: v6df = SLOAD v6dd(0x0)
    0x6e1: JUMP v1ec(0x2432d)

    Begin block 0x2432d
    prev=[0x6dc], succ=[]
    =================================
    0x2432e: v2432e(0x40) = CONST 
    0x24331: v24331 = MLOAD v2432e(0x40)
    0x24334: MSTORE v24331, v6df
    0x24335: v24335 = MLOAD v2432e(0x40)
    0x24339: v24339(0x0) = SUB v24331, v24335
    0x2433a: v2433a(0x20) = CONST 
    0x2433c: v2433c(0x20) = ADD v2433a(0x20), v24339(0x0)
    0x2433e: RETURN v24335, v2433c(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x205
    prev=[], succ=[0x20c, 0x20d]
    =================================
    0x206: v206 = CALLVALUE 
    0x207: v207 = ISZERO v206
    0x208: v208(0x20d) = CONST 
    0x20b: JUMPI v208(0x20d), v207

    Begin block 0x20c
    prev=[0x205], succ=[]
    =================================
    0x20c: THROW 

    Begin block 0x20d
    prev=[0x205], succ=[0x6e2B0x20d]
    =================================
    0x20e: v20e(0x2435e) = CONST 
    0x211: v211(0x1) = CONST 
    0x213: v213(0xa0) = CONST 
    0x215: v215(0x2) = CONST 
    0x217: v217(0x10000000000000000000000000000000000000000) = EXP v215(0x2), v213(0xa0)
    0x218: v218(0xffffffffffffffffffffffffffffffffffffffff) = SUB v217(0x10000000000000000000000000000000000000000), v211(0x1)
    0x219: v219(0x4) = CONST 
    0x21b: v21b = CALLDATALOAD v219(0x4)
    0x21d: v21d = AND v218(0xffffffffffffffffffffffffffffffffffffffff), v21b
    0x21f: v21f(0x24) = CONST 
    0x221: v221 = CALLDATALOAD v21f(0x24)
    0x222: v222 = AND v221, v218(0xffffffffffffffffffffffffffffffffffffffff)
    0x223: v223(0x44) = CONST 
    0x225: v225 = CALLDATALOAD v223(0x44)
    0x226: v226(0x6e2) = CONST 
    0x229: JUMP v226(0x6e2)

    Begin block 0x6e2B0x20d
    prev=[0x20d], succ=[0x732B0x20d, 0x706B0x20d]
    =================================
    0x6e3S0x20d: v6e3V20d(0x1) = CONST 
    0x6e5S0x20d: v6e5V20d(0xa0) = CONST 
    0x6e7S0x20d: v6e7V20d(0x2) = CONST 
    0x6e9S0x20d: v6e9V20d(0x10000000000000000000000000000000000000000) = EXP v6e7V20d(0x2), v6e5V20d(0xa0)
    0x6eaS0x20d: v6eaV20d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e9V20d(0x10000000000000000000000000000000000000000), v6e3V20d(0x1)
    0x6ecS0x20d: v6ecV20d = AND v21d, v6eaV20d(0xffffffffffffffffffffffffffffffffffffffff)
    0x6edS0x20d: v6edV20d(0x0) = CONST 
    0x6f1S0x20d: MSTORE v6edV20d(0x0), v6ecV20d
    0x6f2S0x20d: v6f2V20d(0x1) = CONST 
    0x6f4S0x20d: v6f4V20d(0x20) = CONST 
    0x6f6S0x20d: MSTORE v6f4V20d(0x20), v6f2V20d(0x1)
    0x6f7S0x20d: v6f7V20d(0x40) = CONST 
    0x6faS0x20d: v6faV20d = SHA3 v6edV20d(0x0), v6f7V20d(0x40)
    0x6fbS0x20d: v6fbV20d = SLOAD v6faV20d
    0x6feS0x20d: v6feV20d = LT v6fbV20d, v225
    0x700S0x20d: v700V20d = ISZERO v6feV20d
    0x702S0x20d: v702V20d(0x732) = CONST 
    0x705S0x20d: JUMPI v702V20d(0x732), v6feV20d

    Begin block 0x732B0x20d
    prev=[0x6e2B0x20d, 0x706B0x20d], succ=[0x73eB0x20d, 0x739B0x20d]
    =================================
    0x732_0x0S0x20d: v732_0V20d = PHI v700V20d, v731V20d
    0x734S0x20d: v734V20d = ISZERO v732_0V20d
    0x735S0x20d: v735V20d(0x73e) = CONST 
    0x738S0x20d: JUMPI v735V20d(0x73e), v734V20d

    Begin block 0x73eB0x20d
    prev=[0x732B0x20d, 0x739B0x20d], succ=[0x744B0x20d, 0x7ccB0x20d]
    =================================
    0x73e_0x0S0x20d: v73e_0V20d = PHI v700V20d, v731V20d, v73dV20d
    0x73fS0x20d: v73fV20d = ISZERO v73e_0V20d
    0x740S0x20d: v740V20d(0x7cc) = CONST 
    0x743S0x20d: JUMPI v740V20d(0x7cc), v73fV20d

    Begin block 0x744B0x20d
    prev=[0x73eB0x20d], succ=[0x24637B0x20d]
    =================================
    0x744S0x20d: v744V20d(0x1) = CONST 
    0x746S0x20d: v746V20d(0xa0) = CONST 
    0x748S0x20d: v748V20d(0x2) = CONST 
    0x74aS0x20d: v74aV20d(0x10000000000000000000000000000000000000000) = EXP v748V20d(0x2), v746V20d(0xa0)
    0x74bS0x20d: v74bV20d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v74aV20d(0x10000000000000000000000000000000000000000), v744V20d(0x1)
    0x74eS0x20d: v74eV20d = AND v222, v74bV20d(0xffffffffffffffffffffffffffffffffffffffff)
    0x74fS0x20d: v74fV20d(0x0) = CONST 
    0x753S0x20d: MSTORE v74fV20d(0x0), v74eV20d
    0x754S0x20d: v754V20d(0x1) = CONST 
    0x756S0x20d: v756V20d(0x20) = CONST 
    0x75aS0x20d: MSTORE v756V20d(0x20), v754V20d(0x1)
    0x75bS0x20d: v75bV20d(0x40) = CONST 
    0x75fS0x20d: v75fV20d = SHA3 v74fV20d(0x0), v75bV20d(0x40)
    0x761S0x20d: v761V20d = SLOAD v75fV20d
    0x763S0x20d: v763V20d = ADD v225, v761V20d
    0x765S0x20d: SSTORE v75fV20d, v763V20d
    0x768S0x20d: v768V20d = AND v74bV20d(0xffffffffffffffffffffffffffffffffffffffff), v21d
    0x76bS0x20d: MSTORE v74fV20d(0x0), v768V20d
    0x76eS0x20d: v76eV20d = SHA3 v74fV20d(0x0), v75bV20d(0x40)
    0x770S0x20d: v770V20d = SLOAD v76eV20d
    0x773S0x20d: v773V20d = SUB v770V20d, v225
    0x775S0x20d: SSTORE v76eV20d, v773V20d
    0x776S0x20d: v776V20d(0x2) = CONST 
    0x779S0x20d: MSTORE v756V20d(0x20), v776V20d(0x2)
    0x77cS0x20d: v77cV20d = SHA3 v74fV20d(0x0), v75bV20d(0x40)
    0x77dS0x20d: v77dV20d = CALLER 
    0x780S0x20d: v780V20d = AND v74bV20d(0xffffffffffffffffffffffffffffffffffffffff), v77dV20d
    0x782S0x20d: MSTORE v74fV20d(0x0), v780V20d
    0x785S0x20d: MSTORE v756V20d(0x20), v77cV20d
    0x789S0x20d: v789V20d = SHA3 v74fV20d(0x0), v75bV20d(0x40)
    0x78bS0x20d: v78bV20d = SLOAD v789V20d
    0x78eS0x20d: v78eV20d = SUB v78bV20d, v225
    0x790S0x20d: SSTORE v789V20d, v78eV20d
    0x792S0x20d: v792V20d = MLOAD v75bV20d(0x40)
    0x795S0x20d: MSTORE v792V20d, v225
    0x797S0x20d: v797V20d = MLOAD v75bV20d(0x40)
    0x79bS0x20d: v79bV20d(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x7bfS0x20d: v7bfV20d(0x0) = SUB v792V20d, v797V20d
    0x7c2S0x20d: v7c2V20d(0x20) = ADD v756V20d(0x20), v7bfV20d(0x0)
    0x7c4S0x20d: LOG3 v797V20d, v7c2V20d(0x20), v79bV20d(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v768V20d, v74eV20d
    0x7c6S0x20d: v7c6V20d(0x1) = CONST 
    0x7c8S0x20d: v7c8V20d(0x24637) = CONST 
    0x7cbS0x20d: JUMP v7c8V20d(0x24637)

    Begin block 0x24637B0x20d
    prev=[0x744B0x20d], succ=[0x533e0B0x20d]
    =================================
    0x2b983S0x20d: v2b983V20d(0x533e0) = CONST 
    0x2b9a3S0x20d: JUMP v2b983V20d(0x533e0)

    Begin block 0x533e0B0x20d
    prev=[0x24637B0x20d], succ=[0x2435e]
    =================================
    0x533e6S0x20d: JUMP v20e(0x2435e)

    Begin block 0x2435e
    prev=[0x533e0B0x20d, 0x53473B0x20d], succ=[]
    =================================
    0x20dS0x2435e_0: v229_0V2435e_0 = PHI v7c6V20d(0x1), v7ceV20d(0x0)
    0x2435f: v2435f(0x40) = CONST 
    0x24362: v24362 = MLOAD v2435f(0x40)
    0x24364: v24364 = ISZERO v229_0V2435e_0
    0x24365: v24365 = ISZERO v24364
    0x24367: MSTORE v24362, v24365
    0x24368: v24368 = MLOAD v2435f(0x40)
    0x2436c: v2436c(0x0) = SUB v24362, v24368
    0x2436d: v2436d(0x20) = CONST 
    0x2436f: v2436f(0x20) = ADD v2436d(0x20), v2436c(0x0)
    0x24371: RETURN v24368, v2436f(0x20)

    Begin block 0x7ccB0x20d
    prev=[0x73eB0x20d], succ=[0x4bf9eB0x20d]
    =================================
    0x7ceS0x20d: v7ceV20d(0x0) = CONST 
    0x711cS0x20d: v711cV20d(0x4bf9e) = CONST 
    0x713cS0x20d: JUMP v711cV20d(0x4bf9e)

    Begin block 0x4bf9eB0x20d
    prev=[0x7ccB0x20d], succ=[0x53473B0x20d]
    =================================
    0x532eaS0x20d: v532eaV20d(0x53473) = CONST 
    0x5330aS0x20d: JUMP v532eaV20d(0x53473)

    Begin block 0x53473B0x20d
    prev=[0x4bf9eB0x20d], succ=[0x2435e]
    =================================
    0x53479S0x20d: JUMP v20e(0x2435e)

    Begin block 0x739B0x20d
    prev=[0x732B0x20d], succ=[0x73eB0x20d]
    =================================
    0x73aS0x20d: v73aV20d(0x0) = CONST 
    0x73dS0x20d: v73dV20d = GT v225, v73aV20d(0x0)
    0x671cS0x20d: v671cV20d(0x73e) = CONST 
    0x673cS0x20d: JUMP v671cV20d(0x73e)

    Begin block 0x706B0x20d
    prev=[0x6e2B0x20d], succ=[0x732B0x20d]
    =================================
    0x707S0x20d: v707V20d(0x1) = CONST 
    0x709S0x20d: v709V20d(0xa0) = CONST 
    0x70bS0x20d: v70bV20d(0x2) = CONST 
    0x70dS0x20d: v70dV20d(0x10000000000000000000000000000000000000000) = EXP v70bV20d(0x2), v709V20d(0xa0)
    0x70eS0x20d: v70eV20d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v70dV20d(0x10000000000000000000000000000000000000000), v707V20d(0x1)
    0x711S0x20d: v711V20d = AND v21d, v70eV20d(0xffffffffffffffffffffffffffffffffffffffff)
    0x712S0x20d: v712V20d(0x0) = CONST 
    0x716S0x20d: MSTORE v712V20d(0x0), v711V20d
    0x717S0x20d: v717V20d(0x2) = CONST 
    0x719S0x20d: v719V20d(0x20) = CONST 
    0x71dS0x20d: MSTORE v719V20d(0x20), v717V20d(0x2)
    0x71eS0x20d: v71eV20d(0x40) = CONST 
    0x722S0x20d: v722V20d = SHA3 v712V20d(0x0), v71eV20d(0x40)
    0x723S0x20d: v723V20d = CALLER 
    0x726S0x20d: v726V20d = AND v70eV20d(0xffffffffffffffffffffffffffffffffffffffff), v723V20d
    0x728S0x20d: MSTORE v712V20d(0x0), v726V20d
    0x72bS0x20d: MSTORE v719V20d(0x20), v722V20d
    0x72cS0x20d: v72cV20d = SHA3 v712V20d(0x0), v71eV20d(0x40)
    0x72dS0x20d: v72dV20d = SLOAD v72cV20d
    0x730S0x20d: v730V20d = LT v72dV20d, v225
    0x731S0x20d: v731V20d = ISZERO v730V20d
    0x5d1cS0x20d: v5d1cV20d(0x732) = CONST 
    0x5d3cS0x20d: JUMP v5d1cV20d(0x732)

}

function decimals()() public {
    Begin block 0x23e
    prev=[], succ=[0x245, 0x246]
    =================================
    0x23f: v23f = CALLVALUE 
    0x240: v240 = ISZERO v23f
    0x241: v241(0x246) = CONST 
    0x244: JUMPI v241(0x246), v240

    Begin block 0x245
    prev=[0x23e], succ=[]
    =================================
    0x245: THROW 

    Begin block 0x246
    prev=[0x23e], succ=[0x7d8]
    =================================
    0x247: v247(0x24391) = CONST 
    0x24a: v24a(0x7d8) = CONST 
    0x24d: JUMP v24a(0x7d8)

    Begin block 0x7d8
    prev=[0x246], succ=[0x24391]
    =================================
    0x7d9: v7d9(0x12) = CONST 
    0x7dc: JUMP v247(0x24391)

    Begin block 0x24391
    prev=[0x7d8], succ=[]
    =================================
    0x24392: v24392(0x40) = CONST 
    0x24395: v24395 = MLOAD v24392(0x40)
    0x24398: MSTORE v24395, v7d9(0x12)
    0x24399: v24399 = MLOAD v24392(0x40)
    0x2439d: v2439d(0x0) = SUB v24395, v24399
    0x2439e: v2439e(0x20) = CONST 
    0x243a0: v243a0(0x20) = ADD v2439e(0x20), v2439d(0x0)
    0x243a2: RETURN v24399, v243a0(0x20)

}

function tokenRate()() public {
    Begin block 0x260
    prev=[], succ=[0x267, 0x268]
    =================================
    0x261: v261 = CALLVALUE 
    0x262: v262 = ISZERO v261
    0x263: v263(0x268) = CONST 
    0x266: JUMPI v263(0x268), v262

    Begin block 0x267
    prev=[0x260], succ=[]
    =================================
    0x267: THROW 

    Begin block 0x268
    prev=[0x260], succ=[0x243c2]
    =================================
    0x269: v269(0x243c2) = CONST 
    0x26c: v26c(0x7dd) = CONST 
    0x26f: v26f_0 = CALLPRIVATE v26c(0x7dd), v269(0x243c2)

    Begin block 0x243c2
    prev=[0x268], succ=[]
    =================================
    0x243c3: v243c3(0x40) = CONST 
    0x243c6: v243c6 = MLOAD v243c3(0x40)
    0x243c9: MSTORE v243c6, v26f_0
    0x243ca: v243ca = MLOAD v243c3(0x40)
    0x243ce: v243ce(0x0) = SUB v243c6, v243ca
    0x243cf: v243cf(0x20) = CONST 
    0x243d1: v243d1(0x20) = ADD v243cf(0x20), v243ce(0x0)
    0x243d3: RETURN v243ca, v243d1(0x20)

}

function iceFund()() public {
    Begin block 0x282
    prev=[], succ=[0x289, 0x28a]
    =================================
    0x283: v283 = CALLVALUE 
    0x284: v284 = ISZERO v283
    0x285: v285(0x28a) = CONST 
    0x288: JUMPI v285(0x28a), v284

    Begin block 0x289
    prev=[0x282], succ=[]
    =================================
    0x289: THROW 

    Begin block 0x28a
    prev=[0x282], succ=[0x82d]
    =================================
    0x28b: v28b(0x243f3) = CONST 
    0x28e: v28e(0x82d) = CONST 
    0x291: JUMP v28e(0x82d)

    Begin block 0x82d
    prev=[0x28a], succ=[0x243f3]
    =================================
    0x82e: v82e(0x69e10de76676d0800000) = CONST 
    0x83a: JUMP v28b(0x243f3)

    Begin block 0x243f3
    prev=[0x82d], succ=[]
    =================================
    0x243f4: v243f4(0x40) = CONST 
    0x243f7: v243f7 = MLOAD v243f4(0x40)
    0x243fa: MSTORE v243f7, v82e(0x69e10de76676d0800000)
    0x243fb: v243fb = MLOAD v243f4(0x40)
    0x243ff: v243ff(0x0) = SUB v243f7, v243fb
    0x24400: v24400(0x20) = CONST 
    0x24402: v24402(0x20) = ADD v24400(0x20), v243ff(0x0)
    0x24404: RETURN v243fb, v24402(0x20)

}

function finalize()() public {
    Begin block 0x2a4
    prev=[], succ=[0x2ab, 0x2ac]
    =================================
    0x2a5: v2a5 = CALLVALUE 
    0x2a6: v2a6 = ISZERO v2a5
    0x2a7: v2a7(0x2ac) = CONST 
    0x2aa: JUMPI v2a7(0x2ac), v2a6

    Begin block 0x2ab
    prev=[0x2a4], succ=[]
    =================================
    0x2ab: THROW 

    Begin block 0x2ac
    prev=[0x2a4], succ=[0x83bB0x2ac]
    =================================
    0x2ad: v2ad(0x24424) = CONST 
    0x2b0: v2b0(0x83b) = CONST 
    0x2b3: JUMP v2b0(0x83b)

    Begin block 0x83bB0x2ac
    prev=[0x2ac], succ=[0x84eB0x2ac, 0x853B0x2ac]
    =================================
    0x83cS0x2ac: v83cV2ac(0x5) = CONST 
    0x83eS0x2ac: v83eV2ac = SLOAD v83cV2ac(0x5)
    0x83fS0x2ac: v83fV2ac(0xa0) = CONST 
    0x841S0x2ac: v841V2ac(0x2) = CONST 
    0x843S0x2ac: v843V2ac(0x10000000000000000000000000000000000000000) = EXP v841V2ac(0x2), v83fV2ac(0xa0)
    0x845S0x2ac: v845V2ac = DIV v83eV2ac, v843V2ac(0x10000000000000000000000000000000000000000)
    0x846S0x2ac: v846V2ac(0xff) = CONST 
    0x848S0x2ac: v848V2ac = AND v846V2ac(0xff), v845V2ac
    0x849S0x2ac: v849V2ac = ISZERO v848V2ac
    0x84aS0x2ac: v84aV2ac(0x853) = CONST 
    0x84dS0x2ac: JUMPI v84aV2ac(0x853), v849V2ac

    Begin block 0x84eB0x2ac
    prev=[0x83bB0x2ac], succ=[]
    =================================
    0x84eS0x2ac: v84eV2ac(0x0) = CONST 
    0x850S0x2ac: v850V2ac(0x0) = CONST 
    0x852S0x2ac: REVERT v850V2ac(0x0), v84eV2ac(0x0)

    Begin block 0x853B0x2ac
    prev=[0x83bB0x2ac], succ=[0x86aB0x2ac, 0x86fB0x2ac]
    =================================
    0x854S0x2ac: v854V2ac(0x4) = CONST 
    0x856S0x2ac: v856V2ac = SLOAD v854V2ac(0x4)
    0x857S0x2ac: v857V2ac = CALLER 
    0x858S0x2ac: v858V2ac(0x1) = CONST 
    0x85aS0x2ac: v85aV2ac(0xa0) = CONST 
    0x85cS0x2ac: v85cV2ac(0x2) = CONST 
    0x85eS0x2ac: v85eV2ac(0x10000000000000000000000000000000000000000) = EXP v85cV2ac(0x2), v85aV2ac(0xa0)
    0x85fS0x2ac: v85fV2ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v85eV2ac(0x10000000000000000000000000000000000000000), v858V2ac(0x1)
    0x862S0x2ac: v862V2ac = AND v85fV2ac(0xffffffffffffffffffffffffffffffffffffffff), v857V2ac
    0x864S0x2ac: v864V2ac = AND v856V2ac, v85fV2ac(0xffffffffffffffffffffffffffffffffffffffff)
    0x865S0x2ac: v865V2ac = EQ v864V2ac, v862V2ac
    0x866S0x2ac: v866V2ac(0x86f) = CONST 
    0x869S0x2ac: JUMPI v866V2ac(0x86f), v865V2ac

    Begin block 0x86aB0x2ac
    prev=[0x853B0x2ac], succ=[]
    =================================
    0x86aS0x2ac: v86aV2ac(0x0) = CONST 
    0x86cS0x2ac: v86cV2ac(0x0) = CONST 
    0x86eS0x2ac: REVERT v86cV2ac(0x0), v86aV2ac(0x0)

    Begin block 0x86fB0x2ac
    prev=[0x853B0x2ac], succ=[0x88eB0x2ac, 0x87cB0x2ac]
    =================================
    0x870S0x2ac: v870V2ac(0x7) = CONST 
    0x872S0x2ac: v872V2ac = SLOAD v870V2ac(0x7)
    0x873S0x2ac: v873V2ac = NUMBER 
    0x874S0x2ac: v874V2ac = GT v873V2ac, v872V2ac
    0x875S0x2ac: v875V2ac = ISZERO v874V2ac
    0x877S0x2ac: v877V2ac = ISZERO v875V2ac
    0x878S0x2ac: v878V2ac(0x88e) = CONST 
    0x87bS0x2ac: JUMPI v878V2ac(0x88e), v877V2ac

    Begin block 0x88eB0x2ac
    prev=[0x86fB0x2ac, 0x87cB0x2ac], succ=[0x894B0x2ac, 0x899B0x2ac]
    =================================
    0x88e_0x0S0x2ac: v88e_0V2ac = PHI v875V2ac, v88dV2ac
    0x88fS0x2ac: v88fV2ac = ISZERO v88e_0V2ac
    0x890S0x2ac: v890V2ac(0x899) = CONST 
    0x893S0x2ac: JUMPI v890V2ac(0x899), v88fV2ac

    Begin block 0x894B0x2ac
    prev=[0x88eB0x2ac], succ=[]
    =================================
    0x894S0x2ac: v894V2ac(0x0) = CONST 
    0x896S0x2ac: v896V2ac(0x0) = CONST 
    0x898S0x2ac: REVERT v896V2ac(0x0), v894V2ac(0x0)

    Begin block 0x899B0x2ac
    prev=[0x88eB0x2ac], succ=[0x8eeB0x2ac, 0x2ba07B0x2ac]
    =================================
    0x89aS0x2ac: v89aV2ac(0x5) = CONST 
    0x89dS0x2ac: v89dV2ac = SLOAD v89aV2ac(0x5)
    0x89eS0x2ac: v89eV2ac(0xff0000000000000000000000000000000000000000) = CONST 
    0x8b4S0x2ac: v8b4V2ac(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v89eV2ac(0xff0000000000000000000000000000000000000000)
    0x8b5S0x2ac: v8b5V2ac = AND v8b4V2ac(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v89dV2ac
    0x8b6S0x2ac: v8b6V2ac(0xa0) = CONST 
    0x8b8S0x2ac: v8b8V2ac(0x2) = CONST 
    0x8baS0x2ac: v8baV2ac(0x10000000000000000000000000000000000000000) = EXP v8b8V2ac(0x2), v8b6V2ac(0xa0)
    0x8bbS0x2ac: v8bbV2ac = OR v8baV2ac(0x10000000000000000000000000000000000000000), v8b5V2ac
    0x8bdS0x2ac: SSTORE v89aV2ac(0x5), v8bbV2ac
    0x8beS0x2ac: v8beV2ac(0x4) = CONST 
    0x8c0S0x2ac: v8c0V2ac = SLOAD v8beV2ac(0x4)
    0x8c1S0x2ac: v8c1V2ac(0x40) = CONST 
    0x8c3S0x2ac: v8c3V2ac = MLOAD v8c1V2ac(0x40)
    0x8c4S0x2ac: v8c4V2ac(0x1) = CONST 
    0x8c6S0x2ac: v8c6V2ac(0xa0) = CONST 
    0x8c8S0x2ac: v8c8V2ac(0x2) = CONST 
    0x8caS0x2ac: v8caV2ac(0x10000000000000000000000000000000000000000) = EXP v8c8V2ac(0x2), v8c6V2ac(0xa0)
    0x8cbS0x2ac: v8cbV2ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8caV2ac(0x10000000000000000000000000000000000000000), v8c4V2ac(0x1)
    0x8ceS0x2ac: v8ceV2ac = AND v8cbV2ac(0xffffffffffffffffffffffffffffffffffffffff), v8c0V2ac
    0x8d0S0x2ac: v8d0V2ac = ADDRESS 
    0x8d1S0x2ac: v8d1V2ac = AND v8d0V2ac, v8cbV2ac(0xffffffffffffffffffffffffffffffffffffffff)
    0x8d2S0x2ac: v8d2V2ac = BALANCE v8d1V2ac
    0x8d4S0x2ac: v8d4V2ac = ISZERO v8d2V2ac
    0x8d5S0x2ac: v8d5V2ac(0x8fc) = CONST 
    0x8d8S0x2ac: v8d8V2ac = MUL v8d5V2ac(0x8fc), v8d4V2ac
    0x8daS0x2ac: v8daV2ac(0x0) = CONST 
    0x8e2S0x2ac: v8e2V2ac = CALL v8d8V2ac, v8ceV2ac, v8d2V2ac, v8c3V2ac, v8daV2ac(0x0), v8c3V2ac, v8daV2ac(0x0)
    0x8e8S0x2ac: v8e8V2ac = ISZERO v8e2V2ac
    0x8e9S0x2ac: v8e9V2ac = ISZERO v8e8V2ac
    0x8eaS0x2ac: v8eaV2ac(0x2ba07) = CONST 
    0x8edS0x2ac: JUMPI v8eaV2ac(0x2ba07), v8e9V2ac

    Begin block 0x8eeB0x2ac
    prev=[0x899B0x2ac], succ=[]
    =================================
    0x8eeS0x2ac: v8eeV2ac(0x0) = CONST 
    0x8f0S0x2ac: v8f0V2ac(0x0) = CONST 
    0x8f2S0x2ac: REVERT v8f0V2ac(0x0), v8eeV2ac(0x0)

    Begin block 0x2ba07B0x2ac
    prev=[0x899B0x2ac], succ=[0x53406B0x2ac]
    =================================
    0x2da08S0x2ac: v2da08V2ac(0x53406) = CONST 
    0x2da28S0x2ac: JUMP v2da08V2ac(0x53406)

    Begin block 0x53406B0x2ac
    prev=[0x2ba07B0x2ac], succ=[0x24424]
    =================================
    0x53407S0x2ac: JUMP v2ad(0x24424)

    Begin block 0x24424
    prev=[0x53406B0x2ac], succ=[]
    =================================
    0x24425: STOP 

    Begin block 0x87cB0x2ac
    prev=[0x86fB0x2ac], succ=[0x88eB0x2ac]
    =================================
    0x87dS0x2ac: v87dV2ac(0x0) = CONST 
    0x87fS0x2ac: v87fV2ac = SLOAD v87dV2ac(0x0)
    0x880S0x2ac: v880V2ac(0x422ca8b0a00a425000000) = CONST 
    0x88cS0x2ac: v88cV2ac = EQ v880V2ac(0x422ca8b0a00a425000000), v87fV2ac
    0x88dS0x2ac: v88dV2ac = ISZERO v88cV2ac
    0xa31cS0x2ac: va31cV2ac(0x88e) = CONST 
    0xa33cS0x2ac: JUMP va31cV2ac(0x88e)

}

function version()() public {
    Begin block 0x2b6
    prev=[], succ=[0x2bd, 0x2be]
    =================================
    0x2b7: v2b7 = CALLVALUE 
    0x2b8: v2b8 = ISZERO v2b7
    0x2b9: v2b9(0x2be) = CONST 
    0x2bc: JUMPI v2b9(0x2be), v2b8

    Begin block 0x2bd
    prev=[0x2b6], succ=[]
    =================================
    0x2bd: THROW 

    Begin block 0x2be
    prev=[0x2b6], succ=[0x8f6B0x2be]
    =================================
    0x2bf: v2bf(0x130) = CONST 
    0x2c2: v2c2(0x8f6) = CONST 
    0x2c5: JUMP v2c2(0x8f6)

    Begin block 0x8f6B0x2be
    prev=[0x2be], succ=[0x936B0x2be, 0x2da48B0x2be]
    =================================
    0x8f7S0x2be: v8f7V2be(0x3) = CONST 
    0x8faS0x2be: v8faV2be = SLOAD v8f7V2be(0x3)
    0x8fbS0x2be: v8fbV2be(0x40) = CONST 
    0x8feS0x2be: v8feV2be = MLOAD v8fbV2be(0x40)
    0x8ffS0x2be: v8ffV2be(0x20) = CONST 
    0x901S0x2be: v901V2be(0x2) = CONST 
    0x903S0x2be: v903V2be(0x1) = CONST 
    0x906S0x2be: v906V2be = AND v8faV2be, v903V2be(0x1)
    0x907S0x2be: v907V2be = ISZERO v906V2be
    0x908S0x2be: v908V2be(0x100) = CONST 
    0x90bS0x2be: v90bV2be = MUL v908V2be(0x100), v907V2be
    0x90cS0x2be: v90cV2be(0x0) = CONST 
    0x90eS0x2be: v90eV2be(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v90cV2be(0x0)
    0x90fS0x2be: v90fV2be = ADD v90eV2be(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v90bV2be
    0x912S0x2be: v912V2be = AND v8faV2be, v90fV2be
    0x916S0x2be: v916V2be = DIV v912V2be, v901V2be(0x2)
    0x917S0x2be: v917V2be(0x1f) = CONST 
    0x91aS0x2be: v91aV2be = ADD v916V2be, v917V2be(0x1f)
    0x91dS0x2be: v91dV2be = DIV v91aV2be, v8ffV2be(0x20)
    0x91fS0x2be: v91fV2be = MUL v8ffV2be(0x20), v91dV2be
    0x921S0x2be: v921V2be = ADD v8feV2be, v91fV2be
    0x923S0x2be: v923V2be = ADD v8ffV2be(0x20), v921V2be
    0x926S0x2be: MSTORE v8fbV2be(0x40), v923V2be
    0x929S0x2be: MSTORE v8feV2be, v916V2be
    0x92dS0x2be: v92dV2be = ADD v8feV2be, v8ffV2be(0x20)
    0x931S0x2be: v931V2be = ISZERO v916V2be
    0x932S0x2be: v932V2be(0x2da48) = CONST 
    0x935S0x2be: JUMPI v932V2be(0x2da48), v931V2be

    Begin block 0x936B0x2be
    prev=[0x8f6B0x2be], succ=[0x93eB0x2be, 0x951B0x2be]
    =================================
    0x937S0x2be: v937V2be(0x1f) = CONST 
    0x939S0x2be: v939V2be = LT v937V2be(0x1f), v916V2be
    0x93aS0x2be: v93aV2be(0x951) = CONST 
    0x93dS0x2be: JUMPI v93aV2be(0x951), v939V2be

    Begin block 0x93eB0x2be
    prev=[0x936B0x2be], succ=[0x2da6fB0x2be]
    =================================
    0x93eS0x2be: v93eV2be(0x100) = CONST 
    0x943S0x2be: v943V2be = SLOAD v8f7V2be(0x3)
    0x944S0x2be: v944V2be = DIV v943V2be, v93eV2be(0x100)
    0x945S0x2be: v945V2be = MUL v944V2be, v93eV2be(0x100)
    0x947S0x2be: MSTORE v92dV2be, v945V2be
    0x949S0x2be: v949V2be(0x20) = CONST 
    0x94bS0x2be: v94bV2be = ADD v949V2be(0x20), v92dV2be
    0x94dS0x2be: v94dV2be(0x2da6f) = CONST 
    0x950S0x2be: JUMP v94dV2be(0x2da6f)

    Begin block 0x2da6fB0x2be
    prev=[0x93eB0x2be], succ=[0x1300x2b6]
    =================================
    0x2da76S0x2be: JUMP v2bf(0x130)

    Begin block 0x1300x2b6
    prev=[0x2da48B0x2be, 0x2da6fB0x2be, 0x53372B0x2be], succ=[0x1760x2b6, 0x1560x2b6]
    =================================
    0x1310x2b6: v2b6131(0x40) = CONST 
    0x1340x2b6: v2b6134 = MLOAD v2b6131(0x40)
    0x1350x2b6: v2b6135(0x20) = CONST 
    0x1390x2b6: MSTORE v2b6134, v2b6135(0x20)
    0x13b0x2b6: v2b613b = MLOAD v8feV2be
    0x13e0x2b6: v2b613e = ADD v2b6134, v2b6135(0x20)
    0x13f0x2b6: MSTORE v2b613e, v2b613b
    0x1410x2b6: v2b6141 = MLOAD v8feV2be
    0x1480x2b6: v2b6148 = ADD v2b6134, v2b6131(0x40)
    0x14b0x2b6: v2b614b = ADD v8feV2be, v2b6135(0x20)
    0x1510x2b6: v2b6151 = ISZERO v2b6141
    0x1520x2b6: v2b6152(0x176) = CONST 
    0x1550x2b6: JUMPI v2b6152(0x176), v2b6151

    Begin block 0x1760x2b6
    prev=[0x1560x2b6, 0x1300x2b6], succ=[0x1890x2b6, 0x1a20x2b6]
    =================================
    0x17e0x2b6: v2b617e = ADD v2b6141, v2b6148
    0x1800x2b6: v2b6180(0x1f) = CONST 
    0x1820x2b6: v2b6182 = AND v2b6180(0x1f), v2b6141
    0x1840x2b6: v2b6184 = ISZERO v2b6182
    0x1850x2b6: v2b6185(0x1a2) = CONST 
    0x1880x2b6: JUMPI v2b6185(0x1a2), v2b6184

    Begin block 0x1890x2b6
    prev=[0x1760x2b6], succ=[0x1a20x2b6]
    =================================
    0x18b0x2b6: v2b618b = SUB v2b617e, v2b6182
    0x18d0x2b6: v2b618d = MLOAD v2b618b
    0x18e0x2b6: v2b618e(0x1) = CONST 
    0x1910x2b6: v2b6191(0x20) = CONST 
    0x1930x2b6: v2b6193 = SUB v2b6191(0x20), v2b6182
    0x1940x2b6: v2b6194(0x100) = CONST 
    0x1970x2b6: v2b6197 = EXP v2b6194(0x100), v2b6193
    0x1980x2b6: v2b6198 = SUB v2b6197, v2b618e(0x1)
    0x1990x2b6: v2b6199 = NOT v2b6198
    0x19a0x2b6: v2b619a = AND v2b6199, v2b618d
    0x19c0x2b6: MSTORE v2b618b, v2b619a
    0x19d0x2b6: v2b619d(0x20) = CONST 
    0x19f0x2b6: v2b619f = ADD v2b619d(0x20), v2b618b
    0x2b1c0x2b6: v2b62b1c(0x1a2) = CONST 
    0x2b3c0x2b6: JUMP v2b62b1c(0x1a2)

    Begin block 0x1a20x2b6
    prev=[0x1890x2b6, 0x1760x2b6], succ=[]
    =================================
    0x1a20x2b6_0x1: v1a22b6_1 = PHI v2b619f, v2b617e
    0x1a80x2b6: v2b61a8(0x40) = CONST 
    0x1aa0x2b6: v2b61aa = MLOAD v2b61a8(0x40)
    0x1ad0x2b6: v2b61ad = SUB v1a22b6_1, v2b61aa
    0x1af0x2b6: RETURN v2b61aa, v2b61ad

    Begin block 0x1560x2b6
    prev=[0x1640x2b6, 0x1300x2b6], succ=[0x1640x2b6, 0x1760x2b6]
    =================================
    0x1560x2b6_0x0: v1562b6_0 = PHI v2b6171, v2b614b
    0x1560x2b6_0x1: v1562b6_1 = PHI v2b616f, v2b6148
    0x1560x2b6_0x2: v1562b6_2 = PHI v2b6169, v2b6141
    0x1580x2b6: v2b6158 = MLOAD v1562b6_0
    0x15a0x2b6: MSTORE v1562b6_1, v2b6158
    0x15b0x2b6: v2b615b(0x20) = CONST 
    0x15e0x2b6: v2b615e = GT v1562b6_2, v2b615b(0x20)
    0x15f0x2b6: v2b615f = ISZERO v2b615e
    0x1600x2b6: v2b6160(0x176) = CONST 
    0x1630x2b6: JUMPI v2b6160(0x176), v2b615f

    Begin block 0x1640x2b6
    prev=[0x1560x2b6], succ=[0x1560x2b6]
    =================================
    0x1640x2b6_0x0: v1642b6_0 = PHI v2b6171, v2b614b
    0x1640x2b6_0x1: v1642b6_1 = PHI v2b616f, v2b6148
    0x1640x2b6_0x2: v1642b6_2 = PHI v2b6169, v2b6141
    0x1640x2b6: v2b6164(0x1f) = CONST 
    0x1660x2b6: v2b6166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2b6164(0x1f)
    0x1690x2b6: v2b6169 = ADD v1642b6_2, v2b6166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x16b0x2b6: v2b616b(0x20) = CONST 
    0x16f0x2b6: v2b616f = ADD v2b616b(0x20), v1642b6_1
    0x1710x2b6: v2b6171 = ADD v2b616b(0x20), v1642b6_0
    0x1720x2b6: v2b6172(0x156) = CONST 
    0x1750x2b6: JUMP v2b6172(0x156)

    Begin block 0x951B0x2be
    prev=[0x936B0x2be], succ=[0x95fB0x2be]
    =================================
    0x953S0x2be: v953V2be = ADD v92dV2be, v916V2be
    0x956S0x2be: v956V2be(0x0) = CONST 
    0x958S0x2be: MSTORE v956V2be(0x0), v8f7V2be(0x3)
    0x959S0x2be: v959V2be(0x20) = CONST 
    0x95bS0x2be: v95bV2be(0x0) = CONST 
    0x95dS0x2be: v95dV2be = SHA3 v95bV2be(0x0), v959V2be(0x20)
    0xb71cS0x2be: vb71cV2be(0x95f) = CONST 
    0xb73cS0x2be: JUMP vb71cV2be(0x95f)

    Begin block 0x95fB0x2be
    prev=[0x951B0x2be, 0x95fB0x2be], succ=[0x95fB0x2be, 0x973B0x2be]
    =================================
    0x95f_0x0S0x2be: v95f_0V2be = PHI v92dV2be, v96bV2be
    0x95f_0x1S0x2be: v95f_1V2be = PHI v95dV2be, v967V2be
    0x961S0x2be: v961V2be = SLOAD v95f_1V2be
    0x963S0x2be: MSTORE v95f_0V2be, v961V2be
    0x965S0x2be: v965V2be(0x1) = CONST 
    0x967S0x2be: v967V2be = ADD v965V2be(0x1), v95f_1V2be
    0x969S0x2be: v969V2be(0x20) = CONST 
    0x96bS0x2be: v96bV2be = ADD v969V2be(0x20), v95f_0V2be
    0x96eS0x2be: v96eV2be = GT v953V2be, v96bV2be
    0x96fS0x2be: v96fV2be(0x95f) = CONST 
    0x972S0x2be: JUMPI v96fV2be(0x95f), v96eV2be

    Begin block 0x973B0x2be
    prev=[0x95fB0x2be], succ=[0x53372B0x2be]
    =================================
    0x975S0x2be: v975V2be = SUB v96bV2be, v953V2be
    0x976S0x2be: v976V2be(0x1f) = CONST 
    0x978S0x2be: v978V2be = AND v976V2be(0x1f), v975V2be
    0x97aS0x2be: v97aV2be = ADD v953V2be, v978V2be
    0xc11cS0x2be: vc11cV2be(0x53372) = CONST 
    0xc13cS0x2be: JUMP vc11cV2be(0x53372)

    Begin block 0x53372B0x2be
    prev=[0x973B0x2be], succ=[0x1300x2b6]
    =================================
    0x53379S0x2be: JUMP v2bf(0x130)

    Begin block 0x2da48B0x2be
    prev=[0x8f6B0x2be], succ=[0x1300x2b6]
    =================================
    0x2da4fS0x2be: JUMP v2bf(0x130)

}

function tokenCreationCap()() public {
    Begin block 0x346
    prev=[], succ=[0x34d, 0x34e]
    =================================
    0x347: v347 = CALLVALUE 
    0x348: v348 = ISZERO v347
    0x349: v349(0x34e) = CONST 
    0x34c: JUMPI v349(0x34e), v348

    Begin block 0x34d
    prev=[0x346], succ=[]
    =================================
    0x34d: THROW 

    Begin block 0x34e
    prev=[0x346], succ=[0x984]
    =================================
    0x34f: v34f(0x24445) = CONST 
    0x352: v352(0x984) = CONST 
    0x355: JUMP v352(0x984)

    Begin block 0x984
    prev=[0x34e], succ=[0x24445]
    =================================
    0x985: v985(0x422ca8b0a00a425000000) = CONST 
    0x992: JUMP v34f(0x24445)

    Begin block 0x24445
    prev=[0x984], succ=[]
    =================================
    0x24446: v24446(0x40) = CONST 
    0x24449: v24449 = MLOAD v24446(0x40)
    0x2444c: MSTORE v24449, v985(0x422ca8b0a00a425000000)
    0x2444d: v2444d = MLOAD v24446(0x40)
    0x24451: v24451(0x0) = SUB v24449, v2444d
    0x24452: v24452(0x20) = CONST 
    0x24454: v24454(0x20) = ADD v24452(0x20), v24451(0x0)
    0x24456: RETURN v2444d, v24454(0x20)

}

function balanceOf(address)() public {
    Begin block 0x368
    prev=[], succ=[0x36f, 0x370]
    =================================
    0x369: v369 = CALLVALUE 
    0x36a: v36a = ISZERO v369
    0x36b: v36b(0x370) = CONST 
    0x36e: JUMPI v36b(0x370), v36a

    Begin block 0x36f
    prev=[0x368], succ=[]
    =================================
    0x36f: THROW 

    Begin block 0x370
    prev=[0x368], succ=[0x993B0x370]
    =================================
    0x371: v371(0x24476) = CONST 
    0x374: v374(0x1) = CONST 
    0x376: v376(0xa0) = CONST 
    0x378: v378(0x2) = CONST 
    0x37a: v37a(0x10000000000000000000000000000000000000000) = EXP v378(0x2), v376(0xa0)
    0x37b: v37b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37a(0x10000000000000000000000000000000000000000), v374(0x1)
    0x37c: v37c(0x4) = CONST 
    0x37e: v37e = CALLDATALOAD v37c(0x4)
    0x37f: v37f = AND v37e, v37b(0xffffffffffffffffffffffffffffffffffffffff)
    0x380: v380(0x993) = CONST 
    0x383: JUMP v380(0x993)

    Begin block 0x993B0x370
    prev=[0x370], succ=[0x9adB0x370]
    =================================
    0x994S0x370: v994V370(0x1) = CONST 
    0x996S0x370: v996V370(0xa0) = CONST 
    0x998S0x370: v998V370(0x2) = CONST 
    0x99aS0x370: v99aV370(0x10000000000000000000000000000000000000000) = EXP v998V370(0x2), v996V370(0xa0)
    0x99bS0x370: v99bV370(0xffffffffffffffffffffffffffffffffffffffff) = SUB v99aV370(0x10000000000000000000000000000000000000000), v994V370(0x1)
    0x99dS0x370: v99dV370 = AND v37f, v99bV370(0xffffffffffffffffffffffffffffffffffffffff)
    0x99eS0x370: v99eV370(0x0) = CONST 
    0x9a2S0x370: MSTORE v99eV370(0x0), v99dV370
    0x9a3S0x370: v9a3V370(0x1) = CONST 
    0x9a5S0x370: v9a5V370(0x20) = CONST 
    0x9a7S0x370: MSTORE v9a5V370(0x20), v9a3V370(0x1)
    0x9a8S0x370: v9a8V370(0x40) = CONST 
    0x9abS0x370: v9abV370 = SHA3 v99eV370(0x0), v9a8V370(0x40)
    0x9acS0x370: v9acV370 = SLOAD v9abV370
    0xcb1cS0x370: vcb1cV370(0x9ad) = CONST 
    0xcb3cS0x370: JUMP vcb1cV370(0x9ad)

    Begin block 0x9adB0x370
    prev=[0x993B0x370], succ=[0x24476]
    =================================
    0x9b1S0x370: JUMP v371(0x24476)

    Begin block 0x24476
    prev=[0x9adB0x370], succ=[]
    =================================
    0x24477: v24477(0x40) = CONST 
    0x2447a: v2447a = MLOAD v24477(0x40)
    0x2447d: MSTORE v2447a, v9acV370
    0x2447e: v2447e = MLOAD v24477(0x40)
    0x24482: v24482(0x0) = SUB v2447a, v2447e
    0x24483: v24483(0x20) = CONST 
    0x24485: v24485(0x20) = ADD v24483(0x20), v24482(0x0)
    0x24487: RETURN v2447e, v24485(0x20)

}

function iceFundDeposit()() public {
    Begin block 0x396
    prev=[], succ=[0x39d, 0x39e]
    =================================
    0x397: v397 = CALLVALUE 
    0x398: v398 = ISZERO v397
    0x399: v399(0x39e) = CONST 
    0x39c: JUMPI v399(0x39e), v398

    Begin block 0x39d
    prev=[0x396], succ=[]
    =================================
    0x39d: THROW 

    Begin block 0x39e
    prev=[0x396], succ=[0x9b2]
    =================================
    0x39f: v39f(0x244a7) = CONST 
    0x3a2: v3a2(0x9b2) = CONST 
    0x3a5: JUMP v3a2(0x9b2)

    Begin block 0x9b2
    prev=[0x39e], succ=[0x244a7]
    =================================
    0x9b3: v9b3(0x5) = CONST 
    0x9b5: v9b5 = SLOAD v9b3(0x5)
    0x9b6: v9b6(0x1) = CONST 
    0x9b8: v9b8(0xa0) = CONST 
    0x9ba: v9ba(0x2) = CONST 
    0x9bc: v9bc(0x10000000000000000000000000000000000000000) = EXP v9ba(0x2), v9b8(0xa0)
    0x9bd: v9bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9bc(0x10000000000000000000000000000000000000000), v9b6(0x1)
    0x9be: v9be = AND v9bd(0xffffffffffffffffffffffffffffffffffffffff), v9b5
    0x9c0: JUMP v39f(0x244a7)

    Begin block 0x244a7
    prev=[0x9b2], succ=[]
    =================================
    0x244a8: v244a8(0x40) = CONST 
    0x244ab: v244ab = MLOAD v244a8(0x40)
    0x244ac: v244ac(0x1) = CONST 
    0x244ae: v244ae(0xa0) = CONST 
    0x244b0: v244b0(0x2) = CONST 
    0x244b2: v244b2(0x10000000000000000000000000000000000000000) = EXP v244b0(0x2), v244ae(0xa0)
    0x244b3: v244b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v244b2(0x10000000000000000000000000000000000000000), v244ac(0x1)
    0x244b6: v244b6 = AND v9be, v244b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x244b8: MSTORE v244ab, v244b6
    0x244b9: v244b9 = MLOAD v244a8(0x40)
    0x244bd: v244bd(0x0) = SUB v244ab, v244b9
    0x244be: v244be(0x20) = CONST 
    0x244c0: v244c0(0x20) = ADD v244be(0x20), v244bd(0x0)
    0x244c2: RETURN v244b9, v244c0(0x20)

}

function isFinalized()() public {
    Begin block 0x3c2
    prev=[], succ=[0x3c9, 0x3ca]
    =================================
    0x3c3: v3c3 = CALLVALUE 
    0x3c4: v3c4 = ISZERO v3c3
    0x3c5: v3c5(0x3ca) = CONST 
    0x3c8: JUMPI v3c5(0x3ca), v3c4

    Begin block 0x3c9
    prev=[0x3c2], succ=[]
    =================================
    0x3c9: THROW 

    Begin block 0x3ca
    prev=[0x3c2], succ=[0x9c1]
    =================================
    0x3cb: v3cb(0x244e2) = CONST 
    0x3ce: v3ce(0x9c1) = CONST 
    0x3d1: JUMP v3ce(0x9c1)

    Begin block 0x9c1
    prev=[0x3ca], succ=[0x244e2]
    =================================
    0x9c2: v9c2(0x5) = CONST 
    0x9c4: v9c4 = SLOAD v9c2(0x5)
    0x9c5: v9c5(0xa0) = CONST 
    0x9c7: v9c7(0x2) = CONST 
    0x9c9: v9c9(0x10000000000000000000000000000000000000000) = EXP v9c7(0x2), v9c5(0xa0)
    0x9cb: v9cb = DIV v9c4, v9c9(0x10000000000000000000000000000000000000000)
    0x9cc: v9cc(0xff) = CONST 
    0x9ce: v9ce = AND v9cc(0xff), v9cb
    0x9d0: JUMP v3cb(0x244e2)

    Begin block 0x244e2
    prev=[0x9c1], succ=[]
    =================================
    0x244e3: v244e3(0x40) = CONST 
    0x244e6: v244e6 = MLOAD v244e3(0x40)
    0x244e8: v244e8 = ISZERO v9ce
    0x244e9: v244e9 = ISZERO v244e8
    0x244eb: MSTORE v244e6, v244e9
    0x244ec: v244ec = MLOAD v244e3(0x40)
    0x244f0: v244f0(0x0) = SUB v244e6, v244ec
    0x244f1: v244f1(0x20) = CONST 
    0x244f3: v244f3(0x20) = ADD v244f1(0x20), v244f0(0x0)
    0x244f5: RETURN v244ec, v244f3(0x20)

}

function fundingEndBlock()() public {
    Begin block 0x3e6
    prev=[], succ=[0x3ed, 0x3ee]
    =================================
    0x3e7: v3e7 = CALLVALUE 
    0x3e8: v3e8 = ISZERO v3e7
    0x3e9: v3e9(0x3ee) = CONST 
    0x3ec: JUMPI v3e9(0x3ee), v3e8

    Begin block 0x3ed
    prev=[0x3e6], succ=[]
    =================================
    0x3ed: THROW 

    Begin block 0x3ee
    prev=[0x3e6], succ=[0x9d1]
    =================================
    0x3ef: v3ef(0x24515) = CONST 
    0x3f2: v3f2(0x9d1) = CONST 
    0x3f5: JUMP v3f2(0x9d1)

    Begin block 0x9d1
    prev=[0x3ee], succ=[0x24515]
    =================================
    0x9d2: v9d2(0x7) = CONST 
    0x9d4: v9d4 = SLOAD v9d2(0x7)
    0x9d6: JUMP v3ef(0x24515)

    Begin block 0x24515
    prev=[0x9d1], succ=[]
    =================================
    0x24516: v24516(0x40) = CONST 
    0x24519: v24519 = MLOAD v24516(0x40)
    0x2451c: MSTORE v24519, v9d4
    0x2451d: v2451d = MLOAD v24516(0x40)
    0x24521: v24521(0x0) = SUB v24519, v2451d
    0x24522: v24522(0x20) = CONST 
    0x24524: v24524(0x20) = ADD v24522(0x20), v24521(0x0)
    0x24526: RETURN v2451d, v24524(0x20)

}

function symbol()() public {
    Begin block 0x408
    prev=[], succ=[0x40f, 0x410]
    =================================
    0x409: v409 = CALLVALUE 
    0x40a: v40a = ISZERO v409
    0x40b: v40b(0x410) = CONST 
    0x40e: JUMPI v40b(0x410), v40a

    Begin block 0x40f
    prev=[0x408], succ=[]
    =================================
    0x40f: THROW 

    Begin block 0x410
    prev=[0x408], succ=[0x9d7]
    =================================
    0x411: v411(0x130) = CONST 
    0x414: v414(0x9d7) = CONST 
    0x417: JUMP v414(0x9d7)

    Begin block 0x9d7
    prev=[0x410], succ=[0x1300x408]
    =================================
    0x9d8: v9d8(0x40) = CONST 
    0x9db: v9db = MLOAD v9d8(0x40)
    0x9de: v9de = ADD v9d8(0x40), v9db
    0x9e1: MSTORE v9d8(0x40), v9de
    0x9e2: v9e2(0x3) = CONST 
    0x9e5: MSTORE v9db, v9e2(0x3)
    0x9e6: v9e6(0x4943450000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa07: va07(0x20) = CONST 
    0xa0a: va0a = ADD v9db, va07(0x20)
    0xa0b: MSTORE va0a, v9e6(0x4943450000000000000000000000000000000000000000000000000000000000)
    0xa0d: JUMP v411(0x130)

    Begin block 0x1300x408
    prev=[0x9d7], succ=[0x1760x408, 0x1560x408]
    =================================
    0x1310x408: v408131(0x40) = CONST 
    0x1340x408: v408134 = MLOAD v408131(0x40)
    0x1350x408: v408135(0x20) = CONST 
    0x1390x408: MSTORE v408134, v408135(0x20)
    0x13b0x408: v40813b(0x3) = MLOAD v9db
    0x13e0x408: v40813e = ADD v408134, v408135(0x20)
    0x13f0x408: MSTORE v40813e, v40813b(0x3)
    0x1410x408: v408141(0x3) = MLOAD v9db
    0x1480x408: v408148 = ADD v408134, v408131(0x40)
    0x14b0x408: v40814b = ADD v9db, v408135(0x20)
    0x1510x408: v408151(0x0) = ISZERO v408141(0x3)
    0x1520x408: v408152(0x176) = CONST 
    0x1550x408: JUMPI v408152(0x176), v408151(0x0)

    Begin block 0x1760x408
    prev=[0x1560x408, 0x1300x408], succ=[0x1890x408, 0x1a20x408]
    =================================
    0x17e0x408: v40817e = ADD v408141(0x3), v408148
    0x1800x408: v408180(0x1f) = CONST 
    0x1820x408: v408182(0x3) = AND v408180(0x1f), v408141(0x3)
    0x1840x408: v408184(0x0) = ISZERO v408182(0x3)
    0x1850x408: v408185(0x1a2) = CONST 
    0x1880x408: JUMPI v408185(0x1a2), v408184(0x0)

    Begin block 0x1890x408
    prev=[0x1760x408], succ=[0x1a20x408]
    =================================
    0x18b0x408: v40818b = SUB v40817e, v408182(0x3)
    0x18d0x408: v40818d = MLOAD v40818b
    0x18e0x408: v40818e(0x1) = CONST 
    0x1910x408: v408191(0x20) = CONST 
    0x1930x408: v408193(0x1d) = SUB v408191(0x20), v408182(0x3)
    0x1940x408: v408194(0x100) = CONST 
    0x1970x408: v408197(0x10000000000000000000000000000000000000000000000000000000000) = EXP v408194(0x100), v408193(0x1d)
    0x1980x408: v408198(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v408197(0x10000000000000000000000000000000000000000000000000000000000), v40818e(0x1)
    0x1990x408: v408199(0xffffff0000000000000000000000000000000000000000000000000000000000) = NOT v408198(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x19a0x408: v40819a = AND v408199(0xffffff0000000000000000000000000000000000000000000000000000000000), v40818d
    0x19c0x408: MSTORE v40818b, v40819a
    0x19d0x408: v40819d(0x20) = CONST 
    0x19f0x408: v40819f = ADD v40819d(0x20), v40818b
    0x2b1c0x408: v4082b1c(0x1a2) = CONST 
    0x2b3c0x408: JUMP v4082b1c(0x1a2)

    Begin block 0x1a20x408
    prev=[0x1890x408, 0x1760x408], succ=[]
    =================================
    0x1a20x408_0x1: v1a2408_1 = PHI v40819f, v40817e
    0x1a80x408: v4081a8(0x40) = CONST 
    0x1aa0x408: v4081aa = MLOAD v4081a8(0x40)
    0x1ad0x408: v4081ad = SUB v1a2408_1, v4081aa
    0x1af0x408: RETURN v4081aa, v4081ad

    Begin block 0x1560x408
    prev=[0x1640x408, 0x1300x408], succ=[0x1640x408, 0x1760x408]
    =================================
    0x1560x408_0x0: v156408_0 = PHI v408171, v40814b
    0x1560x408_0x1: v156408_1 = PHI v40816f, v408148
    0x1560x408_0x2: v156408_2 = PHI v408169, v408141(0x3)
    0x1580x408: v408158 = MLOAD v156408_0
    0x15a0x408: MSTORE v156408_1, v408158
    0x15b0x408: v40815b(0x20) = CONST 
    0x15e0x408: v40815e = GT v156408_2, v40815b(0x20)
    0x15f0x408: v40815f = ISZERO v40815e
    0x1600x408: v408160(0x176) = CONST 
    0x1630x408: JUMPI v408160(0x176), v40815f

    Begin block 0x1640x408
    prev=[0x1560x408], succ=[0x1560x408]
    =================================
    0x1640x408_0x0: v164408_0 = PHI v408171, v40814b
    0x1640x408_0x1: v164408_1 = PHI v40816f, v408148
    0x1640x408_0x2: v164408_2 = PHI v408169, v408141(0x3)
    0x1640x408: v408164(0x1f) = CONST 
    0x1660x408: v408166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v408164(0x1f)
    0x1690x408: v408169 = ADD v164408_2, v408166(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x16b0x408: v40816b(0x20) = CONST 
    0x16f0x408: v40816f = ADD v40816b(0x20), v164408_1
    0x1710x408: v408171 = ADD v40816b(0x20), v164408_0
    0x1720x408: v408172(0x156) = CONST 
    0x1750x408: JUMP v408172(0x156)

}

function ethFundDeposit()() public {
    Begin block 0x498
    prev=[], succ=[0x49f, 0x4a0]
    =================================
    0x499: v499 = CALLVALUE 
    0x49a: v49a = ISZERO v499
    0x49b: v49b(0x4a0) = CONST 
    0x49e: JUMPI v49b(0x4a0), v49a

    Begin block 0x49f
    prev=[0x498], succ=[]
    =================================
    0x49f: THROW 

    Begin block 0x4a0
    prev=[0x498], succ=[0xa0e]
    =================================
    0x4a1: v4a1(0x24546) = CONST 
    0x4a4: v4a4(0xa0e) = CONST 
    0x4a7: JUMP v4a4(0xa0e)

    Begin block 0xa0e
    prev=[0x4a0], succ=[0x24546]
    =================================
    0xa0f: va0f(0x4) = CONST 
    0xa11: va11 = SLOAD va0f(0x4)
    0xa12: va12(0x1) = CONST 
    0xa14: va14(0xa0) = CONST 
    0xa16: va16(0x2) = CONST 
    0xa18: va18(0x10000000000000000000000000000000000000000) = EXP va16(0x2), va14(0xa0)
    0xa19: va19(0xffffffffffffffffffffffffffffffffffffffff) = SUB va18(0x10000000000000000000000000000000000000000), va12(0x1)
    0xa1a: va1a = AND va19(0xffffffffffffffffffffffffffffffffffffffff), va11
    0xa1c: JUMP v4a1(0x24546)

    Begin block 0x24546
    prev=[0xa0e], succ=[]
    =================================
    0x24547: v24547(0x40) = CONST 
    0x2454a: v2454a = MLOAD v24547(0x40)
    0x2454b: v2454b(0x1) = CONST 
    0x2454d: v2454d(0xa0) = CONST 
    0x2454f: v2454f(0x2) = CONST 
    0x24551: v24551(0x10000000000000000000000000000000000000000) = EXP v2454f(0x2), v2454d(0xa0)
    0x24552: v24552(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24551(0x10000000000000000000000000000000000000000), v2454b(0x1)
    0x24555: v24555 = AND va1a, v24552(0xffffffffffffffffffffffffffffffffffffffff)
    0x24557: MSTORE v2454a, v24555
    0x24558: v24558 = MLOAD v24547(0x40)
    0x2455c: v2455c(0x0) = SUB v2454a, v24558
    0x2455d: v2455d(0x20) = CONST 
    0x2455f: v2455f(0x20) = ADD v2455d(0x20), v2455c(0x0)
    0x24561: RETURN v24558, v2455f(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x4c4
    prev=[], succ=[0x4cb, 0x4cc]
    =================================
    0x4c5: v4c5 = CALLVALUE 
    0x4c6: v4c6 = ISZERO v4c5
    0x4c7: v4c7(0x4cc) = CONST 
    0x4ca: JUMPI v4c7(0x4cc), v4c6

    Begin block 0x4cb
    prev=[0x4c4], succ=[]
    =================================
    0x4cb: THROW 

    Begin block 0x4cc
    prev=[0x4c4], succ=[0xa1dB0x4cc]
    =================================
    0x4cd: v4cd(0x24581) = CONST 
    0x4d0: v4d0(0x1) = CONST 
    0x4d2: v4d2(0xa0) = CONST 
    0x4d4: v4d4(0x2) = CONST 
    0x4d6: v4d6(0x10000000000000000000000000000000000000000) = EXP v4d4(0x2), v4d2(0xa0)
    0x4d7: v4d7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d6(0x10000000000000000000000000000000000000000), v4d0(0x1)
    0x4d8: v4d8(0x4) = CONST 
    0x4da: v4da = CALLDATALOAD v4d8(0x4)
    0x4db: v4db = AND v4da, v4d7(0xffffffffffffffffffffffffffffffffffffffff)
    0x4dc: v4dc(0x24) = CONST 
    0x4de: v4de = CALLDATALOAD v4dc(0x24)
    0x4df: v4df(0xa1d) = CONST 
    0x4e2: JUMP v4df(0xa1d)

    Begin block 0xa1dB0x4cc
    prev=[0x4cc], succ=[0xa46B0x4cc, 0xa41B0x4cc]
    =================================
    0xa1eS0x4cc: va1eV4cc(0x1) = CONST 
    0xa20S0x4cc: va20V4cc(0xa0) = CONST 
    0xa22S0x4cc: va22V4cc(0x2) = CONST 
    0xa24S0x4cc: va24V4cc(0x10000000000000000000000000000000000000000) = EXP va22V4cc(0x2), va20V4cc(0xa0)
    0xa25S0x4cc: va25V4cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB va24V4cc(0x10000000000000000000000000000000000000000), va1eV4cc(0x1)
    0xa26S0x4cc: va26V4cc = CALLER 
    0xa27S0x4cc: va27V4cc = AND va26V4cc, va25V4cc(0xffffffffffffffffffffffffffffffffffffffff)
    0xa28S0x4cc: va28V4cc(0x0) = CONST 
    0xa2cS0x4cc: MSTORE va28V4cc(0x0), va27V4cc
    0xa2dS0x4cc: va2dV4cc(0x1) = CONST 
    0xa2fS0x4cc: va2fV4cc(0x20) = CONST 
    0xa31S0x4cc: MSTORE va2fV4cc(0x20), va2dV4cc(0x1)
    0xa32S0x4cc: va32V4cc(0x40) = CONST 
    0xa35S0x4cc: va35V4cc = SHA3 va28V4cc(0x0), va32V4cc(0x40)
    0xa36S0x4cc: va36V4cc = SLOAD va35V4cc
    0xa39S0x4cc: va39V4cc = LT va36V4cc, v4de
    0xa3bS0x4cc: va3bV4cc = ISZERO va39V4cc
    0xa3dS0x4cc: va3dV4cc(0xa46) = CONST 
    0xa40S0x4cc: JUMPI va3dV4cc(0xa46), va39V4cc

    Begin block 0xa46B0x4cc
    prev=[0xa1dB0x4cc, 0xa41B0x4cc], succ=[0xa4cB0x4cc, 0xabaB0x4cc]
    =================================
    0xa46_0x0S0x4cc: va46_0V4cc = PHI va3bV4cc, va45V4cc
    0xa47S0x4cc: va47V4cc = ISZERO va46_0V4cc
    0xa48S0x4cc: va48V4cc(0xaba) = CONST 
    0xa4bS0x4cc: JUMPI va48V4cc(0xaba), va47V4cc

    Begin block 0xa4cB0x4cc
    prev=[0xa46B0x4cc], succ=[0x2da96B0x4cc]
    =================================
    0xa4cS0x4cc: va4cV4cc(0x1) = CONST 
    0xa4eS0x4cc: va4eV4cc(0xa0) = CONST 
    0xa50S0x4cc: va50V4cc(0x2) = CONST 
    0xa52S0x4cc: va52V4cc(0x10000000000000000000000000000000000000000) = EXP va50V4cc(0x2), va4eV4cc(0xa0)
    0xa53S0x4cc: va53V4cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB va52V4cc(0x10000000000000000000000000000000000000000), va4cV4cc(0x1)
    0xa54S0x4cc: va54V4cc = CALLER 
    0xa56S0x4cc: va56V4cc = AND va53V4cc(0xffffffffffffffffffffffffffffffffffffffff), va54V4cc
    0xa57S0x4cc: va57V4cc(0x0) = CONST 
    0xa5bS0x4cc: MSTORE va57V4cc(0x0), va56V4cc
    0xa5cS0x4cc: va5cV4cc(0x1) = CONST 
    0xa5eS0x4cc: va5eV4cc(0x20) = CONST 
    0xa62S0x4cc: MSTORE va5eV4cc(0x20), va5cV4cc(0x1)
    0xa63S0x4cc: va63V4cc(0x40) = CONST 
    0xa67S0x4cc: va67V4cc = SHA3 va57V4cc(0x0), va63V4cc(0x40)
    0xa69S0x4cc: va69V4cc = SLOAD va67V4cc
    0xa6cS0x4cc: va6cV4cc = SUB va69V4cc, v4de
    0xa6eS0x4cc: SSTORE va67V4cc, va6cV4cc
    0xa71S0x4cc: va71V4cc = AND v4db, va53V4cc(0xffffffffffffffffffffffffffffffffffffffff)
    0xa74S0x4cc: MSTORE va57V4cc(0x0), va71V4cc
    0xa78S0x4cc: va78V4cc = SHA3 va57V4cc(0x0), va63V4cc(0x40)
    0xa7aS0x4cc: va7aV4cc = SLOAD va78V4cc
    0xa7cS0x4cc: va7cV4cc = ADD v4de, va7aV4cc
    0xa7eS0x4cc: SSTORE va78V4cc, va7cV4cc
    0xa80S0x4cc: va80V4cc = MLOAD va63V4cc(0x40)
    0xa83S0x4cc: MSTORE va80V4cc, v4de
    0xa85S0x4cc: va85V4cc = MLOAD va63V4cc(0x40)
    0xa88S0x4cc: va88V4cc(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xaadS0x4cc: vaadV4cc(0x0) = SUB va80V4cc, va85V4cc
    0xab0S0x4cc: vab0V4cc(0x20) = ADD va5eV4cc(0x20), vaadV4cc(0x0)
    0xab2S0x4cc: LOG3 va85V4cc, vab0V4cc(0x20), va88V4cc(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), va56V4cc, va71V4cc
    0xab4S0x4cc: vab4V4cc(0x1) = CONST 
    0xab6S0x4cc: vab6V4cc(0x2da96) = CONST 
    0xab9S0x4cc: JUMP vab6V4cc(0x2da96)

    Begin block 0x2da96B0x4cc
    prev=[0xa4cB0x4cc], succ=[0x24581]
    =================================
    0x2da9bS0x4cc: JUMP v4cd(0x24581)

    Begin block 0x24581
    prev=[0x2da96B0x4cc, 0x2dabbB0x4cc], succ=[]
    =================================
    0x4ccS0x24581_0: v4e2_0V24581_0 = PHI vab4V4cc(0x1), vabcV4cc(0x0)
    0x24582: v24582(0x40) = CONST 
    0x24585: v24585 = MLOAD v24582(0x40)
    0x24587: v24587 = ISZERO v4e2_0V24581_0
    0x24588: v24588 = ISZERO v24587
    0x2458a: MSTORE v24585, v24588
    0x2458b: v2458b = MLOAD v24582(0x40)
    0x2458f: v2458f(0x0) = SUB v24585, v2458b
    0x24590: v24590(0x20) = CONST 
    0x24592: v24592(0x20) = ADD v24590(0x20), v2458f(0x0)
    0x24594: RETURN v2458b, v24592(0x20)

    Begin block 0xabaB0x4cc
    prev=[0xa46B0x4cc], succ=[0x2dabbB0x4cc]
    =================================
    0xabcS0x4cc: vabcV4cc(0x0) = CONST 
    0xabeS0x4cc: vabeV4cc(0x2dabb) = CONST 
    0xac1S0x4cc: JUMP vabeV4cc(0x2dabb)

    Begin block 0x2dabbB0x4cc
    prev=[0xabaB0x4cc], succ=[0x24581]
    =================================
    0x2dac0S0x4cc: JUMP v4cd(0x24581)

    Begin block 0xa41B0x4cc
    prev=[0xa1dB0x4cc], succ=[0xa46B0x4cc]
    =================================
    0xa42S0x4cc: va42V4cc(0x0) = CONST 
    0xa45S0x4cc: va45V4cc = GT v4de, va42V4cc(0x0)
    0xd51cS0x4cc: vd51cV4cc(0xa46) = CONST 
    0xd53cS0x4cc: JUMP vd51cV4cc(0xa46)

}

function makeTokens()() public {
    Begin block 0x4f7
    prev=[], succ=[0x245b4]
    =================================
    0x4f8: v4f8(0x245b4) = CONST 
    0x4fb: v4fb(0x557) = CONST 
    0x4fe: CALLPRIVATE v4fb(0x557), v4f8(0x245b4)

    Begin block 0x245b4
    prev=[0x4f7], succ=[]
    =================================
    0x245b5: STOP 

}

function fundingStartBlock()() public {
    Begin block 0x501
    prev=[], succ=[0x508, 0x509]
    =================================
    0x502: v502 = CALLVALUE 
    0x503: v503 = ISZERO v502
    0x504: v504(0x509) = CONST 
    0x507: JUMPI v504(0x509), v503

    Begin block 0x508
    prev=[0x501], succ=[]
    =================================
    0x508: THROW 

    Begin block 0x509
    prev=[0x501], succ=[0xac9]
    =================================
    0x50a: v50a(0x245d5) = CONST 
    0x50d: v50d(0xac9) = CONST 
    0x510: JUMP v50d(0xac9)

    Begin block 0xac9
    prev=[0x509], succ=[0x245d5]
    =================================
    0xaca: vaca(0x6) = CONST 
    0xacc: vacc = SLOAD vaca(0x6)
    0xace: JUMP v50a(0x245d5)

    Begin block 0x245d5
    prev=[0xac9], succ=[]
    =================================
    0x245d6: v245d6(0x40) = CONST 
    0x245d9: v245d9 = MLOAD v245d6(0x40)
    0x245dc: MSTORE v245d9, vacc
    0x245dd: v245dd = MLOAD v245d6(0x40)
    0x245e1: v245e1(0x0) = SUB v245d9, v245dd
    0x245e2: v245e2(0x20) = CONST 
    0x245e4: v245e4(0x20) = ADD v245e2(0x20), v245e1(0x0)
    0x245e6: RETURN v245dd, v245e4(0x20)

}

function allowance(address,address)() public {
    Begin block 0x523
    prev=[], succ=[0x52a, 0x52b]
    =================================
    0x524: v524 = CALLVALUE 
    0x525: v525 = ISZERO v524
    0x526: v526(0x52b) = CONST 
    0x529: JUMPI v526(0x52b), v525

    Begin block 0x52a
    prev=[0x523], succ=[]
    =================================
    0x52a: THROW 

    Begin block 0x52b
    prev=[0x523], succ=[0xacfB0x52b]
    =================================
    0x52c: v52c(0x24606) = CONST 
    0x52f: v52f(0x1) = CONST 
    0x531: v531(0xa0) = CONST 
    0x533: v533(0x2) = CONST 
    0x535: v535(0x10000000000000000000000000000000000000000) = EXP v533(0x2), v531(0xa0)
    0x536: v536(0xffffffffffffffffffffffffffffffffffffffff) = SUB v535(0x10000000000000000000000000000000000000000), v52f(0x1)
    0x537: v537(0x4) = CONST 
    0x539: v539 = CALLDATALOAD v537(0x4)
    0x53b: v53b = AND v536(0xffffffffffffffffffffffffffffffffffffffff), v539
    0x53d: v53d(0x24) = CONST 
    0x53f: v53f = CALLDATALOAD v53d(0x24)
    0x540: v540 = AND v53f, v536(0xffffffffffffffffffffffffffffffffffffffff)
    0x541: v541(0xacf) = CONST 
    0x544: JUMP v541(0xacf)

    Begin block 0xacfB0x52b
    prev=[0x52b], succ=[0xaf6B0x52b]
    =================================
    0xad0S0x52b: vad0V52b(0x1) = CONST 
    0xad2S0x52b: vad2V52b(0xa0) = CONST 
    0xad4S0x52b: vad4V52b(0x2) = CONST 
    0xad6S0x52b: vad6V52b(0x10000000000000000000000000000000000000000) = EXP vad4V52b(0x2), vad2V52b(0xa0)
    0xad7S0x52b: vad7V52b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vad6V52b(0x10000000000000000000000000000000000000000), vad0V52b(0x1)
    0xadaS0x52b: vadaV52b = AND v53b, vad7V52b(0xffffffffffffffffffffffffffffffffffffffff)
    0xadbS0x52b: vadbV52b(0x0) = CONST 
    0xadfS0x52b: MSTORE vadbV52b(0x0), vadaV52b
    0xae0S0x52b: vae0V52b(0x2) = CONST 
    0xae2S0x52b: vae2V52b(0x20) = CONST 
    0xae6S0x52b: MSTORE vae2V52b(0x20), vae0V52b(0x2)
    0xae7S0x52b: vae7V52b(0x40) = CONST 
    0xaebS0x52b: vaebV52b = SHA3 vadbV52b(0x0), vae7V52b(0x40)
    0xaeeS0x52b: vaeeV52b = AND v540, vad7V52b(0xffffffffffffffffffffffffffffffffffffffff)
    0xaf0S0x52b: MSTORE vadbV52b(0x0), vaeeV52b
    0xaf3S0x52b: MSTORE vae2V52b(0x20), vaebV52b
    0xaf4S0x52b: vaf4V52b = SHA3 vadbV52b(0x0), vae7V52b(0x40)
    0xaf5S0x52b: vaf5V52b = SLOAD vaf4V52b
    0xe91cS0x52b: ve91cV52b(0xaf6) = CONST 
    0xe93cS0x52b: JUMP ve91cV52b(0xaf6)

    Begin block 0xaf6B0x52b
    prev=[0xacfB0x52b], succ=[0x24606]
    =================================
    0xafbS0x52b: JUMP v52c(0x24606)

    Begin block 0x24606
    prev=[0xaf6B0x52b], succ=[]
    =================================
    0x24607: v24607(0x40) = CONST 
    0x2460a: v2460a = MLOAD v24607(0x40)
    0x2460d: MSTORE v2460a, vaf5V52b
    0x2460e: v2460e = MLOAD v24607(0x40)
    0x24612: v24612(0x0) = SUB v2460a, v2460e
    0x24613: v24613(0x20) = CONST 
    0x24615: v24615(0x20) = ADD v24613(0x20), v24612(0x0)
    0x24617: RETURN v2460e, v24615(0x20)

}

function 0x557(v557arg0) private {
    Begin block 0x557
    prev=[], succ=[0x56f, 0x574]
    =================================
    0x558: v558(0x5) = CONST 
    0x55a: v55a = SLOAD v558(0x5)
    0x55b: v55b(0x0) = CONST 
    0x560: v560(0xa0) = CONST 
    0x562: v562(0x2) = CONST 
    0x564: v564(0x10000000000000000000000000000000000000000) = EXP v562(0x2), v560(0xa0)
    0x566: v566 = DIV v55a, v564(0x10000000000000000000000000000000000000000)
    0x567: v567(0xff) = CONST 
    0x569: v569 = AND v567(0xff), v566
    0x56a: v56a = ISZERO v569
    0x56b: v56b(0x574) = CONST 
    0x56e: JUMPI v56b(0x574), v56a

    Begin block 0x56f
    prev=[0x557], succ=[]
    =================================
    0x56f: v56f(0x0) = CONST 
    0x571: v571(0x0) = CONST 
    0x573: REVERT v571(0x0), v56f(0x0)

    Begin block 0x574
    prev=[0x557], succ=[0x57f, 0x584]
    =================================
    0x575: v575(0x6) = CONST 
    0x577: v577 = SLOAD v575(0x6)
    0x578: v578 = NUMBER 
    0x579: v579 = LT v578, v577
    0x57a: v57a = ISZERO v579
    0x57b: v57b(0x584) = CONST 
    0x57e: JUMPI v57b(0x584), v57a

    Begin block 0x57f
    prev=[0x574], succ=[]
    =================================
    0x57f: v57f(0x0) = CONST 
    0x581: v581(0x0) = CONST 
    0x583: REVERT v581(0x0), v57f(0x0)

    Begin block 0x584
    prev=[0x574], succ=[0x58f, 0x594]
    =================================
    0x585: v585(0x7) = CONST 
    0x587: v587 = SLOAD v585(0x7)
    0x588: v588 = NUMBER 
    0x589: v589 = GT v588, v587
    0x58a: v58a = ISZERO v589
    0x58b: v58b(0x594) = CONST 
    0x58e: JUMPI v58b(0x594), v58a

    Begin block 0x58f
    prev=[0x584], succ=[]
    =================================
    0x58f: v58f(0x0) = CONST 
    0x591: v591(0x0) = CONST 
    0x593: REVERT v591(0x0), v58f(0x0)

    Begin block 0x594
    prev=[0x584], succ=[0x59c, 0x5a1]
    =================================
    0x595: v595 = CALLVALUE 
    0x596: v596 = ISZERO v595
    0x597: v597 = ISZERO v596
    0x598: v598(0x5a1) = CONST 
    0x59b: JUMPI v598(0x5a1), v597

    Begin block 0x59c
    prev=[0x594], succ=[]
    =================================
    0x59c: v59c(0x0) = CONST 
    0x59e: v59e(0x0) = CONST 
    0x5a0: REVERT v59e(0x0), v59c(0x0)

    Begin block 0x5a1
    prev=[0x594], succ=[0x5ad]
    =================================
    0x5a2: v5a2(0x5b2) = CONST 
    0x5a5: v5a5 = CALLVALUE 
    0x5a6: v5a6(0x5ad) = CONST 
    0x5a9: v5a9(0x7dd) = CONST 
    0x5ac: v5ac_0 = CALLPRIVATE v5a9(0x7dd), v5a6(0x5ad)

    Begin block 0x5ad
    prev=[0x5a1], succ=[0x5b2]
    =================================
    0x5ae: v5ae(0xafc) = CONST 
    0x5b1: v5b1_0 = CALLPRIVATE v5ae(0xafc), v5ac_0, v5a5, v5a2(0x5b2)

    Begin block 0x5b2
    prev=[0x5ad], succ=[0x5c0]
    =================================
    0x5b5: v5b5(0x5c0) = CONST 
    0x5b8: v5b8(0x0) = CONST 
    0x5ba: v5ba = SLOAD v5b8(0x0)
    0x5bc: v5bc(0xb2b) = CONST 
    0x5bf: v5bf_0 = CALLPRIVATE v5bc(0xb2b), v5b1_0, v5ba, v5b5(0x5c0)

    Begin block 0x5c0
    prev=[0x5b2], succ=[0x5d7, 0x5dc]
    =================================
    0x5c3: v5c3(0x422ca8b0a00a425000000) = CONST 
    0x5d1: v5d1 = LT v5c3(0x422ca8b0a00a425000000), v5bf_0
    0x5d2: v5d2 = ISZERO v5d1
    0x5d3: v5d3(0x5dc) = CONST 
    0x5d6: JUMPI v5d3(0x5dc), v5d2

    Begin block 0x5d7
    prev=[0x5c0], succ=[]
    =================================
    0x5d7: v5d7(0x0) = CONST 
    0x5d9: v5d9(0x0) = CONST 
    0x5db: REVERT v5d9(0x0), v5d7(0x0)

    Begin block 0x5dc
    prev=[0x5c0], succ=[0x636]
    =================================
    0x5dd: v5dd(0x0) = CONST 
    0x5e1: SSTORE v5dd(0x0), v5bf_0
    0x5e2: v5e2(0x1) = CONST 
    0x5e4: v5e4(0xa0) = CONST 
    0x5e6: v5e6(0x2) = CONST 
    0x5e8: v5e8(0x10000000000000000000000000000000000000000) = EXP v5e6(0x2), v5e4(0xa0)
    0x5e9: v5e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5e8(0x10000000000000000000000000000000000000000), v5e2(0x1)
    0x5ea: v5ea = CALLER 
    0x5eb: v5eb = AND v5ea, v5e9(0xffffffffffffffffffffffffffffffffffffffff)
    0x5ee: MSTORE v5dd(0x0), v5eb
    0x5ef: v5ef(0x1) = CONST 
    0x5f1: v5f1(0x20) = CONST 
    0x5f5: MSTORE v5f1(0x20), v5ef(0x1)
    0x5f6: v5f6(0x40) = CONST 
    0x5fb: v5fb = SHA3 v5dd(0x0), v5f6(0x40)
    0x5fd: v5fd = SLOAD v5fb
    0x5ff: v5ff = ADD v5b1_0, v5fd
    0x601: SSTORE v5fb, v5ff
    0x603: v603 = MLOAD v5f6(0x40)
    0x606: MSTORE v603, v5b1_0
    0x608: v608 = MLOAD v5f6(0x40)
    0x60b: v60b(0xc304ffc4eedb3959e8049ee81db208989d7aa78f7664b9d2ff42a91ce7b89179) = CONST 
    0x630: v630(0x0) = SUB v603, v608
    0x633: v633(0x20) = ADD v5f1(0x20), v630(0x0)
    0x635: LOG2 v608, v633(0x20), v60b(0xc304ffc4eedb3959e8049ee81db208989d7aa78f7664b9d2ff42a91ce7b89179), v5eb
    0x491c: v491c(0x636) = CONST 
    0x493c: JUMP v491c(0x636)

    Begin block 0x636
    prev=[0x5dc], succ=[]
    =================================
    0x639: RETURNPRIVATE v557arg0

}

function 0x7dd(v7ddarg0) private {
    Begin block 0x7dd
    prev=[], succ=[0x7f5, 0x7ec]
    =================================
    0x7de: v7de(0x0) = CONST 
    0x7e0: v7e0(0x6) = CONST 
    0x7e2: v7e2 = SLOAD v7e0(0x6)
    0x7e3: v7e3 = NUMBER 
    0x7e4: v7e4 = LT v7e3, v7e2
    0x7e5: v7e5 = ISZERO v7e4
    0x7e7: v7e7 = ISZERO v7e5
    0x7e8: v7e8(0x7f5) = CONST 
    0x7eb: JUMPI v7e8(0x7f5), v7e7

    Begin block 0x7f5
    prev=[0x7dd, 0x7ec], succ=[0x802, 0x7fb]
    =================================
    0x7f5_0x0: v7f5_0 = PHI v7e5, v7f4
    0x7f6: v7f6 = ISZERO v7f5_0
    0x7f7: v7f7(0x802) = CONST 
    0x7fa: JUMPI v7f7(0x802), v7f6

    Begin block 0x802
    prev=[0x7f5], succ=[0x819, 0x80f]
    =================================
    0x803: v803(0x6) = CONST 
    0x805: v805 = SLOAD v803(0x6)
    0x806: v806 = NUMBER 
    0x807: v807 = LT v806, v805
    0x808: v808 = ISZERO v807
    0x80a: v80a = ISZERO v808
    0x80b: v80b(0x819) = CONST 
    0x80e: JUMPI v80b(0x819), v80a

    Begin block 0x819
    prev=[0x802, 0x80f], succ=[0x826, 0x81f]
    =================================
    0x819_0x0: v819_0 = PHI v808, v818
    0x81a: v81a = ISZERO v819_0
    0x81b: v81b(0x826) = CONST 
    0x81e: JUMPI v81b(0x826), v81a

    Begin block 0x826
    prev=[0x819], succ=[0x53350]
    =================================
    0x828: v828(0x82) = CONST 
    0x991c: v991c(0x53350) = CONST 
    0x993c: JUMP v991c(0x53350)

    Begin block 0x53350
    prev=[0x826], succ=[]
    =================================
    0x53352: RETURNPRIVATE v7ddarg0, v828(0x82)

    Begin block 0x81f
    prev=[0x819], succ=[0x2b9e5]
    =================================
    0x820: v820(0xaa) = CONST 
    0x822: v822(0x2b9e5) = CONST 
    0x825: JUMP v822(0x2b9e5)

    Begin block 0x2b9e5
    prev=[0x81f], succ=[]
    =================================
    0x2b9e7: RETURNPRIVATE v7ddarg0, v820(0xaa)

    Begin block 0x80f
    prev=[0x802], succ=[0x819]
    =================================
    0x810: v810(0x6) = CONST 
    0x812: v812 = SLOAD v810(0x6)
    0x813: v813(0x900e) = CONST 
    0x816: v816 = ADD v813(0x900e), v812
    0x817: v817 = NUMBER 
    0x818: v818 = LT v817, v816
    0x8f1c: v8f1c(0x819) = CONST 
    0x8f3c: JUMP v8f1c(0x819)

    Begin block 0x7fb
    prev=[0x7f5], succ=[0x2b9c3]
    =================================
    0x7fc: v7fc(0xc8) = CONST 
    0x7fe: v7fe(0x2b9c3) = CONST 
    0x801: JUMP v7fe(0x2b9c3)

    Begin block 0x2b9c3
    prev=[0x7fb], succ=[]
    =================================
    0x2b9c5: RETURNPRIVATE v7ddarg0, v7fc(0xc8)

    Begin block 0x7ec
    prev=[0x7dd], succ=[0x7f5]
    =================================
    0x7ed: v7ed(0x6) = CONST 
    0x7ef: v7ef = SLOAD v7ed(0x6)
    0x7f0: v7f0(0xfc) = CONST 
    0x7f2: v7f2 = ADD v7f0(0xfc), v7ef
    0x7f3: v7f3 = NUMBER 
    0x7f4: v7f4 = LT v7f3, v7f2
    0x851c: v851c(0x7f5) = CONST 
    0x853c: JUMP v851c(0x7f5)

}

function 0xafc(vafcarg0, vafcarg1, vafcarg2) private {
    Begin block 0xafc
    prev=[], succ=[0xb09, 0xb180xafc]
    =================================
    0xafd: vafd(0x0) = CONST 
    0xb01: vb01 = MUL vafcarg0, vafcarg1
    0xb03: vb03 = ISZERO vafcarg1
    0xb05: vb05(0xb18) = CONST 
    0xb08: JUMPI vb05(0xb18), vb03

    Begin block 0xb09
    prev=[0xafc], succ=[0xb14, 0xb15]
    =================================
    0xb0e: vb0e = ISZERO vafcarg1
    0xb0f: vb0f = ISZERO vb0e
    0xb10: vb10(0xb15) = CONST 
    0xb13: JUMPI vb10(0xb15), vb0f

    Begin block 0xb14
    prev=[0xb09], succ=[]
    =================================
    0xb14: THROW 

    Begin block 0xb15
    prev=[0xb09], succ=[0xb180xafc]
    =================================
    0xb16: vb16 = DIV vb01, vafcarg1
    0xb17: vb17 = EQ vb16, vafcarg0
    0xf31c: vf31c(0xb18) = CONST 
    0xf33c: JUMP vf31c(0xb18)

    Begin block 0xb180xafc
    prev=[0xafc, 0xb15], succ=[0xb1f0xafc, 0x2dae00xafc]
    =================================
    0xb180xafc_0x0: vb18afc_0 = PHI vb03, vb17
    0xb190xafc: vafcb19 = ISZERO vb18afc_0
    0xb1a0xafc: vafcb1a = ISZERO vafcb19
    0xb1b0xafc: vafcb1b(0x2dae0) = CONST 
    0xb1e0xafc: JUMPI vafcb1b(0x2dae0), vafcb1a

    Begin block 0xb1f0xafc
    prev=[0xb180xafc], succ=[]
    =================================
    0xb1f0xafc: THROW 

    Begin block 0x2dae00xafc
    prev=[0xb180xafc], succ=[0x534270xafc]
    =================================
    0x3ccdc0xafc: vafc3ccdc(0x53427) = CONST 
    0x3ccfc0xafc: JUMP vafc3ccdc(0x53427)

    Begin block 0x534270xafc
    prev=[0x2dae00xafc], succ=[]
    =================================
    0x5342d0xafc: RETURNPRIVATE vafcarg2, vb01

}

function 0xb2b(vb2barg0, vb2barg1, vb2barg2) private {
    Begin block 0xb2b
    prev=[], succ=[0xb3b, 0xb180xb2b]
    =================================
    0xb2c: vb2c(0x0) = CONST 
    0xb30: vb30 = ADD vb2barg0, vb2barg1
    0xb33: vb33 = LT vb30, vb2barg1
    0xb35: vb35 = ISZERO vb33
    0xb37: vb37(0xb18) = CONST 
    0xb3a: JUMPI vb37(0xb18), vb33

    Begin block 0xb3b
    prev=[0xb2b], succ=[0xb40]
    =================================
    0xb3e: vb3e = LT vb30, vb2barg0
    0xb3f: vb3f = ISZERO vb3e
    0x1071c: v1071c(0xb40) = CONST 
    0x1073c: JUMP v1071c(0xb40)

    Begin block 0xb40
    prev=[0xb3b], succ=[0xb47, 0x3cd1c]
    =================================
    0xb41: vb41 = ISZERO vb3f
    0xb42: vb42 = ISZERO vb41
    0xb43: vb43(0x3cd1c) = CONST 
    0xb46: JUMPI vb43(0x3cd1c), vb42

    Begin block 0xb47
    prev=[0xb40], succ=[]
    =================================
    0xb47: THROW 

    Begin block 0x3cd1c
    prev=[0xb40], succ=[0x5344d]
    =================================
    0x4bf18: v4bf18(0x5344d) = CONST 
    0x4bf38: JUMP v4bf18(0x5344d)

    Begin block 0x5344d
    prev=[0x3cd1c], succ=[]
    =================================
    0x53453: RETURNPRIVATE vb2barg2, vb30

    Begin block 0xb180xb2b
    prev=[0xb2b], succ=[0xb1f0xb2b, 0x2dae00xb2b]
    =================================
    0xb190xb2b: vb2bb19 = ISZERO vb35
    0xb1a0xb2b: vb2bb1a = ISZERO vb2bb19
    0xb1b0xb2b: vb2bb1b(0x2dae0) = CONST 
    0xb1e0xb2b: JUMPI vb2bb1b(0x2dae0), vb2bb1a

    Begin block 0xb1f0xb2b
    prev=[0xb180xb2b], succ=[]
    =================================
    0xb1f0xb2b: THROW 

    Begin block 0x2dae00xb2b
    prev=[0xb180xb2b], succ=[0x534270xb2b]
    =================================
    0x3ccdc0xb2b: vb2b3ccdc(0x53427) = CONST 
    0x3ccfc0xb2b: JUMP vb2b3ccdc(0x53427)

    Begin block 0x534270xb2b
    prev=[0x2dae00xb2b], succ=[]
    =================================
    0x5342d0xb2b: RETURNPRIVATE vb2barg2, vb30

}

