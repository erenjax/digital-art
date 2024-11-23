import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 750))
clock = pygame.time.Clock()

pg_img = pygame.image.load("fishHorz.png").convert()
pg_img = pygame.transform.scale(pg_img,(1000,750))
rect = pg_img.get_rect()
pygame.display.set_caption('pixel flashlight')
# screen.blit(pg_img, rect)

cover_surf = pygame.Surface((1000, 750))
cover_surf.set_colorkey((255, 255, 255))
inv_surf = pygame.Surface((1000, 750))
inv_surf.set_colorkey((255, 255, 255))

px = [90, 200, 500]
dx = [1, 2, 3] 

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            inv = pygame.Surface(pg_img.get_rect().size)
            inv.fill((255,255,255))
            inv.blit(pg_img, (0,0), None, pygame.BLEND_RGBA_SUB)
            pg_img = inv
            inv_surf.fill((0, 0, 255))
            inv_surf.blit(pg_img, (0,0))
            pygame.display.flip()
            print("button clicked, inverse")
        if event.type == pygame.MOUSEBUTTONUP:
            inv = pygame.Surface(pg_img.get_rect().size)
            inv.fill((255,255,255))
            inv.blit(pg_img, (0,0), None, pygame.BLEND_RGBA_SUB)
            pg_img = inv
            inv_surf.set_colorkey((255, 255, 255))
            print("mouse release")

    # create cover surface
    cover_surf.fill(0)
    for i in range(3):
        radius = 60 + i*50
        pygame.draw.circle(cover_surf, (255, 255, 255), (px[i], 90+(i*200)), radius)
        px[i] += dx[i]
        if px[i] < radius or px[i] > 1000 - radius:
            dx[i] = -dx[i]
        
    # draw the scene (image)
    screen.blit(pg_img, rect)

    # draw transparent circle and update display
    screen.blit(cover_surf, (0, 0))
    pygame.display.flip()