# 一个对象的 属性 可以是 另外一个类创建的对象
class Gun:
    def __init__(self, mdoel):
        # 枪的型号
        self.model = mdoel
        # 子弹数量
        self.bulletCount = 0

    def addBullet(self, count):
        self.bulletCount += count

    def shoot(self):
        # 判断子弹数量
        if self.bulletCount <= 0:
            print("没有子弹了gg")
            return
        #发射子弹
        self.bulletCount -= 1
        print("%s 突突突 还剩下%d发子弹"  %(self.model,self.bulletCount))


class Soldier:
    def __init__(self, name):
        # 新兵姓名
        self.name = name
        # 新兵没有枪
        self.gun = None
    def fire(self):
        # 判断士兵有没有枪
        if self.gun == None:
            print("%s还没有枪...gg" % self.name)
            return
        # 装子弹
        print("冲啊啊！！ %s 在装子弹" % self.name)
        self.gun.addBullet(30)
        # 发射
        self.gun.shoot()


ak47=Gun("ak47")

# 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun=ak47
xusanduo.fire()