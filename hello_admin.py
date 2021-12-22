usernames = ["admin", "wahyu", "yaskur", "yuwandri", "ricardo"]

if usernames:
	for username in usernames:
		if username == "admin":
			print(f"Hi, Administrator, this is your report!")
		else:
			print(f"Hi, {username}. Welcome back!")
else:
	print("We dont have any online users right now")