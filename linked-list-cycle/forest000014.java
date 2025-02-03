/**
 # Time Complexity : O(n)
 # Space Complexity: O(1)

 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    private final int VISITED = -999999;
    public boolean hasCycle(ListNode head) {
        while (head != null) {
            if (head.val == VISITED) {
                return true;
            }

            head.val = VISITED;
            head = head.next;
        }

        return false;
    }
}
