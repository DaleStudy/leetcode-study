/**
 * 시간복잡도: O(n)
 * -> 노드가 존재하지 않을때 까지 반복,,
 * 공간복잡도: O(1)
 * -> ListNode
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode node1 = head;
        ListNode node2 = node1.next;
        head.next = null;

        while (node1 != null && node2 != null) {
            ListNode t = node2.next;
            node2.next = node1;
            node1 = node2;
            node2 = t;
        }

        return node1;
    }
}
