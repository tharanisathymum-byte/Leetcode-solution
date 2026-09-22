class Solution(object):
    def majorityElement(self, nums):
        c={}
        for i in nums:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
        for i in c:
            if c[i]>len(nums)/2:
                return i        