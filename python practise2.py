Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[1,2,3,4,5,6]
>>> letters=["a","b","c","d"]
>>> 2 in numbers
True
>>> 8 in numbers
False
>>> "c" in letters
True
>>> "e" in letters
False
>>> numbers*3
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> numbers+letters
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
>>> fruits=["cherries","kiwi","lemon","berries","guava"]
>>> fruits.append("apple")
>>> fruits
['cherries', 'kiwi', 'lemon', 'berries', 'guava', 'apple']
>>> fruits.extend(["peach","avocado"])
>>> fruits
['cherries', 'kiwi', 'lemon', 'berries', 'guava', 'apple', 'peach', 'avocado']
>>> fruits.pop()
'avocado'
>>> fruits
['cherries', 'kiwi', 'lemon', 'berries', 'guava', 'apple', 'peach']
>>> fruits.remove("lemon")
>>> fruits
['cherries', 'kiwi', 'berries', 'guava', 'apple', 'peach']
>>> fruits
['cherries', 'kiwi', 'berries', 'guava', 'apple', 'peach']
>>> fruits.reverse()
>>> fruits
['peach', 'apple', 'guava', 'berries', 'kiwi', 'cherries']
>>> fruits.sort
<built-in method sort of list object at 0x015AD198>
>>> fruits.sort()
>>> fruits
['apple', 'berries', 'cherries', 'guava', 'kiwi', 'peach']
>>> fruits.reverse()
>>> fruits
['peach', 'kiwi', 'guava', 'cherries', 'berries', 'apple']
>>> fruits.append("cherries")
>>> fruits.append("guava")
>>> fruits.append("berries")
>>> fruits
['peach', 'kiwi', 'guava', 'cherries', 'berries', 'apple', 'cherries', 'guava', 'berries']
>>> fruits.count("guava")
2
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> sum(numbers)
21
>>> max(numbers)
6
>>> min(numbers)
1
>>> max(fruit)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    max(fruit)
NameError: name 'fruit' is not defined
>>> max(fruits)
'peach'
>>> min(fruits)
'apple'
>>> sum(fruits)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> fruits.index()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    fruits.index()
TypeError: index() takes at least 1 argument (0 given)
>>> fruits[0]
'peach'
>>> fruits[2]
'guava'
>>> fruits[4]
'berries'
>>> numbers[1]
2
>>> numbers[3]
4
>>> numbers[5]
6
>>> numbers[-1:-4]
[]
>>> fruits[3:]
['cherries', 'berries', 'apple', 'cherries', 'guava', 'berries']
>>> numbers[ : -2]
[1, 2, 3, 4]
>>> fruits[-5:-2]
['berries', 'apple', 'cherries']
>>> numbers[-4:-1]
[3, 4, 5]
>>> for item in list:
	do something with(item)
	
SyntaxError: invalid syntax
>>> for fruit in fruits:
	print(fruit)

	
peach
kiwi
guava
cherries
berries
apple
cherries
guava
berries
>>> for car in fruits:
	print(car)

	
peach
kiwi
guava
cherries
berries
apple
cherries
guava
berries
>>> for number in numbers:
	print(number)

	
1
2
3
4
5
6
>>> for number in numbers:
	print(number*10)

	
10
20
30
40
50
60
>>> for number in numbers:
	print(number**2)

	
1
4
9
16
25
36
>>> x=range(5,15)
>>> x
range(5, 15)
>>> for n in x:
	print(n)

	
5
6
7
8
9
10
11
12
13
14
>>> x=range(9,19)
>>> x
range(9, 19)
>>> for n in x:
	print(n*5)

	
45
50
55
60
65
70
75
80
85
90
>>> stars=[number*number for number in numbers]
>>> 
>>> stars
[1, 4, 9, 16, 25, 36]
>>> doubles=[number*2 for number in numbers]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> e=[]
>>> e
[]
>>> for number in numbers:
	x=number*2
	e.append(x)

	
>>> e
[2, 4, 6, 8, 10, 12]
>>> e=doubles
>>> 
>>> e==doubles
True
>>> m=[100,200,300,400,500]
>>> m
[100, 200, 300, 400, 500]
>>> m/7
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    m/7
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> for number in numbers:
	p=m/
	
SyntaxError: invalid syntax
>>> remainder=[numbers/numbers for number in numbers]
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    remainder=[numbers/numbers for number in numbers]
  File "<pyshell#98>", line 1, in <listcomp>
    remainder=[numbers/numbers for number in numbers]
TypeError: unsupported operand type(s) for /: 'list' and 'list'
>>> m=[100,200,300,400,500]
>>> m
[100, 200, 300, 400, 500]
>>> double=[p%7 for p in m]
>>> 
>>> double
[2, 4, 6, 1, 3]
>>> square=[p%7 for p in m]
>>> square
[2, 4, 6, 1, 3]
>>> c=[]
>>> for p in m:
	a=p%7
	c.append(a)

	
>>> c
[2, 4, 6, 1, 3]
>>> c=range(70,90)
>>> c
range(70, 90)
>>> [x*2 of x in c]
SyntaxError: invalid syntax
>>> [x*2 for x in c]
[140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178]
>>> for x in c:
	print(x*2)

	
140
142
144
146
148
150
152
154
156
158
160
162
164
166
168
170
172
174
176
178
>>> 
