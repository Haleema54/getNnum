'''
5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
program:
# Input: Read the number of elements in the tuple
n = int(input())

# Input: Create a tuple by reading n elements from the user
elements = tuple(int(input()) for _ in range(n))

# Calculate the maximum value in the tuple
max_value = max(elements)

# Output: Print the maximum value
print(max_value)
'''
