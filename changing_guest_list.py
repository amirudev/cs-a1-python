friends = ["Richardo", "Yaskur", "Yuwandri"]
message = "I would like to invite you to local theatre"

print(f"Hi {friends[0]}, {message}")
print(f"Hi {friends[1]}, {message}")
print(f"Hi {friends[2]}, {message}")

friend_replace = "Rizal"

print(f"Richardo with seat 1 can't come to that event and {friend_replace} want to replacing Richardo for seat 1")

friends[0] = friend_replace

print(f"Hi {friends[0]}, {message}")