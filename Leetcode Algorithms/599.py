list1 = ["KFC"]
list2 = ["KFC"]

dictionary_1= {}
dictionary_2 = {}
dictionary_3 = {}

for i in range(len(list1)):
    dictionary_1[list1[i]] = i

for j in range(len(list2)):
    dictionary_2[list2[j]] = j

for k,v in dictionary_1.items():
    if k in dictionary_2:
        dictionary_3[k] = v + dictionary_2[k]

temp = []
min_ = 100000 
for k,v in dictionary_3.items():
    if v<=min_:
        min_ = v
for k,v in dictionary_3.items():
    if v == min_:
        temp.append(k)
print(temp)
