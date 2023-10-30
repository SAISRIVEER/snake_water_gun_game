import random

def swg(comp, mychoice):
    if(comp == mychoice):
        return None
    elif(comp == 's' and mychoice == 'g'):
        return True
    elif(comp == 'w' and mychoice == 's'):
        return True
    elif(comp == 'g' and mychoice == 'w'):
        return True
    else:
        return False

choice = ['s', 'w', 'g']
a = random.randint(0, 2)
comp = choice[a]
print("Choose from these three - 's', 'w', 'g'")
mychoice = input("Choice from the given choice : ")
x = swg(comp, mychoice)
print(f"Your choice is {mychoice} and computer's choice is {comp} ")
if x :
    print("You won !")
elif x is None:
    print("Match draw")
else:
    print("You lose")
