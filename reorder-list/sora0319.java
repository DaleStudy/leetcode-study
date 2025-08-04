public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        ListNode backward = head;
        ListNode forward = head;
        while (forward != null && forward.next != null) {
            backward = backward.next;
            forward = forward.next.next;
        }

        ListNode curr = backward.next;
        backward.next = null;

        ListNode prev = null;
        while (curr != null) {
            ListNode tempNext = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tempNext;
        }

        ListNode first = head;
        ListNode second = prev;

        while (second != null) {
            ListNode firstNext = first.next;
            ListNode secondNext = second.next;

            first.next = second;
            second.next = firstNext;

            first = firstNext;
            second = secondNext;
        }
    }
}

