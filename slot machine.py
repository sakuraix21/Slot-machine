import random

def spin_slot_machine():
    # Define possible symbols on the slot machine
    symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓", "7️⃣"]
    
    # Randomly pick 3 symbols for the spin
    spin_result = random.choices(symbols, k=3)
    
    # Print the result of the spin
    print(" | ".join(spin_result))
    
    # Check for winning conditions (e.g., all three symbols are the same)
    if spin_result[0] == spin_result[1] == spin_result[2]:
        print("Congratulations! You won!")
    else:
        print("Sorry! Better luck next time.")

# Play the slot machine
while True:
    input("Press Enter to spin the slot machine... ")
    spin_slot_machine()
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break
