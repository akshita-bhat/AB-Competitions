def solution(x,y):
    a1 = sum(range(x+1))
    b1 = x*(y-1) + sum(range(y-1))
    return str(a1+b1)

print(solution(5, 10))
print(solution(3, 2))
print(solution(2, 3))
print(solution(1, 1))
print(solution(10000000, 10000000))

print(list(range(9)))