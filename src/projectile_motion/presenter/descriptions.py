from projectile_motion.solver.solution import Solution


def describe_solution(sol: Solution) -> str:
    return (
        f"\n\nTotal distance covered: {sol.max_dist:.2f} meters in {sol.total_time:.2f} seconds."
        f"\nMax height achieved: {sol.max_h:.2f} meters.\n"
    )
