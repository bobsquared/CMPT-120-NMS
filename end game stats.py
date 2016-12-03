def end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet):
    show_board(" end of game")
    print("Showing astronaut ... end of game")
    print("The astronaut " + name + " has civilization level " + str(civ_lvl))
    print("He is in position: " + str(position))
    print("and currently has: " + str(fuel_amount) + " fuel litres")
    print("and collected during the whole game" + str(rock_counter) + " rock specimens.")
    if turn_counter == int(max_turns):
        print("So... he is very alive!")
        print("but he cannot move anymore since the game ended!")
    elif int(fuel_amount) == 0:
        print("He is stranded since he has no fuel!")
    elif position == python_planet:
        print("So... he is very alive!")
        print("And he also reached Python Planet,so he won!!!")
    yes_no = input("Do you want to play again? (y/n): ")
    while (yes_no.lower() != "y" and yes_no.lower() != "n"):
        yes_no = input("\nWhat you typed was not y or n. Please try again: ")
    if yes_no.lower() == "y":
        print("Let's get started again then.")
        turn_counter = 0
        fuel_amount = 1
        position = 0
        rock_counter = []

yes_no = "p"


while yes_no.lower() == "y" and turn_counter <= int(max_turns) and int(fuel_amount) > 0 and position != python_planet:

    if turn_counter == 1:
        data = file()
        listStrings = read_string_list_from_file(data)
        listOfString = convert_to_list(listStrings)
        
        planet_number = planet_num(listOfString)
        planet_civ_level = (create_lists_board(listOfString))[0]
        planet_fuel = (create_lists_board(listOfString))[1]
        planet_rocks = (create_lists_board(listOfString))[2]
        display_board(planet_number,listOfString,position)
        name, civ_lvl, fuel_amount, max_turns, amaz_expl, mild_expl, position = game_info()
    
    display_board(planet_number,listOfString,position)
    
    turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, listOfString, rock_counter)

    if mild_expl.lower == "y":
        mild_explosions(listOfString, planet_list, planet_rocks)

    position = movement(planet_number, position)
    if position != python_planet:
        fuel_amount = encounter(fuel_amount, civ_lvl, position, planet_fuel, planet_civ_level)

        if int(fuel_amount) > 0:
            rock_counter = rock_collection(position, rock_counter, planet_rocks)
        else:
            game_count += 1
            end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet) 

    else:
        game_count += 1
        win_count += 1
        end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet)

    if turn_counter == int(max_turns):
        game_count += 1    
        end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet)

    turn_counter += 1



def end_of_all_games(game_count, win_count):
    print("The user played" + str(game_count) + " game in total")
    print("of those, the astonaut won " + str(win_count))
    print("To conclude, the program will do a conversion from binary to decimal!")
    print("taking as source the  list of rock specimens in the last game board")

name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet = "cloud", 2, 4, 5, [1, 1, 1], 10, 10, 4


end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet)




    
    
