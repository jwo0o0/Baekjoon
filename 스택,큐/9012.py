
import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    s = sys.stdin.readline()
    stack = []
    for j in s:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
