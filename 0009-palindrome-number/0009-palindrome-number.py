class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number_string = str(x)

        s = number_string[::-1]
        print(s)
        return str(x) == s
            