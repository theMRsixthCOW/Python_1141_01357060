N = int(input().strip())
arr = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

Q = int(input().strip())

for _ in range(Q): #howmaythimes
    parts = input().split()
    cmd = parts[0]
    L = int(parts[1])
    R = int(parts[2])

    # 轉 0-based index
    L -= 1
    R -= 1

    if cmd == "SUM":
        result = prefix[R+1] - prefix[L]

    elif cmd == "MAX":
        result = max(arr[L:R+1])

    elif cmd == "MIN":
        result = min(arr[L:R+1])

    print(result)
