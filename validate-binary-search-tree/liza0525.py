class Solution:
    # 중위 순회를 한 결과를 리스트에 저장한 후, 그 결과 리스트 내 value들이 정렬이 되어 있는지 확인
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_result_list = []
        
        def inorder_tree(tree_node):
            if tree_node.left:
                inorder_tree(tree_node.left)

            inorder_result_list.append(tree_node.val)

            if tree_node.right:
                inorder_tree(tree_node.right)

        inorder_tree(root)

        for i in range(len(inorder_result_list) - 1):
            # i + 1 인덱스 값보다 i + 1 인덱스의 값이 커야 한다. 아니면 False
            if inorder_result_list[i] >= inorder_result_list[i + 1]:
                return False
        
        return True


# 7기 풀이
# 시간 복잡도: O(n)
#  - 전체 트리 노드를 탐색하기 때문에 n
# 공간 복잡도: O(n)
#  - 노드를 저장하는 리스트는 n의 길이만큼 생김
class Solution:
    # 중위 순회 결과가 strictly increasing인지 확인하는 방식
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree_res = []

        def inorder_search(node):
            if node.left:
                inorder_search(node.left)

            tree_res.append(node.val)
            
            if node.right:
                inorder_search(node.right)
        
        inorder_search(root)

        for i in range(len(tree_res) - 1):
            # i번째 값이 i + 1번째 값보다 크거나 같으면 strictly increasing하지 않다는 의미이므로 False를 리턴한다.
            if tree_res[i] >= tree_res[i + 1]:
                return False
        return True
