import random

# I am going to create a game to play against the computer
# The game is rock, paper, scissors
# The user will choose one of the three options from a list and it should be indicated if they chose a valid option
# The computer will choose one of the three options
# The user's choice will be compared with the computer's choice
# The result of the game will be displayed
# The user will be asked if they want to play again
# If the user responds yes, the game will be played again
# If the user responds no, the game will end

def play_game():
    options = ["rock", "paper", "scissors"]
    
    while True:
        # User's choice
        user_choice = input("Choose rock, paper, or scissors: ")
        
        # Check if user's choice is valid
        if user_choice not in options:
            print("Invalid option. Try again.")
            continue
        
        # Computer's choice
        computer_choice = random.choice(options)
        
        # Compare choices
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose.")
        
        # Ask if user wants to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game()




# Voy a crear un juego para jugar contra la computadora
# El juego es el piedra, papel o tijera
# El usuario va a elegir una de las tres opciones de una lista y se debe indicar si eligió una opción valida
# La computadora va a elegir una de las tres opciones
# Se va a comparar la elección del usuario con la elección de la computadora
# Se va a mostrar el resultado del juego
# Se va a preguntar al usuario si quiere volver a jugar
# Si el usuario responde que sí, se vuelve a jugar
# Si el usuario responde que no, se termina el juego

# def play_game():
#     options = ["piedra", "papel", "tijera"]
    
#     while True:
#         # User's choice
#         user_choice = input("Elige piedra, papel o tijera: ")
        
#         # Check if user's choice is valid
#         if user_choice not in options:
#             print("Opción inválida. Intenta de nuevo.")
#             continue
        
#         # Computer's choice
#         computer_choice = random.choice(options)
        
#         # Compare choices
#         if user_choice == computer_choice:
#             print("Empate!")
#         elif (user_choice == "piedra" and computer_choice == "tijera") or (user_choice == "papel" and computer_choice == "piedra") or (user_choice == "tijera" and computer_choice == "papel"):
#             print("¡Ganaste!")
#         else:
#             print("Perdiste.")
        
#         # Ask if user wants to play again
#         play_again = input("¿Quieres volver a jugar? (s/n): ")
#         if play_again.lower() != "s":
#             break

# play_game()

