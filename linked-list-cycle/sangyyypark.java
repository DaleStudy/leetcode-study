/**
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
    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet();
        ListNode current = head;
        set.add(current);
        while(current != null) {
            if(set.contains(current.next)) {
                return true;
            }
            current = current.next;
            set.add(current);
        }
        return false;

    }
}

