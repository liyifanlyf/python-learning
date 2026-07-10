4.4 循环扩展
x=0
while x<9:
    print('a')
    x+=1
print(10)


x=10
while True:
    print('a')
    x-=1
    if x==0:
        break
print(10)


x=10
while True:
    print('a')
    x-=1
    if x==0:
        break
else:
    print(10)


x=10
while True:
    if x==0:
        continue
    print(x)
    x-=1


for i in range(10):
    if i == 5:
        continue
    print(i)


for i in range(3):
    for j in range(2):
        print(i)
        if i==1:
            break
