import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.employee = Employee("Wahyu", "Amirulloh", 3000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 8000)

	def test_give_custom_raise(self):
		self.employee.give_raise(2000)
		self.assertEqual(self.employee.annual_salary, 5000)

if __name__ == '__main__':
	unittest.main()