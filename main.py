import random

# Snake Water Gun Game
def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)? ").lower()
result = gameWin(comp, you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if result is None:
    print("It's a Tie!")
elif result:
    print("🎉 You Win!")
else:
    print("❌ You Lose!")
