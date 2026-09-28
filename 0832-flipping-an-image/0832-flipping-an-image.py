class Solution(object):
    def flipAndInvertImage(self, image):
        a=[]
        for i in image:
            i.reverse()
            a.append([x^1 for x in i])
        return a