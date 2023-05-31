# Longest Substring Without Repeating Characters 
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = p2 = 0
        max_str = s[0:1]
        while p2 <= len(s):
            temp = s[p1:p2]
            if len(temp) > len(max_str):
                max_str = temp
            if p2 == len(s):
                break
            if s[p2] not in temp:
                p2 += 1
            else:
                p1 += 1
                
        return len(max_str)