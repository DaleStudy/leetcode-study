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
    // 시간복잡도: O(n), 공간복잡도: O(1)
    public void reorderList(ListNode head) {

        // Slow, Fast Pointer
        // 1 - 2 - 3 - 4 - 5
        ListNode slow = head;
        ListNode fast = head;

        // fast가 끝까지 닿을 때 중점 찾기
        // slow = 3
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }


        // 중간 이후부터 끝까지 (second half of list) => reverse order
        // 3 이후부터 -> 4 - 5
        // reverse - 5 - 4
        ListNode backHead = null; // second half of list's new head
        ListNode backSide = slow.next;
        slow.next = null;

        while (backSide != null) {
            ListNode temp = backSide.next;
            backSide.next = backHead;
            backHead = backSide;
            backSide = temp;
        }

        // Merge first and second half

        // 1 - 2 - 3    
        ListNode firstHalf = head;
        // 5 - 4
        ListNode secondHalf = backHead;

        // 1 - 5 - 2 - 4 - 3
        while (secondHalf != null) {
            ListNode temp = firstHalf.next;
            firstHalf.next = secondHalf;
            firstHalf = secondHalf;
            secondHalf = temp;
        }
    }
}


