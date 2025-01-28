class Sieve:
    def __init__(self) -> None:
        self.primes = []
        self.limit = 10
        pass
    def _generate_primes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        self.primes = [x for x in range(limit + 1) if is_prime[x]]

    def nth_prime(self, n: int) -> int:
        while len(self.primes) <= n:
            self.limit *= 2
            self._generate_primes(self.limit)
        
        return self.primes[n]
        pass