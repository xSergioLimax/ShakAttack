import pygame
import random

pygame.init()
altura = 300
largura = 800
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("SharkAttack")
bg = pygame.image.load("assets/fundo.png.jpeg")
bg_destroy = pygame.image.load("assets/bg-destroy.jpeg.jpeg")


gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("assets/tubarão.ico")
pygameDisplay.set_icon(gameIcon)

pink = (255, 125, 198)
black = (0, 0, 0)
white = (255, 255, 255)


explosaoSound = pygame.mixer.Sound("assets/explosao.wav.mpeg")
explosaoSound.set_volume(0.5)

def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, white)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    textoContinue = fonteContinue.render("press enter to restart", True, white)
    gameDisplay.blit(textoContinue, (50, 200))

    pygameDisplay.update()


def jogo():
    jogando = True
    movimentoX = 0
    movimentoY = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXPeixe = 450
    posicaoYPeixe = 100
    movimentoXPeixe = 0
    movimentoYPeixe = 0
    pontos = 0
    arpão = pygame.image.load("assets/arpão.png.jpeg")
    arpão = pygame.transform.flip(arpão, True, False)

    peixe = pygame.image.load("assets/peixe.png.jpeg")
    pygame.mixer.music.load("assets/trilha.mp3.mpeg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    larguraPeixe = 100
    alturaPeixe = 100
    larguraArpão = 150
    alturaArpão = 52
    limiar = 28
    velocidadePeixe = 8

    while True:
    
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXPeixe = -velocidadePeixe
                elif event.key == pygame.K_RIGHT:
                    movimentoXPeixe = velocidadePeixe
                elif event.key == pygame.K_UP:
                    movimentoYPeixe = -velocidadePeixe
                elif event.key == pygame.K_DOWN:
                    movimentoYPeixe = velocidadePeixe
                elif event.key == pygame.K_RETURN:
                    jogo()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXPeixe = 0
                    movimentoYPeixe = 0

        if jogando == True:
          
            posicaoXPeixe = posicaoXPeixe + movimentoXPeixe
            if posicaoXPeixe < 0:
                posicaoXPeixe = 0
            elif posicaoXPeixe > largura - larguraPeixe:
                posicaoXPeixe = largura - larguraPeixe

            posicaoYPeixe = posicaoYPeixe + movimentoYPeixe
            if posicaoYPeixe < 0:
                posicaoYPeixe = 0
            elif posicaoYPeixe > altura - alturaPeixe:
                posicaoYPeixe = altura - alturaPeixe

            gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(peixe, ( posicaoXPeixe, posicaoYPeixe ) )
            gameDisplay.blit(arpão, (movimentoX, movimentoY))
           

            if direcao == True:
                if movimentoX <= 800 - 150:
                    movimentoX = movimentoX + velocidade
                else:
                    
                    direcao = False
                    pontos = pontos + 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    arpão = pygame.transform.flip(arpão, True, False)
            else:
                if movimentoX >= 0:
                    movimentoX = movimentoX - velocidade
                else:
                    
                    direcao = True
                    pontos += 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    arpão = pygame.transform.flip(arpão, True, False)
           
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 280))

            pixelYArpão = list(range(movimentoY, movimentoY+alturaArpão + 1))
            pixelXArpão = list(range(movimentoX, movimentoX+larguraArpão + 1))

            pixelYPeixe = list(range(posicaoYPeixe, posicaoYPeixe + alturaPeixe +1 ))
            pixelXPeixe= list(range(posicaoXPeixe, posicaoXPeixe + larguraPeixe +1 ))

            colisaoY = list( set(pixelYArpão) & set(pixelYPeixe)  )
            colisaoX = list( set(pixelXArpão) & set(pixelXPeixe)  )
            if len(colisaoY) > limiar:
                if len(colisaoX) > limiar:
                    jogando =  False
                    dead(pontos)

            


        pygameDisplay.update()
        clock.tick(60)


jogo()
