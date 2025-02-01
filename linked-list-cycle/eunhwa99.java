
class ListNode {

  int val;
  ListNode next;

  ListNode(int x) {
    val = x;
    next = null;
  }
}

public class Solution {

  // Floyd's Tortoise and Hare Algorithm
  // TC: O(N)
  // SC: O(1)
  public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
      return false;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if (slow == fast) {
        return true;
      }
    }
    return false;
  }
}
