import pygame
from PIL import Image
pygame.init()

window = pygame.display.set_mode((560, 560))
clock = pygame.time.Clock()
pygame.display.set_caption("PAINT")


def create(win):
    win.fill((255, 255, 255))


def draw(win):
    pygame.draw.rect(win, (0, 0, 0), (pos[0]-20, pos[1]-20, 40, 40))
    pygame.display.update()


def save(k, c):
    if k[pygame.K_RETURN]:
        if c % 2 == 0:
            pygame.image.save(window, "Model/pintura.png")
            print("\n>>> IMAGEM SALVA")

            img = Image.open("Model/pintura.png")
            img = img.resize((28, 28), Image.ANTIALIAS)
            img = img.convert("L")
            img.save("Model/pintura.png")
            print("\n>>> IMAGEM REDIMENSIONADA")

        return True


def main(cou):
    global pos
    run, pos = True, (-50, -50,)
    create(window)

    while run:
        clock.tick(90)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos = pygame.mouse.get_pos()

        if save(keys, cou):
            run = False

        draw(window)
