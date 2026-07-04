Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:\Users\Administrator\Desktop\2026.7.4.py =============
x='d'
x="asdfd"
x='''wefrew'''
x="""小明说：'你好'"""
print(x)
小明说：'你好'
小明说：'你好'
SyntaxError: invalid character '：' (U+FF1A)

x
"小明说：'你好'"
isinstance(x,str)
True
type(x)
<class 'str'>
s="世界那么大，我想去看看"
s[0,10]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0,10]
TypeError: string indices must be integers, not 'tuple'
s[0:10]
'世界那么大，我想去看'
s[0,11]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[0,11]
TypeError: string indices must be integers, not 'tuple'
s[0:11]
'世界那么大，我想去看看'
s[-1:-10]
''
s[-1:-10]
''
s[-1]
'看'
s[-1:-5]
''
s[0:5]
'世界那么大'
s[0:5:2]
'世那大'
s[6:]
'我想去看看'
s[:5]
'世界那么大'
 s[0:6:2]
 
SyntaxError: unexpected indent
s[0:6:2]
'世那大'
s[0:6:1]
'世界那么大，'
x[-5:-1:1]
"：'你好"
s[-5:-1:1]
'我想去看'
s[-5:0]
''
s[-6:-1]
'，我想去看'
s[-1:-5:-1]
'看看去想'
s[-5:-1]
'我想去看'
s[::-1]
'看看去想我，大么那界世'
s[-1::-3]
'看想大界'
s[10:3:-2]
'看去我大'
#3.4
x='abc'
y='def'
x+y
'abcdef'
y+x
'defabc'
x*3
'abcabcabc'
x+x+x
'abcabcabc'
3*x
'abcabcabc'
s='abcdef'
x in s
True
y in s
True
x in y
False
len(x)
3
x[-1]
'c'
x[len(x)-1]
'c'
1
1
str(1)
'1'
ord('a')
97
chr('98')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    chr('98')
TypeError: 'str' object cannot be interpreted as an integer
>>> chr(98)
'b'
>>> hex(16)
'0x10'
>>> oct(16)
'0o20'
>>> x='AaBb Cc AaBb'
>>> x.lower()
'aabb cc aabb'
>>> x.upper()
'AABB CC AABB'
>>> x.split()
['AaBb', 'Cc', 'AaBb']
>>> x.split('c')
['AaBb C', ' AaBb']
>>> x='AaBb Cc AaBb'
>>> x.count('b')
2
>>> x.count('Cc')
1
>>> x.replace('Aa','12')
'12Bb Cc 12Bb'
>>> x.replace('Aa','1')
'1Bb Cc 1Bb'
>>> x.replace('A','')
'aBb Cc aBb'
>>> x.center(30,'*')
'*********AaBb Cc AaBb*********'
>>> x='AaBb Cc AaBb'
>>> x.center(4,'*')
'AaBb Cc AaBb'
>>> x.strip('Aa')
'Bb Cc AaBb'
>>> x.strip('a')
'AaBb Cc AaBb'
>>> x.strip('AaBb')
' Cc '
>>> x.join(['1','2','3'])
'1AaBb Cc AaBb2AaBb Cc AaBb3'
