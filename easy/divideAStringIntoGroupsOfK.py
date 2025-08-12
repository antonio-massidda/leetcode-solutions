"""
Title: Divide a String Into Groups of Size k
Difficulty: Easy
Language: Python

Description:
    You are given a string 's' that can be split into groups of size 'k'.
    If the last group is made of less than 'k' elements, the remaining is filled with the 'fill' character.
    Return a list of all the groups.

Example:
    Input: s = "cbaedfihg", k = 3, fill = "x"
    Output: ["cba","edf","ihg"]

Constraints:
    - 1 <= len(s) <= 100
    - 's' is made of only lowercase English letters.
    - 1 <= k <= 100
    - 'k' can only be a lowercase English letter.

Notes:
    Inspired by LeetCode problem #2138 (Divide a String Into Groups of Size k).
"""

from typing import List

def divideString(s: str, k: int, fill: str) -> List[str]:
    """
    Args:
        s (str):    string of lowercase English characters.
        k (int):    number of elements per group.
        fill (str): character to fill in an eventual incomplete group.

    Returns:
        List[str]:  List of all the groups.
    """

    ans = []
    for i in range(0, len(s), k):                   #] Append all the groups to the answer.
        ans.append(s[i:i+k])                        #]
    ans[-1] = ans[-1] + fill * (k - len(ans[-1]))   #} Fill in the last eventual incomplete group
                                                    #} with the 'fill' character.
    return ans

if __name__ == "__main__":
    s = "cbaedfihg"
    k = 3
    fill = "x"
    print(divideString(s, k, fill))