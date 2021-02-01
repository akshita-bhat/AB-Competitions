import math

area = 99
l=int(math.sqrt(area))
temp = []
for i in reversed(range(l+1)):
    if i!=0 and area%i==0:
        if i >= area/i:
            temp.append(i)
            temp.append(int(area/i))
            break
        else:
            temp.append(int(area/i))
            temp.append(i)
            break
        
print(temp)
'''
p = n*k
(n>=k and min(n-k))
'''



