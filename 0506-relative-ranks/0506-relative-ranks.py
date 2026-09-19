class Solution(object):
    def findRelativeRanks(self, score):
        v=sorted(score)
        c=v[::-1]
        d=[]
        for i in range (len(score)):
            if c[0]==score[i]:
                d.append("Gold Medal")
            elif c[1]==score[i]:
                d.append("Silver Medal")
            elif c[2]==score[i]:
                d.append("Bronze Medal")
            else:
                q=c.index(score[i])
                d.append(str(q+1))
        return d