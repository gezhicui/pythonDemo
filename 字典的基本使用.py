xiaoming_dict = {"name": "小明",
                 "age": 18}
print(xiaoming_dict["name"])

# 增加(如果key存在则覆盖)
xiaoming_dict["height"] = 189
print(xiaoming_dict)

# 删除
xiaoming_dict.pop("name")
print(xiaoming_dict)

# 统计键值对数量
print(len(xiaoming_dict))

# 合并字典 (如果key存在则覆盖)
xiaohong = {"name": "小红",
            "sex": "女"}
xiaoming_dict.update(xiaohong)
print(xiaoming_dict)

# 清空字典
xiaoming_dict.clear()
print("------")
print(xiaoming_dict)

# 遍历字典
xiaogang = {"name": "小刚",
            "qq": "123456",
            "phone": "1232412"}
# item是每一次循环中，获取到的键值对的key
for item in xiaogang:
    print("%s - %s" %(item, xiaogang[item]))