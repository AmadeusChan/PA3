VTABLE(_Main) {
    <empty>
    Main
    _Main.tester;
    _Main.start;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 12
    parm _T3
    _T4 =  call _Alloc
    _T5 = 0
    *(_T4 + 4) = _T5
    *(_T4 + 8) = _T5
    _T6 = VTBL <_Main>
    *(_T4 + 0) = _T6
    return _T4
}

FUNCTION(_Main.tester) {
memo '_T0:4 _T1:8'
_Main.tester:
    _T7 = *(_T0 + 8)
    _T8 = 1
    _T9 = 0
    _T10 = (_T8 < _T9)
    if (_T10 == 0) branch _L12
    _T11 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T11
    call _PrintString
    call _Halt
_L12:
    _T12 = 4
    _T13 = (_T12 * _T8)
    _T14 = (_T12 + _T13)
    parm _T14
    _T15 =  call _Alloc
    *(_T15 + 0) = _T8
    _T16 = 0
    _T15 = (_T15 + _T14)
_L13:
    _T14 = (_T14 - _T12)
    if (_T14 == 0) branch _L14
    _T15 = (_T15 - _T12)
    *(_T15 + 0) = _T16
    branch _L13
_L14:
    *(_T0 + 8) = _T15
    _T17 = 0
    _T18 = (_T1 < _T17)
    if (_T18 == 0) branch _L15
    _T19 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T19
    call _PrintString
    call _Halt
_L15:
    _T20 = 4
    _T21 = (_T20 * _T1)
    _T22 = (_T20 + _T21)
    parm _T22
    _T23 =  call _Alloc
    *(_T23 + 0) = _T1
    _T24 = 0
    _T23 = (_T23 + _T22)
_L16:
    _T22 = (_T22 - _T20)
    if (_T22 == 0) branch _L17
    _T23 = (_T23 - _T20)
    *(_T23 + 0) = _T24
    branch _L16
_L17:
    return _T23
}

FUNCTION(_Main.start) {
memo '_T2:4'
_Main.start:
    _T28 = 1
    _T25 = _T28
_L18:
    _T29 = 5
    _T30 = (_T25 < _T29)
    if (_T30 == 0) branch _L19
    _T31 = 2
    if (_T31 != 0) branch _L20
    _T32 = "Decaf runtime error: Division by zero error.\n"
    parm _T32
    call _PrintString
    call _Halt
_L20:
    _T33 = (_T25 % _T31)
    _T34 = 0
    _T35 = (_T33 == _T34)
    if (_T35 == 0) branch _L21
    parm _T2
    parm _T25
    _T36 = *(_T2 + 0)
    _T37 = *(_T36 + 8)
    _T38 =  call _T37
    _T27 = _T38
    branch _L19
_L21:
    _T39 = "Loop "
    parm _T39
    call _PrintString
    parm _T25
    call _PrintInt
    _T40 = "\n"
    parm _T40
    call _PrintString
    _T41 = 1
    _T42 = (_T25 + _T41)
    _T25 = _T42
    branch _L18
_L19:
    _T43 = 0
    _T44 = *(_T27 - 4)
    _T45 = (_T43 < _T44)
    if (_T45 == 0) branch _L22
    _T46 = 0
    _T47 = (_T43 < _T46)
    if (_T47 == 0) branch _L23
_L22:
    _T48 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T48
    call _PrintString
    call _Halt
_L23:
    _T49 = 4
    _T50 = (_T43 * _T49)
    _T51 = (_T27 + _T50)
    _T52 = *(_T51 + 0)
    _T53 = 0
    _T54 = 4
    _T55 = (_T43 * _T54)
    _T56 = (_T27 + _T55)
    *(_T56 + 0) = _T53
    _T57 = 0
    _T58 = *(_T27 - 4)
    _T59 = (_T57 < _T58)
    if (_T59 == 0) branch _L24
    _T60 = 0
    _T61 = (_T57 < _T60)
    if (_T61 == 0) branch _L25
_L24:
    _T62 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T62
    call _PrintString
    call _Halt
_L25:
    _T63 = 4
    _T64 = (_T57 * _T63)
    _T65 = (_T27 + _T64)
    _T66 = *(_T65 + 0)
    _T67 = *(_T27 - 4)
    _T68 = (_T66 < _T67)
    if (_T68 == 0) branch _L26
    _T69 = 0
    _T70 = (_T66 < _T69)
    if (_T70 == 0) branch _L27
_L26:
    _T71 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T71
    call _PrintString
    call _Halt
_L27:
    _T72 = 4
    _T73 = (_T66 * _T72)
    _T74 = (_T27 + _T73)
    _T75 = *(_T74 + 0)
    parm _T75
    call _PrintInt
    _T76 = "\n"
    parm _T76
    call _PrintString
    _T77 = *(_T27 - 4)
    parm _T77
    call _PrintInt
    _T78 = "\n"
    parm _T78
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T79 =  call _Main_New
    parm _T79
    _T80 = *(_T79 + 0)
    _T81 = *(_T80 + 12)
    call _T81
}

