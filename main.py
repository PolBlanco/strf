#Bibliotecas utilizadas
import itertools, os, sys, pygame
from pygame.locals import *
from random import randint
from random import randrange
from conf import knowserversip, servers, difficulties, difficulty, combat_time, combat_times
from online import *
from save import *
from time import sleep
from anticheat import *
#import pyping


#Aqui dibujamos la pantalla y cargamos las imagenes de la vida de los personajes y
#un estilo de letra
SIZE = WIDTH, HEIGHT = 800, 367
pygame.init()
icono=pygame.image.load(f'{os.path.dirname(__file__)}/street.png')
pygame.display.set_icon(icono)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
font3 = pygame.font.Font(f'{os.path.dirname(__file__)}/fonts/8-BIT_WONDER.TTF',15)
letter_color = (255, 255, 255)
font = pygame.font.Font(f'{os.path.dirname(__file__)}/fonts/8-BIT_WONDER.TTF',20)
font2 = pygame.font.Font(f'{os.path.dirname(__file__)}/fonts/8-BIT_WONDER.TTF',80)
barravida1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/barravida1.png')
barravida2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/barravida2.png')
cuadrovida1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/cuadrovida1.png')
cuadrovida2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/cuadrovida2.png')
mainClock = pygame.time.Clock()
from CHARACTERS import CHARACTERS
from SONS import SONS, CONTROL, EFECTS

#Aqui crea un cuadrado para cada boton con su posicion y medidas 
button_1 = pygame.Rect(80, 80, 120, 20)
button_2 = pygame.Rect(80, 100, 120, 20)
button_3 = pygame.Rect(80, 120, 120, 20)
button_4 = pygame.Rect(80, 140, 120, 20)
button_5 = pygame.Rect(80, 160, 120, 20)
button_6 = pygame.Rect(80, 180, 120, 20)
button_7 = pygame.Rect(80, 20, 120, 20)
button_8 = pygame.Rect(80, 200, 120, 20)
button_10 = pygame.Rect(80, 220, 120, 20)
button_9 = pygame.Rect(WIDTH//2+80, 20, 120, 20)
button_11 = pygame.Rect(100, 280, 120, 20)
button_12 = pygame.Rect(WIDTH//2+100, 280, 120, 20)
button_13 = pygame.Rect(WIDTH//2+100, 300, 120, 20) #CPU choose
button_left1 = pygame.Rect(60, 60, 40, 40)
button_right1 = pygame.Rect(260, 60, 40, 40)
button_left2 = pygame.Rect(WIDTH // 2 + 60, 60, 40, 40)
button_right2 = pygame.Rect(WIDTH // 2 + 260, 60, 40, 40)
playing = False #variable para ver si ya ha iniciado partida en world tour

def draw_text(text, font, color, surface, x, y):
    '''Esta funcion dibuja el estilo del texto'''
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    '''En esta funcion se escuentra el menu con sus modos, botones, y hemos creado una transición para
    cada vez que entres y salgas de un modo se vea diferente y cargamos un sonido de fondo'''
    pygame.display.set_caption("STREET FIGHTER: MAIN MENU", "STRF")
    CONTROL["music"].play(SONS["menu"],5,0,0)
    click = False
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/main_menu.png').convert()
    transition = WIDTH//2
    while True:
        screen.blit(background,(0,0))
        pygame.draw.rect(screen, (0, 0, 0), (80-transition, 80, 80, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80, 100-transition, 200, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80-transition, 120, 130, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80, 140-transition, 110, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80-transition, 160, 130, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80, 180-transition, 130, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80-transition, 200, 100, 20))
        pygame.draw.rect(screen, (0, 0, 0), (80, 220-transition, 70, 20))
        mx, my = pygame.mouse.get_pos()
        draw_text('1 vs 1'.upper(), font, letter_color, screen, 80, 80-transition)
        draw_text('World tour'.upper(), font, letter_color, screen, 80-transition, 100)
        draw_text('1 vs CPU'.upper(), font, letter_color, screen, 80, 120-transition)
        draw_text('online'.upper(), font, letter_color, screen, 80-transition, 140)
        draw_text('options'.upper(), font, letter_color, screen, 80, 160-transition)
        draw_text('credits'.upper(), font, letter_color, screen, 80-transition, 180)
        draw_text('stats'.upper(), font, letter_color, screen, 80, 200-transition)
        draw_text('exit'.upper(), font, letter_color, screen, 80-transition, 220)
        '''Aqui esta para cuando cliquemos en un boton entres al modo que toca y cargamos musica de fondo'''
        if button_1.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                _1vs1_menu()
        if button_2.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                world_tour_menu()
        if button_3.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                _1vscpu_menu()
        if button_4.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                online_menu()
        if button_5.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                options()
        if button_6.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                credits()
        if button_8.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                stats()
        if button_10.collidepoint((mx, my)):
            if click:
                SONS["menu"].fadeout(1000)
                CONTROL["efects"].play(EFECTS["escollir"])
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
        if transition != 0:
            transition -= 10

def options():
    '''Este es el menu de optiones donde se puede canviar la dificultat y tiempo de combate, tambien 
    dibujamos botones con su posicion y medidas'''
    pygame.display.set_caption("STREET FIGHTER: OPTIONS", "STRF")
    click = False
    running = True
    global combat_time
    global difficulty
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/options.png').convert()
    button_I1 = pygame.Rect(380, 100, 20, 20)
    button_X1 = pygame.Rect(500, 100, 20, 20)
    button_I2 = pygame.Rect(380, 120, 20, 20)
    button_X2 = pygame.Rect(500, 120, 20, 20)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (WIDTH-220, 20))
        mx, my = pygame.mouse.get_pos()
        draw_text('options'.upper(), font, letter_color, screen, WIDTH//2-35, 20)
        draw_text('difficulty'.upper(), font, letter_color, screen, 80, 80)
        draw_text(str(difficulties[difficulty]), font, letter_color, screen, 400, 80)
        draw_text('sound efects'.upper(), font, letter_color, screen, 80, 100)
        draw_text(str(int(CONTROL["efects"].get_volume()*100)), font, letter_color, screen, 400, 100)
        draw_text('I', font, letter_color, screen, 380, 100)
        draw_text('X', font, letter_color, screen, 500, 100)
        draw_text('music'.upper(), font, letter_color, screen, 80, 120)
        draw_text(str(int(CONTROL["music"].get_volume()*100)), font, letter_color, screen, 400, 120)
        draw_text('I', font, letter_color, screen, 380, 120)
        draw_text('X', font, letter_color, screen, 500, 120)
        draw_text('combat time'.upper(), font, letter_color, screen, 80, 140)
        draw_text(str(combat_times[combat_time][0]), font, letter_color, screen, 400, 140)
        draw_text('Main menu'.upper(), font, letter_color, screen, 80, 160)
        '''Aqui estan los botones para cuando cliques en uno entres al modo que toca y cargamos musica de fondo'''
        if button_1.collidepoint((mx, my)):
            if click:
                difficulty = (difficulty+1)%3
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_X1.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].set_volume((CONTROL["efects"].get_volume()+0.1))
        if button_X2.collidepoint((mx, my)):
            if click:
                CONTROL["music"].set_volume((CONTROL["music"].get_volume()+0.1))
        if button_I1.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].set_volume((CONTROL["efects"].get_volume()-0.1))
        if button_I2.collidepoint((mx, my)):
            if click:
                CONTROL["music"].set_volume((CONTROL["music"].get_volume()-0.1))
        if button_4.collidepoint((mx, my)):
            if click:
                combat_time = (combat_time + 1) % len(combat_times)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_5.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

def end(P1):
    '''Esta funcion es para cuando te pasas el World Tour se muestre como final del juego'''
    global facing
    pygame.display.set_caption("STREET FIGHTER: END", "STRF")
    click = False
    running = True
    image_fons = load_images(path=os.path.join(os.path.dirname(__file__), 'imatges', 'fons', '8'))
    clock = pygame.time.Clock()
    dt = clock.tick(FPS) / 200 * (len(image_fons))
    credit_height = HEIGHT
    background = AnimatedBackground(position=(0, 0), images=image_fons, delay=0.03)
    all_sprites = pygame.sprite.Group(background)
    all_sprites.update(dt)
    while running:
        all_sprites.update(dt)
        screen.fill((0,0,0))
        screen.blit(background.image, background.rect)
        screen.blit(CHARACTERS[P1][3][7][facing[0]][1 % len(CHARACTERS[P1][3][7])],(40, WIDTH//2))
        mx, my = pygame.mouse.get_pos()
        draw_text('credits'.upper(), font, letter_color, screen, 80, 160)
        draw_text('THE END'.upper(), font, letter_color, screen, WIDTH//2-35, 20)
        credit_height = (credit_height - 1) % (HEIGHT * 2)
        draw_text('You survived the hard world of the street fight...'.upper(), font3, letter_color, screen, 80, credit_height)
        draw_text('You are now the new hero of this world...'.upper(), font3, letter_color, screen, 80, credit_height+40)
        draw_text('Congratulations!!!'.upper(), font3, letter_color, screen, 80, credit_height+80)
        if button_5.collidepoint((mx, my)):
            if click:
                credits()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

serverSelection = 0
def online_menu():
    '''Esta funcion es para cargar el sql y poder jugar en LAN, dentro de esta funcion encontramos,
    el menu con sus imagenes musica y botones'''
    pygame.display.set_caption("STREET FIGHTER: ONLINE MENU", "STRF")
    selectionP1 = 0
    global serverSelection
    global servers
    global knowserversip
    if knowserversip == False:
        ips = net_scan()
    click = False
    endmatch = False
    transition = WIDTH
    running = True
    randomizeP1 = False
    global difficulty
    global sound_effects
    global music
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/VS.jpg').convert()
    arrow1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector.png').convert()
    arrow2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector2.png').convert()
    button_left1 = pygame.Rect(60, 60, 40, 40)
    button_right1 = pygame.Rect(260, 60, 40, 40)
    ip = 0
    while running:
        if knowserversip == False:
            if ip != len(ips) and transition == 0:
                servers += scan_servers(ips[ip])
                ip += 1
        elif len(servers) == 0:
            servers.append(input("Introdueix la ip del teu servidor: "))
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()
        screen.blit(arrow2, (60, 60))
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        screen.blit(CHARACTERS[selectionP1][2], (110 - transition, 100))
        screen.blit(arrow1, (260 - transition, 60))
        screen.blit(arrow2, (WIDTH // 2 + 60 - transition, 60))
        pygame.draw.rect(screen, (0, 0, 0), (110, 70, 150, 20))
        screen.blit(arrow1, (WIDTH // 2 + 260 - transition, 60))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 110, 70, 150, 20))
        draw_text('ONLINE SELECT'.upper(), font, letter_color, screen, WIDTH // 2 - 260//2 - transition, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80 - transition, 20)
        draw_text('1P'.upper(), font, letter_color, screen, 160 - transition, 40)
        draw_text(CHARACTERS[selectionP1][1].upper(), font, letter_color, screen, 120 - transition, 70)
        draw_text('Server'.upper(), font, letter_color, screen, WIDTH // 2 + 80 - transition, 40)
        draw_text('PLAY'.upper(), font, letter_color, screen, WIDTH // 1.5 - transition, 20)
        draw_text(CHARACTERS[selectionP1][0].upper(), font, letter_color, screen, 120 - transition, 250)
        ocupied = 2
        if len(servers) > 0:
            try:
                draw_text(str(servers[serverSelection]), font, letter_color, screen, WIDTH // 2 + 95 - transition, 70)
                cnx = mysql.connector.connect(user='spectator',
                                              database='strf',
                                              host=str(servers[serverSelection]),
                                              port=50000,
                                              connection_timeout=5)
            except mysql.connector.Error as err:
                print(err)
                servers.pop(serverSelection)
                servers.append(input("Introdueix la ip del teu servidor: "))
            else:
                cursor = cnx.cursor()
                cursor.execute(f"SELECT * FROM login1")
                passwd = cursor.fetchall()[0][0]
                if passwd == '0':
                    cursor.execute(f"SELECT * FROM login2")
                    passwd = cursor.fetchall()[0][0]
                    if passwd == '0':
                        cursor.execute(f"SELECT chrono FROM spectator")
                        passwd = cursor.fetchall()[0][0]
                        ocupied = 2
                        # cursor.
                        draw_text(f"OCUPIED", font, letter_color, screen, WIDTH // 2 + 95 - transition, 100)
                        draw_text(f"Time left {passwd}", font, letter_color, screen, WIDTH // 2 + 95 - transition, 130)
                    else:
                        ocupied = 1
                else:
                    ocupied = 0
                cnx.close()
        pygame.draw.rect(screen, (0, 0, 0), (100, 280, 180, 20))
        draw_text("randomize".upper(), font, letter_color, screen, 100 - transition, 280)
        if randomizeP1 == True:
            selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
            randomizeP1 = randint(0, 1)
        if button_right1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
        if button_left1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 - 1) % len(CHARACTERS)
        if button_right2.collidepoint((mx, my)):
            if click:
                serverSelection = (serverSelection + 1) % len(servers)
        if button_left2.collidepoint((mx, my)):
            if click:
                serverSelection = (serverSelection - 1) % len(servers)
        if button_7.collidepoint((mx, my)):
            if click:
                main_menu()
        if button_9.collidepoint((mx, my)):
            if click:
                if ocupied == 0:
                    passwd = login(str(servers[serverSelection]), 1)
                    game(selectionP1, "online", onlineplayer=1, passwd = passwd)
                elif ocupied == 1:
                    passwd = login(str(servers[serverSelection]), 2)
                    game(selectionP1, "online", onlineplayer=2, passwd = passwd)
        if button_11.collidepoint((mx, my)):
            if click:
                randomizeP1 = True
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if transition > 0:
            temp = transition
            temp -= 30
            if temp < 0:
                transition = 0
            else:
                transition -= 30
        pygame.display.update()
        mainClock.tick(60)

def world_tour_menu():
    '''Este es el menu del Wordl Tour donde hemos dibujado los botones le hemos puesto musica i se pueden 
    elegir diferentes personajes para intentar pasarte el modo historia'''
    pygame.display.set_caption("STREET FIGHTER: WORLD TOUR MENU", "STRF")
    CONTROL["music"].play(SONS["seleccio"])
    selectionP1 = 0
    click = False
    transition = WIDTH
    running = True
    randomizeP1 = False
    global difficulty
    global sound_effects
    global music
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/VS.jpg').convert()
    arrow1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector.png').convert()
    arrow2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector2.png').convert()
    button_left1 = pygame.Rect(60, 60, 40, 40)
    button_right1 = pygame.Rect(260, 60, 40, 40)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()
        if load()[1] == 0:
            screen.blit(arrow2, (60, 60))
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        screen.blit(CHARACTERS[selectionP1][2], (110 - transition, 100))
        if load()[1] != 0:
            screen.blit(CHARACTERS[load()[5][1]][2], (WIDTH // 2 + 110 - transition, 100))
        if load()[1] == 0:
            screen.blit(arrow1, (260 - transition, 60))
        pygame.draw.rect(screen, (0, 0, 0), (110, 70, 150, 20))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 110, 70, 150, 20))
        draw_text('w.T. SELECT'.upper(), font, letter_color, screen, WIDTH // 2 - 190//2 - transition, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80 - transition, 20)
        draw_text('1P'.upper(), font, letter_color, screen, 160 - transition, 40)
        draw_text(CHARACTERS[selectionP1][1].upper(), font, letter_color, screen, 120 - transition, 70)
        if load()[1] > 0:
            draw_text(CHARACTERS[load()[5][1]][1].upper(), font, letter_color, screen, WIDTH // 2 + 120 - transition, 70)
        draw_text('CPU'.upper(), font, letter_color, screen, WIDTH // 2 + 160 - transition, 40)
        if load()[1] > 0:
            draw_text(CHARACTERS[load()[5][1]][1].upper(), font, letter_color, screen, WIDTH // 2 + 120 - transition, 70)
        draw_text('PLAY'.upper(), font, letter_color, screen, WIDTH // 1.5 - transition, 20)
        draw_text(CHARACTERS[selectionP1][0].upper(), font, letter_color, screen, 120 - transition, 250)
        if load()[1] > 0:
            draw_text(CHARACTERS[load()[5][1]][0].upper(), font, letter_color, screen, WIDTH // 2 + 120 - transition, 250)
        pygame.draw.rect(screen, (0, 0, 0), (100, 280, 180, 20))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 100, 280, 180, 20))
        draw_text("randomize".upper(), font, letter_color, screen, 100 - transition, 280)
        draw_text("new game".upper(), font, letter_color, screen, WIDTH // 2 + 100 - transition, 280)
        if randomizeP1 == True:
            selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
            randomizeP1 = randint(0, 1)
        if button_right1.collidepoint((mx, my)) and load()[5][1] == 0:
            if click:
                selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
        if button_left1.collidepoint((mx, my)) and load()[5][1] == 0:
            if click:
                selectionP1 = (selectionP1 - 1) % len(CHARACTERS)
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        if button_9.collidepoint((mx, my)):
            if click:
                if load()[1] > 0:
                    draw_text("Loading", font, (0, 0, 0), screen, WIDTH // 2 - 40, HEIGHT // 2)
                    pygame.display.update()
                    sleep(1.5)
                    game(selectionP1, "worldtour", P2=load()[1], level=load()[1])
                else:
                    world_tour(selectionP1, 1)
        if button_11.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                randomizeP1 = True
        if button_12.collidepoint((mx, my)):
            if click:
                save(0, 0, 0, 0, 0, 0)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if transition > 0:
            temp = transition
            temp -= 30
            if temp < 0:
                transition = 0
            else:
                transition -= 30
        pygame.display.update()
        mainClock.tick(60)

def world_tour(selectionP1, level):
    '''Aqui muestra una prepartida del World Tour'''
    pygame.display.set_caption("STREET FIGHTER: WORLD TOUR COMBAT", "STRF")
    CONTROL["music"].play(SONS["seleccio"])
    selectionCPU = level - 1
    if selectionP1 == selectionCPU:
        selectionCPU = (selectionCPU + 1) % len(CHARACTERS)
    click = False
    transition = WIDTH
    running = True
    global difficulty
    global sound_effects
    global music
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/VS.jpg').convert()
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        screen.blit(CHARACTERS[selectionP1][2], (110 - transition, 100))
        screen.blit(CHARACTERS[selectionCPU][2], (WIDTH // 2 + 110 - transition, 100))
        pygame.draw.rect(screen, (0, 0, 0), (110, 70, 150, 20))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 110, 70, 150, 20))
        draw_text('world tour'.upper(), font, letter_color, screen, WIDTH // 2 - 100 - transition, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80 - transition, 20)
        draw_text('1P'.upper(), font, letter_color, screen, 160 - transition, 40)
        draw_text(CHARACTERS[selectionP1][1].upper(), font, letter_color, screen, 120 - transition, 70)
        draw_text('CPU'.upper(), font, letter_color, screen, WIDTH // 2 + 160 - transition, 40)
        draw_text(CHARACTERS[selectionCPU][1].upper(), font, letter_color, screen, WIDTH // 2 + 120 - transition, 70)
        draw_text('PLAY'.upper(), font, letter_color, screen, WIDTH // 1.5 - transition, 20)
        draw_text(CHARACTERS[selectionP1][0].upper(), font, letter_color, screen, 120 - transition, 250)
        draw_text(CHARACTERS[selectionCPU][0].upper(), font, letter_color, screen, WIDTH // 2 + 120 - transition, 250)
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        if button_9.collidepoint((mx, my)):
            if click:
                game(selectionP1, "worldtour", P2 = selectionCPU, level = level)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if transition > 0:
            temp = transition
            temp -= 30
            if temp < 0:
                transition = 0
            else:
                transition -= 30
        pygame.display.update()
        mainClock.tick(60)

def _1vs1_menu():
    '''Este es el menu del modo jugador contra jugador cargamos imagenes y musica y botones'''
    pygame.display.set_caption("STREET FIGHTER: 1 VS 1 MENU", "STRF")
    pygame.display.set_caption("STREET FIGHTER: OPTIONS", "STRF")
    CONTROL["music"].play(SONS["seleccio"])
    selectionP1 = 0
    selectionP2 = 0
    click = False
    transition = WIDTH
    running = True
    randomizeP1 = False
    randomizeP2 = False
    global difficulty
    global sound_effects
    global music
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/VS.jpg').convert()
    arrow1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector.png').convert()
    arrow2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector2.png').convert()
    button_left1 = pygame.Rect(60, 60, 40, 40)
    button_right1 = pygame.Rect(260, 60, 40, 40)
    button_left2 = pygame.Rect(WIDTH//2+60, 60, 40, 40)
    button_right2 = pygame.Rect(WIDTH//2+260, 60, 40, 40)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0,0))
        mx, my = pygame.mouse.get_pos()
        screen.blit(arrow2, (60, 60))
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        screen.blit(CHARACTERS[selectionP1][2], (110-transition, 100))
        screen.blit(CHARACTERS[selectionP2][2], (WIDTH//2+110 -transition, 100))
        screen.blit(arrow1, (260-transition, 60))
        screen.blit(arrow2, (WIDTH//2+60-transition, 60))
        pygame.draw.rect(screen, (0,0,0), (110, 70, 150, 20))
        screen.blit(arrow1, (WIDTH//2+260-transition, 60))
        pygame.draw.rect(screen, (0,0,0), (WIDTH//2+110, 70, 150, 20))
        draw_text('1 vs 1'.upper(), font, letter_color, screen, WIDTH // 2-35-transition, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80-transition, 20)
        draw_text('1P'.upper(), font, letter_color, screen, 160-transition, 40)
        draw_text(CHARACTERS[selectionP1][1].upper(), font, letter_color, screen, 120-transition, 70)
        draw_text('2P'.upper(), font, letter_color, screen, WIDTH//2+160-transition, 40)
        draw_text(CHARACTERS[selectionP2][1].upper(), font, letter_color, screen, WIDTH//2+120-transition, 70)
        draw_text('PLAY'.upper(), font, letter_color, screen, WIDTH // 1.5-transition, 20)
        draw_text(CHARACTERS[selectionP1][0].upper(), font, letter_color, screen, 120-transition, 250)
        draw_text(CHARACTERS[selectionP2][0].upper(), font, letter_color, screen, WIDTH // 2 + 120-transition, 250)
        pygame.draw.rect(screen, (0, 0, 0), (100, 280, 180, 20))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH//2+100, 280, 180, 20))
        draw_text("randomize".upper(), font, letter_color, screen, 100-transition, 280)
        draw_text("randomize".upper(), font, letter_color, screen, WIDTH // 2 + 100-transition, 280)
        if randomizeP1 == True:
            selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
            randomizeP1 = randint(0, 1)
            CONTROL["efects"].play(EFECTS["escollir"])
        if randomizeP2 == True:
            selectionP2 = (selectionP2 + 1) % len(CHARACTERS)
            randomizeP2 = randint(0,1)
            CONTROL["efects"].play(EFECTS["escollir"])
        if button_right1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_left1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 - 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_right2.collidepoint((mx, my)):
            if click:
                selectionP2 = (selectionP2 + 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_left2.collidepoint((mx, my)):
            if click:
                selectionP2 = (selectionP2 - 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        if button_9.collidepoint((mx, my)):
            if click:
                game(selectionP1, "1vs1", combat_times[combat_time][1], selectionP2)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_11.collidepoint((mx, my)):
            if click:
                randomizeP1 = True
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_12.collidepoint((mx, my)):
            if click:
                randomizeP2 = True
                CONTROL["efects"].play(EFECTS["escollir"])
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if transition > 0:
            temp = transition
            temp -= 30
            if temp < 0:
                transition = 0
            else:
                transition -= 30
        pygame.display.update()
        mainClock.tick(60)

def _1vscpu_menu():
    '''Este es el menu del modo jugador contra la CPU cargamos imagenes y musica y botones'''
    pygame.display.set_caption("STREET FIGHTER: 1 VS CPU MENU", "STRF")
    pygame.display.set_caption("STREET FIGHTER: OPTIONS", "STRF")
    CONTROL["music"].play(SONS["seleccio"])
    selectionP1 = 0
    selectionCPU = 0
    click = False
    running = True
    transition = WIDTH
    randomizeP1 = False
    randomizeCPU = False
    global difficulty
    global sound_effects
    global music
    cpu_choose = False
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/VS.jpg').convert()
    arrow1 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector.png').convert()
    arrow2 = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/selector2.png').convert()
    button_left1 = pygame.Rect(60, 60, 40, 40)
    button_right1 = pygame.Rect(260, 60, 40, 40)
    button_left2 = pygame.Rect(WIDTH // 2 + 60, 60, 40, 40)
    button_right2 = pygame.Rect(WIDTH // 2 + 260, 60, 40, 40)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()
        screen.blit(arrow2, (60+transition, 60))
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        screen.blit(CHARACTERS[selectionP1][2], (110+transition, 100))
        screen.blit(CHARACTERS[selectionCPU][2], (WIDTH // 2 + 110+transition, 100))
        screen.blit(arrow1, (260+transition, 60))
        screen.blit(arrow2, (WIDTH // 2 + 60+transition, 60))
        pygame.draw.rect(screen, (0, 0, 0), (110, 70, 150, 20))
        screen.blit(arrow1, (WIDTH // 2 + 260+transition, 60))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 110, 70, 150, 20))
        draw_text('1 vs CPU'.upper(), font, letter_color, screen, WIDTH // 2 - 35 +transition, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80+transition, 20)
        draw_text('1P'.upper(), font, letter_color, screen, 160+transition, 40)
        draw_text(CHARACTERS[selectionP1][1].upper(), font, letter_color, screen, 120+transition, 70)
        draw_text('cpu'.upper(), font, letter_color, screen, WIDTH // 2 + 160+transition, 40)
        draw_text(CHARACTERS[selectionCPU][1].upper(), font, letter_color, screen, WIDTH // 2 + 120+transition, 70)
        draw_text('PLAY'.upper(), font, letter_color, screen, WIDTH // 1.5+transition, 20)
        draw_text(CHARACTERS[selectionP1][0].upper(), font, letter_color, screen, 120+transition, 250)
        draw_text(CHARACTERS[selectionCPU][0].upper(), font, letter_color, screen, WIDTH // 2 + 120+transition, 250)
        pygame.draw.rect(screen, (0, 0, 0), (100, 280, 180, 20))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 + 100, 280, 180, 20))
        if cpu_choose == True:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 2 + 100, 300, 190, 20))
            selectionCPU = 3
        else:
            pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 2 + 100+transition, 300, 190, 20))
        draw_text("randomize".upper(), font, letter_color, screen, 100+transition, 280)
        draw_text("randomize".upper(), font, letter_color, screen, WIDTH // 2 + 100+transition, 280)
        draw_text("cpu choose".upper(), font, letter_color, screen, WIDTH // 2 + 100+transition, 300)
        if randomizeP1 == True:
            selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
            randomizeP1 = randint(0, 1)
            CONTROL["efects"].play(EFECTS["escollir"])
        if randomizeCPU == True:
            selectionCPU = (selectionCPU + 1) % len(CHARACTERS)
            randomizeCPU = randint(0,1)
            CONTROL["efects"].play(EFECTS["escollir"])
        if button_right1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 + 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_left1.collidepoint((mx, my)):
            if click:
                selectionP1 = (selectionP1 - 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_right2.collidepoint((mx, my)):
            if click:
                selectionCPU = (selectionCPU + 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_left2.collidepoint((mx, my)):
            if click:
                selectionCPU = (selectionCPU - 1) % len(CHARACTERS)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        if button_9.collidepoint((mx, my)):
            if click:
                game(selectionP1, "1vscpu", combat_times[combat_time][1], selectionCPU)
                CONTROL["efects"].play(EFECTS["escollir"])
        if button_11.collidepoint((mx, my)):
            if click:
                randomizeP1 = True
        if button_12.collidepoint((mx, my)):
            if click:
                randomizeCPU = True
        if button_13.collidepoint((mx, my)):
            if click:
                cpu_choose = not cpu_choose
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if transition > 0:
            temp = transition
            temp -= 30
            if temp < 0:
                transition = 0
            else:
                transition -= 30
        pygame.display.update()
        mainClock.tick(60)

def credits():
    '''Esta funcion muestra la informacion sobre el juego'''
    pygame.display.set_caption("STREET FIGHTER: CREDITS", "STRF")
    click = False
    running = True
    credit_height = HEIGHT
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/credits.png').convert()
    while running:
        screen.fill((13, 92, 98))
        screen.blit(background,(WIDTH-188,HEIGHT//2-150))
        mx, my = pygame.mouse.get_pos()
        draw_text('music                scarybeats'.upper(), font, letter_color, screen, 80, credit_height)
        draw_text('production           pol&jose'.upper(), font, letter_color, screen, 80, credit_height + 20)
        draw_text('idea                 pol&jose'.upper(), font, letter_color, screen, 80, credit_height + 40)
        draw_text('menus                pol&jose'.upper(), font, letter_color, screen, 80, credit_height + 60)
        draw_text('scarybeats           pol'.upper(), font, letter_color, screen, 80, credit_height + 100)
        draw_text('softssl              pol&jose'.upper(), font, letter_color, screen, 80, credit_height + 120)
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        draw_text('credits'.upper(), font, letter_color, screen, WIDTH // 2 - 35, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80, 20)
        credit_height = (credit_height - 1)%(HEIGHT*2)
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mainClock.tick(60)
        pygame.display.update()

def stats():
    '''Aqui muestra la estadistica de hasta que nivel has llegado en el modo World Tour'''
    pygame.display.set_caption("STREET FIGHTER: STATS", "STRF")
    click = False
    running = True
    credit_height = HEIGHT
    background = pygame.image.load(f'{os.path.dirname(__file__)}/imatges/fons/menu/credits.png').convert()
    while running:
        screen.fill((13, 92, 98))
        screen.blit(background, (WIDTH - 188, HEIGHT // 2 - 150))
        mx, my = pygame.mouse.get_pos()
        if load()[1] > 0:
            draw_text(f'Level                {load()[1]}'.upper(), font, letter_color, screen, 80, credit_height)
        else:
            draw_text('Level                not played'.upper(), font, letter_color, screen, 80, credit_height)
        pygame.draw.rect(screen, (0, 72, 82), (0, 0, WIDTH, 40))
        draw_text('stats'.upper(), font, letter_color, screen, WIDTH // 2 - 35, 20)
        draw_text('main menu'.upper(), font, letter_color, screen, 80, 20)
        credit_height = (credit_height - 1) % (HEIGHT * 2)
        if button_7.collidepoint((mx, my)):
            if click:
                CONTROL["efects"].play(EFECTS["escollir"])
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mainClock.tick(60)
        pygame.display.update()

class AnimatedBackground(pygame.sprite.Sprite):
    '''Aqui se carga el fondo animado de cada mapa'''
    def __init__(self, position, images, delay):
        super(AnimatedBackground, self).__init__()
        self.images = itertools.cycle(images)
        self.image = next(self.images)
        self.rect = pygame.Rect(position,  self.image.get_rect().size)
        self.animation_time = delay
        self.current_time = 0
    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image = next(self.images)

def load_images(path):
    '''Esta funcion carga todas las imagenes que utilizamos en el juego'''
    images = [pygame.image.load(path + os.sep + file_name).convert() for file_name in sorted(os.listdir(path))]
    return images

px = [54, WIDTH-108]
py = [HEIGHT-200, HEIGHT-200]
ancho = [108, 108]
velocidad = [12, 12]
salto = [False, False]
cuentaSalto = [10, 10]
patada = [False, False]
cuentapatada = [5, 5]
punyo = [False, False]
cuentapunyo = [5, 5]
izquierda = [False, False]
derecha = [False, False]
damaged = [False, False]
sit = [False, False]
win = [False, False]
heal = [0,0]
cuentaPasos = [0, 0]
facing = [0, 1] #0 derecha 1 izquierda
FPS = 60
endtransition = 0
agacharse = [False,False]
cuentaagacha = [10,10]
kick = [False,False]
punch = [False,False]
rects = ["", ""]

def main():
    '''Carga el antihack'''
    gen_hash()
    if load_hash():
        pygame.init()
        pygame.display.set_caption("STREET FIGHTER", "STRF")
        main_menu()

def game(P1, mode, time=300, P2 = 0, passwd = "", onlineplayer = "", level=0):
    '''En esta funcion se encuentra el motor del juego'''
    BACKGROUND_COLOR = pygame.Color('black')
    CONTROL["efects"].play(EFECTS["start"])
    screen = pygame.display.set_mode(SIZE)
    global px
    global py
    global ancho
    global velocidad
    global CHARACTERS
    global salto
    global cuentaSalto
    global patada
    global cuentapatada
    global punyo
    global cuentapunyo
    global izquierda
    global derecha
    global facing
    global cuentaPasos
    global endtransition
    global serverSelection
    global heal
    global agacharse
    global cuentaagacha
    global kick
    global punch
    global rects
    global win
    global difficulty
    response = 4
    endmatch = False
    #Para reiniciar la partida
    px = [54, WIDTH - 108]
    py = [HEIGHT - 200, HEIGHT - 200]
    ancho = [108, 108]
    velocidad = [12, 12]
    salto = [False, False]
    cuentaSalto = [10, 10]
    patada = [False, False]
    cuentapatada = [10, 10]
    punyo = [False, False]
    cuentapunyo = [10, 10]
    izquierda = [False, False]
    derecha = [False, False]
    damaged = [False, False]
    agacharse = [False, False]
    win = [False, False]
    cuentaagacha = [10, 10]
    if mode == "worldtour":
        if load()[1] >= level:
            time, level, px, py, heal, P1 = load()
            P2 = P1[1]
            P1 = P1[0]
    punch = [CHARACTERS[P1][4]["punch"], CHARACTERS[P2][4]["punch"]]
    kick = [CHARACTERS[P1][4]["kick"], CHARACTERS[P2][4]["kick"]]
    cuentaPasos = [0, 0]
    facing = [0, 1]  # 0 derecha 1 izquierda
    FPS = 60
    endtransition = 0
    heal = [CHARACTERS[P1][4]["heal"], CHARACTERS[P2][4]["heal"]]
    if mode == "online":
        if onlineplayer == 1:
            onlineplayer2 = 2
        else:
            onlineplayer2 = 1
        cnox = mysql.connector.connect(user=f'p{onlineplayer}',
                                       password=passwd,
                                       host=str(servers[serverSelection]),
                                       port=50000,
                                       connection_timeout=1,
                                       database='strf')
        cnox.autocommit = True
        cursor = cnox.cursor()
        cursor.execute(f"UPDATE p{onlineplayer} SET selection = {P1}")
        cursor.execute(f"UPDATE p{onlineplayer} SET life = {CHARACTERS[P1][4]['heal']}")
        cursor.execute(f"SELECT selection FROM p{onlineplayer2}")
        P2 = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT life FROM p{onlineplayer2}")
        heal[1] = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT k FROM login2")
        ocupied = cursor.fetchall()[0][0]
        cnox.commit()
    else:
        ocupied = True
    clock = pygame.time.Clock()
    list_images_fons = []
    for i in range(8):
        list_images_fons.append(load_images(path=os.path.join(os.path.dirname(__file__), 'imatges', 'fons', str(i+1))))
    if mode in ['1vs1', '1vscpu', 'online']:
        images_fons = list_images_fons[randrange(0,3)]
    else:
        images_fons = list_images_fons[P2]
    background = AnimatedBackground(position=(0, 0), images=images_fons, delay = 0.03)
    all_sprites = pygame.sprite.Group(background)
    CONTROL["music"].play(SONS["asian"], 5, 0, 0)
    prematch = 4
    FPS = 18
    transition = 0
    while int(prematch) != 0:
        transition = (transition+ 1/FPS)%2
        dt = clock.tick(FPS) / 200*(len(images_fons) )
        all_sprites.update(dt)
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        if mode == "online":
            if ocupied:
                draw_text(str(int(prematch)), font2, (0, 0, 0), screen, WIDTH // 2 - 30, HEIGHT//2-20)
            else:
                if int(transition) < 1:
                    draw_text("Waiting", font2, (0, 0, 0), screen, WIDTH // 2 - 7*80//2, HEIGHT // 2 - 20)
        else:
            draw_text(str(int(prematch)), font2, (0, 0, 0), screen, WIDTH // 2 - 30, HEIGHT // 2 - 20)
        pygame.display.update()
        if mode == "online":
            cursor.execute(f"SELECT k FROM login2")
            ocupied = int(cursor.fetchall()[0][0])
            if ocupied != 0:
                ocupied = False
            else:
                ocupied = True
                prematch = prematch - 1 / FPS
        else:
            prematch = prematch - 1 / FPS
    while True:
        mainClock.tick(FPS)
        velocidad[0] = CHARACTERS[P1][4]["speed"]
        velocidad[1] = CHARACTERS[P2][4]["speed"]
        if mode == "online":
            try:
                cursor.execute('SELECT partida_empezada FROM partida_empezada')
                partida_empezada = cursor.fetchall()[0][0]
                print(partida_empezada)
                if not partida_empezada:
                    main_menu()
                cursor.execute(f"UPDATE p{onlineplayer} SET life = {heal[0]}, left_ = {izquierda[0]}, life = {heal[0]}, left_ = {izquierda[0]}, right_ = {derecha[0]}, up_ = {salto[0]}, down_ = {salto[0]}, punch = {punyo[0]}, kick = {patada[0]}, damaged = {damaged[0]}, px = {px[0]}, py = {py[0]}, facing = {facing[0]}")
                cnox.commit()
                cursor.execute(f"SELECT left_, up_, down_, right_, punch, kick, damaged, life, selection, px, py, facing FROM p{onlineplayer2}")
                izquierda[1], salto[1], sit[1], derecha[1], punyo[1], patada[1], damaged[1], heal[1], P2, px[1], py[1], facing[1] = cursor.fetchall()[0]
                #print(izquierda[1], salto[1], sit[1], derecha[1], punyo[1], patada[1], damaged[1], heal[1], P2, px[1], py[1], facing[1])
                #print(cursor.fetchall())
            except mysql.connector.Error as err:
                print(err)
        elif mode == "worldtour":
            if randint(0,FPS*2) == 0:
                save(time, level, px, py, heal, [P1, P2])
        if px[0] > WIDTH - 108:
            px[0] = WIDTH -108
        if px[1] > WIDTH - 108:
            px[1] = WIDTH -108
        if px[0] < 0:
            px[0] = 0
        if px[1] < 0:
            px[1] = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if mode == "online":
                    cursor.execute(f"UPDATE partida_empezada SET partida_empezada = FALSE")
                    cnox.commit()
                sys.exit()
        keys = pygame.key.get_pressed()
        #background = AnimatedBackground(position=(0, 0), images=images_fons, delay=0.03)
        all_sprites.update(dt)
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, WIDTH, HEIGHT], 5)
        screen.blit(barravida1, (
        (18 - barravida1.get_rect()[2] + heal[0] * barravida1.get_rect()[2] / CHARACTERS[P1][4]['heal']), 24))
        screen.blit(barravida2, (
        (WIDTH - 186 + barravida2.get_rect()[2] - heal[1] * barravida2.get_rect()[2] / CHARACTERS[P2][4]['heal']), 24))
        screen.blit(cuadrovida1, (0, 20))
        screen.blit(cuadrovida2, (WIDTH-cuadrovida2.get_rect()[2], 20))
        if keys[pygame.K_a] and px[0] > velocidad[0] and not endmatch:
            if salto[0] == False:
                px[0] -= velocidad[0]
            else:
                px[0] -= velocidad[0]//2
            izquierda[0] = True
            facing[0] = 1
            derecha[0] = False
        # Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_d] and px[0] < 900 - velocidad[0] - ancho[0] and not endmatch:
            if salto[0] == False:
                px[0] += velocidad[0]
            else:
                px[0] += velocidad[0] // 2
            izquierda[0] = False
            facing[0] = 0
            derecha[0] = True
        # Personaje quieto
        else:
            izquierda[0] = False
            derecha[0] = False
            # cuentaPasos = 0
        # Tecla SPACE - Salto
        if not (salto[0]):
            if keys[pygame.K_w]  and not endmatch:
                salto[0] = True
                cuentaPasos[0] = 0
        else:
            if cuentaSalto[0] >= -10:
                py[0] -= (cuentaSalto[0] * abs(cuentaSalto[0])) * 0.5
                cuentaSalto[0] -= 1
                izquierda[0] = False
                derecha[0] = False
            else:
                cuentaSalto[0] = 10
                salto[0] = False
        # Tecla patada g
        if not (patada[0]):
            if keys[pygame.K_g] and not endmatch:
                patada[0] = True
                izquierda[0] = False
                derecha[0] = False
                cuentaPasos[0] = 0
        else:
            if cuentapatada[0] >= -5:
                cuentapatada[0] -= 1
            else:
                cuentapatada[0] = 10
                patada[0] = False
        # Tecla puño h
        if not (punyo[0]):
            if keys[pygame.K_h] and not endmatch:
                punyo[0] = True
                izquierda[0] = False
                derecha[0] = False
                cuentaPasos[0] = 0
        else:
            if cuentapunyo[0] >= 0:
                cuentapunyo[0] -= 1
            else:
                cuentapunyo[0] = 10
                punyo[0] = False
        if not (agacharse[0]):
            if keys[pygame.K_s]:
                agacharse[0] = True
                cuentaPasos[0] = 0
        else:
            if cuentaagacha[0] == -5:
                cuentaagacha[0] -= 1
                izquierda[0] = False
                derecha[0] = False
            else:
                cuentaagacha[0] = 10
                agacharse[0] = False
        #P2
        if mode == "1vs1":
            if keys[pygame.K_LEFT] and px[1] > velocidad[1] and not endmatch:
                px[1] -= velocidad[1]
                izquierda[1] = True
                facing[1] = 1
                derecha[1] = False
            # Tecla D - Moviemiento a la derecha
            elif keys[pygame.K_RIGHT] and px[1] < 900 - velocidad[1] - ancho[1] and not endmatch:
                px[1] += velocidad[1]
                izquierda[1] = False
                facing[1] = 0
                derecha[1] = True
            # Personaje quieto
            else:
                izquierda[1] = False
                derecha[1] = False
                # cuentaPasos = 0
            # Tecla SPACE - Salto
            if not (salto[1]):
                if keys[pygame.K_UP]  and not endmatch:
                    salto[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentaSalto[1] >= -10:
                    izquierda[0] = False
                    derecha[0] = False
                    py[1] -= (cuentaSalto[1] * abs(cuentaSalto[1])) * 0.5
                    cuentaSalto[1] -= 1
                else:
                    cuentaSalto[1] = 10
                    salto[1] = False
            # Tecla patada g
            if not (patada[1]):
                if keys[pygame.K_m] and not endmatch:
                    patada[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentapatada[1] >= -5:
                    cuentapatada[1] -= 1
                else:
                    cuentapatada[1] = 10
                    patada[1] = False
            # Tecla puño h
            if not (punyo[1]):
                if keys[pygame.K_n]  and not endmatch:
                    punyo[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentapunyo[1] >= 0:
                    cuentapunyo[1] -= 1
                else:
                    cuentapunyo[1] = 10
                    punyo[1] = False
            if not (agacharse[1]):
                if keys[pygame.K_DOWN]:
                    agacharse[1] = True
                    cuentaPasos[1] = 0
            else:
                if cuentaagacha[1] == -5:
                    cuentaagacha[1] -= 1
                    izquierda[1] = False
                    derecha[1] = False
                else:
                    cuentaagacha[1] = 10
                    agacharse[1] = False
        elif mode in ["1vscpu", "worldtour"]:
            if ((px[0] < px[1] + randint(20,80) ) and randint(difficulty,2) == 2 or px[1] == WIDTH - CHARACTERS[P1][3][0][facing[0]].get_rect()[2]) and not endmatch:
                px[1] -= velocidad[1]
                izquierda[1] = True
                facing[1] = 1
                derecha[1] = False
            # Tecla D - Moviemiento a la derecha
            elif ((px[0] > px[1] + randint(20,80) and not endmatch) and randint(difficulty,2) == 2 or px[1] == 0) and not endmatch:
                px[1] += velocidad[1]
                izquierda[1] = False
                facing[1] = 0
                derecha[1] = True
            # Personaje quieto
            else:
                izquierda[1] = False
                derecha[1] = False
                # cuentaPasos = 0
            # Tecla SPACE - Salto
            if not (salto[1]):
                if ((randint(0,80) == 20 or (px[0] in range(px[1]-80, px[1]-20) or px[0] in range(px[1]+80, px[1]+20)) and randint(0,20) == 10) and randint(difficulty,2) == 2) and not endmatch:
                    salto[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentaSalto[1] >= -10:
                    izquierda[1] = False
                    derecha[1] = False
                    py[1] -= (cuentaSalto[1] * abs(cuentaSalto[1])) * 0.5
                    cuentaSalto[1] -= 1
                else:
                    cuentaSalto[1] = 10
                    salto[1] = False
            # Tecla patada g
            if not (patada[1]):
                if ((px[0] in range(px[1]-60, px[1]+100) and randint(0,2) == 0) and randint(difficulty,2) == 2 and randint(0, response) == response)  and not endmatch:
                    patada[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    punyo[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentapatada[1] >= -5:
                    cuentapatada[1] -= 1
                else:
                    cuentapatada[1] = 10
                    patada[1] = False
            # Tecla puño h
            if not (punyo[1]):
                if ((px[0] in range(px[1]-40, px[1]+80) and randint(0,2) == 0) and randint(difficulty,2) == 2 and randint(0,response) == response) and not endmatch:
                    punyo[1] = True
                    izquierda[1] = False
                    derecha[1] = False
                    patada[1] = False
                    cuentaPasos[1] = 0
            else:
                if cuentapunyo[1] >= 0:
                    cuentapunyo[1] -= 1
                else:
                    cuentapunyo[1] = 10
                    punyo[1] = False
            if not (agacharse[1]):
                if ((randint(0,40) == 20 or px[0] in range(px[1]-80, px[1]+80) and randint(0,10) == 10) and randint(difficulty,2) == 2) and not endmatch:
                    agacharse[1] = True
                    cuentaPasos[1] = 0
            else:
                if cuentaagacha[1] == -5:
                    cuentaagacha[1] -= 1
                    izquierda[1] = False
                    derecha[1] = False
        if mode == "worldtour" and level > 3:
            if heal[1] < CHARACTERS[P1][4]['heal'] * 0.75 and level == 4:
                level += 1
                images_fons = list_images_fons[4]
                background = AnimatedBackground(position=(0, 0), images=images_fons, delay=0.03)
                all_sprites = pygame.sprite.Group(background)
                all_sprites.update(dt)
                if randint(0,3) == 3:
                    heal[1] += randint(0, CHARACTERS[P1][4]['heal'] * 0.25)
            if heal[1] < CHARACTERS[P1][4]['heal'] * 0.50 and level == 5:
                level += 1
                images_fons = list_images_fons[5]
                background = AnimatedBackground(position=(0, 0), images=images_fons, delay=0.03)
                all_sprites = pygame.sprite.Group(background)
                all_sprites.update(dt)
                if randint(0,1) == 1:
                    heal[1] += randint(0, CHARACTERS[P1][4]['heal'] * 0.25)
            if heal[1] < CHARACTERS[P1][4]['heal'] * 0.25 and level == 6:
                level += 1
                images_fons = list_images_fons[6]
                background = AnimatedBackground(position=(0, 0), images=images_fons, delay=0.03)
                all_sprites = pygame.sprite.Group(background)
                all_sprites.update(dt)
                heal[1] += randint(0, CHARACTERS[P1][4]['heal'] * 0.15)
            if heal[1] <= 0:
                level += 1
                images_fons = list_images_fons[7]
                background = AnimatedBackground(position=(0, 0), images=images_fons, delay=0.03)
                all_sprites = pygame.sprite.Group(background)
                all_sprites.update(dt)
        if time != -5:
            time = time - 1 / FPS
            if int(time) > 3:
                draw_text(str(int(time)), font, (0, 0, 0), screen, WIDTH // 2-30, 20)
            else:
                draw_text(str(int(time)), font, (255, 0, 0), screen, WIDTH // 2 - 30, 20)
        if int(time) <= 0 and time != -5 or heal[0] <= 0 or heal[1] <= 0:
            endmatch = True
            endtransition = endtransition + 1 / FPS
            if heal[0] > heal[1]:
                if endtransition == 0.05555555555555555:
                    CONTROL["efects"].play(EFECTS["lose"], 0, 0, 0)
                if mode == "worldtour":
                    draw_text(f"You win {CHARACTERS[P1][1]}", font, (0, 0, 0), screen,
                              WIDTH // 2 - 60 - len(CHARACTERS[P1][1]) // 2, HEIGHT // 2)
                else:
                    draw_text(f"WINNER {CHARACTERS[P1][1]}", font, (0, 0, 0), screen, WIDTH // 2 - 60 - len(CHARACTERS[P1][1])//2, HEIGHT//2)
                win[0] = True
            elif heal[0] < heal[1]:
                if endtransition == 0.05555555555555555:
                    CONTROL["efects"].play(EFECTS["lose"], 0, 0, 0)
                if mode == "worldtour":
                    draw_text(f"You lost {CHARACTERS[P1][1]}", font, (0, 0, 0), screen,
                              WIDTH // 2 - 60 - len(CHARACTERS[P2][1]) // 2, HEIGHT // 2)
                else:
                    draw_text(f"WINNER {CHARACTERS[P2][1]}", font, (0, 0, 0), screen, WIDTH // 2 - 60 - len(CHARACTERS[P2][1])//2, HEIGHT // 2)
                win[1] = True
            else:
                draw_text(f"DRAW", font, (0, 0, 0), screen, WIDTH // 2 - 40, HEIGHT // 2)
            if int(endtransition) == 6:
                FPS = 60
                SONS["asian"].fadeout(1000)
                if mode != "worldtour":
                    main_menu()
                else:
                    if level <= 4:
                        if heal[0] == heal[1]:
                            world_tour(P1, level)
                        elif heal[0] > heal[1]:
                            if difficulty != 2 and level != 1:
                                difficulty += 1
                            world_tour(P1,level+1)
                        else:
                            save(time, 0, px, py, heal, [P1, P2])
                            world_tour_menu()
                    else:
                        save(0, 0, 0, 0, 0, 0)
                        end(P1)
                        break
                        
        recargaPantalla(P1, P2, time)
        pygame.display.update()

pospatada = ["", ""]
pospunyo = ["", ""]

def recargaPantalla(P1, P2, time):
    '''Esta funcion lo que hace es crear el movimiento de los personajes con todos sus movimientos'''
    #Variables globales
    global cuentaPasos
    global izquierda
    global derecha
    global salto
    global punyo
    global FPS
    global patada
    global endtransition
    global facing
    global agacharse
    global cuentaagacha
    global kick
    global punch
    global cuentapatada
    global cuentapunyo
    global rects
    global win
    global pospatada
    global pospunyo
    if not salto[0]:
        if py[0] < 167:
            py[0] += 1
        elif py[0] < 167:
            py[0] -= 1
    if not salto[1]:
        if py[1] < 167:
            py[1] += 1
        elif py[1] > 167:
            py[1] -= 1
    #Fondo en movimiento
    #Contador de pasos
    cuentaPasos[0] = (cuentaPasos[0] + 1) % (60*2)
    cuentaFinal = 0
    #Movimiento a la izquierda
    if not win[0] and not win[1]:
        if izquierda[0]:
            screen.blit(CHARACTERS[P1][3][1][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][1][facing[0]]))],
                        (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][1][facing[0]][
                int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][1][facing[0]]))].get_rect()
            # Movimiento a la derecha
        elif derecha[0]:
            screen.blit(CHARACTERS[P1][3][1][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][1][facing[0]]))],
                        (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][1][facing[0]][
                int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][1][facing[0]]))].get_rect()
        elif salto[0]:
            screen.blit(CHARACTERS[P1][3][2][facing[0]][int(cuentaPasos[0] // 6 % len(CHARACTERS[P1][3][2][facing[0]]))],
                        (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][2][facing[0]][
                int(cuentaPasos[0] // 6 % len(CHARACTERS[P1][3][2][facing[0]]))].get_rect()
        elif patada[0]:
            screen.blit(CHARACTERS[P1][3][3][facing[0]][int(cuentaPasos[0] // 2.5 % len(CHARACTERS[P1][3][3][facing[0]]))],
                        (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][3][facing[0]][
                int(cuentaPasos[0] // 2.5 % len(CHARACTERS[P1][3][3][facing[0]]))].get_rect()
        elif punyo[0]:
            screen.blit(CHARACTERS[P1][3][4][facing[0]][int(cuentaPasos[0] // 2.5 % len(CHARACTERS[P1][3][4][facing[0]]))],
                        (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][4][facing[0]][
                int(cuentaPasos[0] // 2.5 % len(CHARACTERS[P1][3][4][facing[0]]))].get_rect()
        elif agacharse[0]:
            screen.blit(CHARACTERS[P1][3][5][facing[0]][int(cuentaPasos[0] // 6 % len(CHARACTERS[P2][3][5][facing[0]]))],
                        (int(px[0]), int(py[0] + 100)))
            rects[0] = CHARACTERS[P2][3][5][facing[0]][
                int(cuentaPasos[0] // 6 % len(CHARACTERS[P2][3][5][facing[0]]))].get_rect()
        else:
            screen.blit(CHARACTERS[P1][3][0][facing[0]], (int(px[0]), int(py[0])))
            rects[0] = CHARACTERS[P1][3][0][facing[0]].get_rect()
            cuentaPasos[1] -= 1 / 60
        cuentaPasos[1] = (cuentaPasos[1] + 1) % (60 * 2)
    if not win[0] and not win[1]:
        if izquierda[1]:
            screen.blit(CHARACTERS[P2][3][1][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][1][facing[1]]))],
                        (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][1][facing[1]][
                int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][1][facing[1]]))].get_rect()
            # Movimiento a la derecha
        elif derecha[1]:
            screen.blit(CHARACTERS[P2][3][1][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][1][facing[1]]))],
                        (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][1][facing[1]][
                int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][1][facing[1]]))].get_rect()
        elif salto[1]:
            screen.blit(CHARACTERS[P2][3][2][facing[1]][int(cuentaPasos[1] // 6 % len(CHARACTERS[P2][3][2][facing[1]]))],
                        (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][2][facing[1]][
                int(cuentaPasos[1] // 6 % len(CHARACTERS[P2][3][2][facing[1]]))].get_rect()
        elif patada[1]:
            screen.blit(CHARACTERS[P2][3][3][facing[1]][int(cuentaPasos[1] // 2.5 % len(CHARACTERS[P2][3][3][facing[1]]))],
                        (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][3][facing[1]][
                int(cuentaPasos[1] // 2.5 % len(CHARACTERS[P2][3][3][facing[1]]))].get_rect()
        elif punyo[1]:
            screen.blit(CHARACTERS[P2][3][4][facing[1]][int(cuentaPasos[1] // 2.5 % len(CHARACTERS[P2][3][4][facing[1]]))],
                        (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][4][facing[1]][
                int(cuentaPasos[1] // 2.5 % len(CHARACTERS[P2][3][4][facing[1]]))].get_rect()
        elif agacharse[1]:
            screen.blit(CHARACTERS[P2][3][5][facing[1]][int(cuentaPasos[1] // 6 % len(CHARACTERS[P2][3][5][facing[1]]))],
                        (int(px[1]), int(py[1] + CHARACTERS[P1][3][0][facing[0]].get_rect()[3] - CHARACTERS[P2][3][5][facing[1]][int(cuentaPasos[1] // 6 % len(CHARACTERS[P2][3][5][facing[1]]))].get_rect()[3])))
            rects[1] = CHARACTERS[P2][3][5][facing[1]][
                int(cuentaPasos[1] // 6 % len(CHARACTERS[P2][3][5][facing[1]]))].get_rect()
        else:
            screen.blit(CHARACTERS[P2][3][0][facing[1]], (int(px[1]), int(py[1])))
            rects[1] = CHARACTERS[P2][3][0][facing[1]].get_rect()
            cuentaPasos[1] -= 1 / FPS
    if win[0]:
        screen.blit(CHARACTERS[P1][3][7][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][7][facing[0]]))],(int(px[0]), int(py[0])))
        screen.blit(CHARACTERS[P2][3][6][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P2][3][6][facing[0]]))],(int(px[1]), int(py[1])))
        CONTROL["efects"].play(EFECTS["win"])
    elif win[1]:
        screen.blit(CHARACTERS[P2][3][7][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][7][facing[1]]))],(int(px[1]), int(py[1])))
        screen.blit(CHARACTERS[P1][3][6][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P1][3][6][facing[1]]))],(int(px[0]), int(py[0])))
        CONTROL["efects"].play(EFECTS["win"])
    elif time == 0:
        if randint(0,1):
            screen.blit(CHARACTERS[P1][3][7][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][7][facing[0]]))],
                        (int(px[0]), int(py[0])))
            screen.blit(CHARACTERS[P2][3][7][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][7][facing[1]]))],
                        (int(px[1]), int(py[1])))
        else:
            screen.blit(CHARACTERS[P1][3][7][facing[0]][int(cuentaPasos[0] // 2 % len(CHARACTERS[P1][3][7][facing[0]]))],
                (int(px[0]), int(py[0])))
            screen.blit(CHARACTERS[P2][3][7][facing[1]][int(cuentaPasos[1] // 2 % len(CHARACTERS[P2][3][7][facing[1]]))],
                (int(px[1]), int(py[1])))
    rects[0][0] += (int(px[0]))
    rects[0][1] += (int(py[0]))
    rects[1][0] += (int(px[1]))
    rects[1][1] += (int(py[1]))
    g_f = [[rects[0][2]-10, 0],[rects[1][2]-10, 0]]
    if not win[0] and not win[1]:
        if rects[1].collidepoint(int(px[0] + g_f[facing[0]][facing[0]]), int(py[0] + 40)):
            if cuentapatada[0] != 10:
                if len(str(pospatada[0])) == 0:
                    pospatada[0] = cuentapatada[0]
                if pospatada[0] == cuentapatada[0]:
                    heal[1] -= kick[0]
                    CONTROL["efects"].play(EFECTS["kick"])
                    if facing[0] == 0:
                        px[1] += 80
                    else:
                        px[1] -= 80
            else:
                pospatada[0] = ""
            if cuentapunyo[0] != 10:
                if len(str(pospunyo[0])) == 0:
                    pospunyo[0] = cuentapunyo[0]
                if pospunyo[0] == cuentapunyo[0]:
                    heal[1] -= kick[0]
                    CONTROL["efects"].play(EFECTS["punch"])
                    if facing[0] == 0:
                        px[1] += 40
                    else:
                        px[1] -= 40
            else:
                pospunyo[1] = ""
        if rects[0].collidepoint(int(px[1] + g_f[facing[1]][facing[1]]), int(py[1] + 40)):
            if cuentapatada[1] != 10:
                if len(str(pospatada[1])) == 0:
                    pospatada[1] = cuentapatada[1]
                if pospatada[1] == cuentapatada[1]:
                    heal[0] -= kick[1]
                    CONTROL["efects"].play(EFECTS["kick"])
                    if facing[1] == 0:
                        px[0] += 80
                    else:
                        px[0] -= 80
            else:
                pospatada[1] = ""
            if cuentapunyo[1] != 10:
                if len(str(pospunyo[1])) == 0:
                    pospunyo[1] = cuentapunyo[1]
                if pospunyo[1] == cuentapunyo[1]:
                    heal[0] -= kick[1]
                    CONTROL["efects"].play(EFECTS["punch"])
                    if facing[1] == 0:
                        px[0] += 40
                    else:
                        px[0] -= 40
            else:
                pospunyo[0] = ""

if __name__ == '__main__':
    main()