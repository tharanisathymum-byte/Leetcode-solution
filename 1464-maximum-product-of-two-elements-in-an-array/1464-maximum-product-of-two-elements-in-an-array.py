class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-2]-1)*(nums[-1]-1)