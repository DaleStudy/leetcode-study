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
