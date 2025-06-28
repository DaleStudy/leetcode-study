# BST에서 k번째로 작은 value를 반환해라
# 인덱스는 1에서 시작

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 풀이 1. Sort
# 모든 노드의 값을 오름차순으로 정렬 후에 k번째 값을 구한다.
# TC: O(N log N), N은 노드의 개수, 트리 순회 O(N), 정렬 O(N log N)
# SC: O(N), 모든 노드의 값을 저장하는 리스트

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            
            values.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return sorted(values)[k - 1]
    
# 풀이 2. 힙 활용
# k번째로 작은 값 구하기 -> 최대 힙 활용
# - 요소를 -node.val 음수로 변환해 최대 힙 효과를 낸다.
# - 최대 힙에 값을 추가하다가, k개가 초과하면 최대 힙으로부터 최댓값을 제거
#   => 트리 순회 종료 후, 최대 힙에는 가장 작은 k개 값만 남게 된다.
# TC: O(N log K), N은 노드의 개수, K는 찾고자 하는 값의 순서, 트리 순회 O(N), 최대 힙 삽입/제거 O(logK)
# SC: O(K), 최대 k개의 값을 저장하는 최대 힙

from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []  # 최대 k개의 작은 값을 저장할 최대 힙

        def dfs(node):
            if not node:
                return
            
            heappush(heap, -node.val)
            if len(heap) > k:
                heappop(heap)
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # 힙의 최댓값이 k번째로 작은 값
        return -heap[0]

# 풀이 3. 중위 순회 활용
# BST는 중위 순회를 하면 오름차순으로 노드에 접근할 수 있다
# => 입력 트리를 중위 순회 하면서 노드 값을 배열에 저장하면 자연스럽게 배열은 정렬됨
# TC: O(N), N은 노드의 개수, 트리 순회 O(N)
# SC: O(N), 모든 노드의 값을 저장하는 리스트

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values[k - 1]
