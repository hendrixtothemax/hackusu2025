import pygame
import sys 

#Setting up screen width and height for the game
pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Sprout Land")

#Game colors
PASTEL_PINK = (255, 182, 193)
PASTEL_GREEN = (119, 221, 119)
WHITE = (255, 255, 255)

# Function to draw a simple banana shape
def draw_banana(x, y):
    # Draw the banana body (yellow ellipse)
    pygame.draw.ellipse(screen, YELLOW, (x, y, 300, 100))  # Body of the banana
    
    # Draw the tip of the banana (green curve)
    pygame.draw.arc(screen, GREEN, (x + 200, y - 30, 60, 60), 3.14, 2 * 3.14, 5)  # Tip curve
    
    # Draw the top end of the banana (brown stem)
    pygame.draw.rect(screen, BROWN, (x + 120, y - 20, 30, 10))  # Stem

#Setting up clock for frames
clock = pygame.time.Clock()

#Rectangle settings
rect_x, rect_y = 100, 100
rect_width, rect_height = 60, 40
rect_speed = 5


# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Move rectangle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rect_x -= rect_speed
    if keys[pygame.K_d]:
        rect_x += rect_speed
    if keys[pygame.K_w]:
        rect_y -= rect_speed
    if keys[pygame.K_s]:
        rect_y += rect_speed

 # Fill the screen with blue
    screen.fill(PASTEL_PINK)

    # Draw the red rectangle
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)
