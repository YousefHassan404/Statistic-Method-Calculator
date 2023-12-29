from Mean import Mean
class Variance(Mean):
    def __init__(self, list_of_num):
        super().__init__(list_of_num)
    def var(self):
        newList = []
        for i in self.list_of_num:
            newList.append((float(i) - float(self.mean())))
        return float(sum(newList) / float(len(self.list_of_num)))
