import json

filename = "favorite_number_remembered.txt"

try:
	with open(filename) as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("What is your favorite number? ")
	with open(filename, "w") as f:
		json.dump(number, f)
else:
	print(f"As I remembered, your favorite number is {number}")