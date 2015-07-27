#-*-coding:utf-8-*-

import urllib.request
import sqlite3
import string
import re

import os
kontrol = os.path.exists("db.db")
if kontrol == True:

    pass
else:

    basharfler = list(string.ascii_lowercase)
    for i in basharfler:
        ac = urllib.request.urlopen("http://uzmanpara.milliyet.com.tr/canli-borsa/?Harf="+i)
        ac = ac.read()
        p = re.compile('id=\"h_tr_id_([A-Z].+)\" ', re.MULTILINE)
        p = re.findall(p,ac.decode("cp1254"))
        ac = sqlite3.connect("db.db")
        cs = ac.cursor()

        for i in p:

            try:
                cs.execute("CREATE TABLE %s(tarih text,oran text,durum text)" %i)
                ac.commit()

            except sqlite3.OperationalError:
                pass
                print("hata")





