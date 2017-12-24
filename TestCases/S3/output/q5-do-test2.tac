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
    _T6 = 0
    _T3 = _T6
    _T7 = 1
    _T4 = _T7
    _T8 = 2
    _T5 = _T8
_L10:
    _T9 = 0
    _T10 = (_T3 == _T9)
    if (_T10 == 0) branch _L13
_L12:
    _T11 = 8
    _T3 = _T11
    _T12 = _T3
    branch _L10
_L13:
    _T13 = (_T5 + _T3)
    _T14 = (_T13 == _T4)
    if (_T14 == 0) branch _L15
_L14:
    _T15 = 5
    _T16 = (_T5 + _T15)
    _T4 = _T16
    branch _L10
_L15:
    _T17 = 8
    _T18 = (_T3 == _T17)
    if (_T18 == 0) branch _L17
_L16:
    _T19 = 7
    _T3 = _T19
    _T20 = (_T3 + _T5)
    _T4 = _T20
    branch _L10
_L17:
_L11:
    parm _T3
    call _PrintInt
    parm _T4
    call _PrintInt
    parm _T5
    call _PrintInt
}

