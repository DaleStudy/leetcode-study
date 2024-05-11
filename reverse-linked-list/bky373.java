/**
 * https://leetcode.com/problems/reverse-linked-list/
 * TC: O(N)
 * SC: O(N)
 */
class Solution_206 {

    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode a = new ListNode(head.val);
        ListNode b;
        while (head.next != null) {
            b = new ListNode(head.next.val, a);
            a = b;
            head = head.next;
        }
        return a;
    }
}
