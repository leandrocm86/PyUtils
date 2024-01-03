from __future__ import annotations
import time


class Clock:

    clocks_by_name: dict[str, Clock] = {}

    def __init__(self, units: float = 1.0, precision: int = 0, name: str | None = None):
        self.units = units
        self.precision = precision
        if name:
            Clock.clocks_by_name[name] = self
        self.last_timestamp = time.time()
        self.total_time = 0

    def check(self) -> float:
        ''' Returns how much time has passed since the previous check (or since the start, for the first call). '''
        penultimate_timestamp = self.last_timestamp
        self.last_timestamp = time.time()
        diff = self.last_timestamp - penultimate_timestamp
        ajusted_diff = round(diff * self.units, self.precision)
        self.total_time += ajusted_diff
        return ajusted_diff

    def restart(self):
        ''' Restarts the counting for the next check. It doesn't erase the accumulated total time. '''
        self.last_timestamp = time.time()

    @classmethod
    def get(cls, clock_name: str) -> Clock:
        if not cls.clocks_by_name.get(clock_name):
            cls.clocks_by_name[clock_name] = Clock()
        return cls.clocks_by_name[clock_name]
