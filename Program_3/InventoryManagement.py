class InventoryManagement:
	def __init__(self):
		self.product_quantity = 0

	def do_purchase(self, purchase_quantity):
		self.product_quantity += purchase_quantity
		print("Product stock purchase complete.")
		print()

	def do_sale(self, sell_quantity):
		if self.product_quantity < sell_quantity:
			print("Not enough product quantities to sell, please do purchase first.")
		else:
			self.product_quantity -= sell_quantity
			print("Product stock sell complete.")
			print(f"Remaining stock: {self.product_quantity}")
		print()

	def display_stock(self):
		print(f"Available product stock in inventory: {self.product_quantity}")
		print()

