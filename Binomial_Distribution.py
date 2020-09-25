def combination(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def binomial(x, n, p):
    return combination(n, x)*(p**x)*((1-p)**(n-x))

boy, girl = list(map(float, input().split(" ")))
odd=boy/girl
prob_success= odd/(1+odd)
probability=0

for i in range(3, 7):
    probability+=binomial(i, 6, prob_success)

print(round(probability, 3))
