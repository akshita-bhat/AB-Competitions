num1 = '25'
num2 = '32'
'''
# sum of num1 and num2 - 95% 
print(str(int(num1)+int(num2)))

# sum of num1 and num2 - 5% 

sum_ = 0
for i in range(0,len(num1)):
    sum_+=int(num1[len(num1)-1-i])*(10**i)
    
for i in range(0,len(num2)):
    sum_+=int(num2[len(num2)-1-i])*(10**i)        

print(sum_)
'''
#  sum of num1 and num2 without converting in int

i = len(num1)-1
j = len(num2)-1
print(i,j)
carry = 0
sb = ''
while i>=0 or j>=0:
    sum_1 = carry
    if j>=0:
        sum_1+= int(num2[j], 10)
        j-=1
    if i>=0:
        sum_1+= int(num1[i], 10)
        i-=1
    sb+=str(sum_1%10)
    carry = sum_1//10
    #print(sb, carry)
    
if carry!=0:
    sb+=str(carry)
        
print(sb[::-1])




