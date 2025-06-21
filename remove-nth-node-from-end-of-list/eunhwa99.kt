package leetcode_study

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

// 힌트 참고
// Time Complexity: O(L) where L is the length of the linked list
// Space Complexity: O(1) since we are using only a constant amount of space
class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        var left = head
        var right = head
        var step = n
        while (step-- > 0) {
            right = right?.next
        }
        if (right == null) {
            return head?.next // n이 리스트의 길이와 같을 때, 즉 첫 번째 노드를 제거해야 하는 경우
        }
        while (right?.next != null) {
            left = left?.next
            right = right.next
        }

        left?.next = left?.next?.next
        return head
    }
}


