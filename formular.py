
import matplotlib.pyplot as plt
def main():
    h_v1 = []
    h_v2 = []
    for i in range(1,10):
        m1 = i
        m2 = 5

        old_v1 = 2
        old_v2 = 0

        v1 = ((m1 - m2) / (m1 + m2)) * old_v1 + ((2 * m2) / (m1 + m2) * old_v2)
        v2 = 2 * m1 / (m1 + m2) * old_v1 + ((m2 - m1) / (m2 + m1) * old_v2)
        print(i,v1)
        h_v1.append(v1)
        h_v2.append(v2)

    print()

    a = plt.plot([i for i in range(1,10)], h_v1)
    b = plt.plot([i for i in range(1,10)],h_v2, c="orange")
    plt.legend([a,b],["a","b"])

    plt.show()
def small():
    h = []
    for i in range(1, 10):
        m1 = i
        m2 = i

        calc = ((m1 - m2) / (m1 + m2)) * 2
        print(i, calc)
        h.append(calc)

    print()

    plt.plot([i for i in range(1, 10)], h)
    plt.show()


main()