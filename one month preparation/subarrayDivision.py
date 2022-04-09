
def birthday(s, d, m):
    # Write your code here
    results = 0
    for index, number in enumerate(s):
        if sum(s[index:m+index]) == d:
            results += 1
    
    return results
            
        
