import sys
from calcule import *


def solution_z(x):
    s = x[1]/(2*x[2])
    print(int(round(s, 4)))


def solution_p(x, des):
    r = square_root(des)
    s1 = (-x[1] - r) / (2 * x[2])
    s2 = (-x[1] + r) / (2 * x[2])
    print(round(s1, 6))
    print(round(s2, 6))


def solution_n(x, des):
    r = square_root(abs(des))
    a = -x[1]
    b = x[2]
    print("({} - i {}) / (2 * {})".format(a, r, b))
    print("({} + i {}) / (2 * {})".format(a, r, b))

def resolution(x):
    des = descriminant(x)
    if des > 0:
        print("Discriminant is strictly positive({}), the two solutions are:".format(round((des),2)))
        solution_p(x, des)
    elif des == 0:
        print ("Discriminant is null The only solution is:")
        solution_z(x)
    else:
        print("Discriminant is negatif ({})".format(round((des), 2)))
        solution_n(x, des)


def degree(x):
    deg = max(x, key=int)
    print("Polynomial degree: {}".format(deg))
    return deg


def ft_print_reduc(x):
    i = 0
    print("Reduced form: ", end="")
    for cle, val in x.items():

        if val < 0:
            if round(val) != val:
                print("- {} * X^{} ".format(abs(val), cle), end="")
            else:
                print("- {} * X^{} ".format(int(abs(val)), cle), end="")
        elif val >= 0 and i != 0:
            if round(val) != val: 
                print("+ {} * X^{} ".format(abs(val), cle), end="")
            else:
                print("+ {} * X^{} ".format(int(abs(val)), cle), end="")
        else:
            if round(val) != val:
                print("{} * X^{} ".format(abs(val), cle), end="")
            else:
                print("{} * X^{} ".format(int(abs(val)), cle), end="")
        i += 1
    print("= 0")


def ft_reduct(x1, x2):
    for c1, c2, v1, v2 in zip(x1.items(), x2.items()):
        print(c1)

    for cle, valeur in x2.items():
        x2[cle] *= -1
    for c1, v1 in x1.items():
        for c2, v2 in x2.items():
            if c1 == c2:
                x1[c1] = round(x1[c1] + x2[c2], 3)
            else:
                x1[c2] = v2
    for i in x1.keys():
        if i < 0:
            print(x1.keys())
            print("pas possible de resoudre ca !!")
        elif i > 2:
            print("plus que 3")
    if all(x1.values()):
        return x1
    else:
        print(x1)
        print("tout les nombres reel sont solution")
        exit()


def ft_split(x):
    elem = x.split()
    x_co = [float(elem[i]) if elem[i-1] != "-" else float(elem[i])*(-1) for i in range(0, len(elem), 4)]
    print(elem)
    for i in range(2,len(elem),4):
        if "." in elem[i] or "-" in elem[i]:
            print("one of your coef is not Integer please fix it and retry")
            exit(0)
    x_p = [int(elem[i][2:]) for i in range(2, len(elem), 4)]
    f = 0
    dict = {}
    while f < len(x_p):
        g = f + 1
        while g < len(x_p):
            if x_p[f] == x_p[g]:
                x_co[g] += x_co[f]
                x_co.pop(f)
                x_p.pop(g)
            else:
                g += 1
        f += 1
    for i, j in zip(x_p, x_co):
        dict[i] = j
    return dict

def parss(form):
    x = form.split("=")
    # x[0] la partie de droite de l'equation x[1] celle de gauche
    #print()
    xg = ft_split(x[0])
    xd = ft_split(x[1])
    xr = xg
    len_g = len(xg) if len(xg) > len(xd) else len(xd)
    #print(len_g)
    if xd == xg:
        print("tout les nombre reel sont solution")
        exit(0)
    for i in range(len_g):
        if xd.get(i):
            if xg.get(i):
                xr[i] = xg.get(i) - xd.get(i)
            else:
                xr[i] = -xd.get(i)
        elif xg.get(i):
            xr[i] = xg.get(i)
    #x_red = ft_reduct(xg, xd)
    ft_print_reduc(xr)
    for i in xr:
        if type(i) is not int:
            print("Error coeficient must be Integer")
            exit(0)
    d = degree(xr)
    if d == 0:
        eq_zero_degree(xg, xd, xr)
    elif d == 1:
        eq_first_deg(xr)
    elif d > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    else:
        resolution(xr)




def start():
    if len(sys.argv) == 2:
        str_eq = sys.argv[1]
        size = len(str_eq.split("="))
        if size == 2:
            parss(str_eq)
        elif size == 1:
            print("Warning, no '=' in the expression!! \nY/y to continue other to stop by adding ' = 0' ?")
            if  input().upper() == "Y":
                str_eq  += " = 0"
                run(str_eq)
            else:
                print("thank you and good bye")
                exit(0)
        else:
            print("Error, multiple '=' found retry\n")
            exit(0)
    else:
        print("Wrong format: Usage Python3 '[aX2 + bX + c = 0]' ")


if __name__ == '__main__':
    start()
