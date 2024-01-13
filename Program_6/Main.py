import csv
data = dict()
with open('file.csv', mode='r') as file:
	csv_file = csv.reader(file)
	# print(list(csv_file)[0])

	for line in list(csv_file)[1:]:
		tmp_dict = {'Name': line[1], 'Address 1': line[5], 'Address 2': line[6], 'City': line[8], 'Country': line[9], 'Zipcode': line[7]}
		data.update({line[0]: {'customer': tmp_dict}})
		data.update({line[0]})  # .append({'SKU': line[2], 'Price': line[4], 'Quantity': line[3]})

for key, val in data.items():
	print(f"key: {key}")
	for k, v in val.items():
		print(k, v)
print(data)
# print(data)

# index sku-2, qty-3 price-4
