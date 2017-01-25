import csv
# ------------------------------------------------------------------------------------------------------
# global degerlerin disaridan alinip degiskenlere atanmasi

semboller = []
degerler = []

with open("sabit_degerler", "r") as sabit_degerler:  # sabitlerin oldugu txt dosyasini actik
    for satir in sabit_degerler.readlines():  # satirlari okuttuk
        semboldeger, atik = satir.split("\t", 1)  # satirlardaki sembol = deger iceren kismi ayirdik
        sembol, deger = semboldeger.split(' = ')  # sembol ve deger kismimi bolduk
        sembol = str(sembol)  # sembolleri string yaptik
        deger = float(deger)  # sayilari float yaptik
        semboller.append(sembol)  # sembol ve degerleri sirayla yeni listeye ekledik
        degerler.append(deger)

########################################################
# background degerleri

(t_bg,) = degerler[0:1]

(bgU1_Alan, bgU2_Alan, bgU3_Alan, bgCs_Alan, bgTh_Alan, bgK_Alan) = degerler[1:7]
backgroundlar = (bgU1_Alan, bgU2_Alan, bgU3_Alan, bgCs_Alan, bgTh_Alan, bgK_Alan)

(err_bgU1_Alan, err_bgU2_Alan, err_bgU3_Alan, err_bgCs_Alan, err_bgTh_Alan, err_bgK_Alan) = degerler[7:13]
err_backgroundlar = (err_bgU1_Alan, err_bgU2_Alan, err_bgU3_Alan, err_bgCs_Alan, err_bgTh_Alan, err_bgK_Alan)

########################################################
# standart degerleri

(stAU, stATh, stAK, stASoil) = degerler[13:17]
aktiviteler = (stAU, stAU, stAU, stATh, stAK, stASoil)

(err_stAU, err_stATh, err_stAK, err_stASoil) = degerler[17:21]
err_aktiviteler = (err_stAU,err_stAU, err_stAU, err_stATh, err_stAK, err_stASoil)

(m_st,)= degerler[21:22]
(t_stU, t_stTh, t_stK, t_stSoil) = degerler[22:26]
t_standartlar = (t_stU, t_stU, t_stU, t_stTh, t_stK, t_stSoil)


# standart sayimlari
(stU1_Alan, stU2_Alan, stU3_Alan, stCs_Alan, stTh_Alan, stK_Alan) = degerler[26:32]
aktivite_alanlari = (stU1_Alan, stU2_Alan, stU3_Alan, stCs_Alan, stTh_Alan, stK_Alan)

(err_stU1_Alan, err_stU2_Alan, err_stU3_Alan, err_stCs_Alan, err_stTh_Alan, err_stK_Alan) = degerler[32:38]
err_aktivite_alanlari = (err_stU1_Alan, err_stU2_Alan, err_stU3_Alan, err_stCs_Alan, err_stTh_Alan, err_stK_Alan)

(t_stbg,) = degerler[38:39]

# standart lab. bg degerleri
(stbgU1_Alan, stbgU2_Alan, stbgU3_Alan, stbgCs_Alan, stbgTh_Alan, stbgK_Alan) = degerler[39:45]
standart_background = (stbgU1_Alan, stbgU2_Alan, stbgU3_Alan, stbgCs_Alan, stbgTh_Alan, stbgK_Alan)

(err_stbgU1_Alan, err_stbgU2_Alan, err_stbgU3_Alan, err_stbgCs_Alan, err_stbgTh_Alan, err_stbgK_Alan) = degerler[45:51]
err_standart_background = (err_stbgU1_Alan, err_stbgU2_Alan, err_stbgU3_Alan, err_stbgCs_Alan, err_stbgTh_Alan, err_stbgK_Alan)

# ------------------------------------------------------------------------------------------------------
# olcum degerlerinin dis dosyadan okutulmasi

def olcum_degerleri():
    Aktiviteler = []
    err_Aktiviteler = []
    Numuneler = []
    with open("olcumler.csv", "r") as olcumler:
        reader = csv.DictReader(olcumler)
        for satir in reader:
            numune_aktivite = []
            err_numune_aktivite = []
            no = satir['numune']
            m = float(satir['kutle'])
            t = float(satir['sayim suresi'])
            U1 = float(satir['U1'])
            U2 = float(satir['U2'])
            U3 = float(satir['U3'])
            Cs = float(satir['Cs'])
            Th = float(satir['Th'])
            K = float(satir['K'])
            err_U1 = float(satir['U1 hata'])
            err_U2 = float(satir['U2 hata'])
            err_U3 = float(satir['U3 hata'])
            err_Cs = float(satir['Cs hata'])
            err_Th = float(satir['Th hata'])
            err_K = float(satir['K hata'])
            olculer = (U1, U2, U3, Cs, Th, K)
            hatalar = (err_U1, err_U2, err_U3, err_Cs, err_Th, err_K)
            for i in range(len(olculer)):
                alan = olculer[i]
                hata = hatalar[i]
                alan_bg = backgroundlar[i]
                err_alan_bg = err_backgroundlar[i]
                alan_st = aktivite_alanlari[i]
                err_alan_st = err_aktivite_alanlari[i]
                alan_stbg = standart_background[i]
                err_alan_stbg = err_standart_background[i]
                st_A = aktiviteler[i]
                err_st_A = err_aktiviteler[i]
                t_st = t_standartlar [i]

                aktivite = st_A*((alan/t)-(alan_bg/t_bg))/((alan_st/t_st)-(alan_stbg/t_stbg))*(m_st/m)
                err_aktivite = ((err_st_A/100)**2+(((hata/t)**2+(err_alan_bg/t_bg)**2)/(alan/t-alan_bg/t_bg)**2)+(((err_alan_st/t_st)**2+(err_alan_stbg/t_stbg)**2)/(alan_st/t_st-alan_stbg/t_stbg)**2))**(1/2)*aktivite
                numune_aktivite.append(aktivite)
                err_numune_aktivite.append(err_aktivite)

            Aktiviteler.append(numune_aktivite)
            err_Aktiviteler.append(err_numune_aktivite)
            Numuneler.append(no)

# ------------------------------------------------------------------------------------------------------
# sonuclar.txt dosyasına yazdıran kisim
    with open("sonuclar.txt", "w") as sonuclar:
        print("Numune", " "*9, "U1"," "*21, "U2"," "*20, "U3"," "*20, "Cs", " "*20, "Th", " "*20, "K", file=sonuclar, end="\n")
        print("-"*6, " ", "-"*20, " "*2, "-"*20, " "*3, "-"*20, " ", "-"*20, " "*2, "-"*20, " "*2, "-"*20,  file=sonuclar, end="\n")
        for i in range(len(Aktiviteler)):
            print(" ",Numuneler[i]," "*5,
                  Aktiviteler[i][0]," "*(22-len(str(Aktiviteler[i][0]))),
                  Aktiviteler[i][1]," "*(22-len(str(Aktiviteler[i][1]))),
                  Aktiviteler[i][2], " " * (22 - len(str(Aktiviteler[i][2]))),
                  Aktiviteler[i][3], " " * (22 - len(str(Aktiviteler[i][3]))),
                  Aktiviteler[i][4], " " * (22 - len(str(Aktiviteler[i][4]))),
                  Aktiviteler[i][5], " " * (22 - len(str(Aktiviteler[i][5]))),
                  file=sonuclar, end="\n"
                  )
# ------------------------------------------------------------------------------------------------------
# sonuclar.csv dosyasına yazdıran kisim
    with open("sonuclar.csv", "w") as sonuclar:
        print("Numune",",", "U1", ",","U2", ",","U3", ",","Cs", ",","Th", ",","K", file=sonuclar, end="\n")
        for i in range(len(Aktiviteler)):
            print(Numuneler[i],",",
                  Aktiviteler[i][0],",",
                  Aktiviteler[i][1],",",
                  Aktiviteler[i][2],",",
                  Aktiviteler[i][3],",",
                  Aktiviteler[i][4],",",
                  Aktiviteler[i][5],
                  file=sonuclar, end="\n"
                  )
# ------------------------------------------------------------------------------------------------------
# sonuclari ekrana yazdıran kisim
    isim = "Numune", "U1", "U1 hata", "U2", "U2 hata", "U3", "U3 hata", "Cs", "Cs hata", "Th", "Th hata", "K", "K hata"
    print()
    print("|{:^8}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}| |{:^10}|  ".format(isim[0], isim[1], isim[2], isim[0], isim[1], isim[2], isim[0], isim[1], isim[2], isim[0], isim[1], isim[2], isim[2]))

    #    print("Numune", " "*9, "U1"," "*21, "U1 hata"," "*21, "U2"," "*20, "U2 hata"," "*21, "U3"," "*20, "U3 hata"," "*20, "Cs", " "*20, "Cs hata"," "*20, "Th", " "*20, "Th hata", " "*20, "K", " "*20, "K hata",)
    print("-"*6, " ", "-"*20, " "*2, "-"*20, " "*3, "-"*20, " ", "-"*20, " "*2, "-"*20, " "*2, "-"*20)
    for i in range(len(Aktiviteler)):
        print(" ",Numuneler[i]," "*5,
              Aktiviteler[i][0], " " * (22 - len(str(Aktiviteler[i][0]))),
              err_Aktiviteler[i][0], " " * (22 - len(str(err_Aktiviteler[i][0]))),
              Aktiviteler[i][1], " " * (22 - len(str(Aktiviteler[i][1]))),
              err_Aktiviteler[i][1], " " * (22 - len(str(err_Aktiviteler[i][1]))),
              Aktiviteler[i][2], " " * (22 - len(str(Aktiviteler[i][2]))),
              err_Aktiviteler[i][2], " " * (22 - len(str(err_Aktiviteler[i][2]))),
              Aktiviteler[i][3], " " * (22 - len(str(Aktiviteler[i][3]))),
              err_Aktiviteler[i][3], " " * (22 - len(str(err_Aktiviteler[i][3]))),
              Aktiviteler[i][4], " " * (22 - len(str(Aktiviteler[i][4]))),
              err_Aktiviteler[i][4], " " * (22 - len(str(err_Aktiviteler[i][4]))),
              Aktiviteler[i][5], " " * (22 - len(str(Aktiviteler[i][5]))),
              err_Aktiviteler[i][5], " " * (22 - len(str(err_Aktiviteler[i][5]))),
              )


olcum_degerleri()

