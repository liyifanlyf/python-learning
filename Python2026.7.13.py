Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================= RESTART: C:\Users\Administrator\Desktop\1.py =================
>>> f=open('Python2026.7.13.csv')
>>> data=f.readlines()
>>> data
['1,2,3\n', '4,5,6\n', '7,8,9\n']
>>> ls=[]
>>> for i in data:
...     ls.append(i.strip().split(','))
... 
...     
>>> ls
[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
>>> fi=open('2.csv','w')
>>> for i in ls:
...     fi.write(','.join(i)+'\n')
... 
...     
6
6
6
>>> fi.close()
>>> 
