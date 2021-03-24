lista = []
filnamn = "lagring.txt"



def summa():

    summa = 0
    for t in lista:
        summa += t
    return summa





def största():


    största = lista[0]
    for t in lista:
        if t > största:
            största = t
    return största



def minsta():

    minsta = lista[0]
    for t in lista:
        if t < minsta:
            minsta = t
    
    return minsta