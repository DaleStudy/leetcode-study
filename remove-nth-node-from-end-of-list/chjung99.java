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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = getSizeOfListNode(head);

        if (size - n - 1 >= 0) {
            ListNode prev = moveNth(head, size - n - 1);
            ListNode target = moveNth(head, size - n);
            prev.next = target.next;
        } else {
            head = head.next;
        }


        return head;
    }
    public ListNode moveNth(ListNode head, int n){
        while (head != null){
            if (n == 0) break;
            head = head.next;
            n--;
        }
        return head;
    }
    public void removeNth(ListNode head, int n){
        int cnt = n;

    }
    public int getSizeOfListNode(ListNode head){
        int size = 0;
        while (head != null) {
            size ++;
            head = head.next;
        }
        return size;
    }
}


