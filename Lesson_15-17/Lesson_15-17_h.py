import pygame
import os

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
WINNER_BETU = pygame.font.SysFont("arial", 100)

FPS = 60
SEB = 5
LEZER_SEB = 7
MAX_LOVEDEK = 3
URHAJO_SZELESSEG = 80
URHAJO_MAGASSAG = 60

SARGA_TALALAT = pygame.USEREVENT + 1
PIROS_TALALAT = pygame.USEREVENT + 2

SARGA_KEP = pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'spaceship_yellow.png'))
SARGA_URHAJO = pygame.transform.rotate(
    pygame.transform.scale(SARGA_KEP, (URHAJO_SZELESSEG, URHAJO_MAGASSAG)), 270)

PIROS_KEP = pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'spaceship_red.png'))
PIROS_URHAJO = pygame.transform.rotate(
    pygame.transform.scale(PIROS_KEP, (URHAJO_SZELESSEG, URHAJO_MAGASSAG)), 90)

HATTER = pygame.transform.scale(pygame.image.load(os.path.join('Lesson_15-17', 'assets', 'space.png')), (SZELESSEG, MAGASSAG))

def ablak_rajzol(piros, sarga):
    ABLAK.fill(FEHER)
    ABLAK.blit(SARGA_URHAJO, (sarga.x, sarga.y))
    ABLAK.blit(PIROS_URHAJO, (piros.x, piros.y))
    pygame.display.update()

def sarga_mozgat(gombok_lenyomva, sarga):
    if gombok_lenyomva[pygame.K_a]: #bal
        sarga.x -= SEB
    if gombok_lenyomva[pygame.K_d]: #jobb
        sarga.x += SEB
    if gombok_lenyomva[pygame.K_w]: #fel
        sarga.y -= SEB
    if gombok_lenyomva[pygame.K_s]: #le
        sarga.y += SEB

def piros_mozgat(gombok_lenyomva, piros):
    if gombok_lenyomva[pygame.K_LEFT]: #bal
        piros.x -= SEB
    if gombok_lenyomva[pygame.K_RIGHT]: #jobb
        piros.x += SEB
    if gombok_lenyomva[pygame.K_UP]: #fel
        piros.y -= SEB
    if gombok_lenyomva[pygame.K_DOWN]: #le
        piros.y += SEB

def main():
    piros = pygame.Rect(700, 300, URHAJO_SZELESSEG, URHAJO_MAGASSAG)
    sarga = pygame.Rect(100, 300, URHAJO_SZELESSEG, URHAJO_MAGASSAG)

    ora = pygame.time.Clock()
    game = True
    while game:
        ora.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        gombok_lenyomva = pygame.key.get_pressed()
        sarga_mozgat(gombok_lenyomva, sarga)
        piros_mozgat(gombok_lenyomva, piros)
        ablak_rajzol(piros, sarga)
    pygame.quit()


if __name__ == "__main__":
    main()