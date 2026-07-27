class Solution(object):
    def inorderTraversal(self, root):
        s=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            s.append(node.val)
            inorder(node.right)
        inorder(root)
        return s