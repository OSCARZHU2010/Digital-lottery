# -----------2021/6/15----------
# -----------v3.0 beta----------
# -power by Oscar Zhu & Andy Li-
import pygame,sys,random,time
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("青博会抽奖-by Andy Li & Oscar Zhu")
Img1 = pygame.image.load("img.png")
Img2 = pygame.image.load("1.png")
Img3 = pygame.image.load("2.png")
Img4 = pygame.image.load("3.png")
Img5 = pygame.image.load("4.png")
Img6 = pygame.image.load("5.png")
Img7 = pygame.image.load("6.png")
Img8 = pygame.image.load("7.png")
Img9 = pygame.image.load("8.png")
Img10 = pygame.image.load("9.png")
Img11 = pygame.image.load("0.png")
bgSound = pygame.mixer.music.load("BGM.mp3")
pygame.mixer.music.play(-1) 
bool=0
def drawRect(x, y, n): # 参数为中心 x,中心 y,圈数
    for i in range(n):
        myRect = pygame.Rect(100, 100, 50 + i * 30, 50 + i *30)
        myRect.center = (x, y)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255) 
        w = random.randint(1, 20)
        pygame.draw.rect(screen, (r, g, b), myRect, w)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for i in range(10000):
            if bool == 1:
                break
            screen.fill((0, 0, 0))
            drawRect(400, 300, 20)
            pygame.display.update()
        bool=1
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            for i in range(1500):
                a=random.randint(0,9)
                screen.fill((230, 230, 250))
                screen.blit(Img1, (0, 0))
                if a == 0:
                    screen.blit(Img11, (250, 50))
                if a == 1:
                    screen.blit(Img2, (250, 50))
                if a == 2:
                    screen.blit(Img3, (250, 50))
                if a == 3:
                    screen.blit(Img4, (250, 50))
                if a == 4:
                    screen.blit(Img5, (250, 50))
                if a == 5:
                    screen.blit(Img6, (250, 50))
                if a == 6:
                    screen.blit(Img7, (250, 50))
                if a == 7:
                    screen.blit(Img8, (250, 50))
                if a == 8:
                    screen.blit(Img9, (250, 50))
                if a == 9:
                    screen.blit(Img10, (250, 50))
                pygame.display.update()
            if a == 0:
                screen.blit(Img11, (250, 50))
            if a == 1:
                screen.blit(Img2, (250, 50))
            if a == 2:
                screen.blit(Img3, (250, 50))
            if a == 3:
                screen.blit(Img4, (250, 50))
            if a == 4:
                screen.blit(Img5, (250, 50))
            if a == 5:
                screen.blit(Img6, (250, 50))
            if a == 6:
                screen.blit(Img7, (250, 50))
            if a == 7:
                screen.blit(Img8, (250, 50))
            if a == 8:
                screen.blit(Img9, (250, 50))
            if a == 9:
                screen.blit(Img10, (250, 50))
            time.sleep(15)
    screen.fill((230,230,250))
    screen.blit(Img1,(0,0))
    pygame.display.update()
