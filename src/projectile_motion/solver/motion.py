import math
from typing import Literal, Optional

from projectile_motion.solver.quadratic import quadratic_solver
from projectile_motion.solver.solution import Solution


def deg_to_rad(angle: float) -> float:
    return angle * math.pi / 180


def calculate_solution(
    v: float,
    unit: Literal["ms", "kmh"],
    h_init: float,
    angle: float,
    g: float,
    dist: Optional[float],
    n_steps: int,
) -> Solution:
    if unit == "kmh":
        v /= 3.6
    vx = v * math.cos(deg_to_rad(angle))
    vy = v * math.sin(deg_to_rad(angle))
    x: list[float] = [0]
    y: list[float] = [h_init]

    if not dist:
        roots = quadratic_solver(a=g / 2, b=vy, c=h_init)
        total_time = max(roots)
    else:
        total_time = dist / vx
    dt = total_time / n_steps

    curr_time = dt
    while curr_time <= total_time + dt / 100:
        next_x = x[0] + vx * curr_time
        x.append(next_x)
        next_y = y[0] + vy * curr_time + 0.5 * g * curr_time**2
        y.append(next_y)
        curr_time += dt

    return Solution(X=x, Y=y, max_h=max(y), max_dist=max(x), total_time=total_time)
