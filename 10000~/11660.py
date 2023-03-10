import sys

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_arr = [[0 for i in range(n+1)] for j in range(n+1)]
sum_list = []

for i in range(n):
    for j in range(n):
        if (i==0) and (j==0):
            sum_arr[i][j] = arr[i][j]
        elif j==0:
            sum_arr[i][0] = sum_arr[i-1][0] + arr[i][0]
        elif i==0:
            sum_arr[0][j] = sum_arr[0][j-1] + arr[0][j]
        else:
            sum_arr[i][j] = arr[i][j] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

# print(sum_arr)

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum_list.append(sum_arr[x2-1][y2-1] - sum_arr[x2-1][y1-2] - sum_arr[x1-2][y2-1] + sum_arr[x1-2][y1-2])

for val in sum_list:
    print(val)