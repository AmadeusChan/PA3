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
    _T14 = 1
    _T9 = _T14
    parm _T9
    call _PrintInt
    _T15 = "\n"
    parm _T15
    call _PrintString
    _T16 = 3
    _T17 = 0
    _T18 = 12
    _T19 = _T16
    _T20 = 0
    _T21 = (_T19 + _T17)
    _T22 = (_T20 + _T18)
    _T3 = _T21
    _T4 = _T22
    parm _T3
    call _PrintInt
    _T23 = "+"
    parm _T23
    call _PrintString
    parm _T4
    call _PrintInt
    _T24 = "j"
    parm _T24
    call _PrintString
    _T25 = "\n"
    parm _T25
    call _PrintString
    _T26 = 3
    _T27 = 0
    _T28 = 45
    _T29 = _T26
    _T30 = 0
    _T31 = (_T29 + _T27)
    _T32 = (_T30 + _T28)
    _T7 = _T31
    _T8 = _T32
    _T33 = _T3
    _T10 = _T33
    _T34 = _T4
    _T11 = _T34
    parm _T10
    call _PrintInt
    parm _T11
    call _PrintInt
    _T35 = "\n"
    parm _T35
    call _PrintString
    _T36 = (_T10 + _T11)
    _T37 = _T36
    _T38 = 0
    _T5 = _T37
    _T6 = _T38
    parm _T5
    call _PrintInt
    _T39 = "+"
    parm _T39
    call _PrintString
    parm _T6
    call _PrintInt
    _T40 = "j"
    parm _T40
    call _PrintString
    _T41 = "\n"
    parm _T41
    call _PrintString
    _T42 = (_T3 + _T5)
    _T43 = (_T4 + _T6)
    parm _T42
    call _PrintInt
    _T44 = "+"
    parm _T44
    call _PrintString
    parm _T43
    call _PrintInt
    _T45 = "j"
    parm _T45
    call _PrintString
    _T46 = "\n"
    parm _T46
    call _PrintString
    _T47 = (_T3 + _T5)
    _T48 = (_T4 + _T6)
    parm _T47
    call _PrintInt
    _T49 = "+"
    parm _T49
    call _PrintString
    parm _T48
    call _PrintInt
    _T50 = "j"
    parm _T50
    call _PrintString
    parm _T7
    call _PrintInt
    _T51 = "+"
    parm _T51
    call _PrintString
    parm _T8
    call _PrintInt
    _T52 = "j"
    parm _T52
    call _PrintString
    _T53 = "\n"
    parm _T53
    call _PrintString
    _T54 = (_T3 + _T5)
    _T55 = (_T4 + _T6)
    _T7 = _T54
    _T8 = _T55
    _T56 = _T10
    _T57 = 0
    _T58 = (_T3 + _T56)
    _T59 = (_T4 + _T57)
    _T7 = _T58
    _T8 = _T59
    _T60 = 0
    _T61 = 0
    _T62 = (_T3 + _T60)
    _T63 = (_T4 + _T61)
    _T7 = _T62
    _T8 = _T63
    _T64 = 0
    _T65 = 0
    _T66 = _T10
    _T67 = 0
    _T68 = (_T64 + _T66)
    _T69 = (_T65 + _T67)
    _T7 = _T68
    _T8 = _T69
    _T70 = 4
    _T71 = (_T70 + _T10)
    _T13 = _T71
    parm _T13
    call _PrintInt
    _T72 = "\n"
    parm _T72
    call _PrintString
    parm _T7
    call _PrintInt
    _T73 = "+"
    parm _T73
    call _PrintString
    parm _T8
    call _PrintInt
    _T74 = "j"
    parm _T74
    call _PrintString
    _T75 = "\n"
    parm _T75
    call _PrintString
    _T76 = (_T3 * _T5)
    _T78 = (_T4 * _T6)
    _T76 = (_T76 - _T78)
    _T77 = (_T3 * _T6)
    _T78 = (_T4 * _T5)
    _T77 = (_T77 + _T78)
    _T7 = _T76
    _T8 = _T77
    _T79 = _T10
    _T80 = 0
    _T81 = (_T3 * _T79)
    _T83 = (_T4 * _T80)
    _T81 = (_T81 - _T83)
    _T82 = (_T3 * _T80)
    _T83 = (_T4 * _T79)
    _T82 = (_T82 + _T83)
    _T7 = _T81
    _T8 = _T82
    _T84 = 0
    _T85 = 0
    _T86 = (_T3 * _T84)
    _T88 = (_T4 * _T85)
    _T86 = (_T86 - _T88)
    _T87 = (_T3 * _T85)
    _T88 = (_T4 * _T84)
    _T87 = (_T87 + _T88)
    _T7 = _T86
    _T8 = _T87
    _T89 = 0
    _T90 = 0
    _T91 = _T10
    _T92 = 0
    _T93 = (_T89 * _T91)
    _T95 = (_T90 * _T92)
    _T93 = (_T93 - _T95)
    _T94 = (_T89 * _T92)
    _T95 = (_T90 * _T91)
    _T94 = (_T94 + _T95)
    _T7 = _T93
    _T8 = _T94
    _T96 = 4
    _T97 = (_T96 * _T10)
    _T13 = _T97
    parm _T13
    call _PrintInt
    _T98 = "\n"
    parm _T98
    call _PrintString
    parm _T7
    call _PrintInt
    _T99 = "+"
    parm _T99
    call _PrintString
    parm _T8
    call _PrintInt
    _T100 = "j"
    parm _T100
    call _PrintString
    _T101 = "\n"
    parm _T101
    call _PrintString
}

