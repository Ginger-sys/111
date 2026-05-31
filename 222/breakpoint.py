# 断点演示代码
def add_num(x, y):
    res = x + y
    #breakpoint()  # 此处打断点暂停
    return res

a = 5
b = 8
result = add_num(a, b)
print(f"计算结果：{result}")

