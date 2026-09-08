# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)
            
        helper(root)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    result = sol.inorderTraversal(root)

    print("Resultado Inorder:", " ".join(map(str, result)))