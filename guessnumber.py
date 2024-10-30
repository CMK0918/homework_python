import random

def check_input(userinput:any) -> int:
    '''
    make sure input int type
    '''
    while True:
        try:
            return int(input(userinput))
        except Exception as e:
            print(f"input shold be int: {e}")

# lower upper relationship
while True:
    lower = check_input("input lower limit number: ")
    upper = check_input("input upper limit number: ")
    if lower <= upper:
        break
    else:
        print("lower should be smaller than upper")

target = random.randint(lower,upper)

count = 0
while True:
    guess = check_input("guess the number: ")
    if (lower <= guess <= upper):
        count += 1
        if guess == target:
            print(f"just right! you guess {count} times")
            break
        elif guess < target:
            print("guess larger")
        elif guess > target:
            print("guess smaller")
    else:
        print("guess should be in the range")