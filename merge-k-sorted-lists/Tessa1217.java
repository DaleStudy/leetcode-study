import java.util.PriorityQueue;

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

    // 우선순위 큐를 활용
    // 시간복잡도: O(N log k)
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }

        // 우선순위 큐 생성
        PriorityQueue<ListNode> pqueue = new PriorityQueue<>(
                (a, b) -> Integer.compare(a.val, b.val)
        );

        // 첫번째 노드를 우선순위 큐에 삽입
        for (ListNode node : lists) {
            if (node != null) {
                pqueue.offer(node);
            }
        }

        ListNode temp = new ListNode(-1);
        ListNode current = temp;

        // 꺼낸 노드의 다음노드가 있으면 큐에 넣는 것을 반복
        while (!pqueue.isEmpty()) {
            ListNode node = pqueue.poll();
            current.next = node;
            current = current.next;

            if (node.next != null) {
                pqueue.offer(node.next);
            }
        }

        return temp.next;
    }

    // 시간복잡도: O(N log K)
    // public ListNode mergeKLists(ListNode[] lists) {
    //     if (lists == null || lists.length == 0) {
    //         return null;
    //     }

    //     return mergeKLists(lists, 0, lists.length - 1);

    // }

    // 단계마다 left, right로 나누어 리스트 병합
    // private ListNode mergeKLists(ListNode[] lists, int start, int end) {

    //     if (start == end) {
    //         return lists[start];
    //     }

    //     int mid = start + (end - start) / 2;

    //     ListNode left = mergeKLists(lists, start, mid);
    //     ListNode right = mergeKLists(lists, mid + 1, end);

    //     return mergeLists(left, right);
    // }

    // 두 개의 노드에 대해 노드의 값 비교하여 ListNode에 연결하여 하나로 병합
    // private ListNode mergeLists(ListNode node1, ListNode node2) {
    //     ListNode temp = new ListNode(-1);
    //     ListNode current = temp;

    //     while (node1 != null && node2 != null) {
    //         if (node1.val < node2.val) {
    //             current.next = node1;
    //             node1 = node1.next;
    //         } else {
    //             current.next = node2;
    //             node2 = node2.next;
    //         }
    //         current = current.next;
    //     }

    //     if (node1 != null) current.next = node1;
    //     if (node2 != null) current.next = node2;

    //     return temp.next;
    // }

}