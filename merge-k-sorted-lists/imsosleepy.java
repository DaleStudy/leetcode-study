// 우선순위 큐로 다 합쳐버린 다음에
// 큐를 순회돌면서 연결리스트를 재생성한다. 성능은 비교적 낮게 잡힘
// 분할 정복법으로 풀면 더 좋은 성능이 나온다고 한다.
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }

        ListNode newLists = new ListNode(-1);
        ListNode curr = newLists;

        while (!pq.isEmpty()) {
            ListNode minNode = pq.poll();
            curr.next = minNode;
            curr = curr.next;

            if (minNode.next != null) {
                pq.offer(minNode.next);
            }
        }

        return newLists.next;
    }
}
