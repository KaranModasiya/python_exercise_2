from Program_3.InventoryManagement import InventoryManagement
obj = InventoryManagement()
while True:
	print(f"{'-'*35}Menu{'-'*35}")
	print(f"1. Purchase Product")
	print(f"2. Sell Product")
	print(f"3. View Stock Value")
	print(f"4. Exit")
	choise = input(("Enter Your choise: "))

	if choise == '1':
		quantity_to_purchase = int(input(f"How many product quantity do you want to purchase? : "))
		obj.do_purchase(quantity_to_purchase)
	elif choise == '2':
		quantity_to_sell = int(input(f"How many product quantity do you want to sell? : "))
		obj.do_sale(quantity_to_sell)
	elif choise == '3':
		obj.display_stock()
	elif choise == '4':
		print("Thank you!")
		break
	else:
		print("Invalid Input please try again.")
