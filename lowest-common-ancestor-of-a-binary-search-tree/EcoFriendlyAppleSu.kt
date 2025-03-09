package leetcode_study

/**
 * Binary Search Tree에서 가장 근접한 공통 조상을 찾는 문제
 * BST의 성질인 부모 노드보다 작은 값은 왼쪽 부모 노드보다 큰 값은 오른쪽에 위치함을 사용해 문제 해결
 *
 * 시간 복잡도: O(n) or O(logn)
 * -> balanced BST의 경우 조회 구간이 절반으로 줄기 때문에 O(logn)의 시간 복잡도를 갖지만 편향될 경우 O(n)의 시간 복잡도를 가짐.
 *
 * 공간 복잡도: O(1)
 * -> 반복문을 사용하여 추가 메모리를 사용하지 않음
 */
fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    var currentNode = root

    while (currentNode != null) {
        when {
            p?.`val`!! < currentNode.`val` && q?.`val`!! < currentNode.`val` -> currentNode = currentNode.left
            p?.`val`!! > currentNode.`val` && q?.`val`!! > currentNode.`val` -> currentNode = currentNode.right
            else -> return currentNode
        }
    }
    return null
}
