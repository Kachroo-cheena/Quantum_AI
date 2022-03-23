################ Answer 1 #####################

# def findMin(arr, start, end):
#     if end < start:
#         return arr[0]
#     if end == start:
#         return arr[start]

#     mid = int((start + end)/2)
#     if mid < end and arr[mid+1] < arr[mid]:
#         return arr[mid+1]
#     if mid > start and arr[mid] < arr[mid - 1]:
#         return arr[mid]
 
#     if arr[end] > arr[mid]:
#         return findMin(arr, start, mid-1)
#     return findMin(arr, mid+1, end)
 

# arr = [7,8,9,1,2,3,4,5,6]
# n = len(arr)
# print("Minimum element of rotated Array is " + str(findMin(arr, 0, n-1)))
 




############# Answer 2 ####################

def minDis(str1, str2, n, m, dp) :     
  if(n == 0) :
      return m       
  if(m == 0) :
      return n

  if(dp[n][m] != -1)  :
      return dp[n][m]

  if(str1[n - 1] == str2[m - 1]) :          
    if(dp[n - 1][m - 1] == -1) :
        dp[n][m] = minDis(str1, str2, n - 1, m - 1, dp)
        return dp[n][m]                  
    else :
        dp[n][m] = dp[n - 1][m - 1]
        return dp[n][m]     
    
  else :           
    if(dp[n - 1][m] != -1) :  
      m1 = dp[n - 1][m]     
    else :
      m1 = minDis(str1, str2, n - 1, m, dp)
              
    if(dp[n][m - 1] != -1) :               
      m2 = dp[n][m - 1]           
    else :
      m2 = minDis(str1, str2, n, m - 1, dp)  
    if(dp[n - 1][m - 1] != -1) :   
      m3 = dp[n - 1][m - 1]   
    else :
      m3 = minDis(str1, str2, n - 1, m - 1, dp)
     
    dp[n][m] = 1 + min(m1, min(m2, m3))
    return dp[n][m]
     
str1 = "Week Experience"
str2 = "Work Experience"
    
n = len(str1)
m = len(str2)
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
              
print(minDis(str1, str2, n, m, dp))