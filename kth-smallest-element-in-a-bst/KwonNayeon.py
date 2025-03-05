"""
Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Time Complexity: O(n)
- 최악의 경우 모든 노드를 방문

Space Complexity: O(h)
- 여기서 h는 트리의 높이, 스택에 최대 h개의 노드가 저장됨

풀이방법:
1. 중위 순회(in-order)를 활용하여 BST의 노드를 오름차순으로 방문
2. 스택을 활용:
   - 트리의 왼쪽으로 내려가면서 모든 노드를 스택에 저장
   - 스택에서 노드를 꺼내고 카운트 증가
   - k번째 노드를 찾으면 해당 값을 반환
   - 오른쪽 트리에 대해서 이 과정을 반복
3. 중위 순회 시 노드 값을 오름차순으로 방문하므로, k번째로 방문한 노드가 k번째 작은 값
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        count = 0

        while node or stack:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            count += 1

            if count == k:
                return node.val

            node = node.right
