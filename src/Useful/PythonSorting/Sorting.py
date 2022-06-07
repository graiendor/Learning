class Sort:
    def selection(self, array: list) -> None:
        for iterator in range(len(array)):
            lowest_index: int = iterator
            for count in range(iterator + 1, len(array)):
                if array[count] < array[lowest_index]:
                    lowest_index = count
            array[iterator], array[lowest_index] = array[lowest_index], array[iterator]


    def bubble(self, array: list) -> None:
        for iterator in range(len(array)):
            for count in range(iterator + 1, len(array)):
                if array[count] < array[iterator]:
                    array[iterator], array[count] = array[count], array[iterator]

    def insertion(self, array: list) -> None:
        for iterator in range(len(array)):
            count: int = 0
            while array[count] < array[iterator]:
                count += 1
            array.insert(count, array.pop(iterator))

    def merge(self, array: list) -> None:
        length: int = len(array)
        if length > 1:
            left_array: list = array[:length // 2]
            right_array: list = array[length // 2:]
            self.merge(left_array)
            self.merge(right_array)

            position: int = 0
            i: int = 0
            j: int = 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[position] = left_array[i]
                    i += 1
                else: 
                    array[position] = right_array[j]
                    j += 1
                position += 1
            
            for i in range(i, len(left_array)):
                array[position] = left_array[i]
                position += 1

            for j in range(j, len(right_array)):
                array[position] = right_array[j]
                position += 1

    def quick(self, array: list) -> None:
        self.__quicksort__(array, 0, len(array) - 1)


    def __quicksort__(self, array: list, left: int, right: int) -> None:
        if left < right:
            partition_position = self.__partition__(array, left, right)
            self.__quicksort__(array, left, partition_position - 1)
            self.__quicksort__(array, partition_position + 1, right)

    def __partition__(self, array: list, left: int, right: int) -> int:
        i = left
        j = right - 1
        pivot = array[right]

        while i < j:
            while i < right and array[i] < pivot:
                i += 1
            while j > left and array[j] >= pivot:
                j-= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
            
        if array[i] > pivot:
            array[i], array[right] = array[right], array[i]
        
        return i

    def counting(self, array: list) -> list:
        positions: dict[int, int] = {i: 0 for i in range(min(array), max(array) + 1)}
        for _, value in enumerate(array):
            positions.update({value: positions.get(value) + 1})
        future_value = 0
        for _, key in enumerate(positions.keys()):
            value = positions.get(key)
            if value != 0:
                positions.update({key: future_value})
                future_value += value
        output: list = [0 for i in range(len(array))]
        for _, value in enumerate(array):
            output[positions.get(value)] = value
            positions.update({value: positions.get(value) + 1})
        return output
            