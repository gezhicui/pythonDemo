import pygame
hero = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 %d %d" % (hero.x, hero.y))
print("英雄的尺寸 %d %d" % (hero.width, hero.height))
print("%d %d" % (hero.size))