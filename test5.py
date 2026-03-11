"""Simple quick sort implementation."""

from __future__ import annotations


def quick_sort(nums: list[int]) -> list[int]:
    """Return a new list containing the sorted values from nums."""

    if len(nums) <= 1:
        return nums[:]

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample = [3, 6, 2, 7, 5, 4, 1]
    print("input:", sample)
    print("sorted:", quick_sort(sample))
