def plusMinus(arr):
    count_positive=0
    count_negative=0
    count_zero=0
    total_n=len(arr)
    
    for i in arr:
        if i>0:
            count_positive+=1
        elif i<0:
            count_negative+=1
        else:
            count_zero+=1
    print("{0:.6f}".format(count_positive/total_n))
    print("{0: .6f}".format(count_negative/total_n))
    print("{0: .6f}".format(count_zero/total_n))
