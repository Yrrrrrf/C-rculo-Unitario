import sys
import pygame
import math

pygame.init()

width = 1200
height = 1000
radio = width//4

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Círculo Unitario")

ground = (40, 40, 40)
white = (255, 255, 255)
red = (255, 60, 60)
purple = (255, 0, 255)
grey = (220, 220, 220)
green = (60, 255, 100)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
blue = (0, 128, 255)

font = pygame.font.Font("freesansbold.ttf", 48)
titulo = font.render("Círculo unitario", True, white)

fontt = pygame.font.Font("freesansbold.ttf", 18)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #OBTENER POSICIÓN DE MOUSE
    pos_x, pos_y = pygame.mouse.get_pos()
    xc = pos_x - width//2
    yc = height//2 - pos_y
    centro = (width//2, height//2)
    txc = "X: {}".format(xc/radio)
    tyc = "Y: {}".format(yc/radio)

    surface.fill(ground)
    surface.blit(titulo, (20, 20))

    #CIRCULO (SUPERFICIE, COLOR, COORDENADAS, RADIO, GROSOR DEL PERIMETRO)
    pygame.draw.circle(surface, white, centro, radio, 1)
    #LINEA (SUPERFICIE, COLOR, INICIO, FINAL, GROSOR)
    pygame.draw.line(surface, grey, (width//2 + radio, height//2), (width//2 - radio, height//2), 1)
    pygame.draw.line(surface, grey, (width//2, height//2 + radio), (width//2, height//2 - radio), 1)

    #ÁNGULO DEL CIRCULO UNITARIO
    if xc != 0:
        a = math.atan((yc)/(xc))
        angulo = math.degrees(a)
        x = math.cos(a)
        y = math.sin(a)
        tan = (y/x)
        sec = 1 / (x)
    else:
        x = 0.0

    if yc != 0:
        cotan = (x/y)
        csc = 1 / (y)

    xl = x * radio
    yl = y * radio
    tanl = tan * radio
    cotanl = cotan * radio
    secl = sec * radio
    cscl = csc * radio

    #SECANTE
    tsec = "Secante: Indeterminado"
    if yc != 0:
        if xc > 0:
            pygame.draw.line(surface, grey, (width//2, height//2 - cscl), (width//2 + secl, height//2), 1)
            pygame.draw.line(surface, blue, centro, (width//2 + secl, height//2), 3)
        elif xc < 0:
            pygame.draw.line(surface, grey, (width//2, height//2 + cscl), (width//2 - secl, height//2), 1)
            pygame.draw.line(surface, blue, centro, (width//2 - secl, height//2), 3)

    if xc > 0:
        tsec = "Secante: {}".format(sec)
    elif xc < 0:
        tsec = "Secante: {}".format(-sec)

    #COSECANTE
    tcsc = "Cosecante: Indeterminado"
    if yc != 0:
        if xc > 0:
            pygame.draw.line(surface, grey, (width//2, height//2 - cscl), (width//2 + secl, height//2), 1)
            pygame.draw.line(surface, orange, centro, (width//2, height//2 - cscl), 3)
            tcsc = "Cosecante: {}".format(csc)
        elif xc < 0:
            pygame.draw.line(surface, grey, (width//2, height//2 + cscl), (width//2 - secl, height//2), 1)
            pygame.draw.line(surface, orange, centro, (width//2, height//2 + cscl), 3)
            tcsc = "Cosecante: {}".format(-csc)
        else:
            if yc > 0: tcsc = "Cosecante: 1.0"
            if yc < 0: tcsc = "Cosecante: -1.0"

   #LINEA TANGENTE
    ttan = "Tangente: {}".format(tan)
    if xc > 0:
        pygame.draw.line(surface, grey, centro, (width//2 + radio, height//2 - tanl), 1)
        pygame.draw.line(surface, cyan, (width//2 + radio, height//2), (width//2 + radio, height//2 - tanl), 3)
    elif xc < 0:
        pygame.draw.line(surface, grey, centro, (width//2 - radio, height//2 + tanl), 1)
        pygame.draw.line(surface, cyan, (width//2 - radio, height//2), (width//2 - radio, height//2 + tanl), 3)
    else:
        ttan = "Tangente: Indeterminado"

    #LINEA COTANGENTE
    tctan = "Cotangente: {}".format(cotan) 
    if yc > 0:
        pygame.draw.line(surface, grey, centro, (width//2 + cotanl, height//2 - radio), 1)
        pygame.draw.line(surface, yellow, (width//2, height//2 - radio), (width//2 + cotanl, height//2 - radio), 3)
    elif yc < 0:
        pygame.draw.line(surface, grey, centro, (width//2 - cotanl, height//2 + radio), 1)
        pygame.draw.line(surface, yellow, (width//2, height//2 + radio), (width//2 - cotanl, height//2 + radio), 3)
    else:
        tctan = "Cotangente: Indeterminado"

    if angulo == 45:
            ttan = "Tangente: 1.0"
            tctan = "Cotangente: 1.0"
    elif angulo == -45:
            ttan = "Tangente: -1.0"
            tctan = "Cotangente: -1.0"

    #SENO Y COSENO
    #CUADANTE I Y IV
    if xc > 0:
        pygame.draw.line(surface, red, (width//2, height//2 - yl), (width//2 + xl, height//2 - yl), 3)
        pygame.draw.line(surface, green, (width//2 + xl, height//2), (width//2 + xl, height//2 - yl), 3)
        pygame.draw.line(surface, purple, centro, (width//2 + xl, height//2 - yl), 3)
        tx = "X: {}".format(x)
        ty = "Y: {}".format(y)
    #CUADRANTE II Y III
    elif xc < 0:
        pygame.draw.line(surface, red, (width//2, height//2 + yl), (width//2 - xl, height//2 + yl), 3)
        pygame.draw.line(surface, green, (width//2 - xl, height//2), (width//2 - xl, height//2 + yl), 3)
        pygame.draw.line(surface, purple, centro, (width//2 - xl, height//2 + yl), 3)
        tx = "X: {}".format(-x)
        ty = "Y: {}".format(-y)

    #ÁNGULOS
    if xc > 0:
        ta = "Ángluo: {}".format(angulo)
        if yc < 0:
            ta = "Ángluo: {}".format(angulo + 360)
    elif xc < 0:
        ta = "Ángluo: {}".format(angulo + 180)
    else:
        tx = "X: 0.0"
        if yc > 0:
            pygame.draw.line(surface, purple, centro, (width//2, height//2 - radio), 3)
            ty = "Y: 1.0"
            ta = "Ángluo: 90°"
        elif yc < 0:
            pygame.draw.line(surface, purple, centro, (width//2, height//2 + radio), 3)
            ty = "Y: -1.0"
            ta = "Ángluo: 270°"

    xtext = fontt.render(tx, True, red)
    ytext = fontt.render(ty, True, green)
    atext = fontt.render(ta, True, grey)
    ttext = fontt.render(ttan, True, cyan)
    cttext = fontt.render(tctan, True, yellow)
    csctext = fontt.render(tcsc, True, orange)
    sectext = fontt.render(tsec, True, blue)
    pos_xtext = fontt.render(txc, True, white)
    pos_ytext = fontt.render(tyc, True, white)

    surface.blit(xtext, (40, height//12))
    surface.blit(ytext, (40, height//12 + height//32*1))
    surface.blit(atext, (40, height//12 + height//32*2))
    surface.blit(ttext, (40, height//12 + height//32*3))
    surface.blit(cttext, (40, height//12 + height//32*4))
    surface.blit(csctext, (40, height//12 + height//32*5))
    surface.blit(sectext, (40, height//12 + height//32*6))
    surface.blit(pos_xtext, (40, height//12 + height//32 * 7))
    surface.blit(pos_ytext, (40, height//12 + height//32 * 8))

    pygame.display.update()