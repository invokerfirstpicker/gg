    from pygame import *

    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (65, 65))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
            
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
            
    class Player(GameSprite):
        def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += self.speed
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_height - 80:
                self.rect.y += self.speed
        def collidrect(self,rect):
            return self.rect.colliderect(rect)
            
        

    class Enemy(GameSprite):
        direction = "left"
        def update(self):
            if self.rect.x <= 470:
                self.direction = "right"
            if self.rect.x >= win_width - 85:
                self.direction = "left"
            if self.direction == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
    class Wall():
        def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height,):
            self.width = wall_width
            self.height = wall_height
            self.color_1 = color_1
            self.color_2 = color_2
            self.color_3 = color_3
            self.image = Surface((self.width,self.height))
            self.image.fill((color_1,color_2,color_3))
            self.rect = self.image.get_rect()
            self.rect.x = wall_x
            self.rect.y = wall_y
        def draw_wall(self):
            window.blit(self.image,(self.rect.x,self.rect.y))
    win_width = 700
    win_height = 500
    window = display.set_mode((win_width, win_height))
    display.set_caption("Maze")
    background = transform.scale(image.load("background.jpg"), (win_width, win_height))
    font.init()
    f1 = font.Font(None, 100)
    text1 = f1.render('YOU WON', True,(180, 0, 0))

    f2 = font.Font(None, 100)
    text2 = f2.render('YOU LOSE', True,(180, 0, 0))

    
    player = Player('hero.png', 5, win_height - 80, 4)
    monster = Enemy('cyborg.png', win_width - 80, 280, 2)
    final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
    w1 = Wall(154,205,50,0,400,350,10)
    w2 = Wall(154,205,50,300,00,10,400)
    w3 = Wall(154,205,50,450,100,10,500)
    game = True
    finish = False
    clock = time.Clock()
    FPS = 60

    #mixer.init()
    #mixer.music.load('jungles.ogg')
    #mixer.music.play()
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
        if finish != True:
            window.blit(background,(0, 0))
            player.update()
            monster.update()
            player.reset()
            monster.reset()
            final.reset()
            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            if player.collidrect(final):
                window.blit(text1, (win_width//2, win_height//2))
                finish = True
            if player.collidrect(monster):
                window.blit(text2, (win_width//2, win_height//2))
                finish = True
            if player.collidrect(w1):
                window.blit(text2, (win_width//2, win_height//2))
                finish = True
            if player.collidrect(w2):
                window.blit(text2, (win_width//2, win_height//2))
                finish = True
            if player.collidrect(w3):
                window.blit(text2, (win_width//2, win_height//2))
                finish = True
            

        
        display.update()
        clock.tick(FPS)
