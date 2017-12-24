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
    _T8 = 1
    _T5 = _T8
    _T9 = "wow!"
    _T4 = _T9
    _T10 = 3
    _T3 = _T10
    _T11 = 1
    _T12 = 0
    _T13 = 3
    _T14 = _T11
    _T15 = 0
    _T16 = (_T14 + _T12)
    _T17 = (_T15 + _T13)
    _T6 = _T16
    _T7 = _T17
    if (_T5 == 0) branch _L10
    _T18 = 5
    _T19 = (_T3 * _T18)
    _T3 = _T19
_L10:
    parm _T5
    call _PrintBool
    _T20 = " "
    parm _T20
    call _PrintString
    parm _T3
    call _PrintInt
}

