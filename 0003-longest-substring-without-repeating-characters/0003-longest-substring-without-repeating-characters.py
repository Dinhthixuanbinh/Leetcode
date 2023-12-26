class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = result = 0
        seen = {}
        for i, letter in enumerate(s):
            if seen.get(letter, -1) >= start:
                
                start = seen[letter] + 1
            result = max(result, i - start + 1)
            seen[letter] = i
        return result