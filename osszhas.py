import random as rd
import timeit



def buborekRendezes(v, l):
    n = len(v)

    for i in range(n):

        for j in range(0, n - i - 1):

            l += 1

            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

    return l


def buborekRendezesJav1(v, l):
    n = len(v)

    for i in range(n):

        voltECsere = False

        for j in range(0, n - i - 1):

            l += 1

            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

                voltECsere = True

        if voltECsere == False:
            break

    return l


def buborekRendezesJav2(v, l):
    utolsoCsereHelye = 0

    n = len(v)

    i = 1

    while i < n:

        for j in range(0, n - i):

            l += 1

            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

                utolsoCsereHelye = j

            if utolsoCsereHelye == n - i:
                utolsoCsereHelye = j

        i = n - utolsoCsereHelye

    return l


def koktelRendezes(v):
    n = len(v)

    volteCsere = True

    elso = 0

    utolso = n - 1

    while (volteCsere == True):

        volteCsere = False

        for i in range(elso, utolso):

            if (v[i] > v[i + 1]):
                v[i], v[i + 1] = v[i + 1], v[i]

                volteCsere = True

        if (volteCsere == False):
            break

        volteCsere = False

        utolso -= 1

        for i in range(utolso, elso, -1):

            if (v[i] > v[i + 1]):
                v[i], v[i + 1] = v[i + 1], v[i]

                volteCsere = True

        elso += 1

    return "Koktél lépészám: " + str(l)


def kovetkezoRes(res):
    res = (res * 10) / 13

    if res < 1:
        return 1

    return int(res)


def fesusRendezes(v):
    n = len(v)

    res = n

    volteCsere = True

    while res != 1 or volteCsere == True:

        res = kovetkezoRes(res)

        volteCsere = False

        for i in range(0, n - res):

            if v[i] > v[i + res]:
                v[i], v[i + res] = v[i + res], v[i]

                volteCsere = True

    return

def beszuroRendezes(v):

    for i in range(1, len(v)):

        kulcs = v[i]

        j = i-1

        while j >= 0 and kulcs < v[j]:

                v[j + 1] = v[j]

                j -= 1

        v[j + 1] = kulcs

    return v


def particionalas(v, also, felso):
    i = (also - 1)

    pivot = v[felso]

    for j in range(also, felso):

        if v[j] < pivot:
            i = i + 1

            v[i], v[j] = v[j], v[i]

    v[i + 1], v[felso] = v[felso], v[i + 1]

    return (i + 1)


def gyorsRendezes(v, also, felso):
    if also < felso:
        pi = particionalas(v, also, felso)

        gyorsRendezes(v, also, pi - 1)

        gyorsRendezes(v, pi + 1, felso)

    return "A rendezett sorozat: " + str(v)


b=[]
bl=[]
b1=[]
b1l=[]
b2=[]
b2l=[]
besz=[]
gy=[]
k=[]
f=[]
ve=70
def feltolt(v, n, n_max):
    for i in range(0, n):
        v.append(rd.randint(1, n_max))

    return v


for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start = timeit.default_timer()
        eredmenyBuborek = buborekRendezes(v, l)
        stop = timeit.default_timer()
        ##print("Buborék: " + str(stop - start))
        b.append(stop - start)
        bl.append(eredmenyBuborek)
        print()


for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start2 = timeit.default_timer()
        eredmenyBuborekJav1 = buborekRendezesJav1(v, l)
        stop2 = timeit.default_timer()
        ##print("BuborékJav1: " + str(stop2 - start2))
        b1.append(stop2 - start2)
        b1l.append(eredmenyBuborekJav1)
        print()

for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start3 = timeit.default_timer()
        eredmenyBuborekJav2 = buborekRendezesJav2(v, l)
        stop3 = timeit.default_timer()
        ##print("BuborékJav2: " + str(stop3 - start3))
        b2.append(stop3 - start3)
        b2l.append(eredmenyBuborekJav2)
        print()

for i in range(0, 5):
    v = []
    l = 0
    feltolt(v, ve, 100000)
    start4 = timeit.default_timer()
    eredmenyKoktel = koktelRendezes(v)
    stop4 = timeit.default_timer()
    ##print("Koktélrendezés: " + str(stop4 - start4))
    k.append(stop4 - start4)
    print()

for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start5 = timeit.default_timer()
        eredmenyFesus = fesusRendezes(v)
        stop5 = timeit.default_timer()
        ##print("Fésűsrendezés: " + str(stop5 - start5))
        f.append(stop5 - start5)
        print()

for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start6 = timeit.default_timer()
        eredmenyBeszuro = beszuroRendezes(v)
        stop6 = timeit.default_timer()
        ##print("Buborék: " + str(stop - start))
        besz.append(stop6 - start6)
        print()

for i in range(0,5):
        v = []
        l = 0
        feltolt(v, ve, 100000)
        start7 = timeit.default_timer()
        eredmenyGyors = gyorsRendezes(v,0,len(v)-1)
        stop7 = timeit.default_timer()
        ##print("Buborék: " + str(stop - start))
        gy.append(stop7 - start7)
        print()

x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [0.0001999999999497959]

print(b)
print(bl)
print(b1)
print(b1l)
print(b2)
print(b2l)
print(k)
print(f)

bosszeg = 0
blosszeg = 0
b1osszeg = 0
b1losszeg = 0
b2osszeg = 0
b2losszeg = 0
kosszeg = 0
fosszeg= 0
beszosszeg = 0
gyosszeg = 0

for szam in b:
    bosszeg += szam
print("Buborék átlag: "+ str(bosszeg / 5))

for szam in b1:
    b1osszeg += szam
print("Buborék Jav1 átlag: "+ str(b1osszeg / 5))

for szam in b2:
    b2osszeg += szam

print("Buborék Jav2 átlag: "+ str(b2osszeg / 5))

for szam in k:
    kosszeg += szam
print("Koktél átlag: " + str(kosszeg / 5))

for szam in f:
    fosszeg += szam
print("Fésűs átlag: " +str(fosszeg / 5))

for szam in bl:
    blosszeg += szam
print("Buborék átlag: "+ str(blosszeg / 5))

for szam in b1l:
    b1losszeg += szam
print("Buborék átlag: "+ str(b1losszeg / 5))

for szam in b2l:
    b2losszeg += szam
print("Buborék átlag: "+ str(b2losszeg / 5))

for szam in besz:
    beszosszeg += szam
print("Beszúró átlag: "+ str(beszosszeg / 5))

for szam in gy:
    gyosszeg += szam
print("Gyors átlag: "+ str(gyosszeg / 5))



