#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémente n pour éviter une boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <positive_integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Negative number")
    except ValueError:
        print("Please provide a valid positive integer.")
        sys.exit(1)

    f = factorial(num)
    print(f)

