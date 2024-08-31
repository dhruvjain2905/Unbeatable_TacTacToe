from math import inf as infinity
import pygame


pygame.init()

screen = pygame.display.set_mode((900,1000))

image = pygame.image.load("Downloads/tic.png")



board = [' ' for x in range(10)]
def play_again():
    board[0] = ' '
    board[1] = ' '
    board[2] = ' '
    board[3] = ' '
    board[4] = ' '
    board[5] = ' '
    board[6] = ' '
    board[7] = ' '
    board[8] = ' '
    board[9] = ' '


def show_move(letter, pos):
    the_font = pygame.font.Font("freesansbold.ttf", 256)
    show = the_font.render(letter, True, (255,255,255))
    screen.blit(show,pos)

def mod_show_move(letter, pos, size):
    the_font = pygame.font.Font("freesansbold.ttf", size)
    show = the_font.render(letter, True, (255,255,255))
    screen.blit(show,pos)


def insertLetter(letter, pos):
  board[pos] = letter


def spaceIsFree(pos):
  return board[pos] == ' '

def printBoard(board):
  screen.fill((0,0,0))
  pygame.draw.line(screen,(255,255,255),(300,0),(300,900),10)
  pygame.draw.line(screen,(255,255,255),(600,0),(600,900),10)
  pygame.draw.line(screen,(255,255,255),(0,300),(900,300),10)
  pygame.draw.line(screen,(255,255,255),(0,600),(900,600),10)
  pygame.draw.line(screen,(255,255,255),(0,900),(900,900),10)
  show_move(board[1],(75,15))
  show_move(board[2],(375,15))
  show_move(board[3],(675,15))
  show_move(board[4],(75,315))
  show_move(board[5],(375,315))
  show_move(board[6],(675,315))
  show_move(board[7],(75,615))
  show_move(board[8],(375,615))
  show_move(board[9],(675,615))



def isWinner(bo, le):
  return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
          (bo[4] == le and bo[5] == le and bo[6] == le) or 
          (bo[1] == le and bo[2] == le and bo[3] == le) or 
          (bo[1] == le and bo[4] == le and bo[7] == le) or 
          (bo[2] == le and bo[5] == le and bo[8] == le) or 
          (bo[3] == le and bo[6] == le and bo[9] == le) or 
          (bo[1] == le and bo[5] == le and bo[9] == le) or 
          (bo[3] == le and bo[5] == le and bo[7] == le))

def evaluate(bo):
  if isWinner(bo,'o'):
    var = 1
  elif isWinner(bo,'x'):
    var = -1
  else:
    var = 0
  return var
  

mouseX = 0
mouseY = 0

def isBoardFull(board):
  if board.count(' ') > 1:
    return False
  else:
    return True

move = 0

def playerMove():
  global mouseX, mouseY, move
  mouseX = 0
  mouseY = 0
  move = 0
  run = True
  while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()


    if (mouseX < 300 and mouseX > 0) and (mouseY < 300 and mouseY > 0):
        move = 1
    elif (mouseX < 600 and mouseX > 300) and (mouseY < 300 and mouseY > 0):
        move = 2
    elif (mouseX < 900 and mouseX > 600) and (mouseY < 300 and mouseY > 0):
        move = 3
    elif (mouseX < 300 and mouseX > 0) and (mouseY < 600 and mouseY > 300):
        move = 4
    elif (mouseX < 600 and mouseX > 300) and (mouseY < 600 and mouseY > 300):
        move = 5
    elif (mouseX < 900 and mouseX > 600) and (mouseY < 600 and mouseY > 300):
        move = 6
    elif (mouseX < 300 and mouseX > 0) and (mouseY < 900 and mouseY > 600):
        move = 7
    elif (mouseX < 600 and mouseX > 300) and (mouseY < 900 and mouseY > 600):
        move = 8
    elif (mouseX < 900 and mouseX > 600) and (mouseY < 900 and mouseY > 600):
        move = 9


    printBoard(board)
    mod_show_move("Your turn",(365,925),40)
    pygame.display.update()

    if (move>0 and move<10):
        if spaceIsFree(move):
          run = False
          insertLetter('x', move)
          printBoard(board)
          pygame.display.update()
        


def possibleMoves(boa):
  return [x for x, letter in enumerate(boa) if letter == ' ' and x != 0]



def game_over(state):
  return isWinner(state,'x') or isWinner(state, 'o')


def minimax(board, depth, player):          
  

  if player == 'o':
    best = [-1, -infinity]
  else:
    best = [-1, +infinity]
    

  if depth == 0 or game_over(board) or isBoardFull(board):
    score = evaluate(board)
    return [-1,score]


  for cell in possibleMoves(board):                                  
    board[cell] = player                                                         
    if player == 'o':                                
      score = minimax(board, depth-1,'x')
    else:
      score = minimax(board, depth-1,'o')

    board[cell] = ' '
    score[0] = cell
     

    if player == 'o':
      if score[1] > best[1]:
        best = score
    else:
      if score[1] < best[1]:
        best = score
  return best
    
    





print('Hello and welcome to tic-tac-toe')
print('Please Begin')
print('You may go first')




    

def main():
    printBoard(board)
    pygame.display.update()

    while True:
        
        

        
        
        if isBoardFull(board) or isWinner(board, 'o'):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    play_again()
                    main()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            printBoard(board)
            mod_show_move("Click to restart",(310,925),40)
            pygame.display.update()
        else:


        
        
            playerMove()
            if not isBoardFull(board):
                depth = len(possibleMoves(board))
                t = minimax(board, depth, 'o')[0]
                insertLetter('o', t)
                print('Computer placed on: '+str(t))



            printBoard(board)
            pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            main()
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0,0,0))
    mod_show_move("Hello and Welcome",(100,200),50)
    mod_show_move("To Tic-Tac-Toe",(100,300),50)
    mod_show_move("Click to start",(100,400),40)
    #mod_show_move("You may go first",(100,500),25)
    screen.blit(image,(500,500))
    pygame.display.update()
    
