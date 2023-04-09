import pygame


class Obj:

    def __init__(self, image, x, y):

        # cria um grupo e armazena dados de varios objetos
        self.group = pygame.sprite.Group()

        # falando que group pertence ao grupo imagem para poder trabalhar com imagem, dimensoes e etec, pertecendo a ele mesmo
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.tick = 0
        self.frame = 1

    def drawing(self, window):

        # funcao .draw pertece ao group, entao ela ja desesnha, e (window) é onde eu vou desenhar
        self.group.draw(window)
        # window.blit(self.image, (self.rect[0], self.rect[1]))

    # ANIMACAO DA ARANHA, passo as variaveis e quando chamar a funcao eu digo os parametros que serao acrescentados
    def anim(self, image, tick, frames):
        self.tick += 1

        # CONTROLE VELOCIDADE DA ANIMACAO
        # aqui esta falando que a cada 8.tick(frames) a animacao troca
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1

        if self.frame >= frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")


# heranca de classe, a classe Bee esta herdando tudo o que tem na class Obj
class Bee(Obj):

    # depois vir com o mouse em cima do __init__ e colocar add super class
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        #.Sound é para pequenas musicas que comeca e logo acaba, no caso de efeitos e etc...
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")

        self.sound_life = pygame.mixer.Sound("assets/sounds/bateu.ogg")

        # variaveis para verificacao de pontos e vida
        self.life = 3
        self.pts = 0

    # MOVIMENTO DA ABELHA
    def move_bee(self, event):
        # SE O TIPO DE EVENTO FOR IGUAL A MOVIMENTACAO DO MOUSE
        if event.type == pygame.MOUSEMOTION:
            # ENTAO POSICAO X SERA IGUAL A POSICAO X DO MOUSE
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    # VERIFICA COLISOES
    def colision(self, group, name):

        name = name
        # PRIMEIRO COLOCA O QUE VAI IDENTIFICAR AS COLISOES,NO CASO O SELF.SPRITE POIS ELE SE REFERE AO PROPRIO OBJETO
        # SEGUNDO QUAL GRUPO EU QUERO IDENTIFICAR A COLISAO QUE NO CASO VAI SER UM PARAMETRO QUE QUANDO CHAMAR VOU PASSAR
        # TERCEIRO SE QUER DESTRUIR OU MANTER O OBJETO FALSE NAO QUER A DESTRUICAO, TRUE QUER A DESTRUICAO DO OBJETO
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        # SE O NOME FOR IGUAL A Flower E A COLISAO FOR VERDADEIRA ENTAO
        if name == "Flower" and colision:
            # faca isso

            self.pts += 1
            #para chamar a musica de ponto
            self.sound_pts.play()
            if self.pts == 3:
                print("VOCE VENCEU")

            print(self.pts)

        # SENAO SE O NOME FOR IGUAL A Spider E A COLISAO FOR VERDADEIRA ENTAO
        elif name == "Spider" and colision:
            # faca isso
            self.life -= 1
            #para chamar a musica de perder pontos
            self.sound_life.play()
            if self.life == 0:
                print("Voce perdeu")

            print(self.life)


class Text:

    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))
