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
    _T24 =  call _people_New
    _T22 = _T24
    parm _T22
    _T25 = *(_T22 + 0)
    _T26 = *(_T25 + 16)
    call _T26
    _T27 =  call _people_New
    _T28 = 4
    _T29 = 8
    _T32 = (_T22 + _T28)
    _T30 = _T32
    _T33 = (_T27 + _T28)
    _T31 = _T33
    _T34 = *(_T30 + 0)
    *(_T31 + 0) = _T34
    _T35 = (_T30 + _T28)
    _T30 = _T35
    _T36 = (_T31 + _T28)
    _T31 = _T36
    _T37 = *(_T30 + 0)
    _T38 = *(_T30 + 4)
    *(_T31 + 0) = _T37
    *(_T31 + 4) = _T38
    _T39 = (_T30 + _T29)
    _T30 = _T39
    _T40 = (_T31 + _T29)
    _T31 = _T40
    _T41 = *(_T30 + 0)
    _T42 =  call _animal_New
    _T43 = 4
    _T44 = 8
    _T47 = (_T41 + _T43)
    _T45 = _T47
    _T48 = (_T42 + _T43)
    _T46 = _T48
    _T49 = *(_T45 + 0)
    *(_T46 + 0) = _T49
    _T50 = (_T45 + _T43)
    _T45 = _T50
    _T51 = (_T46 + _T43)
    _T46 = _T51
    _T52 = VTBL <_animal>
    *(_T42 + 0) = _T52
    *(_T31 + 0) = _T42
    _T53 = (_T30 + _T28)
    _T30 = _T53
    _T54 = (_T31 + _T28)
    _T31 = _T54
    _T55 = *(_T30 + 0)
    *(_T31 + 0) = _T55
    _T56 = (_T30 + _T28)
    _T30 = _T56
    _T57 = (_T31 + _T28)
    _T31 = _T57
    _T58 = VTBL <_people>
    *(_T27 + 0) = _T58
    _T23 = _T27
    _T59 = 99
    parm _T23
    parm _T59
    _T60 = *(_T23 + 0)
    _T61 = *(_T60 + 8)
    call _T61
    _T62 = "a: \n"
    parm _T62
    call _PrintString
    parm _T22
    _T63 = *(_T22 + 0)
    _T64 = *(_T63 + 12)
    call _T64
    _T65 = "b: \n"
    parm _T65
    call _PrintString
    parm _T23
    _T66 = *(_T23 + 0)
    _T67 = *(_T66 + 12)
    call _T67
}

FUNCTION(_animal.setage) {
memo '_T0:4 _T1:8'
_animal.setage:
    _T68 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_animal.getage) {
memo '_T2:4'
_animal.getage:
    _T69 = *(_T2 + 4)
    parm _T69
    call _PrintInt
    _T70 = "\n"
    parm _T70
    call _PrintString
}

FUNCTION(_people.setaniage) {
memo '_T3:4 _T4:8'
_people.setaniage:
    _T71 = *(_T3 + 16)
    parm _T71
    parm _T4
    _T72 = *(_T71 + 0)
    _T73 = *(_T72 + 8)
    call _T73
}

FUNCTION(_people.getage) {
memo '_T5:4'
_people.getage:
    _T74 = *(_T5 + 4)
    parm _T74
    call _PrintInt
    _T75 = "\n"
    parm _T75
    call _PrintString
    _T76 = *(_T5 + 8)
    _T77 = *(_T5 + 12)
    parm _T76
    call _PrintInt
    _T78 = "+"
    parm _T78
    call _PrintString
    parm _T77
    call _PrintInt
    _T79 = "j"
    parm _T79
    call _PrintString
    _T80 = "\n"
    parm _T80
    call _PrintString
    _T81 = *(_T5 + 16)
    parm _T81
    _T82 = *(_T81 + 0)
    _T83 = *(_T82 + 12)
    call _T83
    _T84 = *(_T5 + 20)
    parm _T84
    call _PrintString
    _T85 = "\n"
    parm _T85
    call _PrintString
}

FUNCTION(_people.setage) {
memo '_T6:4'
_people.setage:
    _T86 = *(_T6 + 16)
    _T87 =  call _animal_New
    *(_T6 + 16) = _T87
    _T88 = 100
    parm _T6
    parm _T88
    _T89 = VTBL <_people>
    _T90 = *(_T89 + 8)
    call _T90
    _T91 = *(_T6 + 4)
    _T92 = 10
    *(_T6 + 4) = _T92
    _T93 = *(_T6 + 20)
    _T94 = "11"
    *(_T6 + 20) = _T94
    _T95 = *(_T6 + 8)
    _T96 = *(_T6 + 12)
    _T97 = 89
    _T98 = 0
    _T99 = 8
    _T100 = _T97
    _T101 = 0
    _T102 = (_T100 + _T98)
    _T103 = (_T101 + _T99)
    *(_T6 + 8) = _T102
    *(_T6 + 12) = _T103
}

