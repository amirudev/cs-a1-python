from random import randint

class Dice:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_dice(self):
		result = randint(1, self.sides)
		print(result)

dice = Dice()

dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()

dice_2 = Dice(10)

dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()

dice_3 = Dice(20)
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()
