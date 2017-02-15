#  Returns either the index of the location in the array or -1 if the array did not contain the targetValue.
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def doSearch(array, targetValue):
    min = 0
    max = len(array) -1
    guess = 0
    counter = 0
    while(min <= max):
        guess = math.floor((max + min)/2)
        counter += 1
        if array[guess] == targetValue:
            print(counter)
            return guess
        elif array[guess] < targetValue:
            min = guess + 1
        else:
            max = guess - 1
    print(guess)
    return -1

result = doSearch(primes, 73)
print("Found prime at index " + repr(result))
