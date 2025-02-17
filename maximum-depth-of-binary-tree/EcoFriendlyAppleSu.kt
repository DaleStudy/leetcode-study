package leetcode_study

/*
* 이진 트리의 최대 깊이를 구하는 문제
* 재귀를 사용해 문제 해결
* 시간 복잡도: O(n)
* -> 이진 트리의 모든 노드를 방문
* 공간 복잡도: O(n) 혹은 O(log n)
* -> findDepth() 함수는 재귀적으로 호출되어 콜 스택에 쌓임
*     -> 균형잡힌 이진트리의 경우 재귀의 깊이는 O(log n) 소요
*     -> 편향된 이진트리의 경우 재귀의 깊이는 O(n) 소요
* */
fun maxDepth(root: TreeNode?): Int {
    if (root == null) return 0
    val maxValue = findDepth(root, 1) // 시작 깊이 값은 `1`
    return maxValue
}

fun findDepth(currentNode: TreeNode?, depth: Int): Int{
    // escape condition
    if (currentNode == null) {
        return depth - 1
    }

    val leftValue = findDepth(currentNode.left, depth + 1)
    val rightValue = findDepth(currentNode.right, depth + 1)
    return maxOf(leftValue, rightValue)
}
