def sockMerchant(n, ar):
    # Write your code here
        
    return sum([ar.count(i)//2 for i in set(ar)])
print(sockMerchant(7, [1,2,1,2,1,3,2,1]))
