import random
kelimeler = ["gözəl", "məlumat", "problem", "təmin etmək", "buraxmaq", "vaxt", "su", "etmək", "istifadə etmək", "yox", "görmək",
             "dərinizdən", "ən çox", "amma", "lirə" , "oynamaq", "çiçək", "şəhər", "yüksəlmək", "döyüşmək", "olmaq", "etmək" ,
             "güvən", "lazım", "müalicə", "vahid", "rahat", "soyuq", "orada", "kitab", "pay", "hesab", "bədən",
             "yer", "üstü", "sistem", "gözəl", "çəkilmə", "texnika", "yaxınlaşma", "il", "tarix", "dəqiq", "bacı",
             "cərimə", "əgər", "halbuki", "qaytarmaq", "vermək", "var", "qalan", "şəxs", "başqa", "dövr", "yenidən", "bunlar",
             "kitab", "hadisə", "olmaq", "sən", "dövlət", "ön", "ən çox", "baxmaq", "on", "bəyənmək", "bəzi", "başlamaq",
             "saxla", "bir-birini", "yox", "do", "su", "kimi", "dövlət", "sağ", "orta", "başqa", "böyük", "etmək",
             "yeni", "daha çox", "soruş", "onlar", "yandır", "hər ikisi", "həmişə", "səs", "anla", "yox", "saat", "necə",
             'bir' , 'və' , 'olmaq' , 'bu' , 'üçün' , 'bu' , 'mən' , 'demək' , 'çox' , 'edmək' , 'nə' , 'bəyənmək' , 'daha çox' , 'götürmək' ,
             'var', 'öz', 'gəl', 'birlikdə', 'vermək', 'amma', 'sonra', 'nə qədər', 'yer', 'çox', 'insanlar', 'yox', 'hər ' ,
             'istəyirəm', 'il', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmək', 'işləmək', 'şey', 'zəng etmək', 'o', 'bilmək', ' əl ', 'zaman',
             'ya' , 'uşaq' , 'iki' , 'bax' , 'iş' , 'in' , 'böyük' , 'yox' , 'start', 'yol', 'qal', 'niyə', 'sən' ,
             'mövzu', 'olmaq', 'yaxşı', 'qadın', 'ev', 'o', 'olmaq', 'demək', 'göz', 'lazımdır', 'dünya',
             'baş', 'dövlət', 'yan', 'keçmək', 'siz', 'onlar', 'yeni', 'əvvəl', 'başqa', 'dövlət', 'orta', 'su', 'girmək' ' , 'ölkə',
             'yemək', 'heç', 'hətta', 'necə', 'hamısı', 'əleyhinə', 'tapmaq', 'belə', 'yaşamaq', 'düşünmək', 'eyni', 'içəridə', ' lakin'',
             'şəxs', 'onlar', 'və ya', 'birinci', 'görə', 'ön', 'oğul', 'kimsə', 'forma', 'vacib', 'üz', 'hər ikisi', ' göstərmək ' , 'etmək' ,
             'alt', 'gətir', 'istifadə', 'çünki', 'yan', 'indi', 'kişi', 'onun', 'başqası', 'indi', 'üstü', 'səs', 'həmişə ' ,
             'sağ', 'durmaq', 'qız', 'hamısı', 'cəlb etmək', 'danışmaq', 'pul', 'anlamaq', 'ana', 'az', 'bəzi', 'ata', 'həyat ' ,
             'yalnız', 'kiçik', 'daha çox', 'məlumat', 'an', 'soruş', 'o', 'o', 'yenidən', 'təmin et', 'nəticə', 'istifadə edilmiş', 'xarici ' ,
             'ad', 'o', 'müddət', 'qayıt', 'açıq', 'oturmaq', 'demək', 'çıxmaq', 'dərhal', 'zaman', 'yaş', 'problem', 'dövlət' ' ,
             'var', 'sətir', 'yazmaq', 'faiz', 'ay', 'atmaq', 'saxlamaq', 'bu', 'hadisə', 'düşmək', 'eşitmək', 'söz', 'gözəl ' ,
             'sevmək' 'bir qədər' 'çətin' 'çıxmaq' 'çətin' 'çıxmaq' 'o' 'qoymaq' 'bir' 'sistem' 'birlikdə' 'verilmək' 'kim' 'almaq "gənc",
             'qapı', 'kitab', 'on', 'burada', 'gecə', 'tarla', 'bir-birimizə', 'burada', 'gözləyin', 'uzun', 'yox', 'bu gün', ' dövr'',
             'dost', 'məhsul', 'ailə', 'üç', 'oxumaq', 'kişi', 'hamı', 'güc', 'bəlkə', 'doğru', 'tam', 'əlaqəli', 'münasibət ' ,
             'ətraf', 'köhnə', 'axtarış', 'həyat', 'ictimai', 'yaxınlıq', 'küçə', 'bəy', 'tarix', 'mülkiyyət', 'bölmə', 'özəl', 'səbəb ' ,
             'heç kim', 'çox deyil', 'dəyər', 'lazımdır', 'qabaqda', 'məna', 'yüksək', 'bank', 'dəfə', 'ayaq', 'daşıma', 'geri', ' cəmiyyət'',
             'avtomobil', 'eşya', 'növ', 'qərar', 'görülən', 'hava', 'nömrə', 'fərqli', 'qrup', 'otaq', 'forma', 'forma', 'xəbərlər' ' ,
             'tanrı', 'həmçinin', 'gəlir', 'az', 'sual', 'geri', 'qazanmaq', 'poçt', 'məktəb', 'on', 'öyrənmək', 'sürüş',
             'dil', 'şirkət', 'mənbə', 'bitir', 'proqram', 'davam et', 'hərəkət et', 'rəng', 'açılış', 'doğru', 'inan',
             'təhsil', 'bucaq', 'parça', 'qəzet', 'yaratmaq', 'mövzu', 'dəyər', 'bilmək', 'struktur', 'doktor', 'gəlir',
             'vəzifə' 'məqsəd' 'region' 'film' '' 'müştəri' 'artıq' 'telefon' 'təlim' 'dəniz' 'ikinci',
             'qalx', 'hətta', 'təsir', 'inkişaf etmək', 'keçmək', 'bədən', 'düşüncə', 'milyon', 'oynamaq', 'dəyişiklik', 'əsas',
             'yaratmaq', 'çatmaq', 'düşünmək', 'keçmək', 'mədəniyyət', 'qurmaq', 'amma', 'buna', 'rəsm etmək', 'işıqlandırmaq', 'içmək',
             'xanım', 'xidmət', 'ehtiyac', 'nöqtə', 'istiqamət', 'bəli', 'oyun', 'artırma', 'yenidən yükləmə', 'proses', 'qısa', 'asan',
             'hansı', 'qiymət', 'əslində', 'qəbul edirəm', 'orada', 'diqqət', 'uzaq', 'kompüter', 'gələcək', 'görünür',
             məsələn' , 'oğul' , 'dinlə' , 'uyğun' 'lirə' 'istehsal' 'dəqiqə' 'unut' 'gəzinti' 'belə' 'pis',
             'avtomobil', 'ağız', 'hiss et', 'tətbiq et', 'hələ', 'nümunə', 'çox'' , 'saat' , 'dərəcə' , 'mümkün' , 'belə',
             'divar', 'on', 'incəsənət', 'əsas', 'xəstəlik', 'tələbə', 'televiziya', 'metod', 'masa', 'ölüm', 'komanda', 'üst',
             'baş', 'musiqi', 'ayrılmaq', 'enerji', 'universitet', 'idman', 'mehriban', 'ruh', 'baxmayaraq', 'hissə', 'ölüm',
             'daimi', 'sağlamlıq', 'müxtəlif', 'bundan', 'hiss', 'halbuki', 'səhər', 'internet', 'texniki', 'çıxış',
             'mərkəz', 'ambians', 'əvəzində', 'səviyyə', 'kənd', 'idarə', 'aşağı', 'cavab', 'yatmaq', 'torpaq','', 'axşam',
             'araşdırma', 'götürmək', 'iştirak etmək', 'əks halda', 'tapmaq', 'ödəmək', 'sanki', 'qan', 'xəstə', 'şəhər', 'enmək',
             'indiki', 'məlum', 'həftə', 'trafik', 'hesab', 'avtomobil', 'yadplanetli', 'davranış', 'mətbəx', 'şəhər', 'bəzən',
             'müəyyən', 'ayrı', 'qiymət', 'haqqında', 'çıxarmaq', 'qol', 'solo', 'hazırlamaq', 'şüşə', 'nəhayət', 'yavaş',
             'zəruri', 'əhəmiyyət', 'ər', 'yalan', 'aktiv', 'sənət', 'faiz', 'siz', 'satış', 'in', 'təbii', 'öz',
             'iqtisadi', 'ağrı', 'yox', 'qorumaq', 'mərtəbə', 'iqtisadiyyat', 'ümumi', 'müəyyən et', 'foto', 'heyvan', 'müharibə',
             'mal', 'saç', 'itirmək', 'qalıq', 'dəyişiklik', 'dörd', 'həqiqətən', 'səhifə', 'texnologiya', 'qurum', 'beş',
             'sektor', 'geniş', 'kağız', 'ətir', 'sağ', 'isti', 'əsr', 'küçə', 'bazar', 'sürücü', 'istifadə', 'sinif',
             'sevgi', 'doğulmuş', 'ağır', 'yenidən', 'günəş', 'siqaret', 'ağac', 'söz', 'bina', 'arvad', 'qaçmaq', 'partiya',' yataq ',
             'müəllif', 'qulaq', 'müəllim', 'səbəb', 'sol', 'yaxşı' 'yağ', 'çünki' 'anlaşılır', 'gəlmək', 'gülmək', 'qayda',
             'satmaq', 'şeir', 'göndərmək', 'uğur', 'möhkəm', 'hökumət', 'ürək', 'hack', 'layihə', 'lazımdır', 'sürət', 'künc',
             'vur', 'model', 'balıq', 'bazar', 'fikir', 'burada', 'hazırlayın', 'miqdar', 'birinci', 'kvadrat', 'ölçü',
             'seçmək', 'tətbiq etmək', 'bağ', 'sevgi', 'çörək', 'boyu', 'qaçmaq', 'dolu', 'quruluş', 'demək', 'qorxu',
             'kömək', 'görüş', 'əşyalar', 'gözəl', 'it', 'məşhur', 'böyümək', 'ətrafında gəzmək', 'olduqca', 'üstəlik',
             'yaşamaq', 'ağ', 'arzu etmək', 'arda', 'sınamaq', 'bacı', 'çəkilmə', 'harada', 'oğurlamaq', 'icazə', 'qorxu',
             'işğal', 'polis', 'yalnız', 'izah et', 'fikir', 'tez', 'pəncərə', 'sövdələşmə', 'daş', 'yanğın', 'fərq',
             'kifayətdir', 'ən çox', 'bəzi', 'şərt', 'qonşuluq', 'lazımdır', 'taxıl', 'istehsal etmək', 'üstündə', 'dayanmaq', 'nazik',
             'neçə', 'ümumi', 'növ', 'şəkil', 'beri', 'dərs', 'sədr', 'kontrakt', 'uzaqlaşma', 'sayı', 'dəfə',
             'olmaq', 'qərb', 'diqqət etmək', 'hər hansı' 'sinema' 'fərqli' 'hədəf' 'yuxu' 'dost' 'yanmaq',
             'anlayış', 'usta', 'mətbuat', 'kənar', 'nəzarət', 'dönüş', 'din', 'güclü', 'hələ', 'plan', 'beyin',
             'elektrik', 'arvad', 'üstü', 'ət', 'təmin edilmiş', 'danışmaq', 'xətt', 'uçmaq', 'üzv', 'dəri', 'ruh',
             'əziz', 'yanaşma', 'proses', 'bax', 'elm', 'irəli', 'ifadə', 'bədən', 'xatırla', 'qəza',
             'boyu', 'dağ', 'yaxın', 'addım', 'ciddi', 'həll', 'impress', 'bələdiyyə', 'inkişaf', 'seçki',
             'ağlama', 'əlaqəli', 'konsept', 'artım', 'fəaliyyət', 'zərər' 'dərin' 'zal' 'bir növ', 'kəsilmiş',
             'izləmək', 'birdən', 'tərkib etmək', 'saymaq', 'toplamaq', 'ütmək', 'qışqırmaq', 'məsuliyyət', 'hərəkət etmək',
             'məktub', 'soyuq', 'canlı', 'idikeylem', 'maşın', 'istifadə etmək', 'köhnə', 'boş', 'görəsən', 'kibrit', 'menecer',
             'gətiriləcək', 'metre', 'tutulacaq', 'keyfiyyət' 'bitki' 'dəyişiklik' 'dərman' 'kredit' 'qanun' 'uğurlu',
             'bir', 'imkan', 'cəza', 'hər şey', 'imtahan', 'top', 'ekspert', 'doldurma', 'kanal', 'boşluq', 'uyğun',
             'illik' , 'beləliklə' , 'yazmaq' , 'aid olmaq' , 'barmaq' , 'saymaq' , 'atmaq' , 'müəyyən etmək' , 'normal' , 'hele',
             'prinsip', 'qırmızı', 'rol', 'mahnı', 'element', 'hazır', 'oxşamaq', 'nəsə', 'müəllim', 'oğlan', 'gündəlik', 'siyasət',
             'cinayət', 'niyə', 'səhnə', 'ilişib', 'özəl', 'oturmaq', 'saxla', 'artist', 'üstünlük', 'uzamaq', 'səhnə',
             'əlavə et', 'meşə', 'ayrı', 'sifariş', 'faiz', 'nəzarətçi', 'həmişə', 'hekayə', 'hüceyrə', 'ora', 'roman',
             'vergi' 'yandır' 'böyük qardaş' 'mətbuat' 'dəstək' 'wear' 'səhv' 'sərhəd' 'birlik' 'iş' 'görüşmək',
             'yarı', 'kafi', 'fərdi', 'qaranlıq' 'avtobus' 'sənaye' 'körpə' 'vətəndaş' 'nazir' 'zaman' 'darı',
             'reklam', 'yüksəlmə', 'ölçü', 'jurnal', 'inflyasiya', 'sosial', 'kimsə', 'keçmiş', 'xəstəxana', 'olma',
             'görüş', 'jurnalist', 'daxili', 'iman', 'ixtisas', 'bitmiş', 'bitirmək', 'yer almaq', 'giriş', 'rahat',
             'cəmi', 'birlikdə', 'mağaza', 'gizli', 'oxşar', 'dəri', 'çevirmək', 'döyüş', 'problem', 'xidmət', 'müalicə',
             'yaşıl', 'nazirlik', 'zülm', 'reaksiya', 'cümlə', 'istək', 'azadlıq', 'gen', 'kimlik', 'məsəl', 'üçüncü',
             'müəyyən et', 'qiymətləndirmək', 'maraqlı', 'sürücü', 'süd', 'tutmaq', 'eşya', 'beynəlxalq', 'namizəd',
             'çəki', 'milyard', 'sağlam', 'sıxıntı', 'tanrı', 'rəftar', 'sosial', 'nəşriyyat', 'diqqətli', 'son dərəcə',
             'topla', 'investisiya et', 'işıqlandırmaq', 'qarışdırmaq', 'təhlükə', 'zaman', 'dairə', 'imkan', 'proses', 'qarışdırmaq',
             'töhfə', 'hekayə', 'tamamilə', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'faiz', 'əlbəttə', 'işçi', 'iş',
             'qısaca', 'mağaza', 'media', 'çünki', 'artım', 'çıxarıldı', 'ictimai', 'sığorta', 'yay', 'ürək', 'sənəd',
             'səy', 'hər gün', 'ekspress', 'risk', 'danışmaq', 'söz', 'demokratiya', 'duz', 'məscid', 'yaş', 'aşağı',
             'ətrafında', 'tezliklə', 'imkan', 'orqan', 'öldürmək', 'başqa', 'il', 'çürümək', 'baxmaq', 'meyvə', 'asmaq',
             'şirin', 'ayaq', 'dəyişiklik', 'qanun', 'külək', 'respublika', 'inkişaf etmək', 'üslub', 'yeddi', 'azalmaq',
             'qoşulmaq', 'mobil telefon', 'əlaqə', 'menecer', 'otel', 'qaçmaq', 'zövq almaq', 'sürüş', 'təhlükəsizlik', 'qanun',
             'make', 'modern', 'oxucu', 'gun', 'tələb', 'ulduz', 'intensiv', 'əsgər', 'sadə', 'adlanacaq', 'qaz',
             'tətbiq', 'istehsal', 'bəyannamə', 'yemək', 'dünən', 'bax', 'yanlaşma', 'alış-veriş', 'şüur', 'çərçivə',
             'lazımdır', 'mövcuddur', 'istehlakçı', 'uzatmaq', 'to', 'at', 'qoşulmaq', 'məsələn', 'demək olar', 'sayt',
             'kömək', 'bacı', 'çiçək', 'hamısı', 'hörmət', 'ödəmək', 'istedad', 'ağırlıq', 'pay', 'çətin', 'bundan başqa',
             'çay', 'get', 'əmin', 'zəngin', 'heç vaxt', 'söz', 'təşkilat', 'ticarət', 'edmək', 'boyun', 'cihaz',
             'balans', 'gedəcək', 'geriyə', 'çünki', 'qəhvə', 'əzələ', 'montaj', 'başqa', 'işləmək', 'ünvan', 'müəyyən ediləcək',
             'paşa', 'temperatur', 'yaxşı', 'güvən', 'marka', 'yarpaq', 'fayda', 'yaymaq', 'axın', 'çəkmək', 'düşünmək',
             'ürək', 'arzu', 'tərəqqi', 'şərab', 'yuxarıda', 'qızıl', 'arandırmaq', 'almaq', 'təqdim etmək', 'təmiz',
             'vitamin', 'əlavə', 'gec', 'aktyor', 'yumurta', 'həddindən artıq', 'hərəkət', 'istəyək', 'kəsmə', 'böhran', 'vahid',
             'söndür'
             ]


def kelime_sec():
    return random.choice(kelimeler)
