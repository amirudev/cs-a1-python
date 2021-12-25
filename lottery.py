from random import choice

serial = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")
lottery = f"{choice(serial)}{choice(serial)}{choice(serial)}{choice(serial)}"

print(f"Todays lottery ticket is {lottery}")