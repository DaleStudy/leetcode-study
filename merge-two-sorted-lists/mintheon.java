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
class Solution {
  /**
   시간복잡도: O(N)
   공간복잡도: O(1)
   */
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode answer = new ListNode(-1);
    ListNode node = answer;

    while(list1 != null && list2 != null) {
      if(list1.val < list2.val) {
        node.next = list1;
        list1 = list1.next;
      } else {
        node.next = list2;
        list2 = list2.next;
      }

      node = node.next;
    }

    node.next = list1 != null ? list1 : list2;

    return answer.next;
  }
}
