class Processor:
    def __init__(self):
        self.cache = []

    def process(self, data):
        self.cache.append(data)
        if len(self.cache) > 50:
            self.cache.clear()
