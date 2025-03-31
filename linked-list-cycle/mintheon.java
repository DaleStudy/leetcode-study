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
//시간복잡도: O(n)
//공간복잡도: O(1)
public class Solution {
  public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while(fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if(slow == fast) return true;
    }

    return false;
  }
}
