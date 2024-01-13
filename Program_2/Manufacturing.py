class Manufacturing:
	def __init__(self, raw_material_product, raw_material_ratio, finished_product):
		self.raw_material = raw_material_product
		self.raw_material_ratio = raw_material_ratio
		self.finished_product = finished_product
		self.raw_material_quantity = 0
		self.finished_product_quantity = 0


	def purchase_raw_material(self, purchase_quantity):
		self.raw_material_quantity += purchase_quantity
		print(f"You have purchased {purchase_quantity} {self.raw_material}.")
		print(f"Now you have total of {self.raw_material_quantity} {self.raw_material} quantity.")
		print()


	def produce(self, produce_quantity):
		required_quantity = produce_quantity * self.raw_material_ratio

		if required_quantity > self.raw_material_quantity:  # not enough raw material
			print(f"Not enough raw material available to produce the product, Please do purchase of raw material.")
			print(f"You have {self.raw_material_quantity} {self.raw_material} and still need {required_quantity - self.raw_material_quantity} to produce {produce_quantity} {self.finished_product}")
		else:
			self.finished_product_quantity += produce_quantity  # increase finished product quantity
			self.raw_material_quantity -= required_quantity  # decrease raw material quality
			print(f"Production of {produce_quantity} {self.finished_product} completed.")
			print(f"Now you have {self.finished_product_quantity} {self.finished_product}")

		if self.raw_material_quantity == 0:
			print(f"Your raw material stock is finished, please do purchase.")
		print()


	def display_raw_material_stock(self):
		# print(f"{'=' * 60}")
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Raw Product', 'Raw Product Quantity'))
		print(f"{'=' * 60}")
		print("{:<10}{:<25}{:<25}".format('1', self.raw_material, self.raw_material_quantity))
		print()


	def display_finished_product_stock(self):
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Finished Product', 'Finished Product Quantity'))
		print(f"{'=' * 60}")
		print("{:<10}{:<25}{:<25}".format('1', self.finished_product, self.finished_product_quantity))
		print()


	def print_details(self):
		print(f"Raw Material Product Name: {self.raw_material}")
		print(f"Raw Material Ratio: {self.raw_material_ratio}")
		print(f"Final Product Name: {self.finished_product}")
		print()
