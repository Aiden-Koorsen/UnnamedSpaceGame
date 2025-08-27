# This is a number of included components in the engine
class Renderable:
    def __init__(self, key = "unknown"):
        self.key = key

class Position:
    def __init__(self, x : int = 0, y : int = 0):
        self.x = x
        self.y = y
        self.tuple_pos = (x, y)