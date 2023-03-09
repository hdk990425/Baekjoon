import sys

s = input()
q = int(input())

arr = [[0 for i in range(26)] for i in range(len(s))]
cnt = []

arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    arr[i][ord(s[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for i in range(q):
    a = input().split()
    if int(a[1]) > 0:       # a[1]: l, a[2]: r
        res = arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    cnt.append(res)

for res in cnt:
    print(res)