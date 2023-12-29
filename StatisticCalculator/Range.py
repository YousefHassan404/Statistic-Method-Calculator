class Range:
    def __init__(self, list_of_num):
        self.__list_of_num = list_of_num
    def range(self):
        greater_num=max(self.__list_of_num)
        smaller_num=min(self.__list_of_num)
        range=greater_num-smaller_num
        return range

