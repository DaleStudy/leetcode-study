# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 루트가 None이면 깊이는 0
        if not root:
            return 0
        
        # 왼쪽 서브트리와 오른쪽 서브트리의 최대 깊이를 재귀적으로 계산
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 현재 노드의 깊이(1) + 왼쪽과 오른쪽 중 더 큰 깊이
        return 1 + max(left_depth, right_depth)

# 테스트 코드
def create_binary_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        current = queue.pop(0)
        
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    
    return root

# 테스트 케이스
solution = Solution()

# 테스트 케이스 1: [3,9,20,None,None,15,7]
tree1 = create_binary_tree([3,9,20,None,None,15,7])
print(solution.maxDepth(tree1))  # 3 출력

# 테스트 케이스 2: [1,None,2]
tree2 = create_binary_tree([1,None,2])
print(solution.maxDepth(tree2))  # 2 출력

# 테스트 케이스 3: []
tree3 = create_binary_tree([])
print(solution.maxDepth(tree3))  # 0 출력 