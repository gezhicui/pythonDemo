class Music(object):
    # 记录第一个被创建的对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法为对象分配空间
            cls.instance=super().__new__(cls)
        # 返该对象的引用
        return cls.instance

    def __init__(self):
        # init方法每次创建实例都会被调用
        print("初始化方法")


# 创建多个对象
music1 = Music()
print(music1)
music2 = Music()
print(music2)