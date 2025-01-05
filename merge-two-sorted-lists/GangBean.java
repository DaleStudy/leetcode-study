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
        /**
        1. understanding
        - merge 2 sorted linked list
        2. strategy
        - assign return ListNode
        - for each node, started in head, compare each node's value, and add smaller value node to return node, and move the node's head to head.next
        3. complexity
        - time: O(N + M), N is the length of list1, M is the length of list2
        - space: O(1), exclude the return variable 
        */
        ListNode curr = null;
        ListNode ret = null;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                ListNode node = new ListNode(list1.val);
                if (ret == null) {
                    ret = node;
                } else {
                    curr.next = node;
                }
                list1 = list1.next;
                curr = node;
            } else {
                ListNode node = new ListNode(list2.val);
                if (ret == null) {
                    ret = node;
                } else {
                    curr.next = node;
                }
                list2 = list2.next;
                curr = node;
            }
        }

        while (list1 != null) {
            ListNode node = new ListNode(list1.val);
            if (ret == null) {
                ret = node;
            } else {
                curr.next = node;
            }
            list1 = list1.next;
            curr = node;
        }

        while (list2 != null) {
            ListNode node = new ListNode(list2.val);
            if (ret == null) {
                ret = node;
            } else {
                curr.next = node;
            }
            list2 = list2.next;
            curr = node;
        }

        return ret;
    }
}

