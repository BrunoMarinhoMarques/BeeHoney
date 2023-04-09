from obj import Obj, Bee, Text

#importa uma biblioteca randomica
import random


class Game:
    def __init__(self):
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)
        #random.randrange(no range de 0, a um range de 300) sera aleatorio
        self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)
        self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), -50)
        self.bee = Bee("assets/bee1.png", 150, 200)
        self.score = Text(120, "0")
        self.lifes = Text(60, "3")




        self.change_scene = False



    def draw(self, window):

        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.bee.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)


    def update(self):
        self.move_bg()
        #estou passando os parametros que defini com variaveis la na funcao anim()
        #quanto menor o tick estiver mais rapida sera a animacao por seg
        self.spider.anim("spider", 8, 5)
        self.flower.anim("florwer", 8, 3)
        self.bee.anim("bee", 2, 5)
        self.move_spider()
        self.move_flower()

        #passando os dois parametros de colisao, primeiro a varivael group e depois a variavel name
        self.bee.colision(self.spider.group, "Spider")
        self.bee.colision(self.flower.group, "Flower")
        self.game_over()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_spider(self):
        self.spider.sprite.rect[1] += 10


        #APAGA A ARANHA DO JOGO, PARA QUE NAO CONTINUE GERANDO CODIGO
        if self.spider.sprite.rect[1] >= 500:
            self.spider.sprite.kill()
            # random.randrange(no range de 0, a um range de 300) sera aleatorio
            self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] >= 670:
            self.flower.sprite.kill()
            self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), -50)

    def game_over(self):
        if self.bee.life <= 0:
            self.change_scene = True



    def move_bg(self):
        self.bg.sprite.rect[1] += 3
        self.bg2.sprite.rect[1] += 3

        if self.bg.sprite.rect[1] >= 640:
           self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
           self.bg2.sprite.rect[1] = -640
