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
        ListNode head = initNode(list1, list2);
        ListNode ptr = head;

        while (true){
            if (list1 != null && list2 != null) {
                if (list1.val < list2.val) {
                    ptr.val = list1.val;
                    list1 = list1.next;
                } else {
                    ptr.val = list2.val;
                    list2 = list2.next;
                }
            }
            else if (list1 == null && list2 != null) {
                ptr.val = list2.val;
                list2 = list2.next;
            }
            else if (list1 != null && list2 == null) {
                ptr.val = list1.val;
                list1 = list1.next;
            }
            if (list1 == null && list2 == null) break;
            ptr.next = new ListNode();
            ptr = ptr.next;
        }
        return head;
    }

    public ListNode initNode(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) return null;
        return new ListNode();
    }
}

