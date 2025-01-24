class Solution {
    // 시간 : O(N), 공간 : O(1)
    // head를 조회하며 새로운 answerRoot에 새로운 ListNode를 생성하고 꼬리에 현재 answerRoot를 넣는다.
    fun reverseList(head: ListNode?): ListNode? {
        var currentHead = head
        var answerRoot: ListNode? = null

        while (currentHead != null) {
            answerRoot = ListNode(currentHead.`val`).apply { next = answerRoot }
            currentHead = currentHead.next
        }
        return answerRoot
    }
}
