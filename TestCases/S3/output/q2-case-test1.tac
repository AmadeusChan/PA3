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
    _T4 = 2
    _T3 = _T4
    _T7 = 2
    _T5 = _T7
    _T8 = 3
    _T6 = _T8
    _T9 = 3
    _T10 = (_T3 * _T9)
    _T12 = 0
    _T13 = (_T5 + _T6)
    _T11 = _T13
    _T14 = (_T12 - _T10)
    if (_T14 == 0) branch _L10
    _T15 = 3
    _T16 = 3
    _T17 = (_T5 + _T16)
    _T11 = _T17
    _T18 = (_T15 - _T10)
    if (_T18 == 0) branch _L10
    _T19 = 6
    _T20 = 2
    _T21 = (_T6 * _T20)
    _T22 = 6
    _T23 = (_T21 + _T22)
    _T11 = _T23
    _T24 = (_T19 - _T10)
    if (_T24 == 0) branch _L10
    _T25 = 100
    _T11 = _T25
_L10:
    _T5 = _T11
    parm _T5
    call _PrintInt
}

