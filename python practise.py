Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> a
10
>>> b
20
>>> c='dog'
>>> d='cat'
>>> e=a/3
>>> e
3.3333333333333335
>>> type(a)
<class 'int'>
>>> type(c)
<class 'str'>
>>> type(e)
<class 'float'>
>>> f=str(a)
>>> f
'10'
>>> type(f)
<class 'str'>
>>> g="123"
>>> h=int(g)
>>> type(g)
<class 'str'>
>>> type(h)
<class 'int'>
>>> i=int(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    i=int(c)
ValueError: invalid literal for int() with base 10: 'dog'
>>> print("Hello Akirachix")
Hello Akirachix
>>> print("Hello Akirachix.\n class of 2019")
Hello Akirachix.
 class of 2019
>>> print("Hello Akirachix.\n class of 2019.")
Hello Akirachix.
 class of 2019.
>>> print("Hello Akirachix.\t class of 2019.")
Hello Akirachix.	 class of 2019.
>>> print("Hello Akirachix.\b class of 2019.")
Hello Akirachix. class of 2019.
>>> first="Connie"
>>> last="Antonnette"
>>> gretings="Hello,{}{}".format(first,last)
>>> print(greetings)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(greetings)
NameError: name 'greetings' is not defined
>>> gretings="Hello, {} {}".format(first,last)
>>> print(greetings)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(greetings)
NameError: name 'greetings' is not defined
>>> print(gretings)
Hello, Connie Antonnette
>>> code="ABC123"
>>> amount=1000
>>> recepient="0721000000"
>>> print("code confirmed ! Hi James.\n you have sent amount to recepient.")
code confirmed ! Hi James.
 you have sent amount to recepient.
>>> greetings="{} {} confirmed!". Hi format(first),.\n you have sent ksh {} {} tto {} {}
SyntaxError: invalid syntax
>>> greetings="{} confirmed! Hi format(first),.\n you have sent ksh {}.\n to {}.
SyntaxError: EOL while scanning string literal
>>> greetings="{} confirmed! Hi {}.\n you have sent ksh {}.\n to recepient {}".format(code,first,amount,recepient,amount)
>>> print(greetings)
ABC123 confirmed! Hi Connie.
 you have sent ksh 1000.
 to recepient 0721000000
>>> 
