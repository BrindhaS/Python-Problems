def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
        
def comm(a,b):
    n = gcd(a,b)
    res = 0
    sq = int(n**(1.0/2))
    for i in range(1,sq):
        if n%i == 0:
            if n/i == i:
                res += 1
            else:
                res += 2
    if res==0 & n!=1:
        res += 1
    return res

lst = [int(x) for x in input().split()]
res = comm(lst[0],lst[1])
print(res)
