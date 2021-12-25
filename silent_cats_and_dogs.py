filename_a = "catsy.txt"
filename_b = "dogs.txt"

def read_pets(filename):
	try:
		with open(filename) as file_object:
			file = file_object.read()
	except FileNotFoundError:
		pass
	else:
		print(file)

read_pets(filename_a)
read_pets(filename_b)