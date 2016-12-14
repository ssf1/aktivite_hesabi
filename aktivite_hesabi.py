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


def olcum_degerleri():
    Aktiviteler = []
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

    for i in range(len(Aktiviteler)):
        print(Aktiviteler[i][0])



olcum_degerleri()

"""

# ------------------------------------------------------------------------------------------------------
# sayim hizlari vs hesaplanmasi

st_sayhizi = st_Alan------/t_st----                		#standartın sayim hizi
stbg_sayhizi = stbg_Alan-----/t_stbg----          		#standarta ait bg sayim hizi
payda = st_sayhizi - stbg_sayhizi       	#aktivite denkleminin paydasi

bg_sayhizi = float(bg_Alan------) / t_bg

class Aktivite():

    def __init__(self, ornek_no, kutle, alan):
        self.ornek_no = ornek_no
        self.kutle = kutle
        self.alan = alan
        self.sayhizi = float(alan)/t
        self.A_nm = stA * (self.sayhizi - bg_sayhizi)/payda * m_st/float(kutle)

    def print(self):
        print("-" * 20)
        print(self.ornek_no, "numaralı numune değerleri : ")
        print("kütle:", self.kutle, "g", "---","alan=", self.alan)
        print("sayım hızı:", self.sayhizi)
        print("aktivite : ", self.A_nm)
        print("-" * 20)

print("-" * 40)
print("----- global değerler -----")
print("BG alanı: ", bg_Alan, "--", "BG sayım süresi", t_bg, "--","BG Sayım hızı : ", bg_sayhizi)
print("Standart aktivitesi:", stA, "--", " St alani:", st_Alan, "--", "St sayım suresi", t_st, "--"," St kutlesi:",m_st)
print("Standartın sayım hızı:", st_sayhizi)
print("Standart BG alanı: ", stbg_Alan, "--","St BG sayım süresi:", t_stbg)
print("Standarta ait BG sayım hızı: ", stbg_sayhizi,"--","St sayım hızı farkı", payda)
print("-" * 40)

# ------------------------------------------------------------------------------------------------------
# numune giris dongusu

i = 0
while (i < 100) :
    numune = Aktivite(input("Numune No = "), input("Numune kutlesi = "), input("Alan = "))
    numune.print()

    i += 1
# ------------------------------------------------------------------------------------------------------

"""