class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []  # [LinkedTuple(),....]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        # LinkedTuuple
        # []
        # [(key, value)]
        self.items[index].add(key, value)
        return

    def get(self, key):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key1, value1), (key, value)]
        return self.items[index].get(key)