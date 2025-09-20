height = int(input("請輸入矩陣高度:"))

if height<=0:
    print("輸入錯誤")
    exit()
n=1
for i in range(1,height+1):
    for j in range(i):
        the= "   " if n<10 else "  " if n<100 else " "
        print(f"{the}{n}",end=" ")
        n+=1
    print()