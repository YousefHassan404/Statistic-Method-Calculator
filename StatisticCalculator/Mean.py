class Mean:
    def __init__(self,list_of_num):
        self.list_of_num = list_of_num
    def mean(self):
        return sum(self.list_of_num)/len(self.list_of_num)
