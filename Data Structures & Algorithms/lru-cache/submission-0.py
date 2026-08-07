class LRUCache:
    #[LRUCache [2], "put [1, 10],  get [1], put [2, 20],
    # "put[3, 30], get [2], get [1]]
    # Output: [null, null, 10, null, null, 20, -1]
    #cache = [] #capacity = 2 #

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache)>self.cap:
            self.cache.popitem(last=False)
