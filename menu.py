import pygame
from obj import Obj


class Menu:
    def __init__(self, image):

        self.background = Obj(image, 0, 0)

        self.change_scene = False

    def draw(self, window):
        #sera desenhado e a variavel(window) sera passado o parametro quando for chamado,que no caso sera na tela
        self.background.group.draw(window)


    def events(self, event):
        #evento que verifica se o enter foi apertado e se for ele troca de tela
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True
                print(self.change_scene)


class GameOver(Menu):

    def __init__(self, image):
        super().__init__(image)


