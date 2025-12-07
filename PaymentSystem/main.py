from payment_methods import Mpesa, Card, PayPal
from checkout import checkout


print("=== MINI PAYMENT SYSTEM ===")

print("Choose payment method:")
print("1. M-Pesa")
print("2. Card")
print("3. PayPal")
print("4. Exit")

choice = input("Enter choice(Option 4 to exit): ")
if choice == "4":
    exit()
amount = float(input("Enter amount: "))

if choice == "1":
    method = Mpesa()
elif choice == "2":
    method = Card()
elif choice == "3":
    method = PayPal()
else:
    print("Invalid option!")
    exit()

checkout(method, amount)