print("Welcome to the beta v0.03")
print("We don't have a title yet...")
print("or really an idea...")

def s_1_start():
    print("You wake up in a room in a small puddle of blood, what do you do?")
    print("(1) Get up")
    print("(2) Check yourself for wounds")
    print("(3) Investigate your surroundings")
    print("(4) Look for a weapon")
    a1 = input("Choice: ")
    choice_1(a1)

def choice_1(a1):
    if a1 == "1":
        print("You got up")
        start()
    elif a1 == "2":
        print("You find a small incession behind your left ear")
        s_1_2()
    elif a1 == "3":
        print("You find yourself in a concrete cell with a single wooden door")
        s_1_3()
    elif a1 == "4":
        print("You find nothing")
        s_1_4()

def s_1_2():
    print("Attempt to fix the wound?")
    print("(1) Yes")
    print("(2) No")
    a2 = input("Choice: ")
    choice_2(a2)

def choice_2(a2):
    if a1 == "1":
        print("In attempt to mend your wound you only made it fatal, YOU HAVE DIED")
        main()
    elif a1 == "2":
        print("You leave your wound alone")
        s_1_start()

def s_1_3():
    print("Move to door?")
    print("(1) Yes")
    print("(2) No")
    a3 = input("Choice: ")
    choice_3(a3)

def choice_3(a3):
    if a3 == "1":
        print("You move to the door")
        s_1_3_2()
    elif a3 == "2":
        print("You remain at the center of the room")
        s_1_start()

def s_1_3_2():
    print("Open door?")
    print("(1) Yes")
    print("(2) No")
    a3_2 = input("Choice: ")
    choice_3_2(a3_2)

def choice_3(a3):
    if a3 == "1":
        print("You open the door, a bright light shines in from outside. You step through the door")
        s_2_start()
    elif a3 == "2":
        print("You remain in this room until you starve to death, YOU DIED")
        main()

start()
