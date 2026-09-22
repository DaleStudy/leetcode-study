"""
시간 복잡도 : O(n)
공간 복잡도 : O(n)

재귀적으로 두 이진 트리의 노드를 비교하면서 값이 같은지 확인한다.
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 두 노드가 둘다 None 이면 True 를 반환한다.
        if p is q:
            return True

        # 두 노드중 하나가 None 이면 False 를 반환한다.
        if not (p and q):
            return False

        # 둘다 None이 아니라면 값을 비교하고 왼쪽과 오른쪽 서브트리도 재귀적으로 비교한다.
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
