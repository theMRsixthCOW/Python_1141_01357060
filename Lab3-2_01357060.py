import sys

input_lines = sys.stdin.read().splitlines()
N=int(input_lines[0])

for line in input_lines[1:]:
    if not line.strip():
        continue

    target = list(map(int, line.strip().split()))
    stack = []
    current = 1
    possible = True

    for num in target:
        while current <= N and (not stack or stack[-1] != num):
            stack.append(current)
            current += 1
        if stack and stack[-1] == num:
            stack.pop()
        else:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")