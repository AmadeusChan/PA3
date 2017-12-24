VTABLE(_A) {
    <empty>
    A
    _A.setAx;
    _A.printAx;
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

FUNCTION(_A.setAx) {
memo '_T0:4 _T1:8'
_A.setAx:
    _T21 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_A.printAx) {
memo '_T2:4'
_A.printAx:
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
    _T51 = 4
    _T52 = 8
    _T55 = (_T35 + _T51)
    _T53 = _T55
    _T56 = (_T50 + _T51)
    _T54 = _T56
    _T57 = *(_T53 + 0)
    *(_T54 + 0) = _T57
    _T58 = (_T53 + _T51)
    _T53 = _T58
    _T59 = (_T54 + _T51)
    _T54 = _T59
    _T60 = *(_T53 + 0)
    _T61 =  call _A_New
    _T62 = 4
    _T63 = 8
    _T66 = (_T60 + _T62)
    _T64 = _T66
    _T67 = (_T61 + _T62)
    _T65 = _T67
    _T68 = *(_T64 + 0)
    *(_T65 + 0) = _T68
    _T69 = (_T64 + _T62)
    _T64 = _T69
    _T70 = (_T65 + _T62)
    _T65 = _T70
    _T71 = VTBL <_A>
    *(_T61 + 0) = _T71
    *(_T54 + 0) = _T61
    _T72 = (_T53 + _T51)
    _T53 = _T72
    _T73 = (_T54 + _T51)
    _T54 = _T73
    _T74 = VTBL <_B>
    *(_T50 + 0) = _T74
    _T36 = _T50
    parm _T36
    _T75 = *(_T36 + 0)
    _T76 = *(_T75 + 24)
    call _T76
    parm _T36
    _T77 = *(_T36 + 0)
    _T78 = *(_T77 + 16)
    call _T78
    _T79 = 3
    parm _T36
    parm _T79
    _T80 = *(_T36 + 0)
    _T81 = *(_T80 + 20)
    call _T81
    _T82 = 4
    parm _T36
    parm _T82
    _T83 = *(_T36 + 0)
    _T84 = *(_T83 + 12)
    call _T84
    parm _T36
    _T85 = *(_T36 + 0)
    _T86 = *(_T85 + 24)
    call _T86
    parm _T36
    _T87 = *(_T36 + 0)
    _T88 = *(_T87 + 16)
    call _T88
    parm _T35
    _T89 = *(_T35 + 0)
    _T90 = *(_T89 + 24)
    call _T90
    parm _T35
    _T91 = *(_T35 + 0)
    _T92 = *(_T91 + 16)
    call _T92
}

