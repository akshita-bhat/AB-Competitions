N = 2
trust = [[1,2]]
dictionary = {}
for i in range(1,N+1):
    dictionary[i] = []
print(dictionary)
for i in trust:
    dictionary[i[1]].append(i[0])
print(dictionary)
temp = list(range(1,N+1))

judge = -1
flag = False
for k,v in dictionary.items():
    if len(v)==N-1: # 3 = [1,2,4]
        for k1,v1 in dictionary.items():
            if k in v1:
                flag = True
        if flag==False:
            judge = k
print(judge)


    



