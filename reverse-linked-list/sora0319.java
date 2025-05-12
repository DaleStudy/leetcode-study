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
        if(head == null) return null;

        ListNode backward = null;
        ListNode forward = head;

        while(forward != null){
            forward = head.next;
            head.next = backward;
            backward = head;
            if(forward != null) head = forward;
        }

        return head;
    }
}

