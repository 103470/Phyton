import random as rd
import timeit
import math

def binarisKereses(v, T):

    e = 0

    u = len(v) - 1

    k = 0

    while e <= u:

        k = (u + e) // 2

        if v[k] < T:

            e = k + 1

        elif v[k] > T:

            u = k - 1

        else:

            return k

    return False


def ugraloKereses(v, n, T ):

    lepesKoz = math.sqrt(n)

    elozo = 0

    while v[int(min(lepesKoz, n)-1)] < T:

        elozo = lepesKoz

        lepesKoz += math.sqrt(n)

        if elozo >= n:

            return -1

    while v[int(elozo)] < T:

        elozo += 1

        if elozo == min(lepesKoz, n):

            return -1

    if v[int(elozo)] == T:

        return int(elozo)

    return False



def feltolt(v, n, n_max):
    for i in range(0, n):
        v.append(rd.randint(1, n_max))

    return v

def beszuroRendezes(sorozat):

    for i in range(1, len(sorozat)):

        kulcs = sorozat[i]

        j = i-1

        while j >= 0 and kulcs < sorozat[j] :

                sorozat[j + 1] = sorozat[j]

                j -= 1

        sorozat[j + 1] = kulcs

    return sorozat




v=[]
feltolt(v, 30000, 10000000)
n=len(v)
beszuroRendezes(v)
T=rd.randint(1,10000000)
start = timeit.default_timer()
eredmenyBinaris = binarisKereses(v, T)
stop = timeit.default_timer()
print("Bináris idő: " + str(stop - start))
print()
start2 = timeit.default_timer()
eredmenyUgro = ugraloKereses(v, n, T)
stop2 = timeit.default_timer()
print("Ugro idő: " + str(stop2 - start2))

atlag = (3.380000000419159e-05+9.520000000406981e-05+3.759999999886077e-05+8.110000000272066e-05+7.529999999889014e-05)/5

print(atlag)
print(eredmenyBinaris)
print(eredmenyUgro)

