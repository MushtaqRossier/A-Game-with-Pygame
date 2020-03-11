import pygame
import random

#Initialize the pygame modules to get everything started.
pygame.init()

#Sets the dimensions of the game window.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

#------------------------------------------------------------------------------
#This creates the characters in the game and gives them the images found in this folder.
player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("alien1.png")
enemy3 = pygame.image.load("alien2.png")
prize = pygame.image.load("prize.jpg")
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#This gets the width and height of each character in order to do boundary detection.
player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Store the positions of the player and enemy as variables so that you can change them later
player_X_Position = 100
player_Y_Position = 50

#Make the enemy start off screen and at a random y position.
enemy1_X_Position = screen_width - 100 
enemy1_Y_Position = random.randint(0, screen_height - enemy1_height)

enemy2_X_Position = screen_width - 200
enemy2_Y_Position = random.randint(0, screen_height - 200)

enemy3_X_Position = screen_width - 300
enemy3_Y_Position = random.randint(0, screen_height - 400)

prize_X_Position = screen_width/2
prize_Y_Position =  random.randint(0, screen_height/2)
#------------------------------------------------------------------------------

#This checks whether the arrow keys are being pressed
#We set them to boolean values because they are not being pressed at the moment
key_up = False
key_down = False
key_right = False
key_left = False

#------------------------------------------------------------------------------
#This is the game loop
#The loop needs to refresh/update the screen window and apply changes to
while 1:
    screen.fill(0) #This clears the screen
    
    #This positions the characters on the screen where specified
    screen.blit(player, (player_X_Position, player_Y_Position))
    screen.blit(enemy1, (enemy1_X_Position, enemy1_Y_Position))
    screen.blit(enemy2, (enemy2_X_Position, enemy2_Y_Position))
    screen.blit(enemy3, (enemy3_X_Position, enemy3_Y_Position))
    screen.blit(prize, (prize_X_Position, prize_Y_Position))
    

    pygame.display.flip()  #This updates the screen

    #This loops through events in the game
    for event in pygame.event.get():
        #This event checks if the user quits the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #This event checks if the user presses a key down 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up = True
            if event.key == pygame.K_DOWN:
                key_down = True
            if event.key == pygame.K_RIGHT:
                key_right = True
            if event.key == pygame.K_LEFT:
                key_left = True

        #This event checks if the key is not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False
            if event.key == pygame.K_RIGHT:
                key_right = False
            if event.key == pygame.K_LEFT:
                key_left = False
    #After events are checked for in the for loop above and values are set,
    #Check key pressed values and move player accordingly.
    
    #The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    #This means that if you want the player to move down you will have to increase the y position. 
    #Sets the boundaries for the movement of the player character
    if key_up == True :
        if player_Y_Position > 0:
            player_Y_Position -= 0.5
           
    if key_down == True:
        if player_Y_Position < screen_height - player_height:
            player_Y_Position += 0.5
            
    if key_right == True:
        if player_X_Position > 0:
            player_X_Position += 0.5
    if key_left == True:
        if player_X_Position < screen_width - player_width:
            player_X_Position -= 0.5
             

    #Sets boxes for the characters in the game.
    #Use boxes to test for collisions for characters
    player_box = pygame.Rect(player.get_rect())
    player_box.top = player_Y_Position
    player_box.left = player_X_Position

    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy1_box.top = enemy1_Y_Position
    enemy1_box.left = enemy1_X_Position

    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy2_box.top = enemy2_Y_Position
    enemy2_box.left = enemy2_X_Position

    enemy3_box = pygame.Rect(enemy3.get_rect())
    enemy3_box.top = enemy3_Y_Position
    enemy3_box.left = enemy3_X_Position

    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_Y_Position
    prize_box.left = prize_X_Position

    #Tets for collisions of boxes
    #If player box collides with enemy boxes then you lose the game
    if (player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box)):
        print("You lose")
        pygame.quit()
        exit(0)

    #If player box collides with prize box then you win the game
    if player_box.colliderect(prize_box):
        print("You win")
        pygame.quit()
        exit(0)

    #Makes the enemy approach the player
    enemy1_X_Position -= 0.1
    enemy2_X_Position -= 0.1
    enemy3_X_Position -= 0.1
#------------------------------------------------------------------------------    
    
