from collections import deque
from unittest import TestCase, main


# Definition of TreeNode:
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.solve_bfs(root, p, q)

    """
    Runtime: 50 ms (Beats 81.68%)
    Time Complexity:`
        - bfs를 이용해 ancetor와 nodes를 초기화 하는데 트리의 모든 p와 q를 포함할 때까지 모든 node를 조회하는데, O(n)
        - p로 부터 부모를 따라 올라가는데, 트리의 모든 node가 편향적으로 연결된 경우 최대 O(n), upper bound
            - q로 부터 부모를 따라 올라가는데, 단, 위 p의 추적 path와 겹치지 않는 곳만 올라가므로, 총합이 O(n)
        > O(n) + (O(P) + O(Q)) = O(n) + O(n) ~= O(n) 

    Memory: 21.20 MB (Beats 14.40%)
    Space Complexity: O(n)
        - p, q가 트리의 리프노드인 경우 dq의 크기는 O(n), upper bound
        - p_ancestors와 q_anscestor의 크기는 합쳐서 O(n)
        > O(n) + O(n) ~= O(n)
    """
    def solve_bfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dq = deque([root])
        ancestor = {root.val: root.val}
        nodes = {root.val: root}
        while dq:
            if p.val in ancestor and q.val in ancestor:
                break

            curr_node = dq.popleft()
            if curr_node.left:
                ancestor[curr_node.left.val] = curr_node.val
                dq.append(curr_node.left)
                nodes[curr_node.left.val] = curr_node.left
            if curr_node.right:
                ancestor[curr_node.right.val] = curr_node.val
                dq.append(curr_node.right)
                nodes[curr_node.right.val] = curr_node.right

        p_val = p.val
        p_ancestors = set()
        p_ancestors.add(root.val)
        while p_val in ancestor and p_val != root.val:
            p_ancestors.add(p_val)
            p_ancestors.add(ancestor[p_val])
            p_val = ancestor[p_val]

        q_val = q.val
        q_ancestors = set()
        q_ancestors.add(q_val)
        while q_val in ancestor and q_val not in p_ancestors:
            q_ancestors.add(q_val)
            q_ancestors.add(ancestor[q_val])
            q_val = ancestor[q_val]

        common_ancestor = p_ancestors & q_ancestors
        if common_ancestor:
            return nodes[common_ancestor.pop()]
        else:
            return root


class _LeetCodeTestCases(TestCase):

    def test_1(self):
        root = TreeNode(5)
        node1 = TreeNode(3)
        node2 = TreeNode(6)
        node3 = TreeNode(2)
        node4 = TreeNode(4)
        node5 = TreeNode(1)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node3.left = node5

        p = node5
        q = node1
        output = root
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q), output)

    def test_2(self):
        root = TreeNode(2)
        node1 = TreeNode(1)

        root.left = node1

        p = TreeNode(2)
        q = TreeNode(1)
        output = root
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q), output)


if __name__ == '__main__':
    main()
