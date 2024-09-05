func indexOf(slice []int, value int) int {
    for i, v := range slice {
        if v == value {
            return i
        }
    }
    return -1
}

func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 || len(inorder) == 0 {
        return nil
    }

    // Preorder의 처음 값으로 root을 만듬
    rootVal := preorder[0]
    root := &TreeNode{Val: rootVal}

    // inorder에서 root의 위치를 찾음
    mid := indexOf(inorder, rootVal)

    // inorder에서 mid의 왼쪽은 left subtree이고 오른쪽은 right subtree이다.
    leftInorder := inorder[:mid]
    rightInorder := inorder[mid+1:]

    // left preorder를 계산한다.
    leftPreorder := preorder[1 : len(leftInorder)+1]
    // right preorder를 계산한다.
    rightPreorder := preorder[len(leftInorder)+1:]

    // tree 만들기
    root.Left = buildTree(leftPreorder, leftInorder)
    root.Right = buildTree(rightPreorder, rightInorder)

    return root
}
