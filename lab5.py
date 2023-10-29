# ІА-34. Варіант 25

x = [0, 0, 0, 0, 1, 1, 1, 1, "x"]
y = [0, 0, 1, 1, 0, 0, 1, 1, "y"]
z = [0, 1, 0, 1, 0, 1, 0, 1, "z"]
F = [1, 0, 1, 0, 0, 1, 1, 0]


def build_truth_table(x: list, y: list, z: list, F: list):
    print("x | y | z || F")
    for i in range(len(F)):
        print(f"{x[i]} | {y[i]} | {z[i]} || {F[i]}")
    print("\n")


def find_dual_function(F: list):
    F_dual = []
    for i in F:
        F_dual.append(int(not i))
    F_dual.reverse()
    return F_dual


# Досконала диз’юнктивна нормальна форма
def to_perfect_disjunctive_normal_form(x: list, y: list, z: list, F: list):
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


# Досконала кон’юнктивна нормальна форма
def to_perfect_conjunctive_normal_form(x: list, y: list, z: list, F: list):
    result = "F(x, y, z) = "
    arguments = [x, y, z]
    for i in range(len(F)):
        if F[i]:
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


if __name__ == "__main__":
    print("Таблиця істинності даної функції.")
    build_truth_table(x, y, z, F)
    print("Таблиця істинності функції, двоїстої до заданої функції.")
    build_truth_table(x, y, z, find_dual_function(F))

    print("Функція, подана в ДДНФ:")
    print(to_perfect_disjunctive_normal_form(x, y, z, F)+"\n")

    print("Функція, подана в ДКНФ:")
    print(to_perfect_conjunctive_normal_form(x, y, z, F))
