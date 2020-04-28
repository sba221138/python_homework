x = eval(input("請輸入數值："))

if x % 2 == 0 and x % 7 == 0:
    print(x,"是2也是7的倍數")
elif x % 2 == 0 :
    print(x,"是2的倍數")
elif x % 7 == 0 :
    print(x,"是7的倍數")
else:
    print(x,"不是2也不是7的倍數")