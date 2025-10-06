import random

def chooose_difficulty():
    print("\nChoose your difficulty level:")
    print("1. Easy (1-10, unlimited guesses)")
    print("2. Medium (1-20, 10 guesses)")
    print("3. Hard (1-50, 7 guesses)")
    print("4. Expert (1-100, 5 guesses)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            match choice:
                case 1:
                    return 10, float('inf'), "Easy"
                case 2:
                    return 20, 10, "Medium"
                case 3:
                    return 50, 7, "Hard"
                case 4:
                    return 100, 5, "Expert"
                case _:
                    print("Please enter a number between 1-4!")
                    
        except ValueError:
            print("Please enter a valid number!")

def calculate_score(attempts, max_attempts, difficulty):
    match difficulty:
        case "Easy":
            base_score = 100
        case "Medium":
            base_score = 200
        case "Hard":
            base_score = 300
        case "Expert":
            base_score = 500

    if max_attempts != float('inf'):
        efficiency_bonus = int((max_attempts - attempts) * 20)
    else:
        efficiency_bonus = max(0, (20 - attempts) * 10)
    
    return max(50, base_score + efficiency_bonus)

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)
    
    total_score = 0
    games_played = 0
    
    while True:
        games_played += 1
        print(f"\nGame #{games_played}")
        
        max_number, max_attempts, difficulty = chooose_difficulty()
        
        secret_number = random.randint(1, max_number)
        attempts = 0
        
        print(f"\nI'm thinking of a number between 1 and {max_number}")
        if max_attempts != float('inf'):
            print(f"You have {max_attempts} attempts to guess it!")
        else:
            print("You have unlimited attempts!")
        print("Let's start!\n")
        
        while attempts < max_attempts:
            try:
                attempts += 1
                
                guess = int(input(f"Attempt #{attempts}: Enter your guess: "))
                
                if guess < 1 or guess > max_number:
                    print(f"Please enter a number between 1 and {max_number}!")
                    attempts -= 1  
                    continue
                
                if guess == secret_number:
                    print(f"You guessed the correct number!")
                    print(f"The number was {secret_number}")
                    print(f"You got it in {attempts} attempts!")
                    
                    game_score = calculate_score(attempts, max_attempts, difficulty)
                    total_score += game_score
                    print(f"🏆 Game Score: {game_score} points")
                    break
                    
                elif guess < secret_number:
                    remaining = max_attempts - attempts
                    if remaining > 0 and max_attempts != float('inf'):
                        print(f"Too low! Try higher. ({remaining} attempts left)")
                    elif max_attempts == float('inf'):
                        print("Too low! Try higher.")
                    
                elif guess > secret_number:
                    remaining = max_attempts - attempts
                    if remaining > 0 and max_attempts != float('inf'):
                        print(f"Too high! Try lower. ({remaining} attempts left)")
                    elif max_attempts == float('inf'):
                        print("Too high! Try lower.")

            except ValueError:
                print("Please enter a valid number!")
                attempts -= 1 
                continue
        
        if attempts >= max_attempts and max_attempts != float('inf'):
            print(f"Sorry, you've run out of attempts!")
            print(f"The correct number was {secret_number}")
            print("Better luck next time!")

        print(f"\nCurrent Stats:")
        print(f"Games Played: {games_played}")
        print(f"Total Score: {total_score}")
        if games_played > 0:
            print(f"Average Score: {total_score // games_played}")
        
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print(f"\nThanks for playing!")
                print(f"Final Stats:")
                print(f"Games Played: {games_played}")
                print(f"Total Score: {total_score}")
                if games_played > 0:
                    print(f"Average Score: {total_score // games_played}")
                print("Hope you had fun!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    play_guessing_game()