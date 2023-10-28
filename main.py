import pygame 


pygame.init()
screen = pygame.display.set_mode((1355, 700), pygame.RESIZABLE)

# Título e Logo 
pygame.display.set_caption("URNA ELETRÔNICA - CTPM")
logo = pygame.image.load("ctpmlogo.png")
pygame.display.set_icon(logo)

layout = pygame.image.load("urnalayoutnv.jpg")
layout = pygame.transform.scale(layout, (1355, 700))

running = True
counter = 1

a1 = (90, 300)
a2 = (183, 300)
a3 = (290, 300)
a4 = (405, 300)


fonte = pygame.font.SysFont('verdana', 90)
fonte2 = pygame.font.SysFont('verdana', 50)

def texto(text1, text2, text3, text4, a1, a2, a3, a4, nomechapa):
    textoz = fonte.render(text1, True, (0, 0, 0))
    textoy = fonte.render(text2, True, (0, 0, 0))
    textox = fonte.render(text3, True, (0, 0, 0))
    textow = fonte.render(text4, True, (0, 0, 0))
    nmchapa = fonte2.render(nomechapa, True, (0, 0, 0))
    screen.blit(textoz, a1)
    screen.blit(textoy, a2)
    screen.blit(textox, a3)
    screen.blit(textow, a4)
    screen.blit(nmchapa, (30, 500))
    pygame.display.update()




nomechapa = ''

chapa = {'nome': [], 'num':[]}
nomes = ['Chapa 1', 'Chapa 2', 'Chapa 3', 'Chapa 4']
numeros = [1010, 2020, 3030, 4040]
for nme in nomes:
    chapa['nome'].append(nme)
for num in numeros:
    chapa['num'].append(num)


def fzrvoto(num1, num2, num3, num4): 
    num1 = str(num1) 
    num2 = str(num2) 
    num3 = str(num3)
    num4 = str(num4)
    num1 += num2 
    num1 += num3
    num1 += num4
    try:
        return int(num1) 
    except Exception:
        pass

num1 = ''
num2 = ''
num3 = ''
num4 = ''


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
                    if num(counter) == 3:
                        num3 = '0'
                    if num(counter) == 4:
                        num4 = '0'
                    counter += 1
                if event.key == pygame.K_1:
                    if num(counter) == 1:
                        num1 = '1'
                    if num(counter) == 2:
                        num2 = '1'
                    if num(counter) == 3:
                        num3 = '1'
                    if num(counter) == 4:
                        num4 = '1'
                    counter += 1
                if event.key == pygame.K_2:
                    if num(counter) == 1:
                        num1 = '2'
                    if num(counter) == 2:
                        num2 = '2'
                    if num(counter) == 3:
                        num3 = '2'
                    if num(counter) == 4:
                        num4 = '2'
                    counter += 1
                if event.key == pygame.K_3:
                    if num(counter) == 1:
                        num1 = '3'
                    if num(counter) == 2:
                        num2 = '3'
                    if num(counter) == 3:
                        num3 = '3'
                    if num(counter) == 4:
                        num4 = '3'
                    counter += 1
                if event.key == pygame.K_4:
                    if num(counter) == 1:
                        num1 = '4'
                    if num(counter) == 2:
                        num2 = '4'
                    if num(counter) == 3:
                        num3 = '4'
                    if num(counter) == 4:
                        num4 = '4'
                    counter += 1
                if event.key == pygame.K_5:
                    if num(counter) == 1:
                        num1 = '5'
                    if num(counter) == 2:
                        num2 = '5'
                    if num(counter) == 3:
                        num3 = '5'
                    if num(counter) == 4:
                        num4 = '5'
                    counter += 1
                if event.key == pygame.K_6:
                    if num(counter) == 1:
                        num1 = '6'
                    if num(counter) == 2:
                        num2 = '6'
                    if num(counter) == 3:
                        num3 = '6'
                    if num(counter) == 4:
                        num4 = '6'
                    counter += 1
                if event.key == pygame.K_7:
                    if num(counter) == 1:
                        num1 = '7'
                    if num(counter) == 2:
                        num2 = '7'
                    if num(counter) == 3:
                        num3 = '7'
                    if num(counter) == 4:
                        num4 = '7'
                    counter += 1
                if event.key == pygame.K_8:
                    if num(counter) == 1:
                        num1 = '8'
                    if num(counter) == 2:
                        num2 = '8'
                    if num(counter) == 3:
                        num3 = '8'
                    if num(counter) == 4:
                        num4 = '8'
                    counter += 1
                if event.key == pygame.K_9:
                    if num(counter) == 1:
                        num1 = '9'
                    if num(counter) == 2:
                        num2 = '9'
                    if num(counter) == 3:
                        num3 = '9'
                    if num(counter) == 4:
                        num4 = '9'
                    counter += 1
                if event.key == pygame.K_BACKSPACE:
                    counter = 0
                    num1 = ''
                    num2 = ''
                    num3 = ''
                    num4 = ''
                    nomechapa = ''
                if event.key == pygame.K_RETURN:
                    voto = fzrvoto(num1, num2, num3, num4)
                    if voto in chapa['num']:
                        indice = chapa['num'].index(voto)
                        nome = chapa['nome'][indice]
                        nomechapa = nome
                    else:
                        nomechapa = 'Voto inválido!'
                
                
    mousex, mousey = pygame.mouse.get_pos()

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


    screen.blit(layout, (5, 5))
    texto(num1, num2, num3, num4, a1, a2, a3, a4, nomechapa)
    pygame.display.update()
    

"""
187, 373
375, 372
592, 366
"""