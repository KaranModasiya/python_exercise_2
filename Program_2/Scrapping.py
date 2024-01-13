from Program_2.Manufacturing import Manufacturing

class Scarpping(Manufacturing):
	def __init__(self, raw_material_product_name, raw_material_ratio_quantity, final_product_name):
		super().__init__(raw_material_product_name, raw_material_ratio_quantity, final_product_name)

	def scrap_raw_material(self, scrap_raw):
		if scrap_raw > self.raw_material_quantity:  # cheacks if raw material is not enough
			print(f"Cannot scrap raw material quantity more than available quantity.")
		else:  # reduces raw material quantity by a given value
			self.raw_material_quantity -= scrap_raw
			print(f"{scrap_raw} {self.raw_material} scrapped.")
		print()

	def scrap_finished_product(self, scrap_finished):
		if scrap_finished > self.finished_product_quantity:  # cheacks if finished product is not enough
			print(f"Cannot scrap finished product quantity more than available quantity.")
		else:  # reduces finished product quantity by a given value
			self.finished_product_quantity -= scrap_finished
			print(f"{scrap_finished} {self.finished_product} scrapped.")
		print()


