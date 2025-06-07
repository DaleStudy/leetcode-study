public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.val));

        for (ListNode list : lists) {
            if (list != null) {
                pq.offer(list);
            }
        }

        ListNode temp = new ListNode(-1);
        ListNode head = temp;

        while (!pq.isEmpty()) {
            ListNode minNode = pq.poll();
            head.next = minNode;
            head = head.next;

            if (minNode.next != null) {
                pq.offer(minNode.next);
            }
        }

        return temp.next;
    }
}
