#4.5 程序的异常处理
try:
    print(10/0)
except ValueError:
    print('出现错误')
except ZeroDivisionError:
    print('0')


try:
    print(10/1)
except:
    print('出现错误')
else:
    print('程序正确')


try:
    print(10/1)
except:
    print('出现错误')
else:
    print('程序正确')
finally:
    print('程序执行完毕')


#5.1 列表
x='abc'
id(x)

x+='eufhdkskk'
id(x)

l=[1,2,3]
id(l)

l+=[1,2,3,4]
id(l)

l=[1,'sad',(1,2,3),2,34,4]
l[1:4]

l.count(1)
l.count('sad')

l.append(10)
l

l.insert(100,11)
l

l.extend('asd')
l

l.append('sad')
l

l.remove('sad')
l

l.pop(1)
l

l.reverse()
l

l1=l.copy()
l1

l.clear()
l1
l2=l1
l2
l1.clear()
l1
l2

l=[1,2,3]
id(l)
l1=l.copy()
id(11)
l2=l
id(l2)

