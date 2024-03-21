import random


input_dice_roll = int(input("Hányszor szeretne dobni a kockával?: "))


x = 0
y = 0

for i in range(input_dice_roll):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice_sum = dice1 + dice2 + dice3


    if dice_sum < 10:
        print(f"Dobás: {dice1} + {dice2} + {dice3} = {dice_sum}     Anni nyert")
        x=x+1
    if dice_sum > 10:
        y=y+1
        print(f"Dobás: {dice1} + {dice2} + {dice3} = {dice_sum}     Panni nyert")


print(f"A játék során {x} alkalommal Anni, {y} alkalommal Panni nyert")