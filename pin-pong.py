from pygame import *
init()
from random import *
mixer.init()



class GameSprite(sprite.Sprite):
    def __init__ (self, image_name, speed, x, y, size ):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
       
        keys = key.get_pressed()
           
        if keys[K_UP] and self.rect.x > self.speed + 5:
           self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.x - self.speed + 5:
           self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
       
        keys = key.get_pressed()
           
        if keys[K_w] and self.rect.x > self.speed + 5:
           self.rect.y -= self.speed
        elif keys[K_s] and self.rect.x - self.speed + 5:
           self.rect.y += self.speed


class Ball(GameSprite):
    
    def update(self):
        global direction
        global direction2
        global player1

        if direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if direction2 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        if self.rect.y >= 470:
            direction2 = 'up'
        if self.rect.y <= 25:
            direction2 = 'down'

        if self.rect.colliderect(player1):
            direction = 'left'
        if self.rect.colliderect(player2):
            direction = 'right'


win = display.set_mode((700, 500))
display.set_caption('Пин-понг')
clock = time.Clock()
direction = 'right'
direction2 = 'up'

background = transform.scale(image.load('fons.jpg'), (700, 500))

ball = Ball('ball.jpg', 2, 250, 250, (60, 60))
player2 = Player2('player.jpg', 4, 100, 250, (20, 90))
player1 = Player1('player.jpg', 4, 600, 250, (20, 90))


game = True
while game:
    win.blit(background, (0, 0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    player1.reset()
    player2.reset()
    ball.reset()

    player1.update()
    player2.update()
    ball.update()
    
    clock.tick(60)
    display.update()