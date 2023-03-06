import sys

n, k = map(int, input().split())
temper = list(map(int, sys.stdin.readline().split()))
temper_sum = [0 for i in range(n+1)]
sum_list = []

for idx in range(n):
    temper_sum[idx+1] = temper_sum[idx] + temper[idx]

for j in range(n-k+1):
    sum_list.append(temper_sum[j+k]-temper_sum[j])

print(max(sum_list))