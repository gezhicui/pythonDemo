import pygame
from plane_sprites import *
pygame.init()


# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1加载图像数据
bg = pygame.image.load("./images/background.png")
# 2blit绘制图像
screen.blit(bg, (0, 0))


# 绘制飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))
# 定义rect记录飞机初始位置
heroRect =pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy2)


# 游戏循环——游戏正式开始
# 创建时钟对象
clock = pygame.time.Clock()

while True:
    # 指定代码执行频率
    clock.tick(60)
    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出！")
            pygame.quit()
            exit()

    # 修改飞机位置
    heroRect.y -= 2
    # 判断飞机的y值是否小于0
    if heroRect.y <= -126:
        heroRect.y = 700
    # 调用bilt方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, heroRect)

    # 让精灵组调用两个方法
    # update —— 让组中的所有精灵更新
    enemy_group.update()
    # draw
    enemy_group.draw(screen)

    # 更新显示
    pygame.display.update()
pygame.quit()