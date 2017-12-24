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
    _T4 = 10
    _T3 = _T4
    _T6 = 10
    _T5 = _T6
_L10:
    _T7 = (_T3 + _T5)
    _T8 = 30
    _T9 = (_T7 > _T8)
    if (_T9 == 0) branch _L13
_L12:
    _T10 = "a+b>30"
    parm _T10
    call _PrintString
    branch _L10
_L13:
    _T11 = 20
    _T12 = (_T3 < _T11)
    if (_T12 == 0) branch _L15
_L14:
    _T13 = "a<20"
    parm _T13
    call _PrintString
    _T14 = 10
    _T15 = (_T3 + _T14)
    _T3 = _T15
    branch _L10
_L15:
    _T16 = 1
    if (_T16 == 0) branch _L17
_L16:
    _T17 = "true"
    parm _T17
    call _PrintString
    branch _L11
    branch _L10
_L17:
    _T18 = 10
    _T19 = (_T5 > _T18)
    if (_T19 == 0) branch _L19
_L18:
    _T20 = (_T3 + _T5)
    _T5 = _T20
    parm _T5
    call _PrintInt
    branch _L10
_L19:
_L11:
}

