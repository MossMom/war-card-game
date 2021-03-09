# Import libraries and initialize the game engine
import pygame
import random

pygame.init()

# Open new window, caption it "War", also grab fonts
print(pygame.font.get_fonts())
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("War")

# Here's the variable that runs our game loop
doExit = False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Text/Font stuff

class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def draw(self, x, y):
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 180))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 100, 180), 3)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text1 = font.render(str(self.number), False, (0, 0, 0))
        text2 = font.render(str(self.suit), 1, (230, 0, 0))
        screen.blit(text1, (x+30, y+30))
        screen.blit(text2, (x+10, y+60))
        
# Create deck list & all 52 cards
# Jack is 11, queen is 12, king is 13
Deck = list()
for j in range(4):
    for i in range(13):
        Deck.append(card(j,i))
random.shuffle(Deck)

p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list()

for i in range(26):
    p1hand.append(Deck[i])

for j in range(26, 52):
    p2hand.append(Deck[j])

turn = False

while not doExit: #GAME LOOP----------------------------------------------------
    
    # Event queue stuff
    
    clock.tick(60) # FPS


    for event in pygame.event.get(): # Check if user did something
        if event.type == pygame.QUIT: # Check if user clicked close
            doExit = True # Flag that we are done so we exit the game loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            turn = True
        if event.type == pygame.MOUSEBUTTONUP:
            turn = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    # Game logic will go here---------------------------------------------------
    
    if len(p1hand) <= 0 or len(p2hand) <= 0:
        if len(p1Discard) > len(p2Discard):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        doExit = True
    
    
    if turn and len(p1hand) > 0 and len(p2hand) > 0:
        if p1hand[len(p1hand)-1].number > p2hand[len(p2hand)-1].number:
            print("Player 1 wins this round!")
            p1Discard.append(p1hand[len(p1hand)-1])
            p1Discard.append(p2hand[len(p2hand)-1])
            p1hand.pop(len(p1hand)-1)
            p2hand.pop(len(p2hand)-1)
        else:
            if p1hand[len(p1hand)-1].number < p2hand[len(p2hand)-1].number:
                print("Player 2 wins this round!")
                p2Discard.append(p1hand[len(p1hand)-1])
                p2Discard.append(p2hand[len(p2hand)-1])
                p1hand.pop(len(p1hand)-1)
                p2hand.pop(len(p2hand)-1)
            else:
                if p1hand[len(p1hand)-1].number == p2hand[len(p2hand)-1].number:
                    print("It's a tie, both cards get discarded!")
                    p1Discard.append(p1hand[len(p1hand)-1])
                    p2Discard.append(p2hand[len(p2hand)-1])
                    p1hand.pop(len(p1hand)-1)
                    p2hand.pop(len(p2hand)-1)
        
    
    # Render section will go here ----------------------------------------------
    
    # Wipe screen green
    screen.fill((37,124,65))
    
    # Draw cards
    for i in range (len(p1hand)):
        p1hand[i].draw(100+(i*5), 50)
    for i in range (len(p2hand)):
        p2hand[i].draw(100+(i*5), 250)
        
    for i in range (len(p1Discard)):
        p1Discard[i].draw(500-(i*5), 50)
    for i in range (len(p2Discard)):
        p2Discard[i].draw(500-(i*5), 250)
    
    # Update the screen
    pygame.display.flip()
    
# END OF GAME LOOP--------------------------------------------------------------

pygame.quit() # When game is done close down pygame