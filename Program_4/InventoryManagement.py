class InventoryManagement:
	def __init__(self):
		self.key = 0
		self.products = {}

	# to purchase product
	def do_purchase(self, price, quantity):
		self.key += 1
		subtotal = price * quantity
		sub_product = {'price': price, 'quantity': quantity, 'subtotal': subtotal}
		self.products.update({self.key: sub_product})
		print("Purchase successful.")  # complition message

	# to sale products
	def do_sale(self, sell_quantity):
		total_quantity = sum(map(lambda x: x['quantity'], self.products.values()))

		if total_quantity < sell_quantity:
			# given value is more than available stock quantity
			print(f"Cannot do the fulfillment for the required quantities.")
		else:
			for key, value in self.products.items():
				if value['quantity'] > sell_quantity:  # checks if rquired quantity is available in single product
					value['quantity'] -= sell_quantity  # if available decreases currunt quantity of product
					value['subtotal'] = value['price'] * value['quantity']  # evaluates subtotal as per change
					break
				else:  # if required quantity is not available in single product
					sell_quantity -= value['quantity']  # decreases required quantity by a fulfilled quantity
					value['quantity'] = 0  # sets product quantity to 0

			# removes product from list because quantity is 0
			tuple(map(lambda x: self.products.pop(x[0]) if x[1]['quantity'] == 0 else None, list(self.products.items())))
			# map(lambda x: self.products.pop(x[0]) if x[1]['quantity'] == 0 else None, list(self.products.items()))
			# not working same pop funtion in map function
			# not working without type-casting
			print("Sell complete.")  # complition message

	# for showing valuation
	def do_valuation(self):
		valuation = 0
		if len(self.products) > 0:  # if product is available in stock
			total_quantity = sum(map(lambda x: x['quantity'], self.products.values()))
			total_subtotal = sum(map(lambda x: x['subtotal'], self.products.values()))
			valuation = total_subtotal / total_quantity

		print("Valuation is: {:.2f}".format(valuation))

	# display all products
	def display_products(self):
		for key, value in self.products.items():
			print(f"No.{key} -> product: {value}")

		if len(self.products) <= 0:
			print("No products are available to show. Please do purchase new products.")

