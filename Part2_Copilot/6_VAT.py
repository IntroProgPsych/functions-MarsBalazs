# Write a function apply_vat(price) that returns the price including 19% VAT.
# Ask the user for a price and print the result.

# Write your code here:

def apply_vat(price) :
    return price * 1.19

user_price = float(input("Enter the price: "))
final_price = apply_vat(user_price)
print("Price including VAT:", final_price)
