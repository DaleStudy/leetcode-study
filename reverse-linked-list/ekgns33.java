/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 *
 *
 * input : head of linked list
 * output : reversed linked list
 *
 * solution1)
 * set fast pointer and slow pointer
 * iterate through the linked list
 *  set fast pointer's next to slow pointer
 *
 * tc : O(n)
 * sc : O(1)
 */
class Solution {
  public ListNode reverseList(ListNode head) {
    if(head == null) return head;
    ListNode curr = head;
    ListNode prev = null;
    while(curr.next != null) {
      ListNode next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    curr.next = prev;
    return curr;
  }
}
