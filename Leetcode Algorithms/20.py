s = "([{})"
def f(s):
    open_brackets = ['(','{','[']
    closed_brackets = [')','}',']']
    temp = []
    count= 0
    if len(s)==0:
        return True
    for i in range(len(s)):
        if s[i] in open_brackets:
            temp.append(s[i])
        elif s[i] in closed_brackets:
            if len(temp)==0:
                count+=1
            else:
                o = temp.pop()
                if (o== '(' and s[i] == ')') or (o== '{' and s[i] == '}') or (o== '[' and s[i] == ']'):
                    continue
                else:
                    count+=1
    return count
                    
print(f(s))                    