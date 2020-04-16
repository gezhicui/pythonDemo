info = ("张三", 18, 190, 190)
# 取值和取索引
print(info[0])
print(info.index("张三"))

# 统计计数
print(info.count(190))
# 统计元组中包含的元素的个数
print(len(info))

#  使用 list 函数可以把元组转换成列表
# list(元组)
#  使用 tuple 函数可以把列表转换成元组
#  newlist=tuple(列表)