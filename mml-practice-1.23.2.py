#2A) If phactor means to write as a sum of positive integers, the phactorization of an integer would not be
#unique. In how many different ways could 6 be phactored, if the order of the terms is irrelevant, i.e., 
#1 + 2 + 3, 1 + 3 + 2, and 3 + 2 + 1 are not considered different

#Addendum: This problem is the partition problem, and solutions are described in OEIS A000041
#                                                                                https://oeis.org/A000041

import itertools
import math

to_phactor = 6

smaller_ints = []
ints_amount = []

for i in range(1, to_phactor + 1):
    smaller_ints.append(i)
    max_quant = math.floor(to_phactor/i)
    ints_amount.append([])
    for j in range(0, max_quant + 1):
        ints_amount[i-1].append(j)

result = itertools.product(*ints_amount)
count = 0
for x in result:
    accum = 0
    for i in range(0, to_phactor):
        accum += (i + 1) * x[i]
    if accum == to_phactor:
        count += 1
        to_print = []
        for i in range(0, to_phactor):
            to_print += [i + 1] * x[i]
        print(to_print)
print("TOTAL: " + str(count))
