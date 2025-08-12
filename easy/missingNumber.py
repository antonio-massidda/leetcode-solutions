"""
Title: Missing Number
Difficulty: Easy
Language: Python

Description:
You are given an array of length n and containing all the numbers in the range [0, n],
except for one. Find that missing number and return it.

Example:
    Input: nums = [0, 3, 1]
    Output: 2

Constraints:
    - n == len(nums)
    - 1 <= n <= 10^4
    - every nums[i] is unique and in the range [0, n]

Notes:
    Inspired by LeetCode problem #268 (Missing Number)
"""

from typing import List

def missingNumber(nums : List[int]) -> int:
    """
    Return the missing number in nums

    Args:
        nums (List[int]): List of n distinct integers in the range [0, n].

    Returns:
        int: The missing integer in the range.
    """

    ans = (len(nums) * (len(nums)+1)) // 2      # Sum all the numbers in the range [0, n]
    for i in nums:                              #] Remove each element of nums from the sum
        ans -= i                                #]
    return ans                                  # Return the remaining number

if __name__ == "__main__":
    example = [0, 3, 1]
    print(missingNumber(example))