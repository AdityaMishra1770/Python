import pygame
import random
import math
import sys

#initialize
pygame.init()

# Set up for screen 
screen = pygame.display.set_mode((750,499))

# Title and Icon
pygame.display.set_caption("Phoenix Fierce")
icon = pygame.image.load("C:\\Users\\Aditya Mishra\\Downloads\\_ec73611f-5de0-4440-b428-65636b11f622.jpg")
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load("C:\\Users\\Aditya Mishra\\Downloads\\phoenix1-removebg-preview.png")
playerX = 340
playerY = 300
playerX_change = 0
playerY_change = 0

# Blue bird
BlueImg = pygame.image.load("C:\\Users\\Aditya Mishra\\Downloads\\Blue_Bird-removebg-preview.png")
BlueX = random.randint(0,682)
BlueY = random.randint(0,200)
Blue_changeX = 0.35
Blue_changeY = 15


# Weapons 
Fire_state = "ready"  #We can't see ball at ready state and fire state fires the bullet 
fireballImg = pygame.image.load("D:\\download\\redball-removebg-preview.png")
fireX = 340
firey = 300
fire_ChangeY = 0.6
blueballImg = pygame.image.load("D:\\download\\magic-blue-fireball-flame-vector-25080053-removebg-preview.png")
blueballX = BlueX
blueballY = BlueY
blueBall_change = 0.42

# Background 
BackgroundImg = pygame.image.load("C:\\Users\\Aditya Mishra\\Downloads\\_9c9e3cec-0bbc-477e-a4bf-4a799b340e56.jpg")


# heart_image
heart_image = pygame.image.load("D:\\download\\heart-removebg-preview.png")
heart_image = pygame.transform.scale(heart_image,(50,60))

#starting image
startImg = pygame.image.load("D:\\download\\start1.jpg")
startImg = pygame.transform.scale(startImg,(750,499))
overlay = pygame.Surface((startImg.get_width(), startImg.get_height()))
overlay.set_alpha(40)
overlay.fill((0,0,0))
startImg.blit(overlay, (0,0))



# transforming image size
playerImg = pygame.transform.scale(playerImg,(75,100))
playerRect = playerImg.get_rect()
BlueImg = pygame.transform.scale(BlueImg,(75,100))
blueBirdRect = BlueImg.get_rect()
BackgroundImg = pygame.transform.scale(BackgroundImg,(780,550))
fireballImg = pygame.transform.scale(fireballImg,(40,50))
fireballImg = pygame.transform.flip(fireballImg,False,True)
FireRect = fireballImg.get_rect()
blueballImg = pygame.transform.scale(blueballImg,(40,50))
blueRect = blueballImg.get_rect()

# Creating font for image
font = pygame.font.SysFont(None, 36)
font2 = pygame.font.SysFont(None, 80)



# Score count and life
score = 0
life = 3
time = 0
clock = pygame.time.Clock()

# Image adding in screen
def player(img,x,y):
    screen.blit(img, (x,y))


def fireball_fire(x,y):
    global Fire_state 
    Fire_state = "fire"
    screen.blit(fireballImg,(x+22, y-38))

def BlueBall_fire(x3,y4):
    screen.blit(blueballImg,(x3+25, y4+38))



# when collision happens between fireball and blue bird
def isCollision(FireRect, blueBirdRect):
    return FireRect.colliderect(blueBirdRect)


# Game loop
running = False
dot_counter = 0

while not running:
    screen.fill((120,140,230))
    screen.blit(startImg,(0,0))
    start = font2.render("To Start Press Enter", True, (255,215,0))
    start_rect = start.get_rect()
    start_rect.center = (screen.get_width()//2, screen.get_height()//2 + 150)
    screen.blit(start, start_rect)
    dot = font.render(". "*dot_counter,True, (255, 215, 0))
    screen.blit(dot, ((screen.get_width()//2 +260), screen.get_height()//2 + 148))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = True
    pygame.display.update()
    dot_counter = (dot_counter + 1) % 7  # Cycle dot_counter between 0 and 3
    pygame.time.wait(250)

while running:
        # RGB format
    screen.fill((0,0,0))
    player(BackgroundImg,0,0)

    if score>= 25:
        running = False

    
    # playerX += 0.1
    # playerY -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or life<=0:
            running = False

    # If keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.25
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.25
            if event.key == pygame.K_UP:
                playerY_change = -0.25
            if event.key == pygame.K_DOWN:
                playerY_change = +0.25
            if event.key == pygame.K_SPACE:
                if Fire_state == "ready":
                    fireX = playerX
                    fireball_fire(fireX,firey)
    # Keystroke is released
        if event.type == pygame.KEYUP:
            playerY_change = 0   
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0            


    playerX += playerX_change
    playerY += playerY_change

# Player boundary
    if playerX >= 682 :
        playerX = 682
    if playerY>=400 :
        playerY = 400
    if playerX<1 :
        playerX = 1
    if playerY<240 :
        playerY = 240

# Blue Bird Boundary
    if BlueX >= 682 :
        BlueX = 682
        Blue_changeX = -0.28
        BlueY += Blue_changeY
    if BlueX <= 1 :
        BlueX = 1
        Blue_changeX = +0.28
        BlueY += Blue_changeY
    if BlueY <= 1 :
        BlueY = 1
    if BlueY>=150 :
        BlueY = 0
        BlueX = 0
    BlueX += Blue_changeX



    # Screen Image load
    player(BlueImg,BlueX,BlueY)
    player(playerImg,playerX,playerY)


    # Updating cemtre
    FireRect.topleft = (fireX, firey)
    playerRect.topleft = (playerX, playerY)
    blueRect.topleft = (blueballX, blueballY)
    blueBirdRect.topleft = (BlueX, BlueY)



    # persist fireball
    if Fire_state == "fire":
        fireball_fire(fireX,firey)
        firey -= fire_ChangeY
    if firey <= 0:
        firey = playerY
        Fire_state = "ready"

    if isCollision(FireRect, blueBirdRect):  
        firey = playerY
        Fire_state = "ready"
        score += 1
        BlueX = random.randint(0,682)
        BlueY = random.randint(0,200)

    if isCollision(blueRect, playerRect):
        life -= 1
        blueballX = BlueX
        blueballY = BlueY
    
    BlueBall_fire(blueballX, blueballY)
    blueballY += blueBall_change
    if blueballY >= playerY+60:
        blueballY = BlueY
        blueballX = BlueX

    # Draw the score and lives on the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {life}', True, (255, 255, 255))

    screen.blit(score_text, (635, 0))
    for i in range(life):
        screen.blit(heart_image, (692-i*52, 25))
    # Update everything
    pygame.display.update()


while (running == False and time<= 9050):
    time += 1
    screen.fill((255, 218, 185))
    text = "GAME"
    if(score >= 24):
        text = "GAME WON"
    else:
        text = "GAME OVER"
    success = font2.render(text,True, (65, 105, 225))
    success_rect = success.get_rect()
    success_rect.center = (screen.get_width()//2, screen.get_height()//2)
    screen.blit(success, success_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()