package leetcode_study

import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 105. Construct Binary Tree from Preorder and Inorder Traversal
 * Medium
 *
 * preorder, inorder, postorder는 트리 탐색 방식
 * preorder(전위): root -> left -> right 순으로 탐색.
 * inorder(중위): left -> root -> right 순으로 탐색.
 * postorder(후위): left -> right -> root 순으로 탐색.
 */
class ConstructBinaryTreeFromPreorderAndInorderTraversal {
    /**
     * Runtime: 38 ms(Beats: 25.41 %)
     * Time Complexity: O(n^2)
     *   - 매 재귀 호출마다 for문이 진행
     *
     * Memory: 86.98 MB(Beats: 9.77 %)
     * Space Complexity: O(n)
     *   - sliceArray() 메서드로 새로운 배열 생성
     */
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        val root = TreeNode(preorder[0])
        if (preorder.size == 1) {
            return root
        }
        var rootIndex = 0
        for (i in inorder.indices) {
            if (inorder[i] == root.`val`) {
                rootIndex = i
                break
            }
        }
        if (rootIndex != 0) {
            root.left = buildTree(preorder.sliceArray(1..rootIndex), inorder.sliceArray(0 until rootIndex))
        }
        if (rootIndex != inorder.lastIndex) {
            root.right = buildTree(
                preorder.sliceArray(rootIndex + 1..preorder.lastIndex),
                inorder.sliceArray(rootIndex + 1..inorder.lastIndex)
            )
        }
        return root
    }

    /**
     * sliceArray로 배열을 만들어 내지 않고, index를 전달하여 공간 복잡도를 O(h)로 감소시킴
     *   - O(h): 재귀 호출 스택에 필요한 공간
     * Runtime: 24 ms(Beats: 55.17 %)
     * Time Complexity: O(n^2)
     *   - 모든 노드에 대해서 O(n)의 검색
     *
     * Memory: 39.72 MB(Beats: 40.18 %)
     * Space Complexity: O(h)
     *   - 균형 잡힌 트리의 경우: O(log n)
     *   - 편향 트리의 경우: O(n)
     */
    fun buildTree2(preorder: IntArray, inorder: IntArray): TreeNode? {
        return buildTreeWithIndex(
            preorder, inorder,
            preStart = 0, preEnd = preorder.lastIndex,
            inStart = 0, inEnd = inorder.lastIndex
        )
    }

    private fun buildTreeWithIndex(
        preorder: IntArray, inorder: IntArray,
        preStart: Int, preEnd: Int,
        inStart: Int, inEnd: Int
    ): TreeNode? {
        // 유효하지 않은 범위인 경우
        if (preStart > preEnd || inStart > inEnd) {
            return null
        }

        // 루트 노드 생성
        val root = TreeNode(preorder[preStart])

        // 단일 노드인 경우
        if (preStart == preEnd) {
            return root
        }

        // 중위 순회에서 루트의 위치 찾기
        var rootIndex = inStart
        while (inorder[rootIndex] != root.`val`) {
            rootIndex++
        }

        // 왼쪽 서브트리의 크기
        val leftSubtreeSize = rootIndex - inStart

        // 왼쪽 서브트리 구성
        root.left = buildTreeWithIndex(
            preorder, inorder,
            preStart = preStart + 1,
            preEnd = preStart + leftSubtreeSize,
            inStart = inStart,
            inEnd = rootIndex - 1
        )

        // 오른쪽 서브트리 구성
        root.right = buildTreeWithIndex(
            preorder, inorder,
            preStart = preStart + leftSubtreeSize + 1,
            preEnd = preEnd,
            inStart = rootIndex + 1,
            inEnd = inEnd
        )

        return root
    }

    /**
     * 매 번 루트 값을 찾는 선형 검색을 O(1)로 만들기 위해 HashMap 사용
     * Runtime: 21 ms(Beats: 57.14 %)
     * Time Complexity: O(n)
     *
     * Memory: 38.62 MB(Beats: 56.62 %)
     * Space Complexity: O(n)
     *   - HashMap
     */
    private lateinit var inorderMap: MutableMap<Int, Int>

    fun buildTree3(preorder: IntArray, inorder: IntArray): TreeNode? {
        // 중위 순회 값들의 인덱스를 HashMap에 저장
        inorderMap = mutableMapOf()
        for (i in inorder.indices) {
            inorderMap[inorder[i]] = i
        }

        return buildTreeWithIndex2(
            preorder, inorder,
            preStart = 0, preEnd = preorder.lastIndex,
            inStart = 0, inEnd = inorder.lastIndex
        )
    }

    private fun buildTreeWithIndex2(
        preorder: IntArray, inorder: IntArray,
        preStart: Int, preEnd: Int,
        inStart: Int, inEnd: Int
    ): TreeNode? {
        // 유효하지 않은 범위인 경우
        if (preStart > preEnd || inStart > inEnd) {
            return null
        }

        // 루트 노드 생성
        val root = TreeNode(preorder[preStart])

        // 단일 노드인 경우
        if (preStart == preEnd) {
            return root
        }

        // HashMap을 사용하여 O(1)로 루트의 위치 찾기
        val rootIndex = inorderMap[root.`val`]!!

        // 왼쪽 서브트리의 크기
        val leftSubtreeSize = rootIndex - inStart

        // 왼쪽 서브트리 구성
        root.left = buildTreeWithIndex2(
            preorder, inorder,
            preStart = preStart + 1,
            preEnd = preStart + leftSubtreeSize,
            inStart = inStart,
            inEnd = rootIndex - 1
        )

        // 오른쪽 서브트리 구성
        root.right = buildTreeWithIndex2(
            preorder, inorder,
            preStart = preStart + leftSubtreeSize + 1,
            preEnd = preEnd,
            inStart = rootIndex + 1,
            inEnd = inEnd
        )

        return root
    }

    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }

    @Test
    fun test() {
        printTree(buildTree(intArrayOf(3, 9, 20, 15, 7), intArrayOf(9, 3, 15, 20, 7))!!)
    }

    // preorder로 출력
    fun printTree(root: TreeNode) {
        println(root.`val`)
        if (root.left != null) {
            printTree(root.left!!)
        }
        if (root.right != null) {
            printTree(root.right!!)
        }
    }
}
/**
 * 기타
 *
 * Runtime이 1ms인 풀이. 아름다워서 공유합니당..
 *
 * private var preIdx = 0
 * private var inIdx = 0
 *
 * fun buildTree4(preorder: IntArray, inorder: IntArray): TreeNode? {
 *     return dfs(preorder, inorder, Int.MAX_VALUE)
 * }
 *
 * fun dfs(preorder: IntArray, inorder: IntArray, limit: Int): TreeNode? {
 *     if (preIdx >= preorder.size) {
 *         return null
 *     }
 *     if (inorder[inIdx] == limit) {
 *         inIdx++
 *         return null
 *     }
 *
 *     val root = TreeNode(preorder[preIdx])
 *     preIdx++
 *
 *     root.left = dfs(preorder, inorder, root.`val`)
 *     root.right = dfs(preorder, inorder, limit)
 *
 *     return root
 * }
 */
