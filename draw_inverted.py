import pygame as pg

pg.init()
X = 1000
Y = 750
#screen under image
scrn = pg.display.set_mode((X, Y))
white = (255, 255, 255)
scrn.fill(white)
#pygame import image
pg_img = pg.image.load("fishHorz.png").convert()
pg_img = pg.transform.scale(pg_img,(1000,750))
rect = pg_img.get_rect()
pg.display.set_caption('pixel draw')
scrn.blit(pg_img, rect)
pg.display.flip()

status = True
while (status):

    #get mouse position 
    mouse_pos = pg.mouse.get_pos()

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pg.event.get():
        pg.draw.circle(scrn, (0), mouse_pos, 25)
        # print(mouse_pos)
        
        if i.type == pg.QUIT:
            status = False

        if i.type == pg.MOUSEBUTTONDOWN:
            inv = pg.Surface(pg_img.get_rect().size)
            inv.fill((255,255,255))
            inv.blit(pg_img, (0,0), None, pg.BLEND_RGBA_SUB)
            pg_img = inv
            scrn.blit(pg_img, (0,0))
            pg.display.flip()
            print("button clicked, inverse")
        if i.type == pg.MOUSEBUTTONUP:
            inv = pg.Surface(pg_img.get_rect().size)
            inv.fill((255,255,255))
            inv.blit(pg_img, (0,0), None, pg.BLEND_RGBA_SUB)
            pg_img = inv
            scrn.blit(pg_img, (0,0))
            pg.display.flip()
            print("mouse release")

    pg.display.update()

pg.quit()