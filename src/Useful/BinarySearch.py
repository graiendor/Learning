from math import ceil
from typing import List


def search(nums: List[int], target: int) -> int:
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


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    assert print(search(nums, 2)) == -1
    assert print(search(nums, 9)) == 5
    
