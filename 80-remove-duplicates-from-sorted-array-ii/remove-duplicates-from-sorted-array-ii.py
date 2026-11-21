class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        i = 2  # write pointer — first two elements are always valid, no check needed
        
        for j in range(2, len(nums)):  # read pointer
            if nums[j] != nums[i - 2]:  # compare two slots back
                nums[i] = nums[j]
                i += 1
        
        return i