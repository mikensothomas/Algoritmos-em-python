import pygame

from pygame.sprite import Sprite


pygame.init()

width=800
height=600
FPS=50


screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Teste')
clock=pygame.time.Clock()
running=True

player= Sprite()
player.image=pygame.Surface((32,32))
player.image.fill((35,35,35))
player.rect=player.image.get_rect()
player.rect.center=(width/2,height/2)
while running:
    delta=clock.tick(FPS)/1000
    for evento in pygame.event.get():
        if evento.type==pygame.quit:
            running=False
    screen.fill((45,156,200))
    screen.blit(player.image,player.rect)
    pygame.display.flip()
    
pygame.quit()