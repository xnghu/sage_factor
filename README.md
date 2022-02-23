# sage_factor
python terminal program that uses Lenstra's Elliptic Curve Method, along with the Miller-Rabin primality test, to factor the input number.

## Lenstra:
The Lenstra elliptic-curve factorization or the elliptic-curve factorization method (ECM) is a fast, sub-exponential running time, algorithm for integer factorization, which employs elliptic curves. For general-purpose factoring, ECM is the third-fastest known factoring method. The second-fastest is the multiple polynomial quadratic sieve, and the fastest is the general number field sieve. The Lenstra elliptic-curve factorization is named after Hendrik Lenstra.

Practically speaking, ECM is considered a special-purpose factoring algorithm, as it is most suitable for finding small factors. Currently, it is still the best algorithm for divisors not exceeding 50 to 60 digits, as its running time is dominated by the size of the smallest factor p rather than by the size of the number n to be factored. Frequently, ECM is used to remove small factors from a very large integer with many factors; if the remaining integer is still composite, then it has only large factors and is factored using general-purpose techniques. The largest factor found using ECM so far has 83 decimal digits and was discovered on 7 September 2013 by R. Propper.[1] Increasing the number of curves tested improves the chances of finding a factor, but they are not linear with the increase in the number of digits.

## Miller-Rabin
he Miller–Rabin primality test or Rabin–Miller primality test is a probabilistic primality test: an algorithm which determines whether a given number is likely to be prime, similar to the Fermat primality test and the Solovay–Strassen primality test.

It is of historical significance in the search for a polynomial-time deterministic primality test. Its probabilistic variant remains widely used in practice, as one of the simplest and fastest tests known.

Gary L. Miller discovered the test in 1976; Miller's version of the test is deterministic, but its correctness relies on the unproven extended Riemann hypothesis.[1] Michael O. Rabin modified it to obtain an unconditional probabilistic algorithm in 1980.
