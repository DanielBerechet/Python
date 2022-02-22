# Fibonacci Method 1
# 1. We first define the Fibonacci function: numbers up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end =' ')
        a, b = b, a+b
    print()
# 2. Now we call the function
fib(2000)

# Fibonacci Method 2
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

# 3. Append to list consecutive numbers
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Lambda function