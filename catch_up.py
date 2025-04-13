from pygame import *
from math import sqrt

init()

def is_sprite_collide(coord1, coord2):
    return sqrt((coord2[0] - coord1[0])**2+ (coord2[1] - coord1[1]**2)) < 25



window = display.set_mode((700,500))
clock = time.Clock()

text_render = font.SysFont('Arial', 36)

display.set_caption('Догонялки')

background_image = transform.scale(image.load('background.png'), (700,500))

player_1 = transform.scale(image.load('sprite1.png'), (60,60))

player_2 = transform.scale(image.load('sprite2.png'), (60,60))

player_1_coords = [100,200]

player_2_coords = [500,290]

window.blit(background_image, (0,0))

game = True

while game:

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP]:
        player_2_coords[1] -= 10

    if keys_pressed[K_DOWN]:
        player_2_coords[1] += 10

    if keys_pressed[K_RIGHT]:
        player_2_coords[0] += 10

    if keys_pressed[K_LEFT]:
        player_2_coords[0] -= 10

    if keys_pressed[K_w]:
        player_1_coords[1] -= 10

    if keys_pressed[K_s]:
        player_1_coords[1] += 10

    if keys_pressed[K_a]:
        player_1_coords[0] -= 10

    if keys_pressed[K_d]:
        player_1_coords[0] += 10


    if is_sprite_collide(player_1_coords, player_2_coords):
        game = False
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background_image, (0,0))
    window.blit(player_1,(player_1_coords[0],player_1_coords[1]))
    window.blit(player_2,(player_2_coords[0],player_2_coords[1]))
    window.blit(text_render.render('0 point', True, (139, 0, 0)), (100,20))
    window.blit(text_render.render('0 point', True, (139, 0, 0)), (500,20))
    display.update()
    clock.tick(60)

