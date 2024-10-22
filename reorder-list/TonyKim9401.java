// TC: O(n)
// -> find middle, reverse, merge -> max O(n)
// SC: O(1)
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode backSide = null;
        ListNode curr = slow.next;
        slow.next = null;

        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = backSide;
            backSide = curr;
            curr = temp;
        }

        ListNode first = head;
        ListNode second = backSide;
        while (second != null) {
            ListNode temp = first.next;
            first.next = second;
            first = second;
            second = temp;
        }
    }
}
