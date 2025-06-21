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

        // length 1인 경우를 위해 temp 생성
        ListNode temp = new ListNode(0);
        temp.next = head;

        // 투 포인터 선언
        ListNode fast = temp;
        ListNode slow = temp;

        // n + 1칸만큼 fast 먼저 이동
        for (int i = 0; i < n + 1; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            // 끊어지는 노드 바로 앞까지 이동
            slow = slow.next;
        }

        // slow.next = 끊어져서 치환해야 하는 위치
        slow.next = slow.next.next;

        return temp.next;
    }
}

