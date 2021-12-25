from random import choice

your_lottery = input("Input 4 character lottery to win a prize! ( 0 - 9 and A - E): ")
current_lottery = "####"
lottery_program = True
lottery_attempts = 0

serial_available = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")

while lottery_program and your_lottery != current_lottery:
	print(f"Congratulations for lottery {current_lottery}")
	current_lottery = f"{choice(serial_available)}{choice(serial_available)}{choice(serial_available)}{choice(serial_available)}"
	lottery_attempts += 1

print("You are a winner!")
print(f"Attempts: {lottery_attempts}")
# Stopping Program
input("")