number = input("Welcome to the quiz program! \n Press 1 - to continue \nPress 2 - to close the program  \n ")
if number == "1":
        print("Great! Let's get started!")
        variant = input("In what year was FIFA founded? \n 1 - 1904 year \n 2 - 1906 year \n 3 - 1920 year: \n ")
        if variant == "1":
            print("You guessed it!")
            variant = input("What was the first processor released by Intel? \n 1 - Intel Atom \n 2 - Intel 4004 \n 3 - Intel Pentium: \n ")
            if variant == "2":
                print("Great! You guessed it again! Let's move on!")
                variant = input("Date of appearance of the Python programming language \n 1 - 1991 year \n 2 - 1996 year \n 3 - 2001 year: \n ")
                if variant == "1":
                    print("Excellent! You have good knowledge! And now the last question!")
                    variant = input("When did Windows 10 come out? \n 1 - 2 september 2015 year \n 2 - 30 june 2015 year \n 3 - 29 july 2015 year: \n ")
                    if variant == "3":
                        print("Your knowledge is amazing! Thank you for your participation! See you soon!")
                        input("To confirm the exit, press Enter")
                    else:
                        print("Oops... It seems you made a mistake. Try again!")
                else:
                    print("Oops... It seems you made a mistake. Try again!")
            else:
                print("Oops... It seems you made a mistake. Try again!")
        else:
            print("Oops... It seems you made a mistake. Try again!")
            input("Press Enter to exit the program")
else:
        print("Thank you for participating! Goodbye!")
        input("To confirm the exit, press Enter")
