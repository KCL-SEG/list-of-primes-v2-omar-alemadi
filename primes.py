"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        print("Error: must be a positive number")
        return []

    list = []
    x = 2

    while len(list) < number_of_primes:
        if all(x % prime != 0 for prime in list):
            list.append(x)
        x += 1

    return list

# Example usage:
result = primes(10)
print(result)
