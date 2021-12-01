def series():
    x = 0
    y = 1
    print(0)
    for i in range(0, 7):
        z = x + y
        print(z)
        x = y
        y = z


def main():
    series()

main()