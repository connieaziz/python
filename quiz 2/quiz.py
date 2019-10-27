def tens():
    x=[1,2,3,4,5,6,7,8,9]
    for n in x:
        print(n*10)

def square():
    square=[number*number for number in range(10)]
    print(square)

def sorted():
        a=[9,1,4,7,3]
        b=[5,2,6,8,0]
        c=set(a+b)
        print(c)

def range_sum(n):
        number=range(1,n+1)
        sum_number=sum(number)
        print(sum_number)

def largest():
        a=[1,3,6,8,2,4,5,7]
        print(max(a))

def smallest():
    a=[1,3,6,8,2,4,5,7]
    print(min(a))

def modules():
    h=dict()
    j=range(10,20)
    for x in j:
        h[x]=x%3
    return (h)

def print_dict():
    students=[{'balance':1000, 'name':'Irene'}, {'balance':2000, 'name':'Pauline'}, {'balance':3000, 'name':'Naima'}, {'balance':1000, 'name':'Rose'}]
    for student in students:
        print("Hello {}, your balance is {}.".format(student['name'],student['balance']))
