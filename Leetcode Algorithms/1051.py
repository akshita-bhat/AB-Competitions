h = [1,1,4,2,1,3]


x = sorted(h)
print(x,h)
count = 0
for i in range(len(x)):
    if x[i] != h[i]:
        count+=1
print(count)


