def primes(limit):
    if limit < 2:
        return []
    
    numbers = set()
    for number in range(2,limit + 1):
        numbers.add(number)
    
    not_primes = set()
    for number in numbers:
        if number in not_primes:
            continue
        multiple = number * 2
        while multiple <= limit:
            not_primes.add(multiple)
            multiple += number
    
    prime_numbers = list(numbers.difference(not_primes))
    prime_numbers.sort()

    return prime_numbers