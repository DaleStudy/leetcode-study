# 7기 풀이
class Solution:
    # 풀이 1 - BFS
    # 시간 복잡도: O(n)
    # - 노드의 개수(n)만큼 모두 탐색하므로 
    # 공간 복잡도: O(w)
    # - 최악은 한 레벨의 최대 노드 수(w)만큼 queue에 쌓임
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        nodes = deque()
        if root:
            nodes.appendleft(root)

        while nodes:
            childs = deque()
            sibling_vals = []
            while nodes:
                node = nodes.pop()
                if not node:
                    continue

                sibling_vals.append(node.val)
                if node.left:
                    childs.appendleft(node.left)
                if node.right:
                    childs.appendleft(node.right)

            res.append(sibling_vals)
            nodes = childs
        
        return res

    # 풀이 2 - DFS
    # 시간 복잡도: O(n)
    # - 노드의 개수(n)만큼 모두 탐색하므로 
    # 공간 복잡도: O(h)
    # - 재귀 스택이 최대 나무의 높이(h)만큼 쌓임
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return res
