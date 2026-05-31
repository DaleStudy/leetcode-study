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
    public void reorderList(ListNode head) {
        Map<Integer, ListNode> order = new HashMap<>();
        ListNode start = head;
        int n = 0;

        while (start != null) {
            order.put(n, start);
            start = start.next;
            n++;
        }

        ListNode cur = head;
        List<Integer> newOrder = generateOrder(n);

        for (int i = 0; i < n; i++) {
            int idx = newOrder.get(i);
            cur = order.get(idx);
            if (i + 1 < n) {
                cur.next = order.get(newOrder.get(i+1));
            } else {
                cur.next = null;
            }
            cur = cur.next;
        }
    }
    public List<Integer> generateOrder(int n) {
        List<Integer> reorder = new ArrayList<>();
        int[] asc = new int[n];
        int[] desc = new int[n];

        for (int i = 0; i < n; i++) {
            asc[i] = i;
            desc[i] = n - 1 - i;
        }

        for (int i = 0; i< n; i++) {
            if (i % 2 == 0) {
                reorder.add(asc[i/2]);
            } else {
                reorder.add(desc[i/2]);
            }
        }
        return reorder;
    }
}

