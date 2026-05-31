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
    public ListNode mergeKLists(ListNode[] lists) {
        /**
        1.문제: ascending liknked list 를 모두 sorted list 로 머지해라.
        2.조건
        - k = list 길이, 최소 = 0, 최대 = 10^4
        - 원소값 0 이상, 500 이하
        3.풀이
        - priority queue(min-heap): time = O(n log k), space = O(k)
        - 각 list 를 min heap 에 넣고 하나씩 뽑아서 새 리스트에 연결.
        - Heap 에 들어가고 나올때마다 O(log k), 총 노드 수 N = O(N logk)
        - Heap 사용 -> space = k
         */

        if(lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> pq = new PriorityQueue<>(lists.length, (a, b) -> a.val - b.val);

        //all list의 첫 노드 넣기
        for(ListNode node: lists) {
            if (node != null) {
                pq.offer(node);
            }
        }

        //결과 리스트를 위한 더미 노드
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while(!pq.isEmpty()) {
            ListNode node = pq.poll(); //최소값 pop
            curr.next = node;   //결과 리스트에 연결
            curr = curr.next;   //포인터 이동
            //다음 노드를 heap에 insert
            if(node.next != null) {
                pq.offer(node.next);
            }
        }
        return dummy.next;
    }
}
