import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Starter")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 182, 193)
PASTEL_GREEN = (119, 221, 119)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Rectangle settings
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
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill the screen with blue
    screen.fill(PASTEL_GREEN)

    # Draw the red rectangle
    pygame.draw.rect(screen, PINK, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)
