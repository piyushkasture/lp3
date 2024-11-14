def fibonacci(n):
    fib_sequence = [0, 1]
    steps = 0

    if n <= 0:
        return "Invalid input. n should be a positive integer."

    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        steps += 1

    return fib_sequence, steps

n = int(input("Enter the value of n: "))
result, step_count = fibonacci(n)
print(f"Fibonacci Sequence (first {n} numbers): {result}")
print(f"Total Steps: {step_count}")