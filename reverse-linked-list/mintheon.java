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
// 실행시간: O(n)
// 공간복잡도: O(1)
class Solution {
  public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode cur = head;

    while(cur != null) {
      ListNode nextTemp = cur.next;
      cur.next = prev;
      prev = cur;
      cur = nextTemp;
    }

    return prev;
  }
}
