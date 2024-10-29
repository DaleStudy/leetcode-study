// TC: O(n)
// Visit all elements in the worst case
// SC: O(1)
// Keep using ready assigned variables only
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode output = new ListNode(0, head);
        ListNode dummy = output;

        for (int i = 0; i < n; i++) head = head.next;

        while (head != null) {
            head = head.next;
            dummy = dummy.next;
        }

        dummy.next = dummy.next.next;

        return output.next;
    }
}
