VTABLE(_Test) {
    <empty>
    Test
    _Test.go;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Test_New) {
memo ''
_Test_New:
    _T1 = 12
    parm _T1
    _T2 =  call _Alloc
    _T3 = 0
    *(_T2 + 4) = _T3
    *(_T2 + 8) = _T3
    _T4 = VTBL <_Test>
    *(_T2 + 0) = _T4
    return _T2
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T5 = 4
    parm _T5
    _T6 =  call _Alloc
    _T7 = VTBL <_Main>
    *(_T6 + 0) = _T7
    return _T6
}

FUNCTION(_Test.go) {
memo '_T0:4'
_Test.go:
    _T8 = *(_T0 + 4)
    _T9 = *(_T0 + 8)
    _T10 = 1
    _T11 = 0
    _T12 = 3
    _T13 = _T10
    _T14 = 0
    _T15 = (_T13 + _T11)
    _T16 = (_T14 + _T12)
    *(_T0 + 4) = _T15
    *(_T0 + 8) = _T16
    _T17 = *(_T0 + 4)
    _T18 = *(_T0 + 8)
    parm _T17
    call _PrintInt
    _T19 = "+"
    parm _T19
    call _PrintString
    parm _T18
    call _PrintInt
    _T20 = "j"
    parm _T20
    call _PrintString
    _T21 = "\n"
    parm _T21
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T23 =  call _Test_New
    _T22 = _T23
    parm _T22
    _T24 = *(_T22 + 0)
    _T25 = *(_T24 + 8)
    call _T25
}

