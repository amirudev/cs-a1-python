filename_a = "cats.txt"
filename_b = "dogs.txt"

try:
	with open(filename_a) as file_object:
		file_a = file_object.read()
	with open(filename_b) as file_object:
		file_b = file_object.read()
except FileNotFoundError:
	print("Sorry, some file required does not exist")
else:
	print(file_a)
	print(file_b)