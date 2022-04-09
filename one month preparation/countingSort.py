def countingSort(arr):
    # Write your code here
    result=[0]*100
    for i in arr:
        result[i]+=1
    return result