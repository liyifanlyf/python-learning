#1.此代码题目为：列表中有四个元素，将其倒序输出。
#原始文件：
#animals = ['cow', 'duck', 'cat', 'dog']
#_____
#print(_____)
#答案：
animals = ['cow', 'duck', 'cat', 'dog']
animals.reverse()
print(animals)


#2.此代码题目为：文件给出字符串，删除字符串开头和末尾的空白，结果屏幕输出。
#原始文件：
#word = "   窗前明月光，疑是地上霜。   "
#print(_____)
#答案：
word = "   窗前明月光，疑是地上霜。   "
print(word.strip())


#3.此代码题目为：使用循环输出从1到50之间的奇数
#原始文件：
#_____
#while count < 50:
#    _____
#    if count % 2 == 0:
#        _____
#    print(count,end=",
#答案：
count = 0
while count < 50:
    count += 1
    if count % 2 == 0:
        continue
    print(count,end=",")


#4.此代码题目为：使用turtle库的turtle.circle()函数、turtle.seth()函数绘制一个四瓣花图形
#原始文件：
#import turtle
#for i in range(_____):
#    turtle.seth(_____)
#    turtle.circle(50,90)
#    turtle.seth(_____)
#    turtle.circle(50,90)
#turtle._____
#答案：
import turtle
for i in range(4):
    turtle.seth(90*(i+1))
    turtle.circle(50,90)
    turtle.seth(-90+i*90)
    turtle.circle(50,90)
turtle.hideturtle()


#5.此代码题目为：使用Python的异常处理结构编写对数计算，要求底数大于0且不等于1，真数大于0，且输入的必须为实数，否则抛出对应的异常。
#原始代码：
#_____
#try:
#    a = eval(input('请输入底数：'))
#    b = eval(input('请输入真数：'))
#    c = _____
#except ValueError:
#    ...
#except ZeroDivisionError:
#    print('底数不能为1')
#except NameError:
#    print('输入必须为实数')
#else:
#    print(c)


#6.此代码题目为：凯撒密码是一种非常古老的加密算法，相传当年凯撒大帝行军打仗时为了保证自己的命令不会被敌军知道，它采用了替换方法将信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即循环后三位，对应关系如下：
#原文：A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
#密文：D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C
#原文字符P，其密文字符C满足如下条件：
#C=(P+3) mod 26
#解密方法反之，满足如下条件：
#P=(C-3) mod 26
#凯撒密码包括加密和解密两个部分。
#凯撒密码的加密算法程序首先接收用户输入的文本，然后对字母a-z和字母A-Z按照密码算法进行转换，同时输出。其它非英文字母原样输出。
#原始代码：
#intxt = input("请输入明文：")
#...
#答案：
intxt = input("请输入明文：")
for p in intxt:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end="")
    elif "A" <= p <= "Z":
        print(chr(ord("A")+(ord(p)-ord("A")+3)%26),end="")
    else:
        print(p,end="")
