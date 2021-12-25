class User:
	def __init__(self, firstname, lastname, country):
		self.firstname = firstname
		self.lastname = lastname
		self.country = country
		self.fullname = f"{firstname.title()} {lastname.title()}"

	def describe_user(self):
		print(f"User Information, Name: {self.fullname}, Nationality: {self.country}")

	def greet_user(self):
		if self.country == "Indonesia":
			print(f"Selamat Pagi, {self.firstname.title()}")
		else:
			print(f"Good Morning, {self.firstname.title()}")

# wahyu = User("Wahyu", "Amirulloh", "United Kingdom")
# yaskur = User("Yaskur", "Fauzan", "Indonesia")

# wahyu.describe_user()
# wahyu.greet_user()

# yaskur.describe_user()
# yaskur.greet_user()