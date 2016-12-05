sabitler = ['S_bg', 't_bg', 'stA_U238', 'S_st', 't_st', 'm_st', 'S_stbg', 't_stbg', 't']

degerler = []

with open("sabit_degerler.txt","r") as sabit_degerler:
    for satir in sabit_degerler.readlines():
        deger, yorum = satir.split("\t",1)
        sayi_deger = float(deger)
        degerler.append(sayi_deger)


if len(sabitler)== len(degerler):
    for i in range(len(sabitler)):
        for j in range(len(sabitler)):
            if i == j:
                sabitler[j] == degerler[j]

print(sabitler, len(sabitler))
print(degerler, len(degerler))
print(S_bg)



"""
st_sayhizi = S_st/t_st                		#standartın sayim hizi
stbg_sayhizi = S_stbg/t_stbg          		#standarta ait bg sayim hizi
payda = st_sayhizi - stbg_sayhizi       	#aktivite denkleminin paydasi

bg_sayhizi = float(S_bg) / t_bg


class Aktivite():

    def __init__(self, ornek_no, kutle, alan):
        self.ornek_no = ornek_no
        self.kutle = kutle
        self.alan = alan
        self.sayhizi = float(alan)/t
        self.A_nm = stA_U238 * (self.sayhizi - bg_sayhizi)/payda * m_st/float(kutle)

    def print(self):
        print("---------------------")
        print(self.ornek_no, "numaralı numune değerleri : ")
        print("kütle:", self.kutle, "g", "---","alan=", self.alan)
        print("sayım hızı:", self.sayhizi)
        print("aktivite : ", self.A_nm)
        print("---------------------")


print("-------------------------------------------------------------------")
print("global değerler")
print("BG alanı: ", S_bg, "--", "sayım süresi", t_bg, "--","BG Sayım hızı : ", bg_sayhizi)
print("Standart aktivitesi:", stA_U238, "--", "alani:", S_st, "--", "sayım suresi", t_st, "--","kutlesi:",m_st)
print("Standartın sayım hızı:", st_sayhizi)
print("Standart BG alanı: ", S_stbg, "--","sayım süresi:", t_stbg)
print("Standarta ait BG sayım hızı: ", stbg_sayhizi,"--","St. sayım hızı farkı", payda)
print("-------------------------------------------------------------------")


i = 0
while (i < 100) :
    numune = Aktivite(input("Numune No = "), input("Numune kutlesi = "), input("Alan = "))
    numune.print()

    i += 1
"""