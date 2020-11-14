from system import System
x = System()

print('Rock, Paper, Scissors'+'             '+'Author: Mahtab')

computer_point = 0
user_point = 0
opt = True
willplay = True
name = None

while willplay:
    if opt:
        print("Enter 'r' for rock, 'p' for paper, 's' for scissors\nRock Wins With Scissors\nPaper Wins With Rock\nScissors Wins With Paper")
        print()

    if not name:
        name = input('Enter Your Name Here: ')

    p = 'a'

    while p.isalpha():
        p = input('Enter The Winning Point Here: ')

    print('Match Has Started..')
    print()

    user = '0'
    p = int(p)
    computer_point = 0
    user_point = 0
    user = 1

    while computer_point != p or user_point != p:
        user = 1

        while user != 'r' and user != 'p' and user != 's':
            user = input("Enter 'r', 'p' or 's': ")
            if user != 'r' and user != 'p' and user != 's':
                print('Invalid!')
                print()

        bot = x.bot()
        print()

        print(f'{name} = {user}  Computer = {bot}')
        print()
        if x.sys_gameOver(user, bot) == 1:
            user_point += 1
        elif x.sys_gameOver(user,bot) == 2:
            computer_point += 1

        print(f"{name}'s point: {user_point}  Computer's Point: {computer_point}  Winning Point: {p}")
        print()
        if computer_point == p or user_point == p:
            break

    print(f"{'You Have Won' if user_point==p else 'Computer Has Won'}")

    print('You Have 3 Options:\n1)Play Again\n2)See The Introduction\n3)Exit')
    m = input('Enter Your Choices Here: ')
    if m == '1':
        willplay = True
        opt = False
    elif m == '2':
        willplay = True
        opt = True
    else:
        break