
n=int(input("請輸入三角形的高度："))
if(n==0):
    print("輸入錯誤")
    exit()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()