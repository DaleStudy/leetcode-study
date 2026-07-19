'''
스택을 활용한 DFS

시간 복잡도: O(N)
공간 복잡도: O(H), H: 트리의 높이
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 트리가 비어있으면 길이는 0
        if root is None:
            return 0

        max_depth = 1

        # 스택에 (현재 노드, 노드의 깊이) 튜플을 저장
        stack = [(root, 1)]

        while stack:
            node, cur_depth = stack.pop()

            # 현재 노드의 깊이와 저장된 최댓값을 비교하여 갱신
            max_depth = max(cur_depth, max_depth)

            # 왼쪽 자식 노드가 있다면 현재 깊이 + 1을 하여 스택에 추가
            if node.left:
                stack.append((node.left, cur_depth + 1))

            # 오른쪽 자식 노드가 있다면 현재 깊이 + 1을 하여 스택에 추가
            if node.right:
                stack.append((node.right, cur_depth + 1))

        return max_depth

'''
큐를 활용한 BFS

시간 복잡도: O(N)
공간 복잡도: O(W), W: 트리의 최대 너비
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 트리가 비어있으면 길이는 0
        if root is None:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # 현재 레벨에 있는 노드의 개수만큼 반복 처리
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 한 레벨의 탐색이 끝나면 깊이 증가
            depth += 1
            
        return depth

'''
재귀 함수 풀이

시간 복잡도: O(N)
공간 복잡도: O(H), H: 스택의 높이
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 현재 자신의 노드 하나를 더해서 최대 깊이를 반환
        return max(left_depth, right_depth) + 1