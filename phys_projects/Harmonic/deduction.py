from math import factorial


def double_factorial(n):
    if n == 0 or n == -1:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result


def gaol(n: int):
    return factorial(2*n) / factorial(n) ** 2


def get_t(m: int, n: int):
    """
    T_{m,n}=2T_{0, n-1}+\\sum_{k=1}^{m+1}T_{k,n-1},m\\ge0,n\\ge1,
    T_{m, 1}=2, \\ \\forall m
    """
    if n == 1:
        return 2
    else:
        return 2 * get_t(0, n - 1) + sum([get_t(k, n - 1) for k in range(1, m + 2)])


def main():
    for n in range(1, 20):
        if gaol(n) == get_t(0, n):
            print(f"n={n} is right")
        else:
            print(f"n={n} is wrong: {gaol(n)} != {get_t(0, n)}")
            break


if __name__ == '__main__':
    main()
