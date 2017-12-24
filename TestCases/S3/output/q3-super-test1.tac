VTABLE(_Computer) {
    <empty>
    Computer
    _Computer.Crash;
}

VTABLE(_Mac) {
    _Computer
    Mac
    _Mac.Crash;
    _Mac.add;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Computer_New) {
memo ''
_Computer_New:
    _T6 = 8
    parm _T6
    _T7 =  call _Alloc
    _T8 = 0
    *(_T7 + 4) = _T8
    _T9 = VTBL <_Computer>
    *(_T7 + 0) = _T9
    return _T7
}

FUNCTION(_Mac_New) {
memo ''
_Mac_New:
    _T10 = 12
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    *(_T11 + 8) = _T12
    _T13 = VTBL <_Mac>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T14 = 4
    parm _T14
    _T15 =  call _Alloc
    _T16 = VTBL <_Main>
    *(_T15 + 0) = _T16
    return _T15
}

FUNCTION(_Computer.Crash) {
memo '_T0:4 _T1:8'
_Computer.Crash:
    _T18 = 0
    _T17 = _T18
    branch _L15
_L16:
    _T19 = 1
    _T20 = (_T17 + _T19)
    _T17 = _T20
_L15:
    _T21 = (_T17 < _T1)
    if (_T21 == 0) branch _L17
    _T22 = "sad\n"
    parm _T22
    call _PrintString
    branch _L16
_L17:
}

FUNCTION(_Mac.add) {
memo '_T2:4 _T3:8'
_Mac.add:
    parm _T2
    parm _T3
    _T23 = VTBL <_Computer>
    _T24 = *(_T23 + 8)
    call _T24
    _T25 = "ack!"
    parm _T25
    call _PrintString
}

FUNCTION(_Mac.Crash) {
memo '_T4:4 _T5:8'
_Mac.Crash:
    parm _T4
    parm _T5
    _T26 = VTBL <_Mac>
    _T27 = *(_T26 + 12)
    call _T27
    _T28 = "ack!"
    parm _T28
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T30 =  call _Mac_New
    _T29 = _T30
    _T31 = 2
    parm _T29
    parm _T31
    _T32 = *(_T29 + 0)
    _T33 = *(_T32 + 8)
    call _T33
}

