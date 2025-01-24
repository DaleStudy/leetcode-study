package leetcode_study

/**
 * 첫번째 문제풀이
 * 시간복잡도 : O(n)
 * - n 번을 순회하며 nodes 에 저장하고, 다시 nodes 에서 노드를 하나씩 꺼내어 연산하므로 O(2n) -> O(n) 입니다.
 * 공간복잡도 : O(n)
 * - n 개의 노드를 nodes 에 저장하므로 O(n) 입니다.
 *
 * 두번째 문제풀이
 * 시간복잡도 : O(n)
 * - curr 이 null 일때까지 while 문을 돌고 있으므로, n번의 순회가 발생할 것입니다. 따라서 시간복잡도는 O(n) 입니다.
 * 공간복잡도 : O(1)
 * - nodes 를 저장했던 첫번째 풀이와 달리 prev, curr 두개의 상수만을 사용하므로 O(1) 만큼의 공간복잡도를 가집니다.
 * */
class ReverseLinkedList {
    class ListNode(var `val`: Int) {
        var next: ListNode? = null
    }

    fun reverseList(head: ListNode?): ListNode? {
        var nowNode = head
        val nodes = mutableListOf<ListNode>()

        while (nowNode != null) {
            nodes.add(nowNode)
            nowNode = nowNode.next
        }

        val dummy = ListNode(-1)
        nowNode = dummy

        while (nodes.isNotEmpty()) {
            val popNode = nodes.removeLast()
            nowNode?.next = popNode
            nowNode = nowNode?.next
        }

        nowNode?.next = null

        return dummy.next
    }
}

class ReverseLinkedList2 {
    class ListNode(var `val`: Int) {
        var next: ListNode? = null
    }

    fun reverseList(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var curr = head

        while (curr != null) {
            val temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        }

        return prev
    }
}
