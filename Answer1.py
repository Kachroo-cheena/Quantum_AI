################ Answer 1 #####################

def findMin(arr, start, end):
    if end < start:
        return arr[0]
    if end == start:
        return arr[start]

    mid = int((start + end)/2)
    if mid < end and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    if mid > start and arr[mid] < arr[mid - 1]:
        return arr[mid]
 
    if arr[end] > arr[mid]:
        return findMin(arr, start, mid-1)
    return findMin(arr, mid+1, end)
 

arr = [7,8,9,1,2,3,4,5,6]
n = len(arr)
print("Minimum element of rotated Array is " + str(findMin(arr, 0, n-1)))
 



