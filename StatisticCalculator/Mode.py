class Mode:
    def __init__(self, list_of_num):
        self.__list_of_num = list_of_num
    def mode(self):
        from collections import Counter
        inputList = self.__list_of_num
        counts = Counter(inputList)
        max_frequency = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_frequency]
        return modes