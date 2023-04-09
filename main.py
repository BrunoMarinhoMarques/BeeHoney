import pygame
from game import Game

from menu import Menu, GameOver


class Main:


    def __init__(self, sizex, sizey, title):

        pygame.init()
        #para conseguir usar musica
        pygame.mixer.init()
        #caminho onde a musica se encontra
        pygame.mixer.music.load("assets/sounds/bg.ogg")

        #para tocar a musica sem parar é preciso colocar o parametro -1
        pygame.mixer.music.play(-1)


        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

        #variavel para o controle de FPS
        self.fps = pygame.time.Clock()

        self.loop = True



    def draw(self):


        #se variavel change_scene dentro de Menu() nao for verdadeira entao será desenhado na tela
        #a variavel change_scene ta como False
        if not self.menu.change_scene:
        #pega o obj Menu() junto com a funcao draw e esta passando o parametro de onde desenhar
            self.menu.draw(self.window)

        #senao se variavel change_scene dentro de Game() for False entao
        elif not self.game.change_scene:

            #DESENHE A TELA GAME
            self.game.draw(self.window)
            self.game.update()
        #senao se variavel change_scene dentro de Game() for False entao
        elif not self.gameover.change_scene:
            #DESENHE A TELA GAMEOVER
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0



    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

            if not self.menu.change_scene:
            #verifica se apertou enter para mudar de cena, pois o paramentro (events) esta pegando todos os eventos
                self.menu.events(events)

            elif not self.game.change_scene:
            #dentro de move bee tem a variavel que esta sendo passado o parametro agora quando el esta sendo chamada
            #entao dentro de Game(), na variavel bee busque move_bee e verifique todos os eventos, caso algum deles
            #seja movimento do mouse, a imagem de bee sera igual o movimento do mouse
                self.game.bee.move_bee(events)

            else:
                self.gameover.events(events)

    def update(self):

        while self.loop:
            self.draw()
            #o .tick() pede para informar quntos frames por segundo eu quero, nesse caso foi colado 30
            self.fps.tick(30)

            self.events()
            pygame.display.update()


game = Main(360, 640, "BeeHoney")
game.update()
