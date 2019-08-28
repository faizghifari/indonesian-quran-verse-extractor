def load_dict():
    target_dict = {
        'text' : 0,
        'bahasa' : 1,
        'kitab' : 2,
        'allah' : 3,
        'arsy' : 4,
        'agama' : 5,
        'petir' : 6,
        'guntur' : 7,
        'hujan' : 8,
        'awan' : 9,
        'angin' : 10,
        'arab' : 11,
        'warna' : 12, #
        'hijau' : 13, 
        'merah' : 14,
        'biru' : 15, #
        'hitam' : 16,
        'putih' : 17,
        'minyak' : 18,
        'karang' : 19,
        'tanah' : 20,
        'mutiara' : 21,
        'kaca' : 22,
        'debu' : 23,
        'sutra' : 24, #
        'tanah liat' : 25, #
        'besi' : 26,
        'emas' : 27,
        'perak' : 28,
        'kuningan' : 29, #
        'permata' : 30,
        'senjata' : 31,
        'dirham' : 32, #
        'tinta' : 33,
        'pena' : 34,
        'tabut' : 35,
        'perahu' : 36,
        'kapal' : 37,
        'lampu' : 38, #
        'kunci' : 39, #
        'tangga' : 40, #
        'bahtera' : 41, #
        'masjid' : 42,
        'gereja' : 43,
        'biara' : 44,
        'masjidil haram' : 45, #
        'masjidil aqsha' : 46,
        'kabah' : 47,
        'pisau' : 48, #
        'panah' : 49,
        'baju besi' : 50, #
        'tubuh' : 51,
        'badan' : 52,
        'penyakit' : 53,
        'sakit' : 54,
        'makanan' : 55,
        'janin' : 56, #
        'darah' : 57,
        'tulang' : 58,
        'telinga' : 59,
        'mata' : 60,
        'jari' : 61,
        'dahi' : 62, #
        'ubun ubun' : 63,
        'jantung' : 64,
        'hati' : 65,
        'dada' : 66, #
        'punggung' : 67, #
        'tangan' : 68,
        'kaki' : 69,
        'perut' : 70,
        'lambung' : 71, #
        'rambut' : 72, #
        'kulit' : 73,
        'leher' : 74, #
        'dagu' : 75, #
        'tumit' : 76, #
        'usus' : 77, #
        'bibir' : 78, #
        'hidung' : 79, #
        'lidah' : 80,
        'sayap' : 81,
        'rusuk' : 82, #
        'kusta' : 83, #
        'daging' : 84,
        'madu' : 85,
        'susu' : 86,
        'garam' : 87,
        'roti' : 88,
        'khamar' : 89, #
        'gandum' : 90,
        'daging babi' : 91,
        'bangkai' : 92, #
        'burung' : 93,
        'tanaman' : 94, 
        'binatang' : 95,
        'ikan' : 96,
        'belalang' : 97, #
        'lebah' : 98, #
        'laba laba' : 99,
        'semut' : 100,
        'kutu' : 101,
        'nyamuk' : 102,
        'lalat' : 103,
        'gagak' : 104,
        'salwa' : 105,
        'hud hud' : 106, 
        'kebun' : 107,
        'mentimun' : 108,
        'kurma' : 109,
        'tin' : 110,
        'jahe' : 111,
        'anggur' : 112,
        'sayur' : 113,
        'daun' : 114,
        'kelopak' : 115,
        'mayang': 116,
        'zaitun' : 117,
        'bawang' : 118,
        'kacang' : 119,
        'pohon' : 120,
        'delima' : 121,
        'unta' : 122,
        'sapi' : 123,
        'babi' : 124,
        'kambing' : 125,
        'kuda' : 126,
        'singa' : 127, #
        'keledai' : 128, #
        'bagal' : 129, #
        'kera' : 130, #
        'serigala' : 131, #
        'katak' : 132, #
        'domba' : 133, #
        'ular' : 134, #
        'anjing' : 135, #
        'malaikat' : 136,
        'jin' : 137,
        'manusia' : 138,
        'binatang melata' : 139, # 
        'jibril' : 140,
        'malaikat maut' : 141,
        'harut' : 142,
        'marut' : 143,
        'malik' : 144, 
        'mikail' : 145,
        'syaitan' : 146,
        'iblis' : 147,
        'raja' : 148,
        'anak adam' : 149,
        'nabi' : 150, 
        'firaun' : 151,
        'uzair' : 152,
        'luqman' : 153,
        'jalut' : 154,
        'dzulkifli' : 155,
        'samiri' : 156,
        'thalut' : 157,
        'karun' : 158,
        'dzulkarnain' : 159,
        'haman' : 160,
        'aad' : 161,
        'tsamud' : 162,
        'madyan' : 163,
        'quraisy' : 164,
        'romawi' : 165, 
        'anshar' : 166,
        'badui' : 167, 
        'tubba' : 168,
        'bani israil' : 169,
        'yajuj' : 170,
        'majuj' : 171,
        'orang yang mendiami gua' : 172,
        'tentara bergajah' : 173,
        'orang yang membuat parit' : 174,
        'penduduk rass' : 175,
        'penduduk aikah' : 176,
        'al hijr' : 177, 
        'abu lahab' : 178,
        'rasul' : 179,
        'zakaria' : 180,
        'yahya' : 181, 
        'harun' : 182,
        'idris' : 183,
        'ilyasa' : 184,
        'ayyub' : 185,
        'adam' : 186,
        'daud' : 187, 
        'sulaiman' : 188,
        'yusuf' : 189,
        'yaqub' : 190,
        'ishaq' : 191,
        'habil' : 192,
        'qabil' : 193,
        'israil' : 194,
        'aazar' : 195,
        'muhammad' : 196,
        'isa' : 197,
        'ibrahim' : 198,
        'ismail' : 199,
        'shaleh' : 200,
        'hud' : 201,
        'syuaib' : 202,
        'yunus' : 203,
        'musa' : 204,
        'nuh' : 205,
        'luth' : 206,
        'ilyas' : 207,
        'ahmad' : 208,
        'zaid' : 209,
        'maryam' : 210,
        'al masih' : 211,
        'quran' : 212,
        'injil' : 213,  
        'zabur' : 214,
        'taurat' : 215,
        'islam' : 216,
        'nasrani' : 217,
        'yahudi' : 218,
        'shabiin' : 219,
        'majusi' : 220,
        'bulan' : 221,
        'bumi' : 222,
        'matahari' : 223, #
        'bintang' : 224,
        'syira' : 225, #
        'gugusan bintang' : 226,
        'al uzza' : 227, #
        'manat' : 228, #
        'al lata' : 229,
        'suwwa' : 230, #
        'baal' : 231, #
        'nasr' : 232, #
        'wadd' : 233, #
        'yaghuts' : 234, #
        'yauq' : 235, #
        'berhala' : 236,
        'lembu' : 237, #
        'akhirat' : 238,
        'jahiliyah' : 239, #
        'jumat' : 240,
        'sabtu' : 241,
        'haji' : 242,
        'umrah' : 243,
        'malam kemuliaan' : 244, #
        'ramadhan' : 245, 
        'fajar' : 246, #
        'kebangkitan' : 247,
        'hari kiamat' : 248,
        'surga' : 249,
        'neraka' : 250,
        'firdaus' : 251,
        'adn' : 252,
        'pohon bidara' : 253,
        'salsabil' : 254,
        'sijjin' : 255,
        'saqar' : 256,
        'zaqqum' : 257,
        'api yang bergejolak' : 258, #
        'ufuk' : 259, #
        'kiblat' : 260,
        'dusun' : 261, #
        'kota' : 262,
        'gunung' : 263,
        'badar' : 264,
        'mekah' : 265,
        'baitullah' : 266, #
        'madinah' : 267, #
        'babil' : 268,
        'hunain' : 269,
        'iram' : 270,
        'yastrib' : 271, #
        'shafa' : 272, 
        'marwa' : 273, 
        'arafah' : 274,
        'sinai' : 275, 
        'bukit judi' : 276,
        'mesir' : 277,
        'saba' : 278,
        'al ahqaf' : 279,
        'imran' : 280,
        'keluarga' : 281, # --------
        'ayah' : 282,
        'ibu' : 283,
        'bapak' : 284,
        'anak' : 285,
        'yatim' : 286,
        'saudara' : 287,
        'budak' : 288,
        'laki' : 289,
        'perempuan' : 290,
        'harta' : 291,
        'niaga' : 292,
        'jual beli' : 293,
        'hutang' : 294,
        'riba' : 295,
        'dagang' : 296,
        'ibadah' : 297,
        'shalat' : 298,
        'puasa' : 299,
        'zakat' : 300,
        'sedekah' : 301,
        'negara' : 302,
        'bangsa' : 303,
        'hukum' : 304,
        'adil' : 305,
        'kisah' : 306,
        'hikmah' : 307,
        'ilmu' : 308,
        'perang' : 309,
        'zalim' : 310
    }

    old_dict = {
        'fenomena cuaca' : 0,
        'bahasa' : 1,
        'atribut fisik' : 2,
        'zat fisik' : 3,
        'artefak' : 4,
        'ciptaan yang hidup' : 5,
        'kitab suci' : 6,
        'allah' : 7,
        'singgasana allah' : 8,
        'tuhan palsu' : 9,
        'agama' : 10,
        'benda astronomi' : 11,
        'peristiwa' : 12,
        'lokasi' : 13,
        'petir' : 14,
        'guntur' : 15,
        'hujan' : 16,
        'awan' : 17,
        'arab' : 18,
        'warna' : 19,
        'hijau' : 20,
        'logam' : 21,
        'mineral' : 22,
        'minyak' : 23,
        'karang' : 24,
        'tanah' : 25,
        'mutiara' : 26,
        'kaca' : 27,
        'debu' : 28,
        'sutra' : 29,
        'tanah liat' : 30,
        'besi' : 31,
        'emas' : 32,
        'perak' : 33,
        'kuningan' : 34,
        'permata' : 35,
        'tempat ibadah' : 36,
        'persenjataan' : 37,
        'koin' : 38,
        'tinta' : 39,
        'pena' : 40,
        'tabut' : 41,
        'perahu' : 42,
        'kapal' : 43,
        'lampu' : 44,
        'kunci' : 45,
        'tangga' : 46,
        'bahtera' : 47,
        'masjid' : 48,
        'gereja' : 49,
        'biara' : 50,
        'sinagog' : 51,
        'masjidil haram' : 52,
        'masjidil aqsa' : 53,
        'kabah' : 54,
        'pisau' : 55,
        'panah' : 56,
        'baju besi' : 57,
        'objek organik' : 58,
        'makhluk hidup' : 59,
        'bagian tubuh' : 60,
        'penyakit' : 61,
        'makanan' : 62,
        'organisme biologis' : 63,
        'embrio' : 64,
        'darah' : 65,
        'tulang' : 66,
        'telinga' : 67,
        'mata' : 68,
        'jari' : 69,
        'dahi' : 70,
        'gombak' : 71,
        'jantung' : 72,
        'tumit' : 73,
        'usus' : 74,
        'bibir' : 75,
        'hidung' : 76,
        'lidah' : 77,
        'sayap' : 78,
        'tulang rusuk' : 79,
        'kusta' : 80,
        'daging' : 81,
        'madu' : 82,
        'susu' : 83,
        'garam' : 84,
        'roti' : 85,
        'wine' : 86,
        'gandum' : 87,
        'daging babi' : 88,
        'bangkai' : 89,
        'serangga' : 90,
        'burung' : 91,
        'tanaman' : 92,
        'binatang' : 93,
        'ikan' : 94,
        'belalang' : 95,
        'lebah' : 96,
        'laba-laba' : 97,
        'semut' : 98,
        'nyamuk' : 99,
        'lalat' : 100,
        'gagak' : 101,
        'puyuh' : 102,
        'hud-hud' : 103,
        'timun' : 104,
        'kurma' : 105,
        'ara' : 106,
        'bawang putih' : 107,
        'jahe' : 108,
        'anggur' : 109,
        'herba' : 110,
        'daun' : 111,
        'kacang' : 112,
        'zaitun' : 113,
        'bawang' : 114,
        'lentil' : 115,
        'pohon' : 116,
        'delima' : 117,
        'unta' : 118,
        'sapi' : 119,
        'babi' : 120,
        'kambing' : 121,
        'kuda' : 122,
        'singa' : 123,
        'keledai' : 124,
        'kera' : 125,
        'serigala' : 126,
        'katak' : 127,
        'domba' : 128,
        'ular' : 129,
        'anjing' : 130,
        'malaikat' : 131,
        'jin' : 132,
        'manusia' : 133,
        'daabbah' : 134,
        'jibril' : 135,
        'malaikat maut' : 136,
        'harut' : 137,
        'marut' : 138,
        'malik' : 139,
        'mikail' : 140,
        'setan' : 141,
        'iblis' : 142,
        'raja' : 143,
        'anak adam' : 144,
        'orang bersejarah' : 145,
        'orang-orang bersejarah' : 146,
        'nabi' : 147,
        'firaun' : 148,
        'uzair' : 149,
        'luqman' : 150,
        'jalut' : 151,
        'dzulkifli' : 152,
        'samiri' : 153,
        'talut' : 154,
        'qarun' : 155,
        'dzulkarnain' : 156,
        'haman' : 157,
        'aad' : 158,
        'tsamud' : 159,
        'madyan' : 160,
        'quraisy' : 161,
        'romawi' : 162,
        'anshar' : 163,
        'arab badui' : 164,
        'tubba' : 165,
        'bani israil' : 166,
        'yajuj dan majuj' : 167,
        'pemuda kahfi' : 168,
        'tentara bergajah' : 169,
        'pembuat parit' : 170,
        'penduduk rass' : 171,
        'penduduk aikah' : 172,
        'penduduk al-hijr' : 173,
        'abu lahab' : 174,
        'ummu jamil' : 175,
        'rasul' : 176,
        'zakaria' : 177,
        'yahya' : 178,
        'harun' : 179,
        'idris' : 180,
        'ilyasa' : 181,
        'ayyub' : 182,
        'adam' : 183,
        'daud' : 184,
        'sulaiman' : 185,
        'yusuf' : 186,
        'yaqub' : 187,
        'ishaq' : 188,
        'habil' : 189,
        'qabil' : 190,
        'israil' : 191,
        'azar' : 192,
        'muhammad' : 193,
        'isa' : 194,
        'ibrahim' : 195,
        'ismail' : 196,
        'salih' : 197,
        'hud' : 198,
        'syuaib' : 199,
        'yunus' : 200,
        'musa' : 201,
        'nuh' : 202,
        'luth' : 203,
        'ilyas' : 204,
        'ahmad' : 205,
        'zaid' : 206,
        'maryam' : 207,
        'messiah' : 208,
        'quran' : 209,
        'injil' : 210,
        'zabur' : 211,
        'taurat' : 212,
        'islam' : 213,
        'kristen' : 214,
        'yahudi' : 215,
        'shabiin' : 216,
        'majusi' : 217,
        'bulan' : 218,
        'bumi' : 219,
        'matahari' : 220,
        'bintang' : 221,
        'sirius' : 222,
        'gugus bintang' : 223,
        'uzza' : 224,
        'manat' : 225,
        'latta' : 226,
        'suwa' : 227,
        'baal' : 228,
        'nasr' : 229,
        'wadd' : 230,
        'yaghuts' : 231,
        'yauq' : 232,
        'sesembahan' : 233,
        'anak lembu emas' : 234,
        'peristiwa bersejarah' : 235,
        'peristiwa kalender' : 236,
        'peristiwa fisik' : 237,
        'peristiwa akhirat' : 238,
        'masa jahiliyah' : 239,
        'hari jumat' : 240,
        'hari sabtu' : 241,
        'haji' : 242,
        'umrah' : 243,
        'lailatul qadar' : 244,
        'bulan ramadhan' : 245,
        'fajar' : 246,
        'hari kebangkitan' : 247,
        'hari kiamat' : 248,
        'lokasi di akhirat' : 249,
        'lokasi geografis' : 250,
        'surga' : 251,
        'neraka' : 252,
        'firdaus' : 253,
        'adn' : 254,
        'pohon bidara' : 255,
        'salsabil' : 256,
        'sijjin' : 257,
        'saqar' : 258,
        'zaqqum' : 259,
        'ladha' : 260,
        'ufuk' : 261,
        'kiblat' : 262,
        'gurun' : 263,
        'kota' : 264,
        'gunung' : 265,
        'tempat bersejarah' : 266,
        'badar' : 267,
        'mekkah' : 268,
        'madinah' : 269,
        'babilonia' : 270,
        'hunain' : 271,
        'iram' : 272,
        'yastrib' : 273,
        'shafa' : 274,
        'marwah' : 275,
        'arafat' : 276,
        'sinai' : 277,
        'judiy' : 278,
        'mesir' : 279,
        'saba' : 280,
        'al-ahqaf' : 281
        # 'kutu' : 282
    }

    surah_dict = {
        '1' : 'Al-Fatihah',
        '2' : 'Al-Baqarah',
        '3' : 'Ali Imran',
        '4' : 'An-Nisaa\'',
        '5' : 'Al-Maa\'idah',
        '6' : 'Al-An\'am',
        '7' : 'Al-A\'raf',
        '8' : 'Al-Anfaal',
        '9' : 'At-Taubah',
        '10' : 'Yunus',
        '11' : 'Hud',
        '12' : 'Yusuf',
        '13' : 'Ar-Ra\'d',
        '14' : 'Ibrahim',
        '15' : 'Al-Hijr',
        '16' : 'An-Nahl',
        '17' : 'Al-Israa\'',
        '18' : 'Al-Kahfi',
        '19' : 'Maryam',
        '20' : 'Ta-Ha',
        '21' : 'Al-Anbiyaa\'',
        '22' : 'Al-Hajj',
        '23' : 'Al-Mu\'minun',
        '24' : 'An-Nuur',
        '25' : 'Al-Furqan',
        '26' : 'Asy-Syu\'ara',
        '27' : 'An-Naml',
        '28' : 'Al-Qasas',
        '29' : 'Al-Ankabut',
        '30' : 'Ar-Ruum',
        '31' : 'Luqman',
        '32' : 'As-Sajdah',
        '33' : 'Al-Ahzab',
        '34' : 'Sabaa\'',
        '35' : 'Fatir',
        '36' : 'Yasin',
        '37' : 'As-Saffaat',
        '38' : 'Shad',
        '39' : 'Az-Zumar',
        '40' : 'Ghaafir',
        '41' : 'Fussilat',
        '42' : 'Asy-Syura\'',
        '43' : 'Az-Zukhruf',
        '44' : 'Ad-Dukhan',
        '45' : 'Al-Jaasiyah',
        '46' : 'Al-Ahqaf',
        '47' : 'Muhammad',
        '48' : 'Al-Fath',
        '49' : 'Al-Hujurat',
        '50' : 'Qaf',
        '51' : 'Adz-Dzariyat',
        '52' : 'At-Tuur',
        '53' : 'An-Najm',
        '54' : 'Al-Qomar',
        '55' : 'Ar-Rahman',
        '56' : 'Al-Waqi\'ah',
        '57' : 'Al-Hadid',
        '58' : 'Al-Mujadilah',
        '59' : 'Al-Hasyr',
        '60' : 'Al-Mumtahanah',
        '61' : 'As-Saff',
        '62' : 'Al-Jumu\'ah',
        '63' : 'Al-Munafiqun',
        '64' : 'At-Taghabun',
        '65' : 'At-Talaq',
        '66' : 'At-Tahrim',
        '67' : 'Al-Mulk',
        '68' : 'Al-Qolam',
        '69' : 'Al-Haqqah',
        '70' : 'Al-Ma\'arij',
        '71' : 'Nuh',
        '72' : 'Al-Jinn',
        '73' : 'Al-Muzammil',
        '74' : 'Al-Muddatsir',
        '75' : 'Al-Qiyamah',
        '76' : 'Al-Insan',
        '77' : 'Al-Mursalat',
        '78' : 'An-Naba',
        '79' : 'An-Nazi\'at',
        '80' : '\'Abasa',
        '81' : 'At-Takwir',
        '82' : 'Al-Infitar',
        '83' : 'Al-Muthaffifin',
        '84' : 'Al-Insyiqaq',
        '85' : 'Al-Buruj',
        '86' : 'At-Thariq',
        '87' : 'Al-A\'la',
        '88' : 'Al-Ghasiyah',
        '89' : 'Al-Fajr',
        '90' : 'Al-Balad',
        '91' : 'Asy-Syams',
        '92' : 'Al-Lail',
        '93' : 'Ad-Dhuha',
        '94' : 'Al-Insyirah',
        '95' : 'At-Tin',
        '96' : 'Al-Alaq',
        '97' : 'Al-Qadr',
        '98' : 'Al-Bayyinah',
        '99' : 'Az-Zalzalah',
        '100' : 'Al-Adiyat',
        '101' : 'Al-Qariah',
        '102' : 'At-Takatsur',
        '103' : 'Al-Asr',
        '104' : 'Al-Humazah',
        '105' : 'Al-Fiil',
        '106' : 'Quraisy',
        '107' : 'Al-Maun',
        '108' : 'Al-Kautsar',
        '109' : 'Al-Kafirun',
        '110' : 'An-Nasr',
        '111' : 'Al-Masad',
        '112' : 'Al-Ikhlas',
        '113' : 'Al-Falaq',
        '114' : 'An-Nas'
    }
    
    return target_dict, old_dict, surah_dict