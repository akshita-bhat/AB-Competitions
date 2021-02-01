
vowels = ['a', 'e','i', 'o', 'u', 'A', 'E','I', 'O', 'U' ]
s = 'aA' # = 'holle' = aei, iea 
ss = list(s)
temp = []

def reverseVowels(s):
    ss = list(s)
    temp = []
    for i in range(len(ss)):
        if ss[i] in vowels:
            temp.append(i)
    
    for i in range(len(temp)):
        ss[temp[i]] = s[temp[len(temp)-i-1]]
    return ''.join(ss)

print(reverseVowels(s))



