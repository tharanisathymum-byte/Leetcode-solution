class Solution(object):
    def winningPlayer(self, x, y):
        moves=min(x,y/4)
        if moves%2==1:
            return "Alice"
        else:
            return "Bob"