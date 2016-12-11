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

(t_bg, bgU1_Alan, bgU2_Alan, bgU3_Alan, bgCs_Alan, bgTh_Alan, bgK_Alan) = degerler[:7]  # background degerleri
(stAU, stATh, stAK, stASoil, m_st) = degerler[7:12]  # standart degerleri
(t_st, stU1_Alan, stU2_Alan, stU3_Alan, stCs_Alan, stTh_Alan, stK_Alan) = degerler[12:19]  # standart sayimlari
(t_stbg, stbgU1_Alan, stbgU2_Alan, stbgU3_Alan, stbgCs_Alan, stbgTh_Alan, stbgK_Alan) = degerler[
                                                                                        19:26]  # standart lab. bg degerleri


def olcum_degerleri():
    with open("olcumler.csv", "r") as olcumler:
        reader = csv.DictReader(olcumler)
        for satir in reader:
            no = satir['numune']
            m = float(satir['kütle'])
            t = float(satir['sayım süresi'])
            U1 = float(satir['U1'])
            U2 = float(satir['U2'])
            U3 = float(satir['U3'])
            Cs = float(satir['Cs'])
            Th = float(satir['Th'])
            K = float(satir['K'])
            semboller = (U1, U2, U3, Cs, Th, K)
            print(no, "", m, "", t)
            for i in semboller:
                print(i * 2)

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