package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `reverse-linked-list` {

    /**
     * TC : O(n), SC: O(1)
     */
    fun reverseList(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var next: ListNode? = null
        var curr: ListNode? = head

        while (curr != null) {
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        }

        return prev
    }

    @Test
    fun `입력 받은 단일 리스트를 반전하고 반전한 목록을 반환한다`() {
        reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
            shouldBe(ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))
    }
}

class ListNode(
    var `val`: Int,
    var next: ListNode? = null
)
