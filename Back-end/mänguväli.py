from random import sample
from re import M
"""
def print_dict(m,laius):
    print("\n".join([" ".join([str(m[j]) for j in range(i,i+laius)]) for i in range(0,len(m),laius)]))

def printm(m):
    print("\n".join([" ".join([str(j) for j in i]) for i in m]))
"""
def genereeri_mänguväli(laius,kõrgus,miinide_arv,täidis = 0):
    while True:
        miinid = sample(range(laius*kõrgus),miinide_arv)
        if len(miinid) == len(set(miinid)):
            break
    miiniväli = [[täidis for i in range(laius)] for j in range(kõrgus)]
    for m in miinid:
        x = m//laius
        y = m%laius
        miiniväli[x][y] = "9"
        for i in range(max(x-1,0),x+2):
            for j in range(max(y-1,0),y+2):
                try:
                    miiniväli[i][j] +=1

                except:
                    continue
    #printm(miiniväli)
    return miiniväli #{i+j*laius:miiniväli[i][j] for j in range(laius) for i in range(kõrgus)}


def avalda(x ,y ,hetkeseis, miiniväli):
    if miiniväli[x][y] == "9":
        return miiniväli
    elif miiniväli[x][y] != 0:
        hetkeseis[x][y] = miiniväli[x][y]
        return hetkeseis
    elif miiniväli[x][y] == 0:
        for i in range(max(x-1,0),x+2):
            for j in range(max(y-1,0),y+2):
                try:
                    if hetkeseis[i][j] == "a":
                        hetkeseis[i][j] = miiniväli[i][j]
                        hetkeseis = avalda(i,j,hetkeseis,miiniväli)
                except:
                    continue
        return hetkeseis
"""
kaart = genereeri_mänguväli(8,8,10)
miiniväli = genereeri_mänguväli(8,8,0,"□")
koordinaat = input().split(" ")
printm(avalda(int(koordinaat[0]),int(koordinaat[1]),miiniväli,kaart))
"""