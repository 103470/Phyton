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

def feltolt(v,n,n_max): 

    for i in range(0,n):

        v.append(rd.randint(1, n_max))

    return v

    
"""print("Adja meg mit keres:")"""
T=15
v=[]
feltolt(v,50,100)
n=len(v)
eredmenyLinker=linearisKereses(v,50,T)
eredmeny=strazsasKereses(v,T)
print(v)
print(eredmeny)
print(eredmenyLinker)
