friends = ["Rizal", "Yaskur", "Yuwandri"]
message = "I would like to invite you to local theatre"

friends_to_add = ["Fajar", "Aditya", "Soleh"]

friends.insert(0, friends_to_add[0])
friends.insert(2, friends_to_add[1])
friends.append(friends_to_add[2])

print(f"Hi {friends[0]}, {message}")
print(f"Hi {friends[2]}, {message}")
print(f"Hi {friends[5]}, {message}")