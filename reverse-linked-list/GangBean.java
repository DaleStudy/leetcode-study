/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    /**
    1. strategy
    - iterate over all Node, save value to list
    - iterate list in reverse order, create Node and link
    2. complexity
    - time: O(N)
    - space: O(N)
     */
    public ListNode reverseList(ListNode head) {
        List<Integer> list = new ArrayList<>();

        while (head != null) {
            list.add(head.val);
            head = head.next;
        }

        ListNode prev = new ListNode();
        ListNode ret = null;

        for (int i=list.size()-1; i>=0; i--) {
            ListNode node = new ListNode(list.get(i));
            prev.next = node;
            prev = prev.next;
            if (ret == null) {
                ret = prev;
            }
        }
        return ret;
    }
}

