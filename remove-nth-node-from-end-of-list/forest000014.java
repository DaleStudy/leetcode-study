/*
# Time Complexity: O(n)
# Space Complexity: O(1)
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        int cnt = 0;
        while (curr != null) {
            cnt++;
            curr = curr.next;
        }

        if (cnt == n) { // 예외 처리
            return head.next;
        }

        ListNode prev = null;
        curr = head;
        for (int i = 0; i < cnt - n; i++, prev = curr, curr = curr.next);
        prev.next = curr.next; // 뒤에서 n번째 노드 제거

        return head;
    }
}
