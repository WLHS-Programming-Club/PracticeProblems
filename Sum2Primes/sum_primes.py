import math


def is_prime(number):
    upper_bound = int((math.sqrt(number)))
    if number == 1: return False
    if number == 2:
    	return True
    for i in range(2, upper_bound+1):
    	if number % i == 0:
    		return False
    return True

Q = int(input())


for i in range(Q):
    string = input().split(" ")
    A = int(string[0])
    B = int(string[1])
    sum = 0
    for i in range(A,B+1):
        if is_prime(i):
            sum = sum+i
    print(sum)
