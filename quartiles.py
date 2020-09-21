from statistics import median
import math
n=int(input())
ary=[int(x) for x in input().split(' ')]
ary.sort()
k=math.floor(n/2)
j=math.ceil(n/2)
L=ary[0:k]
U=ary[j:]

print(int(median(L)))
print(int(median(ary)))
print(int(median(U)))
