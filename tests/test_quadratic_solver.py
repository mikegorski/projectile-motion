import pytest
from projectile_motion.solver.quadratic import quadratic_solver


def test_real_roots():
    a = 1
    b = -3
    c = 2
    roots = quadratic_solver(a, b, c)
    assert roots == (2.0, 1.0) or roots == (1.0, 2.0)


def test_equal_roots():
    a = 1
    b = -4
    c = 4
    roots = quadratic_solver(a, b, c)
    assert roots == (2.0, 2.0)


def test_zero_discriminant():
    a = 1
    b = -2
    c = 1
    roots = quadratic_solver(a, b, c)
    assert roots == (1.0, 1.0)


def test_invalid_coefficients():
    a = 0
    b = 2
    c = 1
    with pytest.raises(ZeroDivisionError):
        quadratic_solver(a, b, c)
