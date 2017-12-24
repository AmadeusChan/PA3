VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.fun;
    _B.setB;
}

VTABLE(_C) {
    _A
    C
    _A.setA;
    _C.print;
    _C.fun;
    _C.setC;
}

VTABLE(_D) {
    _B
    D
    _A.setA;
    _D.print;
    _D.fun;
    _B.setB;
    _D.setD;
}

VTABLE(_E) {
    _C
    E
    _A.setA;
    _E.print;
    _E.fun;
    _C.setC;
    _E.setE;
}

VTABLE(_F) {
    _E
    F
    _A.setA;
    _F.print;
    _F.fun;
    _C.setC;
    _E.setE;
    _F.setF;
}

VTABLE(_G) {
    _C
    G
    _A.setA;
    _G.print;
    _G.fun;
    _C.setC;
    _G.setG;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T34 = 12
    parm _T34
    _T35 =  call _Alloc
    _T36 = 0
    *(_T35 + 4) = _T36
    *(_T35 + 8) = _T36
    _T37 = VTBL <_A>
    *(_T35 + 0) = _T37
    return _T35
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T38 = 20
    parm _T38
    _T39 =  call _Alloc
    _T40 = 0
    *(_T39 + 4) = _T40
    *(_T39 + 8) = _T40
    *(_T39 + 12) = _T40
    *(_T39 + 16) = _T40
    _T41 = VTBL <_B>
    *(_T39 + 0) = _T41
    return _T39
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T42 = 20
    parm _T42
    _T43 =  call _Alloc
    _T44 = 0
    *(_T43 + 4) = _T44
    *(_T43 + 8) = _T44
    *(_T43 + 12) = _T44
    *(_T43 + 16) = _T44
    _T45 = VTBL <_C>
    *(_T43 + 0) = _T45
    return _T43
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T46 = 28
    parm _T46
    _T47 =  call _Alloc
    _T48 = 0
    _T49 = 4
    _T50 = (_T47 + _T46)
_L34:
    _T51 = (_T50 - _T49)
    _T50 = _T51
    _T52 = (_T46 - _T49)
    _T46 = _T52
    if (_T46 == 0) branch _L35
    *(_T50 + 0) = _T48
    branch _L34
_L35:
    _T53 = VTBL <_D>
    *(_T50 + 0) = _T53
    return _T50
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T54 = 28
    parm _T54
    _T55 =  call _Alloc
    _T56 = 0
    _T57 = 4
    _T58 = (_T55 + _T54)
_L37:
    _T59 = (_T58 - _T57)
    _T58 = _T59
    _T60 = (_T54 - _T57)
    _T54 = _T60
    if (_T54 == 0) branch _L38
    *(_T58 + 0) = _T56
    branch _L37
_L38:
    _T61 = VTBL <_E>
    *(_T58 + 0) = _T61
    return _T58
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T62 = 36
    parm _T62
    _T63 =  call _Alloc
    _T64 = 0
    _T65 = 4
    _T66 = (_T63 + _T62)
_L40:
    _T67 = (_T66 - _T65)
    _T66 = _T67
    _T68 = (_T62 - _T65)
    _T62 = _T68
    if (_T62 == 0) branch _L41
    *(_T66 + 0) = _T64
    branch _L40
_L41:
    _T69 = VTBL <_F>
    *(_T66 + 0) = _T69
    return _T66
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T70 = 24
    parm _T70
    _T71 =  call _Alloc
    _T72 = 0
    _T73 = 4
    _T74 = (_T71 + _T70)
_L43:
    _T75 = (_T74 - _T73)
    _T74 = _T75
    _T76 = (_T70 - _T73)
    _T70 = _T76
    if (_T70 == 0) branch _L44
    *(_T74 + 0) = _T72
    branch _L43
_L44:
    _T77 = VTBL <_G>
    *(_T74 + 0) = _T77
    return _T74
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T78 = 4
    parm _T78
    _T79 =  call _Alloc
    _T80 = VTBL <_Main>
    *(_T79 + 0) = _T80
    return _T79
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T81 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T82 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T83 = " a="
    parm _T83
    call _PrintString
    _T84 = *(_T3 + 4)
    parm _T84
    call _PrintInt
    _T85 = " a1="
    parm _T85
    call _PrintString
    _T86 = *(_T3 + 8)
    parm _T86
    call _PrintInt
    _T87 = " "
    parm _T87
    call _PrintString
}

FUNCTION(_A.fun) {
memo '_T4:4'
_A.fun:
    _T88 = "A"
    parm _T88
    call _PrintString
    parm _T4
    _T89 = VTBL <_A>
    _T90 = *(_T89 + 12)
    call _T90
    _T91 = "\n"
    parm _T91
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T5:4 _T6:8 _T7:12'
_B.setB:
    _T92 = *(_T5 + 12)
    *(_T5 + 12) = _T6
    _T93 = *(_T5 + 16)
    *(_T5 + 16) = _T7
}

FUNCTION(_B.print) {
memo '_T8:4'
_B.print:
    _T94 = " b="
    parm _T94
    call _PrintString
    _T95 = *(_T8 + 12)
    parm _T95
    call _PrintInt
    _T96 = " b1="
    parm _T96
    call _PrintString
    _T97 = *(_T8 + 16)
    parm _T97
    call _PrintInt
    _T98 = " "
    parm _T98
    call _PrintString
}

FUNCTION(_B.fun) {
memo '_T9:4'
_B.fun:
    _T99 = "B"
    parm _T99
    call _PrintString
    parm _T9
    _T100 = VTBL <_A>
    _T101 = *(_T100 + 12)
    call _T101
    parm _T9
    _T102 = VTBL <_B>
    _T103 = *(_T102 + 12)
    call _T103
    _T104 = "\n"
    parm _T104
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T10:4 _T11:8 _T12:12'
_C.setC:
    _T105 = *(_T10 + 12)
    *(_T10 + 12) = _T11
    _T106 = *(_T10 + 16)
    *(_T10 + 16) = _T12
}

FUNCTION(_C.print) {
memo '_T13:4'
_C.print:
    _T107 = " c="
    parm _T107
    call _PrintString
    _T108 = *(_T13 + 12)
    parm _T108
    call _PrintInt
    _T109 = " c1="
    parm _T109
    call _PrintString
    _T110 = *(_T13 + 16)
    parm _T110
    call _PrintInt
    _T111 = " "
    parm _T111
    call _PrintString
}

FUNCTION(_C.fun) {
memo '_T14:4'
_C.fun:
    _T112 = "C"
    parm _T112
    call _PrintString
    parm _T14
    _T113 = VTBL <_A>
    _T114 = *(_T113 + 12)
    call _T114
    parm _T14
    _T115 = VTBL <_C>
    _T116 = *(_T115 + 12)
    call _T116
    _T117 = "\n"
    parm _T117
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T15:4 _T16:8 _T17:12'
_D.setD:
    _T118 = *(_T15 + 20)
    *(_T15 + 20) = _T16
    _T119 = *(_T15 + 24)
    *(_T15 + 24) = _T17
}

FUNCTION(_D.print) {
memo '_T18:4'
_D.print:
    _T120 = " d="
    parm _T120
    call _PrintString
    _T121 = *(_T18 + 20)
    parm _T121
    call _PrintInt
    _T122 = " d1="
    parm _T122
    call _PrintString
    _T123 = *(_T18 + 24)
    parm _T123
    call _PrintInt
    _T124 = " "
    parm _T124
    call _PrintString
}

FUNCTION(_D.fun) {
memo '_T19:4'
_D.fun:
    _T125 = "D"
    parm _T125
    call _PrintString
    parm _T19
    _T126 = VTBL <_B>
    _T127 = *(_T126 + 12)
    call _T127
    parm _T19
    _T128 = VTBL <_D>
    _T129 = *(_T128 + 12)
    call _T129
    _T130 = "\n"
    parm _T130
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T20:4 _T21:8 _T22:12'
_E.setE:
    _T131 = *(_T20 + 20)
    *(_T20 + 20) = _T21
    _T132 = *(_T20 + 24)
    *(_T20 + 24) = _T22
}

FUNCTION(_E.print) {
memo '_T23:4'
_E.print:
    _T133 = " e="
    parm _T133
    call _PrintString
    _T134 = *(_T23 + 20)
    parm _T134
    call _PrintInt
    _T135 = " e1="
    parm _T135
    call _PrintString
    _T136 = *(_T23 + 24)
    parm _T136
    call _PrintInt
    _T137 = " "
    parm _T137
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T24:4'
_E.fun:
    _T138 = "E"
    parm _T138
    call _PrintString
    parm _T24
    _T139 = VTBL <_C>
    _T140 = *(_T139 + 12)
    call _T140
    parm _T24
    _T141 = VTBL <_E>
    _T142 = *(_T141 + 12)
    call _T142
    _T143 = "\n"
    parm _T143
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T25:4 _T26:8 _T27:12'
_F.setF:
    _T144 = *(_T25 + 28)
    *(_T25 + 28) = _T26
    _T145 = *(_T25 + 32)
    *(_T25 + 32) = _T27
}

FUNCTION(_F.print) {
memo '_T28:4'
_F.print:
    _T146 = " f="
    parm _T146
    call _PrintString
    _T147 = *(_T28 + 28)
    parm _T147
    call _PrintInt
    _T148 = " f1="
    parm _T148
    call _PrintString
    _T149 = *(_T28 + 32)
    parm _T149
    call _PrintInt
    _T150 = " "
    parm _T150
    call _PrintString
}

FUNCTION(_F.fun) {
memo '_T29:4'
_F.fun:
    _T151 = "F"
    parm _T151
    call _PrintString
    parm _T29
    _T152 = VTBL <_E>
    _T153 = *(_T152 + 12)
    call _T153
    parm _T29
    _T154 = VTBL <_F>
    _T155 = *(_T154 + 12)
    call _T155
    _T156 = "\n"
    parm _T156
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T30:4 _T31:8'
_G.setG:
    _T157 = *(_T30 + 20)
    *(_T30 + 20) = _T31
}

FUNCTION(_G.print) {
memo '_T32:4'
_G.print:
    _T158 = " g="
    parm _T158
    call _PrintString
    _T159 = *(_T32 + 20)
    parm _T159
    call _PrintInt
}

FUNCTION(_G.fun) {
memo '_T33:4'
_G.fun:
    _T160 = "G"
    parm _T160
    call _PrintString
    parm _T33
    _T161 = VTBL <_C>
    _T162 = *(_T161 + 12)
    call _T162
    _T163 = "\n"
    parm _T163
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T171 =  call _A_New
    _T164 = _T171
    _T172 =  call _B_New
    _T165 = _T172
    _T173 =  call _C_New
    _T166 = _T173
    _T174 =  call _D_New
    _T167 = _T174
    _T175 =  call _E_New
    _T168 = _T175
    _T176 =  call _F_New
    _T169 = _T176
    _T177 =  call _G_New
    _T170 = _T177
    _T178 = 10
    _T179 = 11
    parm _T164
    parm _T178
    parm _T179
    _T180 = *(_T164 + 0)
    _T181 = *(_T180 + 8)
    call _T181
    _T182 = 20
    _T183 = 21
    parm _T165
    parm _T182
    parm _T183
    _T184 = *(_T165 + 0)
    _T185 = *(_T184 + 8)
    call _T185
    _T186 = 22
    _T187 = 23
    parm _T165
    parm _T186
    parm _T187
    _T188 = *(_T165 + 0)
    _T189 = *(_T188 + 20)
    call _T189
    _T190 = 30
    _T191 = 31
    parm _T166
    parm _T190
    parm _T191
    _T192 = *(_T166 + 0)
    _T193 = *(_T192 + 8)
    call _T193
    _T194 = 32
    _T195 = 33
    parm _T166
    parm _T194
    parm _T195
    _T196 = *(_T166 + 0)
    _T197 = *(_T196 + 20)
    call _T197
    _T198 = 40
    _T199 = 41
    parm _T167
    parm _T198
    parm _T199
    _T200 = *(_T167 + 0)
    _T201 = *(_T200 + 8)
    call _T201
    _T202 = 42
    _T203 = 43
    parm _T167
    parm _T202
    parm _T203
    _T204 = *(_T167 + 0)
    _T205 = *(_T204 + 20)
    call _T205
    _T206 = 44
    _T207 = 45
    parm _T167
    parm _T206
    parm _T207
    _T208 = *(_T167 + 0)
    _T209 = *(_T208 + 24)
    call _T209
    _T210 = 50
    _T211 = 51
    parm _T168
    parm _T210
    parm _T211
    _T212 = *(_T168 + 0)
    _T213 = *(_T212 + 8)
    call _T213
    _T214 = 52
    _T215 = 53
    parm _T168
    parm _T214
    parm _T215
    _T216 = *(_T168 + 0)
    _T217 = *(_T216 + 20)
    call _T217
    _T218 = 54
    _T219 = 55
    parm _T168
    parm _T218
    parm _T219
    _T220 = *(_T168 + 0)
    _T221 = *(_T220 + 24)
    call _T221
    _T222 = 60
    _T223 = 61
    parm _T169
    parm _T222
    parm _T223
    _T224 = *(_T169 + 0)
    _T225 = *(_T224 + 8)
    call _T225
    _T226 = 62
    _T227 = 63
    parm _T169
    parm _T226
    parm _T227
    _T228 = *(_T169 + 0)
    _T229 = *(_T228 + 20)
    call _T229
    _T230 = 64
    _T231 = 65
    parm _T169
    parm _T230
    parm _T231
    _T232 = *(_T169 + 0)
    _T233 = *(_T232 + 24)
    call _T233
    _T234 = 66
    _T235 = 67
    parm _T169
    parm _T234
    parm _T235
    _T236 = *(_T169 + 0)
    _T237 = *(_T236 + 28)
    call _T237
    _T238 = 70
    _T239 = 71
    parm _T170
    parm _T238
    parm _T239
    _T240 = *(_T170 + 0)
    _T241 = *(_T240 + 8)
    call _T241
    _T242 = 72
    _T243 = 73
    parm _T170
    parm _T242
    parm _T243
    _T244 = *(_T170 + 0)
    _T245 = *(_T244 + 20)
    call _T245
    _T246 = 74
    parm _T170
    parm _T246
    _T247 = *(_T170 + 0)
    _T248 = *(_T247 + 24)
    call _T248
    parm _T164
    _T249 = *(_T164 + 0)
    _T250 = *(_T249 + 16)
    call _T250
    parm _T165
    _T251 = *(_T165 + 0)
    _T252 = *(_T251 + 16)
    call _T252
    parm _T166
    _T253 = *(_T166 + 0)
    _T254 = *(_T253 + 16)
    call _T254
    parm _T167
    _T255 = *(_T167 + 0)
    _T256 = *(_T255 + 16)
    call _T256
    parm _T168
    _T257 = *(_T168 + 0)
    _T258 = *(_T257 + 16)
    call _T258
    parm _T169
    _T259 = *(_T169 + 0)
    _T260 = *(_T259 + 16)
    call _T260
    parm _T170
    _T261 = *(_T170 + 0)
    _T262 = *(_T261 + 16)
    call _T262
}

