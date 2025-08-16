"""Inspired by LeetCode problem #2138 (Divide a String Into Groups of Size k)."""

from typing import List

def divideString(s: str, k: int, fill: str) -> List[str]:
    """
    You are given a string `s` that can be split into groups of size `k`.
    If the last group is made of less than `k` elements, the remaining is filled with the `fill` character.
    Return a list of all the groups.

    Args:
        s (str):    string of lowercase English characters.
        k (int):    number of elements per group.
        fill (str): character to fill in an eventual incomplete group.

    Returns:
        List[str]:  List of all the groups.
    """

    ans = []

    # Append all the groups to ans.
    for i in range(0, len(s), k):
        ans.append(s[i:i+k])
    
    # Fill in the last eventual incomplete group with the `fill` character.
    ans[-1] = ans[-1] + fill * (k - len(ans[-1]))
    return ans

if __name__ == "__main__":
    print(divideString("cbaedfihg", 3, "x"))