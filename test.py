# 撒币算法
import random


# 解二元一次方程
def binary_equation(point1, point2):
    w = (point1[1] - point2[1]) / (point1[0] - point2[0])
    b = point1[1] - w * point1[0]
    return w, b


# 四个flag，全true点才在范围内
def single_random_point(x, y, w1, w2, w3, w4, b1, b2, b3, b4):
    flag1 = (y < (w1 * x + b1))
    if w2 is not None:
        if w2 < 0:
            flag2 = (y < (w2 * x + b2))
        else:
            flag2 = (y > (w2 * x + b2))
    else:
        flag2 = (x < b2)
    flag3 = (y > (w3 * x + b3))
    if w4 is not None:
        if w4 < 0:
            flag4 = (y > (w4 * x + b4))
        else:
            flag4 = (y < (w4 * x + b4))
    else:
        flag4 = (x > b4)
    return [flag1, flag2, flag3, flag4]


# 求四边形在大图中所占比重
# 输入样例：四个坐标，[300,300]
def single_area_ratio(s, size_l):
    w1, w2, w3, w4, b1, b2, b3, b4 = for_w_b(s)

    k = 0
    n = 2000000
    for i in range(n):
        x = random.uniform(0, size_l[0])
        y = random.uniform(0, size_l[1])

        flag = single_random_point(x, y, w1, w2, w3, w4, b1, b2, b3, b4)

        if flag[0] and flag[1] and flag[2] and flag[3]:
            k += 1

    return float(k) / float(n)


# 求四边形四个边的一次方程参数
def for_w_b(s):
    if s[0][0] != s[1][0]:
        w1, b1 = binary_equation(s[0], s[1])
    else:
        w1 = None
        b1 = s[0][0]
    if s[1][0] != s[2][0]:
        w2, b2 = binary_equation(s[1], s[2])
    else:
        w2 = None
        b2 = s[1][0]
    if s[2][0] != s[3][0]:
        w3, b3 = binary_equation(s[2], s[3])
    else:
        w3 = None
        b3 = s[2][0]
    if s[3][0] != s[0][0]:
        w4, b4 = binary_equation(s[3], s[0])
    else:
        w4 = None
        b4 = s[0][0]
    return w1, w2, w3, w4, b1, b2, b3, b4


# 求两个四边形相交区域面积
def double_area_ratio(s1, size_l, s2):
    # one shape
    w1, w2, w3, w4, b1, b2, b3, b4 = for_w_b(s1)
    # another one
    w1_1, w1_2, w1_3, w1_4, b1_1, b1_2, b1_3, b1_4 = for_w_b(s2)

    k = 0
    n = 2000000
    for i in range(n):
        x = random.uniform(0, size_l[0])
        y = random.uniform(0, size_l[1])

        flag = single_random_point(x, y, w1, w2, w3, w4, b1, b2, b3, b4)
        flag1 = single_random_point(x, y, w1_1, w1_2, w1_3, w1_4, b1_1, b1_2, b1_3, b1_4)

        if flag[0] and flag[1] and flag[2] and flag[3] \
                and flag1[0] and flag1[1] and flag1[2] and flag1[3]:
            k += 1

    return float(k) / float(n)


shape1 = [[0, 150], [150, 150], [150, 0], [0, 0]]
shape2 = [[50, 200], [200, 200], [200, 50], [50, 50]]

# print(double_area_ratio(shape1, [200, 200], shape2))

# r1 = double_area_ratio(shape1, [200, 200], shape2) / single_area_ratio(shape1, [200, 200])
# r2 = double_area_ratio(shape1, [200, 200], shape2) / single_area_ratio(shape2, [200, 200])
#
# print('两图相交面积与shape1的比：' + str(int(float(r1) * 100)) + '%')
# print('两图相交面积与shape2的比：' + str(int(float(r2) * 100)) + '%')
print(single_area_ratio(shape1, [200, 200]))
print(double_area_ratio(shape1, [200, 200], shape2))
