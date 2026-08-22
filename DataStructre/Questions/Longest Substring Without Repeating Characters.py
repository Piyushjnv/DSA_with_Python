 # Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
   
        char_index = {}
        longest_sub_string = 0
        left = 0

        for right , letter in enumerate(s):
            if letter in  char_index and char_index[letter] >= left:
                left = char_index[letter] + 1
            char_index[letter] = right 
            longest_sub_string = max(longest_sub_string, right-left + 1)
        return longest_sub_string


solution = Solution()
print(solution.lengthOfLongestSubstring('bbbbbb'))  # Output: 1
print(solution.lengthOfLongestSubstring('abcabcbb'))  # Output: 3
print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3
