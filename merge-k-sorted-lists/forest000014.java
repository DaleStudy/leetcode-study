/*
# Time Complexity: O(nlogk)
  - n은 lists[i].length의 합
# Space Complexity: O(k)
  - pq에는 최대 k개의 원소가 저장됨
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

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;

        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode n1, ListNode n2) {
                return n1.val - n2.val;
            }
        });
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] == null) continue;
            pq.offer(lists[i]);
        }

        ListNode head = next(pq);
        ListNode curr = head;

        while (!pq.isEmpty()) {
            curr.next = next(pq);
            curr = curr.next;
        }

        return head;
    }

    private ListNode next(PriorityQueue<ListNode> pq) {
        ListNode top = pq.poll();
        if (top == null) return null;
        if (top.next != null) pq.offer(top.next);
        return top;
    }
}
