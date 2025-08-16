// 시간 복잡도: O(n + m) 
//   - n: list1의 길이, m: list2의 길이
//   - 두 리스트를 한 번씩만 순회하며 병합하므로 O(n + m)
//
// 공간 복잡도: O(1)
//   - 주어진 노드들을 재사용하여 병합하고, 추가로 더미 노드(dummy) 하나만 사용
//   - 재귀 호출 없이 포인터만 이동하므로 상수 공간만 필요

class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        val dummy = ListNode(0)
        var current = dummy

        var p1 = list1
        var p2 = list2

        while (p1 != null && p2 != null) {
            if (p1.`val` >= p2.`val`) {
                current.next = p2
                p2 = p2.next
            } else {
                current.next = p1
                p1 = p1.next
            }

            current = current.next!!
        }

        current.next = p1 ?: p2

        return dummy.next
    }
}
