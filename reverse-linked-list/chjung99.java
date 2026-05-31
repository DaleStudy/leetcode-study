/**
 * time: O(n)
 * space: O(1)
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
    ListNode tail;
    public ListNode reverseList(ListNode head) {
        reverseNode(head);
        return tail;
    }

    public void reverseNode(ListNode node){
        if (node == null) return;
        if (node.next == null) {
            tail = node;
            return;
        }

        ListNode nextNode = node.next;
        node.next = null;

        reverseNode(nextNode);

        nextNode.next = node;

    }
}

