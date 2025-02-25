import pygame

#pygame window 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#renames the window
pygame.display.set_caption("First Game")

#Main function
def main():
    #To make game run until false 
    run = True
    while run:
        #checks for events occuring in pygame 
        for event in pygame.event.get():
            #Checks for the quit event
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()

# Run main() only if this script is executed directly
if __name__ == "__main__":
    main()