# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicter={}
        ans=[]
        def preorder(root):
            if root:
                if root.val in dicter:
                    dicter[root.val]+=1
                else:
                    dicter[root.val]=1
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        a=max(dicter.values())
        for key,value in dicter.items():
            if value==a:
                ans.append(int(key))
       
        return ans


        