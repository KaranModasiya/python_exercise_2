import csv

data = dict()
with open('file.csv', mode='r') as file:
	csv_file = csv.reader(file)
	# print(list(csv_file)[0])
	for line in list(csv_file)[1:]:
		tmp_dict = {'Name': line[1], 'Address 1': line[5], 'Address 2': line[6], 'City': line[8], 'Country': line[9], 'Zipcode': line[7]}
		tmp_list = [{'SKU': line[2], 'Price': line[4], 'Quantity': line[3]}]

		if line[0] not in data.keys():
			data.update({line[0]: {'customer': tmp_dict}})

		if 'orderline' not in data.get(line[0]).keys():
			data.get(line[0]).update({'orderline': tmp_list})
		else:
			data.get(line[0]).get('orderline').extend(tmp_list)

"""
for key, val in data.items():
	print(f"--> key: {key}")
	for k, v in val.items():
		print(f"-> {k}:")
		if type(v) is dict:
			for k1, v1 in v.items():
				print(f"{k1}: {v1}")
		if type(v) is list:
			for x in v:
				print(x)
	print()
"""
print(data)
