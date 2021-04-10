n = int(input("Вычислить значение полинома Лежандра порядка n = "))
x = float(input("в точке x = "))


def lg(arg_n, arg_x):
    if arg_n == 0:
        return [1, 0]
    if arg_n == 1:
        return [arg_x, 1]
    pn = lg(arg_n - 1, arg_x)
    pn_1 = pn[0]
    pn_2 = pn[1]
    pn = (2 * arg_n - 1) * pn_1
    pn -= (arg_n - 1) * pn_2
    pn /= arg_n
    return [pn, pn_1]


print("Значение полинома Лежандра порядка ", n, " в точке ", x, " = %.5f" % (lg(n, x)[0]))
