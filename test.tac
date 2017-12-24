VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.printA;
}

VTABLE(_B) {
    <empty>
    B
    _B.init;
    _B.setB;
    _B.printB;
    _B.setA;
    _B.printA;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T10 = 8
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    _T13 = VTBL <_A>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T14 = 12
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    _T17 = VTBL <_B>
    *(_T15 + 0) = _T17
    return _T15
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T18 = 4
    parm _T18
    _T19 =  call _Alloc
    _T20 = VTBL <_Main>
    *(_T19 + 0) = _T20
    return _T19
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8'
_A.setA:
    _T21 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_A.printA) {
memo '_T2:4'
_A.printA:
    _T22 = *(_T2 + 4)
    parm _T22
    call _PrintInt
    _T23 = "\n"
    parm _T23
    call _PrintString
}

FUNCTION(_B.init) {
memo '_T3:4'
_B.init:
    _T24 = *(_T3 + 8)
    _T25 =  call _A_New
    *(_T3 + 8) = _T25
}

FUNCTION(_B.setB) {
memo '_T4:4 _T5:8'
_B.setB:
    _T26 = *(_T4 + 4)
    *(_T4 + 4) = _T5
}

FUNCTION(_B.printB) {
memo '_T6:4'
_B.printB:
    _T27 = *(_T6 + 4)
    parm _T27
    call _PrintInt
    _T28 = "\n"
    parm _T28
    call _PrintString
}

FUNCTION(_B.setA) {
memo '_T7:4 _T8:8'
_B.setA:
    _T29 = *(_T7 + 8)
    parm _T29
    parm _T8
    _T30 = *(_T29 + 0)
    _T31 = *(_T30 + 8)
    call _T31
}

FUNCTION(_B.printA) {
memo '_T9:4'
_B.printA:
    _T32 = *(_T9 + 8)
    parm _T32
    _T33 = *(_T32 + 0)
    _T34 = *(_T33 + 12)
    call _T34
}

FUNCTION(main) {
memo ''
main:
    _T37 =  call _B_New
    _T35 = _T37
    parm _T35
    _T38 = *(_T35 + 0)
    _T39 = *(_T38 + 8)
    call _T39
    _T40 = 1
    parm _T35
    parm _T40
    _T41 = *(_T35 + 0)
    _T42 = *(_T41 + 20)
    call _T42
    _T43 = 2
    parm _T35
    parm _T43
    _T44 = *(_T35 + 0)
    _T45 = *(_T44 + 12)
    call _T45
    parm _T35
    _T46 = *(_T35 + 0)
    _T47 = *(_T46 + 24)
    call _T47
    parm _T35
    _T48 = *(_T35 + 0)
    _T49 = *(_T48 + 16)
    call _T49
    _T50 =  call _B_New
    _T51 = 12
    _T52 = 4
_L19:
    if (_T51 == 0) branch _L20
    _T53 = (_T51 - _T52)
    _T51 = _T53
    _T54 = (_T35 + _T51)
    _T55 = *(_T54 + 0)
    _T56 = (_T50 + _T51)
    *(_T56 + 0) = _T55
    branch _L19
_L20:
    _T57 = VTBL <_B>
    *(_T50 + 0) = _T57
    _T36 = _T50
    parm _T36
    _T58 = *(_T36 + 0)
    _T59 = *(_T58 + 24)
    call _T59
    parm _T36
    _T60 = *(_T36 + 0)
    _T61 = *(_T60 + 16)
    call _T61
    _T62 = 3
    parm _T36
    parm _T62
    _T63 = *(_T36 + 0)
    _T64 = *(_T63 + 20)
    call _T64
    _T65 = 4
    parm _T36
    parm _T65
    _T66 = *(_T36 + 0)
    _T67 = *(_T66 + 12)
    call _T67
    parm _T36
    _T68 = *(_T36 + 0)
    _T69 = *(_T68 + 24)
    call _T69
    parm _T36
    _T70 = *(_T36 + 0)
    _T71 = *(_T70 + 16)
    call _T71
    parm _T35
    _T72 = *(_T35 + 0)
    _T73 = *(_T72 + 24)
    call _T73
    parm _T35
    _T74 = *(_T35 + 0)
    _T75 = *(_T74 + 16)
    call _T75
}

