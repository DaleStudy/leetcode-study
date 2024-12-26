package leetcode_study

/**
 * 전위 순회, 중위 순회를 통한 원본 Binary Tree를 구하는 문제
 *
 * 전위 순회 탐색 순서 : 루트 -> 왼쪽 서브 트리 -> 오른쪽 서브 트리
 * 중위 순회 탐색 순서 : 왼쪽 서브 트리 -> 루트 -> 오른쪽 서브 트리
 * 탐색은 동일한 Binary Tree를 두고 진행되기 때문에 배열의 길이는 같습니다.
 *
 * 시간 복잡도: O(n^2)
 * -> Ary RootNode Index 를 찾는 과정: O(n)
 * -> 재귀 안에서 RootNode Index 를 찾는 과정: O(n)
 * --> 두 계의 과정은 별도로 존재하는 것이 아닌 내부적으로 일어나기 때문에 O(n) * O(n). 즉, O(n^2)의 시간 복잡도가 소요됨
 *
 * 공간 복잡도: O(n) or O(logn)
 * -> 재귀를 통할 때마다 배열이 새로 생성. 각 노드에 대해 배열이 나뉘므로 O(n)의 공간 복잡도를 가짐
 * -> 만약 Binary Tree가 한 쪽으로 치우지지 않은 Balanced Binary Tree라면 O(logn)의 공간 복잡도를 가짐.
 */
fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
    if (preorder.isEmpty() || inorder.isEmpty()) return null

    // 왼쪽 오른쪽 분류의 기준이 되는 rootValue를 구하는 과정
    val rootValue = preorder[0]
    val rootNode = TreeNode(rootValue)

    // root를 기준으로 왼쪽, 오른쪽 subTree를 구성
    val pivotValue = inorder.indexOf(rootValue)
    val leftInOrder = inorder.slice(0 until pivotValue)
    val rightInOrder = inorder.slice(pivotValue + 1 until inorder.size)

    // 왼쪽, 오른쪽 subTree를 기준으로 leftPreOrder, rightPreOrder 구성
    val leftPreOrder = preorder.slice(1 until leftInOrder.size + 1)
    val rightPreOrder = preorder.slice(leftInOrder.size + 1 until preorder.size)

    // 재귀를 통한 subTree 생성
    rootNode.left = buildTree(leftPreOrder.toIntArray(), leftInOrder.toIntArray())
    rootNode.right = buildTree(rightPreOrder.toIntArray(), rightInOrder.toIntArray())

    return rootNode
}

class TreeNode(val value: Int, ) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}
