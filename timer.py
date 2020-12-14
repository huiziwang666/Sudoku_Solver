import time


class TimerError(Exception):
    pass


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        # Start a new timer
        if self.start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self.start_time = time.perf_counter()

    def stop(self):
        # Stop the timer, and report the elapsed time
        if self.start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = int(time.perf_counter() - self.start_time)
        sec = elapsed_time % 60
        minute = elapsed_time // 60
        hour = minute // 60

        run_time = " " + str(hour) + ":" + str(minute) + ":" + str(sec)
        self.start_time = None
        print(f"Time used: {run_time}")


def main():
    t = Timer()
    t.start()
    input("Wait for some time and press enter")
    t.stop()


if __name__ == "__main__":
    main()
