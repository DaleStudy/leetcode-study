/**
 * <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">week12-2. remove-nth-node-from-end-of-list</a>
 * <li>Description: Given the head of a linked list, remove the nth node from the end of the list and return its head</li>
 * <li>Topics: Linked List, Two Pointers        </li>
 * <li>Time Complexity: O(N), Runtime 0ms       </li>
 * <li>Space Complexity: O(1), Memory 41.95MB   </li>
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;

        for(int i=0; i<=n; i++){
            fast = fast.next;
        }

        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}
