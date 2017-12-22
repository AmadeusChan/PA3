VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T8 = 6
    _T3 = _T8
    _T9 = 2
    _T4 = _T9
    _T10 = 3
    _T5 = _T10
    _T11 = 3
    _T12 = (_T3 * _T11)
    _T14 = 0
    _T15 = (_T4 + _T5)
    _T13 = _T15
    _T16 = (_T14 - _T12)
    if (_T16 == 0) branch _L10
    _T17 = 3
    _T18 = 3
    _T19 = (_T4 + _T18)
    _T13 = _T19
    _T20 = (_T17 - _T12)
    if (_T20 == 0) branch _L10
    _T21 = 9
    _T22 = 2
    _T23 = (_T5 * _T22)
    _T24 = 6
    _T25 = (_T23 + _T24)
    _T13 = _T25
    _T26 = (_T21 - _T12)
    if (_T26 == 0) branch _L10
    _T27 = 100
    _T13 = _T27
_L10:
    _T4 = _T13
    parm _T4
    call _PrintInt
    _T28 = "\n"
    parm _T28
    call _PrintString
    _T29 = 3
    _T6 = _T29
    _T31 = 0
    _T32 = (_T4 + _T5)
    _T30 = _T32
    _T33 = (_T31 - _T6)
    if (_T33 == 0) branch _L11
    _T34 = 3
    _T35 = 3
    _T36 = (_T4 + _T35)
    _T30 = _T36
    _T37 = (_T34 - _T6)
    if (_T37 == 0) branch _L11
    _T38 = 6
    _T39 = 2
    _T40 = (_T5 * _T39)
    _T41 = 6
    _T42 = (_T40 + _T41)
    _T30 = _T42
    _T43 = (_T38 - _T6)
    if (_T43 == 0) branch _L11
    _T44 = 100
    _T30 = _T44
_L11:
    _T4 = _T30
    parm _T4
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
    _T47 = 0
    _T48 = (_T4 + _T5)
    _T46 = _T48
    _T49 = (_T47 - _T3)
    if (_T49 == 0) branch _L12
    _T50 = 3
    _T51 = 3
    _T52 = (_T4 + _T51)
    _T46 = _T52
    _T53 = (_T50 - _T3)
    if (_T53 == 0) branch _L12
    _T54 = 6
    _T55 = 2
    _T56 = (_T5 * _T55)
    _T57 = 6
    _T58 = (_T56 + _T57)
    _T46 = _T58
    _T59 = (_T54 - _T3)
    if (_T59 == 0) branch _L12
    _T60 = 100
    _T46 = _T60
_L12:
    _T4 = _T46
    parm _T4
    call _PrintInt
    _T61 = "\n"
    parm _T61
    call _PrintString
    _T62 = 6
    _T63 = (_T3 - _T62)
    _T65 = 0
    _T66 = (_T4 + _T5)
    _T64 = _T66
    _T67 = (_T65 - _T63)
    if (_T67 == 0) branch _L13
    _T68 = 3
    _T69 = 3
    _T70 = (_T4 + _T69)
    _T64 = _T70
    _T71 = (_T68 - _T63)
    if (_T71 == 0) branch _L13
    _T72 = 9
    _T73 = 2
    _T74 = (_T5 * _T73)
    _T75 = 6
    _T76 = (_T74 + _T75)
    _T64 = _T76
    _T77 = (_T72 - _T63)
    if (_T77 == 0) branch _L13
    _T78 = 100
    _T64 = _T78
_L13:
    _T4 = _T64
    parm _T4
    call _PrintInt
    _T79 = "\n"
    parm _T79
    call _PrintString
    _T81 = 0
    _T82 = (_T4 + _T5)
    _T80 = _T82
    _T83 = (_T81 - _T3)
    if (_T83 == 0) branch _L14
    _T84 = 3
    _T85 = 3
    _T86 = (_T4 + _T85)
    _T80 = _T86
    _T87 = (_T84 - _T3)
    if (_T87 == 0) branch _L14
    _T88 = 6
    _T89 = 2
    _T90 = (_T5 * _T89)
    _T91 = 6
    _T92 = (_T90 + _T91)
    _T80 = _T92
    _T93 = (_T88 - _T3)
    if (_T93 == 0) branch _L14
    _T94 = 100
    _T80 = _T94
_L14:
    _T95 = ! _T80
    _T7 = _T95
    _T96 = "\n"
    parm _T96
    call _PrintString
    _T98 = 8
    _T99 = (_T4 + _T5)
    _T97 = _T99
    _T100 = (_T98 - _T3)
    if (_T100 == 0) branch _L15
    _T101 = 3
    _T102 = (_T4 + _T3)
    _T97 = _T102
    _T103 = (_T101 - _T3)
    if (_T103 == 0) branch _L15
    _T104 = 0
    _T105 = 8
    _T97 = _T105
    _T106 = (_T104 - _T3)
    if (_T106 == 0) branch _L15
    _T107 = 100
    _T97 = _T107
_L15:
    _T108 = ! _T97
    _T7 = _T108
    _T109 = "\n"
    parm _T109
    call _PrintString
}

