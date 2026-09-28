class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for length in range(1, n):
            if n % length == 0:
                substring = s[:length]

                if substring * (n // length) == s:
                    return True

        return False