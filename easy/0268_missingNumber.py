"""Inspired by LeetCode problem #268 (Missing Number)."""

from typing import List

def missingNumber(nums : List[int]) -> int:
    """
    You are given an array of length `n` and containing all the numbers in the range [0, n], except for one.
    Find that missing number and return it.

    Args:
        nums (List[int]):   List of `n` distinct integers in the range [0, n].

    Returns:
        int:    The missing integer in the range.
    """

    # Sum all the numbers in the range [0, n].
    ans = (len(nums) * (len(nums)+1)) // 2

    # Remove each element of `nums` from the sum.
    for i in nums:
        ans -= i

    # Return the remaining number.
    return ans

if __name__ == "__main__":
    print(missingNumber([0, 3, 1]))