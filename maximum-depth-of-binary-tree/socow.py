
class Solution:
    def maxDepth(self, root: Optional['TreeNode']) -> int:
        """
        문제
        - 이진트리의 최대 깊이를 구하라.

        아이디어 (재귀 DFS)
        - 공집합(None)의 깊이는 0
        - 현재 노드 깊이 = max(왼쪽 서브트리 깊이, 오른쪽 서브트리 깊이) + 1

        시간복잡도: O(n)  — 각 노드를 한 번씩 방문
        공간복잡도: O(h)  — 재귀 스택(h는 트리 높이; 최악 O(n), 평균 O(log n))
        """
        # 1) 빈 트리이면 깊이 0
        if not root:
            return 0

        # 2) 왼쪽/오른쪽 서브트리의 최대 깊이를 구한다
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 3) 현재 노드의 깊이 = 더 큰 서브트리 깊이 + 1(현재 노드 포함)
        return max(left_depth, right_depth) + 1
# dfs(3) - 왼쪽으로 이동
# dfs(9) - 왼쪽으로 이동
# dfs(None) -> 0
# dfs(9) - 오른쪽으로 이동
# dfs(None) -> 0
# dfs(9) 반환: max(0,0)+1 = 1
# dfs(3) - 오른쪽으로 이동
# dfs(20) - 왼쪽으로 이동
# dfs(15) - 왼쪽으로 이동
# dfs(None) -> 0
# dfs(15) - 오른쪽으로 이동
# dfs(None) -> 0
# dfs(15) 반환: max(0,0)+1 = 1
# dfs(20) - 오른쪽으로 이동
# dfs(7) - 왼쪽으로 이동
# dfs(None) -> 0
# dfs(7) - 오른쪽으로 이동
# dfs(None) -> 0
# dfs(7) 반환: max(0,0)+1 = 1
# dfs(20) 반환: max(1,1)+1 = 2
# dfs(3) 반환: max(1,2)+1 = 3
# 최종 결과: 3
