import math
from bitarray import bitarray

class Sieve:
    def __init__(self) -> None:
        self.primes = []
        self.current_max = 1  # Tracks the highest number sieved so far

    def _estimate_upper(self, n: int) -> int:
        if n <= 5:
            return 15  # Precomputed for small n
        log_n = math.log(n)
        log_log_n = math.log(log_n) if log_n > 1 else 0
        upper = n * (log_n + log_log_n)
        return int(upper * 1.15) + 1  # adding a buffer of 10-15% here

    def _generate_primes(self, high_limit: int) -> list[int]:
        if high_limit < 2:
            return []
        is_prime = bitarray(high_limit + 1)
        is_prime.setall(True)
        is_prime[0] = is_prime[1] = False

        max_prime_needed = math.isqrt(high_limit)
        existing_primes = [p for p in self.primes if p <= max_prime_needed]

        # Marking multiples of existing primes
        for p in existing_primes:
            start = p * p
            if start > high_limit:
                continue
            is_prime[start::p] = False

        # Sieving remaining numbers up to maximum prime numbers rangee
        start_p = 2
        if existing_primes:
            start_p = existing_primes[-1] + 1
        for p in range(start_p, max_prime_needed + 1):
            if is_prime[p]:
                start = p * p
                if start > high_limit:
                    continue
                is_prime[start::p] = False

        new_primes = [i for i, is_p in enumerate(is_prime) if is_p]
        return new_primes

    def nth_prime(self, n: int) -> int:
        if n < 0:
            raise ValueError("Index must be non-negative.")
        if n == 0:
            return 2
        
        while len(self.primes) <= n:
            upper_limit = self._estimate_upper(n)
            if upper_limit <= self.current_max:
                # If estimation is too low, incrementally adjust
                upper_limit = self.current_max * 2
            new_primes = self._generate_primes(upper_limit)
            self.primes = new_primes  
            self.current_max = upper_limit
        
        return self.primes[n]