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
// 시간복잡도: O(N)
// 공간복잡도: O(1)
class Solution {
    public ListNode reverseList(ListNode head) {

        ListNode prev = null;

        while (head != null){
            ListNode curr = new ListNode(head.val, prev);
            prev = curr;
            head = head.next;
        }

        return prev;
    }
}
