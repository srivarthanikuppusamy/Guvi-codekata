Problem Statement:
Given a number N, check whether it is prime or not. Print 'yes' if it is prime else print 'no'.

Input Description:
The input consists of a single integer N.

Output Description:
The output is 'yes' if N is prime, otherwise 'no'.

Sample Input:
123

Sample Output:
no

import math
n = int(input())

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
        
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

if is_prime(n):
    print("yes")
else:
    print("no")
