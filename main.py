import time
import random
import os


def generator_de_nr_pt_teste():
    teste = []
    with open('input.txt', "r") as f:
        nr_teste = int(f.readline())
        for line in f:
            teste.append([int(x) for x in line.strip().split()])

    # in matricea teste, teste[index][0] e nr de numere, iar teste[index][1] e val. maxima
    index = 1
    while index <= nr_teste:
        fisier = "test" + str(index) + ".txt"
        lista_random = []
        for i in range(0, teste[index - 1][0]):
            lista_random.append(random.randint(1, teste[index - 1][1]))

        with open(fisier, "w") as g:
            g.write(str(lista_random).replace(", ", " ").replace("[", "").replace("]", ""))

        with open('lista_fisiere.txt', "a") as g:
            g.write(fisier + "\n")
        index += 1
    return teste


def merge(lista_citita, st, mij, dr):
    n1 = mij - st + 1
    n2 = dr - mij
    stanga = [0] * (n1)
    dreapta = [0] * (n2)
    for i in range(0, n1):
        stanga[i] = lista_citita[st + i]
    for j in range(0, n2):
        dreapta[j] = lista_citita[mij + 1 + j]
    i = 0
    j = 0
    k = st
    while i < n1 and j < n2:
        if stanga[i] <= dreapta[j]:
            lista_citita[k] = stanga[i]
            i += 1
        else:
            lista_citita[k] = dreapta[j]
            j += 1
        k += 1
    while i < n1:
        lista_citita[k] = stanga[i]
        i += 1
        k += 1
    while j < n2:
        lista_citita[k] = dreapta[j]
        j += 1
        k += 1


def merge_sort(lista_citita, st, dr):
    try:
        if st < dr:
            mij = st + (dr - st) // 2
            merge_sort(lista_citita, st, mij)
            merge_sort(lista_citita, mij + 1, dr)
            merge(lista_citita, st, mij, dr)

        return lista_citita
    except:
        print("Nu se poate realiza sortarea")


def counting_sort_radix(lista_citita, exponent):
    try:
        lista_cu_index = [0] * 10
        for element in lista_citita:
            lista_cu_index[(element // exponent) % 10] += 1

        for index in range(1, len(lista_cu_index)):
            lista_cu_index[index] += lista_cu_index[index - 1]

        output = [0] * len(lista_citita)
        index = len(lista_citita) - 1
        while index >= 0:
            output[lista_cu_index[(lista_citita[index] // exponent) % 10] - 1] = lista_citita[index]
            lista_cu_index[(lista_citita[index] // exponent) % 10] -= 1
            index -= 1

        return output
    except:
        print("Nu se poate sorta")


def radix_sort(lista_citita):
    try:
        exponent = 1
        while max(lista_citita) // exponent > 0:
            lista_citita = counting_sort_radix(lista_citita, exponent)
            exponent *= 10
        return lista_citita
    except:
        print("Nu se poate realiza sortarea")


def shell_sort(lista_citita):
    try:
        interval = len(lista_citita) // 2
        while interval > 0:
            for i in range(interval, len(lista_citita)):
                temp = lista_citita[i]
                j = i
                while j >= interval and lista_citita[j - interval] > temp:
                    lista_citita[j] = lista_citita[j - interval]
                    j -= interval

                lista_citita[j] = temp
            interval //= 2

        return L
    except:
        print("Nu se poate realiza sortarea")


def counting_sort(lista_citita):
    try:
        lista_cu_index = [0] * (int(max(lista_citita)) + 1)
        for element in lista_citita:
            lista_cu_index[element] += 1

        for index in range(1, len(lista_cu_index)):
            lista_cu_index[index] += lista_cu_index[index - 1]

        output = [0] * len(lista_citita)

        index = len(lista_citita) - 1
        while index >= 0:
            output[lista_cu_index[lista_citita[index]] - 1] = lista_citita[index]
            lista_cu_index[lista_citita[index]] -= 1
            index -= 1

        return output
    except time.time:
        print("Nu se poate realiza sortarea")


def heap_sort(lista_citita):
    build_heap(lista_citita)

    for index in range(len(lista_citita) - 1, 0, -1):
        lista_citita[index], lista_citita[0] = lista_citita[0], lista_citita[index]
        heapify(lista_citita, index, 0)

    return lista_citita


def build_heap(lista_citita):
    try:
        for index in range(len(lista_citita) // 2 - 1, -1, -1):
            heapify(lista_citita, len(lista_citita), index)
    except:
        print("Nu se poate realiza sortarea")


def heapify(lista_citita, lungime_heap, i):
    try:
        index_tata = i
        index_fiu_stanga = 2 * i + 1
        index_fiu_dreapta = 2 * i + 2

        if index_fiu_stanga < lungime_heap and lista_citita[index_fiu_stanga] > lista_citita[index_tata]:
            index_tata = index_fiu_stanga

        if index_fiu_dreapta < lungime_heap and lista_citita[index_fiu_dreapta] > lista_citita[index_tata]:
            index_tata = index_fiu_dreapta

        if index_tata != i:
            lista_citita[i], lista_citita[index_tata] = lista_citita[index_tata], lista_citita[i]
            heapify(lista_citita, lungime_heap, index_tata)
    except:
        print("Nu se poate realiza sortarea")


teste = generator_de_nr_pt_teste()

print("TIM SORT-SORTARE IMPLICITA PYTHON")
nrtest = 1
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L.sort()
        stop = time.time()
        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        nrtest += 1

print("HEAP SORT")
nrtest = 1
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L = heap_sort(L)
        stop = time.time()
        Lnou = L
        Lnou.sort()
        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        if L == Lnou:
            print("TEST=OK")
        nrtest += 1

print("COUNTING SORT")
nrtest = 1
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L = counting_sort(L)
        stop = time.time()
        Lnou = L
        Lnou.sort()

        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        if L == Lnou:
            print("TEST=OK")
        nrtest += 1

nrtest = 1
print("MERGE SORT")
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L = merge_sort(L, 0, len(L) - 1)
        stop = time.time()
        Lnou = L
        Lnou.sort()

        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        if L == Lnou:
            print("TEST=OK")
        nrtest += 1

nrtest = 1
print("RADIX SORT")
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L = radix_sort(L)
        stop = time.time()
        Lnou = L
        Lnou.sort()

        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        if L == Lnou:
            print("TEST=OK")
        nrtest += 1

print("SHELL SORT")
nrtest = 1
with open('lista_fisiere.txt', "r") as lista_fisiere:
    for fisier in lista_fisiere:
        fisier = fisier.strip()
        L = []
        with open(fisier, "r+") as g:
            for line in g:
                L += line.strip().split()

        for index in range(len(L)):
            L[index] = int(L[index])

        start = time.time()
        L = shell_sort(L)
        stop = time.time()
        Lnou = L
        Lnou.sort()

        diferenta = stop - start
        print(f"Testul {nrtest} ({teste[nrtest - 1][0]} numere,{teste[nrtest - 1][1]} val. maxima): {diferenta}")
        if L == Lnou:
            print("TEST=OK")
        nrtest += 1

os.remove("lista_fisiere.txt")
