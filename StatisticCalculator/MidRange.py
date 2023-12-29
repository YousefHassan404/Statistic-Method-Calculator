from Range import Range
class MidRange(Range):
    def __init__(self, list_of_num):
        super().__init__(list_of_num)
    def mid_range(self):
        return self.range()/2

