# https://leetcode.com/problems/validate-binary-search-tree/description/

# 도저히 안풀어서 지피티의 도움을 받았습니다..TT
# 새로 알게 된 개념
# 이진 트리는 하나의 노드가 최대 두 개의 자식 노드를 가지는 트리 자료구조
# 두 개의 포인터를 가지고 있으며, 루트에서 시작해서 아래로 내려가는 계층 구조
# Binary Search Tree(BST)는 이진 트리의 한 종류로 어떤 노드의 왼쪽 서브트리에 있는 모든 값은 해당 노드보다 작고 오른쪽 서브트리에 있는 모든 값은 해당 노드보다 큼
# 이 문제는 주어진 트리가 이 규칙을 만족하는지 확인하는 문제임
# 각 노드가 가질 수 있는 허용 범위(min, max)를 유지하면서 검사해야 함
class Solution:
    def isValidBST(self, root):

        def dfs(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))
