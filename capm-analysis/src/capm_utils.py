from __future__ import annotations
from dataclasses import dataclass

@dataclass
class CapmResult:
    alpha: float
    beta: float
    alpha_t: float
    beta_t: float
    alpha_pval: float
    beta_pval: float
    r2: float
    n: int
    freq: str  # 'D', 'W', 'M'
    model: object

