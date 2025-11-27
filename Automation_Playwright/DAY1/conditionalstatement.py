age=int(input("Enter your age: "))
if age>=18:
    print("your egiable to vote")
else:
    print("your not egiable to vote")

price = int(input("Enter the price of the item: "))
discount = 0

if price == 1000:
    discount = price * 0.1
elif price >= 500 and price < 1000:
    discount = price * 0.05
elif price >= 100 and price < 500:
    discount = price * 0.02
else:
    discount = price * 0.5
final_price = price - discount
print(f"You get a discount of {discount}. The final price is {final_price}.")
