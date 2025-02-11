package leetcode_study

/*
* binary tree 좌우 번경 문제
* 재귀를 통해 문제 해결
* 시간 복잡도: O(n)
* -> n개의 노드를 한 번씩 방문
* 공간 복잡도: O(n) 혹은 O(log n)
* -> 재귀 사용 시 스택에 쌓임
* -> 균형잡힌 binary tree의 경우 O(log n)의 공간이 필요하고 그렇지 않은 경우(최악의 경우) O(n)의 공간 복잡도 요구
* */
fun invertTree(root: TreeNode?): TreeNode? {
    recursiveNode(root)
    return root
}

fun recursiveNode(parentNode: TreeNode?) {
    if (parentNode == null) return

    swapNode(parentNode) // 현재 노드의 left와 right를 교환
    recursiveNode(parentNode.left)  // 왼쪽 서브트리 탐색
    recursiveNode(parentNode.right) // 오른쪽 서브트리 탐색
}

fun swapNode(parentNode: TreeNode?) {
    if (parentNode == null) return

    val temp = parentNode.left
    parentNode.left = parentNode.right
    parentNode.right = temp
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}
