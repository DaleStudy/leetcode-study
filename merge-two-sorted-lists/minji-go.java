/*
    Problem: https://leetcode.com/problems/merge-two-sorted-lists/
    Description: return the head of the merged linked list of two sorted linked lists
    Concept: Linked List, Recursion
    Time Complexity: O(N+M), Runtime 0ms
    Space Complexity: O(1), Memory 42.74MB
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

        ListNode head = new ListNode(0);
        ListNode tail = head;

        while(list1 != null || list2 != null) {
            if (list2 == null || (list1 != null && list1.val <= list2.val)) {
                tail = tail.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                tail = tail.next = new ListNode(list2.val);
                list2 = list2.next;
            }
        }
        return head.next;
    }
}
