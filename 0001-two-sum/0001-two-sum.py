class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        for num in nums:
            
        """
        output =[]
        for i, num in enumerate(nums):
            so = target - num
            if so in nums and nums.index(so) != i :
                output.extend([i, nums.index(so)])
                break
        return output

                
            
