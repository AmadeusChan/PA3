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
    _T4 =  call _ReadInteger
    _T3 = _T4
    _T7 = 0
    _T8 = 1
    _T6 = _T8
    _T9 = (_T7 - _T3)
    if (_T9 == 0) branch _L10
    _T10 = 1
    _T11 = 0
    _T6 = _T11
    _T12 = (_T10 - _T3)
    if (_T12 == 0) branch _L10
    _T13 = 3
    _T14 = 12
    _T6 = _T14
    _T15 = (_T13 - _T3)
    if (_T15 == 0) branch _L10
    _T16 = 2
    _T17 = 41
    _T6 = _T17
    _T18 = (_T16 - _T3)
    if (_T18 == 0) branch _L10
    _T19 = 10
    _T20 = (_T3 - _T19)
    _T6 = _T20
_L10:
    _T5 = _T6
    parm _T5
    call _PrintInt
    _T21 = "\n"
    parm _T21
    call _PrintString
    _T22 = 0
    if (_T22 != 0) branch _L11
    _T23 = "Decaf runtime error: Division by zero error.\n"
    parm _T23
    call _PrintString
    call _Halt
_L11:
    _T24 = (_T3 / _T22)
    _T5 = _T24
}

