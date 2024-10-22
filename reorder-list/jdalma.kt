package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `reorder-list` {

    fun reorderList(root: ListNode?) {
        if (root == null) return
        usingTwoPointers(root)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingStack(input: ListNode) {
        val tail = ArrayDeque<ListNode>().apply {
            var node: ListNode? = input
            while (node != null) {
                this.add(node)
                node = node.next
            }
        }

        val dummy = ListNode(-1)
        var node: ListNode = dummy
        var head: ListNode = input
        for (i in 0 until tail.size) {
            if (i % 2 != 0) {
                node.next = tail.removeLast()
            } else {
                node.next = head
                head.next?.let { head = it }
            }
            node.next?.let { node = it }
        }
        node.next = null
    }

    /**
     * TC: O(n), SC: O(1)
     */
    private fun usingTwoPointers(input: ListNode) {
        if (input.next == null) return

        var slow: ListNode? = input
        var fast: ListNode? = input
        while (fast?.next != null && fast.next?.next != null) {
            slow = slow?.next
            fast = fast.next?.next
        }

        val firstHalfEnd = slow
        var secondHalfStart = slow?.next
        firstHalfEnd?.next = null

        secondHalfStart = reverse(secondHalfStart)

        var node1: ListNode? = input
        var node2: ListNode? = secondHalfStart
        while (node2 != null) {
            val (next1, next2) = (node1?.next to node2?.next)
            node1?.next = node2
            node2.next = next1
            node1 = next1
            node2 = next2
        }
    }

    private fun reverse(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var current = head
        while (current != null) {
            val next = current.next
            current.next = prev
            prev = current
            current = next
        }
        return prev
    }

    @Test
    fun `정렬된 리스트 노드의 참조 체이닝을 특정 순서로 재정렬한다`() {
        val actual = ListNode.of(1,2,3,4,5).apply {
            reorderList(this)
        }
        actual.`val` shouldBe 1
        actual.next!!.`val` shouldBe 5
        actual.next!!.next!!.`val` shouldBe 2
        actual.next!!.next!!.next!!.`val` shouldBe 4
        actual.next!!.next!!.next!!.next!!.`val` shouldBe 3
        actual.next!!.next!!.next!!.next!!.next shouldBe null

        ListNode.of(1,2,3,4,5,6).apply {
            reorderList(this)
        }
    }
}
