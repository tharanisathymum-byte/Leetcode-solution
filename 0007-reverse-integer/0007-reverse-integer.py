class Solution(object):
    def reverse(self, x):
        sy=1
        if x<0:
            x=abs(x)
            sy=-1
        b=0
        while x>0:
            l=x%10
            b=(b*10)+l
            x=x//10
        b*=sy
        if (-(2**31)>b or b>(2**31)-1):
            return 0
        else:
            return b