"""import pygame, os


WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect((WIDTH/2)-5, 0, 10, HEIGHT)

FPS = 30
VEL = 5
BULLET_VEL = 7

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("coolProjects/snake/Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("coolProjects/snake/Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), -90)

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VEL < BORDER.x: #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height + VEL < HEIGHT-10: #down
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH: #right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + red.height + VEL < HEIGHT-10: #down
        red.y += VEL

def draw_window(red, yellow):
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, BORDER)
    win.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    win.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    pass
                if event.key == pygame.K_RCTRL:
                    pass
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
"""


