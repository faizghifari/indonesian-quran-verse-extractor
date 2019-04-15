import hmc

def load_label_hierarchy():
    ch = hmc.ClassHierarchy("konsep")

    ch.add_node("fenomena cuaca", "konsep")
    ch.add_node("bahasa", "konsep")
    ch.add_node("atribut fisik", "konsep")
    ch.add_node("zat fisik", "konsep")
    ch.add_node("artefak", "konsep")
    ch.add_node("ciptaan yang hidup", "konsep")
    ch.add_node("kitab suci", "konsep")
    ch.add_node("allah", "konsep")
    ch.add_node("singgasana allah", "konsep")
    ch.add_node("tuhan palsu", "konsep")
    ch.add_node("agama", "konsep")
    ch.add_node("benda astronomi", "konsep")
    ch.add_node("peristiwa", "konsep")
    ch.add_node("lokasi", "konsep")

    ch.add_node("petir", "fenomena cuaca")
    ch.add_node("guntur", "fenomena cuaca")
    ch.add_node("hujan", "fenomena cuaca")
    ch.add_node("awan", "fenomena cuaca")

    ch.add_node("arab", "bahasa")

    ch.add_node("warna", "atribut fisik")

    ch.add_node("hijau", "warna")

    ch.add_node("logam", "zat fisik")
    ch.add_node("mineral", "zat fisik")
    ch.add_node("minyak", "zat fisik")
    ch.add_node("karang", "zat fisik")
    ch.add_node("tanah", "zat fisik")
    ch.add_node("mutiara", "zat fisik")
    ch.add_node("kaca", "zat fisik")
    ch.add_node("debu", "zat fisik")
    ch.add_node("sutra", "zat fisik")
    ch.add_node("tanah liat", "zat fisik")

    ch.add_node("besi", "logam")
    ch.add_node("emas", "logam")
    ch.add_node("perak", "logam")
    ch.add_node("kuningan", "logam")

    ch.add_node("permata", "mineral")

    ch.add_node("tempat ibadah", "artefak")
    ch.add_node("persenjataan", "artefak")
    ch.add_node("koin", "artefak")
    ch.add_node("tinta", "artefak")
    ch.add_node("pena", "artefak")
    ch.add_node("tabut", "artefak")
    ch.add_node("perahu", "artefak")
    ch.add_node("kapal", "artefak")
    ch.add_node("lampu", "artefak")
    ch.add_node("kunci", "artefak")
    ch.add_node("tangga", "artefak")
    ch.add_node("bahtera", "artefak")

    ch.add_node("masjid", "tempat ibadah")
    ch.add_node("gereja", "tempat ibadah")
    ch.add_node("biara", "tempat ibadah")
    ch.add_node("sinagog", "tempat ibadah")

    ch.add_node("masjidil haram", "masjid")
    ch.add_node("masjidil aqsa", "masjid")
    ch.add_node("kabah", "masjid")

    ch.add_node("pisau", "persenjataan")
    ch.add_node("panah", "persenjataan")
    ch.add_node("baju besi", "persenjataan")

    ch.add_node("objek organik", "ciptaan yang hidup")
    ch.add_node("makhluk hidup", "ciptaan yang hidup")

    ch.add_node("bagian tubuh", "objek organik")
    ch.add_node("penyakit", "objek organik")
    ch.add_node("makanan", "objek organik")
    ch.add_node("organisme biologis", "objek organik")
    ch.add_node("embrio", "objek organik")
    ch.add_node("darah", "objek organik")


    ch.add_node("tulang", "bagian tubuh")
    ch.add_node("telinga", "bagian tubuh")
    ch.add_node("mata", "bagian tubuh")
    ch.add_node("jari", "bagian tubuh")
    ch.add_node("dahi", "bagian tubuh")
    ch.add_node("gombak", "bagian tubuh")
    ch.add_node("jantung", "bagian tubuh")
    ch.add_node("tumit", "bagian tubuh")
    ch.add_node("usus", "bagian tubuh")
    ch.add_node("bibir", "bagian tubuh")
    ch.add_node("hidung", "bagian tubuh")
    ch.add_node("lidah", "bagian tubuh")
    ch.add_node("sayap", "bagian tubuh")

    ch.add_node("tulang rusuk", "tulang")

    ch.add_node("kusta", "penyakit")

    ch.add_node("daging", "makanan")
    ch.add_node("madu", "makanan")
    ch.add_node("susu", "makanan")
    ch.add_node("garam", "makanan")
    ch.add_node("roti", "makanan")
    ch.add_node("wine", "makanan")
    ch.add_node("gandum", "makanan")
    ch.add_node("daging babi", "makanan")
    ch.add_node("bangkai", "makanan")

    ch.add_node("serangga", "organisme biologis")
    ch.add_node("burung", "organisme biologis")
    ch.add_node("tanaman", "organisme biologis")
    ch.add_node("binatang", "organisme biologis")
    ch.add_node("ikan", "organisme biologis")

    ch.add_node("belalang", "serangga")
    ch.add_node("lebah", "serangga")
    ch.add_node("laba-laba", "serangga")
    ch.add_node("semut", "serangga")
    ch.add_node("nyamuk", "serangga")
    ch.add_node("lalat", "serangga")

    ch.add_node("gagak", "burung")
    ch.add_node("puyuh", "burung")
    ch.add_node("hud-hud", "burung")

    ch.add_node("timun", "tanaman")
    ch.add_node("kurma", "tanaman")
    ch.add_node("ara", "tanaman")
    ch.add_node("bawang putih", "tanaman")
    ch.add_node("jahe", "tanaman")
    ch.add_node("anggur", "tanaman")
    ch.add_node("herba", "tanaman")
    ch.add_node("daun", "tanaman")
    ch.add_node("kacang", "tanaman")
    ch.add_node("zaitun", "tanaman")
    ch.add_node("bawang", "tanaman")
    ch.add_node("lentil", "tanaman")
    ch.add_node("pohon", "tanaman")
    ch.add_node("delima", "tanaman")

    ch.add_node("unta", "binatang")
    ch.add_node("sapi", "binatang")
    ch.add_node("babi", "binatang")
    ch.add_node("kambing", "binatang")
    ch.add_node("kuda", "binatang")
    ch.add_node("singa", "binatang")
    ch.add_node("keledai", "binatang")
    ch.add_node("kera", "binatang")
    ch.add_node("serigala", "binatang")
    ch.add_node("katak", "binatang")
    ch.add_node("domba", "binatang")
    ch.add_node("ular", "binatang")
    ch.add_node("anjing", "binatang")

    ch.add_node("malaikat", "makhluk hidup")
    ch.add_node("jin", "makhluk hidup")
    ch.add_node("manusia", "makhluk hidup")
    ch.add_node("daabbah", "makhluk hidup")

    ch.add_node("jibril", "malaikat")
    ch.add_node("malaikat maut", "malaikat")
    ch.add_node("harut", "malaikat")
    ch.add_node("marut", "malaikat")
    ch.add_node("malik", "malaikat")
    ch.add_node("mikail", "malaikat")

    ch.add_node("setan", "jin")

    ch.add_node("iblis", "setan")

    ch.add_node("raja", "manusia")
    ch.add_node("anak adam", "manusia")
    ch.add_node("orang bersejarah", "manusia")
    ch.add_node("orang-orang bersejarah", "manusia")
    ch.add_node("nabi", "manusia")

    ch.add_node("firaun", "orang bersejarah")
    ch.add_node("uzair", "orang bersejarah")
    ch.add_node("luqman", "orang bersejarah")
    ch.add_node("jalut", "orang bersejarah")
    ch.add_node("dzulkifli", "orang bersejarah")
    ch.add_node("samiri", "orang bersejarah")
    ch.add_node("talut", "orang bersejarah")
    ch.add_node("qarun", "orang bersejarah")
    ch.add_node("dzulkarnain", "orang bersejarah")
    ch.add_node("haman", "orang bersejarah")

    ch.add_node("aad", "orang-orang bersejarah")
    ch.add_node("tsamud", "orang-orang bersejarah")
    ch.add_node("madyan", "orang-orang bersejarah")
    ch.add_node("quraisy", "orang-orang bersejarah")
    ch.add_node("romawi", "orang-orang bersejarah")
    ch.add_node("anshar", "orang-orang bersejarah")
    ch.add_node("arab badui", "orang-orang bersejarah")
    ch.add_node("tubba", "orang-orang bersejarah")
    ch.add_node("bani israil", "orang-orang bersejarah")
    ch.add_node("yajuj dan majuj", "orang-orang bersejarah")
    ch.add_node("pemuda kahfi", "orang-orang bersejarah")
    ch.add_node("tentara bergajah", "orang-orang bersejarah")
    ch.add_node("pembuat parit", "orang-orang bersejarah")
    ch.add_node("penduduk rass", "orang-orang bersejarah")
    ch.add_node("penduduk aikah", "orang-orang bersejarah")

    ch.add_node("penduduk al-hijr", "tsamud")

    ch.add_node("abu lahab", "quraisy")

    ch.add_node("ummu jamil", "abu lahab")

    ch.add_node("rasul", "nabi")
    ch.add_node("zakaria", "nabi")
    ch.add_node("yahya", "nabi")
    ch.add_node("harun", "nabi")
    ch.add_node("idris", "nabi")
    ch.add_node("ilyasa", "nabi")
    ch.add_node("ayyub", "nabi")
    ch.add_node("adam", "nabi")
    ch.add_node("daud", "nabi")
    ch.add_node("sulaiman", "nabi")
    ch.add_node("yusuf", "nabi")
    ch.add_node("yaqub", "nabi")
    ch.add_node("ishaq", "nabi")

    ch.add_node("habil", "adam")
    ch.add_node("qabil", "adam")

    ch.add_node("israil", "yaqub")

    ch.add_node("azar", "ibrahim")

    ch.add_node("muhammad", "rasul")
    ch.add_node("isa", "rasul")
    ch.add_node("ibrahim", "rasul")
    ch.add_node("ismail", "rasul")
    ch.add_node("salih", "rasul")
    ch.add_node("hud", "rasul")
    ch.add_node("syuaib", "rasul")
    ch.add_node("yunus", "rasul")
    ch.add_node("musa", "rasul")
    ch.add_node("nuh", "rasul")
    ch.add_node("luth", "rasul")
    ch.add_node("ilyas", "rasul")

    ch.add_node("ahmad", "muhammad")
    ch.add_node("zaid", "muhammad")

    ch.add_node("maryam", "isa")
    ch.add_node("messiah", "isa")

    ch.add_node("quran", "kitab suci")
    ch.add_node("injil", "kitab suci")
    ch.add_node("zabur", "kitab suci")
    ch.add_node("taurat", "kitab suci")

    ch.add_node("islam", "agama")
    ch.add_node("kristen", "agama")
    ch.add_node("yahudi", "agama")
    ch.add_node("shabiin", "agama")
    ch.add_node("majusi", "agama")

    ch.add_node("bulan", "benda astronomi")
    ch.add_node("bumi", "benda astronomi")
    ch.add_node("matahari", "benda astronomi")
    ch.add_node("bintang", "benda astronomi")
    ch.add_node("sirius", "benda astronomi")
    ch.add_node("gugus bintang", "benda astronomi")

    ch.add_node("uzza", "tuhan palsu")
    ch.add_node("manat", "tuhan palsu")
    ch.add_node("latta", "tuhan palsu")
    ch.add_node("suwa", "tuhan palsu")
    ch.add_node("baal", "tuhan palsu")
    ch.add_node("nasr", "tuhan palsu")
    ch.add_node("wadd", "tuhan palsu")
    ch.add_node("yaghuts", "tuhan palsu")
    ch.add_node("yauq", "tuhan palsu")
    ch.add_node("sesembahan", "tuhan palsu")

    ch.add_node("anak lembu emas", "sesembahan")

    ch.add_node("peristiwa bersejarah", "peristiwa")
    ch.add_node("peristiwa kalender", "peristiwa")
    ch.add_node("peristiwa fisik", "peristiwa")
    ch.add_node("peristiwa akhirat", "peristiwa")

    ch.add_node("masa jahiliyah", "peristiwa bersejarah")

    ch.add_node("hari jumat", "peristiwa kalender")
    ch.add_node("hari sabtu", "peristiwa kalender")
    ch.add_node("haji", "peristiwa kalender")
    ch.add_node("umrah", "peristiwa kalender")
    ch.add_node("lailatul qadar", "peristiwa kalender")
    ch.add_node("bulan ramadhan", "peristiwa kalender")

    ch.add_node("fajar", "peristiwa fisik")

    ch.add_node("hari kebangkitan", "peristiwa akhirat")
    ch.add_node("hari kiamat", "hari kebangkitan")

    ch.add_node("lokasi di akhirat", "lokasi")
    ch.add_node("lokasi geografis", "lokasi")

    ch.add_node("surga", "lokasi di akhirat")
    ch.add_node("neraka", "lokasi di akhirat")

    ch.add_node("firdaus", "surga")
    ch.add_node("'adn", "surga")
    ch.add_node("pohon bidara", "surga")
    ch.add_node("salsabil", "surga")

    ch.add_node("sijjin", "neraka")
    ch.add_node("saqar", "neraka")
    ch.add_node("zaqqum", "neraka")
    ch.add_node("ladha", "neraka")

    ch.add_node("ufuk", "lokasi geografis")
    ch.add_node("kiblat", "lokasi geografis")
    ch.add_node("gurun", "lokasi geografis")
    ch.add_node("kota", "lokasi geografis")
    ch.add_node("gunung", "lokasi geografis")
    ch.add_node("tempat bersejarah", "lokasi geografis")

    ch.add_node("badar", "kota")
    ch.add_node("mekkah", "kota")
    ch.add_node("madinah", "kota")
    ch.add_node("babilonia", "kota")
    ch.add_node("hunain", "kota")
    ch.add_node("iram", "kota")

    ch.add_node("yastrib", "madinah")

    ch.add_node("shafa", "gunung")
    ch.add_node("marwah", "gunung")
    ch.add_node("arafat", "gunung")
    ch.add_node("sinai", "gunung")
    ch.add_node("judiy", "gunung")

    ch.add_node("mesir", "tempat bersejarah")
    ch.add_node("saba", "tempat bersejarah")
    ch.add_node("al-ahqaf", "tempat bersejarah")
    
    return ch

def load_label_list():
    labels = []
    
    labels.append("fenomena cuaca")
    labels.append("bahasa")
    labels.append("atribut fisik")
    labels.append("zat fisik")
    labels.append("artefak")
    labels.append("ciptaan yang hidup")
    labels.append("kitab suci")
    labels.append("allah")
    labels.append("singgasana allah")
    labels.append("tuhan palsu")
    labels.append("agama")
    labels.append("benda astronomi")
    labels.append("peristiwa")
    labels.append("lokasi")
    
    labels.append("petir")
    labels.append("guntur")
    labels.append("hujan")
    labels.append("awan")
    
    labels.append("arab")
    
    labels.append("warna")
    
    labels.append("hijau")

    labels.append("logam")
    labels.append("mineral")
    labels.append("minyak")
    labels.append("karang")
    labels.append("tanah")
    labels.append("mutiara")
    labels.append("kaca")
    labels.append("debu")
    labels.append("sutra")
    labels.append("tanah liat")
    
    labels.append("besi")
    labels.append("emas")
    labels.append("perak")
    labels.append("kuningan")
    
    labels.append("permata")
    
    labels.append("tempat ibadah")
    labels.append("persenjataan")
    labels.append("koin")
    labels.append("tinta")
    labels.append("pena")
    labels.append("tabut")
    labels.append("perahu")
    labels.append("kapal")
    labels.append("lampu")
    labels.append("kunci")
    labels.append("tangga")
    labels.append("bahtera")
    
    labels.append("masjid")
    labels.append("gereja")
    labels.append("biara")
    labels.append("sinagog")
    
    labels.append("masjidil haram")
    labels.append("masjidil aqsa")
    labels.append("kabah")
    
    labels.append("pisau")
    labels.append("panah")
    labels.append("baju besi")
    
    labels.append("objek organik")
    labels.append("makhluk hidup")
    
    labels.append("bagian tubuh")
    labels.append("penyakit")
    labels.append("makanan")
    labels.append("organisme biologis")
    labels.append("embrio")
    labels.append("darah")
    
    labels.append("tulang")
    labels.append("telinga")
    labels.append("mata")
    labels.append("jari")
    labels.append("dahi")
    labels.append("gombak")
    labels.append("jantung")
    labels.append("tumit")
    labels.append("usus")
    labels.append("bibir")
    labels.append("hidung")
    labels.append("lidah")
    labels.append("sayap")
    
    labels.append("tulang rusuk")
    
    labels.append("kusta")
    
    labels.append("daging")
    labels.append("madu")
    labels.append("susu")
    labels.append("garam")
    labels.append("roti")
    labels.append("wine")
    labels.append("gandum")
    labels.append("daging babi")
    labels.append("bangkai")
    
    labels.append("serangga")
    labels.append("burung")
    labels.append("tanaman")
    labels.append("binatang")
    labels.append("ikan")
    
    labels.append("belalang")
    labels.append("lebah")
    labels.append("laba-laba")
    labels.append("semut")
    labels.append("nyamuk")
    labels.append("lalat")
    
    labels.append("gagak")
    labels.append("puyuh")
    labels.append("hud-hud")
    
    labels.append("timun")
    labels.append("kurma")
    labels.append("ara")
    labels.append("bawang putih")
    labels.append("jahe")
    labels.append("anggur")
    labels.append("herba")
    labels.append("daun")
    labels.append("kacang")
    labels.append("zaitun")
    labels.append("bawang")
    labels.append("lentil")
    labels.append("pohon")
    labels.append("delima")
    
    labels.append("unta")
    labels.append("sapi")
    labels.append("babi")
    labels.append("kambing")
    labels.append("kuda")
    labels.append("singa")
    labels.append("keledai")
    labels.append("kera")
    labels.append("serigala")
    labels.append("katak")
    labels.append("domba")
    labels.append("ular")
    labels.append("anjing")
    
    labels.append("malaikat")
    labels.append("jin")
    labels.append("manusia")
    labels.append("daabbah")
    
    labels.append("jibril")
    labels.append("malaikat maut")
    labels.append("harut")
    labels.append("marut")
    labels.append("malik")
    labels.append("mikail")
    
    labels.append("setan")
    
    labels.append("iblis")
    
    labels.append("raja")
    labels.append("anak adam")
    labels.append("orang bersejarah")
    labels.append("orang-orang bersejarah")
    labels.append("nabi")
    
    labels.append("firaun")
    labels.append("uzair")
    labels.append("luqman")
    labels.append("jalut")
    labels.append("dzulkifli")
    labels.append("samiri")
    labels.append("talut")
    labels.append("qarun")
    labels.append("dzulkarnain")
    labels.append("haman")
    
    labels.append("aad")
    labels.append("tsamud")
    labels.append("madyan")
    labels.append("quraisy")
    labels.append("romawi")
    labels.append("anshar")
    labels.append("arab badui")
    labels.append("tubba")
    labels.append("bani israil")
    labels.append("yajuj dan majuj")
    labels.append("pemuda kahfi")
    labels.append("tentara bergajah")
    labels.append("pembuat parit")
    labels.append("penduduk rass")
    labels.append("penduduk aikah")
    
    labels.append("penduduk al-hijr")
    
    labels.append("abu lahab")
    
    labels.append("ummu jamil")
    
    labels.append("rasul")
    labels.append("zakaria")
    labels.append("yahya")
    labels.append("harun")
    labels.append("idris")
    labels.append("ilyasa")
    labels.append("ayyub")
    labels.append("adam")
    labels.append("daud")
    labels.append("sulaiman")
    labels.append("yusuf")
    labels.append("yaqub")
    labels.append("ishaq")
    
    labels.append("habil")
    labels.append("qabil")
    
    labels.append("israil")
    
    labels.append("azar")
    
    labels.append("muhammad")
    labels.append("isa")
    labels.append("ibrahim")
    labels.append("ismail")
    labels.append("salih")
    labels.append("hud")
    labels.append("syuaib")
    labels.append("yunus")
    labels.append("musa")
    labels.append("nuh")
    labels.append("luth")
    labels.append("ilyas")
    
    labels.append("ahmad")
    labels.append("zaid")
    
    labels.append("maryam")
    labels.append("messiah")
    
    labels.append("quran")
    labels.append("injil")
    labels.append("zabur")
    labels.append("taurat")
    
    labels.append("islam")
    labels.append("kristen")
    labels.append("yahudi")
    labels.append("shabiin")
    labels.append("majusi")
    
    labels.append("bulan")
    labels.append("bumi")
    labels.append("matahari")
    labels.append("bintang")
    labels.append("sirius")
    labels.append("gugus bintang")
    
    labels.append("uzza")
    labels.append("manat")
    labels.append("latta")
    labels.append("suwa")
    labels.append("baal")
    labels.append("nasr")
    labels.append("wadd")
    labels.append("yaghuts")
    labels.append("yauq")
    labels.append("sesembahan")
    
    labels.append("anak lembu emas")
    
    labels.append("peristiwa bersejarah")
    labels.append("peristiwa kalender")
    labels.append("peristiwa fisik")
    labels.append("peristiwa akhirat")
    
    labels.append("masa jahiliyah")
    
    labels.append("hari jumat")
    labels.append("hari sabtu")
    labels.append("haji")
    labels.append("umrah")
    labels.append("lailatul qadar")
    labels.append("bulan ramadhan")
    
    labels.append("fajar")
    
    labels.append("hari kebangkitan")
    labels.append("hari kiamat")
    
    labels.append("lokasi di akhirat")
    labels.append("lokasi geografis")
    
    labels.append("surga")
    labels.append("neraka")
    
    labels.append("firdaus")
    labels.append("adn")
    labels.append("pohon bidara")
    labels.append("salsabil")
    
    labels.append("sijjin")
    labels.append("saqar")
    labels.append("zaqqum")
    labels.append("ladha")
    
    labels.append("ufuk")
    labels.append("kiblat")
    labels.append("gurun")
    labels.append("kota")
    labels.append("gunung")
    labels.append("tempat bersejarah")
    
    labels.append("badar")
    labels.append("mekkah")
    labels.append("madinah")
    labels.append("babilonia")
    labels.append("hunain")
    labels.append("iram")
    
    labels.append("yastrib")
    
    labels.append("shafa")
    labels.append("marwah")
    labels.append("arafat")
    labels.append("sinai")
    labels.append("judiy")
    
    labels.append("mesir")
    labels.append("saba")
    labels.append("al-ahqaf")
    
    return labels

target_dic = {
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
}