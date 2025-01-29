# BHE Software Engineer Coding Exercise

## The Sieve of Eratosthenes

This project implements an API to retrieve the Nth prime number using 0-based indexing, where the 0th prime number is 2. The implementation is optimized beyond the traditional Sieve of Eratosthenes, incorporating dynamic upper-bound estimation and efficient sieving techniques to handle large inputs efficiently.

### Implementation Details 
-The solution is implemented in Python.  

-It dynamically estimates the upper bound needed to find the Nth prime using logarithmic approximation, ensuring efficient memory and computation usage.  

-A bit-array-based sieve is used to mark primes, significantly reducing space complexity compared to traditional boolean lists.  

-The algorithm is optimized to reuse previously computed primes for faster sieving in cases where additional primes are needed.


### Installation & Setup  

To set up the environment and run tests:  

1. **Install dependencies**  
   ```sh  
   pip install -r python/requirements.txt  

1. **Run test cases**  
   ```sh  
   cd python
   python -m unittest python/test_sieve.py  

### Additional Considerations

-The implementation adheres to the requirement that - f(0)=2, f(19)=71, f(99)=541, ..., f(10000000)=179424691 , f(100000000)=2038074751  

-Additional test cases have been added to further validate the correctness and efficiency of the implementation.  

-The algorithm successfully computes the 10⁸th prime number, but this test takes approximately 70 seconds on my system. If you prefer a faster test run, you may comment out this test case in test_sieve.py. The rest of the test cases execute relatively quickly

