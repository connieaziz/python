def list():
    m=[100,110,120,130,140,150] 
    for p in m:
        print(p%3)

def sorted():
    a=['apple', 'banana', 'mango']
    b=['avocado', 'peach', 'orange']
    c=['pineapple', 'lemon']
    d=set(a+b+c)
    print(d)

def divisible_by_three():
    number=range(1,n/3)
    sum_number=sum(number)
    print(sum_number)

def function():
    x=[[1,2],[3,4],[5,6]]
    y=[1,2,3,4,5,6]
    print(y)

def smallest():
    a=[1,3,6,8,2,4,5,7]
    print(min(a))

def duplicate():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    print('a','b','c','d','e','f','g','h')

def squares():
    h=dict()
    j=range(149,159)
    for x in j:
        h[x]=x**2
    return(h)

def print_dict():
    students=[{'age':19, 'name':'Eunice'}, {'age':21, 'name':'Agnes'}, {'age':18, 'name':'Teresa'}, {'age':22, 'name':'Asha'}]
    for student in students:
        print("Hello {}, you were born in year {}.".format(student['name'],student['year']))
