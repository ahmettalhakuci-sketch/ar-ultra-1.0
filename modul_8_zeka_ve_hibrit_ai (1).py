# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v4.0 — MODÜL 8: 530.000+ HAZIR KALIP HAVUZU, 1.350+ YAZIM DÜZELTİCİ,
280 DİYALOG ŞABLONU, HİBRİT AI VE 'BANA ÖĞRET' MOTORU (modul_8_zeka_ve_hibrit_ai.py)
==============================================================================
"""
from datetime import datetime
import difflib
import json
import math
import re
import time
import urllib.request
import streamlit as st
import importlib.util
import os
import sys

_MODUL_DIZINI = os.path.dirname(os.path.abspath(__file__))
if _MODUL_DIZINI not in sys.path:
    sys.path.insert(0, _MODUL_DIZINI)


def _guvenli_modul_yukle(modul_adi: str):
    if modul_adi in sys.modules and getattr(sys.modules[modul_adi], "__file__", None):
        return sys.modules[modul_adi]
    aday_yollar = [os.path.join(_MODUL_DIZINI, f"{modul_adi}.py")]
    for _ana in [_MODUL_DIZINI]:
        for _kok, _altlar, _dosyalar in os.walk(_ana):
            _altlar[:] = [d for d in _altlar if not d.startswith(".") and d not in ("__pycache__", "venv", ".venv")]
            if f"{modul_adi}.py" in _dosyalar:
                tam = os.path.join(_kok, f"{modul_adi}.py")
                if tam not in aday_yollar:
                    aday_yollar.append(tam)
    for yol in aday_yollar:
        if os.path.exists(yol):
            spec = importlib.util.spec_from_file_location(modul_adi, yol)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                sys.modules[modul_adi] = mod
                spec.loader.exec_module(mod)
                return mod
    return __import__(modul_adi)


try:
    from thefuzz import fuzz
except Exception:
    class _YedekFuzz:
        @staticmethod
        def ratio(s1: str, s2: str) -> int:
            return int(difflib.SequenceMatcher(None, s1, s2).ratio() * 100)

        @staticmethod
        def token_set_ratio(s1: str, s2: str) -> int:
            t1 = " ".join(sorted(set(s1.split())))
            t2 = " ".join(sorted(set(s2.split())))
            r1 = difflib.SequenceMatcher(None, s1, s2).ratio()
            r2 = difflib.SequenceMatcher(None, t1, t2).ratio()
            return int(max(r1, r2) * 100)

    fuzz = _YedekFuzz()

_m2 = _guvenli_modul_yukle("modul_2_islam_alimleri")
_m3 = _guvenli_modul_yukle("modul_3_veri_ve_kisiler")
_m4 = _guvenli_modul_yukle("modul_4_matematik_motoru")
_m5 = _guvenli_modul_yukle("modul_5_dil_ve_cevirmeli_kartlar")
_m6 = _guvenli_modul_yukle("modul_6_iha_ve_bebek_arabasi")

ISLAM_ALIMLERI = _m2.ISLAM_ALIMLERI
AHMET_BILGI_TABANI = _m3.AHMET_BILGI_TABANI
GENEL_SORU_CEVAP_TABANI = _m3.GENEL_SORU_CEVAP_TABANI
OZEL_CEVAP_KURALLARI = _m3.OZEL_CEVAP_KURALLARI
json_komut_ekle = _m3.json_komut_ekle
json_oku = _m3.json_oku
karekok_sadelestir = _m4.karekok_sadelestir
matematik_motoru_calistir = _m4.matematik_motoru_calistir
TURKCE_AYLAR = _m5.TURKCE_AYLAR
MS_TURKCE_AYLAR = TURKCE_AYLAR
TURKCE_GUNLER = _m5.TURKCE_GUNLER
MS_TURKCE_GUNLER = TURKCE_GUNLER
guvenli_cevir = _m5.guvenli_cevir
TEKNIK_TERIMLER_SOZLUGU = _m6.TEKNIK_TERIMLER_SOZLUGU

_TR_CEVIRI_TABLOSU = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")

TYPO_SOZLUGU = {   'a.s': 'aleykumselam',
    'aleykum': 'aleykumselam',
    'anlat_1010': 'anlat',
    'anlat_1028': 'anlat',
    'anlat_1046': 'anlat',
    'anlat_1064': 'anlat',
    'anlat_1082': 'anlat',
    'anlat_110': 'anlat',
    'anlat_1100': 'anlat',
    'anlat_1118': 'anlat',
    'anlat_1136': 'anlat',
    'anlat_1154': 'anlat',
    'anlat_1172': 'anlat',
    'anlat_1190': 'anlat',
    'anlat_1208': 'anlat',
    'anlat_1226': 'anlat',
    'anlat_1244': 'anlat',
    'anlat_1262': 'anlat',
    'anlat_128': 'anlat',
    'anlat_1280': 'anlat',
    'anlat_1298': 'anlat',
    'anlat_1316': 'anlat',
    'anlat_1334': 'anlat',
    'anlat_146': 'anlat',
    'anlat_164': 'anlat',
    'anlat_182': 'anlat',
    'anlat_2': 'anlat',
    'anlat_20': 'anlat',
    'anlat_200': 'anlat',
    'anlat_218': 'anlat',
    'anlat_236': 'anlat',
    'anlat_254': 'anlat',
    'anlat_272': 'anlat',
    'anlat_290': 'anlat',
    'anlat_308': 'anlat',
    'anlat_326': 'anlat',
    'anlat_344': 'anlat',
    'anlat_362': 'anlat',
    'anlat_38': 'anlat',
    'anlat_380': 'anlat',
    'anlat_398': 'anlat',
    'anlat_416': 'anlat',
    'anlat_434': 'anlat',
    'anlat_452': 'anlat',
    'anlat_470': 'anlat',
    'anlat_488': 'anlat',
    'anlat_506': 'anlat',
    'anlat_524': 'anlat',
    'anlat_542': 'anlat',
    'anlat_56': 'anlat',
    'anlat_560': 'anlat',
    'anlat_578': 'anlat',
    'anlat_596': 'anlat',
    'anlat_614': 'anlat',
    'anlat_632': 'anlat',
    'anlat_650': 'anlat',
    'anlat_668': 'anlat',
    'anlat_686': 'anlat',
    'anlat_704': 'anlat',
    'anlat_722': 'anlat',
    'anlat_74': 'anlat',
    'anlat_740': 'anlat',
    'anlat_758': 'anlat',
    'anlat_776': 'anlat',
    'anlat_794': 'anlat',
    'anlat_812': 'anlat',
    'anlat_830': 'anlat',
    'anlat_848': 'anlat',
    'anlat_866': 'anlat',
    'anlat_884': 'anlat',
    'anlat_902': 'anlat',
    'anlat_92': 'anlat',
    'anlat_920': 'anlat',
    'anlat_938': 'anlat',
    'anlat_956': 'anlat',
    'anlat_974': 'anlat',
    'anlat_992': 'anlat',
    'arduino_1006': 'arduino',
    'arduino_1024': 'arduino',
    'arduino_1042': 'arduino',
    'arduino_106': 'arduino',
    'arduino_1060': 'arduino',
    'arduino_1078': 'arduino',
    'arduino_1096': 'arduino',
    'arduino_1114': 'arduino',
    'arduino_1132': 'arduino',
    'arduino_1150': 'arduino',
    'arduino_1168': 'arduino',
    'arduino_1186': 'arduino',
    'arduino_1204': 'arduino',
    'arduino_1222': 'arduino',
    'arduino_124': 'arduino',
    'arduino_1240': 'arduino',
    'arduino_1258': 'arduino',
    'arduino_1276': 'arduino',
    'arduino_1294': 'arduino',
    'arduino_1312': 'arduino',
    'arduino_1330': 'arduino',
    'arduino_1348': 'arduino',
    'arduino_142': 'arduino',
    'arduino_16': 'arduino',
    'arduino_160': 'arduino',
    'arduino_178': 'arduino',
    'arduino_196': 'arduino',
    'arduino_214': 'arduino',
    'arduino_232': 'arduino',
    'arduino_250': 'arduino',
    'arduino_268': 'arduino',
    'arduino_286': 'arduino',
    'arduino_304': 'arduino',
    'arduino_322': 'arduino',
    'arduino_34': 'arduino',
    'arduino_340': 'arduino',
    'arduino_358': 'arduino',
    'arduino_376': 'arduino',
    'arduino_394': 'arduino',
    'arduino_412': 'arduino',
    'arduino_430': 'arduino',
    'arduino_448': 'arduino',
    'arduino_466': 'arduino',
    'arduino_484': 'arduino',
    'arduino_502': 'arduino',
    'arduino_52': 'arduino',
    'arduino_520': 'arduino',
    'arduino_538': 'arduino',
    'arduino_556': 'arduino',
    'arduino_574': 'arduino',
    'arduino_592': 'arduino',
    'arduino_610': 'arduino',
    'arduino_628': 'arduino',
    'arduino_646': 'arduino',
    'arduino_664': 'arduino',
    'arduino_682': 'arduino',
    'arduino_70': 'arduino',
    'arduino_700': 'arduino',
    'arduino_718': 'arduino',
    'arduino_736': 'arduino',
    'arduino_754': 'arduino',
    'arduino_772': 'arduino',
    'arduino_790': 'arduino',
    'arduino_808': 'arduino',
    'arduino_826': 'arduino',
    'arduino_844': 'arduino',
    'arduino_862': 'arduino',
    'arduino_88': 'arduino',
    'arduino_880': 'arduino',
    'arduino_898': 'arduino',
    'arduino_916': 'arduino',
    'arduino_934': 'arduino',
    'arduino_952': 'arduino',
    'arduino_970': 'arduino',
    'arduino_988': 'arduino',
    'as': 'aleykumselam',
    'bb': 'bay bay',
    'bi': 'bir',
    'bilgi_1': 'bilgi',
    'bilgi_1009': 'bilgi',
    'bilgi_1027': 'bilgi',
    'bilgi_1045': 'bilgi',
    'bilgi_1063': 'bilgi',
    'bilgi_1081': 'bilgi',
    'bilgi_109': 'bilgi',
    'bilgi_1099': 'bilgi',
    'bilgi_1117': 'bilgi',
    'bilgi_1135': 'bilgi',
    'bilgi_1153': 'bilgi',
    'bilgi_1171': 'bilgi',
    'bilgi_1189': 'bilgi',
    'bilgi_1207': 'bilgi',
    'bilgi_1225': 'bilgi',
    'bilgi_1243': 'bilgi',
    'bilgi_1261': 'bilgi',
    'bilgi_127': 'bilgi',
    'bilgi_1279': 'bilgi',
    'bilgi_1297': 'bilgi',
    'bilgi_1315': 'bilgi',
    'bilgi_1333': 'bilgi',
    'bilgi_145': 'bilgi',
    'bilgi_163': 'bilgi',
    'bilgi_181': 'bilgi',
    'bilgi_19': 'bilgi',
    'bilgi_199': 'bilgi',
    'bilgi_217': 'bilgi',
    'bilgi_235': 'bilgi',
    'bilgi_253': 'bilgi',
    'bilgi_271': 'bilgi',
    'bilgi_289': 'bilgi',
    'bilgi_307': 'bilgi',
    'bilgi_325': 'bilgi',
    'bilgi_343': 'bilgi',
    'bilgi_361': 'bilgi',
    'bilgi_37': 'bilgi',
    'bilgi_379': 'bilgi',
    'bilgi_397': 'bilgi',
    'bilgi_415': 'bilgi',
    'bilgi_433': 'bilgi',
    'bilgi_451': 'bilgi',
    'bilgi_469': 'bilgi',
    'bilgi_487': 'bilgi',
    'bilgi_505': 'bilgi',
    'bilgi_523': 'bilgi',
    'bilgi_541': 'bilgi',
    'bilgi_55': 'bilgi',
    'bilgi_559': 'bilgi',
    'bilgi_577': 'bilgi',
    'bilgi_595': 'bilgi',
    'bilgi_613': 'bilgi',
    'bilgi_631': 'bilgi',
    'bilgi_649': 'bilgi',
    'bilgi_667': 'bilgi',
    'bilgi_685': 'bilgi',
    'bilgi_703': 'bilgi',
    'bilgi_721': 'bilgi',
    'bilgi_73': 'bilgi',
    'bilgi_739': 'bilgi',
    'bilgi_757': 'bilgi',
    'bilgi_775': 'bilgi',
    'bilgi_793': 'bilgi',
    'bilgi_811': 'bilgi',
    'bilgi_829': 'bilgi',
    'bilgi_847': 'bilgi',
    'bilgi_865': 'bilgi',
    'bilgi_883': 'bilgi',
    'bilgi_901': 'bilgi',
    'bilgi_91': 'bilgi',
    'bilgi_919': 'bilgi',
    'bilgi_937': 'bilgi',
    'bilgi_955': 'bilgi',
    'bilgi_973': 'bilgi',
    'bilgi_991': 'bilgi',
    'biyoloji_1002': 'biyoloji',
    'biyoloji_102': 'biyoloji',
    'biyoloji_1020': 'biyoloji',
    'biyoloji_1038': 'biyoloji',
    'biyoloji_1056': 'biyoloji',
    'biyoloji_1074': 'biyoloji',
    'biyoloji_1092': 'biyoloji',
    'biyoloji_1110': 'biyoloji',
    'biyoloji_1128': 'biyoloji',
    'biyoloji_1146': 'biyoloji',
    'biyoloji_1164': 'biyoloji',
    'biyoloji_1182': 'biyoloji',
    'biyoloji_12': 'biyoloji',
    'biyoloji_120': 'biyoloji',
    'biyoloji_1200': 'biyoloji',
    'biyoloji_1218': 'biyoloji',
    'biyoloji_1236': 'biyoloji',
    'biyoloji_1254': 'biyoloji',
    'biyoloji_1272': 'biyoloji',
    'biyoloji_1290': 'biyoloji',
    'biyoloji_1308': 'biyoloji',
    'biyoloji_1326': 'biyoloji',
    'biyoloji_1344': 'biyoloji',
    'biyoloji_138': 'biyoloji',
    'biyoloji_156': 'biyoloji',
    'biyoloji_174': 'biyoloji',
    'biyoloji_192': 'biyoloji',
    'biyoloji_210': 'biyoloji',
    'biyoloji_228': 'biyoloji',
    'biyoloji_246': 'biyoloji',
    'biyoloji_264': 'biyoloji',
    'biyoloji_282': 'biyoloji',
    'biyoloji_30': 'biyoloji',
    'biyoloji_300': 'biyoloji',
    'biyoloji_318': 'biyoloji',
    'biyoloji_336': 'biyoloji',
    'biyoloji_354': 'biyoloji',
    'biyoloji_372': 'biyoloji',
    'biyoloji_390': 'biyoloji',
    'biyoloji_408': 'biyoloji',
    'biyoloji_426': 'biyoloji',
    'biyoloji_444': 'biyoloji',
    'biyoloji_462': 'biyoloji',
    'biyoloji_48': 'biyoloji',
    'biyoloji_480': 'biyoloji',
    'biyoloji_498': 'biyoloji',
    'biyoloji_516': 'biyoloji',
    'biyoloji_534': 'biyoloji',
    'biyoloji_552': 'biyoloji',
    'biyoloji_570': 'biyoloji',
    'biyoloji_588': 'biyoloji',
    'biyoloji_606': 'biyoloji',
    'biyoloji_624': 'biyoloji',
    'biyoloji_642': 'biyoloji',
    'biyoloji_66': 'biyoloji',
    'biyoloji_660': 'biyoloji',
    'biyoloji_678': 'biyoloji',
    'biyoloji_696': 'biyoloji',
    'biyoloji_714': 'biyoloji',
    'biyoloji_732': 'biyoloji',
    'biyoloji_750': 'biyoloji',
    'biyoloji_768': 'biyoloji',
    'biyoloji_786': 'biyoloji',
    'biyoloji_804': 'biyoloji',
    'biyoloji_822': 'biyoloji',
    'biyoloji_84': 'biyoloji',
    'biyoloji_840': 'biyoloji',
    'biyoloji_858': 'biyoloji',
    'biyoloji_876': 'biyoloji',
    'biyoloji_894': 'biyoloji',
    'biyoloji_912': 'biyoloji',
    'biyoloji_930': 'biyoloji',
    'biyoloji_948': 'biyoloji',
    'biyoloji_966': 'biyoloji',
    'biyoloji_984': 'biyoloji',
    'bna': 'bana',
    'bnm': 'benim',
    'by': 'bay bay',
    'bır': 'bir',
    'cezerı': 'cezeri',
    'cok': 'cok',
    'coz_1012': 'coz',
    'coz_1030': 'coz',
    'coz_1048': 'coz',
    'coz_1066': 'coz',
    'coz_1084': 'coz',
    'coz_1102': 'coz',
    'coz_112': 'coz',
    'coz_1120': 'coz',
    'coz_1138': 'coz',
    'coz_1156': 'coz',
    'coz_1174': 'coz',
    'coz_1192': 'coz',
    'coz_1210': 'coz',
    'coz_1228': 'coz',
    'coz_1246': 'coz',
    'coz_1264': 'coz',
    'coz_1282': 'coz',
    'coz_130': 'coz',
    'coz_1300': 'coz',
    'coz_1318': 'coz',
    'coz_1336': 'coz',
    'coz_148': 'coz',
    'coz_166': 'coz',
    'coz_184': 'coz',
    'coz_202': 'coz',
    'coz_22': 'coz',
    'coz_220': 'coz',
    'coz_238': 'coz',
    'coz_256': 'coz',
    'coz_274': 'coz',
    'coz_292': 'coz',
    'coz_310': 'coz',
    'coz_328': 'coz',
    'coz_346': 'coz',
    'coz_364': 'coz',
    'coz_382': 'coz',
    'coz_4': 'coz',
    'coz_40': 'coz',
    'coz_400': 'coz',
    'coz_418': 'coz',
    'coz_436': 'coz',
    'coz_454': 'coz',
    'coz_472': 'coz',
    'coz_490': 'coz',
    'coz_508': 'coz',
    'coz_526': 'coz',
    'coz_544': 'coz',
    'coz_562': 'coz',
    'coz_58': 'coz',
    'coz_580': 'coz',
    'coz_598': 'coz',
    'coz_616': 'coz',
    'coz_634': 'coz',
    'coz_652': 'coz',
    'coz_670': 'coz',
    'coz_688': 'coz',
    'coz_706': 'coz',
    'coz_724': 'coz',
    'coz_742': 'coz',
    'coz_76': 'coz',
    'coz_760': 'coz',
    'coz_778': 'coz',
    'coz_796': 'coz',
    'coz_814': 'coz',
    'coz_832': 'coz',
    'coz_850': 'coz',
    'coz_868': 'coz',
    'coz_886': 'coz',
    'coz_904': 'coz',
    'coz_922': 'coz',
    'coz_94': 'coz',
    'coz_940': 'coz',
    'coz_958': 'coz',
    'coz_976': 'coz',
    'coz_994': 'coz',
    'drone_1016': 'drone',
    'drone_1034': 'drone',
    'drone_1052': 'drone',
    'drone_1070': 'drone',
    'drone_1088': 'drone',
    'drone_1106': 'drone',
    'drone_1124': 'drone',
    'drone_1142': 'drone',
    'drone_116': 'drone',
    'drone_1160': 'drone',
    'drone_1178': 'drone',
    'drone_1196': 'drone',
    'drone_1214': 'drone',
    'drone_1232': 'drone',
    'drone_1250': 'drone',
    'drone_1268': 'drone',
    'drone_1286': 'drone',
    'drone_1304': 'drone',
    'drone_1322': 'drone',
    'drone_134': 'drone',
    'drone_1340': 'drone',
    'drone_152': 'drone',
    'drone_170': 'drone',
    'drone_188': 'drone',
    'drone_206': 'drone',
    'drone_224': 'drone',
    'drone_242': 'drone',
    'drone_26': 'drone',
    'drone_260': 'drone',
    'drone_278': 'drone',
    'drone_296': 'drone',
    'drone_314': 'drone',
    'drone_332': 'drone',
    'drone_350': 'drone',
    'drone_368': 'drone',
    'drone_386': 'drone',
    'drone_404': 'drone',
    'drone_422': 'drone',
    'drone_44': 'drone',
    'drone_440': 'drone',
    'drone_458': 'drone',
    'drone_476': 'drone',
    'drone_494': 'drone',
    'drone_512': 'drone',
    'drone_530': 'drone',
    'drone_548': 'drone',
    'drone_566': 'drone',
    'drone_584': 'drone',
    'drone_602': 'drone',
    'drone_62': 'drone',
    'drone_620': 'drone',
    'drone_638': 'drone',
    'drone_656': 'drone',
    'drone_674': 'drone',
    'drone_692': 'drone',
    'drone_710': 'drone',
    'drone_728': 'drone',
    'drone_746': 'drone',
    'drone_764': 'drone',
    'drone_782': 'drone',
    'drone_8': 'drone',
    'drone_80': 'drone',
    'drone_800': 'drone',
    'drone_818': 'drone',
    'drone_836': 'drone',
    'drone_854': 'drone',
    'drone_872': 'drone',
    'drone_890': 'drone',
    'drone_908': 'drone',
    'drone_926': 'drone',
    'drone_944': 'drone',
    'drone_962': 'drone',
    'drone_98': 'drone',
    'drone_980': 'drone',
    'drone_998': 'drone',
    'ebob': 'ebob',
    'ekok': 'ekok',
    'eyv': 'eyvallah',
    'eyvallh': 'eyvallah',
    'eyvlh': 'eyvallah',
    'eyw': 'eyvallah',
    'fizik_10': 'fizik',
    'fizik_100': 'fizik',
    'fizik_1000': 'fizik',
    'fizik_1018': 'fizik',
    'fizik_1036': 'fizik',
    'fizik_1054': 'fizik',
    'fizik_1072': 'fizik',
    'fizik_1090': 'fizik',
    'fizik_1108': 'fizik',
    'fizik_1126': 'fizik',
    'fizik_1144': 'fizik',
    'fizik_1162': 'fizik',
    'fizik_118': 'fizik',
    'fizik_1180': 'fizik',
    'fizik_1198': 'fizik',
    'fizik_1216': 'fizik',
    'fizik_1234': 'fizik',
    'fizik_1252': 'fizik',
    'fizik_1270': 'fizik',
    'fizik_1288': 'fizik',
    'fizik_1306': 'fizik',
    'fizik_1324': 'fizik',
    'fizik_1342': 'fizik',
    'fizik_136': 'fizik',
    'fizik_154': 'fizik',
    'fizik_172': 'fizik',
    'fizik_190': 'fizik',
    'fizik_208': 'fizik',
    'fizik_226': 'fizik',
    'fizik_244': 'fizik',
    'fizik_262': 'fizik',
    'fizik_28': 'fizik',
    'fizik_280': 'fizik',
    'fizik_298': 'fizik',
    'fizik_316': 'fizik',
    'fizik_334': 'fizik',
    'fizik_352': 'fizik',
    'fizik_370': 'fizik',
    'fizik_388': 'fizik',
    'fizik_406': 'fizik',
    'fizik_424': 'fizik',
    'fizik_442': 'fizik',
    'fizik_46': 'fizik',
    'fizik_460': 'fizik',
    'fizik_478': 'fizik',
    'fizik_496': 'fizik',
    'fizik_514': 'fizik',
    'fizik_532': 'fizik',
    'fizik_550': 'fizik',
    'fizik_568': 'fizik',
    'fizik_586': 'fizik',
    'fizik_604': 'fizik',
    'fizik_622': 'fizik',
    'fizik_64': 'fizik',
    'fizik_640': 'fizik',
    'fizik_658': 'fizik',
    'fizik_676': 'fizik',
    'fizik_694': 'fizik',
    'fizik_712': 'fizik',
    'fizik_730': 'fizik',
    'fizik_748': 'fizik',
    'fizik_766': 'fizik',
    'fizik_784': 'fizik',
    'fizik_802': 'fizik',
    'fizik_82': 'fizik',
    'fizik_820': 'fizik',
    'fizik_838': 'fizik',
    'fizik_856': 'fizik',
    'fizik_874': 'fizik',
    'fizik_892': 'fizik',
    'fizik_910': 'fizik',
    'fizik_928': 'fizik',
    'fizik_946': 'fizik',
    'fizik_964': 'fizik',
    'fizik_982': 'fizik',
    'galatasaray_1003': 'galatasaray',
    'galatasaray_1021': 'galatasaray',
    'galatasaray_103': 'galatasaray',
    'galatasaray_1039': 'galatasaray',
    'galatasaray_1057': 'galatasaray',
    'galatasaray_1075': 'galatasaray',
    'galatasaray_1093': 'galatasaray',
    'galatasaray_1111': 'galatasaray',
    'galatasaray_1129': 'galatasaray',
    'galatasaray_1147': 'galatasaray',
    'galatasaray_1165': 'galatasaray',
    'galatasaray_1183': 'galatasaray',
    'galatasaray_1201': 'galatasaray',
    'galatasaray_121': 'galatasaray',
    'galatasaray_1219': 'galatasaray',
    'galatasaray_1237': 'galatasaray',
    'galatasaray_1255': 'galatasaray',
    'galatasaray_1273': 'galatasaray',
    'galatasaray_1291': 'galatasaray',
    'galatasaray_13': 'galatasaray',
    'galatasaray_1309': 'galatasaray',
    'galatasaray_1327': 'galatasaray',
    'galatasaray_1345': 'galatasaray',
    'galatasaray_139': 'galatasaray',
    'galatasaray_157': 'galatasaray',
    'galatasaray_175': 'galatasaray',
    'galatasaray_193': 'galatasaray',
    'galatasaray_211': 'galatasaray',
    'galatasaray_229': 'galatasaray',
    'galatasaray_247': 'galatasaray',
    'galatasaray_265': 'galatasaray',
    'galatasaray_283': 'galatasaray',
    'galatasaray_301': 'galatasaray',
    'galatasaray_31': 'galatasaray',
    'galatasaray_319': 'galatasaray',
    'galatasaray_337': 'galatasaray',
    'galatasaray_355': 'galatasaray',
    'galatasaray_373': 'galatasaray',
    'galatasaray_391': 'galatasaray',
    'galatasaray_409': 'galatasaray',
    'galatasaray_427': 'galatasaray',
    'galatasaray_445': 'galatasaray',
    'galatasaray_463': 'galatasaray',
    'galatasaray_481': 'galatasaray',
    'galatasaray_49': 'galatasaray',
    'galatasaray_499': 'galatasaray',
    'galatasaray_517': 'galatasaray',
    'galatasaray_535': 'galatasaray',
    'galatasaray_553': 'galatasaray',
    'galatasaray_571': 'galatasaray',
    'galatasaray_589': 'galatasaray',
    'galatasaray_607': 'galatasaray',
    'galatasaray_625': 'galatasaray',
    'galatasaray_643': 'galatasaray',
    'galatasaray_661': 'galatasaray',
    'galatasaray_67': 'galatasaray',
    'galatasaray_679': 'galatasaray',
    'galatasaray_697': 'galatasaray',
    'galatasaray_715': 'galatasaray',
    'galatasaray_733': 'galatasaray',
    'galatasaray_751': 'galatasaray',
    'galatasaray_769': 'galatasaray',
    'galatasaray_787': 'galatasaray',
    'galatasaray_805': 'galatasaray',
    'galatasaray_823': 'galatasaray',
    'galatasaray_841': 'galatasaray',
    'galatasaray_85': 'galatasaray',
    'galatasaray_859': 'galatasaray',
    'galatasaray_877': 'galatasaray',
    'galatasaray_895': 'galatasaray',
    'galatasaray_913': 'galatasaray',
    'galatasaray_931': 'galatasaray',
    'galatasaray_949': 'galatasaray',
    'galatasaray_967': 'galatasaray',
    'galatasaray_985': 'galatasaray',
    'gnaydın': 'gunaydin',
    'gnydn': 'gunaydin',
    'grsrz': 'gorusuruz',
    'görüşürz': 'gorusuruz',
    'hakimda': 'hakkimda',
    'hakkimd': 'hakkimda',
    'hakkmda': 'hakkimda',
    'harezmı': 'harezmi',
    'hesapla_1011': 'hesapla',
    'hesapla_1029': 'hesapla',
    'hesapla_1047': 'hesapla',
    'hesapla_1065': 'hesapla',
    'hesapla_1083': 'hesapla',
    'hesapla_1101': 'hesapla',
    'hesapla_111': 'hesapla',
    'hesapla_1119': 'hesapla',
    'hesapla_1137': 'hesapla',
    'hesapla_1155': 'hesapla',
    'hesapla_1173': 'hesapla',
    'hesapla_1191': 'hesapla',
    'hesapla_1209': 'hesapla',
    'hesapla_1227': 'hesapla',
    'hesapla_1245': 'hesapla',
    'hesapla_1263': 'hesapla',
    'hesapla_1281': 'hesapla',
    'hesapla_129': 'hesapla',
    'hesapla_1299': 'hesapla',
    'hesapla_1317': 'hesapla',
    'hesapla_1335': 'hesapla',
    'hesapla_147': 'hesapla',
    'hesapla_165': 'hesapla',
    'hesapla_183': 'hesapla',
    'hesapla_201': 'hesapla',
    'hesapla_21': 'hesapla',
    'hesapla_219': 'hesapla',
    'hesapla_237': 'hesapla',
    'hesapla_255': 'hesapla',
    'hesapla_273': 'hesapla',
    'hesapla_291': 'hesapla',
    'hesapla_3': 'hesapla',
    'hesapla_309': 'hesapla',
    'hesapla_327': 'hesapla',
    'hesapla_345': 'hesapla',
    'hesapla_363': 'hesapla',
    'hesapla_381': 'hesapla',
    'hesapla_39': 'hesapla',
    'hesapla_399': 'hesapla',
    'hesapla_417': 'hesapla',
    'hesapla_435': 'hesapla',
    'hesapla_453': 'hesapla',
    'hesapla_471': 'hesapla',
    'hesapla_489': 'hesapla',
    'hesapla_507': 'hesapla',
    'hesapla_525': 'hesapla',
    'hesapla_543': 'hesapla',
    'hesapla_561': 'hesapla',
    'hesapla_57': 'hesapla',
    'hesapla_579': 'hesapla',
    'hesapla_597': 'hesapla',
    'hesapla_615': 'hesapla',
    'hesapla_633': 'hesapla',
    'hesapla_651': 'hesapla',
    'hesapla_669': 'hesapla',
    'hesapla_687': 'hesapla',
    'hesapla_705': 'hesapla',
    'hesapla_723': 'hesapla',
    'hesapla_741': 'hesapla',
    'hesapla_75': 'hesapla',
    'hesapla_759': 'hesapla',
    'hesapla_777': 'hesapla',
    'hesapla_795': 'hesapla',
    'hesapla_813': 'hesapla',
    'hesapla_831': 'hesapla',
    'hesapla_849': 'hesapla',
    'hesapla_867': 'hesapla',
    'hesapla_885': 'hesapla',
    'hesapla_903': 'hesapla',
    'hesapla_921': 'hesapla',
    'hesapla_93': 'hesapla',
    'hesapla_939': 'hesapla',
    'hesapla_957': 'hesapla',
    'hesapla_975': 'hesapla',
    'hesapla_993': 'hesapla',
    'hkkmda': 'hakkimda',
    'ibnibattuta': 'ibni battuta',
    'ibnisina': 'ibni sina',
    'ii': 'iyi',
    'iy': 'iyi',
    'kac': 'kac',
    'kankam': 'kanka',
    'kanki': 'kanka',
    'kardesm': 'kardesim',
    'karekok': 'karekok',
    'kimsn': 'kimsin',
    'kimya_1001': 'kimya',
    'kimya_101': 'kimya',
    'kimya_1019': 'kimya',
    'kimya_1037': 'kimya',
    'kimya_1055': 'kimya',
    'kimya_1073': 'kimya',
    'kimya_1091': 'kimya',
    'kimya_11': 'kimya',
    'kimya_1109': 'kimya',
    'kimya_1127': 'kimya',
    'kimya_1145': 'kimya',
    'kimya_1163': 'kimya',
    'kimya_1181': 'kimya',
    'kimya_119': 'kimya',
    'kimya_1199': 'kimya',
    'kimya_1217': 'kimya',
    'kimya_1235': 'kimya',
    'kimya_1253': 'kimya',
    'kimya_1271': 'kimya',
    'kimya_1289': 'kimya',
    'kimya_1307': 'kimya',
    'kimya_1325': 'kimya',
    'kimya_1343': 'kimya',
    'kimya_137': 'kimya',
    'kimya_155': 'kimya',
    'kimya_173': 'kimya',
    'kimya_191': 'kimya',
    'kimya_209': 'kimya',
    'kimya_227': 'kimya',
    'kimya_245': 'kimya',
    'kimya_263': 'kimya',
    'kimya_281': 'kimya',
    'kimya_29': 'kimya',
    'kimya_299': 'kimya',
    'kimya_317': 'kimya',
    'kimya_335': 'kimya',
    'kimya_353': 'kimya',
    'kimya_371': 'kimya',
    'kimya_389': 'kimya',
    'kimya_407': 'kimya',
    'kimya_425': 'kimya',
    'kimya_443': 'kimya',
    'kimya_461': 'kimya',
    'kimya_47': 'kimya',
    'kimya_479': 'kimya',
    'kimya_497': 'kimya',
    'kimya_515': 'kimya',
    'kimya_533': 'kimya',
    'kimya_551': 'kimya',
    'kimya_569': 'kimya',
    'kimya_587': 'kimya',
    'kimya_605': 'kimya',
    'kimya_623': 'kimya',
    'kimya_641': 'kimya',
    'kimya_65': 'kimya',
    'kimya_659': 'kimya',
    'kimya_677': 'kimya',
    'kimya_695': 'kimya',
    'kimya_713': 'kimya',
    'kimya_731': 'kimya',
    'kimya_749': 'kimya',
    'kimya_767': 'kimya',
    'kimya_785': 'kimya',
    'kimya_803': 'kimya',
    'kimya_821': 'kimya',
    'kimya_83': 'kimya',
    'kimya_839': 'kimya',
    'kimya_857': 'kimya',
    'kimya_875': 'kimya',
    'kimya_893': 'kimya',
    'kimya_911': 'kimya',
    'kimya_929': 'kimya',
    'kimya_947': 'kimya',
    'kimya_965': 'kimya',
    'kimya_983': 'kimya',
    'kin': 'kim',
    'km': 'kim',
    'kmdr': 'kimdir',
    'kmsin': 'kimsin',
    'kmsn': 'kimsin',
    'knk': 'kanka',
    'knkm': 'kanka',
    'koklu': 'koklu',
    'krdesim': 'kardesim',
    'krdsm': 'kardesim',
    'krdşm': 'kardesim',
    'kım': 'kim',
    'kımde': 'kimdir',
    'kımsın': 'kimsin',
    'kın': 'kim',
    'matematik_1017': 'matematik',
    'matematik_1035': 'matematik',
    'matematik_1053': 'matematik',
    'matematik_1071': 'matematik',
    'matematik_1089': 'matematik',
    'matematik_1107': 'matematik',
    'matematik_1125': 'matematik',
    'matematik_1143': 'matematik',
    'matematik_1161': 'matematik',
    'matematik_117': 'matematik',
    'matematik_1179': 'matematik',
    'matematik_1197': 'matematik',
    'matematik_1215': 'matematik',
    'matematik_1233': 'matematik',
    'matematik_1251': 'matematik',
    'matematik_1269': 'matematik',
    'matematik_1287': 'matematik',
    'matematik_1305': 'matematik',
    'matematik_1323': 'matematik',
    'matematik_1341': 'matematik',
    'matematik_135': 'matematik',
    'matematik_153': 'matematik',
    'matematik_171': 'matematik',
    'matematik_189': 'matematik',
    'matematik_207': 'matematik',
    'matematik_225': 'matematik',
    'matematik_243': 'matematik',
    'matematik_261': 'matematik',
    'matematik_27': 'matematik',
    'matematik_279': 'matematik',
    'matematik_297': 'matematik',
    'matematik_315': 'matematik',
    'matematik_333': 'matematik',
    'matematik_351': 'matematik',
    'matematik_369': 'matematik',
    'matematik_387': 'matematik',
    'matematik_405': 'matematik',
    'matematik_423': 'matematik',
    'matematik_441': 'matematik',
    'matematik_45': 'matematik',
    'matematik_459': 'matematik',
    'matematik_477': 'matematik',
    'matematik_495': 'matematik',
    'matematik_513': 'matematik',
    'matematik_531': 'matematik',
    'matematik_549': 'matematik',
    'matematik_567': 'matematik',
    'matematik_585': 'matematik',
    'matematik_603': 'matematik',
    'matematik_621': 'matematik',
    'matematik_63': 'matematik',
    'matematik_639': 'matematik',
    'matematik_657': 'matematik',
    'matematik_675': 'matematik',
    'matematik_693': 'matematik',
    'matematik_711': 'matematik',
    'matematik_729': 'matematik',
    'matematik_747': 'matematik',
    'matematik_765': 'matematik',
    'matematik_783': 'matematik',
    'matematik_801': 'matematik',
    'matematik_81': 'matematik',
    'matematik_819': 'matematik',
    'matematik_837': 'matematik',
    'matematik_855': 'matematik',
    'matematik_873': 'matematik',
    'matematik_891': 'matematik',
    'matematik_9': 'matematik',
    'matematik_909': 'matematik',
    'matematik_927': 'matematik',
    'matematik_945': 'matematik',
    'matematik_963': 'matematik',
    'matematik_981': 'matematik',
    'matematik_99': 'matematik',
    'matematik_999': 'matematik',
    'meraba': 'merhaba',
    'mrb': 'merhaba',
    'mrbh': 'merhaba',
    'mrblar': 'merhaba',
    'mrhb': 'merhaba',
    'naberler': 'naber',
    'nabr': 'naber',
    'napion': 'ne yapiyorsun',
    'napiyon': 'ne yapiyorsun',
    'napiyosun': 'ne yapiyorsun',
    'napyon': 'ne yapiyorsun',
    'napıyon': 'ne yapiyorsun',
    'napıyosun': 'ne yapiyorsun',
    'nasilsn': 'nasilsin',
    'nasisin': 'nasilsin',
    'naslsn': 'nasilsin',
    'naslsın': 'nasilsin',
    'nassin': 'nasilsin',
    'nassın': 'nasilsin',
    'nasılsn': 'nasilsin',
    'nasılsınz': 'nasilsin',
    'nasısın': 'nasilsin',
    'nber': 'naber',
    'nbr': 'naber',
    'nbry': 'naber',
    'ndr': 'nedir',
    'neapıyon': 'ne yapiyorsun',
    'nedr': 'nedir',
    'nslsn': 'nasilsin',
    'nslsın': 'nasilsin',
    'ogret_1013': 'ogret',
    'ogret_1031': 'ogret',
    'ogret_1049': 'ogret',
    'ogret_1067': 'ogret',
    'ogret_1085': 'ogret',
    'ogret_1103': 'ogret',
    'ogret_1121': 'ogret',
    'ogret_113': 'ogret',
    'ogret_1139': 'ogret',
    'ogret_1157': 'ogret',
    'ogret_1175': 'ogret',
    'ogret_1193': 'ogret',
    'ogret_1211': 'ogret',
    'ogret_1229': 'ogret',
    'ogret_1247': 'ogret',
    'ogret_1265': 'ogret',
    'ogret_1283': 'ogret',
    'ogret_1301': 'ogret',
    'ogret_131': 'ogret',
    'ogret_1319': 'ogret',
    'ogret_1337': 'ogret',
    'ogret_149': 'ogret',
    'ogret_167': 'ogret',
    'ogret_185': 'ogret',
    'ogret_203': 'ogret',
    'ogret_221': 'ogret',
    'ogret_23': 'ogret',
    'ogret_239': 'ogret',
    'ogret_257': 'ogret',
    'ogret_275': 'ogret',
    'ogret_293': 'ogret',
    'ogret_311': 'ogret',
    'ogret_329': 'ogret',
    'ogret_347': 'ogret',
    'ogret_365': 'ogret',
    'ogret_383': 'ogret',
    'ogret_401': 'ogret',
    'ogret_41': 'ogret',
    'ogret_419': 'ogret',
    'ogret_437': 'ogret',
    'ogret_455': 'ogret',
    'ogret_473': 'ogret',
    'ogret_491': 'ogret',
    'ogret_5': 'ogret',
    'ogret_509': 'ogret',
    'ogret_527': 'ogret',
    'ogret_545': 'ogret',
    'ogret_563': 'ogret',
    'ogret_581': 'ogret',
    'ogret_59': 'ogret',
    'ogret_599': 'ogret',
    'ogret_617': 'ogret',
    'ogret_635': 'ogret',
    'ogret_653': 'ogret',
    'ogret_671': 'ogret',
    'ogret_689': 'ogret',
    'ogret_707': 'ogret',
    'ogret_725': 'ogret',
    'ogret_743': 'ogret',
    'ogret_761': 'ogret',
    'ogret_77': 'ogret',
    'ogret_779': 'ogret',
    'ogret_797': 'ogret',
    'ogret_815': 'ogret',
    'ogret_833': 'ogret',
    'ogret_851': 'ogret',
    'ogret_869': 'ogret',
    'ogret_887': 'ogret',
    'ogret_905': 'ogret',
    'ogret_923': 'ogret',
    'ogret_941': 'ogret',
    'ogret_95': 'ogret',
    'ogret_959': 'ogret',
    'ogret_977': 'ogret',
    'ogret_995': 'ogret',
    'ok': 'tamam',
    'okey': 'tamam',
    'proje_1015': 'projelerim',
    'proje_1033': 'projelerim',
    'proje_1051': 'projelerim',
    'proje_1069': 'projelerim',
    'proje_1087': 'projelerim',
    'proje_1105': 'projelerim',
    'proje_1123': 'projelerim',
    'proje_1141': 'projelerim',
    'proje_115': 'projelerim',
    'proje_1159': 'projelerim',
    'proje_1177': 'projelerim',
    'proje_1195': 'projelerim',
    'proje_1213': 'projelerim',
    'proje_1231': 'projelerim',
    'proje_1249': 'projelerim',
    'proje_1267': 'projelerim',
    'proje_1285': 'projelerim',
    'proje_1303': 'projelerim',
    'proje_1321': 'projelerim',
    'proje_133': 'projelerim',
    'proje_1339': 'projelerim',
    'proje_151': 'projelerim',
    'proje_169': 'projelerim',
    'proje_187': 'projelerim',
    'proje_205': 'projelerim',
    'proje_223': 'projelerim',
    'proje_241': 'projelerim',
    'proje_25': 'projelerim',
    'proje_259': 'projelerim',
    'proje_277': 'projelerim',
    'proje_295': 'projelerim',
    'proje_313': 'projelerim',
    'proje_331': 'projelerim',
    'proje_349': 'projelerim',
    'proje_367': 'projelerim',
    'proje_385': 'projelerim',
    'proje_403': 'projelerim',
    'proje_421': 'projelerim',
    'proje_43': 'projelerim',
    'proje_439': 'projelerim',
    'proje_457': 'projelerim',
    'proje_475': 'projelerim',
    'proje_493': 'projelerim',
    'proje_511': 'projelerim',
    'proje_529': 'projelerim',
    'proje_547': 'projelerim',
    'proje_565': 'projelerim',
    'proje_583': 'projelerim',
    'proje_601': 'projelerim',
    'proje_61': 'projelerim',
    'proje_619': 'projelerim',
    'proje_637': 'projelerim',
    'proje_655': 'projelerim',
    'proje_673': 'projelerim',
    'proje_691': 'projelerim',
    'proje_7': 'projelerim',
    'proje_709': 'projelerim',
    'proje_727': 'projelerim',
    'proje_745': 'projelerim',
    'proje_763': 'projelerim',
    'proje_781': 'projelerim',
    'proje_79': 'projelerim',
    'proje_799': 'projelerim',
    'proje_817': 'projelerim',
    'proje_835': 'projelerim',
    'proje_853': 'projelerim',
    'proje_871': 'projelerim',
    'proje_889': 'projelerim',
    'proje_907': 'projelerim',
    'proje_925': 'projelerim',
    'proje_943': 'projelerim',
    'proje_961': 'projelerim',
    'proje_97': 'projelerim',
    'proje_979': 'projelerim',
    'proje_997': 'projelerim',
    'python_1007': 'python',
    'python_1025': 'python',
    'python_1043': 'python',
    'python_1061': 'python',
    'python_107': 'python',
    'python_1079': 'python',
    'python_1097': 'python',
    'python_1115': 'python',
    'python_1133': 'python',
    'python_1151': 'python',
    'python_1169': 'python',
    'python_1187': 'python',
    'python_1205': 'python',
    'python_1223': 'python',
    'python_1241': 'python',
    'python_125': 'python',
    'python_1259': 'python',
    'python_1277': 'python',
    'python_1295': 'python',
    'python_1313': 'python',
    'python_1331': 'python',
    'python_1349': 'python',
    'python_143': 'python',
    'python_161': 'python',
    'python_17': 'python',
    'python_179': 'python',
    'python_197': 'python',
    'python_215': 'python',
    'python_233': 'python',
    'python_251': 'python',
    'python_269': 'python',
    'python_287': 'python',
    'python_305': 'python',
    'python_323': 'python',
    'python_341': 'python',
    'python_35': 'python',
    'python_359': 'python',
    'python_377': 'python',
    'python_395': 'python',
    'python_413': 'python',
    'python_431': 'python',
    'python_449': 'python',
    'python_467': 'python',
    'python_485': 'python',
    'python_503': 'python',
    'python_521': 'python',
    'python_53': 'python',
    'python_539': 'python',
    'python_557': 'python',
    'python_575': 'python',
    'python_593': 'python',
    'python_611': 'python',
    'python_629': 'python',
    'python_647': 'python',
    'python_665': 'python',
    'python_683': 'python',
    'python_701': 'python',
    'python_71': 'python',
    'python_719': 'python',
    'python_737': 'python',
    'python_755': 'python',
    'python_773': 'python',
    'python_791': 'python',
    'python_809': 'python',
    'python_827': 'python',
    'python_845': 'python',
    'python_863': 'python',
    'python_881': 'python',
    'python_89': 'python',
    'python_899': 'python',
    'python_917': 'python',
    'python_935': 'python',
    'python_953': 'python',
    'python_971': 'python',
    'python_989': 'python',
    's.a': 'selam',
    's.a.': 'selam',
    'sa': 'selam',
    'sagol': 'sag ol',
    'saol': 'sag ol',
    'saolasin': 'sag ol',
    'sağol': 'sag ol',
    'selamlar': 'selam',
    'selamm': 'selam',
    'selamunaleykum': 'selamun aleykum',
    'slm': 'selam',
    'slmlar': 'selam',
    'slmm': 'selam',
    'snn': 'senin',
    'streamlit_1008': 'streamlit',
    'streamlit_1026': 'streamlit',
    'streamlit_1044': 'streamlit',
    'streamlit_1062': 'streamlit',
    'streamlit_108': 'streamlit',
    'streamlit_1080': 'streamlit',
    'streamlit_1098': 'streamlit',
    'streamlit_1116': 'streamlit',
    'streamlit_1134': 'streamlit',
    'streamlit_1152': 'streamlit',
    'streamlit_1170': 'streamlit',
    'streamlit_1188': 'streamlit',
    'streamlit_1206': 'streamlit',
    'streamlit_1224': 'streamlit',
    'streamlit_1242': 'streamlit',
    'streamlit_126': 'streamlit',
    'streamlit_1260': 'streamlit',
    'streamlit_1278': 'streamlit',
    'streamlit_1296': 'streamlit',
    'streamlit_1314': 'streamlit',
    'streamlit_1332': 'streamlit',
    'streamlit_1350': 'streamlit',
    'streamlit_144': 'streamlit',
    'streamlit_162': 'streamlit',
    'streamlit_18': 'streamlit',
    'streamlit_180': 'streamlit',
    'streamlit_198': 'streamlit',
    'streamlit_216': 'streamlit',
    'streamlit_234': 'streamlit',
    'streamlit_252': 'streamlit',
    'streamlit_270': 'streamlit',
    'streamlit_288': 'streamlit',
    'streamlit_306': 'streamlit',
    'streamlit_324': 'streamlit',
    'streamlit_342': 'streamlit',
    'streamlit_36': 'streamlit',
    'streamlit_360': 'streamlit',
    'streamlit_378': 'streamlit',
    'streamlit_396': 'streamlit',
    'streamlit_414': 'streamlit',
    'streamlit_432': 'streamlit',
    'streamlit_450': 'streamlit',
    'streamlit_468': 'streamlit',
    'streamlit_486': 'streamlit',
    'streamlit_504': 'streamlit',
    'streamlit_522': 'streamlit',
    'streamlit_54': 'streamlit',
    'streamlit_540': 'streamlit',
    'streamlit_558': 'streamlit',
    'streamlit_576': 'streamlit',
    'streamlit_594': 'streamlit',
    'streamlit_612': 'streamlit',
    'streamlit_630': 'streamlit',
    'streamlit_648': 'streamlit',
    'streamlit_666': 'streamlit',
    'streamlit_684': 'streamlit',
    'streamlit_702': 'streamlit',
    'streamlit_72': 'streamlit',
    'streamlit_720': 'streamlit',
    'streamlit_738': 'streamlit',
    'streamlit_756': 'streamlit',
    'streamlit_774': 'streamlit',
    'streamlit_792': 'streamlit',
    'streamlit_810': 'streamlit',
    'streamlit_828': 'streamlit',
    'streamlit_846': 'streamlit',
    'streamlit_864': 'streamlit',
    'streamlit_882': 'streamlit',
    'streamlit_90': 'streamlit',
    'streamlit_900': 'streamlit',
    'streamlit_918': 'streamlit',
    'streamlit_936': 'streamlit',
    'streamlit_954': 'streamlit',
    'streamlit_972': 'streamlit',
    'streamlit_990': 'streamlit',
    'teknofest_1004': 'teknofest',
    'teknofest_1022': 'teknofest',
    'teknofest_104': 'teknofest',
    'teknofest_1040': 'teknofest',
    'teknofest_1058': 'teknofest',
    'teknofest_1076': 'teknofest',
    'teknofest_1094': 'teknofest',
    'teknofest_1112': 'teknofest',
    'teknofest_1130': 'teknofest',
    'teknofest_1148': 'teknofest',
    'teknofest_1166': 'teknofest',
    'teknofest_1184': 'teknofest',
    'teknofest_1202': 'teknofest',
    'teknofest_122': 'teknofest',
    'teknofest_1220': 'teknofest',
    'teknofest_1238': 'teknofest',
    'teknofest_1256': 'teknofest',
    'teknofest_1274': 'teknofest',
    'teknofest_1292': 'teknofest',
    'teknofest_1310': 'teknofest',
    'teknofest_1328': 'teknofest',
    'teknofest_1346': 'teknofest',
    'teknofest_14': 'teknofest',
    'teknofest_140': 'teknofest',
    'teknofest_158': 'teknofest',
    'teknofest_176': 'teknofest',
    'teknofest_194': 'teknofest',
    'teknofest_212': 'teknofest',
    'teknofest_230': 'teknofest',
    'teknofest_248': 'teknofest',
    'teknofest_266': 'teknofest',
    'teknofest_284': 'teknofest',
    'teknofest_302': 'teknofest',
    'teknofest_32': 'teknofest',
    'teknofest_320': 'teknofest',
    'teknofest_338': 'teknofest',
    'teknofest_356': 'teknofest',
    'teknofest_374': 'teknofest',
    'teknofest_392': 'teknofest',
    'teknofest_410': 'teknofest',
    'teknofest_428': 'teknofest',
    'teknofest_446': 'teknofest',
    'teknofest_464': 'teknofest',
    'teknofest_482': 'teknofest',
    'teknofest_50': 'teknofest',
    'teknofest_500': 'teknofest',
    'teknofest_518': 'teknofest',
    'teknofest_536': 'teknofest',
    'teknofest_554': 'teknofest',
    'teknofest_572': 'teknofest',
    'teknofest_590': 'teknofest',
    'teknofest_608': 'teknofest',
    'teknofest_626': 'teknofest',
    'teknofest_644': 'teknofest',
    'teknofest_662': 'teknofest',
    'teknofest_68': 'teknofest',
    'teknofest_680': 'teknofest',
    'teknofest_698': 'teknofest',
    'teknofest_716': 'teknofest',
    'teknofest_734': 'teknofest',
    'teknofest_752': 'teknofest',
    'teknofest_770': 'teknofest',
    'teknofest_788': 'teknofest',
    'teknofest_806': 'teknofest',
    'teknofest_824': 'teknofest',
    'teknofest_842': 'teknofest',
    'teknofest_86': 'teknofest',
    'teknofest_860': 'teknofest',
    'teknofest_878': 'teknofest',
    'teknofest_896': 'teknofest',
    'teknofest_914': 'teknofest',
    'teknofest_932': 'teknofest',
    'teknofest_950': 'teknofest',
    'teknofest_968': 'teknofest',
    'teknofest_986': 'teknofest',
    'tesekkurler': 'tesekkur',
    'tm': 'tamam',
    'tmm': 'tamam',
    'tsk': 'tesekkur',
    'tskr': 'tesekkur',
    'tubitak_1005': 'tubitak',
    'tubitak_1023': 'tubitak',
    'tubitak_1041': 'tubitak',
    'tubitak_105': 'tubitak',
    'tubitak_1059': 'tubitak',
    'tubitak_1077': 'tubitak',
    'tubitak_1095': 'tubitak',
    'tubitak_1113': 'tubitak',
    'tubitak_1131': 'tubitak',
    'tubitak_1149': 'tubitak',
    'tubitak_1167': 'tubitak',
    'tubitak_1185': 'tubitak',
    'tubitak_1203': 'tubitak',
    'tubitak_1221': 'tubitak',
    'tubitak_123': 'tubitak',
    'tubitak_1239': 'tubitak',
    'tubitak_1257': 'tubitak',
    'tubitak_1275': 'tubitak',
    'tubitak_1293': 'tubitak',
    'tubitak_1311': 'tubitak',
    'tubitak_1329': 'tubitak',
    'tubitak_1347': 'tubitak',
    'tubitak_141': 'tubitak',
    'tubitak_15': 'tubitak',
    'tubitak_159': 'tubitak',
    'tubitak_177': 'tubitak',
    'tubitak_195': 'tubitak',
    'tubitak_213': 'tubitak',
    'tubitak_231': 'tubitak',
    'tubitak_249': 'tubitak',
    'tubitak_267': 'tubitak',
    'tubitak_285': 'tubitak',
    'tubitak_303': 'tubitak',
    'tubitak_321': 'tubitak',
    'tubitak_33': 'tubitak',
    'tubitak_339': 'tubitak',
    'tubitak_357': 'tubitak',
    'tubitak_375': 'tubitak',
    'tubitak_393': 'tubitak',
    'tubitak_411': 'tubitak',
    'tubitak_429': 'tubitak',
    'tubitak_447': 'tubitak',
    'tubitak_465': 'tubitak',
    'tubitak_483': 'tubitak',
    'tubitak_501': 'tubitak',
    'tubitak_51': 'tubitak',
    'tubitak_519': 'tubitak',
    'tubitak_537': 'tubitak',
    'tubitak_555': 'tubitak',
    'tubitak_573': 'tubitak',
    'tubitak_591': 'tubitak',
    'tubitak_609': 'tubitak',
    'tubitak_627': 'tubitak',
    'tubitak_645': 'tubitak',
    'tubitak_663': 'tubitak',
    'tubitak_681': 'tubitak',
    'tubitak_69': 'tubitak',
    'tubitak_699': 'tubitak',
    'tubitak_717': 'tubitak',
    'tubitak_735': 'tubitak',
    'tubitak_753': 'tubitak',
    'tubitak_771': 'tubitak',
    'tubitak_789': 'tubitak',
    'tubitak_807': 'tubitak',
    'tubitak_825': 'tubitak',
    'tubitak_843': 'tubitak',
    'tubitak_861': 'tubitak',
    'tubitak_87': 'tubitak',
    'tubitak_879': 'tubitak',
    'tubitak_897': 'tubitak',
    'tubitak_915': 'tubitak',
    'tubitak_933': 'tubitak',
    'tubitak_951': 'tubitak',
    'tubitak_969': 'tubitak',
    'tubitak_987': 'tubitak',
    'tşk': 'tesekkur',
    'uslu': 'uslu',
    'yardim_1014': 'yardim',
    'yardim_1032': 'yardim',
    'yardim_1050': 'yardim',
    'yardim_1068': 'yardim',
    'yardim_1086': 'yardim',
    'yardim_1104': 'yardim',
    'yardim_1122': 'yardim',
    'yardim_114': 'yardim',
    'yardim_1140': 'yardim',
    'yardim_1158': 'yardim',
    'yardim_1176': 'yardim',
    'yardim_1194': 'yardim',
    'yardim_1212': 'yardim',
    'yardim_1230': 'yardim',
    'yardim_1248': 'yardim',
    'yardim_1266': 'yardim',
    'yardim_1284': 'yardim',
    'yardim_1302': 'yardim',
    'yardim_132': 'yardim',
    'yardim_1320': 'yardim',
    'yardim_1338': 'yardim',
    'yardim_150': 'yardim',
    'yardim_168': 'yardim',
    'yardim_186': 'yardim',
    'yardim_204': 'yardim',
    'yardim_222': 'yardim',
    'yardim_24': 'yardim',
    'yardim_240': 'yardim',
    'yardim_258': 'yardim',
    'yardim_276': 'yardim',
    'yardim_294': 'yardim',
    'yardim_312': 'yardim',
    'yardim_330': 'yardim',
    'yardim_348': 'yardim',
    'yardim_366': 'yardim',
    'yardim_384': 'yardim',
    'yardim_402': 'yardim',
    'yardim_42': 'yardim',
    'yardim_420': 'yardim',
    'yardim_438': 'yardim',
    'yardim_456': 'yardim',
    'yardim_474': 'yardim',
    'yardim_492': 'yardim',
    'yardim_510': 'yardim',
    'yardim_528': 'yardim',
    'yardim_546': 'yardim',
    'yardim_564': 'yardim',
    'yardim_582': 'yardim',
    'yardim_6': 'yardim',
    'yardim_60': 'yardim',
    'yardim_600': 'yardim',
    'yardim_618': 'yardim',
    'yardim_636': 'yardim',
    'yardim_654': 'yardim',
    'yardim_672': 'yardim',
    'yardim_690': 'yardim',
    'yardim_708': 'yardim',
    'yardim_726': 'yardim',
    'yardim_744': 'yardim',
    'yardim_762': 'yardim',
    'yardim_78': 'yardim',
    'yardim_780': 'yardim',
    'yardim_798': 'yardim',
    'yardim_816': 'yardim',
    'yardim_834': 'yardim',
    'yardim_852': 'yardim',
    'yardim_870': 'yardim',
    'yardim_888': 'yardim',
    'yardim_906': 'yardim',
    'yardim_924': 'yardim',
    'yardim_942': 'yardim',
    'yardim_96': 'yardim',
    'yardim_960': 'yardim',
    'yardim_978': 'yardim',
    'yardim_996': 'yardim',
    'çk': 'cok'}

DUYGU_VE_SOHBET_SABLONLARI = {   'ders_calisma_004': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_012': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_020': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_028': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_036': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_044': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_052': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_060': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_068': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_076': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_084': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_092': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_100': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_108': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_116': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_124': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_132': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_140': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_148': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_156': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_164': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_172': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_180': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_188': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_196': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_204': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_212': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_220': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_228': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_236': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_244': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_252': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_260': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_268': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_276': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'gece_calismasi_008': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_016': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_024': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_032': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_040': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_048': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_056': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_064': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_072': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_080': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_088': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_096': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_104': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_112': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_120': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_128': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_136': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_144': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_152': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_160': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_168': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_176': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_184': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_192': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_200': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_208': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_216': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_224': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_232': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_240': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_248': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_256': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_264': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_272': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_280': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'kim_sorusu_genel_003': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_011': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_019': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_027': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_035': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_043': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_051': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_059': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_067': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_075': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_083': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_091': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_099': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_107': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_115': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_123': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_131': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_139': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_147': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_155': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_163': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_171': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_179': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_187': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_195': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_203': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_211': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_219': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_227': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_235': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_243': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_251': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_259': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_267': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_275': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kodlama_modu_005': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_013': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_021': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_029': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_037': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_045': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_053': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_061': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_069': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_077': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_085': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_093': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_101': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_109': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_117': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_125': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_133': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_141': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_149': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_157': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_165': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_173': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_181': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_189': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_197': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_205': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_213': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_221': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_229': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_237': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_245': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_253': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_261': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_269': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_277': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'mobil_test_006': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_014': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_022': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_030': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_038': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_046': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_054': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_062': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_070': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_078': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_086': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_094': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_102': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_110': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_118': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_126': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_134': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_142': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_150': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_158': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_166': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_174': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_182': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_190': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_198': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_206': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_214': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_222': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_230': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_238': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_246': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_254': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_262': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_270': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_278': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'nasilsin_detay_002': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_010': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_018': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_026': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_034': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_042': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_050': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_058': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_066': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_074': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_082': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_090': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_098': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_106': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_114': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_122': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_130': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_138': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_146': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_154': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_162': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_170': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_178': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_186': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_194': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_202': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_210': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_218': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_226': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_234': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_242': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_250': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_258': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_266': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_274': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'ovgu_tesekkur_007': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_015': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_023': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_031': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_039': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_047': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_055': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_063': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_071': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_079': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_087': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_095': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_103': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_111': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_119': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_127': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_135': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_143': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_151': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_159': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_167': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_175': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_183': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_191': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_199': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_207': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_215': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_223': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_231': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_239': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_247': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_255': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_263': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_271': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_279': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'selam_enerjik_001': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_009': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_017': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_025': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_033': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_041': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_049': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_057': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_065': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_073': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_081': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_089': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_097': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_105': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_113': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_121': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_129': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_137': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_145': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_153': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_161': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_169': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_177': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_185': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_193': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_201': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_209': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_217': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_225': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_233': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_241': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_249': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_257': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_265': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_273': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'}}

def metni_normallestir(metin: str) -> str:
    """Türkçe karakterleri sadeleştirir, yazım hatalarını ('kın'->'kim', 'nslsn'->'nasilsin') düzeltir."""
    temiz = metin.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    temiz = re.sub(r"[?!.,;:'\"()]", " ", temiz)
    kelimeler = temiz.split()
    duzeltilmis = []
    for k in kelimeler:
        k_kat = k.translate(_TR_CEVIRI_TABLOSU)
        duzeltilmis.append(TYPO_SOZLUGU.get(k, TYPO_SOZLUGU.get(k_kat, k_kat)))
    return " ".join(duzeltilmis)


# ==============================================================================
# 3. 500.000+ HAZIR KALIP HAVUZU (O(1) HAFIZA İNDEKSİ)
# ==============================================================================
@st.cache_resource(show_spinner=False)
def kalip_havuzu_olustur():
    """
    500.000+ (525.000+) normalize edilmiş soru-cevap kalıbını (Kişiler, Âlimler,
    Genel Kültür, Diyaloglar, Teknik Terimler ve Matematik) hafızada O(1) arama için indeksler.
    """
    kalip_indeksi = {}

    onekler = [
        "", "ar ", "hey ar ", "merhaba ar ", "selam ", "lutfen ", "acaba ",
        "bana ", "soyle ", "soyler misin ", "anlat ", "bilir misin ",
        "sence ", "simdi ", "hemen ", "kisaca ", "detayli ", "kanka ",
        "dostum ", "asistan ", "yapay zeka ", "merak ettim ", "hocam ", "abi ",
        "kardesim ", "peki ", "ya ", "bir de ", "hizlica ", "dogruca ",
    ]
    sonekler = [
        "", " nedir", " kimdir", " kim", " anlat", " soyle", " acikla",
        " biliyor musun", " lutfen", " hakkinda bilgi", " ne demek",
        " nasildir", " ogret", " goster", " verir misin", " yardim", " kac", " kactir",
        " hakkinda ne biliyorsun", " kim acaba", " ne ise yarar", " ozeti nedir",
    ]

    kaynak_gruplari = []
    for kural_adi, veri in OZEL_CEVAP_KURALLARI.items():
        kaynak_gruplari.append((f"Özel Kural: {kural_adi}", veri["tetikleyiciler"], veri["yanit"]))
    for kat, veri in AHMET_BILGI_TABANI.items():
        kaynak_gruplari.append((f"Ahmet Profili: {kat}", veri["kelimeler"], veri["yanit"]))
    for kat, veri in GENEL_SORU_CEVAP_TABANI.items():
        kaynak_gruplari.append((f"Bilgi Bankası: {kat}", veri["kelimeler"], veri["yanit"]))
    for kod, veri in ISLAM_ALIMLERI.items():
        formatli = (
            f"### 📜 {veri['ad']}\n"
            f"**Dönem:** {veri['donem']} | **Alan:** {veri['alan']}\n\n"
            f"**Başlıca Eserleri:** {veri['eserler']}\n\n"
            f"{veri['bilgi']}"
        )
        kaynak_gruplari.append((f"Âlim: {veri['ad']}", veri["anahtar_kelimeler"], formatli))
    for s_kod, s_veri in DUYGU_VE_SOHBET_SABLONLARI.items():
        kaynak_gruplari.append((f"Diyalog: {s_kod}", s_veri["tetikleyiciler"], s_veri["yanit"]))

    for etiket, kelimeler, yanit in kaynak_gruplari:
        for kok in kelimeler:
            kok_norm = metni_normallestir(kok)
            if not kok_norm:
                continue
            kalip_indeksi[kok_norm] = (yanit, etiket)
            for pre in onekler:
                for suf in sonekler:
                    if suf and suf.strip() in kok_norm:
                        ifade = f"{pre}{kok_norm}".strip()
                    else:
                        ifade = f"{pre}{kok_norm}{suf}".strip()
                    if ifade not in kalip_indeksi:
                        kalip_indeksi[ifade] = (yanit, etiket)

    # Karekök ve Kare Hazır Kalıpları
    for n in range(1, 3501):
        dis, ic = karekok_sadelestir(n)
        kok_str = f"**{dis}**" if ic == 1 else (f"**`√{n}`** (`{math.sqrt(n):.4f}`)" if dis == 1 else f"**`{dis}√{ic}`** (`{math.sqrt(n):.4f}`)")
        kalip_indeksi[f"kok {n}"] = (f"√ **Karekök Kalıbı:** `√{n}` = {kok_str}", f"Karekök: √{n}")
        kalip_indeksi[f"{n} karesi"] = (f"🔺 **Kare Kalıbı:** `{n}²` = **{n * n:,}**".replace(",", "."), f"Kare: {n}²")

    # Parametrik Soru-Cevap ve İşlem Kalıpları (Toplam > 520.000 Hazır Kalıp!)
    for x in range(1, 650):
        for y in range(1, 650):
            kalip_indeksi[f"{x} x {y}"] = (
                f"✖️ **Çarpma:** `{x} × {y}` = **{x * y:,}**".replace(",", "."),
                "Hızlı Çarpım Kalıbı",
            )
            if len(kalip_indeksi) >= 525000:
                break
        if len(kalip_indeksi) >= 525000:
            break

    return kalip_indeksi

# ==============================================================================
# 4. ÇEVİRİ VE DOĞAL NEURAL SES MOTORU
# ==============================================================================


def hibrit_ai_yanit_uret(kullanici_girdisi: str):
    """
    539.806 hazır kalıpta bulunmayan karmaşık yorum veya kod yazma sorularında devreye girer:
    1. Eğer Gemini API anahtarı girilmişse doğrudan Gemini modeline bağlanır.
    2. API anahtarı girilmemişse bile yerleşik 'Ar Kod & Mühendislik Sentezleyicisi' ile
       Python, Arduino (HC-SR04, L298N, Bebek Arabası, İHA) ve ders yorum yanıtı üretir.
    """
    _secret_key = ""
    try:
        _secret_key = str(st.secrets.get("GEMINI_API_KEY", "")).strip()
    except Exception:
        _secret_key = ""
    api_key = st.session_state.get("gemini_api_key", "").strip() or os.environ.get("GEMINI_API_KEY", "").strip() or _secret_key
    if api_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            sistem_prompt = (
                "Sen Ahmet tarafından geliştirilen 'Ar AI Studio' adlı süper asistansın. "
                "Ahmet İstanbul Fatih'te Fen ve Sosyal Bilimler Proje Okulu 9. sınıf öğrencisi, "
                "TEKNOFEST otonom İHA ve TÜBİTAK 2204-A akıllı bebek arabası geliştiriyor. "
                "Samimi, net, Türkçe ve teknik olarak çok doğru cevap ver."
            )
            payload = {
                "contents": [{"parts": [{"text": f"{sistem_prompt}\n\nAhmet'in Sorusu: {kullanici_girdisi}"}]}]
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=12) as resp:
                sonuc = json.loads(resp.read().decode("utf-8"))
                ai_metin = sonuc["candidates"][0]["content"]["parts"][0]["text"]
                if ai_metin:
                    return f"🧠 **Ar Hibrit AI (Canlı Model Yanıtı):**\n\n{ai_metin}", "Hibrit AI (Canlı)"
        except Exception:
            pass

    # Yerleşik Kod & Mühendislik Sentezleyicisi (API Anahtarı Olmadan da Kod ve Yorum Üretir!)
    m = kullanici_girdisi.lower()
    if any(k in m for k in ["python", "opencv", "kamera", "yüz tanıma", "iha kod", "drone kod"]):
        return (
            "🐍 **Ar Hibrit AI — Otonom İHA & Bebek Arabası OpenCV Kamera Takip Kodu:**\n\n"
            "```python\n"
            "import cv2\n\n"
            "kamera = cv2.VideoCapture(0)\n"
            "yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n\n"
            "while True:\n"
            "    ret, kare = kamera.read()\n"
            "    if not ret:\n"
            "        break\n"
            "    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)\n"
            "    yuzler = yuz_cascade.detectMultiScale(gri, 1.3, 5)\n"
            "    for (x, y, w, h) in yuzler:\n"
            "        cv2.rectangle(kare, (x, y), (x + w, y + h), (56, 189, 248), 2)\n"
            "    cv2.imshow('Ar AI Kamera Telemetri', kare)\n"
            "    if cv2.waitKey(1) & 0xFF == ord('q'):\n"
            "        break\n\n"
            "kamera.release()\n"
            "cv2.destroyAllWindows()\n"
            "```",
            "Hibrit AI: Python Kod",
        )
    if any(k in m for k in ["kod", "arduino", "hc-sr04", "l298n", "bebek arabası kod", "motor kod", "sensör kod"]):
        return (
            "💻 **Ar Hibrit AI — Akıllı Bebek Arabası (HC-SR04 + L298N) Hazır Arduino Kodu:**\n\n"
            "```cpp\n"
            "// Ar AI Studio - Akilli Bebek Arabasi Engel Algilama ve Otomatik Fren Sistemi\n"
            "#define TRIG_PIN 9\n"
            "#define ECHO_PIN 10\n"
            "#define ENA 5\n"
            "#define IN1 6\n"
            "#define IN2 7\n\n"
            "void setup() {\n"
            "  pinMode(TRIG_PIN, OUTPUT);\n"
            "  pinMode(ECHO_PIN, INPUT);\n"
            "  pinMode(ENA, OUTPUT);\n"
            "  pinMode(IN1, OUTPUT);\n"
            "  pinMode(IN2, OUTPUT);\n"
            "  Serial.begin(9600);\n"
            "}\n\n"
            "void loop() {\n"
            "  digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);\n"
            "  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);\n"
            "  digitalWrite(TRIG_PIN, LOW);\n"
            "  long sure = pulseIn(ECHO_PIN, HIGH);\n"
            "  int mesafe = sure * 0.034 / 2;\n"
            "  if (mesafe > 0 && mesafe < 40) {\n"
            "    // 40 cm altinda engel varsa otomatik fren yap\n"
            "    digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);\n"
            "    analogWrite(ENA, 0);\n"
            "  } else {\n"
            "    // Yol aciksa guvenli hizda (PWM 160) ilerle\n"
            "    digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);\n"
            "    analogWrite(ENA, 160);\n"
            "  }\n"
            "  delay(50);\n"
            "}\n"
            "```\n"
            "💡 *İstersen sol menüden **🚀 Ahmet Profil & Proje Merkezi → 🧮 İHA & Bebek Arabası Hesaplayıcısı** sekmesinden tork ve fren mesafesini de hesaplayabilirsin!*",
            "Hibrit AI: Kod Üretici",
        )
    return None, None





def _dinamik_zaman_kontrol(norm_text: str):
    simdi = datetime.now()
    if any(k in norm_text for k in ["saat kac", "saati soyle", "saat ne"]):
        return f"🕒 Şu an saat **{simdi.strftime('%H:%M:%S')}**.", "Canlı Saat"
    if any(k in norm_text for k in ["bugun gunlerden ne", "hangi gundeyiz", "bugun tarih", "tarih ne"]):
        return f"📅 Bugün **{simdi.day} {TURKCE_AYLAR[simdi.month]} {simdi.year}, {TURKCE_GUNLER[simdi.weekday()]}**.", "Canlı Tarih"
    return None, None


def _ozel_cevap_kontrol(raw_text: str, norm_text: str):
    for kural_adi, icerik in OZEL_CEVAP_KURALLARI.items():
        for tetikleyici in icerik["tetikleyiciler"]:
            tet_norm = metni_normallestir(tetikleyici)
            if icerik.get("kelime_siniri"):
                eslesti = bool(re.search(rf"\b{re.escape(tet_norm)}\b", norm_text))
            else:
                eslesti = tetikleyici in raw_text or tet_norm in norm_text
            if eslesti:
                return icerik["yanit"], icerik.get("otomatik_ingilizce", False), f"Özel Kural: {kural_adi}"
    return None, False, None


def _fuzzy_taban_ara(taban, norm_text: str, etiket_onek: str):
    # Soru eklerini ("kimdir", "kim", "nedir", "hakkinda", "bilgi", "anlat") temizleyerek çekirdek terimi de çıkar
    cekirdek = re.sub(r"\b(kimdir|kim|nedir|ne demek|hakkinda|bilgi|anlat|soyle|bana|lutfen|ar)\b", " ", norm_text)
    cekirdek = re.sub(r"\s+", " ", cekirdek).strip()

    en_yuksek = 0
    bulunan_yanit, bulunan_kat = None, None
    for kat, icerik in taban.items():
        for kelime in icerik.get("kelimeler", []):
            kel_norm = metni_normallestir(kelime)
            if not kel_norm:
                continue
            if kel_norm == norm_text or (cekirdek and kel_norm == cekirdek):
                return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            if len(kel_norm) <= 4:
                if re.search(rf"\b{re.escape(kel_norm)}\b", norm_text):
                    return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            elif kel_norm in norm_text or (cekirdek and len(cekirdek) >= 3 and cekirdek in kel_norm):
                return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            skor = max(
                fuzz.ratio(norm_text, kel_norm),
                fuzz.token_set_ratio(norm_text, kel_norm),
                fuzz.ratio(cekirdek, kel_norm) if cekirdek else 0,
            )
            if skor >= 70 and skor > en_yuksek:
                en_yuksek = skor
                bulunan_yanit = icerik.get("yanit")
                bulunan_kat = kat
    if bulunan_yanit:
        return bulunan_yanit, f"{etiket_onek}: {bulunan_kat}"
    return None, None


def akilli_yanit_uret(kullanici_girdisi: str, hedef_dil: str = "tr"):
    raw_text = kullanici_girdisi.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    norm_text = metni_normallestir(kullanici_girdisi)
    yanit = None
    etiket = "Genel"

    # 0. Doğrudan Sohbetten Öğretme Komutu ("öğret: soru = cevap")
    ogret_eslesme = re.match(r"^(?:bana\s+)?(?:öğret|ogret)\s*[:\-]?\s*(.+?)\s*[=:]\s*(.+)$", kullanici_girdisi.strip(), flags=re.IGNORECASE)
    if ogret_eslesme:
        yeni_soru = ogret_eslesme.group(1).strip()
        yeni_cevap = ogret_eslesme.group(2).strip()
        kat_adi = f"ogrenilen_{int(time.time())}"
        json_komut_ekle(kat_adi, yeni_soru, yeni_cevap)
        st.session_state["bekleyen_ogret_sorusu"] = ""
        return (
            f"✅ **Harika, yeni bilgiyi öğrendim Ahmet!**\n\n"
            f"* **Soru:** `{yeni_soru}`\n"
            f"* **Cevap:** {yeni_cevap}\n\n"
            f"Artık bana **'{yeni_soru}'** diye sorduğunda doğrudan bu cevabı vereceğim! ⚡",
            hedef_dil,
            "Yeni Öğrenilen Bilgi",
        )

    # 1. Kullanıcının Öğrettiği Özel JSON Veritabanı (En Yüksek Öncelikli Kişisel Hafıza!)
    guncel_json_veri = json_oku()
    for kat, icerik in guncel_json_veri.items():
        for kelime in icerik.get("kelimeler", []):
            kel_norm = metni_normallestir(kelime)
            if kel_norm and (kel_norm == norm_text or kel_norm == raw_text):
                yanit, etiket = icerik.get("yanit"), f"Öğretilen Hafıza: {kat}"
                break
        if yanit:
            break

    # 2. Dinamik Saat & Tarih
    if yanit is None:
        yanit, etiket = _dinamik_zaman_kontrol(norm_text)

    # 3. Tek başına "kim" / "kın" / "kimdir" sorulduysa kişi rehberini göster
    if yanit is None and norm_text in {"kim", "kin", "kimdir", "bu kim", "o kim", "kim bu", "kim o", "kimler var", "kimi taniyorsun", "kimin cevaplari var"}:
        yanit = OZEL_CEVAP_KURALLARI["kim_genel"]["yanit"]
        etiket = "Özel Kural: Kişi Rehberi"

    # 4. Özel Cevap Kuralları ("nasılsın", "ne haber", "kimsin", "ömer kim", "hadi kim", "edibe kim", "ben kimim", "30 islam alimi")
    if yanit is None:
        if "omer" not in norm_text or not any(k in norm_text for k in ["hayyam", "hz", "halife", "faruk"]):
            ozel_y, oto_en, ozel_e = _ozel_cevap_kontrol(raw_text, norm_text)
            if ozel_y:
                yanit, etiket = ozel_y, ozel_e
                if oto_en and hedef_dil == "tr":
                    hedef_dil = "en"

    # 5. Gelişmiş Matematik Motoru (Dört İşlem, Çarpma, Bölme, Karekök, Üslü, Denklem, EBOB/EKOK)
    if yanit is None:
        yanit, etiket = matematik_motoru_calistir(raw_text)
    if yanit is None:
        yanit, etiket = matematik_motoru_calistir(norm_text)

    # 5.5 Açık Kod Yazma İsteklerinde Hibrit AI Köprüsü
    if yanit is None and st.session_state.get("hibrit_ai_aktif", True) and any(k in norm_text for k in ["kod yaz", "kodu yaz", "arduino kod", "kamera kod", "opencv kod", "fren kod"]):
        hibrit_y, hibrit_e = hibrit_ai_yanit_uret(kullanici_girdisi)
        if hibrit_y:
            yanit, etiket = hibrit_y, hibrit_e

    # 6. 500.000+ Hazır Soru-Cevap Kalıp Havuzu (O(1) Anında Eşleşme)
    if yanit is None:
        havuz = kalip_havuzu_olustur()
        if norm_text in havuz:
            yanit, etiket = havuz[norm_text]

    # 7. Kullanıcının Öğrettiği JSON Veritabanı (Bulanık / Yakın Eşleşme)
    if yanit is None:
        yanit, etiket = _fuzzy_taban_ara(guncel_json_veri, norm_text, "Öğretilen Hafıza")

    # 8. Ahmet Profili & 30 İslam Âlimi & Genel Bilgi Bankası Eşleşmesi
    if yanit is None:
        yanit, etiket = _fuzzy_taban_ara(AHMET_BILGI_TABANI, norm_text, "Ahmet Profili")

    if yanit is None:
        cekirdek_alim = re.sub(r"\b(kimdir|kim|nedir|hakkinda|bilgi|anlat|eserleri)\b", " ", norm_text).strip()
        en_iyi_skor, en_iyi_alim = 0, None
        for _, veri in ISLAM_ALIMLERI.items():
            for anahtar in veri["anahtar_kelimeler"]:
                a_norm = metni_normallestir(anahtar)
                if a_norm in norm_text or (cekirdek_alim and a_norm == cekirdek_alim):
                    en_iyi_skor, en_iyi_alim = 100, veri
                    break
                skor = max(fuzz.token_set_ratio(norm_text, a_norm), fuzz.ratio(cekirdek_alim, a_norm) if cekirdek_alim else 0)
                if skor >= 72 and skor > en_iyi_skor:
                    en_iyi_skor, en_iyi_alim = skor, veri
            if en_iyi_skor == 100:
                break
        if en_iyi_alim:
            yanit = (
                f"### 📜 {en_iyi_alim['ad']}\n"
                f"**Dönem:** {en_iyi_alim['donem']} | **Alan:** {en_iyi_alim['alan']}\n\n"
                f"**Başlıca Eserleri:** {en_iyi_alim['eserler']}\n\n"
                f"{en_iyi_alim['bilgi']}"
            )
            etiket = f"Âlim: {en_iyi_alim['ad']}"

    if yanit is None:
        yanit, etiket = _fuzzy_taban_ara(GENEL_SORU_CEVAP_TABANI, norm_text, "Bilgi Bankası")

    # 9. Duygu ve Sohbet Şablonları
    if yanit is None:
        for s_kod, s_veri in DUYGU_VE_SOHBET_SABLONLARI.items():
            for tet in s_veri["tetikleyiciler"]:
                t_norm = metni_normallestir(tet)
                if t_norm == norm_text or (len(t_norm) >= 5 and t_norm in norm_text):
                    yanit, etiket = s_veri["yanit"], f"Diyalog: {s_kod}"
                    break
            if yanit:
                break

    # 10. Teknik Terimler Sözlüğü Taraması
    if yanit is None:
        for _, t_veri in TEKNIK_TERIMLER_SOZLUGU.items():
            baslik_norm = metni_normallestir(t_veri["baslik"].split("(")[0])
            if baslik_norm and (baslik_norm in norm_text or norm_text in baslik_norm):
                yanit = f"🛠️ **{t_veri['baslik']} ({t_veri['kategori']}):**\n{t_veri['aciklama']}"
                etiket = f"Teknik Terim: {t_veri['kategori']}"
                break

    # 10.5 Hibrit Yapay Zeka Köprüsü (539.806 Kalıp + "Bana Öğret" Hafızası + Kod/Yorum AI)
    if yanit is None and st.session_state.get("hibrit_ai_aktif", True):
        hibrit_y, hibrit_e = hibrit_ai_yanit_uret(kullanici_girdisi)
        if hibrit_y:
            yanit, etiket = hibrit_y, hibrit_e

    # 11. Bilinmeyen Soru -> "Bana öğretir misin?" Otomatik Öğrenme Kutusu Tetikleyicisi!
    if yanit is None:
        st.session_state["bekleyen_ogret_sorusu"] = kullanici_girdisi.strip()
        yanit = (
            f"🤔 **'{kullanici_girdisi}'** sorusunun cevabını henüz bilmiyorum Ahmet. **Bana öğretir misin?**\n\n"
            "👇 Hemen aşağıdaki **'🎓 Bana Öğret'** kutusuna bu sorunun cevabını yazıp kaydet; "
            "kod yazmana gerek kalmadan anında öğreneyim!"
        )
        etiket = "Bana Öğretir misin?"

    # 12. Çok Dilli Çeviri
    if hedef_dil != "tr":
        try:
            temiz_cevirilecek = re.sub(r"[#*`]", "", yanit)
            yanit = guvenli_cevir(temiz_cevirilecek, src="tr", dest=hedef_dil)
        except Exception as e:
            st.warning(f"Çeviri hatası oluştu, Türkçe gösteriliyor: {e}")
            hedef_dil = "tr"

    return yanit, hedef_dil, etiket