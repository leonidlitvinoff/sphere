import pygame


n = int(input())
pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
otstup = 0
for i in range(n):
    pygame.draw.ellipse(screen, (255, 255, 255), (0, otstup // 2, 300, 300 - otstup), 1)
    otstup += 300 // n
otstup = 0
for i in range(n):
    pygame.draw.ellipse(screen, (255, 255, 255), (otstup // 2, 0, 300 - otstup, 300), 1)
    otstup += 300 // n
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()