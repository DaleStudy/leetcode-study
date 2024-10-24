"""TC: O(n), SC: O(h)

h는 주어진 트리의 높이, n은 주어진 트리의 노드 개수.

아이디어:
특정 노드의 깊이는 `max(오른쪽 깊이, 왼쪽 깊이) + 1`이다. 이렇게 설명하자니 부모 노드의 깊이 값이
자식의 깊이 값보다 더 큰 것이 이상하긴 한데... 큰 맥락에서 무슨 말을 하고 싶은지는 이해가 가능하다고
본다.

SC:
- 호출 스택은 트리의 높이(...혹은 깊이)만큼 커진다. O(h).

TC:
- 모든 노드를 방문한다. O(n).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(node: Optional[TreeNode]) -> int:
            return max(get_depth(node.left), get_depth(node.right)) + 1 if node else 0

        return get_depth(root)
