#pygame setup
import pygame


pygame.init()
pygame.display.set_caption("Dare")
clock = pygame.time.Clock()
#variables 
display_width = 900
display_height = 900 
#image
screen = pygame.display.set_mode((display_width,display_height))
housebg= pygame.image.load('house.png')
hallway=pygame.image.load("hallway.png")
player1 = pygame.image.load('player1.png')
#button
playb = pygame.image.load('playbuttton.png')
quitb = pygame.image.load('quitbutton.png')

MOVEBACK = pygame.USEREVENT
pygame.time.set_timer(MOVEBACK, 500)
class Button():

    def __init__(self,image,pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    def update(self, screen):
       screen.blit(self.image, self.rect)
    def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
            return False
class Player():
    def __init__(self,image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self): 
        screen.blit(self.image, self.rect)

player = Player(player1, 450, 450)
monster = Player(pygame.image.load('monster.png'),-50,300)
def lose():
    while True: 
        
        screen = pygame.display.set_mode((display_width,display_height))
        screen.blit(pygame.image.load('losescreen.png'),(0,0))
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()  
                exit 

        pygame.display.update()       
def win():
    screen = pygame.display.set_mode((display_width,display_height))
    screen.blit(pygame.image.load('winscreen.png'),(0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit 
                    
        pygame.display.update()
def game():
    screen = pygame.display.set_mode((1400,display_height))
    while True: 
        screen.blit(hallway,(0,5))
        screen.blit(pygame.image.load("gametext.png"),(390,5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit
            if event.type == MOVEBACK:
                player.rect.x -= 50 
                monster.rect.x += 30

            if monster.rect.x >= player.rect.x : #how to stop it flashing? 
                # MOVEBACK.cancel() 
              lose()
                   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.rect.x += 30 

            if player.rect.x >= 1400:
                win()
           
        monster.update()        
        player.update()
        pygame.display.update()
        clock.tick(60)
def play ():
    while True :
        
        screen.blit(housebg,(0,0))
        screen.blit(pygame.image.load("introtextbox.png"),(15,50))
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                
                 
           
                
        pygame.display.update()
        clock.tick(60)
def main_menu (): 
    while True:
        screen.blit(pygame.image.load("titlescreen.png"),(0,0))
        menu_mouse_pos = pygame.mouse.get_pos()

        play_button = Button(playb, pos = (250,500))
        quit_button = Button(quitb, pos = (250,700))

        for button in [play_button, quit_button]:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                  play()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    exit()
                    
        pygame.display.update()
main_menu()


    