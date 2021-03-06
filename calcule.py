def square_root(number: float):
    if not number:
        return 0

    g = number / 2.0
    g2 = g + 1
    while g != g2:
        n = number / g
        g2 = g
        g = (g + n) / 2
    return round(g, 6)


def descriminant(x):
    return (x[1] ** 2) - (4 * x[0] * x[2])


def eq_zero_degree(x, y, z):
    if x == y:
        print("tous les nombre reel sont solutions")
    else:
        print("pas de solution possible")
    exit()

def eq_first_deg(x):
    res = -x[0] / x[1]
    print("The solution is: ", res)