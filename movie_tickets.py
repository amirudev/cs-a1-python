print("Welconme to IXV Movie Theatre!")
print("------------------------------")

age_prompt = "Please type number of age to see price for tickets \n"

while True:
	age = int(input(age_prompt))

	if age < 3:
		print("Ticket charge: Free")
	elif age >= 3 and age <= 12:
		print("Ticket charge: $10")
	elif age > 12:
		print("Ticket charge: $15")
	else:
		print("Not a number ? Exiting program ...")
		break