def near(x, y, xs, ys, minx, miny):
    nears = list(range(x - minx, x + minx))
    for i in nears:
        if i in xs:
            return True

    nears = list(range(y - miny, y + miny))
    for i in nears:
        if i in ys:
            return True

    return False

xs = [5]
ys = [5]

print(near(2, 546, xs, ys, 5, 5))

