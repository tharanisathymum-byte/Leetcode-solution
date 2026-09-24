class Solution(object):
    def smallestIndex(self, nums):

        for i in range(0,len(nums)):
            b=sum(map(int,str(nums[i])))
            if b==i:
                return i
        return -1