import random as rd
import timeit

start=timeit.default_timer()
def linearisKereses(v, n, T): 

    i = 0

    while i < n and v[i]!=T:

        i+=1

    if i < n:

        return  True

    else:

        return False

stop=timeit.default_timer()

print("Linker futásidő: " + str(stop-start))

start=timeit.default_timer()

def strazsasKereses(v, T):

    i = 0

    while v[i]!=T:

        i+=1

        

    if i < len(v)-1:

        return True

    else:

        return False


stop=timeit.default_timer()

    
print("StrázsásKer futásidő: " + str(stop-start))


def beszuroRendezes(sorozat): 

    for i in range(1, len(sorozat)): 

        kulcs = sorozat[i] 

        j = i-1

        while j >= 0 and kulcs < sorozat[j] : 

                sorozat[j + 1] = sorozat[j] 

                j -= 1

        sorozat[j + 1] = kulcs 

    return sorozat

def feltolt(v,n,n_max): 

    for i in range(0,n):

        v.append(rd.randint(1, n_max))

    return v

T=15
v=[]
n=len(v)
feltolt(v,50,100)
beszuroRendezes(v)
eredmenyLinker=linearisKereses(v,50,T)
eredmeny=strazsasKereses(v,T)
print(v)
print(eredmeny)
print(eredmenyLinker)



print("A v sorozat:\n " + str(v))



print("A rendezett sorozat:")

for i in range(len(v)): 

    print ("% d" % v[i], end='')