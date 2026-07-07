#4.2 分支结构
if 3>2:
    print(3)
print(10)

s=eval(input("请输入一个整数:"))
if s%2==0:
    print("{}可以被2整除".format(s))
else:
    print("{}不可以被2整除".format(s))

if 2>3:
    print(3)
elif 3>2:
    print(2)
elif 4>3:
    print(4)
else:
    print(11)
print(10)

age=50
if age < 18:
    print("未成年“）
else：
    if 18<=age<30:
        print("年轻人")
    elif 30<=age<=60:
        print("中年人")
    else:
        print("老年人")

#4.3 程序的循环
for i in 'abcdefg':
    print(i)

for i in 'abcdefg':
    print(1)

for i in range(1,6):
    print(i)

list('abc')

list(range(1,10,1))

list(range(1,10))

list(range(10))

list(range(1,10,2))

for i in range(0,-10,-1):
    print(i)

for i in range(9):
    print('a')

x=0
while x<9:
    print('a')
    x+=1


