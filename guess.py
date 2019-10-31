import random

guess_count = 1
score = 1000;
real_number = random.randint(0,1000)
#print(f'Number is {real_number}')
get_number = int(input("Guess a number between 0 to 1000 : "))
def guess():
    guesses = int(input("Enter Again: "))
    return guesses

while real_number != get_number:
    if real_number > get_number:
        print("It's not that low.\n ")
        get_number = guess()
        score -= 10
        guess_count += 1
    else:
        print("It's not that high.\n ")
        get_number = guess()
        score -= 10
        guess_count += 1
if real_number == get_number:
    print(f"Congratulations ! You've guessed the number correctly at {guess_count} attempt")
    print(f'And your Score is = {score} out of 1000')
