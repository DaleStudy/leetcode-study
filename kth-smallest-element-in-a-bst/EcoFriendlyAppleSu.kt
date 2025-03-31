package leetcode_study

/**
 * binary search tree에서 k 번째 작은 수를 반환하는 문제
 * stack 자료구조를 사용해 중위 순회를 구현합니다.
 * 
 * 시간 복잡도: O(n) or O(logn)
 * -> 2번의 loop을 순회하기 때문에 O(n^2)의 시간 복잡도로 판단할 수 있지만 제한된 n 안에서 순회를 진행하기 때문에 O(n)을 넘지 않습니다.
 * -> 만약 BST가 균형이 잡혀 있다면 O(logn)의 시간 복잡도를 갖습니다.
 * 
 * 공간 복잡도: O(n)
 * -> 탐색한 node를 저장할 stack 공간
 */
fun kthSmallest(root: TreeNode?, k: Int): Int {
    val stack = ArrayDeque<TreeNode>()
    var current = root
    var count = 0

    while (stack.isNotEmpty() || current != null) {
        // 왼쪽 자식 노드들을 계속 탐색하여 stack에 추가
        while (current != null) {
            stack.addLast(current)
            current = current.left
        }

        // 가장 왼쪽 노드를 pop
        current = stack.removeLast()
        count++

        // k번째 노드라면 값 반환
        if (count == k) return current.`val`

        // 오른쪽 서브트리 탐색
        current = current.right
    }

    return -1  // 이론적으로 도달할 수 없는 부분
}
