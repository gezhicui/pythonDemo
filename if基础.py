# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 引入随机数
import random
player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))

# 电脑 在三个出拳中随机
computer = random.randint(1, 3)

# 比较胜负
# 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
# 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
if ((player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):
    print("噢耶！！！电脑弱爆了！！！ 你出的是%d  电脑出的是%d" % (player, computer))
elif player == computer:
    print("心有灵犀，再来一盘！ 你出的是%d  电脑出的是%d" % (player, computer))
else:
    print("不行，我要和你决战到天亮！ 你出的是%d  电脑出的是%d" % (player, computer))