package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `linked-list-cycle` {

    data class ListNode(var `val`: Int) {
        var next: ListNode? = null
    }

    /**
     * TC: O(n), SC: O(1)
     */
    fun hasCycle(head: ListNode?): Boolean {
        if (head == null) return false

        var slow = head
        var fast = head

        while (fast?.next != null) {
            slow = slow?.next
            fast = fast.next?.next

            if (slow == fast) return true
        }

        return false
    }

    @Test
    fun `입력받은 노드에 사이클이 존재한다면 참을 반환한다`() {
        val three = ListNode(3)
        val two = ListNode(2)
        val zero = ListNode(0)
        val four = ListNode(4)

        three.next = two
        two.next = zero
        zero.next = four
        four.next = two

        hasCycle(three) shouldBe true
    }
}
