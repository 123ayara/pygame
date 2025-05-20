import pygame
pygame.init()
screen_width, screen_height=500,500
display=pygame.display.set_mode((screen_width,screen_height))
background_image=pygame.transform.scale(
    pygame.image.load("on-wood-2106951_1280.jpg"),(screen_width, screen_height)
)
costume=pygame.transform.scale(
    pygame.image.load("penguin-9224527_1280.png"),(200,200)
)
costume_rect=costume.get_rect(center=(screen_width//2,screen_height//2-30))
text=pygame.font.Font(None,36).render("hello world",True,pygame.Color('black'))
text_rect=text.get_rect(center=(screen_width//2,screen_height//2+110))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display.blit(background_image,(0,0))
        display.blit(costume, costume_rect)
        display.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(320)
    pygame.quit()
if __name__=="__main__":
    game_loop()