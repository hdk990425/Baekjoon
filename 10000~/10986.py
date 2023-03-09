import sys

n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))
n_sum = 0
rmd_list = [0 for _ in range(m)]
rmd_list[0] = 1        # 밑에서 5번 밖에 안돔
cnt = 0

for i in range(n):
    n_sum += num_list[i]
    r = n_sum % m
    rmd_list[r] += 1

for j in rmd_list:
    cnt += j*(j-1)//2       # 조합

print(cnt)