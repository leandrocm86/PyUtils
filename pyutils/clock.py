import time


class Clock:
    ts = 0
    @staticmethod
    def start():
        Clock.ts = time.time()
    @staticmethod
    def check(text=''):
        """Prints how much time has passed since the previous check (or since the start, for the first call).
        An optional text can be passed to be printed alongside the result."""
        time_passed = time.time() - Clock.ts
        if text:
            print(text, str(time_passed))
        Clock.ts = time.time()
        return time_passed

    