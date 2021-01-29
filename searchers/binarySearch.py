import math
def binarySearch(arr,l,h,phoneNumber):
    mid=math.floor((l+h)/2)
    if l>h:
        return False     
    if arr[mid]['mobile_number']==phoneNumber:
        return True
    else:
        if(phoneNumber>arr[mid]['mobile_number']):
           return binarySearch(arr,mid+1,h,phoneNumber)
        elif(phoneNumber<arr[mid]['mobile_number']):
          return binarySearch(arr,l,mid-1,phoneNumber)

def binarySearchItems(arr,l,h,id):
    mid=math.floor((l+h)/2)
    if l>h:
        return 'not present'    
    if arr[mid]['id']==id:
        return mid
    else:
        if(id>arr[mid]['id']):
           return binarySearchItems(arr,mid+1,h,id)
        elif(id<arr[mid]['id']):
          return binarySearchItems(arr,l,mid-1,id)


