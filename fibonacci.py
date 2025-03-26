from functools import lru_cache

'''
Write a function to return nth term of fibonacci function
'''

# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for n in range(1, 11):
#     print(n, ":", fibonacci(n))

'''
fibonacci cache function
'''
# fibonacci_cache = {}
# def fibonaccicache(n):
#     # If we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     # Compute the nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonaccicache(n - 1) + fibonaccicache(n - 2)
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
#
# for n in range(1, 1001):
#     print(n, ":", fibonaccicache(n))


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # If we have cached the value, then return it
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 501):
    print(fibonacci("abc"))