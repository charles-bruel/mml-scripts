#4A) There are ten numbers less than 1200 that are the product of exactly 4 distinct primes. 
#Compute a positive integer solution of x2 − x = N , where N is one of those ten numbers.

import itertools
import math

#Primes from 1-200
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

max_N = 1200
num_facs = 4
must_be_distinct = True

max_prime_value = 1
for i in range(0, num_facs-1):
    if must_be_distinct:
        max_prime_value *= primes[i]
    else:
        max_prime_value *= primes[0]

#The largest number, assuming everything else is smallest, that's still less than N
max_prime_value = max_N / max_prime_value
max_prime_index = 0
for i in range(0, len(primes)):
    if primes[i] > max_prime_value:
        break
    max_prime_index = i

usable_primes = primes[0:max_prime_index+1]
if must_be_distinct:
    result = itertools.combinations(usable_primes, num_facs)
else:
    result = itertools.product(usable_primes, repeat=num_facs)

canidates = 0
tested_numbers = []
for x in result:
    N = 1
    for y in x:
        N *= y
    if N > max_N:
        continue
    if N in tested_numbers:
        continue
    tested_numbers.append(N)
    canidates += 1
    #construct quadratic for x^2-x=N
    a = 1
    b = -1
    c = -N

    d = (b**2) - (4*a*c)
    #We take the larger, as we want the positive one
    sol = (-b+math.sqrt(d))/(2*a)
    if sol.is_integer():
        print(str(int(sol)) + " => " + str(N) + ": " + str(x))
    else:
        print("No solution => " + str(N) + ": " + str(x))

print("Num canidates: " + str(canidates))
