# TEAM BA 
# Caolboy, Raymund Leean 
# Cordova, Paulo
# Dilag, Paul Jan
# Estacio, Aaron Jan
# Ong, Vincent David 
# Orddovez, Earl Romeo

import random

turtle = 0
hare = 0
turtle_speed = 1
hare_speed = 2
finish = 100
running = True

def main():
    global turtle, hare, turtle_speed, hare_speed, finish, running
    while running:
        random = generate()
        if(random < 2):
            running = not move_hare(hare, hare_speed, finish)
            hare += hare_speed
        else:
            running = not move_turtle(turtle, turtle_speed, finish)
            turtle += turtle_speed
          
    if(turtle >= finish):
        print("Turtle wins!")
    else:
        print("Hare wins!")
      

def generate():
    return random.randint(0, 5)

        
def move_hare(hare, hare_speed, finish):
    print(f"Hare: {hare}")
    if(hare > finish):
        return True
    hare += hare_speed
    return False


def move_turtle(turtle, turtle_speed, finish):
    print(f"Turtle: {turtle}")
    if(turtle > finish):
        return True
    turtle += turtle_speed
    return False
    
    
main()