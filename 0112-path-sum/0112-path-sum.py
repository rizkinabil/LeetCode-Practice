# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        if not root:
            return False

        def dfs(node, remaining_sum):

            if not node:
                return False

            # substract remaining sum from node value
            remaining_sum -= node.val

            # check if this a leaf node
            is_leaf = node.left is None and node.right is None


            if is_leaf and remaining_sum == 0:
                return True

            # Recursively check left and right subtrees
            # Return True if EITHER path succeeds
            return dfs(node.left, remaining_sum) or dfs(node.right, remaining_sum) 

        
        return dfs(root, targetSum)

        