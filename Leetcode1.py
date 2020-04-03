class Solution(object):
    def singleNumber(self, nums):
        
        val = 0
        for i in range(0,len(nums)):
            val ^= nums[i]
        
        return val
    
