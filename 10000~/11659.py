import sys

n, m = map(int, input().split())

num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0 for i in range(n+1)]

for idx in range(n):
    sum_list[idx+1] = sum_list[idx] + num_list[idx]

for _ in range(m):
    i, j = map(int, input().split())
    if i == j:
        print(num_list[i-1])
    else:
        print(sum_list[j]-sum_list[i-1])