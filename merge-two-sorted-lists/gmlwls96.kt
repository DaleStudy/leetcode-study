/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    // 시간, 공간 : o(n+m),
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var currentList1: ListNode? = list1
        var currentList2: ListNode? = list2
        val answerList = LinkedList<Int>()
        while (currentList1 != null || currentList2 != null) {
            when {
                currentList1 == null -> {
                    answerList.offer(currentList2!!.`val`)
                    currentList2 = currentList2.next
                }
                currentList2 == null -> {
                    answerList.offer(currentList1.`val`)
                    currentList1 = currentList1.next
                }
                currentList1.`val` <= currentList2.`val` -> {
                    answerList.offer(currentList1.`val`)
                    currentList1 = currentList1.next
                }
                currentList2.`val` < currentList1.`val` -> {
                    answerList.offer(currentList2.`val`)
                    currentList2 = currentList2.next
                }
            }
        }
        var answer: ListNode? = null
        var currentAnswer: ListNode? = null
        while (answerList.isNotEmpty()) {
            val num = answerList.poll()
            if (answer == null) {
                answer = ListNode(num)
                currentAnswer = answer
            } else {
                currentAnswer?.next = ListNode(num)
                currentAnswer = currentAnswer?.next
            }
        }
        return answer
    }
}
