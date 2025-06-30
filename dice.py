import random
#dictionary for dice art and storing in tuple
dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),

    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),

    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),

    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),
}

dice = []
total = 0 #where we get the total dice roll

num_of_dice = int(input("How many dice would you like to roll? "))
for die in range(num_of_dice):
    dice.append(random.randint(1,6)) #for every dice result we add all result in it

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="") #for printing dice in sequece
    print()

for die in dice:
    total += die #add all dice result which will be input
print(f"total: {total}")