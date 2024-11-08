import numpy as np


def hermitian_eigen(H):
    # Check if the input is a 2x2 matrix
    if H.shape != (2, 2):
        raise ValueError("Input matrix must be 2x2.")

    # Check if the matrix is Hermitian (equal to its conjugate transpose)
    if not np.allclose(H, H.conj().T):
        raise ValueError("Input matrix must be Hermitian.")

    # Extract matrix elements (a, b are real, c and d define the complex part)
    a = H[0, 0].real
    b = H[1, 1].real
    c = H[0, 1].real
    d = H[0, 1].imag

    # Compute eigenvalues using analytical expressions
    trace = a + b
    det = a * b - (c ** 2 + d ** 2)
    term = np.sqrt((a - b) ** 2 / 4 + c ** 2 + d ** 2)

    lambda1 = trace / 2 + term
    lambda2 = trace / 2 - term
    eigenvalues = np.array([lambda1, lambda2])

    # Compute eigenvectors for each eigenvalue
    # Special case if c == d == 0, making the matrix diagonal
    if c == 0 and d == 0:
        v1 = np.array([1, 0])  # Eigenvector for lambda1
        v2 = np.array([0, 1])  # Eigenvector for lambda2
    else:
        v1 = np.array([c + 1j * d, lambda1 - a])  # Eigenvector for lambda1
        v2 = np.array([c + 1j * d, lambda2 - a])  # Eigenvector for lambda2

    # Normalize the eigenvectors
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)
    eigenvectors = np.column_stack((v1, v2))

    return eigenvalues, eigenvectors


def test_hermitian_eigen():
    # Test case 1: Diagonal matrix
    H1 = np.array([[1, 0], [0, 2]])
    evals1, evecs1 = hermitian_eigen(H1)
    print("Eigenvalues for test case 1:", evals1)

    # Test case 2: Non-diagonal Hermitian matrix
    H2 = np.array([[1, 1 + 1j], [1 - 1j, 2]])
    evals2, evecs2 = hermitian_eigen(H2)
    print("Eigenvalues for test case 2:", evals2)

    # by np.eigh
    evals, evecs = np.linalg.eigh(H2)
    print("Eigenvalues by np.linalg.eigh:", evals)


if __name__ == '__main__':
    test_hermitian_eigen()