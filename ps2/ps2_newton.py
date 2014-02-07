# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    power = 0
    total = 0

    for coefficient in poly:
        total += coefficient * x**power
        power += 1

    return total

def test_evaluate_poly():
    x = -13
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    y = evaluate_poly(poly,x)

    if (y - 180339.9) < 0.1:
        return True
    else:
        return False

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    power = 0
    deriv_poly = []

    for coefficient in poly:
        deriv_poly.append(coefficient * power)
        power += 1

    deriv_poly.pop(0)
    return tuple(deriv_poly)

def test_compute_deriv():
    poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
    deriv_poly =  compute_deriv(poly)

    if deriv_poly == (0.0, 35.0, 9.0, 4.0):
        return True
    else:
        return False


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    deriv_poly = compute_deriv(poly)
    y_0 = evaluate_poly(poly,x_0)

    counter = 1

    while abs(y_0) > epsilon:

        y_prime_0 = evaluate_poly(deriv_poly,x_0)

        if y_prime_0 < 1E-15:
            print 'Error: derivative at', x_0, 'is 0'
            return None

        x = x_0 - y_0/y_prime_0
        y = evaluate_poly(poly, x)

        x_0, y_0 = x, y
        counter += 1

    return (x_0, counter)

def test_compute_root():
    poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
    x_0 = 0.1
    epsilon = .0001

    test = list(compute_root(poly, x_0, epsilon))

    if (test[0] - 0.80679075379635201) < 1e-15 and test[1] == 8:
        return True
    else:
        return False


# Test functions
print 'evaluate_poly', test_evaluate_poly()
print 'compute_deriv', test_compute_deriv()
print 'compute_root', test_compute_root()
