from statistics import median
import math

n=int(input())
ary=[int(x) for x in input().split(" ")]
frq=[int(x) for x in input().split(" ")]

S=[]
for i in range(n):
    S+=([ary[i]]*frq[i])

S.sort()
k=math.floor(len(S)/2)
j=math.ceil(len(S)/2)
L=S[0:k]
U=S[j:]


print(round(median(U)-median(L)+0.0, 1))
