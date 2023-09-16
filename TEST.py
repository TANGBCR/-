dian = []
for i in range(0, 20):
    for j in range(0, 21):
        dian.append((i, j))
result = set()


def gys(x, y):  # 求x,y的最大公约数
    if y == 0:
        return x
    return gys(y, x % y)


for i in range(len(dian) - 1):
    x1, y1 = dian[i]
    for j in range(i + 1, len(dian)):
        x2, y2 = dian[j]
        a = y1 - y2
        b = x2 - x1
        c = x1 * y2 - x2 * y1
        k = gys(gys(a, b), c)
        result.add((a / k, b / k, c / k))

print(len(result))