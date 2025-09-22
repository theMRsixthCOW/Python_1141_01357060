n, m = map(int, input().split())
a_friends = set(map(int, input().split()))
b_friends = set(map(int, input().split()))

common_friends = a_friends & b_friends

print(len(common_friends))

if common_friends:
    print(*common_friends.sort())