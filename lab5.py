# ІА-34. Варіант 25

x = [0, 0, 0, 0, 1, 1, 1, 1, "x"]
y = [0, 0, 1, 1, 0, 0, 1, 1, "y"]
z = [0, 1, 0, 1, 0, 1, 0, 1, "z"]
F = [1, 0, 1, 0, 0, 1, 1, 0]

F1 = [0, 1, 0, 1, 1, 1, 1, 0]


def build_truth_table(F: list):
    print(f"{x[-1]} | {y[-1]} | {z[-1]} || F")
    for i in range(len(F)):
        print(f"{x[i]} | {y[i]} | {z[i]} || {F[i]}")
    print("\n")


def find_dual_function(F: list):
    F_dual = []
    for i in F:
        F_dual.append(int(not i))
    F_dual.reverse()
    return F_dual


# Досконала диз’юнктивна нормальна форма (ДДНФ)
def to_perfect_disjunctive_normal_form(F: list):
    result = "F(x, y, z) = "
    arguments = [x, y, z]
    for i in range(len(F)):
        if F[i]:
            if result != "F(x, y, z) = ":
                result += "∨"

            result += "("
            for j in arguments:
                if j[i]:
                    result += j[-1]
                else:
                    result += "¬" + j[-1]
                if j != z:
                    result += "∧"
            result += ")"
    return result


# Досконала кон’юнктивна нормальна форма (ДКНФ)
def to_perfect_conjunctive_normal_form(F: list):
    result = "F(x, y, z) = "
    arguments = [x, y, z]
    for i in range(len(F)):
        if not F[i]:
            if result != "F(x, y, z) = ":
                result += "∧"

            result += "("
            for j in arguments:
                if not j[i]:
                    result += j[-1]
                else:
                    result += "¬" + j[-1]
                if j != z:
                    result += "∨"
            result += ")"
    return result


# Поліном Жегалкіна
def to_zhegalkin_polynomial(F: list):
    result = "P(x, y, z) = "
    arguments = [x, y, z]
    for i in range(len(F)):
        if F[i]:
            if result != "P(x, y, z) = ":
                result += "⊕ "

            result += "("
            for j in arguments:
                if j[i]:
                    result += j[-1]
                else:
                    result += "(" + j[-1] + "⊕ 1" + ")"
                if j != z:
                    result += "∧"
            result += ")"
    return result


# Чи зберігає константи 1 і 0
def saves_constant_one(F: list):
    if F[-1]:
        return True
    return False


def saves_constant_zero(F: list):
    if F[0]:
        return True
    return False


# Перевірка монотонності
def is_monotonic(F: list):
    arguments = [x, y, z]
    for i in range(len(F)):
        if F[i]:
            if x[i] and y[i] and z[i]:
                continue

            for j in arguments:
                if not j[i]:
                    for k in range(i, len(F)):
                        if j == x:
                            if not (y[i] == y[k]) and not (z[i] == z[k]):
                                continue
                        elif j == y:
                            if not (z[i] == z[k]) and not (x[i] == x[k]):
                                continue
                        elif j == z:
                            if not (y[i] == y[k]) and not (x[i] == x[k]):
                                continue
                        if j[k] and not F[k]:
                            return False
    return True


# Перевірка лінійності
def is_linear(F: list):
    xyz = [x, y, z]
    arguments = {"a": None, "ax": None, "ay": None, "az": None,
                 "axy": None, "ayz": None, "axz": None, "axyz": None}
    formula = 0
    linear_form = ""
    buffer = False
    bool_linear = True
    key = ""

    for i in range(len(F)):
        buffer = False
        for j in xyz:
            if j[i] == 0:
                continue
            if j[i] == 1 and not buffer:
                buffer = []
                buffer.append(j)
            elif j[i] == 1:
                buffer.append(j)
        if not buffer:
            arguments['a'] = F[i]
            # print(keys[i], arguments[keys[i]])
            continue
        if len(buffer) == 1:
            if 1 ^ arguments['a'] == F[i]:
                arguments['a'+buffer[0][-1]] = 1
            else:
                arguments['a'+buffer[0][-1]] = 0
        elif len(buffer) > 1:
            formula = 0
            key = 'a'
            for k in range(len(buffer)):
                if k == 0:
                    formula = arguments[key]
                formula = formula ^ arguments[key+buffer[k][-1]]
            for s in range(len(buffer)-1):
                for v in range(len(buffer)-1-s):
                    key = 'a'
                    for w in range(v, v+s+2):
                        key += buffer[w][-1]
                    if not arguments[key] is None:
                        formula = formula ^ arguments[key]
                    else:
                        if 1 ^ formula == F[i]:
                            arguments[key] = 1
                        else:
                            arguments[key] = 0

    for k, item in arguments.items():
        if k == "a":
            linear_form += str(item)
            continue
        if item:
            linear_form += "⊕ "
            linear_form += k[1:]
            if len(k[1:]) > 1:
                bool_linear = False
    print(arguments)
    return linear_form, bool_linear


if __name__ == "__main__":
    print("Таблиця істинності даної функції.")
    build_truth_table(F)
    print("Таблиця істинності функції, двоїстої до заданої функції.")
    build_truth_table(find_dual_function(F))

    print("Функція, подана в ДДНФ:")
    print(to_perfect_disjunctive_normal_form(F) + "\n")

    print("Функція, подана в ДКНФ:")
    print(to_perfect_conjunctive_normal_form(F) + "\n")

    print("Функція, представлена поліномом Жегалкіна:")
    print(to_zhegalkin_polynomial(F) + "\n")

    if saves_constant_zero(F):
        print("Функція зберігає константу 0" + "\n")
    if saves_constant_one(F):
        print("Функція зберігає константу 1" + "\n")
    if F == find_dual_function(F):
        print("Функція є самодвоїстою." + "\n")
    if is_monotonic(F):
        print("Функція є монотонною." + "\n")

    linear_form, bool_linear = is_linear(F)
    if bool_linear:
        print("Функція є лінійною.\nЇї лінійна форма")
    print("Розкритий поліном Жегалкіна:")
    print(linear_form)
