from dataclasses import dataclass


@dataclass
class Solution:
    X: list[float]
    Y: list[float]
    max_h: float
    max_dist: float
    total_time: float
