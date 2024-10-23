import pygame

pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDHT = 1000
display_surface = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
pygame.display.set_caption("Crtanje")



# Set colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)


# Define the rectangle's position and dimensions
rect_x = 500
rect_y = 200
rect_width = 200
rect_height = 150

# Define the rectangle's position and dimensions
rect_x1 = 100
rect_y1 = 100
rect_width = 200
rect_height = 150

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     #Fil the display
    display_surface.fill(BLACK)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDHT, 64), 2)
    pygame.draw.rect(display_surface, (0, 0, 255), (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(display_surface, WHITE, (rect_x1, rect_y1, rect_width, rect_height))

    pygame.display.update()


pygame.quit()