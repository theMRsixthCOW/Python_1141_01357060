n, m = map(int, input().split())

# 讀取好友清單
friends_a = set(map(int, input().split()))
friends_b = set(map(int, input().split()))

# 取得共同好友
common_friends = sorted(friends_a & friends_b)

# 輸出共同好友數量
print(len(common_friends))

# 若有共同好友，輸出編號
if common_friends:
    print(" ".join(map(str, common_friends)))