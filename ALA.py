print("Grocery Billing")

items = ("Rice","Sugar","Oil")
price = [50,40,120]
name = input("Enter item: ")
qty =int  (input("Enter quantity: ") )

index = items.index(name)

if price[index] * qty > 0:
  total = price[index] * qty
else:
     total = 0
print("Total:",  total)
for i in range(3) :
 print("Billed")
print("Exit")
