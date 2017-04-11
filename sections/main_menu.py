def main():
    print("Welcome to <Insert Title here>")
    print("This is a text based adventure game written by our class.")
    print("The controls are simple, input the number contained in the parenthesis")
    print("(1) Begin Playing")
    print("(2) Veiw Credits")
    print("(3) Exit Window")
    sel = int(input("Selection >> "))
    if sel == 1:
        print("Playing game")
        untitled_section()
    elif sel == 2:
        print("Credits")
        credits()
    elif sel == 3:
        print("Exiting Program")
        quit()
    else:
        sefl = str(sel)
        print(sefl , "is not an accepted input form, returning to top menu.")
        time.sleep(3)
        menu()
