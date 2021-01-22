import random


def throw(cube_walls=6):
    return random.randint(1, cube_walls)


score_user = 0
score_comp = 0
available_dices = (3, 4, 6, 8, 10, 12, 20, 100)
while score_comp < 2001 and score_user < 2001:
    turn_user = 0
    turn_comp = 0

    try:
        size_1 = input('What kind of dice you want to throw first: ').split('D')
        size_2 = input('What kind of dice you want to throw second: ').split('D')

        if (size_1[0] == '' and len(size_1) == 2 and int(size_1[1]) in available_dices) and \
                (size_2[0] == '' and len(size_2) == 2 and int(size_2[1]) in available_dices):
            size_1 = int(size_1[1])
            size_2 = int(size_2[1])
            turn_user += throw(size_1)
            turn_user += throw(size_2)
        else:
            print('Wrong type of dices!')
            continue
    except:
        print('Wrong type of dices!')
        continue

    if (turn_user == 7):
        score_user = score_user // 7
    elif (turn_user == 11):
        score_user = 11 * score_user
    else:
        score_user += turn_user

    print(f'You throw {turn_user} points. Your score is {score_user}')

    turn_comp += throw()
    turn_comp += throw()
    if (turn_comp == 7):
        score_comp = score_comp // 7
    elif (turn_comp == 11):
        score_comp = 11 * score_comp
    else:
        score_comp += turn_comp

    print(f'Your opponent throw {turn_comp} points. Yours opponent score is {score_comp}\n')

if score_user > 2001 and score_comp > 2001:
    print('It\'s a tie')
elif score_comp < 2001:
    print('You won!')
elif score_user < 2001:
    print('You lose!')
