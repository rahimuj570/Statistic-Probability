size=int(input('Insert size of X or Y :'))
x=[]
y=[]


def mean(li):
    mean=0
    for i in li:
        mean+=i
    mean/=size
    print('mean=',mean)
    return mean

def xyMean(x,y):
    res=0
    for i in range(size):
        res+=(x[i]*y[i])
    res/=size
    print('xymean',res)
    return res

def xSqrMean(x):
    res=0
    for i in x:
        res+=(i*i)
    res=res/size
    print('sqrmean',res)
    return res

def calc(givenFlag,x,y):
    m=(mean(x)*mean(y)-xyMean(x,y))/((mean(x)**2)-xSqrMean(x))
    c=mean(y)-m*mean(x)
    print(m,'fffffff',c)
    if(givenFlag=='Y'):
        given = float(input("Insert value of \"X\" : "))
        res=m*given+c
    else:
        given = float(input(f"Insert value of \"Y\" : "))
        res=(given-c)/m
    print("ANSWERE: ",res)

for i in range(0,int(size)):
    print(f'Insert {i+1} number of value of "X" : ')
    x.append(int(input()))

for i in range(0,int(size)):
    print(f'Insert {i+1} number of value of "Y" : ')
    y.append(int(input()))

question=input("Which value you want to find X or Y?\n \t X : 1 || Y : 2 ")
match question:
    case '1':
        calc('X',x,y)
    case '2':
        calc('Y', x, y)
    case _:
        print('Wrong Input')