from random import randint

encoder_caracters = "a1b2c3d4e5f6g7h8i9j0k-l+m[n]o}p{q);r's :t,u<v>w?x/y*z!@#$%^&*(."
password_caracters = "abcdefghijklmnopqrstuvwxyz1234567890*"
not_numbers = "abcdefghijklmnopqrstuvwxyz"

def aleatory_generator():
	while True:
		status = True
		print("How long your password?")
		password_lenght = input("Lenght: ")
		for i in range(len(not_numbers)):
			for x in range(len(password_lenght)):
				if password_lenght[x].__contains__(not_numbers[i]):
					print("Insert a number")
					status = False
				
		if status:
			string = ""
			password_lenght = int(password_lenght)
			for i in range(password_lenght):
				letter = password_caracters[randint(0, len(password_caracters) - 1)]
				string = (string + letter)
			return string

def encoder():
	while True:
		print("Insert the sentence or word you want to code")
		word = input("Word: ").lower()
		index_list = []
		string = ""

		for i in range(len(word)):
			for x in range(len(encoder_caracters)):
				if word[i] == encoder_caracters[x]:
					index_list.append(x)
		print(index_list)
		print(len(encoder_caracters))
		for index in index_list:
			if index >= len(encoder_caracters) - 2 and index < len(encoder_caracters) - 1:
				new_index = len(encoder_caracters) - index - 2
				string = (string + encoder_caracters[new_index])
			elif index == len(encoder_caracters) - 1:
				print("here")
				string = (string + encoder_caracters[1])
			else:
				string = (string + encoder_caracters[index + 2])

		return string

def decoder(word):
	index_list = []
	string = ""

	for i in range(len(word)):
		for x in range(len(encoder_caracters)):
			if word[i] == encoder_caracters[x]:
				index_list.append(x - 2)

	for index in index_list:
		string = (string + encoder_caracters[index])

	return string

def coder_decoder():
	encoded_word = encoder()
	print("Enoded word:")
	print(encoded_word)
	print("Decoded word")
	print(decoder(encoded_word))

def main():
	while True:
		print("Want to generate a password, encode or decode a word?")
		style = input("Selection: ").lower()

		if style.startswith("enc"):
			encoded = encoder()
			return encoded

		if style.startswith("pass") or style.startswith("gen"):
			password = aleatory_generator()
			return password

		if style.startswith("dec"):
			word = input("Insert the word you want to decode: ")
			decoded = decoder(word)
			return decoded

print(main())