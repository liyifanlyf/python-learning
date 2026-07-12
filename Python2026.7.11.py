Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

========== RESTART: C:\Users\Administrator\Desktop\Python2026.7.11.py ==========
(32)
32
(32,)
(32,)
(32, )
(32,)
x=(1,2,3)
id(x)
2224235244160
x+=(1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x+=(1)
TypeError: can only concatenate tuple (not "int") to tuple
x+=(1,)
id(x)
2224235198592
x=tuple()
x
()
x
()
del x
x
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x
NameError: name 'x' is not defined
l=[]
l
[]
del l
l
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l
NameError: name 'l' is not defined
(32)
32
#5.3 字典
d={1:2,3:4,5:6}
d[1]
2
d[1]
2
d[1]=7
d
{1: 7, 3: 4, 5: 6}
d[4]=0
d
{1: 7, 3: 4, 5: 6, 4: 0}
d.keys()
dict_keys([1, 3, 5, 4])
print(d.keys())
dict_keys([1, 3, 5, 4])
for x in d.keys():
    print(x)

    
1
3
5
4
d.values()
dict_values([7, 4, 6, 0])
d.items()
dict_items([(1, 7), (3, 4), (5, 6), (4, 0)])
d
{1: 7, 3: 4, 5: 6, 4: 0}
l=list(d.items())
l
[(1, 7), (3, 4), (5, 6), (4, 0)]
l[0][1]
7
l[0]
(1, 7)
for i in l:
...     print(i[l])
... 
...     
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    print(i[l])
TypeError: tuple indices must be integers or slices, not list
>>> d
{1: 7, 3: 4, 5: 6, 4: 0}
>>> d.get(1,10)
7
>>> d.get(2,11)
11
>>> d
{1: 7, 3: 4, 5: 6, 4: 0}
>>> d[2]=0
>>> d
{1: 7, 3: 4, 5: 6, 4: 0, 2: 0}
>>> d.popitem()
(2, 0)
>>> d
{1: 7, 3: 4, 5: 6, 4: 0}
>>> c
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c=dict()
>>> c
{}
>>> c.popitem()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> d.pop(2,10)
10
>>> d.pop('x',10)
10
