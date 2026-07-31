class Solution:
    def minimumPushes(self, word: str) -> int:
        #Here we count the frequency of each char in the word...
        counts=[word.count(chr(97+i)) for i in range(26)]
        #Then sort them according to the highest frequency>>>
        counts=sorted(counts,reverse=True)
        res=0
        for idx,count in enumerate(counts):
            #this is for optimization
            if(count==0):
                break
            res+=count*((idx//8)+1)
        return res



