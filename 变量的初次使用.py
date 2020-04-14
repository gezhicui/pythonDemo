price_str = input("苹果的单价：")
weight_str = input("苹果的重量：")

# 将价格转换为小数
price = float(price_str)
# 将重量转换为小数
weight = float(weight_str)

money = price*weight

print(money)

