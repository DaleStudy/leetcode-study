class Solution {
    // 시간 : O(n)
    // 세트에 head.val 값을 추가하면서 동일한 값이 있는지 체크. 동일한 값이 존재하면 순회한다고 판단.
    fun hasCycle(head: ListNode?): Boolean {
        val set = mutableSetOf<Int>()
        var next = head
        while (next != null) {
            if (set.contains(next.`val`)) {
                return true
            }
            set.add(next.`val`)
            next = next.next
        }
        return false
    }
}
