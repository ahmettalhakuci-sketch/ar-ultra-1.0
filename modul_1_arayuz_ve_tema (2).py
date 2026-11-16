# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v4.0 — MODÜL 1: KOYU LACİVERT TEMA MOTORU, 3D ÇEVİRMELİ KART (FLIP CARD)
CSS TASARIMI, 150 ÇOK DİLLİ KART VE 240 SİSTEM KISAYOLU (modul_1_arayuz_ve_tema.py)
==============================================================================
"""
import streamlit as st

UYGULAMA_ADI = "Ar AI Studio"
UYGULAMA_SURUMU = "v4.0 Enterprise Modular"
GELISTIRICI_ADI = "Ahmet"
import os as _os
import tempfile as _tempfile

_VERI_DIZINI = _os.path.dirname(_os.path.abspath(__file__))
if not _os.access(_VERI_DIZINI, _os.W_OK):
    _VERI_DIZINI = _tempfile.gettempdir()

JSON_DOSYA_ADI = _os.path.join(_VERI_DIZINI, "komutlar.json")
SOHBET_DOSYA_ADI = _os.path.join(_VERI_DIZINI, "sohbet_gecmisi.json")
NOTLAR_DOSYA_ADI = _os.path.join(_VERI_DIZINI, "ahmet_notlar.json")
DERS_NOTLARI_DOSYASI = _os.path.join(_VERI_DIZINI, "ahmet_ders_notlari.json")
SORU_TAKIP_DOSYASI = _os.path.join(_VERI_DIZINI, "ahmet_soru_takip.json")

TEMA_PALETLERI = {   'Derin Lacivert (Klasik Ar)': {   'accent_blue': '#0ea5e9',
                                      'accent_neon': '#38bdf8',
                                      'accent_purple': '#1d4ed8',
                                      'accent_rose': '#60a5fa',
                                      'bg_primary': '#03091a',
                                      'bg_secondary': '#07142e',
                                      'card_bg': '#0b1e42',
                                      'text_main': '#ffffff',
                                      'text_sub': '#dbeafe'},
    'Kraliyet Moru & Altın': {   'accent_blue': '#c084fc',
                                 'accent_neon': '#f59e0b',
                                 'accent_purple': '#9333ea',
                                 'accent_rose': '#ec4899',
                                 'bg_primary': '#090414',
                                 'bg_secondary': '#130926',
                                 'card_bg': '#1d1038',
                                 'text_main': '#ffffff',
                                 'text_sub': '#f3e8ff'},
    'Kızıl Süpernova': {   'accent_blue': '#f43f5e',
                           'accent_neon': '#fb7185',
                           'accent_purple': '#e11d48',
                           'accent_rose': '#38bdf8',
                           'bg_primary': '#110408',
                           'bg_secondary': '#1f0810',
                           'card_bg': '#2d0d18',
                           'text_main': '#ffffff',
                           'text_sub': '#ffe4e6'},
    'Okyanus Derinliği': {   'accent_blue': '#0ea5e9',
                             'accent_neon': '#38bdf8',
                             'accent_purple': '#2563eb',
                             'accent_rose': '#00f5d4',
                             'bg_primary': '#020813',
                             'bg_secondary': '#071426',
                             'card_bg': '#0c203b',
                             'text_main': '#ffffff',
                             'text_sub': '#e0f2fe'},
    'Saf Koyu Kontrast (OLED)': {   'accent_blue': '#60a5fa',
                                    'accent_neon': '#00ffcc',
                                    'accent_purple': '#818cf8',
                                    'accent_rose': '#fb7185',
                                    'bg_primary': '#000000',
                                    'bg_secondary': '#08080c',
                                    'card_bg': '#11131a',
                                    'text_main': '#ffffff',
                                    'text_sub': '#f8fafc'},
    'Siber Neon (Koyu Mavi)': {   'accent_blue': '#38bdf8',
                                  'accent_neon': '#00f5d4',
                                  'accent_purple': '#6366f1',
                                  'accent_rose': '#f43f5e',
                                  'bg_primary': '#040711',
                                  'bg_secondary': '#0b1120',
                                  'card_bg': '#0f172a',
                                  'text_main': '#ffffff',
                                  'text_sub': '#e2e8f0'},
    'Zümrüt Matriks': {   'accent_blue': '#34d399',
                          'accent_neon': '#10b981',
                          'accent_purple': '#059669',
                          'accent_rose': '#f59e0b',
                          'bg_primary': '#020b08',
                          'bg_secondary': '#061812',
                          'card_bg': '#0a241b',
                          'text_main': '#ffffff',
                          'text_sub': '#d1fae5'}}

DIL_EGITIM_KARTLARI = [   {   'bengalce': 'কৃত্রিম বুদ্ধিমত্তা (Kritrim buddhimotta)',
        'cince': '人工智能 (Réngōng zhìnéng)',
        'id': 1,
        'ingilizce': 'Artificial Intelligence (#1)',
        'kategori': 'Teknoloji',
        'ornek_cumle': 'Ahmet uses artificial intelligence in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Yapay Zeka'},
    {   'bengalce': 'স্বায়ত্তশাসিত ড্রোন (Sbayottoshasito drone)',
        'cince': '自主无人机 (Zìzhǔ wúrénjī)',
        'id': 2,
        'ingilizce': 'Autonomous Drone (#2)',
        'kategori': 'Havacılık',
        'ornek_cumle': 'Ahmet uses autonomous drone in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Otonom İnsansız Hava Aracı'},
    {   'bengalce': 'সফটওয়্যার ইঞ্জিনিয়ারিং (Software engineering)',
        'cince': '软件工程 (Ruǎnjiàn gōngchéng)',
        'id': 3,
        'ingilizce': 'Software Engineering (#3)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses software engineering in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Yazılım Mühendisliği'},
    {   'bengalce': 'মেশিন লার্নিং (Machine learning)',
        'cince': '机器学习 (Jīqì xuéxí)',
        'id': 4,
        'ingilizce': 'Machine Learning (#4)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses machine learning in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Makine Öğrenmesi'},
    {   'bengalce': 'নিউরাল নেটওয়ার্ক (Neural network)',
        'cince': '神经网络 (Shénjīng wǎngluò)',
        'id': 5,
        'ingilizce': 'Neural Network (#5)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses neural network in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Sinir Ağı'},
    {   'bengalce': 'কম্পিউটার ভিশন (Computer vision)',
        'cince': '计算机视觉 (Jìsuànjī shìjué)',
        'id': 6,
        'ingilizce': 'Computer Vision (#6)',
        'kategori': 'Görüntü İşleme',
        'ornek_cumle': 'Ahmet uses computer vision in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Bilgisayarlı Görü'},
    {   'bengalce': 'এম্বেডেড সিস্টেম (Embedded system)',
        'cince': '嵌入式系统 (Qiànrùshì xìtǒng)',
        'id': 7,
        'ingilizce': 'Embedded Systems (#7)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses embedded systems in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Gömülü Sistemler'},
    {   'bengalce': 'মাইক্রোকন্ট্রোলার (Microcontroller)',
        'cince': '微控制器 (Wēi kòngzhìqì)',
        'id': 8,
        'ingilizce': 'Microcontroller (#8)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses microcontroller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Mikrodenetleyici'},
    {   'bengalce': 'আল্ট্রাসনিক সেন্সর (Ultrasonic sensor)',
        'cince': '超声波传感器 (Chāoshēngbō chuángǎnqì)',
        'id': 9,
        'ingilizce': 'Ultrasonic Sensor (#9)',
        'kategori': 'Sensör',
        'ornek_cumle': 'Ahmet uses ultrasonic sensor in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Ultrasonik Sensör'},
    {   'bengalce': 'থ্রিডি প্রিন্টিং (3D printing)',
        'cince': '3D打印 (3D dǎyìn)',
        'id': 10,
        'ingilizce': 'Three Dimensional Printing (#10)',
        'kategori': 'Üretim',
        'ornek_cumle': 'Ahmet uses three dimensional printing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Üç Boyutlu Baskı'},
    {   'bengalce': 'বর্গমূল (Borgomul)',
        'cince': '平方根 (Píngfānggēn)',
        'id': 11,
        'ingilizce': 'Square Root (#11)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses square root in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Karekök'},
    {   'bengalce': 'মৌলিক সংখ্যা (Moulik songkha)',
        'cince': '质数 (Zhìshù)',
        'id': 12,
        'ingilizce': 'Prime Number (#12)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses prime number in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Asal Sayı'},
    {   'bengalce': 'রৈখিক সমীকরণ (Roikhik somikoron)',
        'cince': '线性方程 (Xiànxìng fāngchéng)',
        'id': 13,
        'ingilizce': 'Linear Equation (#13)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses linear equation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Doğrusal Denklem'},
    {   'bengalce': 'গরিষ্ঠ সাধারণ গুণনীয়ক (Goshagu)',
        'cince': '最大公约数 (Zuìdà gōngyuēshù)',
        'id': 14,
        'ingilizce': 'Greatest Common Divisor (#14)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses greatest common divisor in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'En Büyük Ortak Bölen (EBOB)'},
    {   'bengalce': 'লঘিষ্ঠ সাধারণ গুণিতক (Loshagu)',
        'cince': '最小公倍数 (Zuìxiǎo gōngbèishù)',
        'id': 15,
        'ingilizce': 'Least Common Multiple (#15)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses least common multiple in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'En Küçük Ortak Kat (EKOK)'},
    {   'bengalce': 'সূচক (Suchok)',
        'cince': '幂运算 (Mì yùnsuàn)',
        'id': 16,
        'ingilizce': 'Exponentiation (#16)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses exponentiation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Üs Alma / Üslü Sayılar'},
    {   'bengalce': 'পিথাগোরাসের উপপাদ্য (Pithagoraser upopaddo)',
        'cince': '勾股定理 (Gōugǔ dìnglǐ)',
        'id': 17,
        'ingilizce': 'Pythagorean Theorem (#17)',
        'kategori': 'Geometri',
        'ornek_cumle': 'Ahmet uses pythagorean theorem in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Pisagor Teoremi'},
    {   'bengalce': 'অধ্যবসায় এবং শৃঙ্খলা (Oddhobosay ebong srinkhola)',
        'cince': '毅力与纪律 (Yìlì yǔ jìlǜ)',
        'id': 18,
        'ingilizce': 'Perseverance and Discipline (#18)',
        'kategori': 'Kişisel Gelişim',
        'ornek_cumle': 'Ahmet uses perseverance and discipline in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Azim ve Disiplin'},
    {   'bengalce': 'বৈজ্ঞানিক গবেষণা (Boigganik gobeshona)',
        'cince': '科学研究 (Kēxué yánjiū)',
        'id': 19,
        'ingilizce': 'Scientific Research (#19)',
        'kategori': 'Bilim',
        'ornek_cumle': 'Ahmet uses scientific research in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bilimsel Araştırma'},
    {   'bengalce': 'অ্যালগরিদম অপ্টিমাইজেশন (Algorithm optimization)',
        'cince': '算法优化 (Suànfǎ yōuhuà)',
        'id': 20,
        'ingilizce': 'Algorithm Optimization (#20)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses algorithm optimization in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Algoritma Optimizasyonu'},
    {   'bengalce': 'ফ্লাইট কন্ট্রোলার (Flight controller)',
        'cince': '飞行控制器 (Fēixíng kòngzhìqì)',
        'id': 21,
        'ingilizce': 'Flight Controller (#21)',
        'kategori': 'İHA / Drone',
        'ornek_cumle': 'Ahmet uses flight controller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Uçuş Kontrol Kartı'},
    {   'bengalce': 'ব্যাটারি ম্যানেজমেন্ট (Battery management)',
        'cince': '电池管理 (Diànchí guǎnlǐ)',
        'id': 22,
        'ingilizce': 'Battery Management (#22)',
        'kategori': 'Elektronik',
        'ornek_cumle': 'Ahmet uses battery management in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Batarya Yönetimi'},
    {   'bengalce': 'সিগন্যাল প্রসেসিং (Signal processing)',
        'cince': '信号处理 (Xìnhào chǔlǐ)',
        'id': 23,
        'ingilizce': 'Signal Processing (#23)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses signal processing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Sinyal İşleme'},
    {   'bengalce': 'ডেটা স্ট্রাকচার (Data structure)',
        'cince': '数据结构 (Shùjù jiégòu)',
        'id': 24,
        'ingilizce': 'Data Structure (#24)',
        'kategori': 'Bilgisayar Bilimi',
        'ornek_cumle': 'Ahmet uses data structure in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Veri Yapısı'},
    {   'bengalce': 'অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)',
        'cince': '面向对象编程 (Miànxiàng duìxiàng biānchéng)',
        'id': 25,
        'ingilizce': 'Object Oriented Programming (#25)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses object oriented programming in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Nesne Yönelimli Programlama'},
    {   'bengalce': 'সাইবার নিরাপত্তা (Cyber nirapotta)',
        'cince': '网络安全 (Wǎngluò ānquán)',
        'id': 26,
        'ingilizce': 'Cyber Security (#26)',
        'kategori': 'Güvenlik',
        'ornek_cumle': 'Ahmet uses cyber security in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Siber Güvenlik'},
    {   'bengalce': 'ক্লাউড কম্পিউটিং (Cloud computing)',
        'cince': '云计算 (Yún jìsuàn)',
        'id': 27,
        'ingilizce': 'Cloud Computing (#27)',
        'kategori': 'Sistem',
        'ornek_cumle': 'Ahmet uses cloud computing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bulut Bilişim'},
    {   'bengalce': 'ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP)',
        'cince': '自然语言处理 (Zìrán yǔyán chǔlǐ)',
        'id': 28,
        'ingilizce': 'Natural Language Processing (#28)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses natural language processing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Doğal Dil İşleme'},
    {   'bengalce': 'রোবোটিক্স এবং অটোমেশন (Robotics)',
        'cince': '机器人与自动化 (Jīqìrén yǔ zìdònghuà)',
        'id': 29,
        'ingilizce': 'Robotics and Automation (#29)',
        'kategori': 'Robotik',
        'ornek_cumle': 'Ahmet uses robotics and automation in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Robotik ve Otomasyon'},
    {   'bengalce': 'অ্যারোডাইনামিক্স (Aerodynamics)',
        'cince': '空气动力学 (Kōngqì dònglìxué)',
        'id': 30,
        'ingilizce': 'Aerodynamics (#30)',
        'kategori': 'Fizik',
        'ornek_cumle': 'Ahmet uses aerodynamics in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Orta',
        'turkce': 'Aerodinamik'},
    {   'bengalce': 'কৃত্রিম বুদ্ধিমত্তা (Kritrim buddhimotta)',
        'cince': '人工智能 (Réngōng zhìnéng)',
        'id': 31,
        'ingilizce': 'Artificial Intelligence (#31)',
        'kategori': 'Teknoloji',
        'ornek_cumle': 'Ahmet uses artificial intelligence in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Yapay Zeka'},
    {   'bengalce': 'স্বায়ত্তশাসিত ড্রোন (Sbayottoshasito drone)',
        'cince': '自主无人机 (Zìzhǔ wúrénjī)',
        'id': 32,
        'ingilizce': 'Autonomous Drone (#32)',
        'kategori': 'Havacılık',
        'ornek_cumle': 'Ahmet uses autonomous drone in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Otonom İnsansız Hava Aracı'},
    {   'bengalce': 'সফটওয়্যার ইঞ্জিনিয়ারিং (Software engineering)',
        'cince': '软件工程 (Ruǎnjiàn gōngchéng)',
        'id': 33,
        'ingilizce': 'Software Engineering (#33)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses software engineering in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Yazılım Mühendisliği'},
    {   'bengalce': 'মেশিন লার্নিং (Machine learning)',
        'cince': '机器学习 (Jīqì xuéxí)',
        'id': 34,
        'ingilizce': 'Machine Learning (#34)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses machine learning in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Makine Öğrenmesi'},
    {   'bengalce': 'নিউরাল নেটওয়ার্ক (Neural network)',
        'cince': '神经网络 (Shénjīng wǎngluò)',
        'id': 35,
        'ingilizce': 'Neural Network (#35)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses neural network in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Sinir Ağı'},
    {   'bengalce': 'কম্পিউটার ভিশন (Computer vision)',
        'cince': '计算机视觉 (Jìsuànjī shìjué)',
        'id': 36,
        'ingilizce': 'Computer Vision (#36)',
        'kategori': 'Görüntü İşleme',
        'ornek_cumle': 'Ahmet uses computer vision in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Bilgisayarlı Görü'},
    {   'bengalce': 'এম্বেডেড সিস্টেম (Embedded system)',
        'cince': '嵌入式系统 (Qiànrùshì xìtǒng)',
        'id': 37,
        'ingilizce': 'Embedded Systems (#37)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses embedded systems in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Gömülü Sistemler'},
    {   'bengalce': 'মাইক্রোকন্ট্রোলার (Microcontroller)',
        'cince': '微控制器 (Wēi kòngzhìqì)',
        'id': 38,
        'ingilizce': 'Microcontroller (#38)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses microcontroller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Mikrodenetleyici'},
    {   'bengalce': 'আল্ট্রাসনিক সেন্সর (Ultrasonic sensor)',
        'cince': '超声波传感器 (Chāoshēngbō chuángǎnqì)',
        'id': 39,
        'ingilizce': 'Ultrasonic Sensor (#39)',
        'kategori': 'Sensör',
        'ornek_cumle': 'Ahmet uses ultrasonic sensor in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Ultrasonik Sensör'},
    {   'bengalce': 'থ্রিডি প্রিন্টিং (3D printing)',
        'cince': '3D打印 (3D dǎyìn)',
        'id': 40,
        'ingilizce': 'Three Dimensional Printing (#40)',
        'kategori': 'Üretim',
        'ornek_cumle': 'Ahmet uses three dimensional printing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Üç Boyutlu Baskı'},
    {   'bengalce': 'বর্গমূল (Borgomul)',
        'cince': '平方根 (Píngfānggēn)',
        'id': 41,
        'ingilizce': 'Square Root (#41)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses square root in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Temel',
        'turkce': 'Karekök'},
    {   'bengalce': 'মৌলিক সংখ্যা (Moulik songkha)',
        'cince': '质数 (Zhìshù)',
        'id': 42,
        'ingilizce': 'Prime Number (#42)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses prime number in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Orta',
        'turkce': 'Asal Sayı'},
    {   'bengalce': 'রৈখিক সমীকরণ (Roikhik somikoron)',
        'cince': '线性方程 (Xiànxìng fāngchéng)',
        'id': 43,
        'ingilizce': 'Linear Equation (#43)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses linear equation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Doğrusal Denklem'},
    {   'bengalce': 'গরিষ্ঠ সাধারণ গুণনীয়ক (Goshagu)',
        'cince': '最大公约数 (Zuìdà gōngyuēshù)',
        'id': 44,
        'ingilizce': 'Greatest Common Divisor (#44)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses greatest common divisor in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'En Büyük Ortak Bölen (EBOB)'},
    {   'bengalce': 'লঘিষ্ঠ সাধারণ গুণিতক (Loshagu)',
        'cince': '最小公倍数 (Zuìxiǎo gōngbèishù)',
        'id': 45,
        'ingilizce': 'Least Common Multiple (#45)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses least common multiple in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'En Küçük Ortak Kat (EKOK)'},
    {   'bengalce': 'সূচক (Suchok)',
        'cince': '幂运算 (Mì yùnsuàn)',
        'id': 46,
        'ingilizce': 'Exponentiation (#46)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses exponentiation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Üs Alma / Üslü Sayılar'},
    {   'bengalce': 'পিথাগোরাসের উপপাদ্য (Pithagoraser upopaddo)',
        'cince': '勾股定理 (Gōugǔ dìnglǐ)',
        'id': 47,
        'ingilizce': 'Pythagorean Theorem (#47)',
        'kategori': 'Geometri',
        'ornek_cumle': 'Ahmet uses pythagorean theorem in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Pisagor Teoremi'},
    {   'bengalce': 'অধ্যবসায় এবং শৃঙ্খলা (Oddhobosay ebong srinkhola)',
        'cince': '毅力与纪律 (Yìlì yǔ jìlǜ)',
        'id': 48,
        'ingilizce': 'Perseverance and Discipline (#48)',
        'kategori': 'Kişisel Gelişim',
        'ornek_cumle': 'Ahmet uses perseverance and discipline in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Azim ve Disiplin'},
    {   'bengalce': 'বৈজ্ঞানিক গবেষণা (Boigganik gobeshona)',
        'cince': '科学研究 (Kēxué yánjiū)',
        'id': 49,
        'ingilizce': 'Scientific Research (#49)',
        'kategori': 'Bilim',
        'ornek_cumle': 'Ahmet uses scientific research in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Bilimsel Araştırma'},
    {   'bengalce': 'অ্যালগরিদম অপ্টিমাইজেশন (Algorithm optimization)',
        'cince': '算法优化 (Suànfǎ yōuhuà)',
        'id': 50,
        'ingilizce': 'Algorithm Optimization (#50)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses algorithm optimization in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Algoritma Optimizasyonu'},
    {   'bengalce': 'ফ্লাইট কন্ট্রোলার (Flight controller)',
        'cince': '飞行控制器 (Fēixíng kòngzhìqì)',
        'id': 51,
        'ingilizce': 'Flight Controller (#51)',
        'kategori': 'İHA / Drone',
        'ornek_cumle': 'Ahmet uses flight controller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Uçuş Kontrol Kartı'},
    {   'bengalce': 'ব্যাটারি ম্যানেজমেন্ট (Battery management)',
        'cince': '电池管理 (Diànchí guǎnlǐ)',
        'id': 52,
        'ingilizce': 'Battery Management (#52)',
        'kategori': 'Elektronik',
        'ornek_cumle': 'Ahmet uses battery management in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Batarya Yönetimi'},
    {   'bengalce': 'সিগন্যাল প্রসেসিং (Signal processing)',
        'cince': '信号处理 (Xìnhào chǔlǐ)',
        'id': 53,
        'ingilizce': 'Signal Processing (#53)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses signal processing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Sinyal İşleme'},
    {   'bengalce': 'ডেটা স্ট্রাকচার (Data structure)',
        'cince': '数据结构 (Shùjù jiégòu)',
        'id': 54,
        'ingilizce': 'Data Structure (#54)',
        'kategori': 'Bilgisayar Bilimi',
        'ornek_cumle': 'Ahmet uses data structure in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Veri Yapısı'},
    {   'bengalce': 'অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)',
        'cince': '面向对象编程 (Miànxiàng duìxiàng biānchéng)',
        'id': 55,
        'ingilizce': 'Object Oriented Programming (#55)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses object oriented programming in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Nesne Yönelimli Programlama'},
    {   'bengalce': 'সাইবার নিরাপত্তা (Cyber nirapotta)',
        'cince': '网络安全 (Wǎngluò ānquán)',
        'id': 56,
        'ingilizce': 'Cyber Security (#56)',
        'kategori': 'Güvenlik',
        'ornek_cumle': 'Ahmet uses cyber security in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Siber Güvenlik'},
    {   'bengalce': 'ক্লাউড কম্পিউটিং (Cloud computing)',
        'cince': '云计算 (Yún jìsuàn)',
        'id': 57,
        'ingilizce': 'Cloud Computing (#57)',
        'kategori': 'Sistem',
        'ornek_cumle': 'Ahmet uses cloud computing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Bulut Bilişim'},
    {   'bengalce': 'ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP)',
        'cince': '自然语言处理 (Zìrán yǔyán chǔlǐ)',
        'id': 58,
        'ingilizce': 'Natural Language Processing (#58)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses natural language processing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Doğal Dil İşleme'},
    {   'bengalce': 'রোবোটিক্স এবং অটোমেশন (Robotics)',
        'cince': '机器人与自动化 (Jīqìrén yǔ zìdònghuà)',
        'id': 59,
        'ingilizce': 'Robotics and Automation (#59)',
        'kategori': 'Robotik',
        'ornek_cumle': 'Ahmet uses robotics and automation in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Robotik ve Otomasyon'},
    {   'bengalce': 'অ্যারোডাইনামিক্স (Aerodynamics)',
        'cince': '空气动力学 (Kōngqì dònglìxué)',
        'id': 60,
        'ingilizce': 'Aerodynamics (#60)',
        'kategori': 'Fizik',
        'ornek_cumle': 'Ahmet uses aerodynamics in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Aerodinamik'},
    {   'bengalce': 'কৃত্রিম বুদ্ধিমত্তা (Kritrim buddhimotta)',
        'cince': '人工智能 (Réngōng zhìnéng)',
        'id': 61,
        'ingilizce': 'Artificial Intelligence (#61)',
        'kategori': 'Teknoloji',
        'ornek_cumle': 'Ahmet uses artificial intelligence in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Yapay Zeka'},
    {   'bengalce': 'স্বায়ত্তশাসিত ড্রোন (Sbayottoshasito drone)',
        'cince': '自主无人机 (Zìzhǔ wúrénjī)',
        'id': 62,
        'ingilizce': 'Autonomous Drone (#62)',
        'kategori': 'Havacılık',
        'ornek_cumle': 'Ahmet uses autonomous drone in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Otonom İnsansız Hava Aracı'},
    {   'bengalce': 'সফটওয়্যার ইঞ্জিনিয়ারিং (Software engineering)',
        'cince': '软件工程 (Ruǎnjiàn gōngchéng)',
        'id': 63,
        'ingilizce': 'Software Engineering (#63)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses software engineering in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Yazılım Mühendisliği'},
    {   'bengalce': 'মেশিন লার্নিং (Machine learning)',
        'cince': '机器学习 (Jīqì xuéxí)',
        'id': 64,
        'ingilizce': 'Machine Learning (#64)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses machine learning in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Makine Öğrenmesi'},
    {   'bengalce': 'নিউরাল নেটওয়ার্ক (Neural network)',
        'cince': '神经网络 (Shénjīng wǎngluò)',
        'id': 65,
        'ingilizce': 'Neural Network (#65)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses neural network in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Sinir Ağı'},
    {   'bengalce': 'কম্পিউটার ভিশন (Computer vision)',
        'cince': '计算机视觉 (Jìsuànjī shìjué)',
        'id': 66,
        'ingilizce': 'Computer Vision (#66)',
        'kategori': 'Görüntü İşleme',
        'ornek_cumle': 'Ahmet uses computer vision in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Bilgisayarlı Görü'},
    {   'bengalce': 'এম্বেডেড সিস্টেম (Embedded system)',
        'cince': '嵌入式系统 (Qiànrùshì xìtǒng)',
        'id': 67,
        'ingilizce': 'Embedded Systems (#67)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses embedded systems in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Gömülü Sistemler'},
    {   'bengalce': 'মাইক্রোকন্ট্রোলার (Microcontroller)',
        'cince': '微控制器 (Wēi kòngzhìqì)',
        'id': 68,
        'ingilizce': 'Microcontroller (#68)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses microcontroller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Mikrodenetleyici'},
    {   'bengalce': 'আল্ট্রাসনিক সেন্সর (Ultrasonic sensor)',
        'cince': '超声波传感器 (Chāoshēngbō chuángǎnqì)',
        'id': 69,
        'ingilizce': 'Ultrasonic Sensor (#69)',
        'kategori': 'Sensör',
        'ornek_cumle': 'Ahmet uses ultrasonic sensor in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Ultrasonik Sensör'},
    {   'bengalce': 'থ্রিডি প্রিন্টিং (3D printing)',
        'cince': '3D打印 (3D dǎyìn)',
        'id': 70,
        'ingilizce': 'Three Dimensional Printing (#70)',
        'kategori': 'Üretim',
        'ornek_cumle': 'Ahmet uses three dimensional printing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Üç Boyutlu Baskı'},
    {   'bengalce': 'বর্গমূল (Borgomul)',
        'cince': '平方根 (Píngfānggēn)',
        'id': 71,
        'ingilizce': 'Square Root (#71)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses square root in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Karekök'},
    {   'bengalce': 'মৌলিক সংখ্যা (Moulik songkha)',
        'cince': '质数 (Zhìshù)',
        'id': 72,
        'ingilizce': 'Prime Number (#72)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses prime number in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Asal Sayı'},
    {   'bengalce': 'রৈখিক সমীকরণ (Roikhik somikoron)',
        'cince': '线性方程 (Xiànxìng fāngchéng)',
        'id': 73,
        'ingilizce': 'Linear Equation (#73)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses linear equation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Doğrusal Denklem'},
    {   'bengalce': 'গরিষ্ঠ সাধারণ গুণনীয়ক (Goshagu)',
        'cince': '最大公约数 (Zuìdà gōngyuēshù)',
        'id': 74,
        'ingilizce': 'Greatest Common Divisor (#74)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses greatest common divisor in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'En Büyük Ortak Bölen (EBOB)'},
    {   'bengalce': 'লঘিষ্ঠ সাধারণ গুণিতক (Loshagu)',
        'cince': '最小公倍数 (Zuìxiǎo gōngbèishù)',
        'id': 75,
        'ingilizce': 'Least Common Multiple (#75)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses least common multiple in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'En Küçük Ortak Kat (EKOK)'},
    {   'bengalce': 'সূচক (Suchok)',
        'cince': '幂运算 (Mì yùnsuàn)',
        'id': 76,
        'ingilizce': 'Exponentiation (#76)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses exponentiation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Üs Alma / Üslü Sayılar'},
    {   'bengalce': 'পিথাগোরাসের উপপাদ্য (Pithagoraser upopaddo)',
        'cince': '勾股定理 (Gōugǔ dìnglǐ)',
        'id': 77,
        'ingilizce': 'Pythagorean Theorem (#77)',
        'kategori': 'Geometri',
        'ornek_cumle': 'Ahmet uses pythagorean theorem in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Pisagor Teoremi'},
    {   'bengalce': 'অধ্যবসায় এবং শৃঙ্খলা (Oddhobosay ebong srinkhola)',
        'cince': '毅力与纪律 (Yìlì yǔ jìlǜ)',
        'id': 78,
        'ingilizce': 'Perseverance and Discipline (#78)',
        'kategori': 'Kişisel Gelişim',
        'ornek_cumle': 'Ahmet uses perseverance and discipline in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Azim ve Disiplin'},
    {   'bengalce': 'বৈজ্ঞানিক গবেষণা (Boigganik gobeshona)',
        'cince': '科学研究 (Kēxué yánjiū)',
        'id': 79,
        'ingilizce': 'Scientific Research (#79)',
        'kategori': 'Bilim',
        'ornek_cumle': 'Ahmet uses scientific research in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bilimsel Araştırma'},
    {   'bengalce': 'অ্যালগরিদম অপ্টিমাইজেশন (Algorithm optimization)',
        'cince': '算法优化 (Suànfǎ yōuhuà)',
        'id': 80,
        'ingilizce': 'Algorithm Optimization (#80)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses algorithm optimization in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Algoritma Optimizasyonu'},
    {   'bengalce': 'ফ্লাইট কন্ট্রোলার (Flight controller)',
        'cince': '飞行控制器 (Fēixíng kòngzhìqì)',
        'id': 81,
        'ingilizce': 'Flight Controller (#81)',
        'kategori': 'İHA / Drone',
        'ornek_cumle': 'Ahmet uses flight controller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Uçuş Kontrol Kartı'},
    {   'bengalce': 'ব্যাটারি ম্যানেজমেন্ট (Battery management)',
        'cince': '电池管理 (Diànchí guǎnlǐ)',
        'id': 82,
        'ingilizce': 'Battery Management (#82)',
        'kategori': 'Elektronik',
        'ornek_cumle': 'Ahmet uses battery management in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Batarya Yönetimi'},
    {   'bengalce': 'সিগন্যাল প্রসেসিং (Signal processing)',
        'cince': '信号处理 (Xìnhào chǔlǐ)',
        'id': 83,
        'ingilizce': 'Signal Processing (#83)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses signal processing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Sinyal İşleme'},
    {   'bengalce': 'ডেটা স্ট্রাকচার (Data structure)',
        'cince': '数据结构 (Shùjù jiégòu)',
        'id': 84,
        'ingilizce': 'Data Structure (#84)',
        'kategori': 'Bilgisayar Bilimi',
        'ornek_cumle': 'Ahmet uses data structure in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Veri Yapısı'},
    {   'bengalce': 'অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)',
        'cince': '面向对象编程 (Miànxiàng duìxiàng biānchéng)',
        'id': 85,
        'ingilizce': 'Object Oriented Programming (#85)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses object oriented programming in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Nesne Yönelimli Programlama'},
    {   'bengalce': 'সাইবার নিরাপত্তা (Cyber nirapotta)',
        'cince': '网络安全 (Wǎngluò ānquán)',
        'id': 86,
        'ingilizce': 'Cyber Security (#86)',
        'kategori': 'Güvenlik',
        'ornek_cumle': 'Ahmet uses cyber security in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Siber Güvenlik'},
    {   'bengalce': 'ক্লাউড কম্পিউটিং (Cloud computing)',
        'cince': '云计算 (Yún jìsuàn)',
        'id': 87,
        'ingilizce': 'Cloud Computing (#87)',
        'kategori': 'Sistem',
        'ornek_cumle': 'Ahmet uses cloud computing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bulut Bilişim'},
    {   'bengalce': 'ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP)',
        'cince': '自然语言处理 (Zìrán yǔyán chǔlǐ)',
        'id': 88,
        'ingilizce': 'Natural Language Processing (#88)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses natural language processing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Doğal Dil İşleme'},
    {   'bengalce': 'রোবোটিক্স এবং অটোমেশন (Robotics)',
        'cince': '机器人与自动化 (Jīqìrén yǔ zìdònghuà)',
        'id': 89,
        'ingilizce': 'Robotics and Automation (#89)',
        'kategori': 'Robotik',
        'ornek_cumle': 'Ahmet uses robotics and automation in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Robotik ve Otomasyon'},
    {   'bengalce': 'অ্যারোডাইনামিক্স (Aerodynamics)',
        'cince': '空气动力学 (Kōngqì dònglìxué)',
        'id': 90,
        'ingilizce': 'Aerodynamics (#90)',
        'kategori': 'Fizik',
        'ornek_cumle': 'Ahmet uses aerodynamics in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Orta',
        'turkce': 'Aerodinamik'},
    {   'bengalce': 'কৃত্রিম বুদ্ধিমত্তা (Kritrim buddhimotta)',
        'cince': '人工智能 (Réngōng zhìnéng)',
        'id': 91,
        'ingilizce': 'Artificial Intelligence (#91)',
        'kategori': 'Teknoloji',
        'ornek_cumle': 'Ahmet uses artificial intelligence in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Yapay Zeka'},
    {   'bengalce': 'স্বায়ত্তশাসিত ড্রোন (Sbayottoshasito drone)',
        'cince': '自主无人机 (Zìzhǔ wúrénjī)',
        'id': 92,
        'ingilizce': 'Autonomous Drone (#92)',
        'kategori': 'Havacılık',
        'ornek_cumle': 'Ahmet uses autonomous drone in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Otonom İnsansız Hava Aracı'},
    {   'bengalce': 'সফটওয়্যার ইঞ্জিনিয়ারিং (Software engineering)',
        'cince': '软件工程 (Ruǎnjiàn gōngchéng)',
        'id': 93,
        'ingilizce': 'Software Engineering (#93)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses software engineering in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Yazılım Mühendisliği'},
    {   'bengalce': 'মেশিন লার্নিং (Machine learning)',
        'cince': '机器学习 (Jīqì xuéxí)',
        'id': 94,
        'ingilizce': 'Machine Learning (#94)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses machine learning in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Makine Öğrenmesi'},
    {   'bengalce': 'নিউরাল নেটওয়ার্ক (Neural network)',
        'cince': '神经网络 (Shénjīng wǎngluò)',
        'id': 95,
        'ingilizce': 'Neural Network (#95)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses neural network in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Sinir Ağı'},
    {   'bengalce': 'কম্পিউটার ভিশন (Computer vision)',
        'cince': '计算机视觉 (Jìsuànjī shìjué)',
        'id': 96,
        'ingilizce': 'Computer Vision (#96)',
        'kategori': 'Görüntü İşleme',
        'ornek_cumle': 'Ahmet uses computer vision in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Bilgisayarlı Görü'},
    {   'bengalce': 'এম্বেডেড সিস্টেম (Embedded system)',
        'cince': '嵌入式系统 (Qiànrùshì xìtǒng)',
        'id': 97,
        'ingilizce': 'Embedded Systems (#97)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses embedded systems in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Gömülü Sistemler'},
    {   'bengalce': 'মাইক্রোকন্ট্রোলার (Microcontroller)',
        'cince': '微控制器 (Wēi kòngzhìqì)',
        'id': 98,
        'ingilizce': 'Microcontroller (#98)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses microcontroller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Mikrodenetleyici'},
    {   'bengalce': 'আল্ট্রাসনিক সেন্সর (Ultrasonic sensor)',
        'cince': '超声波传感器 (Chāoshēngbō chuángǎnqì)',
        'id': 99,
        'ingilizce': 'Ultrasonic Sensor (#99)',
        'kategori': 'Sensör',
        'ornek_cumle': 'Ahmet uses ultrasonic sensor in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Ultrasonik Sensör'},
    {   'bengalce': 'থ্রিডি প্রিন্টিং (3D printing)',
        'cince': '3D打印 (3D dǎyìn)',
        'id': 100,
        'ingilizce': 'Three Dimensional Printing (#100)',
        'kategori': 'Üretim',
        'ornek_cumle': 'Ahmet uses three dimensional printing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Üç Boyutlu Baskı'},
    {   'bengalce': 'বর্গমূল (Borgomul)',
        'cince': '平方根 (Píngfānggēn)',
        'id': 101,
        'ingilizce': 'Square Root (#101)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses square root in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Temel',
        'turkce': 'Karekök'},
    {   'bengalce': 'মৌলিক সংখ্যা (Moulik songkha)',
        'cince': '质数 (Zhìshù)',
        'id': 102,
        'ingilizce': 'Prime Number (#102)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses prime number in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Orta',
        'turkce': 'Asal Sayı'},
    {   'bengalce': 'রৈখিক সমীকরণ (Roikhik somikoron)',
        'cince': '线性方程 (Xiànxìng fāngchéng)',
        'id': 103,
        'ingilizce': 'Linear Equation (#103)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses linear equation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Doğrusal Denklem'},
    {   'bengalce': 'গরিষ্ঠ সাধারণ গুণনীয়ক (Goshagu)',
        'cince': '最大公约数 (Zuìdà gōngyuēshù)',
        'id': 104,
        'ingilizce': 'Greatest Common Divisor (#104)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses greatest common divisor in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'En Büyük Ortak Bölen (EBOB)'},
    {   'bengalce': 'লঘিষ্ঠ সাধারণ গুণিতক (Loshagu)',
        'cince': '最小公倍数 (Zuìxiǎo gōngbèishù)',
        'id': 105,
        'ingilizce': 'Least Common Multiple (#105)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses least common multiple in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'En Küçük Ortak Kat (EKOK)'},
    {   'bengalce': 'সূচক (Suchok)',
        'cince': '幂运算 (Mì yùnsuàn)',
        'id': 106,
        'ingilizce': 'Exponentiation (#106)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses exponentiation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Üs Alma / Üslü Sayılar'},
    {   'bengalce': 'পিথাগোরাসের উপপাদ্য (Pithagoraser upopaddo)',
        'cince': '勾股定理 (Gōugǔ dìnglǐ)',
        'id': 107,
        'ingilizce': 'Pythagorean Theorem (#107)',
        'kategori': 'Geometri',
        'ornek_cumle': 'Ahmet uses pythagorean theorem in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Pisagor Teoremi'},
    {   'bengalce': 'অধ্যবসায় এবং শৃঙ্খলা (Oddhobosay ebong srinkhola)',
        'cince': '毅力与纪律 (Yìlì yǔ jìlǜ)',
        'id': 108,
        'ingilizce': 'Perseverance and Discipline (#108)',
        'kategori': 'Kişisel Gelişim',
        'ornek_cumle': 'Ahmet uses perseverance and discipline in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Azim ve Disiplin'},
    {   'bengalce': 'বৈজ্ঞানিক গবেষণা (Boigganik gobeshona)',
        'cince': '科学研究 (Kēxué yánjiū)',
        'id': 109,
        'ingilizce': 'Scientific Research (#109)',
        'kategori': 'Bilim',
        'ornek_cumle': 'Ahmet uses scientific research in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Bilimsel Araştırma'},
    {   'bengalce': 'অ্যালগরিদম অপ্টিমাইজেশন (Algorithm optimization)',
        'cince': '算法优化 (Suànfǎ yōuhuà)',
        'id': 110,
        'ingilizce': 'Algorithm Optimization (#110)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses algorithm optimization in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Algoritma Optimizasyonu'},
    {   'bengalce': 'ফ্লাইট কন্ট্রোলার (Flight controller)',
        'cince': '飞行控制器 (Fēixíng kòngzhìqì)',
        'id': 111,
        'ingilizce': 'Flight Controller (#111)',
        'kategori': 'İHA / Drone',
        'ornek_cumle': 'Ahmet uses flight controller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Uçuş Kontrol Kartı'},
    {   'bengalce': 'ব্যাটারি ম্যানেজমেন্ট (Battery management)',
        'cince': '电池管理 (Diànchí guǎnlǐ)',
        'id': 112,
        'ingilizce': 'Battery Management (#112)',
        'kategori': 'Elektronik',
        'ornek_cumle': 'Ahmet uses battery management in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Batarya Yönetimi'},
    {   'bengalce': 'সিগন্যাল প্রসেসিং (Signal processing)',
        'cince': '信号处理 (Xìnhào chǔlǐ)',
        'id': 113,
        'ingilizce': 'Signal Processing (#113)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses signal processing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Sinyal İşleme'},
    {   'bengalce': 'ডেটা স্ট্রাকচার (Data structure)',
        'cince': '数据结构 (Shùjù jiégòu)',
        'id': 114,
        'ingilizce': 'Data Structure (#114)',
        'kategori': 'Bilgisayar Bilimi',
        'ornek_cumle': 'Ahmet uses data structure in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Veri Yapısı'},
    {   'bengalce': 'অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)',
        'cince': '面向对象编程 (Miànxiàng duìxiàng biānchéng)',
        'id': 115,
        'ingilizce': 'Object Oriented Programming (#115)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses object oriented programming in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Nesne Yönelimli Programlama'},
    {   'bengalce': 'সাইবার নিরাপত্তা (Cyber nirapotta)',
        'cince': '网络安全 (Wǎngluò ānquán)',
        'id': 116,
        'ingilizce': 'Cyber Security (#116)',
        'kategori': 'Güvenlik',
        'ornek_cumle': 'Ahmet uses cyber security in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Siber Güvenlik'},
    {   'bengalce': 'ক্লাউড কম্পিউটিং (Cloud computing)',
        'cince': '云计算 (Yún jìsuàn)',
        'id': 117,
        'ingilizce': 'Cloud Computing (#117)',
        'kategori': 'Sistem',
        'ornek_cumle': 'Ahmet uses cloud computing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Bulut Bilişim'},
    {   'bengalce': 'ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP)',
        'cince': '自然语言处理 (Zìrán yǔyán chǔlǐ)',
        'id': 118,
        'ingilizce': 'Natural Language Processing (#118)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses natural language processing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Doğal Dil İşleme'},
    {   'bengalce': 'রোবোটিক্স এবং অটোমেশন (Robotics)',
        'cince': '机器人与自动化 (Jīqìrén yǔ zìdònghuà)',
        'id': 119,
        'ingilizce': 'Robotics and Automation (#119)',
        'kategori': 'Robotik',
        'ornek_cumle': 'Ahmet uses robotics and automation in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Robotik ve Otomasyon'},
    {   'bengalce': 'অ্যারোডাইনামিক্স (Aerodynamics)',
        'cince': '空气动力学 (Kōngqì dònglìxué)',
        'id': 120,
        'ingilizce': 'Aerodynamics (#120)',
        'kategori': 'Fizik',
        'ornek_cumle': 'Ahmet uses aerodynamics in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Aerodinamik'},
    {   'bengalce': 'কৃত্রিম বুদ্ধিমত্তা (Kritrim buddhimotta)',
        'cince': '人工智能 (Réngōng zhìnéng)',
        'id': 121,
        'ingilizce': 'Artificial Intelligence (#121)',
        'kategori': 'Teknoloji',
        'ornek_cumle': 'Ahmet uses artificial intelligence in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Yapay Zeka'},
    {   'bengalce': 'স্বায়ত্তশাসিত ড্রোন (Sbayottoshasito drone)',
        'cince': '自主无人机 (Zìzhǔ wúrénjī)',
        'id': 122,
        'ingilizce': 'Autonomous Drone (#122)',
        'kategori': 'Havacılık',
        'ornek_cumle': 'Ahmet uses autonomous drone in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Otonom İnsansız Hava Aracı'},
    {   'bengalce': 'সফটওয়্যার ইঞ্জিনিয়ারিং (Software engineering)',
        'cince': '软件工程 (Ruǎnjiàn gōngchéng)',
        'id': 123,
        'ingilizce': 'Software Engineering (#123)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses software engineering in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Yazılım Mühendisliği'},
    {   'bengalce': 'মেশিন লার্নিং (Machine learning)',
        'cince': '机器学习 (Jīqì xuéxí)',
        'id': 124,
        'ingilizce': 'Machine Learning (#124)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses machine learning in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Makine Öğrenmesi'},
    {   'bengalce': 'নিউরাল নেটওয়ার্ক (Neural network)',
        'cince': '神经网络 (Shénjīng wǎngluò)',
        'id': 125,
        'ingilizce': 'Neural Network (#125)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses neural network in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Sinir Ağı'},
    {   'bengalce': 'কম্পিউটার ভিশন (Computer vision)',
        'cince': '计算机视觉 (Jìsuànjī shìjué)',
        'id': 126,
        'ingilizce': 'Computer Vision (#126)',
        'kategori': 'Görüntü İşleme',
        'ornek_cumle': 'Ahmet uses computer vision in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Bilgisayarlı Görü'},
    {   'bengalce': 'এম্বেডেড সিস্টেম (Embedded system)',
        'cince': '嵌入式系统 (Qiànrùshì xìtǒng)',
        'id': 127,
        'ingilizce': 'Embedded Systems (#127)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses embedded systems in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Gömülü Sistemler'},
    {   'bengalce': 'মাইক্রোকন্ট্রোলার (Microcontroller)',
        'cince': '微控制器 (Wēi kòngzhìqì)',
        'id': 128,
        'ingilizce': 'Microcontroller (#128)',
        'kategori': 'Donanım',
        'ornek_cumle': 'Ahmet uses microcontroller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Mikrodenetleyici'},
    {   'bengalce': 'আল্ট্রাসনিক সেন্সর (Ultrasonic sensor)',
        'cince': '超声波传感器 (Chāoshēngbō chuángǎnqì)',
        'id': 129,
        'ingilizce': 'Ultrasonic Sensor (#129)',
        'kategori': 'Sensör',
        'ornek_cumle': 'Ahmet uses ultrasonic sensor in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Ultrasonik Sensör'},
    {   'bengalce': 'থ্রিডি প্রিন্টিং (3D printing)',
        'cince': '3D打印 (3D dǎyìn)',
        'id': 130,
        'ingilizce': 'Three Dimensional Printing (#130)',
        'kategori': 'Üretim',
        'ornek_cumle': 'Ahmet uses three dimensional printing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Üç Boyutlu Baskı'},
    {   'bengalce': 'বর্গমূল (Borgomul)',
        'cince': '平方根 (Píngfānggēn)',
        'id': 131,
        'ingilizce': 'Square Root (#131)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses square root in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Karekök'},
    {   'bengalce': 'মৌলিক সংখ্যা (Moulik songkha)',
        'cince': '质数 (Zhìshù)',
        'id': 132,
        'ingilizce': 'Prime Number (#132)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses prime number in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Asal Sayı'},
    {   'bengalce': 'রৈখিক সমীকরণ (Roikhik somikoron)',
        'cince': '线性方程 (Xiànxìng fāngchéng)',
        'id': 133,
        'ingilizce': 'Linear Equation (#133)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses linear equation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Doğrusal Denklem'},
    {   'bengalce': 'গরিষ্ঠ সাধারণ গুণনীয়ক (Goshagu)',
        'cince': '最大公约数 (Zuìdà gōngyuēshù)',
        'id': 134,
        'ingilizce': 'Greatest Common Divisor (#134)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses greatest common divisor in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'En Büyük Ortak Bölen (EBOB)'},
    {   'bengalce': 'লঘিষ্ঠ সাধারণ গুণিতক (Loshagu)',
        'cince': '最小公倍数 (Zuìxiǎo gōngbèishù)',
        'id': 135,
        'ingilizce': 'Least Common Multiple (#135)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses least common multiple in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'En Küçük Ortak Kat (EKOK)'},
    {   'bengalce': 'সূচক (Suchok)',
        'cince': '幂运算 (Mì yùnsuàn)',
        'id': 136,
        'ingilizce': 'Exponentiation (#136)',
        'kategori': 'Matematik',
        'ornek_cumle': 'Ahmet uses exponentiation in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Üs Alma / Üslü Sayılar'},
    {   'bengalce': 'পিথাগোরাসের উপপাদ্য (Pithagoraser upopaddo)',
        'cince': '勾股定理 (Gōugǔ dìnglǐ)',
        'id': 137,
        'ingilizce': 'Pythagorean Theorem (#137)',
        'kategori': 'Geometri',
        'ornek_cumle': 'Ahmet uses pythagorean theorem in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Pisagor Teoremi'},
    {   'bengalce': 'অধ্যবসায় এবং শৃঙ্খলা (Oddhobosay ebong srinkhola)',
        'cince': '毅力与纪律 (Yìlì yǔ jìlǜ)',
        'id': 138,
        'ingilizce': 'Perseverance and Discipline (#138)',
        'kategori': 'Kişisel Gelişim',
        'ornek_cumle': 'Ahmet uses perseverance and discipline in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Orta',
        'turkce': 'Azim ve Disiplin'},
    {   'bengalce': 'বৈজ্ঞানিক গবেষণা (Boigganik gobeshona)',
        'cince': '科学研究 (Kēxué yánjiū)',
        'id': 139,
        'ingilizce': 'Scientific Research (#139)',
        'kategori': 'Bilim',
        'ornek_cumle': 'Ahmet uses scientific research in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bilimsel Araştırma'},
    {   'bengalce': 'অ্যালগরিদম অপ্টিমাইজেশন (Algorithm optimization)',
        'cince': '算法优化 (Suànfǎ yōuhuà)',
        'id': 140,
        'ingilizce': 'Algorithm Optimization (#140)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses algorithm optimization in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Algoritma Optimizasyonu'},
    {   'bengalce': 'ফ্লাইট কন্ট্রোলার (Flight controller)',
        'cince': '飞行控制器 (Fēixíng kòngzhìqì)',
        'id': 141,
        'ingilizce': 'Flight Controller (#141)',
        'kategori': 'İHA / Drone',
        'ornek_cumle': 'Ahmet uses flight controller in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Temel',
        'turkce': 'Uçuş Kontrol Kartı'},
    {   'bengalce': 'ব্যাটারি ম্যানেজমেন্ট (Battery management)',
        'cince': '电池管理 (Diànchí guǎnlǐ)',
        'id': 142,
        'ingilizce': 'Battery Management (#142)',
        'kategori': 'Elektronik',
        'ornek_cumle': 'Ahmet uses battery management in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Batarya Yönetimi'},
    {   'bengalce': 'সিগন্যাল প্রসেসিং (Signal processing)',
        'cince': '信号处理 (Xìnhào chǔlǐ)',
        'id': 143,
        'ingilizce': 'Signal Processing (#143)',
        'kategori': 'Mühendislik',
        'ornek_cumle': 'Ahmet uses signal processing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Sinyal İşleme'},
    {   'bengalce': 'ডেটা স্ট্রাকচার (Data structure)',
        'cince': '数据结构 (Shùjù jiégòu)',
        'id': 144,
        'ingilizce': 'Data Structure (#144)',
        'kategori': 'Bilgisayar Bilimi',
        'ornek_cumle': 'Ahmet uses data structure in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Akademik',
        'turkce': 'Veri Yapısı'},
    {   'bengalce': 'অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)',
        'cince': '面向对象编程 (Miànxiàng duìxiàng biānchéng)',
        'id': 145,
        'ingilizce': 'Object Oriented Programming (#145)',
        'kategori': 'Yazılım',
        'ornek_cumle': 'Ahmet uses object oriented programming in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Nesne Yönelimli Programlama'},
    {   'bengalce': 'সাইবার নিরাপত্তা (Cyber nirapotta)',
        'cince': '网络安全 (Wǎngluò ānquán)',
        'id': 146,
        'ingilizce': 'Cyber Security (#146)',
        'kategori': 'Güvenlik',
        'ornek_cumle': 'Ahmet uses cyber security in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'Orta',
        'turkce': 'Siber Güvenlik'},
    {   'bengalce': 'ক্লাউড কম্পিউটিং (Cloud computing)',
        'cince': '云计算 (Yún jìsuàn)',
        'id': 147,
        'ingilizce': 'Cloud Computing (#147)',
        'kategori': 'Sistem',
        'ornek_cumle': 'Ahmet uses cloud computing in his Ar AI Studio and autonomous drone '
                       'projects.',
        'seviye': 'İleri Mühendislik',
        'turkce': 'Bulut Bilişim'},
    {   'bengalce': 'ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP)',
        'cince': '自然语言处理 (Zìrán yǔyán chǔlǐ)',
        'id': 148,
        'ingilizce': 'Natural Language Processing (#148)',
        'kategori': 'Yapay Zeka',
        'ornek_cumle': 'Ahmet uses natural language processing in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Akademik',
        'turkce': 'Doğal Dil İşleme'},
    {   'bengalce': 'রোবোটিক্স এবং অটোমেশন (Robotics)',
        'cince': '机器人与自动化 (Jīqìrén yǔ zìdònghuà)',
        'id': 149,
        'ingilizce': 'Robotics and Automation (#149)',
        'kategori': 'Robotik',
        'ornek_cumle': 'Ahmet uses robotics and automation in his Ar AI Studio and autonomous '
                       'drone projects.',
        'seviye': 'Temel',
        'turkce': 'Robotik ve Otomasyon'},
    {   'bengalce': 'অ্যারোডাইনামিক্স (Aerodynamics)',
        'cince': '空气动力学 (Kōngqì dònglìxué)',
        'id': 150,
        'ingilizce': 'Aerodynamics (#150)',
        'kategori': 'Fizik',
        'ornek_cumle': 'Ahmet uses aerodynamics in his Ar AI Studio and autonomous drone projects.',
        'seviye': 'Orta',
        'turkce': 'Aerodinamik'}]

SISTEM_KISAYOL_REHBERI = [   {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'},
    {   'aciklama': 'Seçili metni veya kodu panoya kopyalar.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + C'},
    {   'aciklama': 'Panodaki metni veya kodu imlecin olduğu yere yapıştırır.',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + V'},
    {   'aciklama': 'Fare ile bir satırın üzerine 3 kez hızlıca tıklamak tüm satırı tek seferde '
                    'seçer.',
        'platform': 'Hızlı Seçim',
        'tus': 'Üç Kez Tıklama (Triple Click)'},
    {   'aciklama': 'Dosyadaki tüm kodu tek seferde seçer (Kopyala-Yapıştır için en hızlı yöntem).',
        'platform': 'Masaüstü Genel',
        'tus': 'Ctrl + A'},
    {   'aciklama': 'Son yapılan işlemi geri alır / ileri alır.',
        'platform': 'Düzenleme',
        'tus': 'Ctrl + Z / Ctrl + Y'},
    {   'aciklama': 'PyCharm üzerinde aktif Python dosyasını çalıştırır.',
        'platform': 'PyCharm',
        'tus': 'Shift + F10'},
    {   'aciklama': 'PyCharm içinde alt terminali doğrudan açar (`streamlit run main.py` yazmak '
                    'için).',
        'platform': 'PyCharm',
        'tus': 'Alt + F12'},
    {   'aciklama': 'PyCharm içinde Python kodunu PEP8 standartlarına göre otomatik düzenler.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + Alt + L'},
    {   'aciklama': 'Seçili satırları tek tuşla yorum satırı (`#`) yapar veya yorumdan çıkarır.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + /'},
    {   'aciklama': 'Dosya içinde kelime arar / toplu olarak değiştirir.',
        'platform': 'PyCharm',
        'tus': 'Ctrl + F / Ctrl + R'}]

def arayuz_stillerini_yukle(secili_tema_adi: str = "Derin Lacivert (Klasik Ar)"):
    """
    CommonMark 4-boşluk kod bloğu hatasını önlemek için sıfır girintili (sola dayalı)
    HTML/CSS üreten, tüm ekranı koyu lacivert / derin mavi yapan arayüz motoru.
    """
    palet = TEMA_PALETLERI.get(secili_tema_adi, TEMA_PALETLERI["Derin Lacivert (Klasik Ar)"])
    bg1 = palet["bg_primary"]
    bg2 = palet["bg_secondary"]
    card = palet["card_bg"]
    acc1 = palet["accent_neon"]
    acc2 = palet["accent_blue"]
    acc3 = palet["accent_purple"]
    rose = palet["accent_rose"]
    txt = palet["text_main"]
    sub = palet["text_sub"]

    css_metni = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=JetBrains+Mono:wght@600;700;800&display=swap');
:root {{
    --bg-primary: {bg1};
    --bg-secondary: {bg2};
    --card-bg: {card};
    --accent-neon: {acc1};
    --accent-blue: {acc2};
    --accent-purple: {acc3};
    --accent-rose: {rose};
    --text-main: {txt};
    --text-sub: {sub};
    color-scheme: dark !important;
}}
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stApp"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.main, section.main, .block-container {{
    background: linear-gradient(160deg, {bg1} 0%, {bg2} 55%, #020614 100%) !important;
    background-color: {bg1} !important;
    color: {txt} !important;
    font-family: 'Plus Jakarta Sans', 'Segoe UI', Roboto, sans-serif !important;
    font-weight: 700 !important;
}}
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottomBlockContainer"],
.stChatFloatingInputContainer {{
    background: {bg1} !important;
    background-color: {bg1} !important;
    border-top: 1px solid rgba(56, 189, 248, 0.28) !important;
}}
h1, h2, h3, h4, h5, h6 {{
    color: #ffffff !important;
    font-weight: 800 !important;
    letter-spacing: -0.3px !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.55) !important;
}}
p, label, span, div, li, td, th, caption, small {{
    color: {sub} !important;
    font-weight: 600 !important;
}}
strong, b {{
    color: {acc1} !important;
    font-weight: 800 !important;
}}
code, pre {{
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    background-color: #041026 !important;
    color: {acc1} !important;
    border: 1.5px solid {acc2} !important;
    border-radius: 8px !important;
    padding: 3px 8px !important;
}}
[data-testid="stAlert"] {{
    background: linear-gradient(135deg, {card} 0%, {bg2} 100%) !important;
    border: 1.5px solid {acc2} !important;
    border-left: 6px solid {acc1} !important;
    border-radius: 14px !important;
    color: #ffffff !important;
    padding: 14px 18px !important;
}}
[data-testid="stAlert"] p,
[data-testid="stAlert"] div,
[data-testid="stAlert"] span {{
    color: #ffffff !important;
    font-weight: 700 !important;
}}
[data-testid="stForm"],
[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: rgba(7, 20, 46, 0.85) !important;
    border: 1.5px solid rgba(56, 189, 248, 0.38) !important;
    border-radius: 16px !important;
}}
[data-baseweb="base-input"],
[data-baseweb="input"],
[data-baseweb="textarea"] {{
    background-color: #05122c !important;
    border-color: {acc2} !important;
    border-radius: 12px !important;
}}
input[type="text"],
input[type="number"],
textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
[data-testid="stChatInput"] textarea,
[data-testid="stChatInputTextArea"] {{
    background-color: #05122c !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: {acc1} !important;
    border: 2px solid {acc2} !important;
    border-radius: 12px !important;
    font-size: 1.02rem !important;
    font-weight: 700 !important;
    padding: 10px 14px !important;
}}
input::placeholder,
textarea::placeholder,
[data-testid="stChatInput"] textarea::placeholder {{
    color: #93c5fd !important;
    -webkit-text-fill-color: #93c5fd !important;
    opacity: 0.88 !important;
}}
input:focus,
textarea:focus,
[data-testid="stChatInput"] textarea:focus {{
    border-color: {acc1} !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.45) !important;
    outline: none !important;
}}
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInputContainer"] {{
    background: #040e24 !important;
    background-color: #040e24 !important;
    border: 2px solid {acc2} !important;
    border-radius: 16px !important;
    padding: 4px !important;
}}
[data-baseweb="select"] > div {{
    background-color: #05122c !important;
    color: #ffffff !important;
    border: 2px solid {acc2} !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}}
[data-baseweb="select"] span,
[data-baseweb="select"] svg {{
    color: #ffffff !important;
    fill: #ffffff !important;
}}
ul[role="listbox"],
[data-baseweb="popover"] > div {{
    background-color: #061533 !important;
    border: 2px solid {acc2} !important;
    border-radius: 12px !important;
}}
ul[role="listbox"] li {{
    color: #ffffff !important;
    background-color: #061533 !important;
    font-weight: 700 !important;
}}
ul[role="listbox"] li:hover {{
    background-color: #122c5c !important;
}}
[data-testid="stExpander"],
[data-testid="stExpander"] details,
[data-testid="stExpander"] summary {{
    background-color: #061533 !important;
    color: #ffffff !important;
    border: 1.5px solid rgba(56, 189, 248, 0.45) !important;
    border-radius: 12px !important;
}}
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"],
[data-testid="stSidebarUserContent"] {{
    background: linear-gradient(180deg, #020817 0%, #07193d 100%) !important;
    background-color: #020817 !important;
    border-right: 2px solid rgba(56, 189, 248, 0.38) !important;
}}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div {{
    color: #ffffff !important;
    font-weight: 700 !important;
}}
.live-badge {{
    display: inline-block;
    background: rgba(14, 165, 233, 0.25);
    color: #38bdf8 !important;
    border: 1.5px solid #38bdf8;
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 800 !important;
    margin-bottom: 10px;
}}
.silent-badge {{
    display: inline-block;
    background: rgba(244, 63, 94, 0.25);
    color: #fda4af !important;
    border: 1.5px solid #fb7185;
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 800 !important;
    margin-bottom: 10px;
}}
.bubble-group-header {{
    background: linear-gradient(90deg, rgba(56, 189, 248, 0.24), transparent);
    border-left: 4px solid {acc1};
    padding: 6px 10px;
    border-radius: 8px;
    font-size: 0.84rem;
    font-weight: 800 !important;
    color: {acc1} !important;
    margin: 10px 0 6px 0;
}}
.history-bubble {{
    background: linear-gradient(135deg, {card} 0%, {bg1} 100%);
    border: 1.5px solid rgba(56, 189, 248, 0.45);
    border-left: 5px solid {acc1};
    border-radius: 14px 14px 14px 4px;
    padding: 10px 13px;
    margin-bottom: 9px;
}}
.history-bubble-meta {{
    color: {acc1} !important;
    font-weight: 800 !important;
    font-size: 0.76rem;
    margin-bottom: 4px;
}}
.history-bubble-text {{
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 0.87rem;
    line-height: 1.4;
}}
.hero-box {{
    background: linear-gradient(135deg, #0b1e42 0%, #07142e 100%);
    border: 2px solid rgba(56, 189, 248, 0.6);
    border-radius: 18px;
    padding: 18px 24px;
    margin-bottom: 18px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
}}
.hero-title {{
    color: #38bdf8 !important;
    font-weight: 800 !important;
    font-size: clamp(1.4rem, 3vw, 2.2rem) !important;
    margin: 0 0 6px 0;
    line-height: 1.2;
}}
.hero-subtitle {{
    color: #dbeafe !important;
    font-size: clamp(0.88rem, 1.5vw, 1.02rem) !important;
    margin: 0;
    font-weight: 700 !important;
}}
.stMetric {{
    background: linear-gradient(145deg, {card} 0%, {bg1} 100%) !important;
    border: 2px solid rgba(56, 189, 248, 0.45) !important;
    padding: 16px !important;
    border-radius: 16px !important;
}}
.stMetric label {{
    color: #dbeafe !important;
    font-weight: 800 !important;
}}
.stMetric [data-testid="stMetricValue"] {{
    color: {acc1} !important;
    font-weight: 800 !important;
}}
.premium-card {{
    background: linear-gradient(135deg, {card} 0%, {bg1} 100%);
    border-left: 5px solid {acc1};
    border-top: 1.5px solid rgba(56, 189, 248, 0.4);
    border-right: 1.5px solid rgba(56, 189, 248, 0.4);
    border-bottom: 1.5px solid rgba(56, 189, 248, 0.4);
    padding: 16px 20px;
    border-radius: 16px;
    margin-bottom: 14px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.45);
}}
.card-title {{
    color: {acc1} !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    margin-bottom: 6px;
}}
.card-meta {{
    color: #93c5fd !important;
    font-size: 0.86rem !important;
    font-weight: 800 !important;
    margin-bottom: 8px;
}}
.card-desc {{
    color: #ffffff !important;
    font-size: 0.98rem !important;
    font-weight: 600 !important;
    line-height: 1.6;
}}
[data-testid="stChatMessage"] {{
    background: {card} !important;
    background-color: {card} !important;
    border: 2px solid rgba(56, 189, 248, 0.5) !important;
    border-radius: 16px !important;
    padding: 14px 18px !important;
    margin-bottom: 12px !important;
}}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] div {{
    color: #ffffff !important;
    font-size: 1.02rem !important;
    font-weight: 600 !important;
    line-height: 1.6 !important;
}}
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button {{
    background: linear-gradient(90deg, #0369a1 0%, {acc3} 50%, {acc2} 100%) !important;
    color: #ffffff !important;
    border: 1.5px solid rgba(147, 197, 253, 0.45) !important;
    border-radius: 12px !important;
    min-height: 44px !important;
    font-weight: 800 !important;
    font-size: 0.95rem !important;
}}
.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover {{
    border-color: #ffffff !important;
    box-shadow: 0 4px 16px rgba(56, 189, 248, 0.55) !important;
}}
button[data-baseweb="tab"] {{
    background-color: {bg2} !important;
    color: #dbeafe !important;
    border-radius: 10px 10px 0 0 !important;
    font-weight: 800 !important;
    padding: 10px 15px !important;
}}
button[data-baseweb="tab"][aria-selected="true"] {{
    background-color: {card} !important;
    color: {acc1} !important;
    border-bottom: 3px solid {acc1} !important;
}}
.flip-card-label {{
    display: block;
    perspective: 1200px;
    width: 100%;
    cursor: pointer;
    user-select: none;
    margin: 12px 0 18px 0;
}}
.flip-card-checkbox {{
    display: none !important;
}}
.flip-card-inner {{
    position: relative;
    width: 100%;
    min-height: 320px;
    text-align: center;
    transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
    transform-style: preserve-3d;
    border-radius: 22px;
}}
.flip-card-checkbox:checked + .flip-card-inner {{
    transform: rotateY(180deg);
}}
.flip-card-front, .flip-card-back {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    min-height: 320px;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    border-radius: 22px;
    padding: 26px 24px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.65);
}}
.flip-card-front {{
    background: linear-gradient(145deg, #0d2554 0%, #06132e 60%, #03091a 100%);
    border: 2.5px solid {acc1};
}}
.flip-card-back {{
    background: linear-gradient(145deg, #071f42 0%, #0c2d5e 55%, #041026 100%);
    border: 2.5px solid #22c55e;
    transform: rotateY(180deg);
    text-align: left;
}}
.flip-badge-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}}
.flip-badge {{
    background: rgba(56, 189, 248, 0.2);
    border: 1.5px solid {acc1};
    color: {acc1} !important;
    padding: 4px 14px;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 800 !important;
}}
.flip-main-word {{
    font-size: clamp(1.65rem, 3.2vw, 2.45rem) !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin: 16px 0 8px 0;
    line-height: 1.3;
}}
.flip-pronunciation {{
    font-size: 1.08rem !important;
    color: #93c5fd !important;
    font-weight: 700 !important;
    margin-bottom: 10px;
}}
.flip-hint {{
    display: inline-block;
    background: rgba(14, 165, 233, 0.18);
    border: 1px dashed #38bdf8;
    color: #dbeafe !important;
    padding: 6px 16px;
    border-radius: 12px;
    font-size: 0.86rem;
}}
@media (max-width: 768px) {{
    .block-container {{
        padding-top: 1rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }}
    .hero-box {{
        padding: 14px 16px !important;
        border-radius: 14px !important;
    }}
    .flip-card-inner, .flip-card-front, .flip-card-back {{
        min-height: 360px !important;
        padding: 18px 16px !important;
    }}
    .stButton > button {{
        width: 100% !important;
        min-height: 46px !important;
    }}
}}
</style>"""
    st.markdown(css_metni, unsafe_allow_html=True)


# ==============================================================================
# 7. YARDIMCI BİLEŞEN RENDER FONKSİYONLARI (SIFIR GİRİNTİLİ HTML)
# ==============================================================================
def hero_banner_goster(kalip_sayisi: int, aktif_tema: str = "Derin Lacivert (Klasik Ar)"):
    formatli_sayi = f"{kalip_sayisi:,}".replace(",", ".")
    html = (
        f'<div class="hero-box">'
        f'<p class="hero-title">⚡ Ar AI Studio — Masaüstü &amp; Mobil Süper Asistan</p>'
        f'<p class="hero-subtitle">'
        f'{formatli_sayi}+ Hazır Kalıp • Koyu Lacivert Kontrastlı Arayüz ({aktif_tema}) • '
        f'Matematik &amp; Fen Laboratuvarı • İslam Âlimleri • 28 Dil'
        f'</p></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def bilgi_karti_olustur(baslik: str, alt_bilgi: str, aciklama: str) -> str:
    return (
        f'<div class="premium-card">'
        f'<div class="card-title">{baslik}</div>'
        f'<div class="card-meta">{alt_bilgi}</div>'
        f'<div class="card-desc">{aciklama}</div>'
        f'</div>'
    )


def sohbet_baloncuk_karti_olustur(etiket: str, saat: str, kisa_metin: str) -> str:
    return (
        f'<div class="history-bubble">'
        f'<div class="history-bubble-meta">💬 {etiket} &bull; 🕒 {saat}</div>'
        f'<div class="history-bubble-text">👤 {kisa_metin}</div>'
        f'</div>'
    )


# ==============================================================================

def cevirmeli_dil_karti_olustur(kart: dict, on_yuz_dili: str = "🇬🇧 İngilizce", ters_cevir: bool = False, kart_key: str = "tek") -> str:
    """Üzerine dokunulduğunda veya butona basıldığında 3D olarak dönen gerçek çevirmeli kart (Flip Card) üretir."""
    checked_attr = "checked" if ters_cevir else ""
    if "İngilizce" in on_yuz_dili:
        on_baslik = "🇬🇧 İNGİLİZCE KART (ÖN YÜZ)"
        ana_ifade = kart["ingilizce"]
        okunus = f"🗣️ Türkçe Okunuşu: {kart['ing_okunus']}"
        ornek = f"📝 {kart['ornek_en']}"
    elif "Arapça" in on_yuz_dili:
        on_baslik = "🇸🇦 ARAPÇA KART (ÖN YÜZ)"
        ana_ifade = kart["arapca"]
        okunus = f"🗣️ Türkçe Okunuşu: {kart['ara_okunus']}"
        ornek = f"📝 {kart['ornek_ar']}"
    elif "Bengalce" in on_yuz_dili:
        on_baslik = "🇧🇩 BENGALCE KART (ÖN YÜZ)"
        ana_ifade = kart["bengalce"]
        okunus = f"🗣️ Türkçe Okunuşu: {kart['ben_okunus']}"
        ornek = f"📝 {kart['ornek_bn']}"
    else:
        on_baslik = "🇹🇷 TÜRKÇE KART (ÖN YÜZ)"
        ana_ifade = kart["turkce"]
        okunus = "🗣️ 3 Dilde Karşılığı İçin Kartı Çevir"
        ornek = f"Kategori: {kart['kategori']}"

    return (
        f'<label class="flip-card-label" for="flip_{kart_key}_{kart["id"]}">'
        f'<input type="checkbox" id="flip_{kart_key}_{kart["id"]}" class="flip-card-checkbox" {checked_attr}>'
        f'<div class="flip-card-inner">'
        f'<div class="flip-card-front">'
        f'<div class="flip-badge-row">'
        f'<span class="flip-badge">🃏 Kart #{kart["id"]} &bull; {kart["seviye"]}</span>'
        f'<span class="flip-badge">{kart["kategori"]}</span>'
        f'</div>'
        f'<div>'
        f'<div style="color:#38bdf8;font-size:0.88rem;font-weight:800;letter-spacing:0.6px;">{on_baslik}</div>'
        f'<div class="flip-main-word">{ana_ifade}</div>'
        f'<div class="flip-pronunciation">{okunus}</div>'
        f'<div style="color:#dbeafe;font-size:0.95rem;margin-top:6px;">{ornek}</div>'
        f'</div>'
        f'<div><span class="flip-hint">🔄 Kartı Çevirmek İçin Üzerine Dokun / Tıkla (Ön ↔ Arka Yüz)</span></div>'
        f'</div>'
        f'<div class="flip-card-back">'
        f'<div class="flip-badge-row">'
        f'<span class="flip-badge" style="border-color:#22c55e;color:#4ade80 !important;">✅ ARKA YÜZ (TÜRKÇE ANLAMI &amp; 3 DİL)</span>'
        f'<span class="flip-badge">{kart["seviye"]}</span>'
        f'</div>'
        f'<div style="margin:10px 0;">'
        f'<div style="font-size:1.35rem;font-weight:800;color:#4ade80 !important;margin-bottom:10px;">🇹🇷 Anlamı: {kart["turkce"]}</div>'
        f'<div style="margin-bottom:7px;">🇬🇧 <strong>İngilizce:</strong> {kart["ingilizce"]} <span style="color:#93c5fd !important;">({kart["ing_okunus"]})</span><br><small style="color:#cbd5e1 !important;">{kart["ornek_en"]}</small></div>'
        f'<div style="margin-bottom:7px;">🇸🇦 <strong>Arapça:</strong> {kart["arapca"]} <span style="color:#93c5fd !important;">({kart["ara_okunus"]})</span><br><small style="color:#cbd5e1 !important;">{kart["ornek_ar"]}</small></div>'
        f'<div>🇧🇩 <strong>Bengalce:</strong> {kart["bengalce"]} <span style="color:#93c5fd !important;">({kart["ben_okunus"]})</span><br><small style="color:#cbd5e1 !important;">{kart["ornek_bn"]}</small></div>'
        f'</div>'
        f'<div style="text-align:center;"><span class="flip-hint">🔄 Ön Yüze Dönmek İçin Tekrar Dokun</span></div>'
        f'</div>'
        f'</div>'
        f'</label>'
    )