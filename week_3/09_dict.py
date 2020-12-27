class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        # key -> kssdfdsf -> self.items[7] = [(kssdfdsf, "test")]
        # key -> ksdsdfsw -> self.items[7] -> [(kssdfdsf, "test")] -> [(ksdsdfsw, "test33")]
        self.items[index] = value
        return

    def get(self, key):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!