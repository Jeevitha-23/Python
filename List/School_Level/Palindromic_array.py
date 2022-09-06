# This function returns 1 if all the elements of array is Palindrome else 0
def PalinArray(arr ,n):
    for i in arr:
       j = str(i)[::-1]
       if(j!=str(i)):
           return False
    return True
