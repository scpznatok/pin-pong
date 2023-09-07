from pygame import *
from random import randint 
from time import time as timer
import pygame.time as ticks
import pygame

win_width = 1000
win_height = 600
display.set_caption("ping-pong")
mw = display.set_mode((win_width, win_height))


pygame.init()

font.init()
text_font1 = font.SysFont("Arial", 100)


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


class Ball(GameSprite):

    def update(self):
        self.rect.y += self.speed * self.direction1
        self.rect.x += self.speed * self.direction

        if self.rect.y <= 5 or self.rect.y >= 550:
            self.direction1 = -self.direction1
    def res(self):
        self.direction1 = randint(1, 2)
        self.direction = randint(1, 2)
        if self.direction1 == 2:
            self.direction1 = -1
        if self.direction == 2:
            self.direction = -1
        print(self.direction, self.direction1)



class Button():
    def __init__(self, x, y, image, image_hover):
        self.image_original = image
        self.image_hover = image_hover
        self.rect = self.image_original.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
            self.image = self.image_hover
        else:
            self.image = self.image_original

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        mw.blit(self.image, self.rect)

        return action


ball = Ball("images/ball.png", 5, 470, 260, 50 , 50)
raketka_l = Player("images/raketka.png", 5, 10, 10, 25 , 200)
raketka_r = Player("images/raketka.png", 5, 965, 10, 25 , 200)
start_img = transform.scale(image.load("images/start_button.png"), (300, 85))
start_img_hover = transform.scale(image.load("images/start_button_hover.png"), (300, 85))
restart_img = transform.scale(image.load("images/restart_button.png"), (300, 85))
restart_img_hover = transform.scale(image.load("images/restart_button_hover.png"), (300, 85))
exit_img = transform.scale(image.load("images/exit_button.png"), (300, 85))
exit_img_hover = transform.scale(image.load("images/exit_button_hover.png"), (300, 85))
logo = transform.scale(image.load("images/logo.png"), (500, 500))
lose_logo = transform.scale(image.load("images/lose.png"), (500, 500))

raket_group = sprite.Group()
raket_group.add(raketka_l, raketka_r)


start_button = Button(350, 300, start_img, start_img_hover)
restart_button = Button(350, 300, restart_img, restart_img_hover)
exit_button = Button(350, 400, exit_img, exit_img_hover)

timer3 = text_font1.render("3", 1,(255,255,255),(0,0,0))
timer2 = text_font1.render("2", 1,(255,255,255),(0,0,0))
timer1 = text_font1.render("1", 1,(255,255,255),(0,0,0))
timer0 = text_font1.render("1", 1,(0,0,0),(0,0,0))

FPS = 60
clock = pygame.time.Clock()
Game = False
start_game = True
Menu = True
Main = True
Lose = False

while Main:
    for e in event.get():
            if e.type == QUIT:
                Main = False
    if Menu:
        mw.fill((0,0,0))
        mw.blit(logo, (245,-70))
        if start_button.draw():
            Menu = False
            Game = True
            ball.res()
            start_time = ticks.get_ticks()
        if exit_button.draw():
            Main = False
    
    if Game:
        mw.fill((0,0,0))
        raketka_l.update_l()
        raketka_l.reset()
        raketka_r.update_r()
        raketka_r.reset()
        ball.reset()
        if ticks.get_ticks() - start_time >= 1000 and ticks.get_ticks() - start_time <= 2000:
            mw.blit(timer3, (465,50))
        if ticks.get_ticks() - start_time >= 2000 and ticks.get_ticks() - start_time <= 3000:
            mw.blit(timer2, (465,50))
        if ticks.get_ticks() - start_time >= 3000 and ticks.get_ticks() - start_time <= 4000:
            mw.blit(timer1, (465,50))
        if ticks.get_ticks() - start_time >= 4000 and ticks.get_ticks() - start_time <= 4001:
            mw.blit(timer0, (465,50))
        if ticks.get_ticks() - start_time >= 4001 and ticks.get_ticks():
            ball.update()
        if sprite.spritecollide(ball, raket_group, False):
            ball.direction = -ball.direction
        print(ball.rect.x)
        if ball.rect.x >= 950 or ball.rect.x <= 5:
            Game = False
            Lose = True
    if Lose:
        mw.fill((0,0,0))
        mw.blit(lose_logo, (245,-70))
        if restart_button.draw():
            Menu = False
            Lose = False
            Game = True
            ball.res()
            ball.rect.x, ball.rect.y = 470, 260
            raketka_l.rect.y , raketka_r.rect.x = 10,965
            start_time = ticks.get_ticks()
        if exit_button.draw():
            Main = False
    clock.tick(FPS)
    display.update()
    time.delay(50)