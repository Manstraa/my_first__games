import random
randomNumber = random.randint(1, 100)
howmany=0

while True:
    number=input('Guess a Number between 1 and 100  (Enter 0 to Exit):')
    howmany +=1
    if (number==0) :
        print('You Have Exited the Game')
        print('Number : {0}').format(randomNumber)
        break
    elif number >randomNumber :
        if howmany>=11:
            print('You have no rights')
            print('Number : {0}').format(randomNumber)
            break
        print('Enter a Smaller Number')
        continue
    elif number < randomNumber :
        if howmany>=11:
            print('You have no rights')
            print('Number : {0}').format(randomNumber)
            break
        print('Enter a   Larger  Number ')
        continue
    else :
        print('Congratulations You Nowwww!!! The Correct Number : {0} ').format(randomNumber)
        print('You Guessed {0} Times ').format(howmany)
        if howmany < 10 :
            print('You are very lucky')
            break
        elif howmany < 20 :
            print('You are lucky')
            break
        elif howmany < 35 :
            print('You are unlucky')
            break
        else:
            print('You are very bad')
            break
