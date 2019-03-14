Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.pop()
9
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> x.append(10)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
>>> x.remove(5)
>>> x
[0, 1, 2, 3, 4, 6, 7, 8, 10]
>>> x.count(8)
1
>>> x
[0, 1, 2, 3, 4, 6, 7, 8, 10]
>>> x.extend([3])
>>> x
[0, 1, 2, 3, 4, 6, 7, 8, 10, 3]
>>> x.reverse()
>>> x
[3, 10, 8, 7, 6, 4, 3, 2, 1, 0]
>>> x.sort()
>>> x
[0, 1, 2, 3, 3, 4, 6, 7, 8, 10]
>>> x.insert(5,5.5)
>>> x
[0, 1, 2, 3, 3, 5.5, 4, 6, 7, 8, 10]
>>> x.index(7)
8
>>> y=[m*10 for m in x]
>>> y
[0, 10, 20, 30, 30, 55.0, 40, 60, 70, 80, 100]
>>> for k in (x):
	print(k)

	
0
1
2
3
3
5.5
4
6
7
8
10
>>> k=x[ :5]
>>> k
[0, 1, 2, 3, 3]
>>> v=x[5: ]
>>> v
[5.5, 4, 6, 7, 8, 10]
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> for i in n:
	n.append(i)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    n.append(i)
MemoryError
>>> m=[[1,2,3],[4,5,6],[7,8,9]]
>>> for i in n:
	m.append(i)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    m.append(i)
MemoryError
>>> m=[]
>>> for i in n:
	m.append(i)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    m.append(i)
MemoryError
>>> m=[]
>>> for sublist in n:
	for x in sublist:
		m.append(x)

		
Traceback (most recent call last):
  File "<pyshell#44>", line 3, in <module>
    m.append(x)
MemoryError

>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> m=[]
>>> for sublist in n:
	for x in sublist:
		m.append(x)

		
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
