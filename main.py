name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a large lake, you can go around it or swim accross? Type walk to walk around and swim to swim accross:")
    if answer == "swim":
        print("You swam accross and were eaten by an alligator ")

    elif answer == "walk":
        print("You walked for many miles and ran out of water and lost the game")

    else:
        print("Not a valid option. you lose.")

elif answer == "right":
    answer = input("You have come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/head back)")

    if answer == "back":
        answer = input("You were biten by a bulldog you lose")

    elif answer == "cross":
        answer = input("You crossed the bridge and you meet a stranger who tells you to trust him. Do you trust him or not. Type(trust/dont trust)")

        if answer == "trust":
            print("You trusted the stranger and they tricked you you lost")
        elif answer == "dont trust":
            print("You were saved as you didnt trust him and WIN!")
        else:
            print("Not a valid option. you lose.")
    else:
        print("Not a valid option. you lose.")
else:
    print("Not a valid option. you lose.")

print("Thank you for trying ",name)
