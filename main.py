import sys

# the other files from project
#import character
#import healer
#import tank
#import colesium

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
    
    
display_menu()