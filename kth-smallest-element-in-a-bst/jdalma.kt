package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test
import java.util.PriorityQueue

class `kth-smallest-element-in-a-bst` {

    fun kthSmallest(root: TreeNode?, k: Int): Int {
        return inorderTraversal(root, k)
    }

    // 1. 재귀 호출로 모든 트리를 조회 후 정렬
    // 시간복잡도: O(n * log(n)), 공간복잡도: O(n)
    private fun recursionAndSort(root: TreeNode?, k: Int) = mutableSetOf<Int>().apply {
        dfs(root, this)
    }.sorted()[k - 1]

    private fun dfs(node: TreeNode?, set: MutableSet<Int>) {
        if (node == null) return

        set.add(node.`val`)
        dfs(node.left, set)
        dfs(node.right, set)
    }

    // 2. 재귀 호출로 모든 트리의 값을 우선순위 큐에 삽입하고 작은 값으로 계속 큐를 갱신
    // 시간복잡도: O(n * log(k)), 공간복잡도: O(n + k)
    // 트리 순회 : O(n), 우선순위 큐 삽입: O(log k)
    private fun usingPriorityQueue(node: TreeNode?, k: Int): Int {
        fun dfs(node: TreeNode, k: Int, pq: PriorityQueue<Int>) {
            pq.offer(node.`val`)

            if (pq.size > k) {
                pq.poll()
            }
            if (node.left != null) {
                dfs(node.left!!, k, pq)
            }
            if (node.right != null) {
                dfs(node.right!!, k, pq)
            }
        }

        val pq = PriorityQueue { v1: Int, v2: Int -> v2 - v1 }
        dfs(node!!, k, pq)
        return pq.first()
    }

    // 3. 문제의 전제가 이진탐색트리이기에, 중위순회로 탐색하여 값을 누적하면 오름차순의 값이 된다.
    // 시간복잡도: O(n), 공간복잡도: O(n)
    private fun inorderTraversal(node: TreeNode?, k: Int): Int {
        fun dfs(node: TreeNode, k: Int, list: MutableList<Int>) {
            if (node.left != null) {
                dfs(node.left!!, k, list)
            }
            list.add(node.`val`)
            if (node.right != null) {
                dfs(node.right!!, k, list)
            }
        }

        return mutableListOf<Int>().apply {
            dfs(node!!, k, this)
        }[k - 1]
    }

    @Test
    fun `루트와 정수 k가 주어지면 트리에 있는 모든 노드의 값 중 가장 작은 값을 반환한다`() {
        kthSmallest(TreeNode.of(listOf(0, 3,1,4,null,2)), 1) shouldBeEqual 1
        kthSmallest(TreeNode.of(listOf(0, 5,3,6,2,4,null,null,1)), 3) shouldBeEqual 3
    }
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null

    companion object {
        fun of(numbers: List<Int?>): TreeNode? {
            fun setChild(node: TreeNode?, nums: List<Int?>, index: Int): TreeNode? {
                if (node == null) return null
                val (leftIndex, rightIndex) = index * 2 to index * 2 + 1

                if (leftIndex < nums.size && nums[leftIndex] != null) {
                    node.left = TreeNode(nums[leftIndex]!!)
                    setChild(node.left, nums, leftIndex)
                }
                if (rightIndex < nums.size && nums[rightIndex] != null) {
                    node.right = TreeNode(nums[rightIndex]!!)
                    setChild(node.right, nums, rightIndex)
                }
                return node
            }
            return setChild(TreeNode(numbers[1]!!), numbers, 1)
        }
    }
}
