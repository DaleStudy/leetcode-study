class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(k)
    """

    def inOrder(self, root: TreeNode, asc_sorted_list: list[int], k: int) -> None:
        if root.left: 
            self.inOrder(root.left, asc_sorted_list, k)
        
        asc_sorted_list.append(root.val)

        if len(asc_sorted_list) < k and root.right: 
            self.inOrder(root.right, asc_sorted_list, k)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        asc_sorted_list = [] 
        self.inOrder(root, asc_sorted_list, k)

        return asc_sorted_list[k - 1]
