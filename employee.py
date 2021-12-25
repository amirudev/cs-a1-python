class Employee:
	def __init__(self, firstname, lastname, annual_salary):
		self.firstname = firstname
		self.lastname = lastname
		self.annual_salary = annual_salary

	def give_raise(self, amount=5000):
		self.annual_salary += amount