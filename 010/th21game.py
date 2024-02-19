import random
import time
while True:
    current_number=1

    if random.randint(0,1)==0:
        current_player='human'
    else:
        current_player='computer'

    while current_number<=21:
        print('con so hien tai la',current_number)

        if current_player=='human':
            player_choice=""
            while player_choice not in ['1','2','3']:
                player_choice=input("choose your number to add :")
            player_choice=int(player_choice)
            current_number=current_number+player_choice
    

            if current_number>=21:
                print('con so hien tai la',current_number)
                print('you lose')
                break
            current_player="computer"

        else:
            computer_choice=random.randint(1,3)
            current_number = current_number + computer_choice
 
            time.sleep(1)
            if current_number>=21:
                print('con so hien tai la',current_number)
                print('you Win')
                break
            current_player='human'
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break
    