import sys
import re

exp = sys.stdin.readline().rstrip()
arr = re.split('([-|+])', exp)      # -, + split하고 -, + 도 arr에 포함
s = '('
cnt = 0

for i in range(len(arr)):
    if arr[i] == '-':
        if cnt % 2 != 0:
            s += ')' + arr[i] + '('
            cnt = 0
        else:
            s += ')' + arr[i] + '('
            cnt += 1    
    elif arr[i] == '+':
        s += '+'
    else:
        s += str(int(arr[i]))
    
s += ')'

print(eval(s))