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
/**
 input : two sorted integer linked list
 output : merged single linked list with sorted order
 constraints:
 1) both linked list can be empty?
 yes
 2) both given lists are sorted?
 yes
 edge :
 1) if both list are empty return null
 2) if one of input lists is empty return the other one

 solution 1)
 using two pointer

 compare the current pointer's value.
 get the smaller one, set to the next node

 until both pointer reach the end

 tc : O(n) sc : O(1)
 */
class Solution {
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode dummy = new ListNode();
    ListNode p1 = list1;
    ListNode p2 = list2;
    ListNode currNode = dummy;
    while(p1 != null && p2 != null) {
      if(p1.val < p2.val){
        currNode.next = p1;
        p1 = p1.next;
      } else {
        currNode.next = p2;
        p2 = p2.next;
      }
      currNode = currNode.next;
    }

    if(p1 == null) {
      currNode.next = p2;
    } else {
      currNode.next = p1;
    }

    return dummy.next;
  }
}
