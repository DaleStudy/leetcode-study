"""
[문제풀이]
# Inputs
TreeNode 클래스 객체

# Outputs
valid 이진 탐색 트리인지에 대한 여부

# Constraints
The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1

# Ideas
root 배열 길이 기준으로 풀려고 했지만, root는 배열이 아닌 TreeNode 클래스의 객체이다.
1. bfs로 구현해보기
트리 높이 기준으로 퍼지면서 탐색하는 모양이라 bfs 선택

cur = root
q.append(cur)

while not q:
    cur_node = q.popleft()
    if cur_node == null:
        continue

    if  cur_node.right != null and (cur_node.left.val > cur_node.val or cur_node.right.val < cur_node.val):
        return False

    else:
        q.append(cur_node.left)

먼가 조건문이 길어지는 것 같아 효율적인 풀이는 아닌 것 같지만..일단 시도!

n이 node 개수라면
Time: O(n), Space: O(n)

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([])
        q.append(root)

        while q:
            cur_node = q.popleft()
            if cur_node is None:
                continue

            if cur_node.left is not None and cur_node.left.val >= cur_node.val:
                return False

            elif cur_node.right is not None and cur_node.right.val <= cur_node.val:
                return False

            else:
                q.append(cur_node.left)
                q.append(cur_node.right)

        return True

- 반례 발생
root =
[5,4,6,null,null,3,7]

왜 BST가 아닌지 이해가 안간다..
-> 3이 5보다 작아서 그렇다
루트 기준 오른쪽은 자식 값들도 무조건 작아야한다.
그럼 한 단계 위의 값만 보면 안된다는 건데, 탐색 방법 바꿔야 할 것 같다

2. 재귀로 돌면서, 이 값보다는 커야한다는 배열을 인자로 함께 넘겨주기?
하지만, 어느 dfs에서 배열 원소들보다 본인 값이 커야하는지, 작야하는지 모름!!

결국 풀이 참고

[회고]


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = True

        def dfs(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
