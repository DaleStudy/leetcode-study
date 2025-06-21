public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        Queue<ListNode> queue = new LinkedList<>();
        ListNode temp = new ListNode(0, head);
        ListNode node = temp;

        for (int i = 0; i < n + 1; i++) {
            queue.offer(node);
            node = node.next;
        }

        while (node != null) {
            queue.poll();
            queue.offer(node);
            node = node.next;
        }

        ListNode prev = queue.poll();
        prev.next = prev.next.next;

        return temp.next;
    }
}

