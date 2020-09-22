
from statistics import mean
import math
n=int(input())
ary=[int(x) for x in input().split(" ")]

sum=0
for i in range(n):
    sum+=(ary[i]-mean(ary))**2

std = math.sqrt(sum/n)
print(round(std, 1))
