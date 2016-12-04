# Global değerler

# background
S_bg = input("Lab. fon alanının giriniz = ")    # background alani
t_bg = 82599.34                                 # background sayim suresi -saniye-

#standart
stA_U238 = 795

S_st = 56175                                    # standart alanı
t_st = 4077.38                                  # standart sayim suresi -saniye-
m_st = 1000                                    	# standart kütlesi -gram-

S_bgst = 5113                                   # standart lab. background alani
t_bgst = 82599.34                               # standart lab. background sayim suresi -saniye-

#sayim suresi -saniye-
t = 56917.36


st_sayhizi = S_st/t_st                		#standartın sayim hizi
stbg_sayhizi = S_bgst/t_bgst          		#standarta ait bg sayim hizi
payda = st_sayhizi - stbg_sayhizi       	#aktivite denkleminin paydasi


bg_sayhizi = float(S_bg) / t_bg



class Aktivite():

    def __init__(self, ornek_no, kutle, alan):
        self.ornek_no = ornek_no
        self.kutle = kutle
        self.alan = alan
        sayhizi = float(alan)/t
        self.A_nm = stA_U238 * (sayhizi - bg_sayhizi)/payda * m_st/float(kutle)

    def print(self):
        print("---------------------")
        print(self.ornek_no, "numaralı numune değerleri : ")
        print(" kütle:", self.kutle, "g", "---","alan=", self.alan)
        print("aktivite : ", self.A_nm)
        print("---------------------")



print("-------------------------------------------------------------------")
print("global değerler")
print("BG alanı: ", S_bg)
print("-------------------------------------------------------------------")


i = 0

while (i < 100) :
    numune1 = Aktivite(input("Numune No = "), input("Numune kutlesi = "), input("Alan = "))
    numune1.print()

    i += 1
