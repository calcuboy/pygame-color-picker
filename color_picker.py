"""
author: tpig
2023/12/23
"""


import os
import pygame
# import pyperclip

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def copy_to_clip(text):
    command = 'echo ' + text.strip() + ' | clip'
    os.system(command)

colors = []
for item in  pygame.colordict.THECOLORS.items():
    colors.append(item)
# print(colors)

pygame.init()
font = pygame.font.SysFont(None, 32)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bw = SCREEN_WIDTH // 20
bh = SCREEN_HEIGHT // 35

mouse_rect = pygame.Rect(0, 0, bw, bh)
cur_color_name = ""

running = True
while running:
    # event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONUP:
            # copy cur_color_name to clipboard
            # pyperclip.copy(cur_color_name)
            copy_to_clip(cur_color_name)

    # update
    mouse_pos = pygame.mouse.get_pos()
    mouse_line = mouse_pos[1] // bh
    mouse_col = mouse_pos[0] // bw
    mouse_rect.x = mouse_col * bw
    mouse_rect.y = mouse_line * bh

    idx = mouse_line * 20 + mouse_col
    if idx < len(colors):
        cur_color_name =  colors[idx][0]

    # draw
    screen.fill("black")


    for line in range(35):
        for col in range(20):
            idx = line * 20 + col
            if idx < len(colors):
                pygame.draw.rect(screen,
                                 colors[idx][1],
                                 (col * bw, line*bh, bw, bh) )


    # draw mouse rect
    pygame.draw.rect(screen, "yellow", mouse_rect, 2)

    # draw color name
    font_sur = font.render(f"Color Name: {cur_color_name}", True, "white")
    screen.blit(font_sur, (260, SCREEN_HEIGHT - 30))

    pygame.display.flip()

    # clock
    clock.tick(60)
