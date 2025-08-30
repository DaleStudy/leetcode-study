/*
Time Complexity : O(m + n)
Space Complexity : O(1) 
*/
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode tempNode = new ListNode(0);
        ListNode current = tempNode;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        current.next = (list1 != null) ? list1 : list2;
        return tempNode.next;
        // if (list1 == null) {
        //     return list2;
        // }
        // if (list2 == null) {
        //     return list1;
        // }
        // if (list1.val < list2.val) {
        //     list1.next = mergeTwoLists(list1.next, list2);
        //     return list1;
        // } else {
        //     list2.next = mergeTwoLists(list1, list2.next);
        //     return list2;
        // }
    }
}
