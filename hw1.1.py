#Задача 1: Калькулятор чайових з урахуванням знижки

number_of_dishes = int(input("Hello, please, enter the number of dishes you ordered: "))
initial_total_price = 0
price_of_dishes = []
for i in range(number_of_dishes):
        price_of_dishes = float(input(f"Enter a price of a dishes: {i + 1}) "))
        initial_total_price += price_of_dishes



if initial_total_price > 2000:
       discount_total_price = initial_total_price - (initial_total_price/100 * 10)
       print(f"Price with discount {discount_total_price}")

else:
        discount_total_price = initial_total_price
        print(f"Price {discount_total_price}")

tips = int(input("Please enter a tips - 10%, 15% or 20%: "))

tips_amount =  tips/100 * discount_total_price

print(f"Tips amount: {tips_amount}")
print(f"Tips amount + total price:  {tips_amount+discount_total_price}")


