List = ["张三", "李四", "王五"]
print(List.index("李四"))

# 修改
List[1] = "帅哥"

# 增加
# 1 追加数据
List.append("王小二")
# 2 在指定索引位置插入数据
List.insert(1, "小妹咩")
# 3 把另一个列表追加到当前列表末尾
newList = ["哈哈", "喝喝", "嘻嘻"]
List.extend(newList)
# 4删除
List.remove("帅哥")
# pop 默认把列表最后一项删除
List.pop()
# pop方法可以指定要删除的元素的索引
List.pop(2)
# 清空列表
# List.clear()
# 列表长度
i = len(List)
# 迭代遍历
for name in List:
    print(name)


print(List)
print(i)
