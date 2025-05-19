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
/**
 * 링크드 리스트 head가 주어질 때 뒤집은 리스트를 반환하세요.
 */
class Solution {
    public ListNode reverseList(ListNode head) {

        if (head == null) {
            return head;
        }

        ListNode prev = head;
        ListNode next = prev.next;
        head.next = null;

        while (next != null) {
            ListNode temp = next.next;
            next.next = prev;
            prev = next;
            next = temp;
        }

        return prev;
    }

}

