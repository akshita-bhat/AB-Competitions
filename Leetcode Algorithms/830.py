s= "abcdddeeeeeeaabbbcd"
temp = []
for i in range(len(s)):
    if i+2<len(s) and s[i]==s[i+1] and s[i+1]==s[i+2]:
        temp.append([i,i+2])        
ans = []
for x, y in temp:
	if not ans or ans[-1][1] < x: ans.append([x, y])
	else: ans[-1][1] = max(ans[-1][1], y)	
print(ans) 




