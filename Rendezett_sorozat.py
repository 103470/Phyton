import random as rd
import timeit


def linearisKereses(v, n, T):
    i = 0

    while i < n and v[i] != T:
        i += 1

    if i < n:

        return True

    else:

        return False


def strazsasKereses(v, T):
    i = 0
    v.append(T)

    while v[i] != T:
        i += 1

    if i < len(v) - 1:

        return True

    else:

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


v = []
feltolt(v, 30000, 10000000)
n = len(v)
beszuroRendezes(v)
T = rd.randint(1, 10000000)
start = timeit.default_timer()
eredmenyLinKer = linearisKereses(v, n, T)
stop = timeit.default_timer()
print("Lineáris idő: " + str(stop - start))
start2 = timeit.default_timer()
eredmenyStrazsas = strazsasKereses(v, T)
stop2 = timeit.default_timer()
print("Strazsas idő: " + str(stop2 - start2))
print(T)
print(eredmenyStrazsas)
print(eredmenyLinKer)


atlag = (0.0013038999999999135+0.0012553000000004033+0.0012641000000002123+0.0012638000000002592+0.0011356999999989625)/5

print(atlag)
