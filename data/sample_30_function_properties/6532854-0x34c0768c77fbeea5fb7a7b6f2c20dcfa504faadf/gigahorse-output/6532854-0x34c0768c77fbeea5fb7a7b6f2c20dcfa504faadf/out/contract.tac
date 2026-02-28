function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x5003a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x3f23a: v3f23a(0x5003a) = CONST 
    0x3f25a: JUMPI v3f23a(0x5003a), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x50a3a]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x5d2035b) = CONST 
    0x3b: v3b = EQ v34, v35(0x5d2035b)
    0x3fc3a: v3fc3a(0x50a3a) = CONST 
    0x3fc5a: JUMPI v3fc3a(0x50a3a), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x5143a, 0x4b]
    =================================
    0x41: v41(0x6fdde03) = CONST 
    0x46: v46 = EQ v41(0x6fdde03), v34
    0x4063a: v4063a(0x5143a) = CONST 
    0x4065a: JUMPI v4063a(0x5143a), v46

    Begin block 0x5143a
    prev=[0x40], succ=[]
    =================================
    0x5145a: v5145a(0x181) = CONST 
    0x5147a: CALLPRIVATE v5145a(0x181)

    Begin block 0x4b
    prev=[0x40], succ=[0x51e3a, 0x56]
    =================================
    0x4c: v4c(0x95ea7b3) = CONST 
    0x51: v51 = EQ v4c(0x95ea7b3), v34
    0x4103a: v4103a(0x51e3a) = CONST 
    0x4105a: JUMPI v4103a(0x51e3a), v51

    Begin block 0x51e3a
    prev=[0x4b], succ=[]
    =================================
    0x51e5a: v51e5a(0x20b) = CONST 
    0x51e7a: CALLPRIVATE v51e5a(0x20b)

    Begin block 0x56
    prev=[0x4b], succ=[0x5283a, 0x61]
    =================================
    0x57: v57(0x14133a7c) = CONST 
    0x5c: v5c = EQ v57(0x14133a7c), v34
    0x41a3a: v41a3a(0x5283a) = CONST 
    0x41a5a: JUMPI v41a3a(0x5283a), v5c

    Begin block 0x5283a
    prev=[0x56], succ=[]
    =================================
    0x5285a: v5285a(0x22f) = CONST 
    0x5287a: CALLPRIVATE v5285a(0x22f)

    Begin block 0x61
    prev=[0x56], succ=[0x5323a, 0x6c]
    =================================
    0x62: v62(0x18160ddd) = CONST 
    0x67: v67 = EQ v62(0x18160ddd), v34
    0x4243a: v4243a(0x5323a) = CONST 
    0x4245a: JUMPI v4243a(0x5323a), v67

    Begin block 0x5323a
    prev=[0x61], succ=[]
    =================================
    0x5325a: v5325a(0x252) = CONST 
    0x5327a: CALLPRIVATE v5325a(0x252)

    Begin block 0x6c
    prev=[0x61], succ=[0x53c3a, 0x77]
    =================================
    0x6d: v6d(0x23b872dd) = CONST 
    0x72: v72 = EQ v6d(0x23b872dd), v34
    0x42e3a: v42e3a(0x53c3a) = CONST 
    0x42e5a: JUMPI v42e3a(0x53c3a), v72

    Begin block 0x53c3a
    prev=[0x6c], succ=[]
    =================================
    0x53c5a: v53c5a(0x279) = CONST 
    0x53c7a: CALLPRIVATE v53c5a(0x279)

    Begin block 0x77
    prev=[0x6c], succ=[0x5463a, 0x82]
    =================================
    0x78: v78(0x2e4dde60) = CONST 
    0x7d: v7d = EQ v78(0x2e4dde60), v34
    0x4383a: v4383a(0x5463a) = CONST 
    0x4385a: JUMPI v4383a(0x5463a), v7d

    Begin block 0x5463a
    prev=[0x77], succ=[]
    =================================
    0x5465a: v5465a(0x2a3) = CONST 
    0x5467a: CALLPRIVATE v5465a(0x2a3)

    Begin block 0x82
    prev=[0x77], succ=[0x5503a, 0x8d]
    =================================
    0x83: v83(0x313ce567) = CONST 
    0x88: v88 = EQ v83(0x313ce567), v34
    0x4423a: v4423a(0x5503a) = CONST 
    0x4425a: JUMPI v4423a(0x5503a), v88

    Begin block 0x5503a
    prev=[0x82], succ=[]
    =================================
    0x5505a: v5505a(0x2c4) = CONST 
    0x5507a: CALLPRIVATE v5505a(0x2c4)

    Begin block 0x8d
    prev=[0x82], succ=[0x55a3a, 0x98]
    =================================
    0x8e: v8e(0x40c10f19) = CONST 
    0x93: v93 = EQ v8e(0x40c10f19), v34
    0x44c3a: v44c3a(0x55a3a) = CONST 
    0x44c5a: JUMPI v44c3a(0x55a3a), v93

    Begin block 0x55a3a
    prev=[0x8d], succ=[]
    =================================
    0x55a5a: v55a5a(0x2f2) = CONST 
    0x55a7a: CALLPRIVATE v55a5a(0x2f2)

    Begin block 0x98
    prev=[0x8d], succ=[0x5643a, 0xa3]
    =================================
    0x99: v99(0x4c66326d) = CONST 
    0x9e: v9e = EQ v99(0x4c66326d), v34
    0x4563a: v4563a(0x5643a) = CONST 
    0x4565a: JUMPI v4563a(0x5643a), v9e

    Begin block 0x5643a
    prev=[0x98], succ=[]
    =================================
    0x5645a: v5645a(0x316) = CONST 
    0x5647a: CALLPRIVATE v5645a(0x316)

    Begin block 0xa3
    prev=[0x98], succ=[0x56e3a, 0xae]
    =================================
    0xa4: va4(0x66188463) = CONST 
    0xa9: va9 = EQ va4(0x66188463), v34
    0x4603a: v4603a(0x56e3a) = CONST 
    0x4605a: JUMPI v4603a(0x56e3a), va9

    Begin block 0x56e3a
    prev=[0xa3], succ=[]
    =================================
    0x56e5a: v56e5a(0x337) = CONST 
    0x56e7a: CALLPRIVATE v56e5a(0x337)

    Begin block 0xae
    prev=[0xa3], succ=[0x5783a, 0xb9]
    =================================
    0xaf: vaf(0x70a08231) = CONST 
    0xb4: vb4 = EQ vaf(0x70a08231), v34
    0x46a3a: v46a3a(0x5783a) = CONST 
    0x46a5a: JUMPI v46a3a(0x5783a), vb4

    Begin block 0x5783a
    prev=[0xae], succ=[]
    =================================
    0x5785a: v5785a(0x35b) = CONST 
    0x5787a: CALLPRIVATE v5785a(0x35b)

    Begin block 0xb9
    prev=[0xae], succ=[0x5823a, 0xc4]
    =================================
    0xba: vba(0x715018a6) = CONST 
    0xbf: vbf = EQ vba(0x715018a6), v34
    0x4743a: v4743a(0x5823a) = CONST 
    0x4745a: JUMPI v4743a(0x5823a), vbf

    Begin block 0x5823a
    prev=[0xb9], succ=[]
    =================================
    0x5825a: v5825a(0x37c) = CONST 
    0x5827a: CALLPRIVATE v5825a(0x37c)

    Begin block 0xc4
    prev=[0xb9], succ=[0x58c3a, 0xcf]
    =================================
    0xc5: vc5(0x7a983e69) = CONST 
    0xca: vca = EQ vc5(0x7a983e69), v34
    0x47e3a: v47e3a(0x58c3a) = CONST 
    0x47e5a: JUMPI v47e3a(0x58c3a), vca

    Begin block 0x58c3a
    prev=[0xc4], succ=[]
    =================================
    0x58c5a: v58c5a(0x391) = CONST 
    0x58c7a: CALLPRIVATE v58c5a(0x391)

    Begin block 0xcf
    prev=[0xc4], succ=[0x5963a, 0xda]
    =================================
    0xd0: vd0(0x7d64bcb4) = CONST 
    0xd5: vd5 = EQ vd0(0x7d64bcb4), v34
    0x4883a: v4883a(0x5963a) = CONST 
    0x4885a: JUMPI v4883a(0x5963a), vd5

    Begin block 0x5963a
    prev=[0xcf], succ=[]
    =================================
    0x5965a: v5965a(0x3b2) = CONST 
    0x5967a: CALLPRIVATE v5965a(0x3b2)

    Begin block 0xda
    prev=[0xcf], succ=[0x5a03a, 0xe5]
    =================================
    0xdb: vdb(0x8da5cb5b) = CONST 
    0xe0: ve0 = EQ vdb(0x8da5cb5b), v34
    0x4923a: v4923a(0x5a03a) = CONST 
    0x4925a: JUMPI v4923a(0x5a03a), ve0

    Begin block 0x5a03a
    prev=[0xda], succ=[]
    =================================
    0x5a05a: v5a05a(0x3c7) = CONST 
    0x5a07a: CALLPRIVATE v5a05a(0x3c7)

    Begin block 0xe5
    prev=[0xda], succ=[0x5aa3a, 0xf0]
    =================================
    0xe6: ve6(0x923108d9) = CONST 
    0xeb: veb = EQ ve6(0x923108d9), v34
    0x49c3a: v49c3a(0x5aa3a) = CONST 
    0x49c5a: JUMPI v49c3a(0x5aa3a), veb

    Begin block 0x5aa3a
    prev=[0xe5], succ=[]
    =================================
    0x5aa5a: v5aa5a(0x3f8) = CONST 
    0x5aa7a: CALLPRIVATE v5aa5a(0x3f8)

    Begin block 0xf0
    prev=[0xe5], succ=[0x5b43a, 0xfb]
    =================================
    0xf1: vf1(0x95d89b41) = CONST 
    0xf6: vf6 = EQ vf1(0x95d89b41), v34
    0x4a63a: v4a63a(0x5b43a) = CONST 
    0x4a65a: JUMPI v4a63a(0x5b43a), vf6

    Begin block 0x5b43a
    prev=[0xf0], succ=[]
    =================================
    0x5b45a: v5b45a(0x410) = CONST 
    0x5b47a: CALLPRIVATE v5b45a(0x410)

    Begin block 0xfb
    prev=[0xf0], succ=[0x5be3a, 0x106]
    =================================
    0xfc: vfc(0xa9059cbb) = CONST 
    0x101: v101 = EQ vfc(0xa9059cbb), v34
    0x4b03a: v4b03a(0x5be3a) = CONST 
    0x4b05a: JUMPI v4b03a(0x5be3a), v101

    Begin block 0x5be3a
    prev=[0xfb], succ=[]
    =================================
    0x5be5a: v5be5a(0x425) = CONST 
    0x5be7a: CALLPRIVATE v5be5a(0x425)

    Begin block 0x106
    prev=[0xfb], succ=[0x5c83a, 0x111]
    =================================
    0x107: v107(0xb1d6a2f0) = CONST 
    0x10c: v10c = EQ v107(0xb1d6a2f0), v34
    0x4ba3a: v4ba3a(0x5c83a) = CONST 
    0x4ba5a: JUMPI v4ba3a(0x5c83a), v10c

    Begin block 0x5c83a
    prev=[0x106], succ=[]
    =================================
    0x5c85a: v5c85a(0x449) = CONST 
    0x5c87a: CALLPRIVATE v5c85a(0x449)

    Begin block 0x111
    prev=[0x106], succ=[0x5d23a, 0x11c]
    =================================
    0x112: v112(0xcf1b037c) = CONST 
    0x117: v117 = EQ v112(0xcf1b037c), v34
    0x4c43a: v4c43a(0x5d23a) = CONST 
    0x4c45a: JUMPI v4c43a(0x5d23a), v117

    Begin block 0x5d23a
    prev=[0x111], succ=[]
    =================================
    0x5d25a: v5d25a(0x45e) = CONST 
    0x5d27a: CALLPRIVATE v5d25a(0x45e)

    Begin block 0x11c
    prev=[0x111], succ=[0x5dc3a, 0x127]
    =================================
    0x11d: v11d(0xd73dd623) = CONST 
    0x122: v122 = EQ v11d(0xd73dd623), v34
    0x4ce3a: v4ce3a(0x5dc3a) = CONST 
    0x4ce5a: JUMPI v4ce3a(0x5dc3a), v122

    Begin block 0x5dc3a
    prev=[0x11c], succ=[]
    =================================
    0x5dc5a: v5dc5a(0x47f) = CONST 
    0x5dc7a: CALLPRIVATE v5dc5a(0x47f)

    Begin block 0x127
    prev=[0x11c], succ=[0x5e63a, 0x132]
    =================================
    0x128: v128(0xdb0d7a38) = CONST 
    0x12d: v12d = EQ v128(0xdb0d7a38), v34
    0x4d83a: v4d83a(0x5e63a) = CONST 
    0x4d85a: JUMPI v4d83a(0x5e63a), v12d

    Begin block 0x5e63a
    prev=[0x127], succ=[]
    =================================
    0x5e65a: v5e65a(0x4a3) = CONST 
    0x5e67a: CALLPRIVATE v5e65a(0x4a3)

    Begin block 0x132
    prev=[0x127], succ=[0x5f03a, 0x13d]
    =================================
    0x133: v133(0xdd62ed3e) = CONST 
    0x138: v138 = EQ v133(0xdd62ed3e), v34
    0x4e23a: v4e23a(0x5f03a) = CONST 
    0x4e25a: JUMPI v4e23a(0x5f03a), v138

    Begin block 0x5f03a
    prev=[0x132], succ=[]
    =================================
    0x5f05a: v5f05a(0x4c4) = CONST 
    0x5f07a: CALLPRIVATE v5f05a(0x4c4)

    Begin block 0x13d
    prev=[0x132], succ=[0x5fa3a, 0x148]
    =================================
    0x13e: v13e(0xf2fde38b) = CONST 
    0x143: v143 = EQ v13e(0xf2fde38b), v34
    0x4ec3a: v4ec3a(0x5fa3a) = CONST 
    0x4ec5a: JUMPI v4ec3a(0x5fa3a), v143

    Begin block 0x5fa3a
    prev=[0x13d], succ=[]
    =================================
    0x5fa5a: v5fa5a(0x4eb) = CONST 
    0x5fa7a: CALLPRIVATE v5fa5a(0x4eb)

    Begin block 0x148
    prev=[0x13d], succ=[0x5003a, 0x6043a]
    =================================
    0x149: v149(0xf308846f) = CONST 
    0x14e: v14e = EQ v149(0xf308846f), v34
    0x4f63a: v4f63a(0x6043a) = CONST 
    0x4f65a: JUMPI v4f63a(0x6043a), v14e

    Begin block 0x5003a
    prev=[0x0, 0x148], succ=[]
    =================================
    0x5005a: v5005a(0x153) = CONST 
    0x5007a: CALLPRIVATE v5005a(0x153)

    Begin block 0x6043a
    prev=[0x148], succ=[]
    =================================
    0x6045a: v6045a(0x50c) = CONST 
    0x6047a: CALLPRIVATE v6045a(0x50c)

    Begin block 0x50a3a
    prev=[0xd], succ=[]
    =================================
    0x50a5a: v50a5a(0x158) = CONST 
    0x50a7a: CALLPRIVATE v50a5a(0x158)

}

function fallback()() public {
    Begin block 0x153
    prev=[], succ=[]
    =================================
    0x154: v154(0x0) = CONST 
    0x157: REVERT v154(0x0), v154(0x0)

}

function mintingFinished()() public {
    Begin block 0x158
    prev=[], succ=[0x160, 0x164]
    =================================
    0x159: v159 = CALLVALUE 
    0x15b: v15b = ISZERO v159
    0x15c: v15c(0x164) = CONST 
    0x15f: JUMPI v15c(0x164), v15b

    Begin block 0x160
    prev=[0x158], succ=[]
    =================================
    0x160: v160(0x0) = CONST 
    0x163: REVERT v160(0x0), v160(0x0)

    Begin block 0x164
    prev=[0x158], succ=[0x52d]
    =================================
    0x166: v166(0x1afb8) = CONST 
    0x169: v169(0x52d) = CONST 
    0x16c: JUMP v169(0x52d)

    Begin block 0x52d
    prev=[0x164], succ=[0x1afb8]
    =================================
    0x52e: v52e(0x3) = CONST 
    0x530: v530 = SLOAD v52e(0x3)
    0x531: v531(0xa0) = CONST 
    0x533: v533(0x2) = CONST 
    0x535: v535(0x10000000000000000000000000000000000000000) = EXP v533(0x2), v531(0xa0)
    0x537: v537 = DIV v530, v535(0x10000000000000000000000000000000000000000)
    0x538: v538(0xff) = CONST 
    0x53a: v53a = AND v538(0xff), v537
    0x53c: JUMP v166(0x1afb8)

    Begin block 0x1afb8
    prev=[0x52d], succ=[]
    =================================
    0x1afb9: v1afb9(0x40) = CONST 
    0x1afbc: v1afbc = MLOAD v1afb9(0x40)
    0x1afbe: v1afbe = ISZERO v53a
    0x1afbf: v1afbf = ISZERO v1afbe
    0x1afc1: MSTORE v1afbc, v1afbf
    0x1afc2: v1afc2 = MLOAD v1afb9(0x40)
    0x1afc6: v1afc6(0x0) = SUB v1afbc, v1afc2
    0x1afc7: v1afc7(0x20) = CONST 
    0x1afc9: v1afc9(0x20) = ADD v1afc7(0x20), v1afc6(0x0)
    0x1afcb: RETURN v1afc2, v1afc9(0x20)

}

function name()() public {
    Begin block 0x181
    prev=[], succ=[0x189, 0x18d]
    =================================
    0x182: v182 = CALLVALUE 
    0x184: v184 = ISZERO v182
    0x185: v185(0x18d) = CONST 
    0x188: JUMPI v185(0x18d), v184

    Begin block 0x189
    prev=[0x181], succ=[]
    =================================
    0x189: v189(0x0) = CONST 
    0x18c: REVERT v189(0x0), v189(0x0)

    Begin block 0x18d
    prev=[0x181], succ=[0x53d]
    =================================
    0x18f: v18f(0x1afeb) = CONST 
    0x192: v192(0x53d) = CONST 
    0x195: JUMP v192(0x53d)

    Begin block 0x53d
    prev=[0x18d], succ=[0x1afeb]
    =================================
    0x53e: v53e(0x40) = CONST 
    0x541: v541 = MLOAD v53e(0x40)
    0x544: v544 = ADD v53e(0x40), v541
    0x547: MSTORE v53e(0x40), v544
    0x548: v548(0xd) = CONST 
    0x54b: MSTORE v541, v548(0xd)
    0x54c: v54c(0x4175746f6d617465546f6b656e00000000000000000000000000000000000000) = CONST 
    0x56d: v56d(0x20) = CONST 
    0x570: v570 = ADD v541, v56d(0x20)
    0x571: MSTORE v570, v54c(0x4175746f6d617465546f6b656e00000000000000000000000000000000000000)
    0x573: JUMP v18f(0x1afeb)

    Begin block 0x1afeb
    prev=[0x53d], succ=[0x1b80x181]
    =================================
    0x1afec: v1afec(0x40) = CONST 
    0x1afef: v1afef = MLOAD v1afec(0x40)
    0x1aff0: v1aff0(0x20) = CONST 
    0x1aff4: MSTORE v1afef, v1aff0(0x20)
    0x1aff6: v1aff6(0xd) = MLOAD v541
    0x1aff9: v1aff9 = ADD v1afef, v1aff0(0x20)
    0x1affa: MSTORE v1aff9, v1aff6(0xd)
    0x1affc: v1affc(0xd) = MLOAD v541
    0x1b003: v1b003 = ADD v1afef, v1afec(0x40)
    0x1b006: v1b006 = ADD v541, v1aff0(0x20)
    0x1b00b: v1b00b(0x0) = CONST 
    0x1d201: v1d201(0x1b8) = CONST 
    0x1d221: JUMP v1d201(0x1b8)

    Begin block 0x1b80x181
    prev=[0x1afeb, 0x1c10x181], succ=[0x1d00x181, 0x1c10x181]
    =================================
    0x1b80x181_0x0: v1b8181_0 = PHI v1b00b(0x0), v1811cb
    0x1bb0x181: v1811bb = LT v1b8181_0, v1affc(0xd)
    0x1bc0x181: v1811bc = ISZERO v1811bb
    0x1bd0x181: v1811bd(0x1d0) = CONST 
    0x1c00x181: JUMPI v1811bd(0x1d0), v1811bc

    Begin block 0x1d00x181
    prev=[0x1b80x181], succ=[0x1e40x181, 0x1fd0x181]
    =================================
    0x1d90x181: v1811d9 = ADD v1affc(0xd), v1b003
    0x1db0x181: v1811db(0x1f) = CONST 
    0x1dd0x181: v1811dd(0xd) = AND v1811db(0x1f), v1affc(0xd)
    0x1df0x181: v1811df(0x0) = ISZERO v1811dd(0xd)
    0x1e00x181: v1811e0(0x1fd) = CONST 
    0x1e30x181: JUMPI v1811e0(0x1fd), v1811df(0x0)

    Begin block 0x1e40x181
    prev=[0x1d00x181], succ=[0x1fd0x181]
    =================================
    0x1e60x181: v1811e6 = SUB v1811d9, v1811dd(0xd)
    0x1e80x181: v1811e8 = MLOAD v1811e6
    0x1e90x181: v1811e9(0x1) = CONST 
    0x1ec0x181: v1811ec(0x20) = CONST 
    0x1ee0x181: v1811ee(0x13) = SUB v1811ec(0x20), v1811dd(0xd)
    0x1ef0x181: v1811ef(0x100) = CONST 
    0x1f20x181: v1811f2(0x100000000000000000000000000000000000000) = EXP v1811ef(0x100), v1811ee(0x13)
    0x1f30x181: v1811f3(0xffffffffffffffffffffffffffffffffffffff) = SUB v1811f2(0x100000000000000000000000000000000000000), v1811e9(0x1)
    0x1f40x181: v1811f4(0xffffffffffffffffffffffffff00000000000000000000000000000000000000) = NOT v1811f3(0xffffffffffffffffffffffffffffffffffffff)
    0x1f50x181: v1811f5 = AND v1811f4(0xffffffffffffffffffffffffff00000000000000000000000000000000000000), v1811e8
    0x1f70x181: MSTORE v1811e6, v1811f5
    0x1f80x181: v1811f8(0x20) = CONST 
    0x1fa0x181: v1811fa = ADD v1811f8(0x20), v1811e6
    0x2dac0x181: v1812dac(0x1fd) = CONST 
    0x2dcc0x181: JUMP v1812dac(0x1fd)

    Begin block 0x1fd0x181
    prev=[0x1e40x181, 0x1d00x181], succ=[]
    =================================
    0x1fd0x181_0x1: v1fd181_1 = PHI v1811fa, v1811d9
    0x2030x181: v181203(0x40) = CONST 
    0x2050x181: v181205 = MLOAD v181203(0x40)
    0x2080x181: v181208 = SUB v1fd181_1, v181205
    0x20a0x181: RETURN v181205, v181208

    Begin block 0x1c10x181
    prev=[0x1b80x181], succ=[0x1b80x181]
    =================================
    0x1c10x181_0x0: v1c1181_0 = PHI v1b00b(0x0), v1811cb
    0x1c30x181: v1811c3 = ADD v1c1181_0, v1b006
    0x1c40x181: v1811c4 = MLOAD v1811c3
    0x1c70x181: v1811c7 = ADD v1c1181_0, v1b003
    0x1c80x181: MSTORE v1811c7, v1811c4
    0x1c90x181: v1811c9(0x20) = CONST 
    0x1cb0x181: v1811cb = ADD v1811c9(0x20), v1c1181_0
    0x1cc0x181: v1811cc(0x1b8) = CONST 
    0x1cf0x181: JUMP v1811cc(0x1b8)

}

function approve(address,uint256)() public {
    Begin block 0x20b
    prev=[], succ=[0x213, 0x217]
    =================================
    0x20c: v20c = CALLVALUE 
    0x20e: v20e = ISZERO v20c
    0x20f: v20f(0x217) = CONST 
    0x212: JUMPI v20f(0x217), v20e

    Begin block 0x213
    prev=[0x20b], succ=[]
    =================================
    0x213: v213(0x0) = CONST 
    0x216: REVERT v213(0x0), v213(0x0)

    Begin block 0x217
    prev=[0x20b], succ=[0x574]
    =================================
    0x219: v219(0x1d241) = CONST 
    0x21c: v21c(0x1) = CONST 
    0x21e: v21e(0xa0) = CONST 
    0x220: v220(0x2) = CONST 
    0x222: v222(0x10000000000000000000000000000000000000000) = EXP v220(0x2), v21e(0xa0)
    0x223: v223(0xffffffffffffffffffffffffffffffffffffffff) = SUB v222(0x10000000000000000000000000000000000000000), v21c(0x1)
    0x224: v224(0x4) = CONST 
    0x226: v226 = CALLDATALOAD v224(0x4)
    0x227: v227 = AND v226, v223(0xffffffffffffffffffffffffffffffffffffffff)
    0x228: v228(0x24) = CONST 
    0x22a: v22a = CALLDATALOAD v228(0x24)
    0x22b: v22b(0x574) = CONST 
    0x22e: JUMP v22b(0x574)

    Begin block 0x574
    prev=[0x217], succ=[0x1d241]
    =================================
    0x575: v575 = CALLER 
    0x576: v576(0x0) = CONST 
    0x57a: MSTORE v576(0x0), v575
    0x57b: v57b(0x2) = CONST 
    0x57d: v57d(0x20) = CONST 
    0x581: MSTORE v57d(0x20), v57b(0x2)
    0x582: v582(0x40) = CONST 
    0x586: v586 = SHA3 v576(0x0), v582(0x40)
    0x587: v587(0x1) = CONST 
    0x589: v589(0xa0) = CONST 
    0x58b: v58b(0x2) = CONST 
    0x58d: v58d(0x10000000000000000000000000000000000000000) = EXP v58b(0x2), v589(0xa0)
    0x58e: v58e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v58d(0x10000000000000000000000000000000000000000), v587(0x1)
    0x590: v590 = AND v227, v58e(0xffffffffffffffffffffffffffffffffffffffff)
    0x593: MSTORE v576(0x0), v590
    0x596: MSTORE v57d(0x20), v586
    0x599: v599 = SHA3 v576(0x0), v582(0x40)
    0x59c: SSTORE v599, v22a
    0x59e: v59e = MLOAD v582(0x40)
    0x5a1: MSTORE v59e, v22a
    0x5a3: v5a3 = MLOAD v582(0x40)
    0x5aa: v5aa(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x5ce: v5ce(0x0) = SUB v59e, v5a3
    0x5cf: v5cf(0x20) = ADD v5ce(0x0), v57d(0x20)
    0x5d1: LOG3 v5a3, v5cf(0x20), v5aa(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v575, v590
    0x5d3: v5d3(0x1) = CONST 
    0x5d9: JUMP v219(0x1d241)

    Begin block 0x1d241
    prev=[0x574], succ=[]
    =================================
    0x1d242: v1d242(0x40) = CONST 
    0x1d245: v1d245 = MLOAD v1d242(0x40)
    0x1d247: v1d247(0x0) = ISZERO v5d3(0x1)
    0x1d248: v1d248(0x1) = ISZERO v1d247(0x0)
    0x1d24a: MSTORE v1d245, v1d248(0x1)
    0x1d24b: v1d24b = MLOAD v1d242(0x40)
    0x1d24f: v1d24f(0x0) = SUB v1d245, v1d24b
    0x1d250: v1d250(0x20) = CONST 
    0x1d252: v1d252(0x20) = ADD v1d250(0x20), v1d24f(0x0)
    0x1d254: RETURN v1d24b, v1d252(0x20)

}

function setSaleAgent(address)() public {
    Begin block 0x22f
    prev=[], succ=[0x237, 0x23b]
    =================================
    0x230: v230 = CALLVALUE 
    0x232: v232 = ISZERO v230
    0x233: v233(0x23b) = CONST 
    0x236: JUMPI v233(0x23b), v232

    Begin block 0x237
    prev=[0x22f], succ=[]
    =================================
    0x237: v237(0x0) = CONST 
    0x23a: REVERT v237(0x0), v237(0x0)

    Begin block 0x23b
    prev=[0x22f], succ=[0x5da]
    =================================
    0x23d: v23d(0x1d274) = CONST 
    0x240: v240(0x1) = CONST 
    0x242: v242(0xa0) = CONST 
    0x244: v244(0x2) = CONST 
    0x246: v246(0x10000000000000000000000000000000000000000) = EXP v244(0x2), v242(0xa0)
    0x247: v247(0xffffffffffffffffffffffffffffffffffffffff) = SUB v246(0x10000000000000000000000000000000000000000), v240(0x1)
    0x248: v248(0x4) = CONST 
    0x24a: v24a = CALLDATALOAD v248(0x4)
    0x24b: v24b = AND v24a, v247(0xffffffffffffffffffffffffffffffffffffffff)
    0x24c: v24c(0x5da) = CONST 
    0x24f: JUMP v24c(0x5da)

    Begin block 0x5da
    prev=[0x23b], succ=[0x5fd, 0x5ee]
    =================================
    0x5db: v5db(0x4) = CONST 
    0x5dd: v5dd = SLOAD v5db(0x4)
    0x5de: v5de(0x1) = CONST 
    0x5e0: v5e0(0xa0) = CONST 
    0x5e2: v5e2(0x2) = CONST 
    0x5e4: v5e4(0x10000000000000000000000000000000000000000) = EXP v5e2(0x2), v5e0(0xa0)
    0x5e5: v5e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5e4(0x10000000000000000000000000000000000000000), v5de(0x1)
    0x5e6: v5e6 = AND v5e5(0xffffffffffffffffffffffffffffffffffffffff), v5dd
    0x5e7: v5e7 = CALLER 
    0x5e8: v5e8 = EQ v5e7, v5e6
    0x5ea: v5ea(0x5fd) = CONST 
    0x5ed: JUMPI v5ea(0x5fd), v5e8

    Begin block 0x5fd
    prev=[0x5da, 0x5ee], succ=[0x604, 0x608]
    =================================
    0x5fd_0x0: v5fd_0 = PHI v5e8, v5fc
    0x5fe: v5fe = ISZERO v5fd_0
    0x5ff: v5ff = ISZERO v5fe
    0x600: v600(0x608) = CONST 
    0x603: JUMPI v600(0x608), v5ff

    Begin block 0x604
    prev=[0x5fd], succ=[]
    =================================
    0x604: v604(0x0) = CONST 
    0x607: REVERT v604(0x0), v604(0x0)

    Begin block 0x608
    prev=[0x5fd], succ=[0x1d274]
    =================================
    0x609: v609(0x4) = CONST 
    0x60c: v60c = SLOAD v609(0x4)
    0x60d: v60d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x622: v622(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v60d(0xffffffffffffffffffffffffffffffffffffffff)
    0x623: v623 = AND v622(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v60c
    0x624: v624(0x1) = CONST 
    0x626: v626(0xa0) = CONST 
    0x628: v628(0x2) = CONST 
    0x62a: v62a(0x10000000000000000000000000000000000000000) = EXP v628(0x2), v626(0xa0)
    0x62b: v62b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v62a(0x10000000000000000000000000000000000000000), v624(0x1)
    0x62f: v62f = AND v62b(0xffffffffffffffffffffffffffffffffffffffff), v24b
    0x633: v633 = OR v62f, v623
    0x635: SSTORE v609(0x4), v633
    0x636: JUMP v23d(0x1d274)

    Begin block 0x1d274
    prev=[0x608], succ=[]
    =================================
    0x1d275: STOP 

    Begin block 0x5ee
    prev=[0x5da], succ=[0x5fd]
    =================================
    0x5ef: v5ef(0x3) = CONST 
    0x5f1: v5f1 = SLOAD v5ef(0x3)
    0x5f2: v5f2(0x1) = CONST 
    0x5f4: v5f4(0xa0) = CONST 
    0x5f6: v5f6(0x2) = CONST 
    0x5f8: v5f8(0x10000000000000000000000000000000000000000) = EXP v5f6(0x2), v5f4(0xa0)
    0x5f9: v5f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5f8(0x10000000000000000000000000000000000000000), v5f2(0x1)
    0x5fa: v5fa = AND v5f9(0xffffffffffffffffffffffffffffffffffffffff), v5f1
    0x5fb: v5fb = CALLER 
    0x5fc: v5fc = EQ v5fb, v5fa
    0x37ac: v37ac(0x5fd) = CONST 
    0x37cc: JUMP v37ac(0x5fd)

}

function totalSupply()() public {
    Begin block 0x252
    prev=[], succ=[0x25a, 0x25e]
    =================================
    0x253: v253 = CALLVALUE 
    0x255: v255 = ISZERO v253
    0x256: v256(0x25e) = CONST 
    0x259: JUMPI v256(0x25e), v255

    Begin block 0x25a
    prev=[0x252], succ=[]
    =================================
    0x25a: v25a(0x0) = CONST 
    0x25d: REVERT v25a(0x0), v25a(0x0)

    Begin block 0x25e
    prev=[0x252], succ=[0x637]
    =================================
    0x260: v260(0x1d295) = CONST 
    0x263: v263(0x637) = CONST 
    0x266: JUMP v263(0x637)

    Begin block 0x637
    prev=[0x25e], succ=[0x1d295]
    =================================
    0x638: v638(0x1) = CONST 
    0x63a: v63a = SLOAD v638(0x1)
    0x63c: JUMP v260(0x1d295)

    Begin block 0x1d295
    prev=[0x637], succ=[]
    =================================
    0x1d296: v1d296(0x40) = CONST 
    0x1d299: v1d299 = MLOAD v1d296(0x40)
    0x1d29c: MSTORE v1d299, v63a
    0x1d29d: v1d29d = MLOAD v1d296(0x40)
    0x1d2a1: v1d2a1(0x0) = SUB v1d299, v1d29d
    0x1d2a2: v1d2a2(0x20) = CONST 
    0x1d2a4: v1d2a4(0x20) = ADD v1d2a2(0x20), v1d2a1(0x0)
    0x1d2a6: RETURN v1d29d, v1d2a4(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x279
    prev=[], succ=[0x281, 0x285]
    =================================
    0x27a: v27a = CALLVALUE 
    0x27c: v27c = ISZERO v27a
    0x27d: v27d(0x285) = CONST 
    0x280: JUMPI v27d(0x285), v27c

    Begin block 0x281
    prev=[0x279], succ=[]
    =================================
    0x281: v281(0x0) = CONST 
    0x284: REVERT v281(0x0), v281(0x0)

    Begin block 0x285
    prev=[0x279], succ=[0x63dB0x285]
    =================================
    0x287: v287(0x1d2c6) = CONST 
    0x28a: v28a(0x1) = CONST 
    0x28c: v28c(0xa0) = CONST 
    0x28e: v28e(0x2) = CONST 
    0x290: v290(0x10000000000000000000000000000000000000000) = EXP v28e(0x2), v28c(0xa0)
    0x291: v291(0xffffffffffffffffffffffffffffffffffffffff) = SUB v290(0x10000000000000000000000000000000000000000), v28a(0x1)
    0x292: v292(0x4) = CONST 
    0x294: v294 = CALLDATALOAD v292(0x4)
    0x296: v296 = AND v291(0xffffffffffffffffffffffffffffffffffffffff), v294
    0x298: v298(0x24) = CONST 
    0x29a: v29a = CALLDATALOAD v298(0x24)
    0x29b: v29b = AND v29a, v291(0xffffffffffffffffffffffffffffffffffffffff)
    0x29c: v29c(0x44) = CONST 
    0x29e: v29e = CALLDATALOAD v29c(0x44)
    0x29f: v29f(0x63d) = CONST 
    0x2a2: JUMP v29f(0x63d)

    Begin block 0x63dB0x285
    prev=[0x285], succ=[0x64dB0x285]
    =================================
    0x63eS0x285: v63eV285(0x0) = CONST 
    0x640S0x285: v640V285(0x1f88d) = CONST 
    0x643S0x285: v643V285(0x64d) = CONST 
    0x649S0x285: v649V285(0xccd) = CONST 
    0x64cS0x285: v64c_0V285 = CALLPRIVATE v649V285(0xccd), v29e, v29b, v296, v643V285(0x64d)

    Begin block 0x64dB0x285
    prev=[0x63dB0x285], succ=[0x1f88dB0x285]
    =================================
    0x651S0x285: v651V285(0xd66) = CONST 
    0x654S0x285: v654_0V285 = CALLPRIVATE v651V285(0xd66), v29e, v29b, v296, v64c_0V285, v640V285(0x1f88d)

    Begin block 0x1f88dB0x285
    prev=[0x64dB0x285], succ=[0x1d2c6]
    =================================
    0x1f894S0x285: JUMP v287(0x1d2c6)

    Begin block 0x1d2c6
    prev=[0x1f88dB0x285], succ=[]
    =================================
    0x1d2c7: v1d2c7(0x40) = CONST 
    0x1d2ca: v1d2ca = MLOAD v1d2c7(0x40)
    0x1d2cc: v1d2cc = ISZERO v654_0V285
    0x1d2cd: v1d2cd = ISZERO v1d2cc
    0x1d2cf: MSTORE v1d2ca, v1d2cd
    0x1d2d0: v1d2d0 = MLOAD v1d2c7(0x40)
    0x1d2d4: v1d2d4(0x0) = SUB v1d2ca, v1d2d0
    0x1d2d5: v1d2d5(0x20) = CONST 
    0x1d2d7: v1d2d7(0x20) = ADD v1d2d5(0x20), v1d2d4(0x0)
    0x1d2d9: RETURN v1d2d0, v1d2d7(0x20)

}

function unlockAddressDuringITO(address)() public {
    Begin block 0x2a3
    prev=[], succ=[0x2ab, 0x2af]
    =================================
    0x2a4: v2a4 = CALLVALUE 
    0x2a6: v2a6 = ISZERO v2a4
    0x2a7: v2a7(0x2af) = CONST 
    0x2aa: JUMPI v2a7(0x2af), v2a6

    Begin block 0x2ab
    prev=[0x2a3], succ=[]
    =================================
    0x2ab: v2ab(0x0) = CONST 
    0x2ae: REVERT v2ab(0x0), v2ab(0x0)

    Begin block 0x2af
    prev=[0x2a3], succ=[0x65d]
    =================================
    0x2b1: v2b1(0x1d2f9) = CONST 
    0x2b4: v2b4(0x1) = CONST 
    0x2b6: v2b6(0xa0) = CONST 
    0x2b8: v2b8(0x2) = CONST 
    0x2ba: v2ba(0x10000000000000000000000000000000000000000) = EXP v2b8(0x2), v2b6(0xa0)
    0x2bb: v2bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ba(0x10000000000000000000000000000000000000000), v2b4(0x1)
    0x2bc: v2bc(0x4) = CONST 
    0x2be: v2be = CALLDATALOAD v2bc(0x4)
    0x2bf: v2bf = AND v2be, v2bb(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c0: v2c0(0x65d) = CONST 
    0x2c3: JUMP v2c0(0x65d)

    Begin block 0x65d
    prev=[0x2af], succ=[0x680, 0x671]
    =================================
    0x65e: v65e(0x4) = CONST 
    0x660: v660 = SLOAD v65e(0x4)
    0x661: v661(0x1) = CONST 
    0x663: v663(0xa0) = CONST 
    0x665: v665(0x2) = CONST 
    0x667: v667(0x10000000000000000000000000000000000000000) = EXP v665(0x2), v663(0xa0)
    0x668: v668(0xffffffffffffffffffffffffffffffffffffffff) = SUB v667(0x10000000000000000000000000000000000000000), v661(0x1)
    0x669: v669 = AND v668(0xffffffffffffffffffffffffffffffffffffffff), v660
    0x66a: v66a = CALLER 
    0x66b: v66b = EQ v66a, v669
    0x66d: v66d(0x680) = CONST 
    0x670: JUMPI v66d(0x680), v66b

    Begin block 0x680
    prev=[0x65d, 0x671], succ=[0x687, 0x68b]
    =================================
    0x680_0x0: v680_0 = PHI v66b, v67f
    0x681: v681 = ISZERO v680_0
    0x682: v682 = ISZERO v681
    0x683: v683(0x68b) = CONST 
    0x686: JUMPI v683(0x68b), v682

    Begin block 0x687
    prev=[0x680], succ=[]
    =================================
    0x687: v687(0x0) = CONST 
    0x68a: REVERT v687(0x0), v687(0x0)

    Begin block 0x68b
    prev=[0x680], succ=[0x1d2f9]
    =================================
    0x68c: v68c(0x1) = CONST 
    0x68e: v68e(0xa0) = CONST 
    0x690: v690(0x2) = CONST 
    0x692: v692(0x10000000000000000000000000000000000000000) = EXP v690(0x2), v68e(0xa0)
    0x693: v693(0xffffffffffffffffffffffffffffffffffffffff) = SUB v692(0x10000000000000000000000000000000000000000), v68c(0x1)
    0x694: v694 = AND v693(0xffffffffffffffffffffffffffffffffffffffff), v2bf
    0x695: v695(0x0) = CONST 
    0x699: MSTORE v695(0x0), v694
    0x69a: v69a(0x5) = CONST 
    0x69c: v69c(0x20) = CONST 
    0x69e: MSTORE v69c(0x20), v69a(0x5)
    0x69f: v69f(0x40) = CONST 
    0x6a2: v6a2 = SHA3 v695(0x0), v69f(0x40)
    0x6a4: v6a4 = SLOAD v6a2
    0x6a5: v6a5(0xff) = CONST 
    0x6a7: v6a7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v6a5(0xff)
    0x6a8: v6a8 = AND v6a7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v6a4
    0x6a9: v6a9(0x1) = CONST 
    0x6ab: v6ab = OR v6a9(0x1), v6a8
    0x6ad: SSTORE v6a2, v6ab
    0x6ae: JUMP v2b1(0x1d2f9)

    Begin block 0x1d2f9
    prev=[0x68b], succ=[]
    =================================
    0x1d2fa: STOP 

    Begin block 0x671
    prev=[0x65d], succ=[0x680]
    =================================
    0x672: v672(0x3) = CONST 
    0x674: v674 = SLOAD v672(0x3)
    0x675: v675(0x1) = CONST 
    0x677: v677(0xa0) = CONST 
    0x679: v679(0x2) = CONST 
    0x67b: v67b(0x10000000000000000000000000000000000000000) = EXP v679(0x2), v677(0xa0)
    0x67c: v67c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v67b(0x10000000000000000000000000000000000000000), v675(0x1)
    0x67d: v67d = AND v67c(0xffffffffffffffffffffffffffffffffffffffff), v674
    0x67e: v67e = CALLER 
    0x67f: v67f = EQ v67e, v67d
    0x41ac: v41ac(0x680) = CONST 
    0x41cc: JUMP v41ac(0x680)

}

function decimals()() public {
    Begin block 0x2c4
    prev=[], succ=[0x2cc, 0x2d0]
    =================================
    0x2c5: v2c5 = CALLVALUE 
    0x2c7: v2c7 = ISZERO v2c5
    0x2c8: v2c8(0x2d0) = CONST 
    0x2cb: JUMPI v2c8(0x2d0), v2c7

    Begin block 0x2cc
    prev=[0x2c4], succ=[]
    =================================
    0x2cc: v2cc(0x0) = CONST 
    0x2cf: REVERT v2cc(0x0), v2cc(0x0)

    Begin block 0x2d0
    prev=[0x2c4], succ=[0x6af]
    =================================
    0x2d2: v2d2(0x2d9) = CONST 
    0x2d5: v2d5(0x6af) = CONST 
    0x2d8: JUMP v2d5(0x6af)

    Begin block 0x6af
    prev=[0x2d0], succ=[0x2d9]
    =================================
    0x6b0: v6b0(0x12) = CONST 
    0x6b3: JUMP v2d2(0x2d9)

    Begin block 0x2d9
    prev=[0x6af], succ=[]
    =================================
    0x2da: v2da(0x40) = CONST 
    0x2dd: v2dd = MLOAD v2da(0x40)
    0x2de: v2de(0xffffffff) = CONST 
    0x2e5: v2e5(0x12) = AND v6b0(0x12), v2de(0xffffffff)
    0x2e7: MSTORE v2dd, v2e5(0x12)
    0x2e8: v2e8 = MLOAD v2da(0x40)
    0x2ec: v2ec(0x0) = SUB v2dd, v2e8
    0x2ed: v2ed(0x20) = CONST 
    0x2ef: v2ef(0x20) = ADD v2ed(0x20), v2ec(0x0)
    0x2f1: RETURN v2e8, v2ef(0x20)

}

function mint(address,uint256)() public {
    Begin block 0x2f2
    prev=[], succ=[0x2fa, 0x2fe]
    =================================
    0x2f3: v2f3 = CALLVALUE 
    0x2f5: v2f5 = ISZERO v2f3
    0x2f6: v2f6(0x2fe) = CONST 
    0x2f9: JUMPI v2f6(0x2fe), v2f5

    Begin block 0x2fa
    prev=[0x2f2], succ=[]
    =================================
    0x2fa: v2fa(0x0) = CONST 
    0x2fd: REVERT v2fa(0x0), v2fa(0x0)

    Begin block 0x2fe
    prev=[0x2f2], succ=[0x6b4]
    =================================
    0x300: v300(0x1d31a) = CONST 
    0x303: v303(0x1) = CONST 
    0x305: v305(0xa0) = CONST 
    0x307: v307(0x2) = CONST 
    0x309: v309(0x10000000000000000000000000000000000000000) = EXP v307(0x2), v305(0xa0)
    0x30a: v30a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v309(0x10000000000000000000000000000000000000000), v303(0x1)
    0x30b: v30b(0x4) = CONST 
    0x30d: v30d = CALLDATALOAD v30b(0x4)
    0x30e: v30e = AND v30d, v30a(0xffffffffffffffffffffffffffffffffffffffff)
    0x30f: v30f(0x24) = CONST 
    0x311: v311 = CALLDATALOAD v30f(0x24)
    0x312: v312(0x6b4) = CONST 
    0x315: JUMP v312(0x6b4)

    Begin block 0x6b4
    prev=[0x2fe], succ=[0x6da, 0x6cb]
    =================================
    0x6b5: v6b5(0x4) = CONST 
    0x6b7: v6b7 = SLOAD v6b5(0x4)
    0x6b8: v6b8(0x0) = CONST 
    0x6bb: v6bb(0x1) = CONST 
    0x6bd: v6bd(0xa0) = CONST 
    0x6bf: v6bf(0x2) = CONST 
    0x6c1: v6c1(0x10000000000000000000000000000000000000000) = EXP v6bf(0x2), v6bd(0xa0)
    0x6c2: v6c2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c1(0x10000000000000000000000000000000000000000), v6bb(0x1)
    0x6c3: v6c3 = AND v6c2(0xffffffffffffffffffffffffffffffffffffffff), v6b7
    0x6c4: v6c4 = CALLER 
    0x6c5: v6c5 = EQ v6c4, v6c3
    0x6c7: v6c7(0x6da) = CONST 
    0x6ca: JUMPI v6c7(0x6da), v6c5

    Begin block 0x6da
    prev=[0x6b4, 0x6cb], succ=[0x6f0, 0x6e1]
    =================================
    0x6da_0x0: v6da_0 = PHI v6c5, v6d9
    0x6dc: v6dc = ISZERO v6da_0
    0x6dd: v6dd(0x6f0) = CONST 
    0x6e0: JUMPI v6dd(0x6f0), v6dc

    Begin block 0x6f0
    prev=[0x6da, 0x6e1], succ=[0x6f7, 0x6fb]
    =================================
    0x6f0_0x0: v6f0_0 = PHI v6c5, v6d9, v6ef
    0x6f1: v6f1 = ISZERO v6f0_0
    0x6f2: v6f2 = ISZERO v6f1
    0x6f3: v6f3(0x6fb) = CONST 
    0x6f6: JUMPI v6f3(0x6fb), v6f2

    Begin block 0x6f7
    prev=[0x6f0], succ=[]
    =================================
    0x6f7: v6f7(0x0) = CONST 
    0x6fa: REVERT v6f7(0x0), v6f7(0x0)

    Begin block 0x6fb
    prev=[0x6f0], succ=[0x71b, 0x773]
    =================================
    0x6fc: v6fc(0x1) = CONST 
    0x6fe: v6fe(0xa0) = CONST 
    0x700: v700(0x2) = CONST 
    0x702: v702(0x10000000000000000000000000000000000000000) = EXP v700(0x2), v6fe(0xa0)
    0x703: v703(0xffffffffffffffffffffffffffffffffffffffff) = SUB v702(0x10000000000000000000000000000000000000000), v6fc(0x1)
    0x705: v705 = AND v30e, v703(0xffffffffffffffffffffffffffffffffffffffff)
    0x706: v706(0x0) = CONST 
    0x70a: MSTORE v706(0x0), v705
    0x70b: v70b(0x20) = CONST 
    0x70f: MSTORE v70b(0x20), v706(0x0)
    0x710: v710(0x40) = CONST 
    0x713: v713 = SHA3 v706(0x0), v710(0x40)
    0x714: v714 = SLOAD v713
    0x715: v715 = ISZERO v714
    0x716: v716 = ISZERO v715
    0x717: v717(0x773) = CONST 
    0x71a: JUMPI v717(0x773), v716

    Begin block 0x71b
    prev=[0x6fb], succ=[0x773]
    =================================
    0x71b: v71b(0x6) = CONST 
    0x71e: v71e = SLOAD v71b(0x6)
    0x71f: v71f(0x1) = CONST 
    0x722: v722 = ADD v71e, v71f(0x1)
    0x724: SSTORE v71b(0x6), v722
    0x725: v725(0x0) = CONST 
    0x72a: MSTORE v725(0x0), v71b(0x6)
    0x72b: v72b(0xf652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f) = CONST 
    0x74c: v74c = ADD v72b(0xf652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f), v71e
    0x74e: v74e = SLOAD v74c
    0x74f: v74f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x764: v764(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v74f(0xffffffffffffffffffffffffffffffffffffffff)
    0x765: v765 = AND v764(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v74e
    0x766: v766(0x1) = CONST 
    0x768: v768(0xa0) = CONST 
    0x76a: v76a(0x2) = CONST 
    0x76c: v76c(0x10000000000000000000000000000000000000000) = EXP v76a(0x2), v768(0xa0)
    0x76d: v76d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v76c(0x10000000000000000000000000000000000000000), v766(0x1)
    0x76f: v76f = AND v30e, v76d(0xffffffffffffffffffffffffffffffffffffffff)
    0x770: v770 = OR v76f, v765
    0x772: SSTORE v74c, v770
    0x5fac: v5fac(0x773) = CONST 
    0x5fcc: JUMP v5fac(0x773)

    Begin block 0x773
    prev=[0x71b, 0x6fb], succ=[0x786]
    =================================
    0x774: v774(0x1) = CONST 
    0x776: v776 = SLOAD v774(0x1)
    0x777: v777(0x786) = CONST 
    0x77c: v77c(0xffffffff) = CONST 
    0x781: v781(0xe22) = CONST 
    0x784: v784(0xe22) = AND v781(0xe22), v77c(0xffffffff)
    0x785: v785_0 = CALLPRIVATE v784(0xe22), v311, v776, v777(0x786)

    Begin block 0x786
    prev=[0x773], succ=[0x7b2]
    =================================
    0x787: v787(0x1) = CONST 
    0x789: SSTORE v787(0x1), v785_0
    0x78a: v78a(0x1) = CONST 
    0x78c: v78c(0xa0) = CONST 
    0x78e: v78e(0x2) = CONST 
    0x790: v790(0x10000000000000000000000000000000000000000) = EXP v78e(0x2), v78c(0xa0)
    0x791: v791(0xffffffffffffffffffffffffffffffffffffffff) = SUB v790(0x10000000000000000000000000000000000000000), v78a(0x1)
    0x793: v793 = AND v30e, v791(0xffffffffffffffffffffffffffffffffffffffff)
    0x794: v794(0x0) = CONST 
    0x798: MSTORE v794(0x0), v793
    0x799: v799(0x20) = CONST 
    0x79d: MSTORE v799(0x20), v794(0x0)
    0x79e: v79e(0x40) = CONST 
    0x7a1: v7a1 = SHA3 v794(0x0), v79e(0x40)
    0x7a2: v7a2 = SLOAD v7a1
    0x7a3: v7a3(0x7b2) = CONST 
    0x7a8: v7a8(0xffffffff) = CONST 
    0x7ad: v7ad(0xe22) = CONST 
    0x7b0: v7b0(0xe22) = AND v7ad(0xe22), v7a8(0xffffffff)
    0x7b1: v7b1_0 = CALLPRIVATE v7b0(0xe22), v311, v7a2, v7a3(0x7b2)

    Begin block 0x7b2
    prev=[0x786], succ=[0x1d31a]
    =================================
    0x7b3: v7b3(0x1) = CONST 
    0x7b5: v7b5(0xa0) = CONST 
    0x7b7: v7b7(0x2) = CONST 
    0x7b9: v7b9(0x10000000000000000000000000000000000000000) = EXP v7b7(0x2), v7b5(0xa0)
    0x7ba: v7ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b9(0x10000000000000000000000000000000000000000), v7b3(0x1)
    0x7bc: v7bc = AND v30e, v7ba(0xffffffffffffffffffffffffffffffffffffffff)
    0x7bd: v7bd(0x0) = CONST 
    0x7c1: MSTORE v7bd(0x0), v7bc
    0x7c2: v7c2(0x20) = CONST 
    0x7c6: MSTORE v7c2(0x20), v7bd(0x0)
    0x7c7: v7c7(0x40) = CONST 
    0x7cc: v7cc = SHA3 v7bd(0x0), v7c7(0x40)
    0x7d0: SSTORE v7cc, v7b1_0
    0x7d2: v7d2 = MLOAD v7c7(0x40)
    0x7d5: MSTORE v7d2, v311
    0x7d7: v7d7 = MLOAD v7c7(0x40)
    0x7da: v7da(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0x7ff: v7ff(0x0) = SUB v7d2, v7d7
    0x800: v800(0x20) = ADD v7ff(0x0), v7c2(0x20)
    0x802: LOG2 v7d7, v800(0x20), v7da(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), v7bc
    0x803: v803(0x40) = CONST 
    0x806: v806 = MLOAD v803(0x40)
    0x809: MSTORE v806, v311
    0x80b: v80b = MLOAD v803(0x40)
    0x80c: v80c(0x1) = CONST 
    0x80e: v80e(0xa0) = CONST 
    0x810: v810(0x2) = CONST 
    0x812: v812(0x10000000000000000000000000000000000000000) = EXP v810(0x2), v80e(0xa0)
    0x813: v813(0xffffffffffffffffffffffffffffffffffffffff) = SUB v812(0x10000000000000000000000000000000000000000), v80c(0x1)
    0x815: v815 = AND v30e, v813(0xffffffffffffffffffffffffffffffffffffffff)
    0x817: v817(0x0) = CONST 
    0x81a: v81a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x83e: v83e(0x0) = SUB v806, v80b
    0x83f: v83f(0x20) = CONST 
    0x841: v841(0x20) = ADD v83f(0x20), v83e(0x0)
    0x843: LOG3 v80b, v841(0x20), v81a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v817(0x0), v815
    0x845: v845(0x1) = CONST 
    0x84b: JUMP v300(0x1d31a)

    Begin block 0x1d31a
    prev=[0x7b2], succ=[]
    =================================
    0x1d31b: v1d31b(0x40) = CONST 
    0x1d31e: v1d31e = MLOAD v1d31b(0x40)
    0x1d320: v1d320(0x0) = ISZERO v845(0x1)
    0x1d321: v1d321(0x1) = ISZERO v1d320(0x0)
    0x1d323: MSTORE v1d31e, v1d321(0x1)
    0x1d324: v1d324 = MLOAD v1d31b(0x40)
    0x1d328: v1d328(0x0) = SUB v1d31e, v1d324
    0x1d329: v1d329(0x20) = CONST 
    0x1d32b: v1d32b(0x20) = ADD v1d329(0x20), v1d328(0x0)
    0x1d32d: RETURN v1d324, v1d32b(0x20)

    Begin block 0x6e1
    prev=[0x6da], succ=[0x6f0]
    =================================
    0x6e2: v6e2(0x3) = CONST 
    0x6e4: v6e4 = SLOAD v6e2(0x3)
    0x6e5: v6e5(0xa0) = CONST 
    0x6e7: v6e7(0x2) = CONST 
    0x6e9: v6e9(0x10000000000000000000000000000000000000000) = EXP v6e7(0x2), v6e5(0xa0)
    0x6eb: v6eb = DIV v6e4, v6e9(0x10000000000000000000000000000000000000000)
    0x6ec: v6ec(0xff) = CONST 
    0x6ee: v6ee = AND v6ec(0xff), v6eb
    0x6ef: v6ef = ISZERO v6ee
    0x55ac: v55ac(0x6f0) = CONST 
    0x55cc: JUMP v55ac(0x6f0)

    Begin block 0x6cb
    prev=[0x6b4], succ=[0x6da]
    =================================
    0x6cc: v6cc(0x3) = CONST 
    0x6ce: v6ce = SLOAD v6cc(0x3)
    0x6cf: v6cf(0x1) = CONST 
    0x6d1: v6d1(0xa0) = CONST 
    0x6d3: v6d3(0x2) = CONST 
    0x6d5: v6d5(0x10000000000000000000000000000000000000000) = EXP v6d3(0x2), v6d1(0xa0)
    0x6d6: v6d6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6d5(0x10000000000000000000000000000000000000000), v6cf(0x1)
    0x6d7: v6d7 = AND v6d6(0xffffffffffffffffffffffffffffffffffffffff), v6ce
    0x6d8: v6d8 = CALLER 
    0x6d9: v6d9 = EQ v6d8, v6d7
    0x4bac: v4bac(0x6da) = CONST 
    0x4bcc: JUMP v4bac(0x6da)

}

function deregisterCallback(address)() public {
    Begin block 0x316
    prev=[], succ=[0x31e, 0x322]
    =================================
    0x317: v317 = CALLVALUE 
    0x319: v319 = ISZERO v317
    0x31a: v31a(0x322) = CONST 
    0x31d: JUMPI v31a(0x322), v319

    Begin block 0x31e
    prev=[0x316], succ=[]
    =================================
    0x31e: v31e(0x0) = CONST 
    0x321: REVERT v31e(0x0), v31e(0x0)

    Begin block 0x322
    prev=[0x316], succ=[0x84c]
    =================================
    0x324: v324(0x1d34d) = CONST 
    0x327: v327(0x1) = CONST 
    0x329: v329(0xa0) = CONST 
    0x32b: v32b(0x2) = CONST 
    0x32d: v32d(0x10000000000000000000000000000000000000000) = EXP v32b(0x2), v329(0xa0)
    0x32e: v32e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32d(0x10000000000000000000000000000000000000000), v327(0x1)
    0x32f: v32f(0x4) = CONST 
    0x331: v331 = CALLDATALOAD v32f(0x4)
    0x332: v332 = AND v331, v32e(0xffffffffffffffffffffffffffffffffffffffff)
    0x333: v333(0x84c) = CONST 
    0x336: JUMP v333(0x84c)

    Begin block 0x84c
    prev=[0x322], succ=[0x85f, 0x863]
    =================================
    0x84d: v84d(0x3) = CONST 
    0x84f: v84f = SLOAD v84d(0x3)
    0x850: v850(0x1) = CONST 
    0x852: v852(0xa0) = CONST 
    0x854: v854(0x2) = CONST 
    0x856: v856(0x10000000000000000000000000000000000000000) = EXP v854(0x2), v852(0xa0)
    0x857: v857(0xffffffffffffffffffffffffffffffffffffffff) = SUB v856(0x10000000000000000000000000000000000000000), v850(0x1)
    0x858: v858 = AND v857(0xffffffffffffffffffffffffffffffffffffffff), v84f
    0x859: v859 = CALLER 
    0x85a: v85a = EQ v859, v858
    0x85b: v85b(0x863) = CONST 
    0x85e: JUMPI v85b(0x863), v85a

    Begin block 0x85f
    prev=[0x84c], succ=[]
    =================================
    0x85f: v85f(0x0) = CONST 
    0x862: REVERT v85f(0x0), v85f(0x0)

    Begin block 0x863
    prev=[0x84c], succ=[0x1d34d]
    =================================
    0x864: v864(0x1) = CONST 
    0x866: v866(0xa0) = CONST 
    0x868: v868(0x2) = CONST 
    0x86a: v86a(0x10000000000000000000000000000000000000000) = EXP v868(0x2), v866(0xa0)
    0x86b: v86b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86a(0x10000000000000000000000000000000000000000), v864(0x1)
    0x86c: v86c = AND v86b(0xffffffffffffffffffffffffffffffffffffffff), v332
    0x86d: v86d(0x0) = CONST 
    0x871: MSTORE v86d(0x0), v86c
    0x872: v872(0x7) = CONST 
    0x874: v874(0x20) = CONST 
    0x876: MSTORE v874(0x20), v872(0x7)
    0x877: v877(0x40) = CONST 
    0x87a: v87a = SHA3 v86d(0x0), v877(0x40)
    0x87c: v87c = SLOAD v87a
    0x87d: v87d(0xff) = CONST 
    0x87f: v87f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v87d(0xff)
    0x880: v880 = AND v87f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v87c
    0x882: SSTORE v87a, v880
    0x883: JUMP v324(0x1d34d)

    Begin block 0x1d34d
    prev=[0x863], succ=[]
    =================================
    0x1d34e: STOP 

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x337
    prev=[], succ=[0x33f, 0x343]
    =================================
    0x338: v338 = CALLVALUE 
    0x33a: v33a = ISZERO v338
    0x33b: v33b(0x343) = CONST 
    0x33e: JUMPI v33b(0x343), v33a

    Begin block 0x33f
    prev=[0x337], succ=[]
    =================================
    0x33f: v33f(0x0) = CONST 
    0x342: REVERT v33f(0x0), v33f(0x0)

    Begin block 0x343
    prev=[0x337], succ=[0x884]
    =================================
    0x345: v345(0x1d36e) = CONST 
    0x348: v348(0x1) = CONST 
    0x34a: v34a(0xa0) = CONST 
    0x34c: v34c(0x2) = CONST 
    0x34e: v34e(0x10000000000000000000000000000000000000000) = EXP v34c(0x2), v34a(0xa0)
    0x34f: v34f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v34e(0x10000000000000000000000000000000000000000), v348(0x1)
    0x350: v350(0x4) = CONST 
    0x352: v352 = CALLDATALOAD v350(0x4)
    0x353: v353 = AND v352, v34f(0xffffffffffffffffffffffffffffffffffffffff)
    0x354: v354(0x24) = CONST 
    0x356: v356 = CALLDATALOAD v354(0x24)
    0x357: v357(0x884) = CONST 
    0x35a: JUMP v357(0x884)

    Begin block 0x884
    prev=[0x343], succ=[0x8b1, 0x8d9]
    =================================
    0x885: v885 = CALLER 
    0x886: v886(0x0) = CONST 
    0x88a: MSTORE v886(0x0), v885
    0x88b: v88b(0x2) = CONST 
    0x88d: v88d(0x20) = CONST 
    0x891: MSTORE v88d(0x20), v88b(0x2)
    0x892: v892(0x40) = CONST 
    0x896: v896 = SHA3 v886(0x0), v892(0x40)
    0x897: v897(0x1) = CONST 
    0x899: v899(0xa0) = CONST 
    0x89b: v89b(0x2) = CONST 
    0x89d: v89d(0x10000000000000000000000000000000000000000) = EXP v89b(0x2), v899(0xa0)
    0x89e: v89e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v89d(0x10000000000000000000000000000000000000000), v897(0x1)
    0x8a0: v8a0 = AND v353, v89e(0xffffffffffffffffffffffffffffffffffffffff)
    0x8a2: MSTORE v886(0x0), v8a0
    0x8a5: MSTORE v88d(0x20), v896
    0x8a7: v8a7 = SHA3 v886(0x0), v892(0x40)
    0x8a8: v8a8 = SLOAD v8a7
    0x8ab: v8ab = GT v356, v8a8
    0x8ac: v8ac = ISZERO v8ab
    0x8ad: v8ad(0x8d9) = CONST 
    0x8b0: JUMPI v8ad(0x8d9), v8ac

    Begin block 0x8b1
    prev=[0x884], succ=[0x90e]
    =================================
    0x8b1: v8b1 = CALLER 
    0x8b2: v8b2(0x0) = CONST 
    0x8b6: MSTORE v8b2(0x0), v8b1
    0x8b7: v8b7(0x2) = CONST 
    0x8b9: v8b9(0x20) = CONST 
    0x8bd: MSTORE v8b9(0x20), v8b7(0x2)
    0x8be: v8be(0x40) = CONST 
    0x8c2: v8c2 = SHA3 v8b2(0x0), v8be(0x40)
    0x8c3: v8c3(0x1) = CONST 
    0x8c5: v8c5(0xa0) = CONST 
    0x8c7: v8c7(0x2) = CONST 
    0x8c9: v8c9(0x10000000000000000000000000000000000000000) = EXP v8c7(0x2), v8c5(0xa0)
    0x8ca: v8ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8c9(0x10000000000000000000000000000000000000000), v8c3(0x1)
    0x8cc: v8cc = AND v353, v8ca(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ce: MSTORE v8b2(0x0), v8cc
    0x8d1: MSTORE v8b9(0x20), v8c2
    0x8d3: v8d3 = SHA3 v8b2(0x0), v8be(0x40)
    0x8d4: SSTORE v8d3, v8b2(0x0)
    0x8d5: v8d5(0x90e) = CONST 
    0x8d8: JUMP v8d5(0x90e)

    Begin block 0x90e
    prev=[0x8b1, 0x8e9], succ=[0x1d36e]
    =================================
    0x90f: v90f = CALLER 
    0x910: v910(0x0) = CONST 
    0x914: MSTORE v910(0x0), v90f
    0x915: v915(0x2) = CONST 
    0x917: v917(0x20) = CONST 
    0x91b: MSTORE v917(0x20), v915(0x2)
    0x91c: v91c(0x40) = CONST 
    0x920: v920 = SHA3 v910(0x0), v91c(0x40)
    0x921: v921(0x1) = CONST 
    0x923: v923(0xa0) = CONST 
    0x925: v925(0x2) = CONST 
    0x927: v927(0x10000000000000000000000000000000000000000) = EXP v925(0x2), v923(0xa0)
    0x928: v928(0xffffffffffffffffffffffffffffffffffffffff) = SUB v927(0x10000000000000000000000000000000000000000), v921(0x1)
    0x92a: v92a = AND v353, v928(0xffffffffffffffffffffffffffffffffffffffff)
    0x92d: MSTORE v910(0x0), v92a
    0x930: MSTORE v917(0x20), v920
    0x934: v934 = SHA3 v910(0x0), v91c(0x40)
    0x935: v935 = SLOAD v934
    0x937: v937 = MLOAD v91c(0x40)
    0x93a: MSTORE v937, v935
    0x93c: v93c = MLOAD v91c(0x40)
    0x940: v940(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x965: v965(0x0) = SUB v937, v93c
    0x968: v968(0x20) = ADD v917(0x20), v965(0x0)
    0x96a: LOG3 v93c, v968(0x20), v940(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v90f, v92a
    0x96c: v96c(0x1) = CONST 
    0x973: JUMP v345(0x1d36e)

    Begin block 0x1d36e
    prev=[0x90e], succ=[]
    =================================
    0x1d36f: v1d36f(0x40) = CONST 
    0x1d372: v1d372 = MLOAD v1d36f(0x40)
    0x1d374: v1d374(0x0) = ISZERO v96c(0x1)
    0x1d375: v1d375(0x1) = ISZERO v1d374(0x0)
    0x1d377: MSTORE v1d372, v1d375(0x1)
    0x1d378: v1d378 = MLOAD v1d36f(0x40)
    0x1d37c: v1d37c(0x0) = SUB v1d372, v1d378
    0x1d37d: v1d37d(0x20) = CONST 
    0x1d37f: v1d37f(0x20) = ADD v1d37d(0x20), v1d37c(0x0)
    0x1d381: RETURN v1d378, v1d37f(0x20)

    Begin block 0x8d9
    prev=[0x884], succ=[0x8e9]
    =================================
    0x8da: v8da(0x8e9) = CONST 
    0x8df: v8df(0xffffffff) = CONST 
    0x8e4: v8e4(0xe35) = CONST 
    0x8e7: v8e7(0xe35) = AND v8e4(0xe35), v8df(0xffffffff)
    0x8e8: v8e8_0 = CALLPRIVATE v8e7(0xe35), v356, v8a8, v8da(0x8e9)

    Begin block 0x8e9
    prev=[0x8d9], succ=[0x90e]
    =================================
    0x8ea: v8ea = CALLER 
    0x8eb: v8eb(0x0) = CONST 
    0x8ef: MSTORE v8eb(0x0), v8ea
    0x8f0: v8f0(0x2) = CONST 
    0x8f2: v8f2(0x20) = CONST 
    0x8f6: MSTORE v8f2(0x20), v8f0(0x2)
    0x8f7: v8f7(0x40) = CONST 
    0x8fb: v8fb = SHA3 v8eb(0x0), v8f7(0x40)
    0x8fc: v8fc(0x1) = CONST 
    0x8fe: v8fe(0xa0) = CONST 
    0x900: v900(0x2) = CONST 
    0x902: v902(0x10000000000000000000000000000000000000000) = EXP v900(0x2), v8fe(0xa0)
    0x903: v903(0xffffffffffffffffffffffffffffffffffffffff) = SUB v902(0x10000000000000000000000000000000000000000), v8fc(0x1)
    0x905: v905 = AND v353, v903(0xffffffffffffffffffffffffffffffffffffffff)
    0x907: MSTORE v8eb(0x0), v905
    0x90a: MSTORE v8f2(0x20), v8fb
    0x90c: v90c = SHA3 v8eb(0x0), v8f7(0x40)
    0x90d: SSTORE v90c, v8e8_0
    0x69ac: v69ac(0x90e) = CONST 
    0x69cc: JUMP v69ac(0x90e)

}

function balanceOf(address)() public {
    Begin block 0x35b
    prev=[], succ=[0x363, 0x367]
    =================================
    0x35c: v35c = CALLVALUE 
    0x35e: v35e = ISZERO v35c
    0x35f: v35f(0x367) = CONST 
    0x362: JUMPI v35f(0x367), v35e

    Begin block 0x363
    prev=[0x35b], succ=[]
    =================================
    0x363: v363(0x0) = CONST 
    0x366: REVERT v363(0x0), v363(0x0)

    Begin block 0x367
    prev=[0x35b], succ=[0x974]
    =================================
    0x369: v369(0x1d3a1) = CONST 
    0x36c: v36c(0x1) = CONST 
    0x36e: v36e(0xa0) = CONST 
    0x370: v370(0x2) = CONST 
    0x372: v372(0x10000000000000000000000000000000000000000) = EXP v370(0x2), v36e(0xa0)
    0x373: v373(0xffffffffffffffffffffffffffffffffffffffff) = SUB v372(0x10000000000000000000000000000000000000000), v36c(0x1)
    0x374: v374(0x4) = CONST 
    0x376: v376 = CALLDATALOAD v374(0x4)
    0x377: v377 = AND v376, v373(0xffffffffffffffffffffffffffffffffffffffff)
    0x378: v378(0x974) = CONST 
    0x37b: JUMP v378(0x974)

    Begin block 0x974
    prev=[0x367], succ=[0x1d3a1]
    =================================
    0x975: v975(0x1) = CONST 
    0x977: v977(0xa0) = CONST 
    0x979: v979(0x2) = CONST 
    0x97b: v97b(0x10000000000000000000000000000000000000000) = EXP v979(0x2), v977(0xa0)
    0x97c: v97c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97b(0x10000000000000000000000000000000000000000), v975(0x1)
    0x97d: v97d = AND v97c(0xffffffffffffffffffffffffffffffffffffffff), v377
    0x97e: v97e(0x0) = CONST 
    0x982: MSTORE v97e(0x0), v97d
    0x983: v983(0x20) = CONST 
    0x987: MSTORE v983(0x20), v97e(0x0)
    0x988: v988(0x40) = CONST 
    0x98b: v98b = SHA3 v97e(0x0), v988(0x40)
    0x98c: v98c = SLOAD v98b
    0x98e: JUMP v369(0x1d3a1)

    Begin block 0x1d3a1
    prev=[0x974], succ=[]
    =================================
    0x1d3a2: v1d3a2(0x40) = CONST 
    0x1d3a5: v1d3a5 = MLOAD v1d3a2(0x40)
    0x1d3a8: MSTORE v1d3a5, v98c
    0x1d3a9: v1d3a9 = MLOAD v1d3a2(0x40)
    0x1d3ad: v1d3ad(0x0) = SUB v1d3a5, v1d3a9
    0x1d3ae: v1d3ae(0x20) = CONST 
    0x1d3b0: v1d3b0(0x20) = ADD v1d3ae(0x20), v1d3ad(0x0)
    0x1d3b2: RETURN v1d3a9, v1d3b0(0x20)

}

function renounceOwnership()() public {
    Begin block 0x37c
    prev=[], succ=[0x384, 0x388]
    =================================
    0x37d: v37d = CALLVALUE 
    0x37f: v37f = ISZERO v37d
    0x380: v380(0x388) = CONST 
    0x383: JUMPI v380(0x388), v37f

    Begin block 0x384
    prev=[0x37c], succ=[]
    =================================
    0x384: v384(0x0) = CONST 
    0x387: REVERT v384(0x0), v384(0x0)

    Begin block 0x388
    prev=[0x37c], succ=[0x98f]
    =================================
    0x38a: v38a(0x1d3d2) = CONST 
    0x38d: v38d(0x98f) = CONST 
    0x390: JUMP v38d(0x98f)

    Begin block 0x98f
    prev=[0x388], succ=[0x9a2, 0x9a6]
    =================================
    0x990: v990(0x3) = CONST 
    0x992: v992 = SLOAD v990(0x3)
    0x993: v993(0x1) = CONST 
    0x995: v995(0xa0) = CONST 
    0x997: v997(0x2) = CONST 
    0x999: v999(0x10000000000000000000000000000000000000000) = EXP v997(0x2), v995(0xa0)
    0x99a: v99a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v999(0x10000000000000000000000000000000000000000), v993(0x1)
    0x99b: v99b = AND v99a(0xffffffffffffffffffffffffffffffffffffffff), v992
    0x99c: v99c = CALLER 
    0x99d: v99d = EQ v99c, v99b
    0x99e: v99e(0x9a6) = CONST 
    0x9a1: JUMPI v99e(0x9a6), v99d

    Begin block 0x9a2
    prev=[0x98f], succ=[]
    =================================
    0x9a2: v9a2(0x0) = CONST 
    0x9a5: REVERT v9a2(0x0), v9a2(0x0)

    Begin block 0x9a6
    prev=[0x98f], succ=[0x1d3d2]
    =================================
    0x9a7: v9a7(0x3) = CONST 
    0x9a9: v9a9 = SLOAD v9a7(0x3)
    0x9aa: v9aa(0x40) = CONST 
    0x9ac: v9ac = MLOAD v9aa(0x40)
    0x9ad: v9ad(0x1) = CONST 
    0x9af: v9af(0xa0) = CONST 
    0x9b1: v9b1(0x2) = CONST 
    0x9b3: v9b3(0x10000000000000000000000000000000000000000) = EXP v9b1(0x2), v9af(0xa0)
    0x9b4: v9b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9b3(0x10000000000000000000000000000000000000000), v9ad(0x1)
    0x9b7: v9b7 = AND v9a9, v9b4(0xffffffffffffffffffffffffffffffffffffffff)
    0x9b9: v9b9(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820) = CONST 
    0x9db: v9db(0x0) = CONST 
    0x9de: LOG2 v9ac, v9db(0x0), v9b9(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820), v9b7
    0x9df: v9df(0x3) = CONST 
    0x9e2: v9e2 = SLOAD v9df(0x3)
    0x9e3: v9e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9f8: v9f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v9e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x9f9: v9f9 = AND v9f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v9e2
    0x9fb: SSTORE v9df(0x3), v9f9
    0x9fc: JUMP v38a(0x1d3d2)

    Begin block 0x1d3d2
    prev=[0x9a6], succ=[]
    =================================
    0x1d3d3: STOP 

}

function lockAddressDuringITO(address)() public {
    Begin block 0x391
    prev=[], succ=[0x399, 0x39d]
    =================================
    0x392: v392 = CALLVALUE 
    0x394: v394 = ISZERO v392
    0x395: v395(0x39d) = CONST 
    0x398: JUMPI v395(0x39d), v394

    Begin block 0x399
    prev=[0x391], succ=[]
    =================================
    0x399: v399(0x0) = CONST 
    0x39c: REVERT v399(0x0), v399(0x0)

    Begin block 0x39d
    prev=[0x391], succ=[0x9fd]
    =================================
    0x39f: v39f(0x1d3f3) = CONST 
    0x3a2: v3a2(0x1) = CONST 
    0x3a4: v3a4(0xa0) = CONST 
    0x3a6: v3a6(0x2) = CONST 
    0x3a8: v3a8(0x10000000000000000000000000000000000000000) = EXP v3a6(0x2), v3a4(0xa0)
    0x3a9: v3a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a8(0x10000000000000000000000000000000000000000), v3a2(0x1)
    0x3aa: v3aa(0x4) = CONST 
    0x3ac: v3ac = CALLDATALOAD v3aa(0x4)
    0x3ad: v3ad = AND v3ac, v3a9(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ae: v3ae(0x9fd) = CONST 
    0x3b1: JUMP v3ae(0x9fd)

    Begin block 0x9fd
    prev=[0x39d], succ=[0xa20, 0xa11]
    =================================
    0x9fe: v9fe(0x4) = CONST 
    0xa00: va00 = SLOAD v9fe(0x4)
    0xa01: va01(0x1) = CONST 
    0xa03: va03(0xa0) = CONST 
    0xa05: va05(0x2) = CONST 
    0xa07: va07(0x10000000000000000000000000000000000000000) = EXP va05(0x2), va03(0xa0)
    0xa08: va08(0xffffffffffffffffffffffffffffffffffffffff) = SUB va07(0x10000000000000000000000000000000000000000), va01(0x1)
    0xa09: va09 = AND va08(0xffffffffffffffffffffffffffffffffffffffff), va00
    0xa0a: va0a = CALLER 
    0xa0b: va0b = EQ va0a, va09
    0xa0d: va0d(0xa20) = CONST 
    0xa10: JUMPI va0d(0xa20), va0b

    Begin block 0xa20
    prev=[0x9fd, 0xa11], succ=[0xa27, 0xa2b]
    =================================
    0xa20_0x0: va20_0 = PHI va0b, va1f
    0xa21: va21 = ISZERO va20_0
    0xa22: va22 = ISZERO va21
    0xa23: va23(0xa2b) = CONST 
    0xa26: JUMPI va23(0xa2b), va22

    Begin block 0xa27
    prev=[0xa20], succ=[]
    =================================
    0xa27: va27(0x0) = CONST 
    0xa2a: REVERT va27(0x0), va27(0x0)

    Begin block 0xa2b
    prev=[0xa20], succ=[0x1d3f3]
    =================================
    0xa2c: va2c(0x1) = CONST 
    0xa2e: va2e(0xa0) = CONST 
    0xa30: va30(0x2) = CONST 
    0xa32: va32(0x10000000000000000000000000000000000000000) = EXP va30(0x2), va2e(0xa0)
    0xa33: va33(0xffffffffffffffffffffffffffffffffffffffff) = SUB va32(0x10000000000000000000000000000000000000000), va2c(0x1)
    0xa34: va34 = AND va33(0xffffffffffffffffffffffffffffffffffffffff), v3ad
    0xa35: va35(0x0) = CONST 
    0xa39: MSTORE va35(0x0), va34
    0xa3a: va3a(0x5) = CONST 
    0xa3c: va3c(0x20) = CONST 
    0xa3e: MSTORE va3c(0x20), va3a(0x5)
    0xa3f: va3f(0x40) = CONST 
    0xa42: va42 = SHA3 va35(0x0), va3f(0x40)
    0xa44: va44 = SLOAD va42
    0xa45: va45(0xff) = CONST 
    0xa47: va47(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT va45(0xff)
    0xa48: va48 = AND va47(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), va44
    0xa4a: SSTORE va42, va48
    0xa4b: JUMP v39f(0x1d3f3)

    Begin block 0x1d3f3
    prev=[0xa2b], succ=[]
    =================================
    0x1d3f4: STOP 

    Begin block 0xa11
    prev=[0x9fd], succ=[0xa20]
    =================================
    0xa12: va12(0x3) = CONST 
    0xa14: va14 = SLOAD va12(0x3)
    0xa15: va15(0x1) = CONST 
    0xa17: va17(0xa0) = CONST 
    0xa19: va19(0x2) = CONST 
    0xa1b: va1b(0x10000000000000000000000000000000000000000) = EXP va19(0x2), va17(0xa0)
    0xa1c: va1c(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1b(0x10000000000000000000000000000000000000000), va15(0x1)
    0xa1d: va1d = AND va1c(0xffffffffffffffffffffffffffffffffffffffff), va14
    0xa1e: va1e = CALLER 
    0xa1f: va1f = EQ va1e, va1d
    0x73ac: v73ac(0xa20) = CONST 
    0x73cc: JUMP v73ac(0xa20)

}

function finishMinting()() public {
    Begin block 0x3b2
    prev=[], succ=[0x3ba, 0x3be]
    =================================
    0x3b3: v3b3 = CALLVALUE 
    0x3b5: v3b5 = ISZERO v3b3
    0x3b6: v3b6(0x3be) = CONST 
    0x3b9: JUMPI v3b6(0x3be), v3b5

    Begin block 0x3ba
    prev=[0x3b2], succ=[]
    =================================
    0x3ba: v3ba(0x0) = CONST 
    0x3bd: REVERT v3ba(0x0), v3ba(0x0)

    Begin block 0x3be
    prev=[0x3b2], succ=[0xa4c]
    =================================
    0x3c0: v3c0(0x1d414) = CONST 
    0x3c3: v3c3(0xa4c) = CONST 
    0x3c6: JUMP v3c3(0xa4c)

    Begin block 0xa4c
    prev=[0x3be], succ=[0xa72, 0xa63]
    =================================
    0xa4d: va4d(0x4) = CONST 
    0xa4f: va4f = SLOAD va4d(0x4)
    0xa50: va50(0x0) = CONST 
    0xa53: va53(0x1) = CONST 
    0xa55: va55(0xa0) = CONST 
    0xa57: va57(0x2) = CONST 
    0xa59: va59(0x10000000000000000000000000000000000000000) = EXP va57(0x2), va55(0xa0)
    0xa5a: va5a(0xffffffffffffffffffffffffffffffffffffffff) = SUB va59(0x10000000000000000000000000000000000000000), va53(0x1)
    0xa5b: va5b = AND va5a(0xffffffffffffffffffffffffffffffffffffffff), va4f
    0xa5c: va5c = CALLER 
    0xa5d: va5d = EQ va5c, va5b
    0xa5f: va5f(0xa72) = CONST 
    0xa62: JUMPI va5f(0xa72), va5d

    Begin block 0xa72
    prev=[0xa4c, 0xa63], succ=[0xa88, 0xa79]
    =================================
    0xa72_0x0: va72_0 = PHI va5d, va71
    0xa74: va74 = ISZERO va72_0
    0xa75: va75(0xa88) = CONST 
    0xa78: JUMPI va75(0xa88), va74

    Begin block 0xa88
    prev=[0xa72, 0xa79], succ=[0xa8f, 0xa93]
    =================================
    0xa88_0x0: va88_0 = PHI va5d, va71, va87
    0xa89: va89 = ISZERO va88_0
    0xa8a: va8a = ISZERO va89
    0xa8b: va8b(0xa93) = CONST 
    0xa8e: JUMPI va8b(0xa93), va8a

    Begin block 0xa8f
    prev=[0xa88], succ=[]
    =================================
    0xa8f: va8f(0x0) = CONST 
    0xa92: REVERT va8f(0x0), va8f(0x0)

    Begin block 0xa93
    prev=[0xa88], succ=[0x1d414]
    =================================
    0xa94: va94(0x3) = CONST 
    0xa97: va97 = SLOAD va94(0x3)
    0xa98: va98(0xff0000000000000000000000000000000000000000) = CONST 
    0xaae: vaae(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT va98(0xff0000000000000000000000000000000000000000)
    0xaaf: vaaf = AND vaae(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), va97
    0xab0: vab0(0xa0) = CONST 
    0xab2: vab2(0x2) = CONST 
    0xab4: vab4(0x10000000000000000000000000000000000000000) = EXP vab2(0x2), vab0(0xa0)
    0xab5: vab5 = OR vab4(0x10000000000000000000000000000000000000000), vaaf
    0xab7: SSTORE va94(0x3), vab5
    0xab8: vab8(0x40) = CONST 
    0xaba: vaba = MLOAD vab8(0x40)
    0xabb: vabb(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08) = CONST 
    0xadd: vadd(0x0) = CONST 
    0xae0: LOG1 vaba, vadd(0x0), vabb(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08)
    0xae2: vae2(0x1) = CONST 
    0xae5: JUMP v3c0(0x1d414)

    Begin block 0x1d414
    prev=[0xa93], succ=[]
    =================================
    0x1d415: v1d415(0x40) = CONST 
    0x1d418: v1d418 = MLOAD v1d415(0x40)
    0x1d41a: v1d41a(0x0) = ISZERO vae2(0x1)
    0x1d41b: v1d41b(0x1) = ISZERO v1d41a(0x0)
    0x1d41d: MSTORE v1d418, v1d41b(0x1)
    0x1d41e: v1d41e = MLOAD v1d415(0x40)
    0x1d422: v1d422(0x0) = SUB v1d418, v1d41e
    0x1d423: v1d423(0x20) = CONST 
    0x1d425: v1d425(0x20) = ADD v1d423(0x20), v1d422(0x0)
    0x1d427: RETURN v1d41e, v1d425(0x20)

    Begin block 0xa79
    prev=[0xa72], succ=[0xa88]
    =================================
    0xa7a: va7a(0x3) = CONST 
    0xa7c: va7c = SLOAD va7a(0x3)
    0xa7d: va7d(0xa0) = CONST 
    0xa7f: va7f(0x2) = CONST 
    0xa81: va81(0x10000000000000000000000000000000000000000) = EXP va7f(0x2), va7d(0xa0)
    0xa83: va83 = DIV va7c, va81(0x10000000000000000000000000000000000000000)
    0xa84: va84(0xff) = CONST 
    0xa86: va86 = AND va84(0xff), va83
    0xa87: va87 = ISZERO va86
    0x87ac: v87ac(0xa88) = CONST 
    0x87cc: JUMP v87ac(0xa88)

    Begin block 0xa63
    prev=[0xa4c], succ=[0xa72]
    =================================
    0xa64: va64(0x3) = CONST 
    0xa66: va66 = SLOAD va64(0x3)
    0xa67: va67(0x1) = CONST 
    0xa69: va69(0xa0) = CONST 
    0xa6b: va6b(0x2) = CONST 
    0xa6d: va6d(0x10000000000000000000000000000000000000000) = EXP va6b(0x2), va69(0xa0)
    0xa6e: va6e(0xffffffffffffffffffffffffffffffffffffffff) = SUB va6d(0x10000000000000000000000000000000000000000), va67(0x1)
    0xa6f: va6f = AND va6e(0xffffffffffffffffffffffffffffffffffffffff), va66
    0xa70: va70 = CALLER 
    0xa71: va71 = EQ va70, va6f
    0x7dac: v7dac(0xa72) = CONST 
    0x7dcc: JUMP v7dac(0xa72)

}

function owner()() public {
    Begin block 0x3c7
    prev=[], succ=[0x3cf, 0x3d3]
    =================================
    0x3c8: v3c8 = CALLVALUE 
    0x3ca: v3ca = ISZERO v3c8
    0x3cb: v3cb(0x3d3) = CONST 
    0x3ce: JUMPI v3cb(0x3d3), v3ca

    Begin block 0x3cf
    prev=[0x3c7], succ=[]
    =================================
    0x3cf: v3cf(0x0) = CONST 
    0x3d2: REVERT v3cf(0x0), v3cf(0x0)

    Begin block 0x3d3
    prev=[0x3c7], succ=[0xae6]
    =================================
    0x3d5: v3d5(0x1d447) = CONST 
    0x3d8: v3d8(0xae6) = CONST 
    0x3db: JUMP v3d8(0xae6)

    Begin block 0xae6
    prev=[0x3d3], succ=[0x1d447]
    =================================
    0xae7: vae7(0x3) = CONST 
    0xae9: vae9 = SLOAD vae7(0x3)
    0xaea: vaea(0x1) = CONST 
    0xaec: vaec(0xa0) = CONST 
    0xaee: vaee(0x2) = CONST 
    0xaf0: vaf0(0x10000000000000000000000000000000000000000) = EXP vaee(0x2), vaec(0xa0)
    0xaf1: vaf1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaf0(0x10000000000000000000000000000000000000000), vaea(0x1)
    0xaf2: vaf2 = AND vaf1(0xffffffffffffffffffffffffffffffffffffffff), vae9
    0xaf4: JUMP v3d5(0x1d447)

    Begin block 0x1d447
    prev=[0xae6], succ=[]
    =================================
    0x1d448: v1d448(0x40) = CONST 
    0x1d44b: v1d44b = MLOAD v1d448(0x40)
    0x1d44c: v1d44c(0x1) = CONST 
    0x1d44e: v1d44e(0xa0) = CONST 
    0x1d450: v1d450(0x2) = CONST 
    0x1d452: v1d452(0x10000000000000000000000000000000000000000) = EXP v1d450(0x2), v1d44e(0xa0)
    0x1d453: v1d453(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d452(0x10000000000000000000000000000000000000000), v1d44c(0x1)
    0x1d456: v1d456 = AND vaf2, v1d453(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d458: MSTORE v1d44b, v1d456
    0x1d459: v1d459 = MLOAD v1d448(0x40)
    0x1d45d: v1d45d(0x0) = SUB v1d44b, v1d459
    0x1d45e: v1d45e(0x20) = CONST 
    0x1d460: v1d460(0x20) = ADD v1d45e(0x20), v1d45d(0x0)
    0x1d462: RETURN v1d459, v1d460(0x20)

}

function tokenHolders(uint256)() public {
    Begin block 0x3f8
    prev=[], succ=[0x400, 0x404]
    =================================
    0x3f9: v3f9 = CALLVALUE 
    0x3fb: v3fb = ISZERO v3f9
    0x3fc: v3fc(0x404) = CONST 
    0x3ff: JUMPI v3fc(0x404), v3fb

    Begin block 0x400
    prev=[0x3f8], succ=[]
    =================================
    0x400: v400(0x0) = CONST 
    0x403: REVERT v400(0x0), v400(0x0)

    Begin block 0x404
    prev=[0x3f8], succ=[0xaf5]
    =================================
    0x406: v406(0x1d482) = CONST 
    0x409: v409(0x4) = CONST 
    0x40b: v40b = CALLDATALOAD v409(0x4)
    0x40c: v40c(0xaf5) = CONST 
    0x40f: JUMP v40c(0xaf5)

    Begin block 0xaf5
    prev=[0x404], succ=[0xb02, 0xb03]
    =================================
    0xaf6: vaf6(0x6) = CONST 
    0xaf9: vaf9 = SLOAD vaf6(0x6)
    0xafd: vafd = LT v40b, vaf9
    0xafe: vafe(0xb03) = CONST 
    0xb01: JUMPI vafe(0xb03), vafd

    Begin block 0xb02
    prev=[0xaf5], succ=[]
    =================================
    0xb02: THROW 

    Begin block 0xb03
    prev=[0xaf5], succ=[0x1d482]
    =================================
    0xb04: vb04(0x0) = CONST 
    0xb08: MSTORE vb04(0x0), vaf6(0x6)
    0xb09: vb09(0x20) = CONST 
    0xb0d: vb0d = SHA3 vb04(0x0), vb09(0x20)
    0xb0e: vb0e = ADD vb0d, v40b
    0xb0f: vb0f = SLOAD vb0e
    0xb10: vb10(0x1) = CONST 
    0xb12: vb12(0xa0) = CONST 
    0xb14: vb14(0x2) = CONST 
    0xb16: vb16(0x10000000000000000000000000000000000000000) = EXP vb14(0x2), vb12(0xa0)
    0xb17: vb17(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb16(0x10000000000000000000000000000000000000000), vb10(0x1)
    0xb18: vb18 = AND vb17(0xffffffffffffffffffffffffffffffffffffffff), vb0f
    0xb1c: JUMP v406(0x1d482)

    Begin block 0x1d482
    prev=[0xb03], succ=[]
    =================================
    0x1d483: v1d483(0x40) = CONST 
    0x1d486: v1d486 = MLOAD v1d483(0x40)
    0x1d487: v1d487(0x1) = CONST 
    0x1d489: v1d489(0xa0) = CONST 
    0x1d48b: v1d48b(0x2) = CONST 
    0x1d48d: v1d48d(0x10000000000000000000000000000000000000000) = EXP v1d48b(0x2), v1d489(0xa0)
    0x1d48e: v1d48e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d48d(0x10000000000000000000000000000000000000000), v1d487(0x1)
    0x1d491: v1d491 = AND vb18, v1d48e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d493: MSTORE v1d486, v1d491
    0x1d494: v1d494 = MLOAD v1d483(0x40)
    0x1d498: v1d498(0x0) = SUB v1d486, v1d494
    0x1d499: v1d499(0x20) = CONST 
    0x1d49b: v1d49b(0x20) = ADD v1d499(0x20), v1d498(0x0)
    0x1d49d: RETURN v1d494, v1d49b(0x20)

}

function symbol()() public {
    Begin block 0x410
    prev=[], succ=[0x418, 0x41c]
    =================================
    0x411: v411 = CALLVALUE 
    0x413: v413 = ISZERO v411
    0x414: v414(0x41c) = CONST 
    0x417: JUMPI v414(0x41c), v413

    Begin block 0x418
    prev=[0x410], succ=[]
    =================================
    0x418: v418(0x0) = CONST 
    0x41b: REVERT v418(0x0), v418(0x0)

    Begin block 0x41c
    prev=[0x410], succ=[0xb1d]
    =================================
    0x41e: v41e(0x1d4bd) = CONST 
    0x421: v421(0xb1d) = CONST 
    0x424: JUMP v421(0xb1d)

    Begin block 0xb1d
    prev=[0x41c], succ=[0x1d4bd]
    =================================
    0xb1e: vb1e(0x40) = CONST 
    0xb21: vb21 = MLOAD vb1e(0x40)
    0xb24: vb24 = ADD vb1e(0x40), vb21
    0xb27: MSTORE vb1e(0x40), vb24
    0xb28: vb28(0x3) = CONST 
    0xb2b: MSTORE vb21, vb28(0x3)
    0xb2c: vb2c(0x414d540000000000000000000000000000000000000000000000000000000000) = CONST 
    0xb4d: vb4d(0x20) = CONST 
    0xb50: vb50 = ADD vb21, vb4d(0x20)
    0xb51: MSTORE vb50, vb2c(0x414d540000000000000000000000000000000000000000000000000000000000)
    0xb53: JUMP v41e(0x1d4bd)

    Begin block 0x1d4bd
    prev=[0xb1d], succ=[0x1b80x410]
    =================================
    0x1d4be: v1d4be(0x40) = CONST 
    0x1d4c1: v1d4c1 = MLOAD v1d4be(0x40)
    0x1d4c2: v1d4c2(0x20) = CONST 
    0x1d4c6: MSTORE v1d4c1, v1d4c2(0x20)
    0x1d4c8: v1d4c8(0x3) = MLOAD vb21
    0x1d4cb: v1d4cb = ADD v1d4c1, v1d4c2(0x20)
    0x1d4cc: MSTORE v1d4cb, v1d4c8(0x3)
    0x1d4ce: v1d4ce(0x3) = MLOAD vb21
    0x1d4d5: v1d4d5 = ADD v1d4c1, v1d4be(0x40)
    0x1d4d8: v1d4d8 = ADD vb21, v1d4c2(0x20)
    0x1d4dd: v1d4dd(0x0) = CONST 
    0x1f6d3: v1f6d3(0x1b8) = CONST 
    0x1f6f3: JUMP v1f6d3(0x1b8)

    Begin block 0x1b80x410
    prev=[0x1d4bd, 0x1c10x410], succ=[0x1d00x410, 0x1c10x410]
    =================================
    0x1b80x410_0x0: v1b8410_0 = PHI v1d4dd(0x0), v4101cb
    0x1bb0x410: v4101bb = LT v1b8410_0, v1d4ce(0x3)
    0x1bc0x410: v4101bc = ISZERO v4101bb
    0x1bd0x410: v4101bd(0x1d0) = CONST 
    0x1c00x410: JUMPI v4101bd(0x1d0), v4101bc

    Begin block 0x1d00x410
    prev=[0x1b80x410], succ=[0x1e40x410, 0x1fd0x410]
    =================================
    0x1d90x410: v4101d9 = ADD v1d4ce(0x3), v1d4d5
    0x1db0x410: v4101db(0x1f) = CONST 
    0x1dd0x410: v4101dd(0x3) = AND v4101db(0x1f), v1d4ce(0x3)
    0x1df0x410: v4101df(0x0) = ISZERO v4101dd(0x3)
    0x1e00x410: v4101e0(0x1fd) = CONST 
    0x1e30x410: JUMPI v4101e0(0x1fd), v4101df(0x0)

    Begin block 0x1e40x410
    prev=[0x1d00x410], succ=[0x1fd0x410]
    =================================
    0x1e60x410: v4101e6 = SUB v4101d9, v4101dd(0x3)
    0x1e80x410: v4101e8 = MLOAD v4101e6
    0x1e90x410: v4101e9(0x1) = CONST 
    0x1ec0x410: v4101ec(0x20) = CONST 
    0x1ee0x410: v4101ee(0x1d) = SUB v4101ec(0x20), v4101dd(0x3)
    0x1ef0x410: v4101ef(0x100) = CONST 
    0x1f20x410: v4101f2(0x10000000000000000000000000000000000000000000000000000000000) = EXP v4101ef(0x100), v4101ee(0x1d)
    0x1f30x410: v4101f3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v4101f2(0x10000000000000000000000000000000000000000000000000000000000), v4101e9(0x1)
    0x1f40x410: v4101f4(0xffffff0000000000000000000000000000000000000000000000000000000000) = NOT v4101f3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1f50x410: v4101f5 = AND v4101f4(0xffffff0000000000000000000000000000000000000000000000000000000000), v4101e8
    0x1f70x410: MSTORE v4101e6, v4101f5
    0x1f80x410: v4101f8(0x20) = CONST 
    0x1fa0x410: v4101fa = ADD v4101f8(0x20), v4101e6
    0x2dac0x410: v4102dac(0x1fd) = CONST 
    0x2dcc0x410: JUMP v4102dac(0x1fd)

    Begin block 0x1fd0x410
    prev=[0x1e40x410, 0x1d00x410], succ=[]
    =================================
    0x1fd0x410_0x1: v1fd410_1 = PHI v4101fa, v4101d9
    0x2030x410: v410203(0x40) = CONST 
    0x2050x410: v410205 = MLOAD v410203(0x40)
    0x2080x410: v410208 = SUB v1fd410_1, v410205
    0x20a0x410: RETURN v410205, v410208

    Begin block 0x1c10x410
    prev=[0x1b80x410], succ=[0x1b80x410]
    =================================
    0x1c10x410_0x0: v1c1410_0 = PHI v1d4dd(0x0), v4101cb
    0x1c30x410: v4101c3 = ADD v1c1410_0, v1d4d8
    0x1c40x410: v4101c4 = MLOAD v4101c3
    0x1c70x410: v4101c7 = ADD v1c1410_0, v1d4d5
    0x1c80x410: MSTORE v4101c7, v4101c4
    0x1c90x410: v4101c9(0x20) = CONST 
    0x1cb0x410: v4101cb = ADD v4101c9(0x20), v1c1410_0
    0x1cc0x410: v4101cc(0x1b8) = CONST 
    0x1cf0x410: JUMP v4101cc(0x1b8)

}

function transfer(address,uint256)() public {
    Begin block 0x425
    prev=[], succ=[0x42d, 0x431]
    =================================
    0x426: v426 = CALLVALUE 
    0x428: v428 = ISZERO v426
    0x429: v429(0x431) = CONST 
    0x42c: JUMPI v429(0x431), v428

    Begin block 0x42d
    prev=[0x425], succ=[]
    =================================
    0x42d: v42d(0x0) = CONST 
    0x430: REVERT v42d(0x0), v42d(0x0)

    Begin block 0x431
    prev=[0x425], succ=[0xb54B0x431]
    =================================
    0x433: v433(0x1f713) = CONST 
    0x436: v436(0x1) = CONST 
    0x438: v438(0xa0) = CONST 
    0x43a: v43a(0x2) = CONST 
    0x43c: v43c(0x10000000000000000000000000000000000000000) = EXP v43a(0x2), v438(0xa0)
    0x43d: v43d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43c(0x10000000000000000000000000000000000000000), v436(0x1)
    0x43e: v43e(0x4) = CONST 
    0x440: v440 = CALLDATALOAD v43e(0x4)
    0x441: v441 = AND v440, v43d(0xffffffffffffffffffffffffffffffffffffffff)
    0x442: v442(0x24) = CONST 
    0x444: v444 = CALLDATALOAD v442(0x24)
    0x445: v445(0xb54) = CONST 
    0x448: JUMP v445(0xb54)

    Begin block 0xb54B0x431
    prev=[0x431], succ=[0xb63B0x431]
    =================================
    0xb55S0x431: vb55V431(0x0) = CONST 
    0xb57S0x431: vb57V431(0xb6b) = CONST 
    0xb5aS0x431: vb5aV431(0xb63) = CONST 
    0xb5fS0x431: vb5fV431(0xe47) = CONST 
    0xb62S0x431: vb62_0V431 = CALLPRIVATE vb5fV431(0xe47), v444, v441, vb5aV431(0xb63)

    Begin block 0xb63B0x431
    prev=[0xb54B0x431], succ=[0xb6bB0x431]
    =================================
    0xb64S0x431: vb64V431 = CALLER 
    0xb67S0x431: vb67V431(0xd66) = CONST 
    0xb6aS0x431: vb6a_0V431 = CALLPRIVATE vb67V431(0xd66), v444, v441, vb64V431, vb62_0V431, vb57V431(0xb6b)

    Begin block 0xb6bB0x431
    prev=[0xb63B0x431], succ=[0x1f713]
    =================================
    0xb71S0x431: JUMP v433(0x1f713)

    Begin block 0x1f713
    prev=[0xb6bB0x431], succ=[]
    =================================
    0x1f714: v1f714(0x40) = CONST 
    0x1f717: v1f717 = MLOAD v1f714(0x40)
    0x1f719: v1f719 = ISZERO vb6a_0V431
    0x1f71a: v1f71a = ISZERO v1f719
    0x1f71c: MSTORE v1f717, v1f71a
    0x1f71d: v1f71d = MLOAD v1f714(0x40)
    0x1f721: v1f721(0x0) = SUB v1f717, v1f71d
    0x1f722: v1f722(0x20) = CONST 
    0x1f724: v1f724(0x20) = ADD v1f722(0x20), v1f721(0x0)
    0x1f726: RETURN v1f71d, v1f724(0x20)

}

function saleAgent()() public {
    Begin block 0x449
    prev=[], succ=[0x451, 0x455]
    =================================
    0x44a: v44a = CALLVALUE 
    0x44c: v44c = ISZERO v44a
    0x44d: v44d(0x455) = CONST 
    0x450: JUMPI v44d(0x455), v44c

    Begin block 0x451
    prev=[0x449], succ=[]
    =================================
    0x451: v451(0x0) = CONST 
    0x454: REVERT v451(0x0), v451(0x0)

    Begin block 0x455
    prev=[0x449], succ=[0xb72]
    =================================
    0x457: v457(0x1f746) = CONST 
    0x45a: v45a(0xb72) = CONST 
    0x45d: JUMP v45a(0xb72)

    Begin block 0xb72
    prev=[0x455], succ=[0x1f746]
    =================================
    0xb73: vb73(0x4) = CONST 
    0xb75: vb75 = SLOAD vb73(0x4)
    0xb76: vb76(0x1) = CONST 
    0xb78: vb78(0xa0) = CONST 
    0xb7a: vb7a(0x2) = CONST 
    0xb7c: vb7c(0x10000000000000000000000000000000000000000) = EXP vb7a(0x2), vb78(0xa0)
    0xb7d: vb7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb7c(0x10000000000000000000000000000000000000000), vb76(0x1)
    0xb7e: vb7e = AND vb7d(0xffffffffffffffffffffffffffffffffffffffff), vb75
    0xb80: JUMP v457(0x1f746)

    Begin block 0x1f746
    prev=[0xb72], succ=[]
    =================================
    0x1f747: v1f747(0x40) = CONST 
    0x1f74a: v1f74a = MLOAD v1f747(0x40)
    0x1f74b: v1f74b(0x1) = CONST 
    0x1f74d: v1f74d(0xa0) = CONST 
    0x1f74f: v1f74f(0x2) = CONST 
    0x1f751: v1f751(0x10000000000000000000000000000000000000000) = EXP v1f74f(0x2), v1f74d(0xa0)
    0x1f752: v1f752(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f751(0x10000000000000000000000000000000000000000), v1f74b(0x1)
    0x1f755: v1f755 = AND vb7e, v1f752(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f757: MSTORE v1f74a, v1f755
    0x1f758: v1f758 = MLOAD v1f747(0x40)
    0x1f75c: v1f75c(0x0) = SUB v1f74a, v1f758
    0x1f75d: v1f75d(0x20) = CONST 
    0x1f75f: v1f75f(0x20) = ADD v1f75d(0x20), v1f75c(0x0)
    0x1f761: RETURN v1f758, v1f75f(0x20)

}

function registerCallback(address)() public {
    Begin block 0x45e
    prev=[], succ=[0x466, 0x46a]
    =================================
    0x45f: v45f = CALLVALUE 
    0x461: v461 = ISZERO v45f
    0x462: v462(0x46a) = CONST 
    0x465: JUMPI v462(0x46a), v461

    Begin block 0x466
    prev=[0x45e], succ=[]
    =================================
    0x466: v466(0x0) = CONST 
    0x469: REVERT v466(0x0), v466(0x0)

    Begin block 0x46a
    prev=[0x45e], succ=[0xb81]
    =================================
    0x46c: v46c(0x1f781) = CONST 
    0x46f: v46f(0x1) = CONST 
    0x471: v471(0xa0) = CONST 
    0x473: v473(0x2) = CONST 
    0x475: v475(0x10000000000000000000000000000000000000000) = EXP v473(0x2), v471(0xa0)
    0x476: v476(0xffffffffffffffffffffffffffffffffffffffff) = SUB v475(0x10000000000000000000000000000000000000000), v46f(0x1)
    0x477: v477(0x4) = CONST 
    0x479: v479 = CALLDATALOAD v477(0x4)
    0x47a: v47a = AND v479, v476(0xffffffffffffffffffffffffffffffffffffffff)
    0x47b: v47b(0xb81) = CONST 
    0x47e: JUMP v47b(0xb81)

    Begin block 0xb81
    prev=[0x46a], succ=[0xb94, 0xb98]
    =================================
    0xb82: vb82(0x3) = CONST 
    0xb84: vb84 = SLOAD vb82(0x3)
    0xb85: vb85(0x1) = CONST 
    0xb87: vb87(0xa0) = CONST 
    0xb89: vb89(0x2) = CONST 
    0xb8b: vb8b(0x10000000000000000000000000000000000000000) = EXP vb89(0x2), vb87(0xa0)
    0xb8c: vb8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb8b(0x10000000000000000000000000000000000000000), vb85(0x1)
    0xb8d: vb8d = AND vb8c(0xffffffffffffffffffffffffffffffffffffffff), vb84
    0xb8e: vb8e = CALLER 
    0xb8f: vb8f = EQ vb8e, vb8d
    0xb90: vb90(0xb98) = CONST 
    0xb93: JUMPI vb90(0xb98), vb8f

    Begin block 0xb94
    prev=[0xb81], succ=[]
    =================================
    0xb94: vb94(0x0) = CONST 
    0xb97: REVERT vb94(0x0), vb94(0x0)

    Begin block 0xb98
    prev=[0xb81], succ=[0x1f781]
    =================================
    0xb99: vb99(0x1) = CONST 
    0xb9b: vb9b(0xa0) = CONST 
    0xb9d: vb9d(0x2) = CONST 
    0xb9f: vb9f(0x10000000000000000000000000000000000000000) = EXP vb9d(0x2), vb9b(0xa0)
    0xba0: vba0(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb9f(0x10000000000000000000000000000000000000000), vb99(0x1)
    0xba1: vba1 = AND vba0(0xffffffffffffffffffffffffffffffffffffffff), v47a
    0xba2: vba2(0x0) = CONST 
    0xba6: MSTORE vba2(0x0), vba1
    0xba7: vba7(0x7) = CONST 
    0xba9: vba9(0x20) = CONST 
    0xbab: MSTORE vba9(0x20), vba7(0x7)
    0xbac: vbac(0x40) = CONST 
    0xbaf: vbaf = SHA3 vba2(0x0), vbac(0x40)
    0xbb1: vbb1 = SLOAD vbaf
    0xbb2: vbb2(0xff) = CONST 
    0xbb4: vbb4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vbb2(0xff)
    0xbb5: vbb5 = AND vbb4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vbb1
    0xbb6: vbb6(0x1) = CONST 
    0xbb8: vbb8 = OR vbb6(0x1), vbb5
    0xbba: SSTORE vbaf, vbb8
    0xbbb: JUMP v46c(0x1f781)

    Begin block 0x1f781
    prev=[0xb98], succ=[]
    =================================
    0x1f782: STOP 

}

function increaseApproval(address,uint256)() public {
    Begin block 0x47f
    prev=[], succ=[0x487, 0x48b]
    =================================
    0x480: v480 = CALLVALUE 
    0x482: v482 = ISZERO v480
    0x483: v483(0x48b) = CONST 
    0x486: JUMPI v483(0x48b), v482

    Begin block 0x487
    prev=[0x47f], succ=[]
    =================================
    0x487: v487(0x0) = CONST 
    0x48a: REVERT v487(0x0), v487(0x0)

    Begin block 0x48b
    prev=[0x47f], succ=[0xbbc]
    =================================
    0x48d: v48d(0x1f7a2) = CONST 
    0x490: v490(0x1) = CONST 
    0x492: v492(0xa0) = CONST 
    0x494: v494(0x2) = CONST 
    0x496: v496(0x10000000000000000000000000000000000000000) = EXP v494(0x2), v492(0xa0)
    0x497: v497(0xffffffffffffffffffffffffffffffffffffffff) = SUB v496(0x10000000000000000000000000000000000000000), v490(0x1)
    0x498: v498(0x4) = CONST 
    0x49a: v49a = CALLDATALOAD v498(0x4)
    0x49b: v49b = AND v49a, v497(0xffffffffffffffffffffffffffffffffffffffff)
    0x49c: v49c(0x24) = CONST 
    0x49e: v49e = CALLDATALOAD v49c(0x24)
    0x49f: v49f(0xbbc) = CONST 
    0x4a2: JUMP v49f(0xbbc)

    Begin block 0xbbc
    prev=[0x48b], succ=[0xbf0]
    =================================
    0xbbd: vbbd = CALLER 
    0xbbe: vbbe(0x0) = CONST 
    0xbc2: MSTORE vbbe(0x0), vbbd
    0xbc3: vbc3(0x2) = CONST 
    0xbc5: vbc5(0x20) = CONST 
    0xbc9: MSTORE vbc5(0x20), vbc3(0x2)
    0xbca: vbca(0x40) = CONST 
    0xbce: vbce = SHA3 vbbe(0x0), vbca(0x40)
    0xbcf: vbcf(0x1) = CONST 
    0xbd1: vbd1(0xa0) = CONST 
    0xbd3: vbd3(0x2) = CONST 
    0xbd5: vbd5(0x10000000000000000000000000000000000000000) = EXP vbd3(0x2), vbd1(0xa0)
    0xbd6: vbd6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbd5(0x10000000000000000000000000000000000000000), vbcf(0x1)
    0xbd8: vbd8 = AND v49b, vbd6(0xffffffffffffffffffffffffffffffffffffffff)
    0xbda: MSTORE vbbe(0x0), vbd8
    0xbdd: MSTORE vbc5(0x20), vbce
    0xbdf: vbdf = SHA3 vbbe(0x0), vbca(0x40)
    0xbe0: vbe0 = SLOAD vbdf
    0xbe1: vbe1(0xbf0) = CONST 
    0xbe6: vbe6(0xffffffff) = CONST 
    0xbeb: vbeb(0xe22) = CONST 
    0xbee: vbee(0xe22) = AND vbeb(0xe22), vbe6(0xffffffff)
    0xbef: vbef_0 = CALLPRIVATE vbee(0xe22), v49e, vbe0, vbe1(0xbf0)

    Begin block 0xbf0
    prev=[0xbbc], succ=[0x1f7a2]
    =================================
    0xbf1: vbf1 = CALLER 
    0xbf2: vbf2(0x0) = CONST 
    0xbf6: MSTORE vbf2(0x0), vbf1
    0xbf7: vbf7(0x2) = CONST 
    0xbf9: vbf9(0x20) = CONST 
    0xbfd: MSTORE vbf9(0x20), vbf7(0x2)
    0xbfe: vbfe(0x40) = CONST 
    0xc02: vc02 = SHA3 vbf2(0x0), vbfe(0x40)
    0xc03: vc03(0x1) = CONST 
    0xc05: vc05(0xa0) = CONST 
    0xc07: vc07(0x2) = CONST 
    0xc09: vc09(0x10000000000000000000000000000000000000000) = EXP vc07(0x2), vc05(0xa0)
    0xc0a: vc0a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc09(0x10000000000000000000000000000000000000000), vc03(0x1)
    0xc0c: vc0c = AND v49b, vc0a(0xffffffffffffffffffffffffffffffffffffffff)
    0xc0f: MSTORE vbf2(0x0), vc0c
    0xc12: MSTORE vbf9(0x20), vc02
    0xc16: vc16 = SHA3 vbf2(0x0), vbfe(0x40)
    0xc19: SSTORE vc16, vbef_0
    0xc1b: vc1b = MLOAD vbfe(0x40)
    0xc1e: MSTORE vc1b, vbef_0
    0xc1f: vc1f = MLOAD vbfe(0x40)
    0xc22: vc22(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xc47: vc47(0x0) = SUB vc1b, vc1f
    0xc4a: vc4a(0x20) = ADD vbf9(0x20), vc47(0x0)
    0xc4c: LOG3 vc1f, vc4a(0x20), vc22(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vbf1, vc0c
    0xc4e: vc4e(0x1) = CONST 
    0xc54: JUMP v48d(0x1f7a2)

    Begin block 0x1f7a2
    prev=[0xbf0], succ=[]
    =================================
    0x1f7a3: v1f7a3(0x40) = CONST 
    0x1f7a6: v1f7a6 = MLOAD v1f7a3(0x40)
    0x1f7a8: v1f7a8(0x0) = ISZERO vc4e(0x1)
    0x1f7a9: v1f7a9(0x1) = ISZERO v1f7a8(0x0)
    0x1f7ab: MSTORE v1f7a6, v1f7a9(0x1)
    0x1f7ac: v1f7ac = MLOAD v1f7a3(0x40)
    0x1f7b0: v1f7b0(0x0) = SUB v1f7a6, v1f7ac
    0x1f7b1: v1f7b1(0x20) = CONST 
    0x1f7b3: v1f7b3(0x20) = ADD v1f7b1(0x20), v1f7b0(0x0)
    0x1f7b5: RETURN v1f7ac, v1f7b3(0x20)

}

function unlockedAddressesDuringITO(address)() public {
    Begin block 0x4a3
    prev=[], succ=[0x4ab, 0x4af]
    =================================
    0x4a4: v4a4 = CALLVALUE 
    0x4a6: v4a6 = ISZERO v4a4
    0x4a7: v4a7(0x4af) = CONST 
    0x4aa: JUMPI v4a7(0x4af), v4a6

    Begin block 0x4ab
    prev=[0x4a3], succ=[]
    =================================
    0x4ab: v4ab(0x0) = CONST 
    0x4ae: REVERT v4ab(0x0), v4ab(0x0)

    Begin block 0x4af
    prev=[0x4a3], succ=[0xc55]
    =================================
    0x4b1: v4b1(0x1f7d5) = CONST 
    0x4b4: v4b4(0x1) = CONST 
    0x4b6: v4b6(0xa0) = CONST 
    0x4b8: v4b8(0x2) = CONST 
    0x4ba: v4ba(0x10000000000000000000000000000000000000000) = EXP v4b8(0x2), v4b6(0xa0)
    0x4bb: v4bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ba(0x10000000000000000000000000000000000000000), v4b4(0x1)
    0x4bc: v4bc(0x4) = CONST 
    0x4be: v4be = CALLDATALOAD v4bc(0x4)
    0x4bf: v4bf = AND v4be, v4bb(0xffffffffffffffffffffffffffffffffffffffff)
    0x4c0: v4c0(0xc55) = CONST 
    0x4c3: JUMP v4c0(0xc55)

    Begin block 0xc55
    prev=[0x4af], succ=[0x1f7d5]
    =================================
    0xc56: vc56(0x5) = CONST 
    0xc58: vc58(0x20) = CONST 
    0xc5a: MSTORE vc58(0x20), vc56(0x5)
    0xc5b: vc5b(0x0) = CONST 
    0xc5f: MSTORE vc5b(0x0), v4bf
    0xc60: vc60(0x40) = CONST 
    0xc63: vc63 = SHA3 vc5b(0x0), vc60(0x40)
    0xc64: vc64 = SLOAD vc63
    0xc65: vc65(0xff) = CONST 
    0xc67: vc67 = AND vc65(0xff), vc64
    0xc69: JUMP v4b1(0x1f7d5)

    Begin block 0x1f7d5
    prev=[0xc55], succ=[]
    =================================
    0x1f7d6: v1f7d6(0x40) = CONST 
    0x1f7d9: v1f7d9 = MLOAD v1f7d6(0x40)
    0x1f7db: v1f7db = ISZERO vc67
    0x1f7dc: v1f7dc = ISZERO v1f7db
    0x1f7de: MSTORE v1f7d9, v1f7dc
    0x1f7df: v1f7df = MLOAD v1f7d6(0x40)
    0x1f7e3: v1f7e3(0x0) = SUB v1f7d9, v1f7df
    0x1f7e4: v1f7e4(0x20) = CONST 
    0x1f7e6: v1f7e6(0x20) = ADD v1f7e4(0x20), v1f7e3(0x0)
    0x1f7e8: RETURN v1f7df, v1f7e6(0x20)

}

function allowance(address,address)() public {
    Begin block 0x4c4
    prev=[], succ=[0x4cc, 0x4d0]
    =================================
    0x4c5: v4c5 = CALLVALUE 
    0x4c7: v4c7 = ISZERO v4c5
    0x4c8: v4c8(0x4d0) = CONST 
    0x4cb: JUMPI v4c8(0x4d0), v4c7

    Begin block 0x4cc
    prev=[0x4c4], succ=[]
    =================================
    0x4cc: v4cc(0x0) = CONST 
    0x4cf: REVERT v4cc(0x0), v4cc(0x0)

    Begin block 0x4d0
    prev=[0x4c4], succ=[0xc6a]
    =================================
    0x4d2: v4d2(0x1f808) = CONST 
    0x4d5: v4d5(0x1) = CONST 
    0x4d7: v4d7(0xa0) = CONST 
    0x4d9: v4d9(0x2) = CONST 
    0x4db: v4db(0x10000000000000000000000000000000000000000) = EXP v4d9(0x2), v4d7(0xa0)
    0x4dc: v4dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4db(0x10000000000000000000000000000000000000000), v4d5(0x1)
    0x4dd: v4dd(0x4) = CONST 
    0x4df: v4df = CALLDATALOAD v4dd(0x4)
    0x4e1: v4e1 = AND v4dc(0xffffffffffffffffffffffffffffffffffffffff), v4df
    0x4e3: v4e3(0x24) = CONST 
    0x4e5: v4e5 = CALLDATALOAD v4e3(0x24)
    0x4e6: v4e6 = AND v4e5, v4dc(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e7: v4e7(0xc6a) = CONST 
    0x4ea: JUMP v4e7(0xc6a)

    Begin block 0xc6a
    prev=[0x4d0], succ=[0x1f808]
    =================================
    0xc6b: vc6b(0x1) = CONST 
    0xc6d: vc6d(0xa0) = CONST 
    0xc6f: vc6f(0x2) = CONST 
    0xc71: vc71(0x10000000000000000000000000000000000000000) = EXP vc6f(0x2), vc6d(0xa0)
    0xc72: vc72(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc71(0x10000000000000000000000000000000000000000), vc6b(0x1)
    0xc75: vc75 = AND vc72(0xffffffffffffffffffffffffffffffffffffffff), v4e1
    0xc76: vc76(0x0) = CONST 
    0xc7a: MSTORE vc76(0x0), vc75
    0xc7b: vc7b(0x2) = CONST 
    0xc7d: vc7d(0x20) = CONST 
    0xc81: MSTORE vc7d(0x20), vc7b(0x2)
    0xc82: vc82(0x40) = CONST 
    0xc86: vc86 = SHA3 vc76(0x0), vc82(0x40)
    0xc8a: vc8a = AND vc72(0xffffffffffffffffffffffffffffffffffffffff), v4e6
    0xc8c: MSTORE vc76(0x0), vc8a
    0xc90: MSTORE vc7d(0x20), vc86
    0xc91: vc91 = SHA3 vc76(0x0), vc82(0x40)
    0xc92: vc92 = SLOAD vc91
    0xc94: JUMP v4d2(0x1f808)

    Begin block 0x1f808
    prev=[0xc6a], succ=[]
    =================================
    0x1f809: v1f809(0x40) = CONST 
    0x1f80c: v1f80c = MLOAD v1f809(0x40)
    0x1f80f: MSTORE v1f80c, vc92
    0x1f810: v1f810 = MLOAD v1f809(0x40)
    0x1f814: v1f814(0x0) = SUB v1f80c, v1f810
    0x1f815: v1f815(0x20) = CONST 
    0x1f817: v1f817(0x20) = ADD v1f815(0x20), v1f814(0x0)
    0x1f819: RETURN v1f810, v1f817(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x4eb
    prev=[], succ=[0x4f3, 0x4f7]
    =================================
    0x4ec: v4ec = CALLVALUE 
    0x4ee: v4ee = ISZERO v4ec
    0x4ef: v4ef(0x4f7) = CONST 
    0x4f2: JUMPI v4ef(0x4f7), v4ee

    Begin block 0x4f3
    prev=[0x4eb], succ=[]
    =================================
    0x4f3: v4f3(0x0) = CONST 
    0x4f6: REVERT v4f3(0x0), v4f3(0x0)

    Begin block 0x4f7
    prev=[0x4eb], succ=[0xc95B0x4f7]
    =================================
    0x4f9: v4f9(0x1f839) = CONST 
    0x4fc: v4fc(0x1) = CONST 
    0x4fe: v4fe(0xa0) = CONST 
    0x500: v500(0x2) = CONST 
    0x502: v502(0x10000000000000000000000000000000000000000) = EXP v500(0x2), v4fe(0xa0)
    0x503: v503(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502(0x10000000000000000000000000000000000000000), v4fc(0x1)
    0x504: v504(0x4) = CONST 
    0x506: v506 = CALLDATALOAD v504(0x4)
    0x507: v507 = AND v506, v503(0xffffffffffffffffffffffffffffffffffffffff)
    0x508: v508(0xc95) = CONST 
    0x50b: JUMP v508(0xc95)

    Begin block 0xc95B0x4f7
    prev=[0x4f7], succ=[0xca8B0x4f7, 0xcacB0x4f7]
    =================================
    0xc96S0x4f7: vc96V4f7(0x3) = CONST 
    0xc98S0x4f7: vc98V4f7 = SLOAD vc96V4f7(0x3)
    0xc99S0x4f7: vc99V4f7(0x1) = CONST 
    0xc9bS0x4f7: vc9bV4f7(0xa0) = CONST 
    0xc9dS0x4f7: vc9dV4f7(0x2) = CONST 
    0xc9fS0x4f7: vc9fV4f7(0x10000000000000000000000000000000000000000) = EXP vc9dV4f7(0x2), vc9bV4f7(0xa0)
    0xca0S0x4f7: vca0V4f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc9fV4f7(0x10000000000000000000000000000000000000000), vc99V4f7(0x1)
    0xca1S0x4f7: vca1V4f7 = AND vca0V4f7(0xffffffffffffffffffffffffffffffffffffffff), vc98V4f7
    0xca2S0x4f7: vca2V4f7 = CALLER 
    0xca3S0x4f7: vca3V4f7 = EQ vca2V4f7, vca1V4f7
    0xca4S0x4f7: vca4V4f7(0xcac) = CONST 
    0xca7S0x4f7: JUMPI vca4V4f7(0xcac), vca3V4f7

    Begin block 0xca8B0x4f7
    prev=[0xc95B0x4f7], succ=[]
    =================================
    0xca8S0x4f7: vca8V4f7(0x0) = CONST 
    0xcabS0x4f7: REVERT vca8V4f7(0x0), vca8V4f7(0x0)

    Begin block 0xcacB0x4f7
    prev=[0xc95B0x4f7], succ=[0xed6B0x4f7]
    =================================
    0xcadS0x4f7: vcadV4f7(0xcb5) = CONST 
    0xcb1S0x4f7: vcb1V4f7(0xed6) = CONST 
    0xcb4S0x4f7: JUMP vcb1V4f7(0xed6)

    Begin block 0xed6B0x4f7
    prev=[0xcacB0x4f7], succ=[0xee7B0x4f7, 0xeebB0x4f7]
    =================================
    0xed7S0x4f7: ved7V4f7(0x1) = CONST 
    0xed9S0x4f7: ved9V4f7(0xa0) = CONST 
    0xedbS0x4f7: vedbV4f7(0x2) = CONST 
    0xeddS0x4f7: veddV4f7(0x10000000000000000000000000000000000000000) = EXP vedbV4f7(0x2), ved9V4f7(0xa0)
    0xedeS0x4f7: vedeV4f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB veddV4f7(0x10000000000000000000000000000000000000000), ved7V4f7(0x1)
    0xee0S0x4f7: vee0V4f7 = AND v507, vedeV4f7(0xffffffffffffffffffffffffffffffffffffffff)
    0xee1S0x4f7: vee1V4f7 = ISZERO vee0V4f7
    0xee2S0x4f7: vee2V4f7 = ISZERO vee1V4f7
    0xee3S0x4f7: vee3V4f7(0xeeb) = CONST 
    0xee6S0x4f7: JUMPI vee3V4f7(0xeeb), vee2V4f7

    Begin block 0xee7B0x4f7
    prev=[0xed6B0x4f7], succ=[]
    =================================
    0xee7S0x4f7: vee7V4f7(0x0) = CONST 
    0xeeaS0x4f7: REVERT vee7V4f7(0x0), vee7V4f7(0x0)

    Begin block 0xeebB0x4f7
    prev=[0xed6B0x4f7], succ=[0xcb5B0x4f7]
    =================================
    0xeecS0x4f7: veecV4f7(0x3) = CONST 
    0xeeeS0x4f7: veeeV4f7 = SLOAD veecV4f7(0x3)
    0xeefS0x4f7: veefV4f7(0x40) = CONST 
    0xef1S0x4f7: vef1V4f7 = MLOAD veefV4f7(0x40)
    0xef2S0x4f7: vef2V4f7(0x1) = CONST 
    0xef4S0x4f7: vef4V4f7(0xa0) = CONST 
    0xef6S0x4f7: vef6V4f7(0x2) = CONST 
    0xef8S0x4f7: vef8V4f7(0x10000000000000000000000000000000000000000) = EXP vef6V4f7(0x2), vef4V4f7(0xa0)
    0xef9S0x4f7: vef9V4f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vef8V4f7(0x10000000000000000000000000000000000000000), vef2V4f7(0x1)
    0xefcS0x4f7: vefcV4f7 = AND v507, vef9V4f7(0xffffffffffffffffffffffffffffffffffffffff)
    0xefeS0x4f7: vefeV4f7 = AND veeeV4f7, vef9V4f7(0xffffffffffffffffffffffffffffffffffffffff)
    0xf00S0x4f7: vf00V4f7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xf22S0x4f7: vf22V4f7(0x0) = CONST 
    0xf25S0x4f7: LOG3 vef1V4f7, vf22V4f7(0x0), vf00V4f7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vefeV4f7, vefcV4f7
    0xf26S0x4f7: vf26V4f7(0x3) = CONST 
    0xf29S0x4f7: vf29V4f7 = SLOAD vf26V4f7(0x3)
    0xf2aS0x4f7: vf2aV4f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf3fS0x4f7: vf3fV4f7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vf2aV4f7(0xffffffffffffffffffffffffffffffffffffffff)
    0xf40S0x4f7: vf40V4f7 = AND vf3fV4f7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vf29V4f7
    0xf41S0x4f7: vf41V4f7(0x1) = CONST 
    0xf43S0x4f7: vf43V4f7(0xa0) = CONST 
    0xf45S0x4f7: vf45V4f7(0x2) = CONST 
    0xf47S0x4f7: vf47V4f7(0x10000000000000000000000000000000000000000) = EXP vf45V4f7(0x2), vf43V4f7(0xa0)
    0xf48S0x4f7: vf48V4f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf47V4f7(0x10000000000000000000000000000000000000000), vf41V4f7(0x1)
    0xf4cS0x4f7: vf4cV4f7 = AND vf48V4f7(0xffffffffffffffffffffffffffffffffffffffff), v507
    0xf50S0x4f7: vf50V4f7 = OR vf4cV4f7, vf40V4f7
    0xf52S0x4f7: SSTORE vf26V4f7(0x3), vf50V4f7
    0xf53S0x4f7: JUMP vcadV4f7(0xcb5)

    Begin block 0xcb5B0x4f7
    prev=[0xeebB0x4f7], succ=[0x1f839]
    =================================
    0xcb7S0x4f7: JUMP v4f9(0x1f839)

    Begin block 0x1f839
    prev=[0xcb5B0x4f7], succ=[]
    =================================
    0x1f83a: STOP 

}

function registeredCallbacks(address)() public {
    Begin block 0x50c
    prev=[], succ=[0x514, 0x518]
    =================================
    0x50d: v50d = CALLVALUE 
    0x50f: v50f = ISZERO v50d
    0x510: v510(0x518) = CONST 
    0x513: JUMPI v510(0x518), v50f

    Begin block 0x514
    prev=[0x50c], succ=[]
    =================================
    0x514: v514(0x0) = CONST 
    0x517: REVERT v514(0x0), v514(0x0)

    Begin block 0x518
    prev=[0x50c], succ=[0xcb8]
    =================================
    0x51a: v51a(0x1f85a) = CONST 
    0x51d: v51d(0x1) = CONST 
    0x51f: v51f(0xa0) = CONST 
    0x521: v521(0x2) = CONST 
    0x523: v523(0x10000000000000000000000000000000000000000) = EXP v521(0x2), v51f(0xa0)
    0x524: v524(0xffffffffffffffffffffffffffffffffffffffff) = SUB v523(0x10000000000000000000000000000000000000000), v51d(0x1)
    0x525: v525(0x4) = CONST 
    0x527: v527 = CALLDATALOAD v525(0x4)
    0x528: v528 = AND v527, v524(0xffffffffffffffffffffffffffffffffffffffff)
    0x529: v529(0xcb8) = CONST 
    0x52c: JUMP v529(0xcb8)

    Begin block 0xcb8
    prev=[0x518], succ=[0x1f85a]
    =================================
    0xcb9: vcb9(0x7) = CONST 
    0xcbb: vcbb(0x20) = CONST 
    0xcbd: MSTORE vcbb(0x20), vcb9(0x7)
    0xcbe: vcbe(0x0) = CONST 
    0xcc2: MSTORE vcbe(0x0), v528
    0xcc3: vcc3(0x40) = CONST 
    0xcc6: vcc6 = SHA3 vcbe(0x0), vcc3(0x40)
    0xcc7: vcc7 = SLOAD vcc6
    0xcc8: vcc8(0xff) = CONST 
    0xcca: vcca = AND vcc8(0xff), vcc7
    0xccc: JUMP v51a(0x1f85a)

    Begin block 0x1f85a
    prev=[0xcb8], succ=[]
    =================================
    0x1f85b: v1f85b(0x40) = CONST 
    0x1f85e: v1f85e = MLOAD v1f85b(0x40)
    0x1f860: v1f860 = ISZERO vcca
    0x1f861: v1f861 = ISZERO v1f860
    0x1f863: MSTORE v1f85e, v1f861
    0x1f864: v1f864 = MLOAD v1f85b(0x40)
    0x1f868: v1f868(0x0) = SUB v1f85e, v1f864
    0x1f869: v1f869(0x20) = CONST 
    0x1f86b: v1f86b(0x20) = ADD v1f869(0x20), v1f868(0x0)
    0x1f86d: RETURN v1f864, v1f86b(0x20)

}

function 0xccd(vccdarg0, vccdarg1, vccdarg2, vccdarg3) private {
    Begin block 0xccd
    prev=[], succ=[0xcf7, 0xce5]
    =================================
    0xcce: vcce(0x3) = CONST 
    0xcd0: vcd0 = SLOAD vcce(0x3)
    0xcd1: vcd1(0x0) = CONST 
    0xcd6: vcd6(0xa0) = CONST 
    0xcd8: vcd8(0x2) = CONST 
    0xcda: vcda(0x10000000000000000000000000000000000000000) = EXP vcd8(0x2), vcd6(0xa0)
    0xcdc: vcdc = DIV vcd0, vcda(0x10000000000000000000000000000000000000000)
    0xcdd: vcdd(0xff) = CONST 
    0xcdf: vcdf = AND vcdd(0xff), vcdc
    0xce1: vce1(0xcf7) = CONST 
    0xce4: JUMPI vce1(0xcf7), vcdf

    Begin block 0xcf7
    prev=[0xccd, 0xce5], succ=[0xd0f, 0xcfd]
    =================================
    0xcf7_0x0: vcf7_0 = PHI vcdf, vcf6
    0xcf9: vcf9(0xd0f) = CONST 
    0xcfc: JUMPI vcf9(0xd0f), vcf7_0

    Begin block 0xd0f
    prev=[0xcf7, 0xcfd], succ=[0xd47, 0xd15]
    =================================
    0xd0f_0x0: vd0f_0 = PHI vcdf, vcf6, vd0e
    0xd11: vd11(0xd47) = CONST 
    0xd14: JUMPI vd11(0xd47), vd0f_0

    Begin block 0xd47
    prev=[0xd0f, 0xd15, 0xd2a], succ=[0xd4e, 0xd52]
    =================================
    0xd47_0x0: vd47_0 = PHI vcdf, vcf6, vd0e, vd23, vd46
    0xd48: vd48 = ISZERO vd47_0
    0xd49: vd49 = ISZERO vd48
    0xd4a: vd4a(0xd52) = CONST 
    0xd4d: JUMPI vd4a(0xd52), vd49

    Begin block 0xd4e
    prev=[0xd47], succ=[]
    =================================
    0xd4e: vd4e(0x0) = CONST 
    0xd51: REVERT vd4e(0x0), vd4e(0x0)

    Begin block 0xd52
    prev=[0xd47], succ=[0xf54]
    =================================
    0xd53: vd53(0xd5d) = CONST 
    0xd59: vd59(0xf54) = CONST 
    0xd5c: JUMP vd59(0xf54)

    Begin block 0xf54
    prev=[0xd52], succ=[0xf67, 0xf6b]
    =================================
    0xf55: vf55(0x0) = CONST 
    0xf57: vf57(0x1) = CONST 
    0xf59: vf59(0xa0) = CONST 
    0xf5b: vf5b(0x2) = CONST 
    0xf5d: vf5d(0x10000000000000000000000000000000000000000) = EXP vf5b(0x2), vf59(0xa0)
    0xf5e: vf5e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf5d(0x10000000000000000000000000000000000000000), vf57(0x1)
    0xf60: vf60 = AND vccdarg1, vf5e(0xffffffffffffffffffffffffffffffffffffffff)
    0xf61: vf61 = ISZERO vf60
    0xf62: vf62 = ISZERO vf61
    0xf63: vf63(0xf6b) = CONST 
    0xf66: JUMPI vf63(0xf6b), vf62

    Begin block 0xf67
    prev=[0xf54], succ=[]
    =================================
    0xf67: vf67(0x0) = CONST 
    0xf6a: REVERT vf67(0x0), vf67(0x0)

    Begin block 0xf6b
    prev=[0xf54], succ=[0xf8c, 0xf90]
    =================================
    0xf6c: vf6c(0x1) = CONST 
    0xf6e: vf6e(0xa0) = CONST 
    0xf70: vf70(0x2) = CONST 
    0xf72: vf72(0x10000000000000000000000000000000000000000) = EXP vf70(0x2), vf6e(0xa0)
    0xf73: vf73(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf72(0x10000000000000000000000000000000000000000), vf6c(0x1)
    0xf75: vf75 = AND vccdarg2, vf73(0xffffffffffffffffffffffffffffffffffffffff)
    0xf76: vf76(0x0) = CONST 
    0xf7a: MSTORE vf76(0x0), vf75
    0xf7b: vf7b(0x20) = CONST 
    0xf7f: MSTORE vf7b(0x20), vf76(0x0)
    0xf80: vf80(0x40) = CONST 
    0xf83: vf83 = SHA3 vf76(0x0), vf80(0x40)
    0xf84: vf84 = SLOAD vf83
    0xf86: vf86 = GT vccdarg0, vf84
    0xf87: vf87 = ISZERO vf86
    0xf88: vf88(0xf90) = CONST 
    0xf8b: JUMPI vf88(0xf90), vf87

    Begin block 0xf8c
    prev=[0xf6b], succ=[]
    =================================
    0xf8c: vf8c(0x0) = CONST 
    0xf8f: REVERT vf8c(0x0), vf8c(0x0)

    Begin block 0xf90
    prev=[0xf6b], succ=[0xfbc, 0xfc0]
    =================================
    0xf91: vf91(0x1) = CONST 
    0xf93: vf93(0xa0) = CONST 
    0xf95: vf95(0x2) = CONST 
    0xf97: vf97(0x10000000000000000000000000000000000000000) = EXP vf95(0x2), vf93(0xa0)
    0xf98: vf98(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf97(0x10000000000000000000000000000000000000000), vf91(0x1)
    0xf9a: vf9a = AND vccdarg2, vf98(0xffffffffffffffffffffffffffffffffffffffff)
    0xf9b: vf9b(0x0) = CONST 
    0xf9f: MSTORE vf9b(0x0), vf9a
    0xfa0: vfa0(0x2) = CONST 
    0xfa2: vfa2(0x20) = CONST 
    0xfa6: MSTORE vfa2(0x20), vfa0(0x2)
    0xfa7: vfa7(0x40) = CONST 
    0xfab: vfab = SHA3 vf9b(0x0), vfa7(0x40)
    0xfac: vfac = CALLER 
    0xfae: MSTORE vf9b(0x0), vfac
    0xfb1: MSTORE vfa2(0x20), vfab
    0xfb3: vfb3 = SHA3 vf9b(0x0), vfa7(0x40)
    0xfb4: vfb4 = SLOAD vfb3
    0xfb6: vfb6 = GT vccdarg0, vfb4
    0xfb7: vfb7 = ISZERO vfb6
    0xfb8: vfb8(0xfc0) = CONST 
    0xfbb: JUMPI vfb8(0xfc0), vfb7

    Begin block 0xfbc
    prev=[0xf90], succ=[]
    =================================
    0xfbc: vfbc(0x0) = CONST 
    0xfbf: REVERT vfbc(0x0), vfbc(0x0)

    Begin block 0xfc0
    prev=[0xf90], succ=[0xfe9]
    =================================
    0xfc1: vfc1(0x1) = CONST 
    0xfc3: vfc3(0xa0) = CONST 
    0xfc5: vfc5(0x2) = CONST 
    0xfc7: vfc7(0x10000000000000000000000000000000000000000) = EXP vfc5(0x2), vfc3(0xa0)
    0xfc8: vfc8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfc7(0x10000000000000000000000000000000000000000), vfc1(0x1)
    0xfca: vfca = AND vccdarg2, vfc8(0xffffffffffffffffffffffffffffffffffffffff)
    0xfcb: vfcb(0x0) = CONST 
    0xfcf: MSTORE vfcb(0x0), vfca
    0xfd0: vfd0(0x20) = CONST 
    0xfd4: MSTORE vfd0(0x20), vfcb(0x0)
    0xfd5: vfd5(0x40) = CONST 
    0xfd8: vfd8 = SHA3 vfcb(0x0), vfd5(0x40)
    0xfd9: vfd9 = SLOAD vfd8
    0xfda: vfda(0xfe9) = CONST 
    0xfdf: vfdf(0xffffffff) = CONST 
    0xfe4: vfe4(0xe35) = CONST 
    0xfe7: vfe7(0xe35) = AND vfe4(0xe35), vfdf(0xffffffff)
    0xfe8: vfe8_0 = CALLPRIVATE vfe7(0xe35), vccdarg0, vfd9, vfda(0xfe9)

    Begin block 0xfe9
    prev=[0xfc0], succ=[0x101e]
    =================================
    0xfea: vfea(0x1) = CONST 
    0xfec: vfec(0xa0) = CONST 
    0xfee: vfee(0x2) = CONST 
    0xff0: vff0(0x10000000000000000000000000000000000000000) = EXP vfee(0x2), vfec(0xa0)
    0xff1: vff1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vff0(0x10000000000000000000000000000000000000000), vfea(0x1)
    0xff4: vff4 = AND vccdarg2, vff1(0xffffffffffffffffffffffffffffffffffffffff)
    0xff5: vff5(0x0) = CONST 
    0xff9: MSTORE vff5(0x0), vff4
    0xffa: vffa(0x20) = CONST 
    0xffe: MSTORE vffa(0x20), vff5(0x0)
    0xfff: vfff(0x40) = CONST 
    0x1003: v1003 = SHA3 vff5(0x0), vfff(0x40)
    0x1007: SSTORE v1003, vfe8_0
    0x100a: v100a = AND vccdarg1, vff1(0xffffffffffffffffffffffffffffffffffffffff)
    0x100c: MSTORE vff5(0x0), v100a
    0x100d: v100d = SHA3 vff5(0x0), vfff(0x40)
    0x100e: v100e = SLOAD v100d
    0x100f: v100f(0x101e) = CONST 
    0x1014: v1014(0xffffffff) = CONST 
    0x1019: v1019(0xe22) = CONST 
    0x101c: v101c(0xe22) = AND v1019(0xe22), v1014(0xffffffff)
    0x101d: v101d_0 = CALLPRIVATE v101c(0xe22), vccdarg0, v100e, v100f(0x101e)

    Begin block 0x101e
    prev=[0xfe9], succ=[0x1060]
    =================================
    0x101f: v101f(0x1) = CONST 
    0x1021: v1021(0xa0) = CONST 
    0x1023: v1023(0x2) = CONST 
    0x1025: v1025(0x10000000000000000000000000000000000000000) = EXP v1023(0x2), v1021(0xa0)
    0x1026: v1026(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1025(0x10000000000000000000000000000000000000000), v101f(0x1)
    0x1029: v1029 = AND vccdarg1, v1026(0xffffffffffffffffffffffffffffffffffffffff)
    0x102a: v102a(0x0) = CONST 
    0x102e: MSTORE v102a(0x0), v1029
    0x102f: v102f(0x20) = CONST 
    0x1033: MSTORE v102f(0x20), v102a(0x0)
    0x1034: v1034(0x40) = CONST 
    0x1038: v1038 = SHA3 v102a(0x0), v1034(0x40)
    0x103c: SSTORE v1038, v101d_0
    0x103f: v103f = AND vccdarg2, v1026(0xffffffffffffffffffffffffffffffffffffffff)
    0x1041: MSTORE v102a(0x0), v103f
    0x1042: v1042(0x2) = CONST 
    0x1045: MSTORE v102f(0x20), v1042(0x2)
    0x1048: v1048 = SHA3 v102a(0x0), v1034(0x40)
    0x1049: v1049 = CALLER 
    0x104b: MSTORE v102a(0x0), v1049
    0x104e: MSTORE v102f(0x20), v1048
    0x104f: v104f = SHA3 v102a(0x0), v1034(0x40)
    0x1050: v1050 = SLOAD v104f
    0x1051: v1051(0x1060) = CONST 
    0x1056: v1056(0xffffffff) = CONST 
    0x105b: v105b(0xe35) = CONST 
    0x105e: v105e(0xe35) = AND v105b(0xe35), v1056(0xffffffff)
    0x105f: v105f_0 = CALLPRIVATE v105e(0xe35), vccdarg0, v1050, v1051(0x1060)

    Begin block 0x1060
    prev=[0x101e], succ=[0xd5d]
    =================================
    0x1061: v1061(0x1) = CONST 
    0x1063: v1063(0xa0) = CONST 
    0x1065: v1065(0x2) = CONST 
    0x1067: v1067(0x10000000000000000000000000000000000000000) = EXP v1065(0x2), v1063(0xa0)
    0x1068: v1068(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1067(0x10000000000000000000000000000000000000000), v1061(0x1)
    0x106b: v106b = AND vccdarg2, v1068(0xffffffffffffffffffffffffffffffffffffffff)
    0x106c: v106c(0x0) = CONST 
    0x1070: MSTORE v106c(0x0), v106b
    0x1071: v1071(0x2) = CONST 
    0x1073: v1073(0x20) = CONST 
    0x1077: MSTORE v1073(0x20), v1071(0x2)
    0x1078: v1078(0x40) = CONST 
    0x107c: v107c = SHA3 v106c(0x0), v1078(0x40)
    0x107d: v107d = CALLER 
    0x107f: MSTORE v106c(0x0), v107d
    0x1081: MSTORE v1073(0x20), v107c
    0x1085: v1085 = SHA3 v106c(0x0), v1078(0x40)
    0x1089: SSTORE v1085, v105f_0
    0x108b: v108b = MLOAD v1078(0x40)
    0x108e: MSTORE v108b, vccdarg0
    0x1090: v1090 = MLOAD v1078(0x40)
    0x1093: v1093 = AND vccdarg1, v1068(0xffffffffffffffffffffffffffffffffffffffff)
    0x1097: v1097(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x10bc: v10bc(0x0) = SUB v108b, v1090
    0x10bf: v10bf(0x20) = ADD v1073(0x20), v10bc(0x0)
    0x10c1: LOG3 v1090, v10bf(0x20), v1097(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v106b, v1093
    0x10c3: v10c3(0x1) = CONST 
    0x10ca: JUMP vd53(0xd5d)

    Begin block 0xd5d
    prev=[0x1060], succ=[]
    =================================
    0xd65: RETURNPRIVATE vccdarg3, v10c3(0x1)

    Begin block 0xd15
    prev=[0xd0f], succ=[0xd47, 0xd2a]
    =================================
    0xd16: vd16(0x3) = CONST 
    0xd18: vd18 = SLOAD vd16(0x3)
    0xd19: vd19(0xa0) = CONST 
    0xd1b: vd1b(0x2) = CONST 
    0xd1d: vd1d(0x10000000000000000000000000000000000000000) = EXP vd1b(0x2), vd19(0xa0)
    0xd1f: vd1f = DIV vd18, vd1d(0x10000000000000000000000000000000000000000)
    0xd20: vd20(0xff) = CONST 
    0xd22: vd22 = AND vd20(0xff), vd1f
    0xd23: vd23 = ISZERO vd22
    0xd25: vd25 = ISZERO vd23
    0xd26: vd26(0xd47) = CONST 
    0xd29: JUMPI vd26(0xd47), vd25

    Begin block 0xd2a
    prev=[0xd15], succ=[0xd47]
    =================================
    0xd2b: vd2b(0x1) = CONST 
    0xd2d: vd2d(0xa0) = CONST 
    0xd2f: vd2f(0x2) = CONST 
    0xd31: vd31(0x10000000000000000000000000000000000000000) = EXP vd2f(0x2), vd2d(0xa0)
    0xd32: vd32(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd31(0x10000000000000000000000000000000000000000), vd2b(0x1)
    0xd34: vd34 = AND vccdarg2, vd32(0xffffffffffffffffffffffffffffffffffffffff)
    0xd35: vd35(0x0) = CONST 
    0xd39: MSTORE vd35(0x0), vd34
    0xd3a: vd3a(0x5) = CONST 
    0xd3c: vd3c(0x20) = CONST 
    0xd3e: MSTORE vd3c(0x20), vd3a(0x5)
    0xd3f: vd3f(0x40) = CONST 
    0xd42: vd42 = SHA3 vd35(0x0), vd3f(0x40)
    0xd43: vd43 = SLOAD vd42
    0xd44: vd44(0xff) = CONST 
    0xd46: vd46 = AND vd44(0xff), vd43
    0xa5ac: va5ac(0xd47) = CONST 
    0xa5cc: JUMP va5ac(0xd47)

    Begin block 0xcfd
    prev=[0xcf7], succ=[0xd0f]
    =================================
    0xcfe: vcfe(0x3) = CONST 
    0xd00: vd00 = SLOAD vcfe(0x3)
    0xd01: vd01(0x1) = CONST 
    0xd03: vd03(0xa0) = CONST 
    0xd05: vd05(0x2) = CONST 
    0xd07: vd07(0x10000000000000000000000000000000000000000) = EXP vd05(0x2), vd03(0xa0)
    0xd08: vd08(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd07(0x10000000000000000000000000000000000000000), vd01(0x1)
    0xd0b: vd0b = AND vd08(0xffffffffffffffffffffffffffffffffffffffff), vccdarg2
    0xd0d: vd0d = AND vd00, vd08(0xffffffffffffffffffffffffffffffffffffffff)
    0xd0e: vd0e = EQ vd0d, vd0b
    0x9bac: v9bac(0xd0f) = CONST 
    0x9bcc: JUMP v9bac(0xd0f)

    Begin block 0xce5
    prev=[0xccd], succ=[0xcf7]
    =================================
    0xce6: vce6(0x4) = CONST 
    0xce8: vce8 = SLOAD vce6(0x4)
    0xce9: vce9(0x1) = CONST 
    0xceb: vceb(0xa0) = CONST 
    0xced: vced(0x2) = CONST 
    0xcef: vcef(0x10000000000000000000000000000000000000000) = EXP vced(0x2), vceb(0xa0)
    0xcf0: vcf0(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcef(0x10000000000000000000000000000000000000000), vce9(0x1)
    0xcf3: vcf3 = AND vcf0(0xffffffffffffffffffffffffffffffffffffffff), vccdarg2
    0xcf5: vcf5 = AND vce8, vcf0(0xffffffffffffffffffffffffffffffffffffffff)
    0xcf6: vcf6 = EQ vcf5, vcf3
    0x91ac: v91ac(0xcf7) = CONST 
    0x91cc: JUMP v91ac(0xcf7)

}

function 0xd66(vd66arg0, vd66arg1, vd66arg2, vd66arg3, vd66arg4) private {
    Begin block 0xd66
    prev=[], succ=[0xd8e, 0xd71]
    =================================
    0xd67: vd67(0x0) = CONST 
    0xd6c: vd6c = ISZERO vd66arg3
    0xd6d: vd6d(0xd8e) = CONST 
    0xd70: JUMPI vd6d(0xd8e), vd6c

    Begin block 0xd8e
    prev=[0xd66, 0xd71], succ=[0x1f8b4, 0xd94]
    =================================
    0xd8e_0x0: vd8e_0 = PHI vd8d, vd66arg3
    0xd8f: vd8f = ISZERO vd8e_0
    0xd90: vd90(0x1f8b4) = CONST 
    0xd93: JUMPI vd90(0x1f8b4), vd8f

    Begin block 0x1f8b4
    prev=[0xd8e], succ=[]
    =================================
    0x1f8bd: RETURNPRIVATE vd66arg4, vd66arg3

    Begin block 0xd94
    prev=[0xd8e], succ=[0xdfb, 0xdff]
    =================================
    0xd95: vd95(0x40) = CONST 
    0xd98: vd98 = MLOAD vd95(0x40)
    0xd99: vd99(0x3b66d02b00000000000000000000000000000000000000000000000000000000) = CONST 
    0xdbb: MSTORE vd98, vd99(0x3b66d02b00000000000000000000000000000000000000000000000000000000)
    0xdbc: vdbc(0x1) = CONST 
    0xdbe: vdbe(0xa0) = CONST 
    0xdc0: vdc0(0x2) = CONST 
    0xdc2: vdc2(0x10000000000000000000000000000000000000000) = EXP vdc0(0x2), vdbe(0xa0)
    0xdc3: vdc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdc2(0x10000000000000000000000000000000000000000), vdbc(0x1)
    0xdc6: vdc6 = AND vdc3(0xffffffffffffffffffffffffffffffffffffffff), vd66arg2
    0xdc7: vdc7(0x4) = CONST 
    0xdca: vdca = ADD vd98, vdc7(0x4)
    0xdcb: MSTORE vdca, vdc6
    0xdcc: vdcc(0x24) = CONST 
    0xdcf: vdcf = ADD vd98, vdcc(0x24)
    0xdd2: MSTORE vdcf, vd66arg0
    0xdd4: vdd4 = MLOAD vd95(0x40)
    0xdd8: vdd8 = AND vd66arg1, vdc3(0xffffffffffffffffffffffffffffffffffffffff)
    0xdda: vdda(0x3b66d02b) = CONST 
    0xde0: vde0(0x44) = CONST 
    0xde4: vde4 = ADD vd98, vde0(0x44)
    0xde6: vde6(0x0) = CONST 
    0xded: vded(0x0) = SUB vd98, vdd4
    0xdee: vdee(0x44) = ADD vded(0x0), vde0(0x44)
    0xdf3: vdf3 = EXTCODESIZE vdd8
    0xdf4: vdf4 = ISZERO vdf3
    0xdf6: vdf6 = ISZERO vdf4
    0xdf7: vdf7(0xdff) = CONST 
    0xdfa: JUMPI vdf7(0xdff), vdf6

    Begin block 0xdfb
    prev=[0xd94], succ=[]
    =================================
    0xdfb: vdfb(0x0) = CONST 
    0xdfe: REVERT vdfb(0x0), vdfb(0x0)

    Begin block 0xdff
    prev=[0xd94], succ=[0xe0a, 0xe13]
    =================================
    0xe01: ve01 = GAS 
    0xe02: ve02 = CALL ve01, vdd8, vde6(0x0), vdd4, vdee(0x44), vdd4, vde6(0x0)
    0xe03: ve03 = ISZERO ve02
    0xe05: ve05 = ISZERO ve03
    0xe06: ve06(0xe13) = CONST 
    0xe09: JUMPI ve06(0xe13), ve05

    Begin block 0xe0a
    prev=[0xdff], succ=[]
    =================================
    0xe0a: ve0a = RETURNDATASIZE 
    0xe0b: ve0b(0x0) = CONST 
    0xe0e: RETURNDATACOPY ve0b(0x0), ve0b(0x0), ve0a
    0xe0f: ve0f = RETURNDATASIZE 
    0xe10: ve10(0x0) = CONST 
    0xe12: REVERT ve10(0x0), ve0f

    Begin block 0xe13
    prev=[0xdff], succ=[0x1f904]
    =================================
    0xb9ac: vb9ac(0x1f904) = CONST 
    0xb9cc: JUMP vb9ac(0x1f904)

    Begin block 0x1f904
    prev=[0xe13], succ=[]
    =================================
    0x1f90d: RETURNPRIVATE vd66arg4, vd66arg3

    Begin block 0xd71
    prev=[0xd66], succ=[0xd8e]
    =================================
    0xd72: vd72(0x1) = CONST 
    0xd74: vd74(0xa0) = CONST 
    0xd76: vd76(0x2) = CONST 
    0xd78: vd78(0x10000000000000000000000000000000000000000) = EXP vd76(0x2), vd74(0xa0)
    0xd79: vd79(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd78(0x10000000000000000000000000000000000000000), vd72(0x1)
    0xd7b: vd7b = AND vd66arg1, vd79(0xffffffffffffffffffffffffffffffffffffffff)
    0xd7c: vd7c(0x0) = CONST 
    0xd80: MSTORE vd7c(0x0), vd7b
    0xd81: vd81(0x7) = CONST 
    0xd83: vd83(0x20) = CONST 
    0xd85: MSTORE vd83(0x20), vd81(0x7)
    0xd86: vd86(0x40) = CONST 
    0xd89: vd89 = SHA3 vd7c(0x0), vd86(0x40)
    0xd8a: vd8a = SLOAD vd89
    0xd8b: vd8b(0xff) = CONST 
    0xd8d: vd8d = AND vd8b(0xff), vd8a
    0xafac: vafac(0xd8e) = CONST 
    0xafcc: JUMP vafac(0xd8e)

}

function 0xe22(ve22arg0, ve22arg1, ve22arg2) private {
    Begin block 0xe22
    prev=[], succ=[0xe2e, 0xe2f]
    =================================
    0xe25: ve25 = ADD ve22arg0, ve22arg1
    0xe28: ve28 = LT ve25, ve22arg1
    0xe29: ve29 = ISZERO ve28
    0xe2a: ve2a(0xe2f) = CONST 
    0xe2d: JUMPI ve2a(0xe2f), ve29

    Begin block 0xe2e
    prev=[0xe22], succ=[]
    =================================
    0xe2e: THROW 

    Begin block 0xe2f
    prev=[0xe22], succ=[]
    =================================
    0xe34: RETURNPRIVATE ve22arg2, ve25

}

function 0xe35(ve35arg0, ve35arg1, ve35arg2) private {
    Begin block 0xe35
    prev=[], succ=[0xe40, 0xe41]
    =================================
    0xe36: ve36(0x0) = CONST 
    0xe3a: ve3a = GT ve35arg0, ve35arg1
    0xe3b: ve3b = ISZERO ve3a
    0xe3c: ve3c(0xe41) = CONST 
    0xe3f: JUMPI ve3c(0xe41), ve3b

    Begin block 0xe40
    prev=[0xe35], succ=[]
    =================================
    0xe40: THROW 

    Begin block 0xe41
    prev=[0xe35], succ=[]
    =================================
    0xe44: ve44 = SUB ve35arg1, ve35arg0
    0xe46: RETURNPRIVATE ve35arg2, ve44

}

function 0xe47(ve47arg0, ve47arg1, ve47arg2) private {
    Begin block 0xe47
    prev=[], succ=[0xe71, 0xe5f]
    =================================
    0xe48: ve48(0x3) = CONST 
    0xe4a: ve4a = SLOAD ve48(0x3)
    0xe4b: ve4b(0x0) = CONST 
    0xe4e: ve4e = CALLER 
    0xe50: ve50(0xa0) = CONST 
    0xe52: ve52(0x2) = CONST 
    0xe54: ve54(0x10000000000000000000000000000000000000000) = EXP ve52(0x2), ve50(0xa0)
    0xe56: ve56 = DIV ve4a, ve54(0x10000000000000000000000000000000000000000)
    0xe57: ve57(0xff) = CONST 
    0xe59: ve59 = AND ve57(0xff), ve56
    0xe5b: ve5b(0xe71) = CONST 
    0xe5e: JUMPI ve5b(0xe71), ve59

    Begin block 0xe71
    prev=[0xe47, 0xe5f], succ=[0xe89, 0xe77]
    =================================
    0xe71_0x0: ve71_0 = PHI ve59, ve70
    0xe73: ve73(0xe89) = CONST 
    0xe76: JUMPI ve73(0xe89), ve71_0

    Begin block 0xe89
    prev=[0xe71, 0xe77], succ=[0xec1, 0xe8f]
    =================================
    0xe89_0x0: ve89_0 = PHI ve59, ve70, ve88
    0xe8b: ve8b(0xec1) = CONST 
    0xe8e: JUMPI ve8b(0xec1), ve89_0

    Begin block 0xec1
    prev=[0xe89, 0xe8f, 0xea4], succ=[0xec8, 0xecc]
    =================================
    0xec1_0x0: vec1_0 = PHI ve59, ve70, ve88, ve9d, vec0
    0xec2: vec2 = ISZERO vec1_0
    0xec3: vec3 = ISZERO vec2
    0xec4: vec4(0xecc) = CONST 
    0xec7: JUMPI vec4(0xecc), vec3

    Begin block 0xec8
    prev=[0xec1], succ=[]
    =================================
    0xec8: vec8(0x0) = CONST 
    0xecb: REVERT vec8(0x0), vec8(0x0)

    Begin block 0xecc
    prev=[0xec1], succ=[0x10cb]
    =================================
    0xecd: vecd(0x1f8dd) = CONST 
    0xed2: ved2(0x10cb) = CONST 
    0xed5: JUMP ved2(0x10cb)

    Begin block 0x10cb
    prev=[0xecc], succ=[0x10de, 0x10e2]
    =================================
    0x10cc: v10cc(0x0) = CONST 
    0x10ce: v10ce(0x1) = CONST 
    0x10d0: v10d0(0xa0) = CONST 
    0x10d2: v10d2(0x2) = CONST 
    0x10d4: v10d4(0x10000000000000000000000000000000000000000) = EXP v10d2(0x2), v10d0(0xa0)
    0x10d5: v10d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10d4(0x10000000000000000000000000000000000000000), v10ce(0x1)
    0x10d7: v10d7 = AND ve47arg1, v10d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x10d8: v10d8 = ISZERO v10d7
    0x10d9: v10d9 = ISZERO v10d8
    0x10da: v10da(0x10e2) = CONST 
    0x10dd: JUMPI v10da(0x10e2), v10d9

    Begin block 0x10de
    prev=[0x10cb], succ=[]
    =================================
    0x10de: v10de(0x0) = CONST 
    0x10e1: REVERT v10de(0x0), v10de(0x0)

    Begin block 0x10e2
    prev=[0x10cb], succ=[0x10fa, 0x10fe]
    =================================
    0x10e3: v10e3 = CALLER 
    0x10e4: v10e4(0x0) = CONST 
    0x10e8: MSTORE v10e4(0x0), v10e3
    0x10e9: v10e9(0x20) = CONST 
    0x10ed: MSTORE v10e9(0x20), v10e4(0x0)
    0x10ee: v10ee(0x40) = CONST 
    0x10f1: v10f1 = SHA3 v10e4(0x0), v10ee(0x40)
    0x10f2: v10f2 = SLOAD v10f1
    0x10f4: v10f4 = GT ve47arg0, v10f2
    0x10f5: v10f5 = ISZERO v10f4
    0x10f6: v10f6(0x10fe) = CONST 
    0x10f9: JUMPI v10f6(0x10fe), v10f5

    Begin block 0x10fa
    prev=[0x10e2], succ=[]
    =================================
    0x10fa: v10fa(0x0) = CONST 
    0x10fd: REVERT v10fa(0x0), v10fa(0x0)

    Begin block 0x10fe
    prev=[0x10e2], succ=[0x111e]
    =================================
    0x10ff: v10ff = CALLER 
    0x1100: v1100(0x0) = CONST 
    0x1104: MSTORE v1100(0x0), v10ff
    0x1105: v1105(0x20) = CONST 
    0x1109: MSTORE v1105(0x20), v1100(0x0)
    0x110a: v110a(0x40) = CONST 
    0x110d: v110d = SHA3 v1100(0x0), v110a(0x40)
    0x110e: v110e = SLOAD v110d
    0x110f: v110f(0x111e) = CONST 
    0x1114: v1114(0xffffffff) = CONST 
    0x1119: v1119(0xe35) = CONST 
    0x111c: v111c(0xe35) = AND v1119(0xe35), v1114(0xffffffff)
    0x111d: v111d_0 = CALLPRIVATE v111c(0xe35), ve47arg0, v110e, v110f(0x111e)

    Begin block 0x111e
    prev=[0x10fe], succ=[0x1150]
    =================================
    0x111f: v111f = CALLER 
    0x1120: v1120(0x0) = CONST 
    0x1124: MSTORE v1120(0x0), v111f
    0x1125: v1125(0x20) = CONST 
    0x1129: MSTORE v1125(0x20), v1120(0x0)
    0x112a: v112a(0x40) = CONST 
    0x112e: v112e = SHA3 v1120(0x0), v112a(0x40)
    0x1132: SSTORE v112e, v111d_0
    0x1133: v1133(0x1) = CONST 
    0x1135: v1135(0xa0) = CONST 
    0x1137: v1137(0x2) = CONST 
    0x1139: v1139(0x10000000000000000000000000000000000000000) = EXP v1137(0x2), v1135(0xa0)
    0x113a: v113a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1139(0x10000000000000000000000000000000000000000), v1133(0x1)
    0x113c: v113c = AND ve47arg1, v113a(0xffffffffffffffffffffffffffffffffffffffff)
    0x113e: MSTORE v1120(0x0), v113c
    0x113f: v113f = SHA3 v1120(0x0), v112a(0x40)
    0x1140: v1140 = SLOAD v113f
    0x1141: v1141(0x1150) = CONST 
    0x1146: v1146(0xffffffff) = CONST 
    0x114b: v114b(0xe22) = CONST 
    0x114e: v114e(0xe22) = AND v114b(0xe22), v1146(0xffffffff)
    0x114f: v114f_0 = CALLPRIVATE v114e(0xe22), ve47arg0, v1140, v1141(0x1150)

    Begin block 0x1150
    prev=[0x111e], succ=[0x1f8dd]
    =================================
    0x1151: v1151(0x1) = CONST 
    0x1153: v1153(0xa0) = CONST 
    0x1155: v1155(0x2) = CONST 
    0x1157: v1157(0x10000000000000000000000000000000000000000) = EXP v1155(0x2), v1153(0xa0)
    0x1158: v1158(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1157(0x10000000000000000000000000000000000000000), v1151(0x1)
    0x115a: v115a = AND ve47arg1, v1158(0xffffffffffffffffffffffffffffffffffffffff)
    0x115b: v115b(0x0) = CONST 
    0x115f: MSTORE v115b(0x0), v115a
    0x1160: v1160(0x20) = CONST 
    0x1164: MSTORE v1160(0x20), v115b(0x0)
    0x1165: v1165(0x40) = CONST 
    0x116a: v116a = SHA3 v115b(0x0), v1165(0x40)
    0x116e: SSTORE v116a, v114f_0
    0x1170: v1170 = MLOAD v1165(0x40)
    0x1173: MSTORE v1170, ve47arg0
    0x1175: v1175 = MLOAD v1165(0x40)
    0x1178: v1178 = CALLER 
    0x117a: v117a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x119e: v119e(0x0) = SUB v1170, v1175
    0x11a1: v11a1(0x20) = ADD v1160(0x20), v119e(0x0)
    0x11a3: LOG3 v1175, v11a1(0x20), v117a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1178, v115a
    0x11a5: v11a5(0x1) = CONST 
    0x11ab: JUMP vecd(0x1f8dd)

    Begin block 0x1f8dd
    prev=[0x1150], succ=[]
    =================================
    0x1f8e4: RETURNPRIVATE ve47arg2, v11a5(0x1)

    Begin block 0xe8f
    prev=[0xe89], succ=[0xec1, 0xea4]
    =================================
    0xe90: ve90(0x3) = CONST 
    0xe92: ve92 = SLOAD ve90(0x3)
    0xe93: ve93(0xa0) = CONST 
    0xe95: ve95(0x2) = CONST 
    0xe97: ve97(0x10000000000000000000000000000000000000000) = EXP ve95(0x2), ve93(0xa0)
    0xe99: ve99 = DIV ve92, ve97(0x10000000000000000000000000000000000000000)
    0xe9a: ve9a(0xff) = CONST 
    0xe9c: ve9c = AND ve9a(0xff), ve99
    0xe9d: ve9d = ISZERO ve9c
    0xe9f: ve9f = ISZERO ve9d
    0xea0: vea0(0xec1) = CONST 
    0xea3: JUMPI vea0(0xec1), ve9f

    Begin block 0xea4
    prev=[0xe8f], succ=[0xec1]
    =================================
    0xea5: vea5(0x1) = CONST 
    0xea7: vea7(0xa0) = CONST 
    0xea9: vea9(0x2) = CONST 
    0xeab: veab(0x10000000000000000000000000000000000000000) = EXP vea9(0x2), vea7(0xa0)
    0xeac: veac(0xffffffffffffffffffffffffffffffffffffffff) = SUB veab(0x10000000000000000000000000000000000000000), vea5(0x1)
    0xeae: veae = AND ve4e, veac(0xffffffffffffffffffffffffffffffffffffffff)
    0xeaf: veaf(0x0) = CONST 
    0xeb3: MSTORE veaf(0x0), veae
    0xeb4: veb4(0x5) = CONST 
    0xeb6: veb6(0x20) = CONST 
    0xeb8: MSTORE veb6(0x20), veb4(0x5)
    0xeb9: veb9(0x40) = CONST 
    0xebc: vebc = SHA3 veaf(0x0), veb9(0x40)
    0xebd: vebd = SLOAD vebc
    0xebe: vebe(0xff) = CONST 
    0xec0: vec0 = AND vebe(0xff), vebd
    0xd7ac: vd7ac(0xec1) = CONST 
    0xd7cc: JUMP vd7ac(0xec1)

    Begin block 0xe77
    prev=[0xe71], succ=[0xe89]
    =================================
    0xe78: ve78(0x3) = CONST 
    0xe7a: ve7a = SLOAD ve78(0x3)
    0xe7b: ve7b(0x1) = CONST 
    0xe7d: ve7d(0xa0) = CONST 
    0xe7f: ve7f(0x2) = CONST 
    0xe81: ve81(0x10000000000000000000000000000000000000000) = EXP ve7f(0x2), ve7d(0xa0)
    0xe82: ve82(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve81(0x10000000000000000000000000000000000000000), ve7b(0x1)
    0xe85: ve85 = AND ve82(0xffffffffffffffffffffffffffffffffffffffff), ve4e
    0xe87: ve87 = AND ve7a, ve82(0xffffffffffffffffffffffffffffffffffffffff)
    0xe88: ve88 = EQ ve87, ve85
    0xcdac: vcdac(0xe89) = CONST 
    0xcdcc: JUMP vcdac(0xe89)

    Begin block 0xe5f
    prev=[0xe47], succ=[0xe71]
    =================================
    0xe60: ve60(0x4) = CONST 
    0xe62: ve62 = SLOAD ve60(0x4)
    0xe63: ve63(0x1) = CONST 
    0xe65: ve65(0xa0) = CONST 
    0xe67: ve67(0x2) = CONST 
    0xe69: ve69(0x10000000000000000000000000000000000000000) = EXP ve67(0x2), ve65(0xa0)
    0xe6a: ve6a(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve69(0x10000000000000000000000000000000000000000), ve63(0x1)
    0xe6d: ve6d = AND ve6a(0xffffffffffffffffffffffffffffffffffffffff), ve4e
    0xe6f: ve6f = AND ve62, ve6a(0xffffffffffffffffffffffffffffffffffffffff)
    0xe70: ve70 = EQ ve6f, ve6d
    0xc3ac: vc3ac(0xe71) = CONST 
    0xc3cc: JUMP vc3ac(0xe71)

}

