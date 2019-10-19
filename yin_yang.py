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
import random

def pick_letter(i):
    mu, sigma = 1.2, 2.5  # mean an d standar d deviation
    x = numpy.random.normal(mu, sigma, 1)
    if i==1:    
        if x<=0.5:
            return "y"
        else:
            return "Y"
    else:
        if x<0.3:
            return "Y"
        else:
            return "y"
        
    
n = get_number()
result=""

for i in range(n):
    result+=pick_letter(i%2)

print(result)
