# Question:
# Given a string S, print 'yes' if it has a vowel in it else print 'no'.

# Sample Input:
# codekata

# Sample Output:
# yes

s = input()
vowels = {'a','e','i','o','u','A','E','I','O','U'}
if any(char in vowels for char in s):
    print("yes")
else:
    print("no")
