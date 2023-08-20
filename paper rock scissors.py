import random

computer_score=0
user_score=0

while True:
    computer  = ('paper','rock','scissors')
    
    comchoice = random.choice(computer)
    
    unserchoice = input("paper , rock or scissors !! : ")
    while unserchoice not in(computer):
        unserchoice = input("paper , rock or scissors !! : ")
    'rokh'>'cut'
    'paper'>'rock'
    'cut'>'paper'

    
    if unserchoice == comchoice:

        print ('ITS A TIE ! computer choice is :',comchoice,'your choice is :',unserchoice)
    
    if unserchoice < comchoice: 
        user_score = user_score + 1 
        print ('YOU WON! computer choice is :',comchoice,'your choice is :',unserchoice)
    
    if unserchoice > comchoice:
        computer_score = computer_score + 1
        print ('COMPUTER WON! computer choice is :',comchoice,'your choice is :',unserchoice)

    
    yn=('y','n','Y','N')
    continue_yn = input("continue (y/n) ? : ")
    while continue_yn not in (yn):
        continue_yn = input("continue (y/n) ? : ")

    if continue_yn.lower() != 'y':
        break
    
    
    if computer_score == 3 :
        print (" YOU LOSE , ITS : computer",computer_score ," | ",user_score,"you")
        break

    if user_score == 3 :
        print (" YOU WON , ITS : computer",computer_score ," | ",user_score,"you")
        break


