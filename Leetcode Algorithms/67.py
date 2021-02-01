a = '1010' # 0*2**0 +2**1
b = '1011'
a_ = 0
b_ = 0
for i in range(0,len(a)):
    a_+=int(a[len(a)-1-i])*(2**i)
for i in range(0,len(b)):
    b_+=int(b[len(b)-1-i])*(2**i)        
sum_ = a_+b_

print(a_, b_,sum_,str(bin(sum_)[2:]))




