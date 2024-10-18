package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.lang.RuntimeException

class `merge-k-sorted-lists` {

    data class ListNode(var `val`: Int) {
        var next: ListNode? = null

        companion object {
            fun of(vararg `val`: Int): ListNode {
                val dummy = ListNode(-1)
                var prev = dummy
                for (v in `val`) {
                    prev.next = ListNode(v)
                    prev = prev.next ?: throw RuntimeException()
                }
                return dummy.next ?: throw RuntimeException()
            }
        }
    }

    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        return if (lists.isEmpty()) null
        else if (lists.size == 1) lists.first()
        else mergeDivideAndConquer(lists)
    }

    /**
     * TC: O(lists.size * ListNode.size), SC: O(1)
     */
    private fun usingBruteForce(lists: Array<ListNode?>): ListNode? {
        val dummy = ListNode(-1)
        var prev = dummy

        while (true) {
            var minNode: ListNode? = null
            var minIndex = -1

            for (index in lists.indices) {
                val curr = lists[index] ?: continue
                if (minNode == null || curr.`val` < minNode.`val`) {
                    minNode = curr
                    minIndex = index
                }
            }
            prev.next = minNode ?: break
            prev = prev.next ?: throw RuntimeException()

            lists[minIndex] = minNode.next
        }

        return dummy.next
    }

    /**
     * TC: O(lists.size * ListNode.size), SC: O(1)
     */
    private fun mergeLists(lists: Array<ListNode?>): ListNode? {
        fun merge(node1: ListNode?, node2: ListNode?): ListNode? {
            val dummy = ListNode(-1)
            var prev = dummy
            var (n1, n2) = node1 to node2
            while (n1 != null && n2 != null) {
                if (n1.`val` < n2.`val`) {
                    prev.next = n1
                    n1 = n1.next
                } else {
                    prev.next = n2
                    n2 = n2.next
                }
                prev.next?.let { prev = it }
            }
            prev.next = n1 ?: n2
            return dummy.next
        }
        for (index in 1 until lists.size) {
            lists[0] = merge(lists[0], lists[index])
        }
        return lists[0]
    }

    /**
     * TC: O(lists.size * ListNode.size), SC: O(lists.size)
     */
    private fun mergeDivideAndConquer(lists: Array<ListNode?>): ListNode? {
        fun merge(node1: ListNode?, node2: ListNode?): ListNode? {
            val dummy = ListNode(-1)
            var prev = dummy
            var (n1, n2) = node1 to node2
            while (n1 != null && n2 != null) {
                if (n1.`val` < n2.`val`) {
                    prev.next = n1
                    n1 = n1.next
                } else {
                    prev.next = n2
                    n2 = n2.next
                }
                prev.next?.let { prev = it }
            }
            prev.next = n1 ?: n2
            return dummy.next
        }

        fun divideAndConquer(lists: Array<ListNode?>, s: Int, e: Int): ListNode? {
            if (s > e) return null
            else if (s == e) return lists[s]

            val mid = (s + e) / 2
            val left = divideAndConquer(lists, s, mid)
            val right = divideAndConquer(lists, mid + 1, e)
            return merge(left, right)
        }

        return divideAndConquer(lists, 0, lists.size - 1)
    }

    @Test
    fun `전달받은 노드들을 정렬하고 병합된 결과를 반환한다`() {
        mergeKLists(
            arrayOf(
                ListNode.of(1,4,5),
                ListNode.of(1,3,4),
                ListNode.of(2,6)
            )
        ) shouldBe ListNode.of(1,1,2,3,4,4,5,6)
    }
}
