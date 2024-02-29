# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        max_val=float('-inf')
        min_val=float('inf')
        def traverse(root,max_val,min_val):
            if not root:
                val=max_val-min_val
                return val
            max_val=max(max_val,root.val)
            min_val=min(min_val,root.val)
            left=traverse(root.left,max_val,min_val)
            right=traverse(root.right,max_val,min_val)
            ans=max(left,right)
            return ans
        return traverse(root,max_val,min_val)
            

        
        
        