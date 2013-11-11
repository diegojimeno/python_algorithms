# -*- coding: utf-8 -*-
"""
@Author Diego Jimeno Prieto
@version 1.0
"""
import random 

def fquick_sort(array):
        
    """
    Optimized quick sort implemented in python by vectorizing
    all operations involved 
    """    
    if len(array) <= 1:
        return array
    
    less = []
    greater = []    
    
    pivot = 0
    #choose the pivot as being the median of 
    #the first middle and third, otherwise the middle
    if len(array) > 3: 
        
        median_list = [array[1], array[len(array)/2], array[-1]]  
        pivot = median_list[len(median_list) / 2]
    else:
        pivot = random.choice(array)
     
    #too much verbose to remove the pivot, can be changed by "del" function    
    array = array[0:array.index(pivot):] + array[-(len(array) - array.index(pivot) - 1)::]
   
    [less.append(i) if i < pivot else greater.append(i) for i in array]
    
    #two recursive calls
    return fquick_sort(less) + [pivot] + fquick_sort(greater)
    
res = fquick_sort([3, 23, 1, 54])
