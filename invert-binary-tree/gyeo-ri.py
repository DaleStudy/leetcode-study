"""
[결과 요약]
# 시도한 로직 수: 2
    1. DFS를 활용하는 방법
        - 현재 노드의 좌우를 바꾼 다음 바로 아래 노드로 이동
            - 하위 노드가 없는 노드를 만날 때까지 반복되고 종료됨
        - 시간복잡도는 O(n)
            - 공간복잡도는 O(n)이고, 트리가 균형이면 O(logn)까지 가능(B-Tree 같은 경우)
    2. BFS를 활용하는 방법
        - 시간복잡도/공간복잡도 모두 O(n)
            - DFS와 성능 차이가 크게 없음
    3. BFS에서 약간의 메모리 개선하기
        - None을 queue에 넣지 않는 방법
        - 트리 크기가 아주 크지 않다면 큰 효과는 없음
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        next_nodes: deque[TreeNode] = deque([root])

        while next_nodes:
            current = next_nodes.popleft()
            if not current:
                continue

            current.left, current.right = current.right, current.left

            if current.left:
                next_nodes.append(current.left)
            if current.right:
                next_nodes.append(current.right)

        return root


"""
# DFS를 활용한 방법
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(current: TreeNode | None):
            if not current:
                return

            current.left, current.right = current.right, current.left

            dfs(current.right)
            dfs(current.left)

        dfs(root)
        return root
"""

if __name__ == "__main__":
    from collections import deque

    def _build_tree(values: list[int | None]) -> TreeNode | None:
        if not values:
            return None

        nodes = [TreeNode(value) if value is not None else None for value in values]

        child_idx = 1

        for node in nodes:
            if node is not None:
                if child_idx < len(nodes):
                    node.left = nodes[child_idx]
                    child_idx += 1

                if child_idx < len(nodes):
                    node.right = nodes[child_idx]
                    child_idx += 1

        return nodes[0]

    def _tree_to_list(root: TreeNode | None) -> list[int | None]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append(None)
                continue

            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while result and result[-1] is None:
            result.pop()

        return result

    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, None, 2]),
    ]

    solution = Solution()

    for idx, (inp, expected) in enumerate(test_cases, start=1):
        root = _build_tree(inp)

        result_root = solution.invertTree(root)
        result = _tree_to_list(result_root)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")
