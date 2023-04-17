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


v = []
feltolt(v, 1000, 20000000)
n = len(v)
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


atlag = (0.07968400000000031+0.31138509999999897+0.07898409999999956+0.08577430000000064+0.33931809999999984)/5

print(atlag)
