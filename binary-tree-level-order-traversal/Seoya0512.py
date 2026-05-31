''''
Time Complexity: O(N)
- 모든 노드를 한 번씩 방문하므로 O(N)

Space Complexity: O(N)
- 결과를 저장하기 위해 values 리스트와 큐에 최대 N개의 노드가 저장
'''
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if not root:
            return result

        queue = deque([root])

        while queue:
            values = []
            for _ in range(len(queue)): # 같은 레벨에 있는 노드를 함께 처리
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(values)
        
        return result
