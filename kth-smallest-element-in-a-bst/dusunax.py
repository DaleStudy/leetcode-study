'''
# 230. Kth Smallest Element in a BST

BST에서 k 번째의 값 찾기

- Inorder Traversal: 이진 탐색 트리를 중위 순회하면 트리의 모든 값을 오름 차순으로 방문할 수 있다.
  - 중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
- k번째 가장 작은 값을 구하면 방문을 중단한다.
'''
class Solution:
    '''
    ## 1. count를 사용하여 k번째 가장 작은 값을 찾는 방법
    - 중위 순회를 하면서 노드를 방문하고, 방문한 횟수를 세서 k번째 값을 찾습니다.
    - 순회를 중단하는 방식으로 메모리를 절약합니다.
    TC: O(n)
    SC: O(h) - 재귀 호출 스택 공간 (h는 트리의 높이)
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def inorder(node):
            nonlocal count, result 

            if not node:
                return
            
            inorder(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            inorder(node.right)
        
        inorder(root)

        return result
    
    '''
    ## 2. 순회 결과를 리스트에 저장하여 가장 작은 값을 찾는 방법
    - 순회 결과를 리스트에 저장하여 가장 작은 값을 찾습니다.
    - 메모리를 더 많이 사용하지만, 코드가 더 간결합니다.
    TC: O(n)
    SC: O(n)
    '''
    def kthSmallestWithResultList(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node):
            if not node:
                return
            if len(result) > k:
                return node

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return result[k - 1]
