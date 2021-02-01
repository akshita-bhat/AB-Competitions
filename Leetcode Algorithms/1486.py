#print(0^2^4^6^8)
n = 5
start = 0

xor = 0

for i in range(n):
    #x = 
    xor = xor^(start+2*i)
print(xor)

