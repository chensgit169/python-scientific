import sympy as sp

# Define the symbolic variables and parameters
t, w = sp.symbols('t w', real=True)
Tp, w0, c = sp.symbols('Tp w0 c', real=True, positive=True, constant=True)


def fourier_transform(phi_p, phi_n):
    """
    Fourier transform of the frequency-domain electric field of a laser pulse
    into the time domain, given the phase of the positive and negative.
    """
    # Define the frequency-domain field amplitude
    E_w_n = sp.exp(-c * Tp ** 2 * (w - w0) ** 2) * sp.exp(sp.I * phi_n)
    E_w_p = sp.exp(-c * Tp ** 2 * (w + w0) ** 2) * sp.exp(sp.I * phi_p)

    E_w_n = E_w_n.simplify()
    sp.pprint(E_w_n)
    E_w_p = E_w_p.simplify()

    E_w = E_w_p + E_w_n


    E_w = E_w.simplify()
    # Compute the Fourier transform of the time-domain signal
    # E_t = sp.fourier_transform(E_w, w, t/2/sp.pi)
    E_t_p = sp.fourier_transform(E_w_p, w, t/2/sp.pi)
    print("E_t_p:")
    sp.pprint(E_t_p)
    E_t_n = sp.fourier_transform(E_w_n, w, t/2/sp.pi)
    E_t = E_t_p + E_t_n
    return E_t.simplify()


def bandwidth_limit():
    Phi_p = 0
    Phi_n = 0
    E_t = fourier_transform(Phi_p, Phi_n)
    # Print the result of the Fourier transform
    print("Fourier Transform E(t):")
    sp.pprint(sp.factor(E_t))


def envelope_phase():
    Delta_phi = sp.symbols('Delta_phi', real=True, constant=True)

    Phi_p = - Delta_phi * (w+w0)
    Phi_n = - Delta_phi * (w-w0)
    E_t = fourier_transform(Phi_p, Phi_n)
    # Print the result of the Fourier transform
    print("Fourier Transform E(t):")
    sp.pprint(sp.factor(E_t))


def linear_chirp():
    alpha = sp.symbols('alpha', real=True, constant=True)

    Phi_p = - alpha * (w + w0) ** 2
    Phi_n = + alpha * (w - w0) ** 2
    E_t = fourier_transform(Phi_p, Phi_n)
    # Print the result of the Fourier transform
    print("Fourier Transform E(t):")
    sp.pprint(E_t.simplify())
    return E_t


if __name__ == '__main__':
    # bandwidth_limit()
    # envelope_phase()
    linear_chirp()