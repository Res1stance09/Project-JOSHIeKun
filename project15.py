import time 
import random
import sys

def race():
    track_l = 60
    player1 = 0 
    player2 = 0
    
    start = 6
    for i in range(1,start):
        sys.stdout.write(f"\rThe Race Begin in {i}")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\n  GOO!")
    time.sleep(1)
    
    while player1 < track_l and player2 < track_l:
        player1 += random.randint(1,3)
        player2 += random.randint(1,3)
        
        print("\033[H\033[J", end="")
        
        finish_line = "🏁"
        grass = ""
        for x in range(1,60):
             grass += "🌳"
             
        print(grass)
        
        print("Player1: " + (" " * min(player1, 99) + "ō͡≡o").ljust(64) + "|")
        print("Player2: " + (" " * min(player2, 99) + "ō͡≡o").ljust(64) + "|")
        print(grass)
        time.sleep(0.3)
    
    if player1 >= track_l and player2 >= track_l:
        print("It's a TIE!")
    elif player2 >= track_l:
        print("Player 2 WIN!")
    else:
        print("Player 1 WIN!")

if __name__ == "__main__":
    race()