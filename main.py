#imports

import pygame as pg
import random
#import the .py file with the settings.
from settingsplatformer import *
from sprites import *


class Game:
    def __init__(self):
        # window/initialize
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for ground in GROUND_LIST:
            p = Platform(*ground)
            self.all_sprites.add(p)
            self.platforms.add(p)
        p2 = Platform(WIDTH / 2 -50, HEIGHT * 3 /4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.run()
        # start game window
        
    def run(self):
        #game loop
        self.playing = True
        while self.playing:    
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    #update
    def update(self):
        self.all_sprites.update()
        #check if player hits ground if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top +1
                self.player.vel.y = 0

            # if player reaches right 1/4 of screen.
            if self.player.rect.right <= WIDTH / 4:
                self.player.pos.x -= abs(self.player.vel.x)
                for ground in self.platforms:
                    ground.rect.x -= abs(self.player.vel.x)
                for p2 in self.platforms:
                    ground.rect.x -= abs(self.player.vel.x)

    def events(self):
        #events
        for event in pg.event.get():
        # check for X in corner
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

    def draw(self):
        #draw
        #draw/render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # after drawing flip display
        pg.display.flip()

    def show_start_screen(self):
        #start screen
        pass

    def show_go_screen(self):
        #game over
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()


