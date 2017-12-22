VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = VTBL <_Main>
    *(_T4 + 0) = _T5
    return _T4
}

FUNCTION(_Main.Binky) {
memo '_T0:4 _T1:8 _T2:12'
_Main.Binky:
    _T6 = 0
    _T7 = *(_T2 - 4)
    _T8 = (_T6 < _T7)
    if (_T8 == 0) branch _L11
    _T9 = 0
    _T10 = (_T6 < _T9)
    if (_T10 == 0) branch _L12
_L11:
    _T11 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T11
    call _PrintString
    call _Halt
_L12:
    _T12 = 4
    _T13 = (_T6 * _T12)
    _T14 = (_T2 + _T13)
    _T15 = *(_T14 + 0)
    _T16 = *(_T1 - 4)
    _T17 = (_T15 < _T16)
    if (_T17 == 0) branch _L13
    _T18 = 0
    _T19 = (_T15 < _T18)
    if (_T19 == 0) branch _L14
_L13:
    _T20 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T20
    call _PrintString
    call _Halt
_L14:
    _T21 = 4
    _T22 = (_T15 * _T21)
    _T23 = (_T1 + _T22)
    _T24 = *(_T23 + 0)
    return _T24
}

FUNCTION(main) {
memo ''
main:
    _T27 = 5
    _T28 = 0
    _T29 = (_T27 < _T28)
    if (_T29 == 0) branch _L15
    _T30 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T30
    call _PrintString
    call _Halt
_L15:
    _T31 = 4
    _T32 = (_T31 * _T27)
    _T33 = (_T31 + _T32)
    parm _T33
    _T34 =  call _Alloc
    *(_T34 + 0) = _T27
    _T35 = 0
    _T34 = (_T34 + _T33)
_L16:
    _T33 = (_T33 - _T31)
    if (_T33 == 0) branch _L17
    _T34 = (_T34 - _T31)
    *(_T34 + 0) = _T35
    branch _L16
_L17:
    _T26 = _T34
    _T36 = 0
    _T37 = *(_T26 - 4)
    _T38 = (_T36 < _T37)
    if (_T38 == 0) branch _L18
    _T39 = 0
    _T40 = (_T36 < _T39)
    if (_T40 == 0) branch _L19
_L18:
    _T41 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T41
    call _PrintString
    call _Halt
_L19:
    _T42 = 4
    _T43 = (_T36 * _T42)
    _T44 = (_T26 + _T43)
    _T45 = *(_T44 + 0)
    _T46 = 12
    _T47 = 0
    _T48 = (_T46 < _T47)
    if (_T48 == 0) branch _L20
    _T49 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T49
    call _PrintString
    call _Halt
_L20:
    _T50 = 4
    _T51 = (_T50 * _T46)
    _T52 = (_T50 + _T51)
    parm _T52
    _T53 =  call _Alloc
    *(_T53 + 0) = _T46
    _T54 = 0
    _T53 = (_T53 + _T52)
_L21:
    _T52 = (_T52 - _T50)
    if (_T52 == 0) branch _L22
    _T53 = (_T53 - _T50)
    *(_T53 + 0) = _T54
    branch _L21
_L22:
    _T55 = 4
    _T56 = (_T36 * _T55)
    _T57 = (_T26 + _T56)
    *(_T57 + 0) = _T53
    _T58 = 10
    _T59 = 0
    _T60 = (_T58 < _T59)
    if (_T60 == 0) branch _L23
    _T61 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T61
    call _PrintString
    call _Halt
_L23:
    _T62 = 4
    _T63 = (_T62 * _T58)
    _T64 = (_T62 + _T63)
    parm _T64
    _T65 =  call _Alloc
    *(_T65 + 0) = _T58
    _T66 = 0
    _T65 = (_T65 + _T64)
_L24:
    _T64 = (_T64 - _T62)
    if (_T64 == 0) branch _L25
    _T65 = (_T65 - _T62)
    *(_T65 + 0) = _T66
    branch _L24
_L25:
    _T25 = _T65
    _T67 = 0
    _T68 = *(_T25 - 4)
    _T69 = (_T67 < _T68)
    if (_T69 == 0) branch _L26
    _T70 = 0
    _T71 = (_T67 < _T70)
    if (_T71 == 0) branch _L27
_L26:
    _T72 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T72
    call _PrintString
    call _Halt
_L27:
    _T73 = 4
    _T74 = (_T67 * _T73)
    _T75 = (_T25 + _T74)
    _T76 = *(_T75 + 0)
    _T77 = 4
    _T78 = 5
    _T79 = 3
    _T80 = (_T78 * _T79)
    _T81 = 4
    if (_T81 != 0) branch _L28
    _T82 = "Decaf runtime error: Division by zero error.\n"
    parm _T82
    call _PrintString
    call _Halt
_L28:
    _T83 = (_T80 / _T81)
    _T84 = 2
    if (_T84 != 0) branch _L29
    _T85 = "Decaf runtime error: Division by zero error.\n"
    parm _T85
    call _PrintString
    call _Halt
_L29:
    _T86 = (_T83 % _T84)
    _T87 = (_T77 + _T86)
    _T88 = 4
    _T89 = (_T67 * _T88)
    _T90 = (_T25 + _T89)
    *(_T90 + 0) = _T87
    _T91 = 0
    _T92 = *(_T26 - 4)
    _T93 = (_T91 < _T92)
    if (_T93 == 0) branch _L30
    _T94 = 0
    _T95 = (_T91 < _T94)
    if (_T95 == 0) branch _L31
_L30:
    _T96 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T96
    call _PrintString
    call _Halt
_L31:
    _T97 = 4
    _T98 = (_T91 * _T97)
    _T99 = (_T26 + _T98)
    _T100 = *(_T99 + 0)
    _T101 = 0
    _T102 = *(_T25 - 4)
    _T103 = (_T101 < _T102)
    if (_T103 == 0) branch _L32
    _T104 = 0
    _T105 = (_T101 < _T104)
    if (_T105 == 0) branch _L33
_L32:
    _T106 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T106
    call _PrintString
    call _Halt
_L33:
    _T107 = 4
    _T108 = (_T101 * _T107)
    _T109 = (_T25 + _T108)
    _T110 = *(_T109 + 0)
    _T111 = *(_T100 - 4)
    _T112 = (_T110 < _T111)
    if (_T112 == 0) branch _L34
    _T113 = 0
    _T114 = (_T110 < _T113)
    if (_T114 == 0) branch _L35
_L34:
    _T115 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T115
    call _PrintString
    call _Halt
_L35:
    _T116 = 4
    _T117 = (_T110 * _T116)
    _T118 = (_T100 + _T117)
    _T119 = *(_T118 + 0)
    _T120 = 55
    _T121 = 4
    _T122 = (_T110 * _T121)
    _T123 = (_T100 + _T122)
    *(_T123 + 0) = _T120
    _T124 = 0
    _T125 = *(_T25 - 4)
    _T126 = (_T124 < _T125)
    if (_T126 == 0) branch _L36
    _T127 = 0
    _T128 = (_T124 < _T127)
    if (_T128 == 0) branch _L37
_L36:
    _T129 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T129
    call _PrintString
    call _Halt
_L37:
    _T130 = 4
    _T131 = (_T124 * _T130)
    _T132 = (_T25 + _T131)
    _T133 = *(_T132 + 0)
    parm _T133
    call _PrintInt
    _T134 = " "
    parm _T134
    call _PrintString
    _T135 = 2
    _T136 = 100
    _T137 = 0
    _T138 = *(_T26 - 4)
    _T139 = (_T137 < _T138)
    if (_T139 == 0) branch _L38
    _T140 = 0
    _T141 = (_T137 < _T140)
    if (_T141 == 0) branch _L39
_L38:
    _T142 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T142
    call _PrintString
    call _Halt
_L39:
    _T143 = 4
    _T144 = (_T137 * _T143)
    _T145 = (_T26 + _T144)
    _T146 = *(_T145 + 0)
    parm _T136
    parm _T146
    parm _T25
    _T147 =  call _Main.Binky
    _T148 = (_T135 * _T147)
    parm _T148
    call _PrintInt
}

