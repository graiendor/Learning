from typing import List
from math import pow


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
