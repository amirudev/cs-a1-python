favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
invited_people = ["jen", "sarah", "edward", "phil", "yaskur", "yuwandri"]

for person in invited_people:
	if person in favorite_languages.keys():
		print(f"thank you for your respond!, {person}.")
	else:
		print(f"Hi, {person}. You're invited to respond this poll!")