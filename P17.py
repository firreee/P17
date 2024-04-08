import random

def generate_powerball():
    numbers = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 27)
    numbers.append(powerball)
    numbers.sort()
    return numbers

def generate_mega_million():
    numbers = random.sample(range(1, 71), 5)
    numbers.sort()
    return numbers

def generate_lucky_day_lotto():
    numbers = random.sample(range(1, 46), 5)
    numbers.sort()
    return numbers

def generate_lotto():
    numbers = random.sample(range(1, 53), 6)
    numbers.sort()
    return numbers

def game_info():
    print("Lottery Game Information:")
    print("Powerball Highest number generated: 69 How many numbers to generate: 5")
    print("Mega Million Highest number generated: 70 How many numbers to generate: 5")
    print("Lucky Day Lotto Highest number generated: 45 How many numbers to generate: 5")
    print("Lotto Highest number generated: 52 How many numbers to generate: 6")
    print()

def main():
    game_info()
    running = True
    
    while running:
        print("1. Powerball")
        print("2. Mega Million")
        print("3. Lucky Day Lotto")
        print("4. Lotto")
        print("9. Quit")

        selection = input("Select a lottery game (1-4, 9 to quit): ")

        if selection == '1':
            lottery_name = "Powerball"
            numbers = generate_powerball()
        elif selection == '2':
            lottery_name = "Mega Million"
            numbers = generate_mega_million()
        elif selection == '3':
            lottery_name = "Lucky Day Lotto"
            numbers = generate_lucky_day_lotto()
        elif selection == '4':
            lottery_name = "Lotto"
            numbers = generate_lotto()
        elif selection == '9':
            print("--- Program Quit ---")
            running = False
        else:
            print("Invalid selection. Please choose a number from 1 to 4 or 9 to quit.")
            continue

        print(f"{lottery_name}: {', '.join(map(str, numbers))}")
        run_again = input("Do you want to run again? (y/n): ")

if __name__ == "__main__":
    main()
