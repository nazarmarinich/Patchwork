import pygame

pygame.init()

pro_version = "1.0.0"
sc = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Patchwork MNG " + pro_version)
# pygame.display.set_icon(pygame.image.load("pics/patchwork_icon.jpg"))
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
# pygame.draw.rect(sc, WHITE, (20, 20, 100, 200))
pygame.draw.rect(sc, WHITE, (100, 100, 25, 25))
pygame.draw.rect(sc, WHITE, (125, 100, 25, 25))
pygame.draw.rect(sc, WHITE, (125, 125, 25, 25))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Pushed: ", event.button)

    clock.tick(FPS)
