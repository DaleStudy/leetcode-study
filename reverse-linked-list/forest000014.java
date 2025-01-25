/*
Time Complexity: O(n)
Space Complexity: O(1)

head에서부터 하나씩 next를 탐색하면서, 연결을 반대로 맺어준다.
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
    public ListNode reverseList(ListNode head) {
         if (head == null) {
             return null;
         }

         ListNode curr = head;
         ListNode next = head.next;

         head.next = null; // 마지막 노드가 될 노드의 next는 null로 세팅
         while (next != null) {
             ListNode nnext = next.next; // 연결을 끊기 전에, 그 다음 노드를 미리 nnext로 참조해둔다.
             next.next = curr; // 연결을 반대로 맺어준다.
             curr = next;
             next = nnext;
         }

         return curr;
    }
}
