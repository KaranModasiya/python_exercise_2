from Program_2.Scrapping import Scarpping

finished_product_name = input("Enter Finished Product Name: ")
raw_material_product_name = input("Enter Raw Material Product Name: ")
raw_material_ratio_quantity = int(input(f"How many {raw_material_product_name} will need to make one {finished_product_name}: "))
print()

# creating new object
obj = Scarpping(raw_material_product_name, raw_material_ratio_quantity, finished_product_name)

while True:
	print(f"{'-'*35}Menu{'-'*35}")
	print(f"1. Purchase Raw Material Product")
	print(f"2. Manufacture Final Product")
	print(f"3. Show Raw Material Quantity")
	print(f"4. Show Final Material Quantity")
	print(f"5. Scrap Raw Material")
	print(f"6. Scrap Finished Product")
	print(f"7. Exit")
	choise = input(("Enter Your choise: "))

	if choise == '1':
		quantity_to_purchase = int(input(f"How many {obj.raw_material} do you want to purchase? : "))
		obj.purchase_raw_material(quantity_to_purchase)
	elif choise == '2':
		quantity_to_produce = int(input(f"How many {obj.finished_product} do you want to manufacture? : "))
		obj.produce(quantity_to_produce)
	elif choise == '3':
		obj.display_raw_material_stock()
	elif choise == '4':
		obj.display_finished_product_stock()
	elif choise == '5':
		scrap_raw = int(input(f"How many {obj.raw_material} do you want to scrap? : "))
		obj.scrap_raw_material(scrap_raw)
	elif choise == '6':
		scrap_finished = int(input(f"How many {obj.finished_product} do you want to scrap? : "))
		obj.scrap_finished_product(scrap_finished)
	elif choise == '7':
		print("Thank you!")
		break
	else:
		print("Invalid Input please try again.")
