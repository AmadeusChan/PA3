VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.allprint;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.allprint;
    _B.fun;
    _B.setB;
}

VTABLE(_C) {
    _A
    C
    _A.setA;
    _C.print;
    _C.allprint;
    _C.fun;
    _C.setC;
}

VTABLE(_D) {
    _B
    D
    _A.setA;
    _D.print;
    _D.allprint;
    _D.fun;
    _B.setB;
    _D.setD;
}

VTABLE(_E) {
    _C
    E
    _A.setA;
    _E.print;
    _E.allprint;
    _E.fun;
    _C.setC;
    _E.setE;
}

VTABLE(_F) {
    _E
    F
    _A.setA;
    _F.print;
    _F.allprint;
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
    _G.allprint;
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
    _T41 = 12
    parm _T41
    _T42 =  call _Alloc
    _T43 = 0
    *(_T42 + 4) = _T43
    *(_T42 + 8) = _T43
    _T44 = VTBL <_A>
    *(_T42 + 0) = _T44
    return _T42
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T45 = 20
    parm _T45
    _T46 =  call _Alloc
    _T47 = 0
    *(_T46 + 4) = _T47
    *(_T46 + 8) = _T47
    *(_T46 + 12) = _T47
    *(_T46 + 16) = _T47
    _T48 = VTBL <_B>
    *(_T46 + 0) = _T48
    return _T46
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T49 = 20
    parm _T49
    _T50 =  call _Alloc
    _T51 = 0
    *(_T50 + 4) = _T51
    *(_T50 + 8) = _T51
    *(_T50 + 12) = _T51
    *(_T50 + 16) = _T51
    _T52 = VTBL <_C>
    *(_T50 + 0) = _T52
    return _T50
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T53 = 28
    parm _T53
    _T54 =  call _Alloc
    _T55 = 0
    _T56 = 4
    _T57 = (_T54 + _T53)
_L41:
    _T58 = (_T57 - _T56)
    _T57 = _T58
    _T59 = (_T53 - _T56)
    _T53 = _T59
    if (_T53 == 0) branch _L42
    *(_T57 + 0) = _T55
    branch _L41
_L42:
    _T60 = VTBL <_D>
    *(_T57 + 0) = _T60
    return _T57
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T61 = 28
    parm _T61
    _T62 =  call _Alloc
    _T63 = 0
    _T64 = 4
    _T65 = (_T62 + _T61)
_L44:
    _T66 = (_T65 - _T64)
    _T65 = _T66
    _T67 = (_T61 - _T64)
    _T61 = _T67
    if (_T61 == 0) branch _L45
    *(_T65 + 0) = _T63
    branch _L44
_L45:
    _T68 = VTBL <_E>
    *(_T65 + 0) = _T68
    return _T65
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T69 = 36
    parm _T69
    _T70 =  call _Alloc
    _T71 = 0
    _T72 = 4
    _T73 = (_T70 + _T69)
_L47:
    _T74 = (_T73 - _T72)
    _T73 = _T74
    _T75 = (_T69 - _T72)
    _T69 = _T75
    if (_T69 == 0) branch _L48
    *(_T73 + 0) = _T71
    branch _L47
_L48:
    _T76 = VTBL <_F>
    *(_T73 + 0) = _T76
    return _T73
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T77 = 24
    parm _T77
    _T78 =  call _Alloc
    _T79 = 0
    _T80 = 4
    _T81 = (_T78 + _T77)
_L50:
    _T82 = (_T81 - _T80)
    _T81 = _T82
    _T83 = (_T77 - _T80)
    _T77 = _T83
    if (_T77 == 0) branch _L51
    *(_T81 + 0) = _T79
    branch _L50
_L51:
    _T84 = VTBL <_G>
    *(_T81 + 0) = _T84
    return _T81
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T85 = 4
    parm _T85
    _T86 =  call _Alloc
    _T87 = VTBL <_Main>
    *(_T86 + 0) = _T87
    return _T86
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T88 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T89 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T90 = " a="
    parm _T90
    call _PrintString
    _T91 = *(_T3 + 4)
    parm _T91
    call _PrintInt
    _T92 = " a1="
    parm _T92
    call _PrintString
    _T93 = *(_T3 + 8)
    parm _T93
    call _PrintInt
    _T94 = " "
    parm _T94
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T95 = VTBL <_A>
    _T96 = *(_T95 + 12)
    call _T96
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T97 = "A"
    parm _T97
    call _PrintString
    parm _T5
    _T98 = VTBL <_A>
    _T99 = *(_T98 + 12)
    call _T99
    _T100 = "\n"
    parm _T100
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T101 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T102 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T103 = " b="
    parm _T103
    call _PrintString
    _T104 = *(_T9 + 12)
    parm _T104
    call _PrintInt
    _T105 = " b1="
    parm _T105
    call _PrintString
    _T106 = *(_T9 + 16)
    parm _T106
    call _PrintInt
    _T107 = " "
    parm _T107
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    parm _T10
    _T108 = VTBL <_A>
    _T109 = *(_T108 + 16)
    call _T109
    parm _T10
    _T110 = VTBL <_B>
    _T111 = *(_T110 + 12)
    call _T111
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T112 = "B"
    parm _T112
    call _PrintString
    parm _T11
    _T113 = VTBL <_A>
    _T114 = *(_T113 + 16)
    call _T114
    parm _T11
    _T115 = VTBL <_B>
    _T116 = *(_T115 + 12)
    call _T116
    _T117 = "\n"
    parm _T117
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T118 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T119 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T120 = " c="
    parm _T120
    call _PrintString
    _T121 = *(_T15 + 12)
    parm _T121
    call _PrintInt
    _T122 = " c1="
    parm _T122
    call _PrintString
    _T123 = *(_T15 + 16)
    parm _T123
    call _PrintInt
    _T124 = " "
    parm _T124
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T125 = VTBL <_A>
    _T126 = *(_T125 + 16)
    call _T126
    parm _T16
    _T127 = VTBL <_C>
    _T128 = *(_T127 + 12)
    call _T128
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T129 = "C"
    parm _T129
    call _PrintString
    parm _T17
    _T130 = VTBL <_A>
    _T131 = *(_T130 + 16)
    call _T131
    parm _T17
    _T132 = VTBL <_C>
    _T133 = *(_T132 + 12)
    call _T133
    _T134 = "\n"
    parm _T134
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T135 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T136 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T137 = " d="
    parm _T137
    call _PrintString
    _T138 = *(_T21 + 20)
    parm _T138
    call _PrintInt
    _T139 = " d1="
    parm _T139
    call _PrintString
    _T140 = *(_T21 + 24)
    parm _T140
    call _PrintInt
    _T141 = " "
    parm _T141
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    parm _T22
    _T142 = VTBL <_B>
    _T143 = *(_T142 + 16)
    call _T143
    parm _T22
    _T144 = VTBL <_D>
    _T145 = *(_T144 + 12)
    call _T145
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T146 = "D"
    parm _T146
    call _PrintString
    parm _T23
    _T147 = VTBL <_B>
    _T148 = *(_T147 + 16)
    call _T148
    parm _T23
    _T149 = VTBL <_D>
    _T150 = *(_T149 + 12)
    call _T150
    _T151 = "\n"
    parm _T151
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T152 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T153 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T154 = " e="
    parm _T154
    call _PrintString
    _T155 = *(_T27 + 20)
    parm _T155
    call _PrintInt
    _T156 = " e1="
    parm _T156
    call _PrintString
    _T157 = *(_T27 + 24)
    parm _T157
    call _PrintInt
    _T158 = " "
    parm _T158
    call _PrintString
}

FUNCTION(_E.allprint) {
memo '_T28:4'
_E.allprint:
    parm _T28
    _T159 = VTBL <_C>
    _T160 = *(_T159 + 16)
    call _T160
    parm _T28
    _T161 = VTBL <_E>
    _T162 = *(_T161 + 12)
    call _T162
}

FUNCTION(_E.fun) {
memo '_T29:4'
_E.fun:
    _T163 = "E"
    parm _T163
    call _PrintString
    parm _T29
    _T164 = VTBL <_C>
    _T165 = *(_T164 + 16)
    call _T165
    parm _T29
    _T166 = VTBL <_E>
    _T167 = *(_T166 + 12)
    call _T167
    _T168 = "\n"
    parm _T168
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T30:4 _T31:8 _T32:12'
_F.setF:
    _T169 = *(_T30 + 28)
    *(_T30 + 28) = _T31
    _T170 = *(_T30 + 32)
    *(_T30 + 32) = _T32
}

FUNCTION(_F.print) {
memo '_T33:4'
_F.print:
    _T171 = " f="
    parm _T171
    call _PrintString
    _T172 = *(_T33 + 28)
    parm _T172
    call _PrintInt
    _T173 = " f1="
    parm _T173
    call _PrintString
    _T174 = *(_T33 + 32)
    parm _T174
    call _PrintInt
    _T175 = " "
    parm _T175
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T34:4'
_F.allprint:
    parm _T34
    _T176 = VTBL <_E>
    _T177 = *(_T176 + 16)
    call _T177
    parm _T34
    _T178 = VTBL <_F>
    _T179 = *(_T178 + 12)
    call _T179
}

FUNCTION(_F.fun) {
memo '_T35:4'
_F.fun:
    _T180 = "F"
    parm _T180
    call _PrintString
    parm _T35
    _T181 = VTBL <_E>
    _T182 = *(_T181 + 16)
    call _T182
    parm _T35
    _T183 = VTBL <_F>
    _T184 = *(_T183 + 12)
    call _T184
    _T185 = "\n"
    parm _T185
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T36:4 _T37:8'
_G.setG:
    _T186 = *(_T36 + 20)
    *(_T36 + 20) = _T37
}

FUNCTION(_G.print) {
memo '_T38:4'
_G.print:
    _T187 = " g="
    parm _T187
    call _PrintString
    _T188 = *(_T38 + 20)
    parm _T188
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T39:4'
_G.allprint:
    parm _T39
    _T189 = VTBL <_C>
    _T190 = *(_T189 + 16)
    call _T190
    parm _T39
    _T191 = VTBL <_G>
    _T192 = *(_T191 + 12)
    call _T192
}

FUNCTION(_G.fun) {
memo '_T40:4'
_G.fun:
    _T193 = "G"
    parm _T193
    call _PrintString
    parm _T40
    _T194 = VTBL <_C>
    _T195 = *(_T194 + 16)
    call _T195
    parm _T40
    _T196 = VTBL <_G>
    _T197 = *(_T196 + 12)
    call _T197
    _T198 = "\n"
    parm _T198
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T206 =  call _A_New
    _T199 = _T206
    _T207 =  call _B_New
    _T200 = _T207
    _T208 =  call _C_New
    _T201 = _T208
    _T209 =  call _D_New
    _T202 = _T209
    _T210 =  call _E_New
    _T203 = _T210
    _T211 =  call _F_New
    _T204 = _T211
    _T212 =  call _G_New
    _T205 = _T212
    _T213 = 10
    _T214 = 11
    parm _T199
    parm _T213
    parm _T214
    _T215 = *(_T199 + 0)
    _T216 = *(_T215 + 8)
    call _T216
    _T217 = 20
    _T218 = 21
    parm _T200
    parm _T217
    parm _T218
    _T219 = *(_T200 + 0)
    _T220 = *(_T219 + 8)
    call _T220
    _T221 = 22
    _T222 = 23
    parm _T200
    parm _T221
    parm _T222
    _T223 = *(_T200 + 0)
    _T224 = *(_T223 + 24)
    call _T224
    _T225 = 30
    _T226 = 31
    parm _T201
    parm _T225
    parm _T226
    _T227 = *(_T201 + 0)
    _T228 = *(_T227 + 8)
    call _T228
    _T229 = 32
    _T230 = 33
    parm _T201
    parm _T229
    parm _T230
    _T231 = *(_T201 + 0)
    _T232 = *(_T231 + 24)
    call _T232
    _T233 = 40
    _T234 = 41
    parm _T202
    parm _T233
    parm _T234
    _T235 = *(_T202 + 0)
    _T236 = *(_T235 + 8)
    call _T236
    _T237 = 42
    _T238 = 43
    parm _T202
    parm _T237
    parm _T238
    _T239 = *(_T202 + 0)
    _T240 = *(_T239 + 24)
    call _T240
    _T241 = 44
    _T242 = 45
    parm _T202
    parm _T241
    parm _T242
    _T243 = *(_T202 + 0)
    _T244 = *(_T243 + 28)
    call _T244
    _T245 = 50
    _T246 = 51
    parm _T203
    parm _T245
    parm _T246
    _T247 = *(_T203 + 0)
    _T248 = *(_T247 + 8)
    call _T248
    _T249 = 52
    _T250 = 53
    parm _T203
    parm _T249
    parm _T250
    _T251 = *(_T203 + 0)
    _T252 = *(_T251 + 24)
    call _T252
    _T253 = 54
    _T254 = 55
    parm _T203
    parm _T253
    parm _T254
    _T255 = *(_T203 + 0)
    _T256 = *(_T255 + 28)
    call _T256
    _T257 = 60
    _T258 = 61
    parm _T204
    parm _T257
    parm _T258
    _T259 = *(_T204 + 0)
    _T260 = *(_T259 + 8)
    call _T260
    _T261 = 62
    _T262 = 63
    parm _T204
    parm _T261
    parm _T262
    _T263 = *(_T204 + 0)
    _T264 = *(_T263 + 24)
    call _T264
    _T265 = 64
    _T266 = 65
    parm _T204
    parm _T265
    parm _T266
    _T267 = *(_T204 + 0)
    _T268 = *(_T267 + 28)
    call _T268
    _T269 = 66
    _T270 = 67
    parm _T204
    parm _T269
    parm _T270
    _T271 = *(_T204 + 0)
    _T272 = *(_T271 + 32)
    call _T272
    _T273 = 70
    _T274 = 71
    parm _T205
    parm _T273
    parm _T274
    _T275 = *(_T205 + 0)
    _T276 = *(_T275 + 8)
    call _T276
    _T277 = 72
    _T278 = 73
    parm _T205
    parm _T277
    parm _T278
    _T279 = *(_T205 + 0)
    _T280 = *(_T279 + 24)
    call _T280
    _T281 = 74
    parm _T205
    parm _T281
    _T282 = *(_T205 + 0)
    _T283 = *(_T282 + 28)
    call _T283
    parm _T199
    _T284 = *(_T199 + 0)
    _T285 = *(_T284 + 20)
    call _T285
    parm _T200
    _T286 = *(_T200 + 0)
    _T287 = *(_T286 + 20)
    call _T287
    parm _T201
    _T288 = *(_T201 + 0)
    _T289 = *(_T288 + 20)
    call _T289
    parm _T202
    _T290 = *(_T202 + 0)
    _T291 = *(_T290 + 20)
    call _T291
    parm _T203
    _T292 = *(_T203 + 0)
    _T293 = *(_T292 + 20)
    call _T293
    parm _T204
    _T294 = *(_T204 + 0)
    _T295 = *(_T294 + 20)
    call _T295
    parm _T205
    _T296 = *(_T205 + 0)
    _T297 = *(_T296 + 20)
    call _T297
}

