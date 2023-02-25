def sumArray(arr):
    total = 0
    for i in arr:
        total += i
    return total


# driver function
arr = []
# input values to list
arr = [1,2,3,4,5]
 
 
ans = sumArray(arr)
 
# display sum
print('Sum of the array is ', ans)