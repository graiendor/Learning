from typing import List
from math import pow, ceil


class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        """Finds the maximum number of consecutive 1's in the array"""
        count: int = 0
        final_count: int = 0
        for it in nums:
            if it == 1:
                count += 1
            else:
                if count > final_count:
                    final_count = count
                count = 0
        if count > final_count:
            final_count = count
        return final_count

    def find_numbers(self, nums: List[int]) -> int:
        """Finds numbers in the given array, which contains only even number of digits (for example: 1234)"""
        count: int = 0
        total_count: int = 0
        for it in nums:
            while it > 1:
                it /= 10
                count += 1
            if count % 2 == 0:
                total_count += 1
            count = 0

        return total_count

    def sorted_squares(self, nums: List[int]) -> List[int]:
        """Squares negative and positive numbers in the given array,
        and returns the sorted array of squares"""
        positive: List[int] = []
        negative: List[int] = []
        for it in nums:
            if it < 0:
                negative.insert(0, int(pow(it, 2)))
            else:
                positive.append(int(pow(it, 2)))
        index = 0
        if not positive:
            positive = negative
        else:
            for i in negative:
                length = len(positive)
                if i >= positive[index]:
                    if index < length:
                        index += 1
                        while index + 1 <= length and i >= positive[index]:
                            index += 1
                        positive.insert(index, i)
                    else:
                        positive.append(i)
                else:
                    positive.insert(0, i)

        return positive

    def duplicate_zeros(arr: List[int]) -> None:
        """Duplicates any zero in an array"""
        index: int = 0
        to_insert: List[int] = []
        length = len(arr)
        while index < length:
            if arr[index] == 0:
                arr.insert(index + 1, 0)
                index += 1
                arr.pop()
            index += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merges two sorted in a non-decreasing order arrays, changing only nums1"""
        index_nums1 = m - 1
        index_nums2 = n - 1

        if len(nums1) > 0:
            while index_nums2 >= 0:
                print(index_nums1)
                if nums1[index_nums1] < nums2[index_nums2]:
                    nums1.insert(index_nums1 + 1, nums2[index_nums2])
                    nums2.pop()
                    index_nums2 -= 1
                elif index_nums1 > 0:
                    index_nums1 -= 1
                else:
                    nums1.insert(0, nums2[index_nums2])
                    nums2.pop()
                    index_nums2 -= 1

        else:
            for i in nums2:
                nums1.append(i)

    def remove_element(self, nums: List[int], val: int) -> int:
        for i, v in enumerate(nums):
            if v == val:
                nums.remove(v)

        return len(nums)

    def remove_duplicates(self, nums: List[int]) -> int:
        """Remove all duplicates in the given unsorted array"""
        previous: dict = {}
        index: int = 0
        # length: int = len(nums)
        for v in nums:
            print(v)
            if not previous.get(v):
                nums[index] = v
                index += 1
                previous.update({v: 1})

        return index

    def rotate_array(self, nums: List[int], k: int) -> None:
        """Shifts right the one-dimensional array by k"""
        k = k % len(nums)
        diff = len(nums) - k
        nums[:k], nums[k:] = nums[diff:],nums[:diff]

    def moveZeroes(self, nums: List[int]) -> None:
        """Moves all the 0 to the end of the given list"""
        nonzero: int = 0
        length = len(nums)
        for value in nums:
            if value:
                nums[nonzero] = value
                nonzero += 1
        for count in range(length - nonzero):
            nums[nonzero] = 0
            nonzero += 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for count, value in enumerate(numbers):
            match: int = self.search(numbers, target - value)
            found_value = numbers[match]
            while match == count and numbers[match] == found_value:
                match += 1
            if numbers[match] + value == target:
                return [count + 1, match + 1]

    def search(self, nums: List[int], target: int) -> int:
        right: int = len(nums) - 1
        left: int = 0
        middle: int = ceil(right / 2)

        while nums[middle] != target and middle != -1:
            if nums[middle] > target:
                right = middle - 1
                middle = left + ceil((right - left) / 2)
            if nums[middle] < target:
                left = middle + 1
                middle = left + ceil((right - left) / 2)
            if left > right:
                middle = -1

        return middle

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

        Performs a flood fill on the image starting from the pixel image[sr][sc].

        Returns the modified image after performing the flood fill."""
        source: int = image[sr][sc]
        if source != newColor:
            image[sr][sc] = newColor
            image = self.recursiveFill(image, sr, sc, newColor, source)
        return image

    def recursiveFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, source: int) -> List[List[int]]:
        column_length: int = len(image)
        rows_length: int = len(image[0])
        if sr + 1 in range(column_length) and image[sr + 1][sc] == source:
            image[sr + 1][sc] = newColor
            image = self.recursiveFill(image, sr + 1, sc, newColor, source)
        if sr - 1 in range(column_length) and image[sr - 1][sc] == source:
            image[sr - 1][sc] = newColor
            image = self.recursiveFill(image, sr - 1, sc, newColor, source)
        if sc + 1 in range(rows_length) and image[sr][sc + 1] == source:
            image[sr][sc + 1] = newColor
            image = self.recursiveFill(image, sr, sc + 1, newColor, source)
        if sc - 1 in range(rows_length) and image[sr][sc - 1] == source:
            image[sr][sc - 1] = newColor
            image = self.recursiveFill(image, sr, sc - 1, newColor, source)
        return image

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    counting_size: int = 0
                    counting_size = self.count_size(grid, i, j, counting_size)
                    max_size = max(max_size, counting_size)
        return max_size

    def count_size(self, grid: List[List[int]], i, j, counting_size) -> int:
        """Given an m x n binary matrix grid. An island is a group of 1's (representing land)
        connected 4-directionally (horizontal or vertical.)

        The area of an island is the number of cells with a value 1 in the island.

        Returns the maximum area of an island in grid. If there is no island, returns 0."""
        if grid[i][j] == 1:
            grid[i][j] = 2
            counting_size += 1
            if i > 0: counting_size = self.count_size(grid, i - 1, j, counting_size)
            if j > 0: counting_size = self.count_size(grid, i, j - 1, counting_size)
            if i + 1 < len(grid): counting_size = self.count_size(grid, i + 1, j, counting_size)
            if j + 1 < len(grid[0]): counting_size = self.count_size(grid, i, j + 1, counting_size)
        return counting_size


if __name__ == "__main__":
    # print(Solution.sorted_squares([-4, -1, 0, 3, 10]))
    # print(Solution.sorted_squares([-10000, -9999, -7, -5, 0, 0, 10000]))
    # print(Solution.sorted_squares([-1, 2, 2]))
    # a: Solution
    # arr = [1, 0, 2, 3, 0, 4, 5, 0]
    # Solution.duplicateZeros(arr)
    # print(arr)
    print(Solution().remove_duplicates([1, 2, 1, 6, 2, 5, 6, 4]))

    # print(32 / 10)
