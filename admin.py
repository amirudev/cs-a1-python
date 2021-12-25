from user import User
from privilege import Privilege

class Admin(User):
	def __init__(self, firstname, lastname, country, privileges):
		super().__init__(firstname, lastname, country)
		self.privileges = Privilege(privileges)

wahyu = Admin("Wahyu", "Amirulloh", "United Kingdom", ["add post", "delete post", "ban user"])
wahyu.privileges.show_privileges()