package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `remove-nth-node-from-end-of-list` {

    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        if (head == null || (head.next == null && n == 1)) {
            return null
        }
        return usingTwoPointers(head, n)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingExtraList(head: ListNode, n: Int): ListNode {

        fun toList(node: ListNode): List<ListNode> {
            val list = mutableListOf<ListNode>()
            var tmp: ListNode? = node
            while (tmp != null) {
                list.add(tmp)
                tmp = tmp.next
            }
            return list
        }

        val list = toList(head)
        var root = head
        if (list.size == n) {
            root = list[1]
        } else {
            list[list.size - n - 1].next = list[list.size - n].next
        }
        return root
    }

    /**
     * fast를 n만큼 먼저 이동 시킨 후 fast.next가 null일 때까지 fast와 slow를 다음 노드로 이동시킨다.
     * fast를 n만큼 이동시키면 결국 slow는 n의 이전 노드에 도달하게 되기에 해당 slow 노드의 next를 변경하면 된다.
     * TC: O(n), SC: O(1)
     */
    private fun usingTwoPointers(head: ListNode, n: Int): ListNode? {
        var fast: ListNode? = head
        var slow: ListNode? = head

        repeat(n) {
            fast = fast?.next
        }
        if (fast == null) return head.next

        while (fast?.next != null) {
            fast = fast?.next
            slow = slow?.next
        }
        slow?.next = slow?.next?.next
        return head
    }

    @Test
    fun `링크된 목록의 헤드가 주어지면 목록의 끝에서 n번째 노드를 제거하고 그 헤드를 반환합니다`() {
        removeNthFromEnd(ListNode.of(1), 1).also {
            it shouldBe null
        }

        removeNthFromEnd(ListNode.of(1, 2), 2).also {
            it shouldBe ListNode(2)
        }

        removeNthFromEnd(ListNode.of(1, 2), 1)!!.also {
            it shouldBe ListNode(1)
            it.next shouldBe null
        }

        removeNthFromEnd(ListNode.of(1, 2, 3, 4, 5), 2)!!.also {
            it.next!!.next!!.`val` shouldBe 3
            it.next!!.next!!.next!!.`val` shouldBe 5
        }
    }
}
