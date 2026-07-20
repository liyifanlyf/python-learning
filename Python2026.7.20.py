Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================= RESTART: C:\Users\Administrator\Desktop\1.py =================
#7.4 lambda函数
>>> f=lambda a,b:a+b
>>> f(1,2)
3
>>> d=[('张三',90),('tom',80),('lihua',99),('wei',71)]
>>> d.sort(key=lambda x:x[-1])
>>> d
[('wei', 71), ('tom', 80), ('张三', 90), ('lihua', 99)]
>>> d.sort(key=lambda x:x[-1],reverse=True)
>>> d
[('lihua', 99), ('张三', 90), ('tom', 80), ('wei', 71)]
>>> ls=sorted(d,key=lambda x:x[-1],reverse=False)
>>> ls
[('wei', 71), ('tom', 80), ('张三', 90), ('lihua', 99)]
>>> a=(('张三',90),('tom',80),('lihua',99),('wei',71))
>>> ls=sorted(a,key=lambda x:x[-1],reverse=False)
>>> ls
[('wei', 71), ('tom', 80), ('张三', 90), ('lihua', 99)]

#8.3 Python的内置函数
all([1,1,1,2,3,-1])
True
all([1,0])
False
all([])
True
any([1,0])
True
any([0,0])
False
any([])
False
>>> chr(98)
'b'
>>> ord('b')
98
>>> 'a'<'b'
True
>>> '123'<'2'
True
>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord('1')
49
>>> ord('2')
50
>>> divmod(3,10)
(0, 3)
>>> eval('print(1)')
1
>>> exec('print')
>>> exec('print(1)')
1
>>> eval('print(1)\nprint(1+1)')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    eval('print(1)\nprint(1+1)')
  File "<string>", line 2
    print(1+1)
    ^^^^^
SyntaxError: invalid syntax
>>> exec('print(1)\nprint(1+1)')
1
2
>>> reversed([1,2,3,4,5])
<list_reverseiterator object at 0x000001F2613AF2E0>
>>> list(reversed([1,2,3,4,5]))
[5, 4, 3, 2, 1]
