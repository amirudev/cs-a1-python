current_users = ["admin", "wahyu", "yaskur", "yuwandri", "ricardo"]
new_users = ["rizal", "aditya", "fajar", "soleh", "yaskur"]

for user in new_users:
	if user in current_users:
		print(f"username {user} already exists")
	else:
		print(f"username {user} is available")