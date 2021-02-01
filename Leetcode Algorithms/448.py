n = [4,3,2,7,8,2,3,1]
nn = set(n)
new = set(i+1 for i in range(len(n)))
print(list(new-nn))    



