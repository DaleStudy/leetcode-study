/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

/**
 * TC: O(n)
 * SC: O(n)
 */
class Solution1 {
    fun hasCycle(head: ListNode?): Boolean {
        val visited = mutableSetOf<ListNode>()
        var current = head

        while (current != null) {
            if (current in visited) return true
            visited.add(current)
            current = current.next
        }
        return false
    }
}

/**
 * TC: O(n)
 * SC: O(1)
 */
class Solution2 {
    fun hasCycle(head: ListNode?): Boolean {
        var slow = head
        var fast = head?.next?.next

        while (fast != null) {
            if (slow == fast) return true
            slow = slow?.next
            fast = fast?.next?.next
        }
        return false
    }
}
