class Solution:
    def runningSum(self, nums):
        s = 0
        ans = []
        for num in nums:
            s += num
            ans.append(s)
        return ans