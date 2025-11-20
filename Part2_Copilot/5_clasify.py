# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:

def describe_number(n):
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else: 
        return "negative"
num = float(input("Enter a number: "))
m= describe_number(num)
print(m)