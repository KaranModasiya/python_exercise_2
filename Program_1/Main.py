from Program_1.Manufacturing import Manufacturing

finished_product_name = input("Enter Finished Product Name: ")
raw_material_product_name = input("Enter Raw Material Product Name: ")
raw_material_ratio_quantity = int(input(f"How many {raw_material_product_name} will need to make one {finished_product_name}: "))
print()

# creating new object
obj = Manufacturing(raw_material_product_name, raw_material_ratio_quantity, finished_product_name)

while True:
	print(f"{'-'*35}Menu{'-'*35}")
	print(f"1. Purchase Raw Material Product")
	print(f"2. Manufacture Final Product")
	print(f"3. Show Raw Material Quantity")
	print(f"4. Show Final Material Quantity")
	print(f"5. Exit")
	choise = input(("Enter Your choise: "))

	if choise == '1':
		quantity_to_purchase = int(input(f"How many {obj.raw_material_product_name} do you want to purchase? : "))
		obj.purchase_raw_material(quantity_to_purchase)
	elif choise == '2':
		quantity_to_produce = int(input(f"How many {obj.finished_product_name} do you want to manufacture? : "))
		obj.produce(quantity_to_produce)
	elif choise == '3':
		obj.display_raw_material_stock()
	elif choise == '4':
		obj.display_finished_product_stock()
	elif choise == '5':
		print("Thank you!")
		break
	else:
		print("Invalid Input please try again.")
