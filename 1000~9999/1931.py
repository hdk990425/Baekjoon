import sys

n = int(input())
time_arr = [list(map(int, input().split())) for _ in range(n)]

time_arr.sort(key=lambda x: (x[1], x[0]))
end = time_arr[0][1]
cnt = 1

for val in time_arr[1:]:
    if val[0]>=end:
        end = val[1]
        cnt += 1

print(cnt)