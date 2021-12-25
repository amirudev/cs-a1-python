import json

filename = "verify_user.txt"
user_loggedin = False

def get_current_user_username():
	try:
		with open(filename) as f:
			return json.load(f)
	except:
		return None

def set_current_user_username():
	username = input("Hello, would you like to make a new username ? please type here: ")

	with open(filename, "w") as f:
		json.dump(username.lower(), f)

	user_loggedin = True

def greet_user(username):
	print(f"Good Morning, {username}")

def prompt_current_user_username():
	current_username = get_current_user_username()
	current_username_censored = current_username

	if len(current_username) > 8:
		current_username_censored = f"{current_username[:2]}***{current_username[-2:]}"
	elif len(current_username) > 2:
		current_username_censored = f"{current_username[:2]}***"

	username = input(f"is {current_username_censored} your username ? please type again to confirm: ")

	if username == current_username:
		greet_user(current_username)
		user_loggedin = True
	else:
		if input("it is not your username, would you like to make a new one [yes/no] ? ") == 'yes':
			set_current_user_username()

while user_loggedin == False:
	prompt_current_user_username()

greet_user()