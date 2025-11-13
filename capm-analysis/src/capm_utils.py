from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

import pandas as pd
import yfinance as yf

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
    freq: str
    model: object


def _to_datetime(x) -> pd.DatetimeIndex:
    return pd.to_datetime(x).tz_localize(None)
    
def download_prices(tickers: Iterable[str], start: str, end: str | None = None, interval: str = "1d") -> pd.DataFrame:
    tickers = list(tickers)
    data = yf.download(tickers = tickers, start = start, end = end, interval = interval, auto_adjust = True, progress = False)

    if isinstance(data, pd.Dataframe) and isinstance(data.columns, pd.Multindex):
        df = data["Close"].copy()
    else:
        df = data if "Close" not in data.columns else data["Close"]

    if isinstance(df, pd.Series):
        df = df.to_frame()

    df.index = _to_datetime(df.index)
    df = df.sort_index().ffill()
    return df.astype(float)
        
