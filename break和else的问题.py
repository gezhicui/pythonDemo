for num in [1, 2, 3]:

    print(num)

    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执行
    print("会执行吗？")

print("循环结束")


#  ----------------  -实例-  ------------------------
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

find_name = "阿土"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print("找到了")

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:
    print("没有找到")

print("循环结束")