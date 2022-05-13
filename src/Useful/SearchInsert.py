from math import ceil

def search_insert(nums, target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    found: bool = False
    middle = 0
    if target > nums[right]:
        middle = right + 1
    elif target < nums[left]:
        middle = left
    else:
        while left <= right and not found:
            middle = ceil(left + (right - left) / 2)
            print(left, middle, right)
            if target == nums[middle]:
                found = True
            if target > nums[middle]:
                left = middle + 1
            if target < nums[middle]:
                right = middle - 1
        if not found and target > nums[middle]:
            middle += 1

    return middle


if __name__ == "__main__":
    ok = [1, 3, 5, 6]
    print("result = ", search_insert(ok, 2))
