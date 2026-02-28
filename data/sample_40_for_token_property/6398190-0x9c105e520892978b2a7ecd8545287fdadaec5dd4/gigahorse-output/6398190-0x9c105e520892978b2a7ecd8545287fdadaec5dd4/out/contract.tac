function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x1556]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x156: v156(0x1556) = CONST 
    0x176: JUMPI v156(0x1556), v8

    Begin block 0xc
    prev=[0x0], succ=[0x1556, 0x1f56]
    =================================
    0xc: vc(0xffffffff) = CONST 
    0x11: v11(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f(0x0) = CONST 
    0x31: v31 = CALLDATALOAD v2f(0x0)
    0x32: v32 = DIV v31, v11(0x100000000000000000000000000000000000000000000000000000000)
    0x33: v33 = AND v32, vc(0xffffffff)
    0x34: v34(0xc542675e) = CONST 
    0x3a: v3a = EQ v33, v34(0xc542675e)
    0xb56: vb56(0x1f56) = CONST 
    0xb76: JUMPI vb56(0x1f56), v3a

    Begin block 0x1556
    prev=[0x0, 0xc], succ=[]
    =================================
    0x1576: v1576(0x3e) = CONST 
    0x1596: CALLPRIVATE v1576(0x3e)

    Begin block 0x1f56
    prev=[0xc], succ=[]
    =================================
    0x1f76: v1f76(0x43) = CONST 
    0x1f96: CALLPRIVATE v1f76(0x43)

}

function fallback()() public {
    Begin block 0x3e
    prev=[], succ=[]
    =================================
    0x3f: v3f(0x0) = CONST 
    0x42: REVERT v3f(0x0), v3f(0x0)

}

function fus(uint256)() public {
    Begin block 0x43
    prev=[], succ=[0x4a, 0x4e]
    =================================
    0x44: v44 = CALLVALUE 
    0x46: v46 = ISZERO v44
    0x47: v47(0x4e) = CONST 
    0x49: JUMPI v47(0x4e), v46

    Begin block 0x4a
    prev=[0x43], succ=[]
    =================================
    0x4a: v4a(0x0) = CONST 
    0x4d: REVERT v4a(0x0), v4a(0x0)

    Begin block 0x4e
    prev=[0x43], succ=[0x6a]
    =================================
    0x50: v50(0x58) = CONST 
    0x52: v52(0x4) = CONST 
    0x54: v54 = CALLDATALOAD v52(0x4)
    0x55: v55(0x6a) = CONST 
    0x57: JUMP v55(0x6a)

    Begin block 0x6a
    prev=[0x4e], succ=[0x58]
    =================================
    0x6b: v6b(0x64) = CONST 
    0x6d: v6d = MUL v6b(0x64), v54
    0x6f: JUMP v50(0x58)

    Begin block 0x58
    prev=[0x6a], succ=[]
    =================================
    0x59: v59(0x40) = CONST 
    0x5c: v5c = MLOAD v59(0x40)
    0x5f: MSTORE v5c, v6d
    0x60: v60 = MLOAD v59(0x40)
    0x64: v64(0x0) = SUB v5c, v60
    0x65: v65(0x20) = CONST 
    0x67: v67(0x20) = ADD v65(0x20), v64(0x0)
    0x69: RETURN v60, v67(0x20)

}

