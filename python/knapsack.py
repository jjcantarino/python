
# coding: utf-8

# In[1]:

import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
def RP(V1,V2,V3,X):
    #fem una matriu de 0 on posarem les cotes
    items = [[0 for x in range(0,X+1)] for y in V1]
    i=0
    #i=0, recorregut pels n items
    while i < len(V1):
        j = 1
        #trobem el màxim que podem ficar amb cada item (de menor a major) fins arribar a la capacitat màxima 
        #tot combinant-los amb els items de menor cost (files anteriors)
        while j <= X:
            #inicialitzem a cada posició el contingut de la fila anterior ja que si finalment l'item es de pes
            #major al que pot suportar la motxilla, ficarem el contingut de la fila anterior com a màxim en aquesta posició
            items[i][j] = items[i-1][j]
            k = 1
            #comprovem el màxim amb k ∈ V3 unitats del item
            while k <= V3[i] and j >= V1[i]*k:
                #ja que j significa el pes que pot suportar la motxilla a aquesta iteració, el pes total ha d'esser inferior
                items[i][j] = max(V2[i]*k + items[i-1][j-V1[i]*k] , items[i][j])
                k = k + 1
            j = j + 1
        i = i + 1
    for i in items:
        print i
    output = []
    i = len(V1) - 1
    j = X
    cota = 0
    #per trobar la solució òptima, apuntem a l'últim element d'items, que 
    #representa la solució òptima amb el pes màxim que pot suportar la
    #motxilla amb l'últim item.
    while i >= 0 and j > 0 : 
        if i == 0:
            cota = cota + V1[i]
            output.append([i,j])
            j = j - V1[i]
            i = i - 1
        #si l'element i,j es igual que i-1,j vol dir que l'item i no forma
        #part de la solució òptima i apuntem al item anterior (i-1)
        elif items[i][j] == items[i-1][j]:
            i = i - 1
        #si no, vol dir que l'item "i" forma part de la solució 1 cop més
        else:
            cota = cota + V1[i]
            output.append([i,j])
            #si la solució òptima en aquesta posició pes "j" modul el valor
            #d'aquest item "i" resulta el valor de l'element anterior
            #vol dir que l'item "i-1" també és solució
            if items[i][j] % V2[i] == V2[i-1]:
                k=1
                #observem quantes aparicions de l'element "i" trobem a la solució
                while k < V3[i] and items[i][j] / V2[i]*k != V2[i-1]:
                    cota = cota + V1[i]
                    output.append([i,j])
                    k=k+1;
                j = j - k * V1[i]
                i = i - 1
            #si no, vol dir que nomès "i" es solució i reduim el pes de la motxila
            else:
                j = j - V1[i]
    
    path_x = [point[1] for point in output]
    path_y = [point[0] for point in output]
    plt.plot(path_x, path_y)
    lines = plt.plot(path_x, path_y, 'ro')
    plt.setp(lines, color='r', linewidth=2.0)
    im = plt.imshow(items,interpolation='nearest',cmap='Blues')
    plt.xlabel("Weight")
    plt.ylabel("Element")
    cbar = plt.colorbar(im,ticks=[0,items[len(items)-1][len(items[len(items)-1])-1]/2,items[len(items)-1][len(items[len(items)-1])-1]],orientation='horizontal')
    cbar.ax.set_xticklabels(['0','KnapSack Value',items[len(items)-1][len(items[len(items)-1])-1]])
    plt.grid()
    for elem in range (0, len(output)):
        output[elem] = output[elem][0]
    return output, cota
RP([3,4,4,20,2],[100,30,20,3,7],[1,2,5,8,2],20)

