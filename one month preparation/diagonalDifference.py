def diagonalDifference(arr):
    # Write your code here
    first=0
    second=0
    for i in range(len(arr)):
        first+=arr[i][i]
        second+=arr[i][len(arr)-1-i]
    return abs(first-second)
