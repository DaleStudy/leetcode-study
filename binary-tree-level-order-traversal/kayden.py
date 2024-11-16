class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, level):
            if not node:
                return

            if len(result) <= level:
                result.append([])

            result[level].append(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        result = []
        traverse(root, 0)
        return result