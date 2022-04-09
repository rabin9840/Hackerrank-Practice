def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    totalSum=0
    for i in arr:
        totalSum+=i
    minSum=totalSum-arr[len(arr)-1]
    maxSum=totalSum-arr[0]
    print(minSum,maxSum)