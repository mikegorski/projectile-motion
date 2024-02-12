from typing import Literal, Optional

from colorama import Fore
from colorama import init as colorama_init
from cyclopts import App

from projectile_motion.presenter.descriptions import describe_solution
from projectile_motion.presenter.plots import generate_plot
from projectile_motion.solver.motion import calculate_solution

colorama_init()
app = App()


@app.default
def throw(
    v: float,
    unit: Literal["ms", "kmh"] = "ms",
    angle: float = 0,
    h_init: float = 0,
    g: float = -9.81,
    dist: Optional[float] = None,
    n_steps: int = 100,
):
    """Calculate and plot trajectory of a projectile given initial conditions.
    If the projectile does not move upwards (i.e. angle <= 0 and h_init <= 0), DIST needs to be specified."""

    if all((angle <= 0, h_init <= 0, not dist)):
        print(
            f"{Fore.LIGHTRED_EX}You specified {angle = } degrees and {h_init = } meters. "
            f"In this case, dist needs to be defined.{Fore.RESET}"
        )
        exit()

    solution = calculate_solution(v, unit, h_init, angle, g, dist, n_steps)
    print(describe_solution(solution))
    generate_plot(x_pts=solution.X, y_pts=solution.Y)


if __name__ == "__main__":
    app()
