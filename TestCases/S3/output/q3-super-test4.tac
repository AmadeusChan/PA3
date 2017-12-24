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
    _C.allprint;
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
    _T40 = 12
    parm _T40
    _T41 =  call _Alloc
    _T42 = 0
    *(_T41 + 4) = _T42
    *(_T41 + 8) = _T42
    _T43 = VTBL <_A>
    *(_T41 + 0) = _T43
    return _T41
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T44 = 20
    parm _T44
    _T45 =  call _Alloc
    _T46 = 0
    *(_T45 + 4) = _T46
    *(_T45 + 8) = _T46
    *(_T45 + 12) = _T46
    *(_T45 + 16) = _T46
    _T47 = VTBL <_B>
    *(_T45 + 0) = _T47
    return _T45
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T48 = 20
    parm _T48
    _T49 =  call _Alloc
    _T50 = 0
    *(_T49 + 4) = _T50
    *(_T49 + 8) = _T50
    *(_T49 + 12) = _T50
    *(_T49 + 16) = _T50
    _T51 = VTBL <_C>
    *(_T49 + 0) = _T51
    return _T49
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T52 = 28
    parm _T52
    _T53 =  call _Alloc
    _T54 = 0
    _T55 = 4
    _T56 = (_T53 + _T52)
_L40:
    _T57 = (_T56 - _T55)
    _T56 = _T57
    _T58 = (_T52 - _T55)
    _T52 = _T58
    if (_T52 == 0) branch _L41
    *(_T56 + 0) = _T54
    branch _L40
_L41:
    _T59 = VTBL <_D>
    *(_T56 + 0) = _T59
    return _T56
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T60 = 28
    parm _T60
    _T61 =  call _Alloc
    _T62 = 0
    _T63 = 4
    _T64 = (_T61 + _T60)
_L43:
    _T65 = (_T64 - _T63)
    _T64 = _T65
    _T66 = (_T60 - _T63)
    _T60 = _T66
    if (_T60 == 0) branch _L44
    *(_T64 + 0) = _T62
    branch _L43
_L44:
    _T67 = VTBL <_E>
    *(_T64 + 0) = _T67
    return _T64
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T68 = 36
    parm _T68
    _T69 =  call _Alloc
    _T70 = 0
    _T71 = 4
    _T72 = (_T69 + _T68)
_L46:
    _T73 = (_T72 - _T71)
    _T72 = _T73
    _T74 = (_T68 - _T71)
    _T68 = _T74
    if (_T68 == 0) branch _L47
    *(_T72 + 0) = _T70
    branch _L46
_L47:
    _T75 = VTBL <_F>
    *(_T72 + 0) = _T75
    return _T72
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T76 = 24
    parm _T76
    _T77 =  call _Alloc
    _T78 = 0
    _T79 = 4
    _T80 = (_T77 + _T76)
_L49:
    _T81 = (_T80 - _T79)
    _T80 = _T81
    _T82 = (_T76 - _T79)
    _T76 = _T82
    if (_T76 == 0) branch _L50
    *(_T80 + 0) = _T78
    branch _L49
_L50:
    _T83 = VTBL <_G>
    *(_T80 + 0) = _T83
    return _T80
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T84 = 4
    parm _T84
    _T85 =  call _Alloc
    _T86 = VTBL <_Main>
    *(_T85 + 0) = _T86
    return _T85
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T87 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T88 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T89 = " a="
    parm _T89
    call _PrintString
    _T90 = *(_T3 + 4)
    parm _T90
    call _PrintInt
    _T91 = " a1="
    parm _T91
    call _PrintString
    _T92 = *(_T3 + 8)
    parm _T92
    call _PrintInt
    _T93 = " "
    parm _T93
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T94 = VTBL <_A>
    _T95 = *(_T94 + 12)
    call _T95
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T96 = "A"
    parm _T96
    call _PrintString
    parm _T5
    _T97 = VTBL <_A>
    _T98 = *(_T97 + 12)
    call _T98
    _T99 = "\n"
    parm _T99
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T100 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T101 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T102 = " b="
    parm _T102
    call _PrintString
    _T103 = *(_T9 + 12)
    parm _T103
    call _PrintInt
    _T104 = " b1="
    parm _T104
    call _PrintString
    _T105 = *(_T9 + 16)
    parm _T105
    call _PrintInt
    _T106 = " "
    parm _T106
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    parm _T10
    _T107 = VTBL <_A>
    _T108 = *(_T107 + 16)
    call _T108
    parm _T10
    _T109 = VTBL <_B>
    _T110 = *(_T109 + 12)
    call _T110
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T111 = "B"
    parm _T111
    call _PrintString
    parm _T11
    _T112 = VTBL <_A>
    _T113 = *(_T112 + 16)
    call _T113
    parm _T11
    _T114 = VTBL <_B>
    _T115 = *(_T114 + 12)
    call _T115
    _T116 = "\n"
    parm _T116
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T117 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T118 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T119 = " c="
    parm _T119
    call _PrintString
    _T120 = *(_T15 + 12)
    parm _T120
    call _PrintInt
    _T121 = " c1="
    parm _T121
    call _PrintString
    _T122 = *(_T15 + 16)
    parm _T122
    call _PrintInt
    _T123 = " "
    parm _T123
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T124 = VTBL <_C>
    _T125 = *(_T124 + 12)
    call _T125
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T126 = "C"
    parm _T126
    call _PrintString
    parm _T17
    _T127 = VTBL <_A>
    _T128 = *(_T127 + 16)
    call _T128
    parm _T17
    _T129 = VTBL <_C>
    _T130 = *(_T129 + 12)
    call _T130
    _T131 = "\n"
    parm _T131
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T132 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T133 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T134 = " d="
    parm _T134
    call _PrintString
    _T135 = *(_T21 + 20)
    parm _T135
    call _PrintInt
    _T136 = " d1="
    parm _T136
    call _PrintString
    _T137 = *(_T21 + 24)
    parm _T137
    call _PrintInt
    _T138 = " "
    parm _T138
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    parm _T22
    _T139 = VTBL <_B>
    _T140 = *(_T139 + 16)
    call _T140
    parm _T22
    _T141 = VTBL <_D>
    _T142 = *(_T141 + 12)
    call _T142
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T143 = "D"
    parm _T143
    call _PrintString
    parm _T23
    _T144 = VTBL <_B>
    _T145 = *(_T144 + 16)
    call _T145
    parm _T23
    _T146 = VTBL <_D>
    _T147 = *(_T146 + 12)
    call _T147
    _T148 = "\n"
    parm _T148
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T149 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T150 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T151 = " e="
    parm _T151
    call _PrintString
    _T152 = *(_T27 + 20)
    parm _T152
    call _PrintInt
    _T153 = " e1="
    parm _T153
    call _PrintString
    _T154 = *(_T27 + 24)
    parm _T154
    call _PrintInt
    _T155 = " "
    parm _T155
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T28:4'
_E.fun:
    _T156 = "E"
    parm _T156
    call _PrintString
    parm _T28
    _T157 = VTBL <_E>
    _T158 = *(_T157 + 16)
    call _T158
    parm _T28
    _T159 = VTBL <_E>
    _T160 = *(_T159 + 12)
    call _T160
    _T161 = "\n"
    parm _T161
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T29:4 _T30:8 _T31:12'
_F.setF:
    _T162 = *(_T29 + 28)
    *(_T29 + 28) = _T30
    _T163 = *(_T29 + 32)
    *(_T29 + 32) = _T31
}

FUNCTION(_F.print) {
memo '_T32:4'
_F.print:
    _T164 = " f="
    parm _T164
    call _PrintString
    _T165 = *(_T32 + 28)
    parm _T165
    call _PrintInt
    _T166 = " f1="
    parm _T166
    call _PrintString
    _T167 = *(_T32 + 32)
    parm _T167
    call _PrintInt
    _T168 = " "
    parm _T168
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T33:4'
_F.allprint:
    parm _T33
    _T169 = VTBL <_E>
    _T170 = *(_T169 + 16)
    call _T170
    parm _T33
    _T171 = VTBL <_F>
    _T172 = *(_T171 + 12)
    call _T172
}

FUNCTION(_F.fun) {
memo '_T34:4'
_F.fun:
    _T173 = "F"
    parm _T173
    call _PrintString
    parm _T34
    _T174 = VTBL <_E>
    _T175 = *(_T174 + 16)
    call _T175
    parm _T34
    _T176 = VTBL <_F>
    _T177 = *(_T176 + 12)
    call _T177
    _T178 = "\n"
    parm _T178
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T35:4 _T36:8'
_G.setG:
    _T179 = *(_T35 + 20)
    *(_T35 + 20) = _T36
}

FUNCTION(_G.print) {
memo '_T37:4'
_G.print:
    _T180 = " g="
    parm _T180
    call _PrintString
    _T181 = *(_T37 + 20)
    parm _T181
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T38:4'
_G.allprint:
    parm _T38
    _T182 = VTBL <_C>
    _T183 = *(_T182 + 16)
    call _T183
    parm _T38
    _T184 = VTBL <_G>
    _T185 = *(_T184 + 12)
    call _T185
}

FUNCTION(_G.fun) {
memo '_T39:4'
_G.fun:
    _T186 = "G"
    parm _T186
    call _PrintString
    parm _T39
    _T187 = VTBL <_C>
    _T188 = *(_T187 + 16)
    call _T188
    parm _T39
    _T189 = VTBL <_G>
    _T190 = *(_T189 + 12)
    call _T190
    _T191 = "\n"
    parm _T191
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T199 =  call _A_New
    _T192 = _T199
    _T200 =  call _B_New
    _T193 = _T200
    _T201 =  call _C_New
    _T194 = _T201
    _T202 =  call _D_New
    _T195 = _T202
    _T203 =  call _E_New
    _T196 = _T203
    _T204 =  call _F_New
    _T197 = _T204
    _T205 =  call _G_New
    _T198 = _T205
    _T206 = 10
    _T207 = 11
    parm _T192
    parm _T206
    parm _T207
    _T208 = *(_T192 + 0)
    _T209 = *(_T208 + 8)
    call _T209
    _T210 = 20
    _T211 = 21
    parm _T193
    parm _T210
    parm _T211
    _T212 = *(_T193 + 0)
    _T213 = *(_T212 + 8)
    call _T213
    _T214 = 22
    _T215 = 23
    parm _T193
    parm _T214
    parm _T215
    _T216 = *(_T193 + 0)
    _T217 = *(_T216 + 24)
    call _T217
    _T218 = 30
    _T219 = 31
    parm _T194
    parm _T218
    parm _T219
    _T220 = *(_T194 + 0)
    _T221 = *(_T220 + 8)
    call _T221
    _T222 = 32
    _T223 = 33
    parm _T194
    parm _T222
    parm _T223
    _T224 = *(_T194 + 0)
    _T225 = *(_T224 + 24)
    call _T225
    _T226 = 40
    _T227 = 41
    parm _T195
    parm _T226
    parm _T227
    _T228 = *(_T195 + 0)
    _T229 = *(_T228 + 8)
    call _T229
    _T230 = 42
    _T231 = 43
    parm _T195
    parm _T230
    parm _T231
    _T232 = *(_T195 + 0)
    _T233 = *(_T232 + 24)
    call _T233
    _T234 = 44
    _T235 = 45
    parm _T195
    parm _T234
    parm _T235
    _T236 = *(_T195 + 0)
    _T237 = *(_T236 + 28)
    call _T237
    _T238 = 50
    _T239 = 51
    parm _T196
    parm _T238
    parm _T239
    _T240 = *(_T196 + 0)
    _T241 = *(_T240 + 8)
    call _T241
    _T242 = 52
    _T243 = 53
    parm _T196
    parm _T242
    parm _T243
    _T244 = *(_T196 + 0)
    _T245 = *(_T244 + 24)
    call _T245
    _T246 = 54
    _T247 = 55
    parm _T196
    parm _T246
    parm _T247
    _T248 = *(_T196 + 0)
    _T249 = *(_T248 + 28)
    call _T249
    _T250 = 60
    _T251 = 61
    parm _T197
    parm _T250
    parm _T251
    _T252 = *(_T197 + 0)
    _T253 = *(_T252 + 8)
    call _T253
    _T254 = 62
    _T255 = 63
    parm _T197
    parm _T254
    parm _T255
    _T256 = *(_T197 + 0)
    _T257 = *(_T256 + 24)
    call _T257
    _T258 = 64
    _T259 = 65
    parm _T197
    parm _T258
    parm _T259
    _T260 = *(_T197 + 0)
    _T261 = *(_T260 + 28)
    call _T261
    _T262 = 66
    _T263 = 67
    parm _T197
    parm _T262
    parm _T263
    _T264 = *(_T197 + 0)
    _T265 = *(_T264 + 32)
    call _T265
    _T266 = 70
    _T267 = 71
    parm _T198
    parm _T266
    parm _T267
    _T268 = *(_T198 + 0)
    _T269 = *(_T268 + 8)
    call _T269
    _T270 = 72
    _T271 = 73
    parm _T198
    parm _T270
    parm _T271
    _T272 = *(_T198 + 0)
    _T273 = *(_T272 + 24)
    call _T273
    _T274 = 74
    parm _T198
    parm _T274
    _T275 = *(_T198 + 0)
    _T276 = *(_T275 + 28)
    call _T276
    parm _T192
    _T277 = *(_T192 + 0)
    _T278 = *(_T277 + 20)
    call _T278
    parm _T193
    _T279 = *(_T193 + 0)
    _T280 = *(_T279 + 20)
    call _T280
    parm _T194
    _T281 = *(_T194 + 0)
    _T282 = *(_T281 + 20)
    call _T282
    parm _T195
    _T283 = *(_T195 + 0)
    _T284 = *(_T283 + 20)
    call _T284
    parm _T196
    _T285 = *(_T196 + 0)
    _T286 = *(_T285 + 20)
    call _T286
    parm _T197
    _T287 = *(_T197 + 0)
    _T288 = *(_T287 + 20)
    call _T288
    parm _T198
    _T289 = *(_T198 + 0)
    _T290 = *(_T289 + 20)
    call _T290
}

