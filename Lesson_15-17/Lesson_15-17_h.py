import pygame
import os
import random
import math

pygame.font.init()
pygame.mixer.init()

SZELESSEG = 900
MAGASSAG = 500
ABLAK = pygame.display.set_mode((SZELESSEG, MAGASSAG))
pygame.display.set_caption("Űrhajos játék")

FEHER = (255, 255, 255)
FEKETE = (0, 0, 0)
PIROS = (255, 0, 0)
SARGA = (255, 255, 0)

ELVALASZTO = pygame.Rect(SZELESSEG // 2 - 5, 0, 10, MAGASSAG)

ROBBANAS_HANG = pygame.mixer.Sound(os.path.join('Lesson_15-17', 'assets', 'explosion.wav'))
LEZER_HANG = pygame.mixer.Sound(os.path.join("Lesson_15-17", 'assets', 'laser.wav'))

ELET_BETU = pygame.font.SysFont("arial", 40)
WINNER_BETU = pygame.font.SysFont("arial", 90)

FPS = 60
SEB = 5
LEZER_SEB = 7
MAX_LOVEDEK = 3
URHAJO_SZELESSEG = 80
URHAJO_MAGASSAG = 60
METEOR_SZELESSEG = 50
METEOR_MAGASSAG = 50
METEOR_SEB = 2

METEOR_1_IRANY = random.randint(0, 359)
METEOR_2_IRANY = random.randint(0, 359)
METEOR_3_IRANY = random.randint(0, 359)

METEOR_1_X_SEB = math.cos(METEOR_1_IRANY) * METEOR_SEB
METEOR_1_Y_SEB = math.sin(METEOR_1_IRANY) * METEOR_SEB
METEOR_2_X_SEB = math.cos(METEOR_2_IRANY) * METEOR_SEB
METEOR_2_Y_SEB = math.sin(METEOR_2_IRANY) * METEOR_SEB
METEOR_3_X_SEB = math.cos(METEOR_3_IRANY) * METEOR_SEB
METEOR_3_Y_SEB = math.sin(METEOR_3_IRANY) * METEOR_SEB

SARGA_TALALAT = pygame.USEREVENT + 1
PIROS_TALALAT = pygame.USEREVENT + 2

SARGA_KEP = pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'spaceship_yellow.png'))
SARGA_URHAJO = pygame.transform.rotate(
    pygame.transform.scale(SARGA_KEP, (URHAJO_SZELESSEG, URHAJO_MAGASSAG)), 270)

PIROS_KEP = pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'spaceship_red.png'))
PIROS_URHAJO = pygame.transform.rotate(
    pygame.transform.scale(PIROS_KEP, (URHAJO_SZELESSEG, URHAJO_MAGASSAG)), 90)

HATTER = pygame.transform.scale(pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'space.png')), (SZELESSEG, MAGASSAG))

METEOR_KEP = pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'meteor.png'))
METEOR_1 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_KEP, (METEOR_SZELESSEG, METEOR_MAGASSAG)), 90)
METEOR_2 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_KEP, (METEOR_SZELESSEG, METEOR_MAGASSAG)), 90)
METEOR_3 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_KEP, (METEOR_SZELESSEG, METEOR_MAGASSAG)), 90)

def ablak_rajzol(piros, sarga, piros_lovedekek, sarga_lovedekek, 
                 piros_elet, sarga_elet, meteor_1, meteor_2, meteor_3):
    #ABLAK.fill(FEHER)
    ABLAK.blit(HATTER, (0, 0))
    pygame.draw.rect(ABLAK, FEKETE, ELVALASZTO)
    piros_elet_szoveg = ELET_BETU.render(f"Élet: {piros_elet}", True, FEHER)
    ABLAK.blit(piros_elet_szoveg, (SZELESSEG - piros_elet_szoveg.get_width() - 10, 10))
    
    sarga_elet_szoveg = ELET_BETU.render(f"Élet: {sarga_elet}", True, FEHER)
    ABLAK.blit(sarga_elet_szoveg, (10, 10))
    
    ABLAK.blit(SARGA_URHAJO, (sarga.x, sarga.y))
    ABLAK.blit(PIROS_URHAJO, (piros.x, piros.y))
    ABLAK.blit(METEOR_1, (meteor_1.x, meteor_1.y))
    ABLAK.blit(METEOR_2, (meteor_2.x, meteor_2.y))
    ABLAK.blit(METEOR_3, (meteor_3.x, meteor_3.y))

    for lovedek in piros_lovedekek:
        pygame.draw.rect(ABLAK, PIROS, lovedek)
    for lovedek in sarga_lovedekek:
        pygame.draw.rect(ABLAK, SARGA, lovedek)
    pygame.display.update()

def sarga_mozgat(gombok_lenyomva, sarga):
    if gombok_lenyomva[pygame.K_a] and sarga.x - SEB > -15: #bal
        sarga.x -= SEB
    if gombok_lenyomva[pygame.K_d] and sarga.x + SEB + sarga.width - 35 < ELVALASZTO.x: #jobb
        sarga.x += SEB
    if gombok_lenyomva[pygame.K_w] and sarga.y - SEB > -10: #fel
        sarga.y -= SEB
    if gombok_lenyomva[pygame.K_s] and sarga.y + SEB + sarga.height < MAGASSAG: #le
        sarga.y += SEB

def piros_mozgat(gombok_lenyomva, piros):
    if gombok_lenyomva[pygame.K_LEFT] and piros.x - SEB + 15 > ELVALASZTO.x + ELVALASZTO.width: #bal
        piros.x -= SEB
    if gombok_lenyomva[pygame.K_RIGHT] and piros.x + SEB + piros.width - 35 < SZELESSEG: #jobb
        piros.x += SEB
    if gombok_lenyomva[pygame.K_UP] and piros.y - SEB > -10: #fel
        piros.y -= SEB
    if gombok_lenyomva[pygame.K_DOWN] and piros.y + SEB + piros.height < MAGASSAG: #le
        piros.y += SEB

def lovedek_mozgat(sarga_lovedekek, piros_lovedekek, sarga, piros, 
                   meteor_1, meteor_2, meteor_3):
    for lovedek in sarga_lovedekek:
        lovedek.x += LEZER_SEB
        if piros.colliderect(lovedek):
            pygame.event.post(pygame.event.Event(PIROS_TALALAT))
            sarga_lovedekek.remove(lovedek)
        elif lovedek.x > SZELESSEG: 
            sarga_lovedekek.remove(lovedek)
        elif (meteor_1.colliderect(lovedek) or meteor_2.colliderect(lovedek) 
              or meteor_3.colliderect(lovedek)):
            sarga_lovedekek.remove(lovedek)
    for lovedek in piros_lovedekek:
        lovedek.x -= LEZER_SEB
        if sarga.colliderect(lovedek):
            pygame.event.post(pygame.event.Event(SARGA_TALALAT))
            piros_lovedekek.remove(lovedek)
        elif lovedek.x < 0:
            piros_lovedekek.remove(lovedek)
        elif (meteor_1.colliderect(lovedek) or meteor_2.colliderect(lovedek) 
              or meteor_3.colliderect(lovedek)):
            piros_lovedekek.remove(lovedek)
    if sarga.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(SARGA_TALALAT))
    if sarga.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(SARGA_TALALAT))
    if sarga.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(SARGA_TALALAT))

    if piros.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(PIROS_TALALAT))
    if piros.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(PIROS_TALALAT))
    if piros.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(PIROS_TALALAT))

def meteor_mozgat(meteor_1, meteor_2, meteor_3):
    meteor_1.x += METEOR_1_X_SEB
    meteor_1.y += METEOR_1_Y_SEB 
    meteor_2.x += METEOR_2_X_SEB
    meteor_2.y += METEOR_2_Y_SEB 
    meteor_3.x += METEOR_3_X_SEB
    meteor_3.y += METEOR_3_Y_SEB 

    if meteor_1.x > 999:
        meteor_1.x = 1
    if meteor_1.x < 1:
        meteor_1.x = 999
    if meteor_1.y > 499:
        meteor_1.y = 1
    if meteor_1.y < 1: 
        meteor_1.y = 499

    if meteor_2.x > 999:
        meteor_2.x = 1
    if meteor_2.x < 1:
        meteor_2.x = 999
    if meteor_2.y > 499:
        meteor_2.y = 1
    if meteor_2.y < 1: 
        meteor_2.y = 499

    if meteor_3.x > 999:
        meteor_3.x = 1
    if meteor_3.x < 1:
        meteor_3.x = 999
    if meteor_3.y > 499:
        meteor_3.y = 1
    if meteor_3.y < 1: 
        meteor_3.y = 499

def nyertes_rajzol(nyertes_szoveg):
    szoveg = WINNER_BETU.render(nyertes_szoveg, True, FEHER)
    ABLAK.blit(szoveg, (SZELESSEG / 2 - szoveg.get_width() / 2, 
                        MAGASSAG / 2 - szoveg.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    piros = pygame.Rect(700, 300, URHAJO_SZELESSEG, URHAJO_MAGASSAG)
    sarga = pygame.Rect(100, 300, URHAJO_SZELESSEG, URHAJO_MAGASSAG)

    piros_lovedekek = []
    sarga_lovedekek = []

    piros_elet = 10
    sarga_elet = 10

    meteor_1 = pygame.Rect(480, 240, METEOR_SZELESSEG, METEOR_MAGASSAG)
    meteor_2 = pygame.Rect(480, 240, METEOR_SZELESSEG, METEOR_MAGASSAG)
    meteor_3 = pygame.Rect(480, 240, METEOR_SZELESSEG, METEOR_MAGASSAG)

    ora = pygame.time.Clock()
    game = True
    while game:
        ora.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(sarga_lovedekek) < MAX_LOVEDEK:
                    sarga_lovedekek.append(
                        pygame.Rect(sarga.x + sarga.width, sarga.y + sarga.height // 2, 10, 5))
                    LEZER_HANG.play()
                if event.key == pygame.K_RETURN and len(piros_lovedekek) < MAX_LOVEDEK:
                    piros_lovedekek.append(
                        pygame.Rect(piros.x, piros.y + piros.height // 2, 10, 5))
                    LEZER_HANG.play()
            if event.type == PIROS_TALALAT:
                piros_elet -= 1
                ROBBANAS_HANG.play()
            if event.type == SARGA_TALALAT:
                sarga_elet -= 1
                ROBBANAS_HANG.play()
        nyertes_szoveg = ""
        if piros_elet <= 0:
            nyertes_szoveg = "Nyert a sárga űrhajó!"
        if sarga_elet <= 0:
            nyertes_szoveg = "Nyert a piros űrhajó!"
        if nyertes_szoveg != "":
            nyertes_rajzol(nyertes_szoveg)
            break

        gombok_lenyomva = pygame.key.get_pressed()
        sarga_mozgat(gombok_lenyomva, sarga)
        piros_mozgat(gombok_lenyomva, piros)
        meteor_mozgat(meteor_1, meteor_2, meteor_3)
        lovedek_mozgat(sarga_lovedekek, piros_lovedekek, 
                       sarga, piros, meteor_1, meteor_2, meteor_3)
        ablak_rajzol(piros, sarga, piros_lovedekek, sarga_lovedekek, 
                     piros_elet, sarga_elet, meteor_1, meteor_2, meteor_3)
    pygame.quit()


if __name__ == "__main__":
    main()