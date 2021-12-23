albums = []
album_program = True

def make_album(artist, title, number_of_songs=None):
	album = {"artist": artist, "title": title}
	if number_of_songs:
		album["number_of_songs"] = number_of_songs
	else:
		album["number_of_songs"] = 0

	return album

while album_program:
	artist = input("Artist Name: ")
	title = input("Album Title: ")
	number_of_songs = input("Number of Snongs (optional): ")

	album = make_album(artist, title, number_of_songs)
	albums.append(album)

	program_prompt = input("Click enter to continue listing album or type quit to exit program and see results ")

	if program_prompt == 'quit':
		album_program = False

print("--- Album List ---")
for album in albums:
	print(f"{album['artist']} has album titled {album['title']} and has been made {album['number_of_songs']} music")