"""
[문제풀이]
# Inputs
root, subRoot

# Outputs
subRoot의 트리가 root 트리의 서브 트리인지에 대한 여부

# Constraints
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

# Ideas
정확히 구조랑 노드 개수도 같아야 함
-> subRoot의 root 노드 찾으면, 탐색 시작
-> 탐색 끝나고 나서의 node 수 반환
탐색 도중에 node.value 다르면 false 반환

[회고]

"""
# 1차 제출 코드
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(r, sr):
            print('start compare')
            if r is not None and sr.val is not None:
                if r.val != sr.val:
                    print('not same, exit compare')
                    return False

                elif r.val == sr.val == None:
                    print('same, exit compare')
                    return True

                else:
                    print('continue compare')
                    return compare(r.left, sr.left) or compare(r.right, sr.right)

            return True

        def dfs(cur):
            if cur.val != subRoot.val:
                print('going left in root')
                dfs(cur.left)

                print('going right in root')
                dfs(cur.right)

            else:
                print('begin compare')
                return compare(cur, subRoot)
            return

        return dfs(root)

# gpt 수정 코드

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            # 아래 둘 중 하나라도 True면 즉시 return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


