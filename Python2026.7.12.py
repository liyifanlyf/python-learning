Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================= RESTART: C:\Users\Administrator\Desktop\1.py =================
#5.4 集合
s={1,2,3,1}
s
{1, 2, 3}
s=set([1,2,3,1,2,3,1,2,3])
s
{1, 2, 3}
s={[1],[2]}
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s={[1],[2]}
TypeError: unhashable type: 'list'
s={1,2,3,4}
s[1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s
{1, 2, 3, 4}
s[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s=set()
s
set()
type(s)
<class 'set'>
s={1,2,3,4,5,6}
t={5,6,7,8,9,0}
s-t
{1, 2, 3, 4}
s&t
{5, 6}
s^t
{0, 1, 2, 3, 4, 7, 8, 9}
s|t
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
(s|t)-(s^t)==(s&t)
True
s={1,2,3,4,5,6}
s.add(6)
s
{1, 2, 3, 4, 5, 6}
s.add(7)
s
{1, 2, 3, 4, 5, 6, 7}
s.remove(7)
s.remove(7)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.remove(7)
KeyError: 7
>>> s.clear()
>>> s
set()
>>> t={0,5,6,7,8,9}
>>> s.update(t)
>>> s
{0, 5, 6, 7, 8, 9}
>>> s.pop()
0
>>> s
{5, 6, 7, 8, 9}
>>> 5 in s
True
>>> 1 in s
False
>>> 5 not in s
False
>>> s.discard(10)
>>> s
{5, 6, 7, 8, 9}
>>> s.discard(9)
>>> s
{5, 6, 7, 8}
>>> s={1,2,3,4,5,6}
>>> t={5,6,7,8,9,0}
>>> s|t
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s.union(t)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s.intersection(t)
{5, 6}
>>> s.difference(t)
{1, 2, 3, 4}
>>> s.symmetric_difference(t)
{0, 1, 2, 3, 4, 7, 8, 9}
