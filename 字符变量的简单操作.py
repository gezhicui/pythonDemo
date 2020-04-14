# 字符串拼接
fitst_name = "张"
last_name = "三"
print(fitst_name+last_name)

# 格式化输出
name = "小明"
print("我的名叫 %s" % name)

# %d表示输出的参数是整数，%06d表示不足6位用0补齐
studentId = 1
print("我的学号：%06d" % studentId)

# %f输出时用.来控制输出位数，%.2f表示输出位数为小数点后面2位
price = float(input("苹果的单价："))
weight = float(input("苹果的重量："))
total = price*weight
print("苹果一斤%.2f元 重量%.2f斤 一共%.2f元" % (price, weight, total))

# 输出的内容带% 用%%表示%
scale = 0.25
print("数据比例是 %.2f%%" % (scale*100))
