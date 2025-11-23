def decompress(s):
    stack = []
    num = 0
    cur = ""

    for ch in s:
        if ch.isdigit():    
            num = num * 10 + int(ch)

        elif ch == '(':
            stack.append((cur, num))
            cur = ""
            num = 0

        elif ch == ')':
            prev, k = stack.pop()
            cur = prev + cur * k

        else:
            cur += ch
    return cur

s = input().strip()
print(decompress(s))
