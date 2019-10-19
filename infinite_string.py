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

def insert_chars(sequence):
    global chars_used
    x_list = []
    # print(sequence)
    for i in range(len(chars_used)):
        x_list.append(sequence + chars_used[i])
    return x_list
    
def update_sequence(current_sequences):
    global B
    # print(sequence)
    new_sequences = []
    for i in range(len(current_sequences)):
        x_list = insert_chars(current_sequences[i])
        new_sequences.extend(x_list)
    del current_sequences
    return new_sequences

tests = get_number()

for i in range(tests):
    B = get_number()
    X = get_number()
    
    chars_used = [str(chr(97 + i)) for i in range(B)]
    current_sequences = chars_used.copy()
    ans = ""
    while (len(ans)) < X:
        for i in range(len(current_sequences)):
            ans += current_sequences[i]
        current_sequences = update_sequence(current_sequences)
        # print(current_sequences)
    
    print(ans[X])
    
# for i in range(tests):
