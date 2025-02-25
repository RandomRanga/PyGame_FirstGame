import pygame
import os



#pygame window 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#renames the window
pygame.display.set_caption("First Game")

#Color white
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

BORDER_WIDTH = 10
BORDER = pygame.Rect(WIDTH/2 - BORDER_WIDTH, 0, BORDER_WIDTH, HEIGHT)

FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 7

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#imports the images and then resizes and rotates. 
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)


def draw_window(yellow, red, red_bullets, yellow_bullets):
    #Gives the window a background
    WIN.fill(WHITE)
    
    #draws the images onto the window at the pos of the yellow and red rects
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    #draws border use .draw as it is a simple shape not an image 
    pygame.draw.rect(WIN, BLACK, BORDER)

    
    for bullet in yellow_bullets: 
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullet in red_bullets: 
        pygame.draw.rect(WIN, RED, bullet)


    #Updates the display
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    #moves yellow ship left if a is pressed. 
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: #left key 
        yellow.x -= VELOCITY 
    #moves yellow ship right if d is pressed.
    if keys_pressed[pygame.K_d]and yellow.x + VELOCITY + yellow.width < BORDER.x: #right key 
        yellow.x += VELOCITY 
    #moves yellow ship up if w is pressed.
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: #up key 
        yellow.y -= VELOCITY 
    #moves yellow ship down if s is pressed.
    if keys_pressed[pygame.K_s]and yellow.y + VELOCITY + yellow.height < HEIGHT - 15: #down key 
        yellow.y += VELOCITY 
def red_handle_movement(keys_pressed, red):
    #moves yellow ship left if left arrow is pressed. Ensures can't move past boarder.
    if keys_pressed[pygame.K_LEFT]and red.x - VELOCITY > BORDER.x + BORDER.width: #left key 
        red.x -= VELOCITY 
    #moves yellow ship right if right arrow is pressed. Ensures can't move out of window.
    if keys_pressed[pygame.K_RIGHT]and red.x + VELOCITY + red.width < WIDTH: #right key 
        red.x += VELOCITY 
    #moves yellow ship up if up arrow is pressed. Ensures can't move out of window.
    if keys_pressed[pygame.K_UP]and red.y - VELOCITY > 0: #up key 
        red.y -= VELOCITY 
    #moves yellow ship down if down arrow is pressed. Ensures can't move out of window.
    if keys_pressed[pygame.K_DOWN]and red.y + VELOCITY + red.height < HEIGHT - 15: #down key 
        red.y += VELOCITY 
    



def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets: 
        bullet.x += BULLET_VELOCITY

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
      








#Main function
def main():

    #Creates rectangles to then put the spaceships inside
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    #To make game run until false 
    run = True
    while run:
        #ensures that never goes faster than assigned FPS
        clock.tick(FPS)
        #Checks for events occuring in pygame 
        for event in pygame.event.get():
            #Checks for the quit event
            if event.type == pygame.QUIT:
                run = False

            #Checks if a key has been pressed 
            if event.type == pygame.KEYDOWN:
                #Checks if the key pressed was left control then 
                if event.key == pygame.K_LCTRL:
                    #Creates the bullet and adds to the list 
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 3, 10, 6)
                    yellow_bullets.append(bullet)


                if event.key == pygame.K_RCTRL:
                    #Creates the bullet and adds to the list 
                    bullet = pygame.Rect(red.x, red.y + yellow.height/2 - 3, 10, 6)
                    red_bullets.append(bullet)


        #Tells us which keys are being pressed/ held down
        keys_pressed = pygame.key.get_pressed()
        #Calls fuctions for moving both ships
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        #runs draw window fuction with red and yellow passed in. 
        draw_window(yellow, red, yellow_bullets, red_bullets)
        
        
    pygame.quit()

# Run main() only if this script is executed directly
if __name__ == "__main__":
    main()