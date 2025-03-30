# Time Complexity: O(m * n) m: number of nodes in root, n: number of nodes in subRoot, n: number of nodes in subRoot - might call the check function (which is O(n)) on every node in root.
# Space Complexity: O(n) - use a queue for BFS that can hold up to O(n) nodes in the worst case.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False 
        if subRoot is None:
            return True

        # helper to compare two trees
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True 
            if node1 is None or node2 is None:
                return False 
            if node1.val != node2.val:
                return False 
            # check left and right recursively
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        # BFS through the main tree
        queue = [root]
        while queue:
            curr = queue.pop(0)
            # if value matches subRoot, check deeper
            if curr.val == subRoot.val:
                if check(curr, subRoot):
                    return True
            # add child nodes to keep exploring
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return False
