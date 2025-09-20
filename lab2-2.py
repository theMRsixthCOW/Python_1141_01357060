
n = int(input("請輸入n:"))
print("請輸入數列:")
nums = []
for i in range(n):
    nums.append(int(input()))
print("排列前數列為:")
for j in range(n):
  print(nums[j], end=" ")
  
print()
nums.sort()
print("排列後數列為:")
for j in range(n):
  print(nums[j], end=" ")
  