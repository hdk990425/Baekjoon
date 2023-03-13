import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = list(int(input()) for _ in range(n))
cnt = 0

for i in reversed(coin_list):
    if k >= i:
        s = k // i
        k = k % i
        cnt += s

print(cnt)        
