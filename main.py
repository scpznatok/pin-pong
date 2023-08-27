from pygame import *


win_width = 1000
win_height = 600
display.set_caption("ping-pong")
mw = display.set_mode((win_width, win_height))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x , player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 :
            self.rect.y -=self.speed
        elif keys[K_s] and self.rect.y < 390 :
            self.rect.y +=self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -=self.speed
        elif keys[K_DOWN] and self.rect.y < 390 :
            self.rect.y +=self.speed

raketka_l = Player("images/raketka.png", 5, 10, 10, 25 , 200)
raketka_r = Player("images/raketka.png", 5, 965, 10, 25 , 200)

Game = True

while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    mw.fill((0,0,0))
    raketka_l.update_l()
    raketka_l.reset()
    raketka_r.update_r()
    raketka_r.reset()
    
    
    
    
    display.update()
    time.delay(50)