/**
 * <a href="https://leetcode.com/problems/linked-list-cycle/">week9-1. linked-list-cycle</a>
 * <li>Description: Return true if there is a cycle in the linked list. </li>
 * <li>Topics: Hash Table, Linked List, Two Pointers</li>
 * <li>Time Complexity: O(N), Runtime 0ms   </li>
 * <li>Space Complexity: O(1), Memory 44.37MB</li>
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }

        return true;
    }
}
