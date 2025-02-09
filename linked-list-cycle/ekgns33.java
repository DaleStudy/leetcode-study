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

/*
* input : singly linked list and head node
* output : return true if list has cycle
*
* solution : tortoise and hare algorithm
*   with two pointer (slow and fast)
* tc : O(n)
* sc : O(1)
*
* */
public class Solution {
  public boolean hasCycle(ListNode head) {
    if(head == null) return false;
    ListNode slow = head;
    ListNode fast = head;
    while(fast.next != null && fast.next.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      if(fast == slow) return true;
    }
    return false;
  }
}
