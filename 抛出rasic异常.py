def inputPassword():
    pwd = input("请输入密码！：")
    if len(pwd) >= 8:
        return pwd

    print("抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够！")
    # 主动抛出异常,raise相当于自定义异常信息
    raise ex

try:
    print(inputPassword())
except Exception as result:
    print(result)