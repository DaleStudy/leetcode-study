"""TC: O(n), SC: O(h)


아이디어:
- 각 노드를 부모, 혹은 자식 노드의 관점에서 분석할 수 있다.
- 부모 노드의 관점에서 경로를 만들때:
    - 부모 노드는 양쪽 자식 노드에 연결된 경로를 잇는 다리 역할을 할 수 있다.
    - 이때 자식 노드는
        - 경로에 포함되지 않아도 된다. 이 경우 path에 0만큼 기여하는 것으로 볼 수 있다.
        - 자식 노드의 두 자식 노드 중 한 쪽의 경로와 부모 노드를 이어주는 역할을 한다.
          아래서 좀 더 자세히 설명.
- 자식 노드의 관점에서 경로를 만들때:
    - 자식 노드는 부모 노드와 연결될 수 있어야 한다.
    - 그렇기 때문에 자신의 자식 노드 중 한 쪽과만 연결되어있을 수 있다. 만약 부모 노드와
      본인의 양쪽 자식 노드 모두와 연결되어 있으면 이 노드가 세 갈림길이 되어서 경로를 만들
      수 없기 때문.
- 위의 분석을 통해 최대 경로를 만들고 싶다면, 다음의 함수를 root를 기준으로 재귀적으로 실행한다.
    - 특정 node가 부모 노드가 되었다고 했을때 본인의 값에 두 자식의 max(최대 경로, 0) 값을 더해서
      경로를 만들어본다. 이 값이 기존 solution보다 클 경우 solution을 업데이트.
    - 특정 node가 자식 노드가 될 경우 본인의 두 자식 중 더 큰 경로를 부모에 제공해야 한다.
      본인의 값에 max(왼쪽 경로, 오른쪽 경로)을 더해서 리턴.

SC:
- solution값을 관리한다. O(1).
- 호출 스택은 트리의 높이만큼 쌓일 수 있다. O(h).
- 종합하면 O(h).

TC:
- 각 노드에서 O(1) 시간이 소요되는 작업 수행.
- 모든 노드에 접근하므로 O(n).
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
