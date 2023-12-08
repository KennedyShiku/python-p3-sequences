# sequences.py

def print_fibonacci(length):
    if length == 0:
        print('[]')
    elif length == 1:
        print('[0]')
    else:
        fib_sequence = [0, 1]
        for i in range(2, length):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(f'[{", ".join(map(str, fib_sequence))}]')
