print("Welcome to the beta v0.02")
print("We don't have a title yet...")
print("or really an idea...")

def start():
    print("You wake up in a room in a small puddle of blood, what do you do?")
    print("(1) Check yourself for wounds")
    print("(2) Investigate your surroundings")
    print("(3) Look for a weapon")
    a1 = input("Choice: ")
    choice_1(a1)

def s_1():
    print("You wake up in a room in a small puddle of blood, what do you do?")
    print("(1) Check yourself for wounds")
    print("(2) Investigate your surroundings")
    print("(3) Look for a weapon")
    a2 = input("Choice: ")
    choice_2(a2)

def choice_1(a1):
    if a1 == "1":
        print("You find a small wound behind your left ear")
        s_1()
    elif a1 == "2":
        print("You find yourself in a concrete cell with a single door")
        s_1()
    elif a1 == "3":
        print("You find nothing")
        s_1()

start()
