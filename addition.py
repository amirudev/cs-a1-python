try:
	number_1 = int(input("Type any number: "))
	number_2 = int(input("Type any number: "))
except ValueError:
	print("Sorry, you are not typing number correctly")
else:
	print(f"{number_1} + {number_2} = {number_1 + number_2}")
