/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  ListNode? reverseList(ListNode? head) {
    var u = null; // S(n) = O(1)
    while (head != null) { // T(n) = O(n)
        final temp = head.next;
        head.next = u;
        u = head;
        head = temp;
    }
    return u;
  }
}
