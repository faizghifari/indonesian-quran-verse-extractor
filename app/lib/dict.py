def load_dict():
    target_dict = {
        'fenomena cuaca' : 0, # x
        'bahasa' : 1,
        'atribut fisik' : 2, # x
        'zat fisik' : 3, # x
        'artefak' : 4, # x
        'ciptaan yang hidup' : 5, # x
        'kitab suci' : 6, # y
        'allah' : 7,
        'singgasana allah' : 8,
        'tuhan palsu' : 9, # x
        'agama' : 10, # y
        'benda astronomi' : 11, # x
        'peristiwa' : 12, # x
        'lokasi' : 13, # x
        'petir' : 14,
        'guntur' : 15,
        'hujan' : 16,
        'awan' : 17,
        'arab' : 18,
        'warna' : 19,
        'hijau' : 20, # merah, biru, hitam, putih
        'logam' : 21, # x
        'mineral' : 22, # x
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
        'tempat ibadah' : 36, # x
        'persenjataan' : 37, # senjata
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
        'objek organik' : 58,  # x
        'makhluk hidup' : 59, # x
        'bagian tubuh' : 60, # tubuh, badan
        'penyakit' : 61, # y
        'makanan' : 62, # y
        'organisme biologis' : 63, # x
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
        'wine' : 86, # khamar
        'gandum' : 87,
        'daging babi' : 88,
        'bangkai' : 89,
        'serangga' : 90, # x
        'burung' : 91,
        'tanaman' : 92, # y
        'binatang' : 93, # y
        'ikan' : 94,
        'belalang' : 95, 
        'lebah' : 96,
        'laba-laba' : 97, # laba laba
        'semut' : 98, # + kutu, after this
        'nyamuk' : 99,
        'lalat' : 100,
        'gagak' : 101, # burung gagak (add)
        'puyuh' : 102, # salwa, burung puyuh (add)
        'hud-hud' : 103, # hud hud
        'timun' : 104, # mentimun
        'kurma' : 105, 
        'ara' : 106, # tin
        'bawang putih' : 107,
        'jahe' : 108,
        'anggur' : 109,
        'herba' : 110, # sayur
        'daun' : 111, # kelopak, mayang
        'kacang' : 112,
        'zaitun' : 113,
        'bawang' : 114, # bawang merah
        'lentil' : 115, # kacang adas
        'pohon' : 116,
        'delima' : 117,
        'unta' : 118,
        'sapi' : 119,
        'babi' : 120,
        'kambing' : 121,
        'kuda' : 122,
        'singa' : 123,
        'keledai' : 124, # baghal, bagal
        'kera' : 125,
        'serigala' : 126,
        'katak' : 127,
        'domba' : 128,
        'ular' : 129,
        'anjing' : 130,
        'malaikat' : 131, # y
        'jin' : 132,
        'manusia' : 133, # y
        'daabbah' : 134, # binatang melata
        'jibril' : 135,
        'malaikat maut' : 136,
        'harut' : 137,
        'marut' : 138,
        'malik' : 139,
        'mikail' : 140,
        'setan' : 141, # syaitan
        'iblis' : 142,
        'raja' : 143,
        'anak adam' : 144, # anak anak adam, etc
        'orang bersejarah' : 145, # x
        'orang-orang bersejarah' : 146, # x
        'nabi' : 147, # y
        'firaun' : 148,
        'uzair' : 149,
        'luqman' : 150,
        'jalut' : 151,
        'dzulkifli' : 152, # zulkifli
        'samiri' : 153,
        'talut' : 154, # thalut
        'qarun' : 155, # karun
        'dzulkarnain' : 156, 
        'haman' : 157,
        'aad' : 158, #  Aad
        'tsamud' : 159,
        'madyan' : 160, 
        'quraisy' : 161,
        'romawi' : 162, 
        'anshar' : 163,
        'arab badui' : 164, # badui
        'tubba' : 165,
        'bani israil' : 166,
        'yajuj dan majuj' : 167, # yajuj majuj pisah
        'pemuda kahfi' : 168, # orang-orang yang mendiami gua
        'tentara bergajah' : 169,
        'pembuat parit' : 170, # orang-orang yang membuat parit
        'penduduk rass' : 171, 
        'penduduk aikah' : 172,
        'penduduk al-hijr' : 173, # al hijr, penduduk-penduduk kota al hijr
        'abu lahab' : 174,
        'ummu jamil' : 175, # x
        'rasul' : 176, # y
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
        'azar' : 192, # Aazar
        'muhammad' : 193,
        'isa' : 194,
        'ibrahim' : 195,
        'ismail' : 196,
        'salih' : 197,  # shaleh
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
        'messiah' : 208, # al masih
        'quran' : 209, # al quran
        'injil' : 210,
        'zabur' : 211,
        'taurat' : 212,
        'islam' : 213,
        'kristen' : 214, # nasrani
        'yahudi' : 215,
        'shabiin' : 216, 
        'majusi' : 217,
        'bulan' : 218,
        'bumi' : 219,
        'matahari' : 220,
        'bintang' : 221,
        'sirius' : 222, # syira
        'gugus bintang' : 223, # gugusan bintang
        'uzza' : 224, # al uzza
        'manat' : 225, 
        'latta' : 226, # al lata
        'suwa' : 227, # suwwa
        'baal' : 228,
        'nasr' : 229,
        'wadd' : 230,
        'yaghuts' : 231,
        'yauq' : 232,
        'sesembahan' : 233, # berhala
        'anak lembu emas' : 234, # lembu
        'peristiwa bersejarah' : 235, # x
        'peristiwa kalender' : 236, # x
        'peristiwa fisik' : 237, # x
        'peristiwa akhirat' : 238, # akhirat
        'masa jahiliyah' : 239, # jahiliyah
        'hari jumat' : 240, # jumat
        'hari sabtu' : 241, # sabtu
        'haji' : 242, 
        'umrah' : 243,
        'lailatul qadar' : 244, # malam kemuliaan
        'bulan ramadhan' : 245, # ramadhan
        'fajar' : 246,
        'hari kebangkitan' : 247, # kebangkitan
        'hari kiamat' : 248,
        'lokasi di akhirat' : 249, # x
        'lokasi geografis' : 250, # x
        'surga' : 251,
        'neraka' : 252,
        'firdaus' : 253,
        'adn' : 254,
        'pohon bidara' : 255,
        'salsabil' : 256,
        'sijjin' : 257,
        'saqar' : 258,
        'zaqqum' : 259,
        'ladha' : 260, # api yang bergejolak (?)
        'ufuk' : 261,
        'kiblat' : 262,
        'gurun' : 263, # dusun
        'kota' : 264, # y
        'gunung' : 265, # y
        'tempat bersejarah' : 266, # x
        'badar' : 267,
        'mekkah' : 268, # mekah, baitullah
        'madinah' : 269,
        'babilonia' : 270, # babil
        'hunain' : 271,
        'iram' : 272,
        'yastrib' : 273,
        'shafa' : 274,
        'marwah' : 275, # marwa
        'arafat' : 276, # arafah
        'sinai' : 277, 
        'judiy' : 278, # judi, bukit judi
        'mesir' : 279,
        'saba' : 280,
        'al-ahqaf' : 281 # al ahqaf
        # 'kutu' : 282
        # 'imran' : 283
        # angin, kebun
        # keluarga, ayah, ibu, bapak, anak, yatim, saudara, budak, laki, perempuan
        # harta, niaga, jual beli, hutang, riba, dagang
        # ibadah, shalat, puasa, zakat, sedekah
        # negara, bangsa, hukum, adil
        # kisah, hikmah, ilmu
        # perang
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

    return target_dict, surah_dict