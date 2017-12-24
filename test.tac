VTABLE(_A) {
    <empty>
    A
    _A.go;
    _A.exec;
}

VTABLE(_B) {
    _A
    B
    _B.go;
    _B.exec;
}

VTABLE(_C) {
    _B
    C
    _C.go;
    _C.exec;
    _C.hello;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T7 = 4
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_A>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T10 = 4
    parm _T10
    _T11 =  call _Alloc
    _T12 = VTBL <_B>
    *(_T11 + 0) = _T12
    return _T11
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T13 = 4
    parm _T13
    _T14 =  call _Alloc
    _T15 = VTBL <_C>
    *(_T14 + 0) = _T15
    return _T14
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T16 = 4
    parm _T16
    _T17 =  call _Alloc
    _T18 = VTBL <_Main>
    *(_T17 + 0) = _T18
    return _T17
}

FUNCTION(_A.go) {
memo '_T0:4'
_A.go:
    _T19 = "class A\n"
    parm _T19
    call _PrintString
}

FUNCTION(_A.exec) {
memo '_T1:4'
_A.exec:
    parm _T1
    _T20 = VTBL <_A>
    _T21 = *(_T20 + 8)
    call _T21
}

FUNCTION(_B.go) {
memo '_T2:4'
_B.go:
    _T22 = "class B\n"
    parm _T22
    call _PrintString
}

FUNCTION(_B.exec) {
memo '_T3:4'
_B.exec:
    parm _T3
    _T23 = VTBL <_B>
    _T24 = *(_T23 + 8)
    call _T24
}

FUNCTION(_C.go) {
memo '_T4:4'
_C.go:
    _T25 = "class B\n"
    parm _T25
    call _PrintString
}

FUNCTION(_C.hello) {
memo '_T5:4'
_C.hello:
    parm _T5
    _T26 = VTBL <_B>
    _T27 = *(_T26 + 12)
    call _T27
}

FUNCTION(_C.exec) {
memo '_T6:4'
_C.exec:
    parm _T6
    _T28 = VTBL <_C>
    _T29 = *(_T28 + 8)
    call _T29
}

FUNCTION(main) {
memo ''
main:
    _T31 =  call _C_New
    _T30 = _T31
    parm _T30
    _T32 = *(_T30 + 0)
    _T33 = *(_T32 + 16)
    call _T33
}

