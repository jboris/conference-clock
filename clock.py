class Clock:
    def __init__(self, min=20):
        self.start = min * 60
        self.seg = self.start
        self.state = 'STOP'

    def get_time_seg(self):
        return self.seg

    def get_time_min_seg(self):
        return {
            'minutes:': self.seg // 60,
            'seconds': self.seg - self.seg // 60}

    def set_time_min(self, value):
        if value <= 0:
            raise ValueError('Minimoum 1 minute.')
        else:
            self.start = min * 60
            self.seg = self.start
            self.state = 'STOP'

    def start(self):
        if self.state != 'RUN':
            self.state = 'RUN'

    def update(self):
        if self.state == 'RUN':
            self.seg =- 1

    def stop(self):
        self.state = 'STOP'
        self.seg = self.start

    def pause(self):
        self.state = 'PAUSE'