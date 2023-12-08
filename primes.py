"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("must be apositive number")

    list = []
    num = 2

    while len(list) < number_of_primes:
        isp = all(num % prime != 0 for prime in list)
        if isp:
            list.append(num)
        num += 1

    return list


try:
    result = primes(10)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

