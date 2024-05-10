/**
 * - 문제: https://leetcode.com/problems/linked-list-cycle/
 * - TC: O(N)
 * - SC: O(1)
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        int min = -10001;

        while (head.next != null) {
            if (head.next.val == min) {
                return true;
            }
            head.val = min;
            head = head.next;
        }
        return false;
    }
}
