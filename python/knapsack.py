
# coding: utf-8

# In[1]:

import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


#Algorithm that finds the optimal solution for the knapsack problem
#avoiding compare each posible combination and based in the last best combination

#Problem description:

#Due a max "X" value the knapsack can handle and a combination of items
#that have a "V1" value, "V2" weight and appear certain "V3" times 
#each position of V1, V2, V3 vectors represents / points each item
#it means each vector size must be equal and that size represents the number of items


def RP(V1,V2,V3,X):
    #init matrix of 0
    items = [[0 for x in range(0,X+1)] for y in V1]
    i=0
    #for each item
    while i < len(V1):
        j = 1
        #first we find max value we can fit until we reach max capacity (weight)
        #for each capacity in X (max capacity)
        while j <= X:
            #init in this [i][j] position the combination set in the row above [j-1]
            #because if we don't find an optimal combination it will remain as previous row
            items[i][j] = items[i-1][j]
            k = 1
            #for each k unit of this item and j (actual max weight) less or equal than the weight of this item k times 
            while k <= V3[i] and j >= V1[i]*k:
                #optimal combination in this i,j position is the max value between:
                # - Previous row / item (items[i][j])
                # - Value of this i item k times + max value of the previous 
                  # item with the remain weight (j actual max weight - weight of his i item k times)  
                items[i][j] = max(V2[i]*k + items[i-1][j-V1[i]*k] , items[i][j])
                k = k + 1
            j = j + 1
        i = i + 1
    for i in items:
        print i
    output = []
    i = len(V1) - 1
    j = X
    height = 0
    #to find the optimal solution we point the last and heaviest item of the array, 
    #which obviously represents the best solution the knapsack can handle
    #and we iterate backwards
    while i >= 0 and j > 0 : 
        if i == 0:
            height = height + V1[i]
            output.append([i,j])
            j = j - V1[i]
            i = i - 1
            
        #if i,j combination is equal than previous row (previous item best combination)
        #it means i item it's not part of the actual best solution
        #we decrement a row (look previous item)
        elif items[i][j] == items[i-1][j]:
            i = i - 1
        #else, means actual i item is part of the combination at least once
        else:
            height = height + V1[i]
            output.append([i,j])
            #if optimal value in that row with that "j" weight modulus (%) 
            #the value of the actual "i" item is equal to the previous item value
            #it means previous "i-1" item is also part of the optimal solution
            if items[i][j] % V2[i] == V2[i-1]:
                k=1
                #How many times does actual "i" item appear?
                #for each "k" time item "i" appears and the value of the previous item
                #is different than the  actual optimal solution divided the value of actual item "k" times
                #the actual item will be combination again
                while k < V3[i] and items[i][j] / V2[i]*k != V2[i-1]:
                    height = height + V1[i]
                    output.append([i,j])
                    k=k+1;
                j = j - k * V1[i]
                i = i - 1
            #else, it means previous item is not part of the solution, j next optimal
            #solution weight pointer will be the result of reducing actual item weight
            else:
                j = j - V1[i]
    #represent the final matrix and solution as the image attached in repository
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
    return output, height
#program input example
RP([3,4,4,20,2],[100,30,20,3,7],[1,2,5,8,2],20)

