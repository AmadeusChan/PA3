VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_animal) {
    <empty>
    animal
    _animal.setage;
    _animal.getage;
}

VTABLE(_people) {
    <empty>
    people
    _people.setaniage;
    _people.getage;
    _people.setage;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T7 = 4
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_Main>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_animal_New) {
memo ''
_animal_New:
    _T10 = 8
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    _T13 = VTBL <_animal>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_people_New) {
memo ''
_people_New:
    _T14 = 24
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    _T17 = 4
    _T18 = (_T15 + _T14)
_L17:
    _T19 = (_T18 - _T17)
    _T18 = _T19
    _T20 = (_T14 - _T17)
    _T14 = _T20
    if (_T14 == 0) branch _L18
    *(_T18 + 0) = _T16
    branch _L17
_L18:
    _T21 = VTBL <_people>
    *(_T18 + 0) = _T21
    return _T18
}

FUNCTION(main) {
memo ''
main:
    _T25 =  call _people_New
    _T23 = _T25
    parm _T23
    _T26 = *(_T23 + 0)
    _T27 = *(_T26 + 16)
    call _T27
    _T28 =  call _people_New
    _T29 = 24
    _T30 = 4
_L19:
    if (_T29 == 0) branch _L20
    _T31 = (_T29 - _T30)
    _T29 = _T31
    _T32 = (_T23 + _T29)
    _T33 = *(_T32 + 0)
    _T34 = (_T28 + _T29)
    *(_T34 + 0) = _T33
    branch _L19
_L20:
    _T35 = VTBL <_people>
    *(_T28 + 0) = _T35
    _T24 = _T28
    _T36 = 99
    parm _T24
    parm _T36
    _T37 = *(_T24 + 0)
    _T38 = *(_T37 + 8)
    call _T38
    _T39 = "a: \n"
    parm _T39
    call _PrintString
    parm _T23
    _T40 = *(_T23 + 0)
    _T41 = *(_T40 + 12)
    call _T41
    _T42 = "b: \n"
    parm _T42
    call _PrintString
    parm _T24
    _T43 = *(_T24 + 0)
    _T44 = *(_T43 + 12)
    call _T44
}

FUNCTION(_animal.setage) {
memo '_T0:4 _T1:8'
_animal.setage:
    _T45 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_animal.getage) {
memo '_T2:4'
_animal.getage:
    _T46 = *(_T2 + 4)
    parm _T46
    call _PrintInt
    _T47 = "\n"
    parm _T47
    call _PrintString
}

FUNCTION(_people.setaniage) {
memo '_T3:4 _T4:8'
_people.setaniage:
    _T48 = *(_T3 + 16)
    parm _T48
    parm _T4
    _T49 = *(_T48 + 0)
    _T50 = *(_T49 + 8)
    call _T50
}

FUNCTION(_people.getage) {
memo '_T5:4'
_people.getage:
    _T51 = *(_T5 + 4)
    parm _T51
    call _PrintInt
    _T52 = "\n"
    parm _T52
    call _PrintString
    _T53 = *(_T5 + 8)
    _T54 = *(_T5 + 12)
    parm _T53
    call _PrintInt
    _T55 = "+"
    parm _T55
    call _PrintString
    parm _T54
    call _PrintInt
    _T56 = "j"
    parm _T56
    call _PrintString
    _T57 = "\n"
    parm _T57
    call _PrintString
    _T58 = *(_T5 + 16)
    parm _T58
    _T59 = *(_T58 + 0)
    _T60 = *(_T59 + 12)
    call _T60
    _T61 = *(_T5 + 20)
    parm _T61
    call _PrintString
    _T62 = "\n"
    parm _T62
    call _PrintString
}

FUNCTION(_people.setage) {
memo '_T6:4'
_people.setage:
    _T63 = *(_T6 + 16)
    _T64 =  call _animal_New
    *(_T6 + 16) = _T64
    _T65 = 100
    parm _T6
    parm _T65
    _T66 = VTBL <_people>
    _T67 = *(_T66 + 8)
    call _T67
    _T68 = *(_T6 + 4)
    _T69 = 10
    *(_T6 + 4) = _T69
    _T70 = *(_T6 + 20)
    _T71 = "11"
    *(_T6 + 20) = _T71
    _T72 = *(_T6 + 8)
    _T73 = *(_T6 + 12)
    _T74 = 89
    _T75 = 0
    _T76 = 8
    _T77 = _T74
    _T78 = 0
    _T79 = (_T77 + _T75)
    _T80 = (_T78 + _T76)
    *(_T6 + 8) = _T79
    *(_T6 + 12) = _T80
}

