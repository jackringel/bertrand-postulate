# Graph "prime density" between a number and its double up to a given n
# i.e. every n >=1 has some number of primes n < {p} <= 2n, size{p} >= 1
# Give an n and construct that graph up to that n

# Construct list of primes up to 2n
# Array from 1 to n
# For each number, count number of primes > n and <= 2n
# Create new array with number
# Graph
import matplotlib.pyplot as plt
import math

def main():
    n = int(input("Graph up to: "))
    xvals, yvals = solve(n)
    plt.scatter(xvals, yvals)
    plt.show()

def solve(n):
    xvals = [i+1 for i in range(n)]
    primes = get_primes(2*n)
    yvals = []
    for x in xvals:
        k = 0
        j = 0
        while primes[k] <= 2*x:
            if primes[k] > x:
                j+=1
            k+=1
            if k >= len(primes):
                break
        yvals.append(j)
        if not j:
            print("COUNTEREXAMPLE AT " + x)
    return xvals, yvals

def get_primes(n):
    primes = [2]
    for i in range(3, n+1):
        prime = True
        k = 0
        while primes[k] <= math.sqrt(i):
            if not i%primes[k]:
                prime = False
                break
            k+=1
        if prime:
            primes.append(i)
    return primes

if __name__ == '__main__':
    main()
