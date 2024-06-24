/**
 * time: O(N)
 * space: O(1)
 */
class Solution {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int sz = 0;
        ListNode current = head;

        while (current != null) {
            current = current.next;
            sz++;
        }

        if (sz == n) {
            return head.next;
        }

        int removedIndex = sz - n;
        current = head;
        for (int i = 0; i < removedIndex-1; i++) {
            current = current.next;
        }
        current.next = current.next.next;
        return head;
    }
}
