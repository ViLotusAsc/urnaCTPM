import pygame 
import json
from datetime import datetime
from pygame import mixer

pygame.init()
scrn_size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((1355, 700), pygame.RESIZABLE, pygame.FULLSCREEN)

mixer.init()
mixer.music.load("votocomputado.mp3")
mixer.music.set_volume(1)

# Título e Logo 
pygame.display.set_caption("URNA ELETRÔNICA - CTPM")
logo = pygame.image.load("ctpmlogo.png")
pygame.display.set_icon(logo)

layout = pygame.image.load("image.jpg")
layout = pygame.transform.scale(layout, (scrn_size[0][0]-100, scrn_size[0][1]-100))

running = True
counter = 1

a1 = (420, 300)
a2 = (558, 300)
a3 = (290, 300)
a4 = (405, 300)


fonte = pygame.font.SysFont('verdana', 90)
fonte2 = pygame.font.SysFont('verdana', 50)

def updateVotes():
    with open("votos_database.json", "r") as file:
        return json.load(file)


def texto(text1, text2, text3, text4, a1, a2, nomechapa, voto_cm):
    textoz = fonte.render(text1, True, (0, 0, 0))
    textoy = fonte.render(text2, True, (0, 0, 0))
    nmchapa = fonte2.render(nomechapa, True, (0, 0, 0))
    votocomputado = fonte2.render("Voto Computado!", True, (0, 255, 0))
    screen.blit(textoz, a1)
    screen.blit(textoy, a2)
    screen.blit(nmchapa, (350, 500))
    if voto_cm:
        screen.blit(votocomputado, (650, 500))
    pygame.display.update()




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
    texto(num1, num2, num3, num4, a1, a2, nomechapa, show_voto)
    pygame.display.update()
    

"""
187, 373
375, 372
592, 366
"""