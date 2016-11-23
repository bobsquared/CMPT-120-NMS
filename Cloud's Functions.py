def start_game():
    yes_no = input(print("Do you want play? (y/n): "))
    while (yes_no.lower() != y or yes_no.lower() != n):
        yes_no = input(print("What you typed was not y or n. Please try again: "))
    if yes_no.lower() == n:
        print ("That's okay. Maybe you'll play next time. Bye!")
        return
    
    
