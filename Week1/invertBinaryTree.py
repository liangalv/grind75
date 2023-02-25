# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Given the root of a binary tree, invert the tree, and return its root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #first let's define the behaviour when the node is empty 
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left, right = root.left, root.right
        #go left
        root.right = Solution.invertTree(self,left)
        #go right
        root.left = Solution.invertTree(self,right)
        return root

