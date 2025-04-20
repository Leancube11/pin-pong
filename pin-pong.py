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
           
        if keys[K_a] and self.rect.x > self.speed + 5:
           self.rect.y -= self.speed
        elif keys[K_d] and self.rect.x - self.speed + 5:
           self.rect.y += self.speed

class Ball(GameSprite):
    
    def update(self):
        if direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if direction2 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed


win = display.set_mode((700, 500))
display.set_caption('Пин-понг')
clock = time.Clock()
background = transform.scale(image.load('fon'), (700, 500))


game = True
while game:
    win.blit(background, (0, 0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    

    

    clock.tick(60)
    display.update()