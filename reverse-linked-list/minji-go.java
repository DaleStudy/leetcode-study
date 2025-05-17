/**
 * <a href="https://leetcode.com/problems/reverse-linked-list/">week07-1.reverse-linked-list</a>
 * <li>Description: return the reversed list    </li>
 * <li>Topics: Linked List, Recursion           </li>
 * <li>Time Complexity: O(N), Runtime 0ms       </li>
 * <li>Space Complexity: O(1), Memory 43.04MB   </li>
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
}
