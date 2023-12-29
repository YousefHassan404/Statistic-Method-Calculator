from Variance import Variance
class StanderDevation(Variance):
    def __init__(self, list_of_num):
        super().__init__(list_of_num)
    def sd(self):
        import math
        standerDvation = (self.var())
        return ((math.sqrt(float(standerDvation))))
