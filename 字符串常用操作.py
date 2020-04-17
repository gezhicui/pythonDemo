str1 = "hello python"
str2 = '我的外号是"大西瓜"'

print(str2)
print(str1[6])
# 循环遍历
for char in str2:

    print(char)


# --------------字符串统计操作
hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一个小（子）字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 3. 某一个子字符串出现的位置
print(hello_str.index("llo"))

