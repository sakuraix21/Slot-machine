
import random

def spin_slots():
    "Simulates a spin of the slot machine."
    symbols = ["|Jackpot|", "|Maxwin|", "|Scatter|",]
    reels = [random.choice(symbols) for _ in range(3)]
    return reels

def display_result(reels):
    "Displays the result of the spin."
    print(" ".join(reels))

# Example usage
reels = spin_slots()
display_result(reels)