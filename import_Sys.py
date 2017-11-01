import random
def getAnswer(ansNumber):
        if ansNumber == 1:
           return 'It is certain'
        elif ansNumber == 2:
           return 'It is decidedly so'
        elif ansNumber == 3:
           return 'Yes'
        elif ansNumber == 4:
           return 'Reply hazy try again'
        elif ansNumber == 5:
           return 'Ask again later'
        elif ansNumber == 6:
           return 'Concentrate and ask again'
        elif ansNumber == 7:
           return 'My reply is no'
        elif ansNumber == 8:
           return 'Outlook not so good'
        elif ansNumber == 9:
           return 'Very doubtful'
r=random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
