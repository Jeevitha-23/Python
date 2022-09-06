# Searching an element in an array and returning it's index 
# N- Size of an array
# X- element to be searched
class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        for i in range(N):
            if arr[i]==X:
                return i
        return -1
