class User:
	def __init__(self, firstname, lastname, country):
		self.firstname = firstname
		self.lastname = lastname
		self.country = country
		self.fullname = f"{firstname.title()} {lastname.title()}"
		self.login_attempts = 0

	def describe_user(self):
		print(f"User Information, Name: {self.fullname}, Nationality: {self.country}")
		if self.login_attempts:
			print(f"You have attempting login for {self.login_attempts} times before successfully this login")

	def greet_user(self):
		if self.country == "Indonesia":
			print(f"Selamat Pagi, {self.firstname.title()}")
		else:
			print(f"Good Morning, {self.firstname.title()}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

wahyu = User("Wahyu", "Amirulloh", "United Kingdom")

wahyu.describe_user()
wahyu.increment_login_attempts()
wahyu.increment_login_attempts()
wahyu.increment_login_attempts()
wahyu.describe_user()
wahyu.reset_login_attempts()
wahyu
wahyu.describe_user()