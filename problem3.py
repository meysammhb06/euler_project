def largest_prime_factor(n):
    factor = 2
    # Continue dividing n by factors until factor squared is greater than n
    while factor * factor <= n:
        # If n is divisible by factor, divide it by factor
        if n % factor == 0:
            n //= factor
        else:
            # If not divisible, move to the next possible factor
            factor += 1
    return n

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor:", result)
