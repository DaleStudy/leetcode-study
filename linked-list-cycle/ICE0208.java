class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        // fast가 끝에 도달하면 cycle이 없다.
        while (fast != null && fast.next != null) {
            slow = slow.next;           // 한 칸 이동
            fast = fast.next.next;      // 두 칸 이동

            // cycle이 있다면 두 포인터는 결국 같은 노드에서 만난다.
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}
