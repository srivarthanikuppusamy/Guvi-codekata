# Question:
# Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.

# Sample Input:
# 3
# 2 6

# Sample Output:
# yes

n = int(input())
l, r =map ( int , input().split())


if n >= l and n <= r :
    print("yes")
else:
    print("no")
