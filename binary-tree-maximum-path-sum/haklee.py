"""TC: O(), SC: O()


아이디어:
- 

SC:
- 

TC:
- 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = [-1001]  # 노드의 최소값보다 1 작은 값. 현 문제 세팅에서 -inf 역할을 함.

        def try_get_best_path(node):
            if node is None:
                # 노드가 비어있을때 경로 없음. 이때 이 노드로부터 얻을 수 있는 최대 경로 값을
                # 0으로 칠 수 있다.
                return 0

            # 왼쪽, 오른쪽 노드로부터 얻을 수 있는 최대 경로 값.
            l = max(try_get_best_path(node.left), 0)
            r = max(try_get_best_path(node.right), 0)

            # 현 노드를 다리 삼아서 양쪽 자식 노드의 경로를 이었을때 나올 수 있는 경로 값이
            # 최대 경로일 수도 있다. 이 값을 현 솔루션과 비교해서 업데이트 해준다.
            sol[0] = max(node.val + l + r, sol[0])

            # 현 노드의 부모 노드가 `이 노드를 통해 얻을 수 있는 최대 경로 값`으로 사용할 값을 리턴.
            return node.val + max(l, r)

        try_get_best_path(root)
        return sol[0]
