Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:\Users\Administrator\Desktop\2026.7.4.py =============
x='abcdefg'
'{:@>30}'.format(x)
'@@@@@@@@@@@@@@@@@@@@@@@abcdefg'
'{:*^30}'.fpormat(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    '{:*^30}'.fpormat(x)
AttributeError: 'str' object has no attribute 'fpormat'. Did you mean: 'format'?
'{:*^30}'.format(x)
'***********abcdefg************'
x.center(30,'*')
'***********abcdefg************'
'{:,}'.format(21342432)
'21,342,432'
'{:.3}'.format(x)
'abc'
'{:.3}'.format(123.4353)
'1.23e+02'
KeyboardInterrupt
KeyboardInterrupt
'{:.3f}'.format(123.4353)
'123.435'
'{:.3e}'.format(123.4353)
'1.234e+02'
'{:.3b}'.format(123.4353)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    '{:.3b}'.format(123.4353)
ValueError: Unknown format code 'b' for object of type 'float'
'{:.3b}'.format(1234353)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    '{:.3b}'.format(1234353)
ValueError: Precision not allowed in integer format specifier
'{:.3b}'.format(1234353)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '{:.3b}'.format(1234353)
ValueError: Precision not allowed in integer format specifier
'{:.3E}'.format(123.4353)
'1.234E+02'
'{:.3%}'.format(123.4353)
'12343.530%'
'{:.3o}'.format(1234353)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    '{:.3o}'.format(1234353)
ValueError: Precision not allowed in integer format specifier
'{:b}'.format(123)
'1111011'
'{:x}'.format(123)
'7b'
'{:c}'.format(123)
'{'
#3.7 类型判断与类型间的转换
x=3.2
type(x)
<class 'float'>
>>> int(x)
3
>>> int(3.5)
3
>>> float(3)
3.0
>>> int('243')
243
>>> float('3442.324')
3442.324
>>> eval('34')
34
>>> eval('234.432')
234.432
>>> int('3.34')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int('3.34')
ValueError: invalid literal for int() with base 10: '3.34'
>>> tstr='television'
>>> print(tstr[-6:6])
vi
>>> s="hello world"
>>> print(len(s.split())
... print(s.title())
...       
SyntaxError: '(' was never closed
>>> print(len(s.split())
... print(s.title())
...       
SyntaxError: '(' was never closed
>>> print(len(s.split(sep=None))
... print(s.title())
...       
SyntaxError: '(' was never closed
>>> print(len(s.split()))
...       
2
