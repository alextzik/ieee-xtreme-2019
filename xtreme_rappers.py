# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

a = get_number()
b = get_number()
result=0

if b > a:
    c = a
    a = b
    b = c

if a==0 or b==0:
    res=0
else:
    result=numpy.floor(a/2)
    res=int(min(result, b))
    
    if res==result:
        result=(max(numpy.floor((b-res)/2),0))
        res=res+int(min(result, a-2*res))


print(res)
