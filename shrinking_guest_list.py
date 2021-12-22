friends = ["Rizal", "Yaskur", "Yuwandri", "Fajar", "Aditya", "Soleh"]

cancelled_friend_1, cancelled_friend_2, cancelled_friend_3, cancelled_friend_4 = friends.pop(), friends.pop(), friends.pop(), friends.pop()

sorry_message = "Sorry, due to coronavirus you can't attend to this event"
still_invited_message = "You're got your seat as informed before"

print(f"{sorry_message}, {cancelled_friend_1}")
print(f"{sorry_message}, {cancelled_friend_2}")
print(f"{sorry_message}, {cancelled_friend_3}")
print(f"{sorry_message}, {cancelled_friend_4}")
print(f"{friends[0]}, {still_invited_message}")
print(f"{friends[1]}, {still_invited_message}")

print(f"Attendee list: {friends}")

del friends[1]
del friends[0]

print(f"Attendee list: {friends}")