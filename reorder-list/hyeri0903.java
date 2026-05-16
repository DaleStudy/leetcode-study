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
    public void reorderList(ListNode head) {
        /**
        1.Reorder linekd list from 0, n, 1, n-1, ...
        2.solution:
        - 중간을 반으로 쪼개고,앞/뒤 리스트를 번갈아가면서 연결
        - step 1) 중간 노드 찾기
        - step 2) 뒤 리스트 reverse
        - step 3) 두 리스트 merge
        time: O(n), space: O(1)
         */

         ListNode slow = head;
         ListNode fast = head;

         while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
         }

         ListNode second = slow.next;
         slow.next = null;

         ListNode prev = null;
        ListNode curr =  second;

        //reverse second linked list
         while(curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
         }

        //merge two linked list
        ListNode first = head;
        LintNode secondHalf = prev;

        while(secondHalf != null) {
            ListNode next1 = first.next;
            ListNode next2 = secondHalf.next;

            next1.next = secondHalf
            secondHalf.next = next1;

            first = next1;
            secondHalf = next2;
        }
        
    }
}
