nums1 = [1,1,1,1]
nums2 = [1,2,3,1,1,3]
from collections import Counter
import math
def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))
# output = (0,1), (0,2), (0,3), (0,4), (1,2), (2,3), (1,4)   
# [1,2,3,1,1,3] output = (0,3); (0,4); (3,4) and (2,5)
temp = []
count = 0
'''
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        #print(i,j)
        if nums[i] == nums[j]:
            count+=1
print(count)
'''
       
d = Counter(nums2)
print(d)
for k,v in d.items():
    if v>1:
        count+= (round(nCr(v,2)))
print(count)




