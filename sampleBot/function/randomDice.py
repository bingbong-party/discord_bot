import random

def getRandomDiceNumber():
    botNumber = random.randint(1, 6)
    userNumber = random.randint(1, 6)

    if botNumber > userNumber:
        result = '패배'
        barColor = 0xFF0000
    elif botNumber == userNumber:
        result = '무승부'
        barColor = 0x808080
    else:
        result = '승리'
        barColor = 0x00ff56

    return result, barColor, botNumber, userNumber