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
s = get_number()
A = numpy.zeros(a)
S = numpy.zeros(s)
res = numpy.zeros(a+s)
for i in range(a):
    A[i] = get_number()
for i in range(s):
    S[i] = get_number()

S = sorted(S,reverse = False)
a_index = 0
s_index = 0
for i in range(a+s):
        if s_index == s:
            for k in range(i,len(res)):
                res[k] = A[a_index]
                a_index = a_index + 1
            break
        if a_index == a:
            for k in range(i,len(res)):
                res[k] = S[s_index]
                s_index = s_index + 1
            break
        if S[s_index] < A[a_index]:
            res[i] = S[s_index]
            s_index = s_index + 1
        else:
            res[i] = A[a_index]
            a_index = a_index + 1
ans = ""
for i in range(a+s):
    ans += str(int(res[i])) + " "
print(ans)
