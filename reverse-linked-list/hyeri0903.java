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
    public ListNode reverseList(ListNode head) {
        if(head == null) {
            return null;
        }

        Deque<Integer> stack = new ArrayDeque<>();
        ListNode node = head;

        while(node != null) {
            stack.push(node.val);
            node = node.next;
        }

        ListNode dummy = new ListNode();
        ListNode cur = dummy;

        while(stack.size() > 0) {
            int val = stack.pop();
            cur.next = new ListNode(val);
            cur = cur.next;
        }   

        return dummy.next;
    }
}
