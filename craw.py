#-*-coding:utf-8-*-
import datetime

import sqlite3
import requests
from lxml import html
tarih = datetime.datetime.now().strftime("%Y-%m-%d")
ac = sqlite3.connect("db.db")
cs = ac.cursor()
sorgu = cs.execute("SELECT * FROM sqlite_master where type='table' ")
liste = []
for i in sorgu:

    liste.append(i[1])
cs.close()
ac.close()
for i in liste:
    firmaad = i

    ac = sqlite3.connect("db.db")
    cs = ac.cursor()
    url = requests.get("http://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/%s/" %firmaad)
    source = html.fromstring(url.text)
    #<span class="price-arrow-down">62,20</span>#

    fiyat = source.xpath('/html/body/div[4]/div[9]/div[3]/div[1]/span[1]/text()')

    degisim = source.xpath('/html/body/div[4]/div[9]/div[3]/div[1]/table/tbody/tr[1]/td[2]/span[1]/text()')
    fiyat = ''.join(fiyat)
    degisim = ''.join(degisim)
    firmaad = ''.join(firmaad)
    # print("%s değeri: %s gözlenen değişim : %s"%(firmaad,fiyat,degisim))





    cs.execute("INSERT INTO {} VALUES (?,?,?)".format(firmaad),(tarih,degisim,fiyat))
    ac.commit()
cs.close()
ac.close()
    # ac.commit()
    # url = url.read()
    # print(firmaad)
    #
    # #Regex
    # p = re.compile("<span class=\"price-arrow-[a-z]+\">([0-9].+|[0-9]+[0-9])<\/span>",re.MULTILINE)
    # a = re.findall(p,url.decode("cp1254"))
    # #Yüzde
    # c = re.compile(" (.[0-9]{0,3},[0-9].*)\% ")
    # c = re.findall(c,url.decode("cp1254"))
    #
    # print(c)
    # #Endeks
    # p = re.compile("^([0-9].*)</span>")
    # p = re.findall(p,a[0])
    # print(p)
    # # durum = p[0][0]
    # # oran = p[0][1]
    # sorgu = "INSERT INTO %s VALUES(%s,%s,%s)"%(firmaad,tarih,oran,durum)
    # print(sorgu)


