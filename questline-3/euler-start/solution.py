def problem1(limit=1000):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)
print("Answer for problem 1:", problem1())

#2
def problem2(limit=4000000):
    """Finds the sum of even Fibonacci numbers not exceeding limit."""
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
print("Answer for problem 2:", problem2())

