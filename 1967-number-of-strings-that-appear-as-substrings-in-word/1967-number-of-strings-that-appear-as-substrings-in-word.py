class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(patterns in word for patterns in patterns)