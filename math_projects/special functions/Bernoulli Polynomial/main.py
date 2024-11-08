from scipy.special import comb
import numpy as np


def reduction_list(n: int):
    """
    Calculate the Bernoulli numbers.
    :param n:
    :return:
    """
    if n == 0:
        return [1.0]
    elif n == 1:
        return [1.0, - 1 / 2]
    else:
        bs = np.array(reduction_list(n - 1))
        # if n % 2 == 1:
        #     b_np1 = 0
        # else:
        #     # reduction
        #     b_np1 = - bs @ comb(n+1, np.arange(n)) / (n+1)
        b_np1 = - bs @ comb(n+1, np.arange(n)) / (n+1)
        if n % 2 == 1:
            assert abs(b_np1) <= 1e-10, f"n={n}, b_np1={b_np1}"
        return np.append(bs, b_np1)


def test_bernoulli_nums():
    """
    Test the function bernoulli_nums.
    :return:
    """
    for n in range(1, 10):
        print(f"B_{n} = {(-1)**(n-1)*reduction_list(2*n)[-1]}")


if __name__ == '__main__':
    test_bernoulli_nums()
