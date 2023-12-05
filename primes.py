"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("must be a positive number")

    prime_list = []
    x = 2

    while len(prime_list) < number_of_primes:
        is_prime = all(x % prime != 0 for prime in prime_list)
        if is_prime:
            prime_list.append(x)
        x += 1

    return prime_list

# Example usage:
try:
    result = primes(10)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
