import pygame 
import json
from datetime import datetime
from pygame import mixer

pygame.init()
scrn_size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((1355, 700), pygame.RESIZABLE, pygame.FULLSCREEN)

mixer.init()
mixer.music.load("imgs/votocomputado.mp3")
mixer.music.set_volume(1)

# Título e Logo 
pygame.display.set_caption("URNA ELETRÔNICA - CTPM")
logo = pygame.image.load("imgs/ctpmlogon.png")
pygame.display.set_icon(logo)

layout = pygame.image.load("imgs/lytbrnc.jpg")
layout = pygame.transform.scale(layout, (scrn_size[0][0]-100, scrn_size[0][1]-100))

running = True
counter = 1

a1 = (420, 300)
a2 = (558, 300)
a3 = (290, 300)
a4 = (405, 300)

barRect = pygame.Rect((1100, 200), (400, 400))


fonte = pygame.font.SysFont('verdana', 90)
fonte2 = pygame.font.SysFont('verdana', 50)
fonte3 = pygame.font.SysFont('verdana', 30)
fonte4 = pygame.font.SysFont('verdana', 20)

def updateVotes():
    with open("votos_database.json", "r") as file:
        return json.load(file)


def texto(text1, text2, text3, text4, a1, a2, nomechapa, voto_cm):
    textoz = fonte.render(text1, True, (0, 0, 0))
    textoy = fonte.render(text2, True, (0, 0, 0))
    nmchapa = fonte2.render(nomechapa, True, (0, 0, 0))
    votocomputado = fonte2.render("Voto Computado!", True, (0, 0, 0))
    screen.blit(textoz, a1)
    screen.blit(textoy, a2)
    screen.blit(nmchapa, (350, 500))
    if voto_cm:
        screen.blit(votocomputado, (350, 500))
    pygame.display.update()


def blitInfo(hour, minute, second, milisecond):
    txNum = fonte2.render("Número:", True, (0, 0, 0))
    txChapa = fonte2.render("Chapa:", True, (0, 0, 0))
    txAprTecla = fonte3.render("Aperte a tecla:", True, (0, 0, 0))
    txEnter = fonte3.render("Enter para confirmar", True, (0, 0, 0))
    txBkspc = fonte3.render("Backspace para restaurar", True, (0, 0, 0))
    txColegio = fonte2.render("Colégio Tiradentes", True, (0, 0, 0))
    svoto = fonte3.render("Seu voto para:", True, (0, 0, 0))
    txGremio = fonte2.render("Grêmio Estudantil", True, (0, 0, 0))
    hour = fonte4.render(f"{hour}:{minute}:{second}:{milisecond}", True, (0, 0, 0))
    txPresid = fonte4.render("Presidente:", True, (0, 0, 0))
    txVice = fonte4.render("Vice:", True, (0, 0, 0))
    tx1sec = fonte4.render("1 Secretário:", True, (0, 0, 0))
    tx2sec = fonte4.render("2 Secretário:", True, (0, 0, 0))
    tx1tes = fonte4.render("1 Tesoureiro:", True, (0, 0, 0))
    tx2tes = fonte4.render("2 Tesoureiro:", True, (0, 0, 0))
    txdsoc = fonte4.render("Diretor Social:", True, (0, 0, 0))
    txdesp = fonte4.render("Diretor de Esportes:", True, (0, 0, 0))
    txdsau = fonte4.render("Diretor de Saúde:", True, (0, 0, 0))
    txpori = fonte4.render("Professor Orientador:", True, (0, 0, 0))


    screen.blit(txColegio, (1000, 100))
    screen.blit(txNum, (90, 340))
    screen.blit(txChapa, (90, 500))
    screen.blit(txAprTecla, (90, 650))
    screen.blit(txEnter, (90, 700))
    screen.blit(txBkspc, (90, 750))
    screen.blit(pygame.transform.scale(logo, (95, 95)),(1200, 5))
    screen.blit(svoto, (100, 10))
    screen.blit(hour, (700, 10))
    screen.blit(txGremio, (300, 170))
    screen.blit(txPresid, (1110, 240))
    screen.blit(txVice, (1110, 270))
    screen.blit(tx1sec, (1110, 300))
    screen.blit(tx2sec, (1110, 330))
    screen.blit(tx1tes, (1110, 360))
    screen.blit(tx2tes, (1110, 390))
    screen.blit(txdsoc, (1110, 420))
    screen.blit(txdesp, (1110, 450))
    screen.blit(txdsau, (1110, 480))
    screen.blit(txpori, (1110, 510))


nomechapa = ''

chapa = {'nome': [], 'num':[]}
nomes = ['Chapa 1', 'Chapa 2', 'Chapa 3', 'Chapa 4']
numeros = [10, 20, 30, 40]
for nme in nomes:
    chapa['nome'].append(nme)
for num in numeros:
    chapa['num'].append(num)


def fzrvoto(num1, num2): 
    num1 = str(num1) 
    num2 = str(num2) 
    num1 += num2
    try:
        return int(num1) 
    except Exception:
        pass

num1 = ''
num2 = ''


voto = 0

def num(contador):
    if contador == 1:
         return 1
    if contador == 2:
         return 2
    if contador == 3:
         return 3
    if contador == 4:
        return 4
    
show_voto = False
scnds = 0

while running: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    print(f"X: {mousex}, Y: {mousey}")
                if event.key == pygame.K_0:
                    if num(counter) == 1:
                        num1 = '0'
                    if num(counter) == 2:
                        num2 = '0'
                    counter += 1
                if event.key == pygame.K_1:
                    if num(counter) == 1:
                        num1 = '1'
                    if num(counter) == 2:
                        num2 = '1'
                    counter += 1
                if event.key == pygame.K_2:
                    if num(counter) == 1:
                        num1 = '2'
                    if num(counter) == 2:
                        num2 = '2'
                    counter += 1
                if event.key == pygame.K_3:
                    if num(counter) == 1:
                        num1 = '3'
                    if num(counter) == 2:
                        num2 = '3'
                    counter += 1
                if event.key == pygame.K_4:
                    if num(counter) == 1:
                        num1 = '4'
                    if num(counter) == 2:
                        num2 = '4'
                    counter += 1
                if event.key == pygame.K_5:
                    if num(counter) == 1:
                        num1 = '5'
                    if num(counter) == 2:
                        num2 = '5'
                    counter += 1
                if event.key == pygame.K_6:
                    if num(counter) == 1:
                        num1 = '6'
                    if num(counter) == 2:
                        num2 = '6'
                    counter += 1
                if event.key == pygame.K_7:
                    if num(counter) == 1:
                        num1 = '7'
                    if num(counter) == 2:
                        num2 = '7'
                    counter += 1
                if event.key == pygame.K_8:
                    if num(counter) == 1:
                        num1 = '8'
                    if num(counter) == 2:
                        num2 = '8'
                    counter += 1
                if event.key == pygame.K_9:
                    if num(counter) == 1:
                        num1 = '9'
                    if num(counter) == 2:
                        num2 = '9'
                    counter+=1
                if event.key == pygame.K_BACKSPACE:
                    counter = 0
                    num1 = ''
                    num2 = ''
                    nomechapa = ''
                if event.key == pygame.K_RETURN:
                    time = datetime.now()
                    voto = fzrvoto(num1, num2)
                    if voto in chapa['num']:
                        indice = chapa['num'].index(voto)
                        nome = chapa['nome'][indice]
                        nomechapa = nome
                        thevote = updateVotes()
                        thevote["votos"].update({f"Voto{time.microsecond}": {"Voto":nome, "horario":f"{str(time.hour)}:{time.minute}:{time.second}:{time.microsecond}"}})
                        with open("votos_database.json", "w") as file:
                            file = json.dump(thevote, file, indent=4)
                        scnds = time.second
                        mixer.music.play()
                        if show_voto == False:
                            show_voto = True

                        counter = 0
                        num1, num2 = '', ''
                        nomechapa = ''
                       
                
    if show_voto:
        scnds_N = datetime.now().second
        if (scnds_N - 1) > scnds:
            show_voto = False

    mousex, mousey = pygame.mouse.get_pos()

    voto = fzrvoto(num1, num2)
    if voto in chapa['num']:
        indice = chapa['num'].index(voto)
        nome = chapa['nome'][indice]
        nomechapa = nome
    else:
        if voto != None:
            if len(str(voto)) > 1:
                nomechapa = "Voto Inválido!"

    if num2 == '':
        num3 = ''
    if num3 == '':
        num4 = ''

    if counter > 4:
        counter = 4
    if counter < 1:
        counter = 1

    if voto in chapa == False:
        nomechapa = ''


    screen.blit(layout, (55, 5))
    hora = datetime.now()
    blitInfo(hour=hora.hour, minute=hora.minute, second=hora.second, milisecond=hora.microsecond)
    pygame.draw.rect(screen, (0, 0, 0), barRect, 2)
    texto(num1, num2, num3, num4, a1, a2, nomechapa, show_voto)
    pygame.display.update()
    

"""
187, 373
375, 372
592, 366
"""