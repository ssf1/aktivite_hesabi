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

# background degerleri
(t_bg,) = degerler[0:1]
(bgU1_Alan, bgU2_Alan, bgU3_Alan, bgCs_Alan, bgTh_Alan, bgK_Alan) = degerler[1:7]
backgroundlar = (bgU1_Alan, bgU2_Alan, bgU3_Alan, bgCs_Alan, bgTh_Alan, bgK_Alan)   ############################
# standart degerleri
(stAU, stATh, stAK, stASoil) = degerler[7:11]
aktiviteler = (stAU, stAU, stAU, stATh, stAK, stASoil)                              ############################
(m_st,)= degerler[11:12]
(t_st,) = degerler[12:13]
(stU1_Alan, stU2_Alan, stU3_Alan, stCs_Alan, stTh_Alan, stK_Alan) = degerler[13:19]  # standart sayimlari
aktivite_alanlari = (stU1_Alan, stU2_Alan, stU3_Alan, stCs_Alan, stTh_Alan, stK_Alan)   ############################
(t_stbg,) = degerler[19:20]
(stbgU1_Alan, stbgU2_Alan, stbgU3_Alan, stbgCs_Alan, stbgTh_Alan, stbgK_Alan) = degerler[20:26]  # standart lab. bg degerleri
standart_background = (stbgU1_Alan, stbgU2_Alan, stbgU3_Alan, stbgCs_Alan, stbgTh_Alan, stbgK_Alan)     #############

# ------------------------------------------------------------------------------------------------------
# olcum degerlerinin dis dosyadan okutulmasi

def olcum_degerleri():
    Aktiviteler = []
    Numuneler = []
    with open("olcumler.csv", "r") as olcumler:
        reader = csv.DictReader(olcumler)
        for satir in reader:
            numune_aktivite = []
            no = satir['numune']
            m = float(satir['kutle'])
            t = float(satir['sayim suresi'])
            U1 = float(satir['U1'])
            U2 = float(satir['U2'])
            U3 = float(satir['U3'])
            Cs = float(satir['Cs'])
            Th = float(satir['Th'])
            K = float(satir['K'])
            olculer = (U1, U2, U3, Cs, Th, K)
            for i in range(len(olculer)):
                alan = olculer[i]
                alan_bg = backgroundlar[i]
                alan_st = aktivite_alanlari[i]
                alan_stbg = standart_background[i]
                st_A = aktiviteler[i]

                aktivite = st_A*((alan/t)-(alan_bg/t_bg))/((alan_st/t_st)-(alan_stbg/t_stbg))*(m_st/m)
                numune_aktivite.append(aktivite)

            Aktiviteler.append(numune_aktivite)
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
    print("Numune", " "*9, "U1"," "*21, "U2"," "*20, "U3"," "*20, "Cs", " "*20, "Th", " "*20, "K")
    print("-"*6, " ", "-"*20, " "*2, "-"*20, " "*3, "-"*20, " ", "-"*20, " "*2, "-"*20, " "*2, "-"*20)
    for i in range(len(Aktiviteler)):
        print(" ",Numuneler[i]," "*5,
              Aktiviteler[i][0], " " * (22 - len(str(Aktiviteler[i][0]))),
              Aktiviteler[i][1], " " * (22 - len(str(Aktiviteler[i][1]))),
              Aktiviteler[i][2], " " * (22 - len(str(Aktiviteler[i][2]))),
              Aktiviteler[i][3], " " * (22 - len(str(Aktiviteler[i][3]))),
              Aktiviteler[i][4], " " * (22 - len(str(Aktiviteler[i][4]))),
              Aktiviteler[i][5], " " * (22 - len(str(Aktiviteler[i][5]))),
              )


olcum_degerleri()

