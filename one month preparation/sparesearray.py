def matchingStrings(strings, queries):
    # Write your code here
    b=[]
    for i in queries:
        b.append(strings.count(i))
    return b