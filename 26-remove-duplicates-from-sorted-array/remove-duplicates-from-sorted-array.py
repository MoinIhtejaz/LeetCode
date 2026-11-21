class Solution(object):
    def removeDuplicates(self, nums):
        


        # using 2 pointers i and j, 
        # i overwrites and j compares
        i=0
        for j in range(0 , len(nums) -1):
            if nums[j] != nums[j+1]:
                i = i+1
                nums[i] = nums[j+1]
                

        nums[:] = nums[0:i+1]

        return len(nums)