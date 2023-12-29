class Median:
    def __init__(self, list_of_num):
        self.__list_of_num = list_of_num
    def median(self):
        arranged_numbers = sorted(self.__list_of_num)
        length_of_List = len(arranged_numbers)
        if length_of_List % 2 == 0:
            index = (length_of_List + 1) / 2
            return f"{((arranged_numbers[int(index + .5) - 1] + arranged_numbers[int(index - .5) - 1]) / 2)}"
        elif length_of_List % 2 == 1:
            index = (length_of_List + 1) / 2
            return arranged_numbers[int(index) - 1]