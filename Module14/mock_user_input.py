def yes_or_no():
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        return("Sorry to see you go!")
    elif answer == "no":
        return("Awesome!")
    else:
        return("BANG!")
