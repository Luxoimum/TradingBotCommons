from dataclasses import dataclass


@dataclass
class StrategyParameters:
    ema_length: int = 20
    sma_length: int = 50
    array_size: int = 100  # This number would be grater than all above
    window: int = 50
    chop_length: int = 14
    rsi_length: int = 7
