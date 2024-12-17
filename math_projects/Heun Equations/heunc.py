import numpy as np

"""
Compute the 1st and 2nd HeunC function using power series expansion around z=0.
HeunC equation is given by:
    z(z-1)y'' + [gamma*(z-1) + delta*z + z(z-1)*epsilon]y' + (alpha*z-q)y = 0

References:
    - Oleg V. Motygin https://arxiv.org/abs/1804.01007, see also https://github.com/motygin/Heun_functions.git
    - Wolfram MathWorld https://reference.wolfram.com/language/ref/HeunC.html
    
TODOs:
extend to non-positive integer gamma
extend to complex values of the parameters and variable
"""

# Global convergence limit
HEUN_KLIMIT = 1000  # Maximum number of terms for series expansion


def heun_c_gen_1st(q, alpha, gamma, delta, epsilon, z):
    """
    Power series computation of the first HeunC when gamma is not a non-positive integer.
    HeunC_1(z=0) = 1, HeunC'_1(z=0) = -q / gamma

    :return: val, dval, err, numb, wrnmsg
    """
    if gamma <= 0 and np.ceil(gamma - 5 * np.finfo(float).eps) + abs(gamma) < 5 * np.finfo(float).eps:
        return np.nan, np.nan, np.nan, np.nan, "gamma is a non-positive integer"

    if z == 0:
        return 1, -q / gamma, 0, 1, ""

    def recurrence(k, ckm1, ckm2):
        """
        Recurrence relation for to compute the k-th order term.

        c_k = (c_{k-1} * q_k(z) + c_{k-2} * r_k(z)) / p_k

        """
        pk = k * (k + gamma - 1)
        qk_z = z * (-q + (k - 1) * (gamma - epsilon + delta + k - 2))
        rk_z = z ** 2 * ((k - 2) * epsilon + alpha)
        return (ckm1 * qk_z + ckm2 * rk_z) / pk

    # initial terms
    ckm2 = 1
    ckm1 = -z * q / gamma

    # values, first derivative, and second derivative
    val = ckm1 + ckm2
    dval = -q / gamma
    ddval = 0

    for k in range(2, HEUN_KLIMIT):
        ck = recurrence(k, ckm1, ckm2)
        val += ck
        dval += k * ck / z
        ddval += k * (k - 1) * ck / z ** 2
        ckm2 = ckm1
        ckm1 = ck
        if abs(ck) < np.finfo(np.float64).eps:
            numb = k
            break
    else:
        numb = HEUN_KLIMIT

    if np.isinf(val) or np.isnan(val):
        return np.nan, np.nan, np.nan, np.nan, "Failed convergence of recurrence and summation"

    if q - alpha * z != 0:
        val2 = (z * (z - 1) * ddval + (gamma * (z - 1) + delta * z + epsilon * z * (z - 1)) * dval) / (q - alpha * z)
        err = abs(val - val2)
    else:
        # TODO: use another estimation for err
        err = np.inf

    return val, dval, err, numb, ""


def heun_c_gen_2nd(q, alpha, gamma, delta, epsilon, z):
    """
    Power series computation of the second HeunC when gamma is not a non-positive integer.

    HeunC_2 = z^(1 - gamma) * HeunC_1[
        q + (gamma - 1) * (epsilon + delta), alpha + epsilon * (1 - gamma), 2 - gamma, delta, epsilon
    ](z)

    :return:
    """
    q2 = q + (gamma - 1) * (epsilon + delta)
    alpha2 = alpha + epsilon * (1 - gamma)
    gamma2 = 2 - gamma

    val, dval, err, numb, wrnmsg = heun_c_gen_1st(q2, alpha2, gamma2, delta, epsilon, z)
    val *= z ** (1 - gamma)
    dval = (1 - gamma) * z ** (-gamma) * val + z ** (1 - gamma) * dval
    err = abs(z ** (1 - gamma)) * err

    return val, dval, err, numb, wrnmsg


def test_1():
    q = 1 / 4
    alpha = 0
    gamma = 1 / 2
    delta = 1 / 2
    epsilon = 0

    for z in np.arange(0.01, 0.9, 0.01):
        val, dval, err, numb, wrnmsg = heun_c_gen_1st(q, alpha, gamma, delta, epsilon, z)

        err_expected = abs((1 - z) ** (1 / 2) - val)
        assert err_expected < 1e-13

        # For the 2nd HeunC, essentially exact values are expected
        val, dval, err, numb, wrnmsg = heun_c_gen_2nd(q, alpha, gamma, delta, epsilon, z)
        assert abs(z ** (1 / 2) - val) == 0
        assert numb == 2


def test_2():
    """
    Test the 1st HeunC function for a specific set of parameters given
    :return:
    """
    q = 4
    alpha = -0.6
    gamma = -0.7
    delta = -0.18
    epsilon = 0.3
    z = 0.12

    val, dval, err, numb, wrnmsg = heun_c_gen_1st(q, alpha, gamma, delta, epsilon, z)
    # expected: 1.05543
    print(val, dval, err, numb, wrnmsg)

    zs = np.arange(-0.3, 0.9, 0.01)
    vals = [heun_c_gen_1st(q, alpha, gamma, delta, epsilon, z)[0] for z in zs]
    import matplotlib.pyplot as plt
    plt.plot(zs, vals)
    plt.show()


if __name__ == '__main__':
    test_1()
