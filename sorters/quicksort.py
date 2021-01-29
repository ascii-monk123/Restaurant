import math
from os import dup
def partition(low,high,arr):
    l=low-1
    h=high+1
    pivot=math.floor((low+high)/2)
    ele=arr[pivot]['times_ordered']
    while(l<h):
        l+=1
        while(arr[l]['times_ordered']<ele and l<len(arr)-1):
            l+=1
        h-=1
        while(arr[h]['times_ordered']>ele and h>0):
            h-=1
        if l<h:
            temp=arr[l]
            arr[l]=arr[h]
            arr[h]=temp
    return h
def partitionCustomer(low,high,arr):
    l=low-1
    h=high+1
    pivot=math.floor((low+high)/2)
    ele=arr[pivot]['mobile_number']
    while(l<h):
        l+=1
        while(arr[l]['mobile_number']<ele and l<len(arr)-1):
            l+=1
        h-=1
        while(arr[h]['mobile_number']>ele and h>0):
            h-=1
        if l<h:
            temp=arr[l]
            arr[l]=arr[h]
            arr[h]=temp
    return h

def quick(arr,low,high):
    if low<high:
        piv=partition(low,high,arr)
        quick(arr,low,piv)
        quick(arr,piv+1,high)

    else:
        return 

def quick2(arr,low,high):
    if low<high:
        piv=partitionCustomer(low,high,arr)
        quick2(arr,low,piv)
        quick2(arr,piv+1,high)
    else:
        return
# arr=[7, 10, 6, 8, 9, 1, 9, 8, 5, 6, 2, 9, 8, 4, 6, 9, 4, 9, 8, 5, 9, 6, 6, 0, 1, 4, 6, 3, 5, 1]
# quick(arr,0,len(arr)-1)
# print(arr)


def quickSort(arr,type):
    duparr=[items for items in arr]
    if type=="items":
        quick(duparr,0,len(duparr)-1)
    elif type=='customers':
        quick2(duparr,0,len(duparr)-1)
    return duparr
        


