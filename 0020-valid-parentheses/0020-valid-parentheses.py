class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dirs = {'(': ')', '{': '}', '[' :']'}
        for item in s:
            if item in dirs:
                stack.append(item)
            elif len(stack) == 0 or dirs[stack.pop()] != item:
                return False
        return len(stack) == 0