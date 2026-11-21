class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        array1 = nums[len(nums) - k :]
        #this captures the elements to be roateted
        array2 = nums[0 : len(nums) - k]

        nums[:] = array1 + array2

        