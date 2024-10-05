package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `merge-two-sorted-lists` {

    data class ListNode(
        var `val`: Int,
        var next: ListNode? = null
    )

    /**
     * TC: O(n + m), SC: O(1)
     */
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var (l1, l2) = list1 to list2
        var current = ListNode(-1)
        val result: ListNode = current

        while (l1 != null && l2 != null) {
            if (l1.`val` < l2.`val`) {
                current.next = l1
                l1 = l1.next
            } else {
                current.next = l2
                l2 = l2.next
            }
            current.next?.let { current = it }
        }

        if (l1 != null) current.next = l1
        if (l2 != null) current.next = l2

        return result.next
    }

    @Test
    fun `두 개의 리스트 노드를 정렬하여 병합한다`() {
        mergeTwoLists(
            ListNode(1,ListNode(2,ListNode(4))),
            ListNode(1,ListNode(3,ListNode(4)))
        ) shouldBe ListNode(1,ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    }
}
