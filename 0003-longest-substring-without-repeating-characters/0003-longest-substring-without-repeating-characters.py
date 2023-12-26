class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_list =[]
        max_len = 0
        for word in s:
            if word not in count_list :
                count_list.append(word)
                print(count_list)
            else:
                
                if len(count_list) > max_len:
                    max_len = len(count_list) 
                 
                print(max_len)
                del count_list[: count_list.index(word)+1]
                count_list.append(word)
                print(count_list)
        if len(count_list) > max_len:
            max_len = len(count_list)
        return max_len