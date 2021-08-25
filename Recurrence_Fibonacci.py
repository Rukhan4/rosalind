"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs 
(instead of only 1 pair).

Create two variables: one for the old bunny and one for the baby bunny
Each will have a value of 1. This is the first two numbers in our sequence.
Loop over the number of months in the given input, minus 1 — we have already had the values for the first month.
Assign new values to the baby bunny and big bunny variables.
The baby bunny becomes a big bunny and so is given a new value corresponding to the number of old bunnies
The big bunny value is now the number of big bunnies + the number of baby bunnies, multiplied by the offspring input.

""" 
import sys

def recurrence(months, offspring):
    # n = months
    # k = offsprings
    BabyBunny, BigBunny = 1,1
    if months <=2: #Takes 1 month for a bunny pair to mature to produce offspring, month 1 = 1 pair, month 2 = 1 pair, month 3 = month 2 * offspring and so on
        return 1
    else:
        for _ in range(months-1):
            # a,b = a, b+a -- modified because increment depends on the number of offspring each month of bunny pairs produce
            BabyBunny, BigBunny = BigBunny, BigBunny + (BabyBunny * offspring)
        return BabyBunny


#print(recurrence(5,3))

if __name__ == "__main__":

    with open(sys.argv[1]) as inpfile:
        digits = inpfile.readline().split()
        n,k = [int(i) for i in digits]
        # n = int(digits[0])
        # k = int(digits[1])
    print(recurrence(n,k))



# Mimic program using dynamic programming 

# FibArray = [0, 1] -- storage method for Dynamic Programming
# Dynamic Programming is an algorithmic method applying solutions to larger and larger cases to inductively solve a problem.
# The small solutions are stored in a List that is built as the algorithm grows and can be called for a solution

# def fibonacci(n):

#     if n <= len(FibArray):
#         return FibArray[n - 1]
#     else:
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
