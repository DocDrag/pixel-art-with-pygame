import pygame
import os
import xy

# ดึงตำแหน่ง x y จากในไฟล์
p = xy.p

pygame.init()

width, height = 375, 500

# กำหนดตำแหน่งหน้าต่างไปที่มุมขวาของหน้าจอ
os.environ["SDL_VIDEO_WINDOW_POS"] = (
    f"{pygame.display.Info().current_w - (width+50)},100"
)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display Image Pixel by Pixel")


running = True
clock = pygame.time.Clock()

x, y = 0, 0
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if x < width and y < height:
        color = (255, 255, 255)

        pygame.draw.rect(screen, color, (p[count]["x"], p[count]["y"], 1, 1))

        x += 1
        if x >= width:
            x = 0
            y += 1

        if count < len(p) - 1:
            count += 1
    else:
        running = False

    pygame.display.flip()
    clock.tick(5000)

pygame.quit()