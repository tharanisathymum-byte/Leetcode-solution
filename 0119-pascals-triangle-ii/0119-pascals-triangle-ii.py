class Solution(object):
    def getRow(self, rowIndex):
        n=rowIndex
        for i in range(n+1):
            val=1
            c=[]
            for j in range(i+1):
                c.append(val)
                val=val*(i-j)//(j+1)
        return c