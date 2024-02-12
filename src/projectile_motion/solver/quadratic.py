import math


def quadratic_solver(a, b, c):
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
    - a: Coefficient of the quadratic term.
    - b: Coefficient of the linear term.
    - c: Constant term.

    Returns:
    - Tuple containing the roots of the quadratic equation.
    """
    discriminant = math.sqrt(b**2 - 4 * a * c)

    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return root1, root2
