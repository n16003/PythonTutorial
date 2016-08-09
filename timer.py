import time


class Timer(object):
    def __init__(self, verbose = False):

        self.verbose = verbose

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.secs = self.end_time - self.start_time
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapsed time: {0:f} ms'.format(self.millis))
