def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n ==2:
        return[0,1]
    else:
        fib_sequence = [0,1]
        while n > len(fib_sequence):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
            print(fib_sequence)
        # print(fib_sequence[-1])

fibonacci(10)