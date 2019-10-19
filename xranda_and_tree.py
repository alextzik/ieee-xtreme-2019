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

node_count = get_number()

cost = numpy.zeros((node_count, node_count))
cost = cost.astype(int)
sum = 0

for i in range (0, node_count - 1):
	parent = get_number()
	child = get_number()
	weight = get_number()
	cost[parent - 1][child - 1] = weight
	cost[child - 1][parent - 1] = weight

for u in range (0, node_count):
     for v in range (0, node_count):
         cost[u][v] = max(cost[int(numpy.floor(u/2)), v], cost[int(numpy.floor(u/2)), u], cost[u][v])
         if v < u:
            sum += cost[u][v]


#1300

res = int(sum) % (10**9 + 7)
print(res)
