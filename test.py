class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ls = []
        self.getLayer(root,ls,0)
        if max(ls) - min(ls) >1:
            return False
        else: return True
    def getLayer(self,root,ls,layer):
        if not root:
            ls.append(layer)
            return
        return self.getLayer(root.left,ls,layer+1) and self.getLayer(root.right,ls,layer+1)

if __name__ == "__main__":
    s = Solution()
    print(s.isBalanced(TreeNode[1,2,2,3,3,1,1,4,4]))
 