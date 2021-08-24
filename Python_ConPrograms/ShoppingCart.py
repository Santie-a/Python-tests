shopItems = [
	{'name': 'Milk', 'price': 2.99, 'q': 0},
	{'name': 'Bread', 'price': 1.99, 'q': 0},
	{'name': 'Onions', 'price': 0.99, 'q': 0},
	{'name': 'Tomatoes', 'price': 0.55, 'q': 0},
	{'name': 'Bananas', 'price': 1.99, 'q': 0},
	{'name': 'Candies', 'price': 20.55, 'q': 0},
	{'name': 'Rice', 'price': 15.99, 'q': 0},
]

shoppingCart = []

item = ''
status = ''
subtotal = 0
total = 0

def spaceCount(str):
	space = ''
	string = ""	
	count = 11
	while count > len(str):
		count = count - 1		
		space = space + ' '
	return space
		
def shopTable(shopItems):
	print('----------------------------')
	print('|    Item    ||   Price    |')
	print('----------------------------')
	for item in shopItems:
		print('| ' + item['name'] + spaceCount(item['name']) + '|| ' + str((item['price'])) + spaceCount(str(item['price'])) + '|')
	print('----------------------------')

def wordComp(word, list):
	for x in list:
		if x == word:
			return True
			break
	return False

def toList(shopItems):
	array = []
	for item in shopItems:
		array.append(item['name'])
	return array

def listIndex(item, list):
	index = 0
	for x in list:
		if x == item:
			return index
		else:
			index = index + 1

# def shoppingCart(shopingCart, shopItems):

print('''
Welcome to the groceries store

The Following list are the aviable inventory:
''')

shopTable(shopItems)

while item != 'exit':
	item = input('''
Write the items you want to take (Insert exit to pay): ''')	

	if wordComp(item.capitalize(), toList(shopItems)) == True:
		if shopItems[listIndex(item.capitalize(), toList(shopItems))]['q'] == 0:
			shoppingCart = shoppingCart + [shopItems[listIndex(item.capitalize(), toList(shopItems))]['name']]
		shopItems[listIndex(item.capitalize(), toList(shopItems))]['q'] = shopItems[listIndex(item.capitalize(), toList(shopItems))]['q'] + 1
		print('''
Added ''' + item.lower())
		subtotal = subtotal + shopItems[listIndex(item.capitalize(), toList(shopItems))]['price']
		print('Current subtotal is: ' + str(subtotal))
		print('Current shopping cart: ' + str(shoppingCart))
		print('Quantity of ' + item.lower()+ ' : ' + str(shopItems[listIndex(item.capitalize(), toList(shopItems))]['q']))
	elif wordComp(item.capitalize(), toList(shopItems)) == False:
		if item != 'exit':
			print('No existencies')

if shoppingCart != []:
	while status != 'quit':
		print('''
This is your shopping cart:
''')
		total = subtotal * 1.19 
		print(shoppingCart)
		print('The total is: ' + str(total))

		status = input('''
Pay using credit card or money?:
''')
		status = status.capitalize()
		if status == 'Credit card':
			print('''
Succesfull payment''')
			break
		elif status == 'Money':
			effective = input('Deposite you money: ')
			if float(effective) < total:
				print('''
Not enough money''')
				effective = input('Deposite you money again: ')
				if float(effective) >= total:
					change = float(effective) - total
					print('''
Your change is: ''' + str(change))
					break
			elif float(effective) >= total:
				change = float(effective) - total
				print('''
Your change is: ''' + str(change))
			break
else:
	print('No item was selected')

print('''Thanks for visiting us''')