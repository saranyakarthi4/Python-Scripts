player1 = input('what is player 1 move?')
player2 = input('what is player 2 move?')
# Game: Stone Paper Scissor 
if player1 == player2:
    print ('DRAW')
else:
    if (player1 =='Stone' and player2 =='Paper'):
        print ('Player 2 Wins')
    elif (player2 =='Stone' and player1 =='Paper'):
        print ('Player 1 Wins')
    elif (player1 =='Stone' and player2 =='Scissor'):
        print ('Player 1 Wins')
    elif (player2 =='Stone' and player1 =='Scissor'):
        print ('Player 2 Wins')
    elif (player1 =='Paper' and player2 =='Scissor'):
        print ('Player 2 Wins')
    elif (player2 =='Paper' and player1 =='Scissor'):
        print ('Player 1 Wins')



# Player A   Player B    Result
# Stone       Stone      DRAW
# Stone       Paper   Player B wins
# Stone       Scissor Player A wins

# Paper       Stone   Player A wins
# Paper       Paper   DRAW
# Paper       Scissor Player B wins
# Scissor     Scissor DRAW
# Scissor     Stone   Player B wins
# Scissor     Paper   Player A wins



