class Privilege:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		for privilege in self.privileges:
			print(f"can {privilege}")