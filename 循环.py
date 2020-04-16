# 封装为函数
def chenfabiao(i):
    col = 1
    while col <= i:
        row = 1
        while row <= col:
            print(" %d*%d=%d" % (row, col, col*row),end="\t")
            row +=1
        print("\n")
        col += 1


chenfabiao(7)