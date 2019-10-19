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

class Node:

    # Constructor to create a Node
    def __init__(self, data):
        self.key= data
        self.left = None
        self.right = self.parent = None

def insert(root, key):

    node = Node(key)
    x = root
    y = None
    height = 1

    while (x != None):
        y = x
        if (key < x.key):
            x = x.left
        else:
            x = x.right
        height += 1

    if (y == None):
        y = node
    elif (key <= y.key):
        y.left = node
    else:
        y.right = node

    return height


n = get_number()
arr = [0] * n
for i in range(n):
    arr[i] = get_number()

tree = Node(arr[0])
heights = [1]
for i in range(1,n):
    h = insert(tree, arr[i])
    heights.append(h)

ans = ""
for i in range(len(heights)):
    ans += str(heights[i]) + " "
print(ans)
