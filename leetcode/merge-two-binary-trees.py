# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root1, root2):
            if not root1 and not root2:
                return None
            elif not root1:
                return root2
            elif not root2:
                return root1
            else:
                new_node = TreeNode(root1.val + root2.val)
                new_node.left = traverse(root1.left, root2.left)
                new_node.right = traverse(root1.right, root2.right)
                return new_node

        return traverse(root1, root2)
