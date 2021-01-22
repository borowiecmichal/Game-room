import random


def throw(cube_walls=6):
    return random.randint(1, cube_walls)



score_user = 0
score_comp = 0
while score_comp < 2001 and score_user < 2001:
    turn_user = 0
    turn_comp = 0

    input('Press enter to roll the dice')
    turn_user += throw()
    turn_user += throw()
    if (turn_user == 7):
        score_user = score_user//7
    elif(turn_user == 11):
        score_user = 11*score_user
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
elif score_comp<2001:
    print('You won!')
elif score_user<2001:
    print('You lose!')
