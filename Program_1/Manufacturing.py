class Manufacturing:

	def __init__(self, raw_material_product_name, raw_material_ratio_quantity, final_product_name):
		self.raw_material_product_name = raw_material_product_name
		self.raw_material_ratio_quantity = raw_material_ratio_quantity
		self.final_product_name = final_product_name
		self.raw_material_quantity = 0
		self.finished_product_quantity = 0


	def purchase_raw_material(self, quantity_to_purchase):
		self.raw_material_quantity += quantity_to_purchase
		print(f"You have purchased {quantity_to_purchase} {self.raw_material_product_name}.")
		print(f"Now you have total of {self.raw_material_quantity} {self.raw_material_product_name} quantity.")
		print()


	def produce(self, quantity_to_produce):
		required_quantity = quantity_to_produce * self.raw_material_ratio_quantity

		if required_quantity > self.raw_material_quantity:  # not enough raw material
			print(f"Not enough raw material available to produce the product, Please do purchase of raw material.")
			print(f"You have {self.raw_material_quantity} {self.raw_material_product_name} and still need {required_quantity-self.raw_material_quantity} to produce {quantity_to_produce} {self.final_product_name}")
		else:
			self.finished_product_quantity += quantity_to_produce  # increase finished product quantity
			self.raw_material_quantity -= required_quantity  # decrease raw material quality
			print(f"Production of {quantity_to_produce} {self.final_product_name} completed.")
			print(f"Now you have {self.finished_product_quantity} {self.final_product_name}")

		if self.raw_material_quantity == 0:
			print(f"Your raw material stock is finished, please do purchase.")

		print()


	def display_raw_material_stock(self):
		# print(f"{'=' * 60}")
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Raw Product', 'Raw Product Quantity'))
		print(f"{'=' * 60}")
		print("{:<10}{:<25}{:<25}".format('1', self.raw_material_product_name, self.raw_material_quantity))
		print()


	def display_finished_product_stock(self):
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Finished Product', 'Finished Product Quantity'))
		print(f"{'=' * 60}")
		print("{:<10}{:<25}{:<25}".format('1', self.final_product_name, self.finished_product_quantity))
		print()


	def print_details(self):
		print(f"Raw Material Product Name: {self.raw_material_product_name}")
		print(f"Raw Material Ratio: {self.raw_material_ratio_quantity}")
		print(f"Final Product Name: {self.final_product_name}")
		print()
