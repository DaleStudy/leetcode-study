class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class InvertBinaryTree {
    fun invertTree(root: TreeNode?): TreeNode? {
        // 이진 트리의 root 를 주면, 트리를 뒤집고, 그것의 Root를 반환해라
        // 재귀적으로 left, right 를 바꾸면 된다. child가 둘다 null 이면 종료
        // 시간복잡도: O(N), 공간복잡도: O(1)
        if (root == null) return null

        if (root.left == null && root.right == null) {
            return root
        }

        val temp = root.left
        root.left = root.right
        root.right = temp

        invertTree(root.left)
        invertTree(root.right)

        return root
    }

}
