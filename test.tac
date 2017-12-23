VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T2 = 4
    parm _T2
    _T3 =  call _Alloc
    _T4 = VTBL <_Main>
    *(_T3 + 0) = _T4
    return _T3
}

FUNCTION(_Main.Go) {
memo '_T0:4 _T1:8'
_Main.Go:
    _T5 = 1
    _T6 = _T5
    _T7 = 0
    _T8 = (_T0 + _T6)
    _T9 = (_T1 + _T7)
    _T10 = 0
    _T11 = 2
    _T12 = (_T8 + _T10)
    _T13 = (_T9 + _T11)
    parm _T12
    call _PrintInt
    _T14 = "+"
    parm _T14
    call _PrintString
    parm _T13
    call _PrintInt
    _T15 = "j"
    parm _T15
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T21 =  call _ReadInteger
    _T20 = _T21
    _T24 = 0
    _T25 = 1
    _T26 = 0
    _T27 = 1
    _T28 = _T25
    _T29 = 0
    _T30 = (_T28 + _T26)
    _T31 = (_T29 + _T27)
    _T22 = _T30
    _T23 = _T31
    _T32 = (_T24 - _T20)
    if (_T32 == 0) branch _L11
    _T33 = 1
    _T34 = 3
    _T35 = 0
    _T36 = 3
    _T37 = _T34
    _T38 = 0
    _T39 = (_T37 + _T35)
    _T40 = (_T38 + _T36)
    _T22 = _T39
    _T23 = _T40
    _T41 = (_T33 - _T20)
    if (_T41 == 0) branch _L11
    _T42 = 2
    _T43 = 0
    _T44 = 2
    _T45 = _T42
    _T46 = 0
    _T47 = (_T45 + _T43)
    _T48 = (_T46 + _T44)
    _T22 = _T47
    _T23 = _T48
_L11:
    _T18 = _T22
    _T19 = _T23
    parm _T18
    call _PrintInt
    _T49 = "+"
    parm _T49
    call _PrintString
    parm _T19
    call _PrintInt
    _T50 = "j"
    parm _T50
    call _PrintString
    _T51 = "\n"
    parm _T51
    call _PrintString
    parm _T18
    parm _T19
    call _Main.Go
}

