from utils import Singleton


class StopMine(Singleton):
    def __init__(self):
        if not hasattr(self, "h"):
            self.h = 0
        if not hasattr(self, "mine_h"):
            self.mine_h = 1
