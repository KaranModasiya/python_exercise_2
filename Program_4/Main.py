from Program_4.InventoryManagement import InventoryManagement
obj = InventoryManagement()

while True:
	print()  # for extra space in output
	print(f"{'-'*35}Menu{'-'*35}")
	print(f"1. Purchase Product")
	print(f"2. Sell Product")
	print(f"3. View Stock Value")
	print(f"4. Show Valuation")
	print(f"5. Exit")
	choice = input(("Enter Your choice: "))
	print()  # for extra space in output

	if choice == '1':
		quantity = int(input(f"Quantity of product? : "))
		price = int(input(f"Price of product? : "))
		obj.do_purchase(price, quantity)
	elif choice == '2':
		quantity = int(input(f"How many product quantity do you want to sell? : "))
		obj.do_sale(quantity)
	elif choice == '3':
		obj.display_products()
	elif choice == '4':
		obj.do_valuation()
	elif choice == '5':
		print("Thank you!")
		break
	else:
		print("Invalid Input please try again.")
