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
    _T4 = 0
    _T3 = _T4
_L10:
    _T5 = 2
    _T6 = (_T3 < _T5)
    if (_T6 == 0) branch _L13
_L12:
    _T7 = 1
    _T8 = (_T3 + _T7)
    _T3 = _T8
    branch _L10
_L13:
    _T9 = 4
    _T10 = (_T3 < _T9)
    if (_T10 == 0) branch _L15
_L14:
    _T11 = 3
    _T12 = (_T3 + _T11)
    _T3 = _T12
    branch _L10
_L15:
_L11:
    parm _T3
    call _PrintInt
    _T13 = "\n"
    parm _T13
    call _PrintString
}

