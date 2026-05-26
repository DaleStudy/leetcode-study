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
        /**
        1.linked list 에서 뒤에서 n번째 node remove
        2.constraints:
        node 개수(sz) min=1, max=30
        n값  min = 1, max= sz
        3.solutions: two pointers
        - fast, slow pointer 2개의 간격 = n
        - fast 가 끝지점에 도달하면 그때 slow.next 를 제거
        time: O(n), space: O(1)
         */

         ListNode dummy = new ListNode(0);
         dummy.next = head;

         ListNode fast = dummy;
         ListNode slow = dummy;

         //fast pointer n+1칸 이동, fast - slow = n
         for(int i = 0; i <= n; i++) {
            fast = fast.next; 
         }

         while(fast != null) {
            fast = fast.next;
            slow = slow.next;
         }

         //slow pointer 의 다음 노드(slow.next) 제거
         slow.next = slow.next.next;

         return dummy.next;
        
    }
}
