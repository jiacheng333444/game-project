import sys

# the other files from project
import enemy
import character
import healer
import tank
#import colesium
import duelist

def display_menu():
    # Displays the main menu options to the player
    print("\n" + "="*30)
    print("       COLESIUM BATTLER     ")
    print("="*30)
    print("1. Create Character")
    print("2. Enter the Colesium")
    print("3. Quit")
    print("="*30)

def main(): 
    # main game loop handling menu navigation
    player_character = None

    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            print("\n--- Character Creation ---")
            print("1. Tank")
            print("2. Healer")
            print("3. Duelist")
            class_choice = input("Choose your class (1-3): ").strip()

            print("\nExcellent choice.")
            char_name = input("What is your character's name? ").strip()

            if class_choice == '1':
                print(f"You chose tank class for {char_name}.")
            
            elif class_choice == '2':
                print(f"You chose healer class for {char_name}.")
            
            elif class_choice == '3':
                print(f"You chose duelist class for {char_name}.")
            
            else:
                print("Thats not a class fr")
        
        elif choice == '2':
            print("\n--- Entering the Colesium ---")
            if player_character is None:
                print("You gotta create a character first")
            else:
                print("The battle starts")
            
        elif choice == '3':
            print("\nThanks for playing fr")
            sys.exit()
        
        else:
            print("\nInvalid input bro. Enter 1, 2, or 3")
        
if __name__ == "__main__":
    main()    
    
    
