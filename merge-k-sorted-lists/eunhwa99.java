import java.util.PriorityQueue;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode next; ListNode() {}
 * ListNode(int val) { this.val = val; } ListNode(int val, ListNode next) { this.val = val;
 * this.next = next; } }
 */

// TC : PQ -> O(NlogN)
  // SC: Linked list -> O(N)
class Solution {

  public ListNode mergeKLists(ListNode[] lists) {
    if (lists == null || lists.length == 0) {
      return null;
    }
    PriorityQueue<Integer> pq = new PriorityQueue<>();

    for (int i = 0; i < lists.length; i++) {
      while (lists[i] != null) {
        pq.add(lists[i].val);
        lists[i] = lists[i].next;
      }
    }
    ListNode dummy = new ListNode(0);
    ListNode current = dummy;
    while (!pq.isEmpty()) {
      current.next = new ListNode(pq.poll());
      current = current.next;
    }

    return dummy.next;
  }
}

