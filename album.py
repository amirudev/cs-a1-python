def make_album(name, title, number_of_songs=None):
	album = {"artist": name, "title": title}
	if number_of_songs:
		album["number_of_songs"] = number_of_songs
	return album

album_a = make_album("Wahyu", "Song A")
album_b = make_album("Yaskur", "Song B", 4)
album_c = make_album("Yuwandir", "Song C")

print(album_a)
print(album_b)
print(album_c)

