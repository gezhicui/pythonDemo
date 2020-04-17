import card_tools


while True:

    card_tools.showMenu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    # 123针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            card_tools.new_card()
        # 显示全部
        elif action_str == "2":
            card_tools.show_all()
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()
    # 0退出系统
    elif action_str == "0":
        print("欢迎下次使用！")
        break
    else:
        print("您输入的不正确，请重新输入")

