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

// 시간 복잡도: O(N)
// 공간복잡도: O(N)
class Solution {
  public ListNode reverseList(ListNode head) {
    if(head==null) return head;

    ListNode pointer = new ListNode(head.val);

    ListNode tempPointer;
    while(head.next!=null){
      tempPointer = new ListNode(head.next.val, pointer);
      pointer = tempPointer;
      head = head.next;
    }
  }
    return pointer;
}

