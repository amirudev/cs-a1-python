import json

fav_number = input("Type your favorite number: ")

filename = "favorite_number.txt"

with open(filename, "w") as f:
	json.dump(fav_number, f)